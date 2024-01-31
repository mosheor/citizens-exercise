def test_resolver(resolver):
    assert resolver.can_visit("Aco", "Armory") is False
    assert resolver.can_visit("Aro", "City Wall") is True
    assert resolver.can_visit("Baco", "Storage") is True
