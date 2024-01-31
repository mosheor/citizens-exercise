from loaders.base import BaseConfigLoader
from models import Config, Role


class PermissionHandler:
    def __init__(self, loader: BaseConfigLoader):
        self.loader = loader
        self.config: Config | None = None
        self.permissions: dict[str, set] = {}  # {citizen: {allowed_places}}

    def load_dataset(self, path: str):
        self.config = self.loader.load_config(path=path)
        self.permissions = {}

        for citizen_name, citizen in self.config.citizens.items():
            allowed_places = set(citizen.allowed_places)
            for role in citizen.roles:
                allowed_places.update(self._get_allowed_places(role=self.config.roles[role]))
            self.permissions[citizen_name] = allowed_places

    def _get_allowed_places(self, role: Role, seen_roles: list[str] = None) -> set:
        seen_roles = seen_roles or set()
        allowed_places = set(role.allowed_places)
        seen_roles.add(role.title)
        for role_title in role.sub_roles or []:
            if role_title not in seen_roles:
                allowed_places.update(self._get_allowed_places(self.config.roles[role_title], seen_roles))
        return allowed_places

    def can_visit(self, citizen: str, place: str) -> bool:
        assert self.config, "Dataset is not loaded"
        return place in self.permissions.get(citizen, {})
