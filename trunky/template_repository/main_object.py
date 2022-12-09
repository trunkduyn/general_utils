from trunky.template_repository.main_object_config import MainObjectConfig


class MainObject:

    def __int__(self, config: MainObjectConfig = MainObjectConfig()):
        self.config = config