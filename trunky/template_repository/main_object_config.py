from dataclasses import dataclass

@dataclass
class MainObjectConfig:
    # trunkie_object: TrunkieObject = None
    resource_path: str = None

    @staticmethod
    def from_env():
        try:
            # get from environment variables and generic conversion (impement in general utils)
            # resource_path = config.get_string("RESOURCE_PATH")
            resource_path="config"
        except ValueError:
            resource_path = None

        # call other trunkie objects to init them via .env as well
        # return ContextClassifierConfig(TrunkieObject.from_env(), resource_path)
        return MainObjectConfig(resource_path)
