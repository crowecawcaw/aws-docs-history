# Work with views

A view in Amazon Athena is a logical table, not a physical table. The query that defines a
view runs each time the view is referenced in a query. You can create a view from a
`SELECT` query and then reference this view in future queries.

You can use two different kinds of views in Athena: Athena views and AWS Glue Data Catalog
views.

## When to use Athena views?

You may want to create Athena views to:

- Query a subset of data – For example,
  you can create a view with a subset of columns from the original table to
  simplify querying data.
- Combine tables – You can use views to
  combine multiple tables into one query. When you have multiple tables and want
  to combine them with `UNION ALL`, you can create a view with that
  expression to simplify queries against the combined tables.
- Hide complexity – Use views to hide the
  complexity of existing base queries and simplify queries run by users. Base
  queries often include joins between tables, expressions in the column list, and
  other SQL syntax that make it difficult to understand and debug them. You might
  create a view that hides the complexity and simplifies queries.
- Optimize queries – You can use views to
  experiment with optimization techniques to create optimized queries. For
  example, if you find a combination of `WHERE` conditions,
  `JOIN` order, or other expressions that demonstrate the best
  performance, you can create a view with these clauses and expressions.
  Applications can then make relatively simple queries against this view. If you
  later find a better way to optimize the original query, when you recreate the
  view, all the applications immediately take advantage of the optimized base
  query.
- Hide underlying names – You can use
  views to hide underlying table and column names, and minimize maintenance
  problems if the names change. If the names change, you can simply recreate the
  view using the new names. Queries that use the view rather than the tables
  directly keep running with no changes.

For more information, see [Work with Athena views](views-console.md "views-console.md").

## When to use AWS Glue Data Catalog views?

Use AWS Glue Data Catalog views when you want a single common view across AWS services like
Amazon Athena and Amazon Redshift. In Data Catalog views, access permissions are defined by the user who
created the view instead of the user who queries the view. This method of granting
permissions is called _definer_ semantics.

The following use cases show how you can use Data Catalog views.

- Greater access control – You create a
  view that restricts data access based on the level of permissions the user
  requires. For example, you can use Data Catalog views to prevent employees who don't
  work in the human resources (HR) department from seeing personally identifiable
  information.
- Ensure complete records – By applying
  certain filters onto your Data Catalog view, you make sure that the data records in a
  Data Catalog view are always complete.
- Enhanced security – In Data Catalog views,
  the query definition that creates the view must be intact in order for the view
  to be created. This makes Data Catalog views less susceptible to SQL commands from
  malicious actors.
- Prevent access to underlying tables –
  Definer semantics allow users to access a view without making the underlying
  table available to them. Only the user who defines the view requires access to
  the tables.

Data Catalog view definitions are stored in the AWS Glue Data Catalog. This means that you can use
AWS Lake Formation to grant access through resource grants, column grants, or tag-based access
controls. For more information about granting and revoking access in Lake Formation, see [Granting and
revoking permissions on Data Catalog resources](../../../lake-formation/latest/dg/granting-catalog-permissions.md "../../../lake-formation/latest/dg/granting-catalog-permissions.md") in the
_AWS Lake Formation Developer Guide_.

For more information, see [Use Data Catalog views in Athena](views-glue.md "views-glue.md").
