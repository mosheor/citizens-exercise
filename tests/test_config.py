def test_config(resolver):
    config = resolver.config
    assert config.dict() == {
        "citizens": {
            "Aco": {"name": "Aco", "roles": ["Priest"], "allowed_places": ["Aco Home"]},
            "Aro": {"name": "Aro", "roles": ["High Priest", "Guard"], "allowed_places": []},
            "Baco": {"name": "Baco", "roles": ["Farmer"], "allowed_places": ["City Wall"]},
        },
        "roles": {
            "Priest": {"title": "Priest", "allowed_places": ["Temple"], "sub_roles": []},
            "Guard": {"title": "Guard", "allowed_places": ["Armory", "City Wall"], "sub_roles": []},
            "Carrier": {"title": "Carrier", "allowed_places": [], "sub_roles": ["Organizer"]},
            "High Priest": {
                "title": "High Priest",
                "allowed_places": ["Hidden Room", "City Wall"],
                "sub_roles": ["Priest"],
            },
            "Farmer": {"title": "Farmer", "allowed_places": ["Farm"], "sub_roles": ["Carrier"]},
            "Organizer": {"title": "Organizer", "allowed_places": ["Storage"], "sub_roles": ["Farmer"]},
        },
    }
