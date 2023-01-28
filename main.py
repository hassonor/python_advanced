import examples.ecommerce_oo_example.products

# Absolute.

product_1 = examples.ecommerce_oo_example.products.Product("fore")

# or

from examples.ecommerce_oo_example.products import Product

product_2 = Product("main")

# or

from examples.ecommerce_oo_example import products

product_3 = products.Product("mizzen")

test_1 = """
>>> import ecommerce.products
>>> product_1 = ecommerce.products.Product("fore")
>>> product_1.name
'fore'
"""

test_2 = """
>>> from ecommerce.products import Product
>>> product_2 = Product("main")
>>> product_2.name
'main'
"""

test_3 = """
>>> from ecommerce import products
>>> product_3 = products.Product("mizzen")
>>> product_3.name
'mizzen'
"""

disabled_test_path = """
Change the name to test_path for a test that (a) fails
and (b) exposes the `PYTHONPATH` setting in force for the
test.

>>> import sys
>>> sys.path
[]

"""

__test__ = {name: case for name, case in globals().items() if name.startswith("test_")}
