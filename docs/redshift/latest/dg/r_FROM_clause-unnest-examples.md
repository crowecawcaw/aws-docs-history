Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# UNNEST examples

UNNEST is a parameter in the FROM clause that expands
nested data into columns that hold the data’s unnested
elements. For information on unnesting data, see
[Querying semi-structured data](query-super.md "query-super.md").

The following statement creates and populates the `orders` table,
which contains a `products` column containing arrays of product
IDs. The examples in this section use the sample data in this table.

```
CREATE TABLE orders (
    order_id INT,
    products SUPER
);

-- Populate table
INSERT INTO orders VALUES
(1001, JSON_PARSE('[
        {
            "product_id": "P456",
            "name": "Monitor",
            "price": 299.99,
            "quantity": 1,
            "specs": {
                "size": "27 inch",
                "resolution": "4K"
            }
        }
    ]
')),
(1002, JSON_PARSE('
    [
        {
            "product_id": "P567",
            "name": "USB Cable",
            "price": 9.99,
            "quantity": 3
        },
        {
            "product_id": "P678",
            "name": "Headphones",
            "price": 159.99,
            "quantity": 1,
            "specs": {
                "type": "Wireless",
                "battery_life": "20 hours"
            }
        }
    ]
'));
```

Following are some examples of unnesting queries
with the sample data using PartiQL syntax.

## Unnesting an array without an OFFSET column

The following query unnests the SUPER arrays in the products column,
with each row representing an item from the order in `order_id`.

```
SELECT o.order_id, unnested_products.product
FROM orders o, UNNEST(o.products) AS unnested_products(product);

 `order_id | product
----------+-----------------------------------------------------------------------------------------------------------------------------
 1001 | {"product_id":"P456","name":"Monitor","price":299.99,"quantity":1,"specs":{"size":"27 inch","resolution":"4K"}}
 1002 | {"product_id":"P567","name":"USB Cable","price":9.99,"quantity":3}
 1002 | {"product_id":"P678","name":"Headphones","price":159.99,"quantity":1,"specs":{"type":"Wireless","battery_life":"20 hours"}}
(3 rows)`
```

The following query finds the most expensive product in each order.

```
SELECT o.order_id, MAX(unnested_products.product)
FROM orders o, UNNEST(o.products) AS unnested_products(product);

 `order_id | product
----------+-----------------------------------------------------------------------------------------------------------------------------
 1001 | {"product_id":"P456","name":"Monitor","price":299.99,"quantity":1,"specs":{"size":"27 inch","resolution":"4K"}}
 1002 | {"product_id":"P678","name":"Headphones","price":159.99,"quantity":1,"specs":{"type":"Wireless","battery_life":"20 hours"}}
(2 rows)`
```

## Unnesting an array with an implicit OFFSET column

The following query uses the `UNNEST ... WITH OFFSET`
parameter to show the zero-based position of each product
within its order array.

```
SELECT o.order_id, up.product, up.offset_col
FROM orders o, UNNEST(o.products) WITH OFFSET AS up(product);

 `order_id | product | offset_col
----------+-----------------------------------------------------------------------------------------------------------------------------+------------
 1001 | {"product_id":"P456","name":"Monitor","price":299.99,"quantity":1,"specs":{"size":"27 inch","resolution":"4K"}} | 0
 1002 | {"product_id":"P567","name":"USB Cable","price":9.99,"quantity":3} | 0
 1002 | {"product_id":"P678","name":"Headphones","price":159.99,"quantity":1,"specs":{"type":"Wireless","battery_life":"20 hours"}} | 1
(3 rows)`
```

Since the statement doesn’t specify an alias for the offset column, Amazon Redshift defaults to naming it `offset_col`.

## Unnesting an array with an explicit OFFSET column

The following query also uses the `UNNEST ... WITH OFFSET`
parameter to show the products within their order arrays.
The difference in this query compared to the query in
the previous example is that it explicitly names
the offset column with the alias `idx`.

```
SELECT o.order_id, up.product, up.idx
FROM orders o, UNNEST(o.products) WITH OFFSET AS up(product, idx);

 `order_id | product | idx
----------+-----------------------------------------------------------------------------------------------------------------------------+-----
 1001 | {"product_id":"P456","name":"Monitor","price":299.99,"quantity":1,"specs":{"size":"27 inch","resolution":"4K"}} | 0
 1002 | {"product_id":"P567","name":"USB Cable","price":9.99,"quantity":3} | 0
 1002 | {"product_id":"P678","name":"Headphones","price":159.99,"quantity":1,"specs":{"type":"Wireless","battery_life":"20 hours"}} | 1
(3 rows)`
```
