from permission_handler import PermissionHandler
from loaders.json import JsonConfigLoader

if __name__ == "__main__":
    loader = JsonConfigLoader()
    resolver = PermissionHandler(loader=loader)
    resolver.load_dataset("config.json")

    print(resolver.can_visit("Aco", "Armory"))  # False
    print(resolver.can_visit("Aro", "City Wall"))  # True
    print(resolver.can_visit("Baco", "Storage"))  # True
    print(resolver.can_visit("Baco", "Storage2"))  # False
