# ALTER VIEW DIALECT

Adds or drops an engine dialect from a AWS Glue Data Catalog view. Applies to AWS Glue Data Catalog views
only. Requires `Lake Formation` admin or definer permissions.

For more information about AWS Glue Data Catalog views, see [Use Data Catalog views in Athena](views-glue.md "views-glue.md").

## Syntax

```
ALTER VIEW `name` [ FORCE ] [ ADD|UPDATE ] DIALECT AS query
```

```
ALTER VIEW `name` [ DROP ] DIALECT
```

**FORCE**

The `FORCE` keyword causes conflicting engine dialect
information in a view to be overwritten with the new definition. The
`FORCE` keyword is useful when an update to a Data Catalog view
results in conflicting view definitions across existing engine dialects.
Suppose a Data Catalog view has both the Athena and Amazon Redshift dialects and the update
results in a conflict with Amazon Redshift in the view definition. In this case, you
can use the `FORCE` keyword to allow the update to complete and
mark the Amazon Redshift dialect as stale. When engines marked as stale query the view,
the query fails. The engines throw an exception to disallow stale results.
To correct this, update the stale dialects in the view.

**ADD**

Adds a new engine dialect to the Data Catalog view. The engine specified must
not already exist in the Data Catalog view.

**UPDATE**

Updates an engine dialect that already exists in the Data Catalog view.

**DROP**

Drops an existing engine dialect from a Data Catalog view. After you drop an
engine from a Data Catalog view, the Data Catalog view cannot be queried by the engine
that was dropped. Other engine dialects in the view can still query the
view.

**DIALECT AS**

Introduces an engine-specific SQL query.

## Examples

```
ALTER VIEW orders_by_date FORCE ADD DIALECT
AS
SELECT orderdate, sum(totalprice) AS price
FROM orders
GROUP BY orderdate
```

```
ALTER VIEW orders_by_date FORCE UPDATE DIALECT
AS
SELECT orderdate, sum(totalprice) AS price
FROM orders
GROUP BY orderdate
```

```
ALTER VIEW orders_by_date DROP DIALECT
```
