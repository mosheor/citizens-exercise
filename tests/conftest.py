from pathlib import Path

import pytest

from loaders.json import JsonConfigLoader
from permission_handler import PermissionHandler


@pytest.fixture
def loader():
    return JsonConfigLoader()


@pytest.fixture
def resolver(loader):
    ph = PermissionHandler(loader=loader)
    ph.load_dataset(str(Path(__file__).parent / "test_config.json"))
    return ph
