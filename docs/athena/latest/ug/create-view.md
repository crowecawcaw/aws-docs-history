# CREATE VIEW and CREATE PROTECTED MULTI

DIALECT VIEW

A view is a logical table that can be referenced by future queries. Views do not contain
any data and do not write data. Instead, the query specified by the view runs each time you
reference the view by another query.

- `CREATE VIEW` creates an Athena view from a specified
  `SELECT` query. Athena views work within Athena. For more information
  about Athena views, see [Work with views](views.md "views.md").
- `CREATE PROTECTED MULTI DIALECT VIEW` creates a AWS Glue Data Catalog view in the
  AWS Glue Data Catalog. AWS Glue Data Catalog views provide a single common view across AWS services
  like Amazon Athena and Amazon Redshift. For more information about AWS Glue Data Catalog views, see [Use Data Catalog views in Athena](views-glue.md "views-glue.md").

## CREATE VIEW

Creates a view for use within Athena.

### Synopsis

```
CREATE [ OR REPLACE ] VIEW view_name AS query
```

The optional `OR REPLACE` clause lets you update the existing view by
replacing it. For more information, see [Create views](views-console.md#creating-views "views-console.md#creating-views").

### Examples

To create a view `test` from the table `orders`, use a query
similar to the following:

```
CREATE VIEW test AS
SELECT
orderkey,
orderstatus,
totalprice / 2 AS half
FROM orders;
```

To create a view `orders_by_date` from the table `orders`,
use the following query:

```
CREATE VIEW orders_by_date AS
SELECT orderdate, sum(totalprice) AS price
FROM orders
GROUP BY orderdate;
```

To update an existing view, use an example similar to the following:

```
CREATE OR REPLACE VIEW test AS
SELECT orderkey, orderstatus, totalprice / 4 AS quarter
FROM orders;
```

For more information about using Athena views, see [Work with views](views.md "views.md").

## CREATE PROTECTED MULTI

DIALECT VIEW

Creates a AWS Glue Data Catalog view in the AWS Glue Data Catalog. A Data Catalog view is a single view schema
that works across Athena and other SQL engines such as Amazon Redshift and Amazon EMR.

### Syntax

```
CREATE [ OR REPLACE ] PROTECTED MULTI DIALECT VIEW `view_name`
SECURITY DEFINER
[ SHOW VIEW JSON ]
AS `query`
```

**OR REPLACE**

(Optional) Updates the existing view by replacing it. A Data Catalog view
cannot be replaced if SQL dialects from other engines are present in the
view. If the calling engine has the only SQL dialect present in the
view, the view can be replaced.

**PROTECTED**

Required keyword. Specifies that the view is protected against data
leaks. Data Catalog views can only be created as a `PROTECTED`
view.

**MULTI DIALECT**

Specifies that the view supports the SQL dialects of different query
engines and can therefore be read by those engines.

**SECURITY DEFINER**

Specifies that definer semantics are in force for this view. Definer
semantics mean that the effective read permissions on the underlying
tables belong to the principal or role that defined the view rather than
the principal that performs the actual read.

**SHOW VIEW JSON**

(Optional) Returns the JSON for the Data Catalog view specification without
actually creating a view. This "dry-run" option is useful when you want
to validate the SQL for the view and return the table metadata that
AWS Glue will use.

### Example

The following example creates the `orders_by_date` Data Catalog view based
on a query on the `orders` table.

```
CREATE PROTECTED MULTI DIALECT VIEW orders_by_date
SECURITY DEFINER
AS
SELECT orderdate, sum(totalprice) AS price
FROM orders
WHERE order_city = 'SEATTLE'
GROUP BY orderdate
```

For more information about using AWS Glue Data Catalog views, see [Use Data Catalog views in Athena](views-glue.md "views-glue.md").
