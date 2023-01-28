from ..database import Database

test_2 = """
>>> db = Database("path/to/data")
>>> db.fetch("test_2")
{'key': 'test_2'}
"""

__test__ = {name: case for name, case in globals().items() if name.startswith("test_")}
