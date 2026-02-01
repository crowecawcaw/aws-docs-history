Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Nested data use cases

This topic describes use cases for nested data. Nested data is
data that contains nested fields. Nested fields are fields that are joined together
as a single entity, such as arrays, structs, or objects.

You can combine the extensions described previously with the usual SQL
features. The following use cases illustrate some common combinations. These examples
help demonstrate how you can use nested data. They aren't part of the
tutorial.

###### Topics

- [Ingesting nested data](#ingesting-nested-data "#ingesting-nested-data")
- [Aggregating nested data with subqueries](#aggregating-with-subquery "#aggregating-with-subquery")
- [Joining Amazon Redshift and nested data](#joining-redshift-data "#joining-redshift-data")

## Ingesting nested data

You can use a `CREATE TABLE AS` statement to ingest data from
an external table that contains complex data types. The following query extracts all
customers and their phone numbers from the external table, using `LEFT
 JOIN`, and stores them in the Amazon Redshift table `CustomerPhones`.

```
CREATE TABLE CustomerPhones AS
SELECT  c.name.given, c.name.family, p AS phone
FROM    spectrum.customers c LEFT JOIN c.phones p ON true;
```

##

Aggregating nested data with subqueries

You can use a subquery to aggregate nested data. The following example
illustrates this approach.

```
SELECT c.name.given, c.name.family, (SELECT COUNT(*) FROM c.orders o) AS ordercount
FROM   spectrum.customers c;
```

The following data is returned.

```
given   |  family  |  ordercount
--------|----------|--------------
 Jenny  |  Doe     |       0
 John   |  Smith   |       2
 Andy   |  Jones   |       1
 (3 rows)
```

###### Note

When you aggregate nested data by grouping by the parent row, the most
efficient way is the one shown in the previous example. In that example, the
nested rows of `c.orders` are grouped by their parent row
`c`. Alternatively, if you know that `id` is unique
for each `customer` and `o.shipdate` is never null, you
can aggregate as shown in the following example. However, this approach
generally isn't as efficient as the previous example.

```
SELECT    c.name.given, c.name.family, COUNT(o.shipdate) AS ordercount
FROM      spectrum.customers c LEFT JOIN c.orders o ON true
GROUP BY  c.id, c.name.given, c.name.family;
```

You can also write the query by using a subquery in the `FROM` clause that
refers to an alias (`c`) of the ancestor query and extracts array data.
The following example demonstrates this approach.

```
SELECT c.name.given, c.name.family, s.count AS ordercount
FROM   spectrum.customers c, (SELECT count(*) AS count FROM c.orders o) s;
```

## Joining Amazon Redshift and nested data

You can also join Amazon Redshift data with nested data in an external table. For
example, suppose that you have the following nested data in Amazon S3.

```
CREATE EXTERNAL TABLE spectrum.customers2 (
  id      int,
  name    struct<given:varchar(20), family:varchar(20)>,
  phones  array<varchar(20)>,
  orders  array<struct<shipdate:timestamp, item:int>>
);
```

Suppose also that you have the following table in Amazon Redshift.

```
CREATE TABLE prices (
  id int,
  price double precision
);
```

The following query finds the total number and amount of each
customer's purchases based on the preceding. The following example is only an
illustration. It only returns data if you have created the tables described
previously.

```
SELECT   c.name.given, c.name.family, COUNT(o.date) AS ordercount, SUM(p.price) AS ordersum
FROM     spectrum.customers2 c, c.orders o, prices p ON o.item = p.id
GROUP BY c.id, c.name.given, c.name.family;
```
