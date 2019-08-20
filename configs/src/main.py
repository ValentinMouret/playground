import dataclasses

import pyhocon


class Config:
    @classmethod
    def from_config_tree(cls, conf: pyhocon.ConfigTree):
        return cls(**conf.as_plain_ordered_dict())


@dataclasses.dataclass
class ImportantConfig(Config):
    name: str
    destination: dict


def main():
    conf = {"name": "foo", "destination": {"fizz": "buzz"}}
    important_config = ImportantConfig(**conf)
    print(important_config)

    hoconf = pyhocon.ConfigFactory.from_dict(conf)
    important_config = ImportantConfig.from_config_tree(hoconf)
    print(important_config)


if __name__ == "__main__":
    main()
