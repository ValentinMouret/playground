import random

N_SHARDS = 100
LINES_PER_SHARD = 1000


def main():
    for shard_id in range(N_SHARDS):
        with open(f"./data/shard_{shard_id}.csv", "w") as f:
            f.writelines(
                [
                    f"{random.randint(0, 1)};{shard_id};{i}\n"
                    for i in range(LINES_PER_SHARD)
                ]
            )


if __name__ == "__main__":
    main()
