# Data filtering limitations

When you grant Lake Formation permissions on a Data Catalog table, you can include data filtering
specifications to restrict access to certain data in query results and engines integrated with
Lake Formation. Lake Formation uses data filtering to achieve column-level security, row-level security, and
cell-level security. You can define and apply data filters on nested columns if your
source data contains nested structures.

## Notes and restrictions for column-level

filtering

There are three ways to specify column filtering:

- By using data filters
- By using simple column filtering or nested column filtering.
- By using TAGs.

Simple column filtering just specifies a list of columns to include or exclude. Both the
Lake Formation console, the API, and the AWS CLI support simple column filtering. For an example, see
[Grant with Simple Column Filtering](granting-table-permissions.md#simple-column-filter-example "granting-table-permissions.md#simple-column-filter-example").

The following notes and restrictions apply to column filtering:

- AWS Glue 5.0 or higher supports fine-grained access control via Lake Formation only for
  Apache Hive and Apache Iceberg tables.
- To grant `SELECT` with the grant option and column filtering, you must use
  an include list, not an exclude list. Without the grant option, you can use either include
  or exclude lists.
- To grant `SELECT` on a table with column filtering, you must have been
  granted `SELECT` on the table with the grant option and without any row
  restrictions. You must have access to all rows.
- If you grant `SELECT` with the grant option and column filtering to a
  principal in your account, that principal must specify column filtering for the same
  columns or a subset of the granted columns when granting to another principal. If you
  grant `SELECT` with the grant option and column filtering to an external
  account, the data lake administrator in the external account can grant `SELECT`
  on all columns to another principal in their account. However, even with
  `SELECT` on all columns, that principal will have visibility only on the
  columns granted to the external account.
- You can't apply column filtering on partition keys.
- A principal with the `SELECT` permission on a subset of columns in a table
  can't be granted the `ALTER`, `DROP`, `DELETE`, or
  `INSERT` permission on that table. For a principal with the
  `ALTER`, `DROP`, `DELETE`, or `INSERT`
  permission on a table, if you grant the `SELECT` permission with column
  filtering, it has no effect.

The following notes and restrictions apply to nested column filtering:

- You can include or exclude five-levels of nested fields in a data filter.

Col1.Col1_1.Col1_1_1.Col1_1_1_1.Col1_1_1_1_1

- You can't apply column filtering on nested fields within partition columns.
- If your table schema contains a top-level column name ("customer"."address") that has
  the same pattern of a nested field representation within a data filter (a nested column
  with a top level column name `customer` and a nested field name
  `address` is specified as `"customer"."address"` in a data
  filter), you can't explicitly specify access to either top level column or nested field
  because both are represented using the same pattern in the inclusion/exclusion lists. This
  is ambiguous, and Lake Formation can't resolve if you're specifying the top level column or the
  nested field.
- If a top level column or nested field contains a double quote within the name, you
  must include a second double quote when you specify access to a nested field within a data
  cells filter's include and exclude list.

Example nested column name with double quotes – `a.b.double"quote`

Example nested column representation within a data filter – `"a"."b"."double""quote"`

## Cell-level filtering limitations

Keep in mind the following notes and restrictions for row-level and cell-level
filtering.

- Cell-level security is not supported on nested columns, views, and resource links.
- All expressions that are supported on top level columns are also supported on nested
  columns. However, nested fields under partition columns should **NOT** be referenced when defining nested row-level expressions.
- Cell-level security is available in all regions when using Athena engine version 3 or Amazon Redshift Spectrum.
  For other services, cell-level security is only available in the regions mentioned on the [Supported Regions](supported-regions.md "supported-regions.md").
- `SELECT INTO` statements are not supported.
- The `array`, and `map` data types aren't
  supported in row filter expressions. The `struct` data type is supported.
- There is no limit to the number of data filters that can be defined on a table, but there is a limit of 100 data filter for a single principal on a table.
- To apply a data filter with a row filter expression, you must have `SELECT` with the grant option on all table columns.
  This restriction doesn't apply to administrators in external accounts when the grant was
  made to the external account.
- If a principal is a member of a group and both the principal and the group are granted
  permissions on a subset of rows, the principal's effective row permissions are the union
  of the principal's permissions and the group's permissions.
- The following column names are restricted in a table for row-level and cell-level filtering:
  - ctid
  - oid
  - xmin
  - cmin
  - xmax
  - cmax
  - tableoid
  - insertxid
  - deletexid
  - importoid
  - redcatuniqueid

- If you apply the all-rows filter expression on a table concurrently with other
  filter expressions with predicates, the all-rows expression will prevail over all other filter expressions.
- When permissions on a subset of rows are granted to an external AWS account and the
  data lake administrator of the external account grants those permissions to a principal in
  that account, the principal's effective filter predicate is the intersection of the
  account's predicate and any predicate that was directly granted to the principal.

For example, if the account has row permissions with the predicate
`dept='hr'` and the principal was separately granted permission for `country='us'`,
the principal has access only to rows with `dept='hr'` and `country='us'`.

For more information about cell-level filtering, see [Data filtering and cell-level security in Lake Formation](data-filtering.md "data-filtering.md").

For consideration and limitations when querying tables using Amazon Redshift Spectrum with
row-level security policies, see [Considerations and limitations using RLS
policies](../../../redshift/latest/dg/t_rls_usage.md "../../../redshift/latest/dg/t_rls_usage.md") in the Amazon Redshift Database Developer Guide.
