from examples.ecommerce_oo_example.products import Product
import examples.ecommerce_oo_example.products
import examples.ecommerce_oo_example.payments.stripe


def test_products_db_1():
    db = examples.ecommerce_oo_example.products.database.Database("path/to/data")
    assert db.fetch("test_1") == {'key': 'test_1'}


def test_products_db_2():
    db = examples.ecommerce_oo_example.products.Database("path/to/data")
    assert db.fetch("test_2") == {'key': 'test_2'}


def test_products_db_3():
    db = examples.ecommerce_oo_example.products.DB("path/to/data")
    assert db.fetch("test_3") == {'key': 'test_3'}


def test_products_db_4():
    db = examples.ecommerce_oo_example.products.DB("path/to/data")
    q = examples.ecommerce_oo_example.products.Query(db, "products")


def test_products_db_5():
    examples.ecommerce_oo_example.products.database.initialize_database("production/data")
    assert examples.ecommerce_oo_example.products.database.db.connection == 'production/data'


def test_products_db_6():
    db = examples.ecommerce_oo_example.products.database.get_database("production/data")
    assert db.connection == 'production/data'


def test_payments_db():
    assert examples.ecommerce_oo_example.payments.stripe.payment() == {"key": "test_2"}
