import os
import pathlib
import random

import pandas as pd
import tensorflow as tf

DATA_FOLDER = pathlib.Path("/data")


def parse_row(*cols):
    target = cols[0]
    shard_id = cols[1]
    line = cols[2]
    return {"shard_id": shard_id, "line": line}, target


def ds_from_shard(shard: str) -> tf.data.Dataset:
    return tf.data.experimental.CsvDataset(
        shard, record_defaults=[0, 0, 0], header=False, field_delim=";"
    )


def get_dataset(shards: [str], epoch: int, batch_size: int):
    return (
        tf.data.Dataset.from_tensor_slices(shards)
        # .shuffle(len(shards))
        .flat_map(ds_from_shard)
        .map(parse_row)
        .cache("/cache")
        .shuffle(len(shards) * batch_size * 2)
        .batch(batch_size)
        .prefetch(3)
        .repeat(epoch)
    )


def main():
    epochs = 10
    rows_per_file = 1000
    batch_size = 500
    steps_per_file = (rows_per_file // batch_size) + (
        1 if rows_per_file % batch_size != 0 else 0
    )

    shards = [str(DATA_FOLDER / s) for s in os.listdir(DATA_FOLDER)]
    random.shuffle(shards)
    train_shards = shards[:3]

    ds = get_dataset(train_shards, epochs, batch_size)
    print(f"training on: {train_shards}")

    epochs = []
    shard_ids = []

    for step, (X, _) in enumerate(ds):
        epochs.append(step // (steps_per_file * len(train_shards)))
        shard_ids.append(",".join(str(s) for s in set(X["shard_id"].numpy())))

    print(pd.DataFrame({"epochs": epochs, "shard_ids": shard_ids}))


if __name__ == "__main__":
    main()
