# Data query–SQL query and table configurations

Data Exports enables you to write SQL queries (column selections, row filtering, column aliasing)
that are executed against the tables provided–CUR 2.0, for example. Each table might also have
table configurations that alter the data contained within the table. For example, with CUR
2.0, you can specify a configuration to choose a time granularity of hourly, daily, or
monthly, or a configuration to add cost and usage data at resource-level granularity.

For an export data query to be fully defined, you must specify the following two
attributes:

- **SQL query:** The SQL statement is executed against a
  table and determines what data is returned by the export.
- **Table configurations:** The table configuration
  settings change what data is contained within the table before the SQL query is executed
  against it.
  In the **Data Exports** console page, you can use the workflow that builds the
  SQL statement and table configurations based on your selections. In the Data Exports SDK/CLI, you can
  write your own SQL statement and table configurations.

Data Exports SQL statements (`QueryStatement`) use the following syntax:

```
SELECT <column_name_a>, <column_name_b>.<attribute_name> AS <new_name>, ...
FROM <TABLE_NAME>
[ WHERE <column_name> OPERATOR <value> AND|OR ... ]
[ LIMIT number ]

```

Data Exports table configurations (`TableConfigurations`) use the following
syntax:

```
{"<TABLE_NAME>":
    {"<CONFIGURATION_NAME_A>": "<value>",
     "<CONFIGURATION_NAME_B>": "<value>",
     ...}
            }
```

## SQL query

The SQL query is executed against a table and determines what data is returned in an
export. The SQL statement can be altered after an export has been created, but the table
selected can't be changed.

SQL statements (in the QueryStatement field) can have a maximum of 36,000
characters.

The possible keywords in a Data Exports SQL query are as follows.

###### Note

The keywords are not case-sensitive. The column names and table names are
case-sensitive.

**SELECT**

Required.

Specifies which columns are to be selected from the table. There can only be one
SELECT statement per query.

Use the dot operator `.` to specify selecting an attribute of a MAP or
STRUCT column as a separate column. The name of the resulting column in the SQL output
is the attribute name by default.

For example, you can select attributes from the product MAP column.

`SELECT product.from_location FROM COST_AND_USAGE_REPORT`

This selects the `from_location` attribute from the
`product` column and creates a new column with the attribute’s data. By
default, in the output, this column’s name will be `from_location`.
However, it can be renamed with `AS`.

For more information on the MAP and STRUCT columns available in each table, and
the attributes these columns have, see the [Data Exports table dictionary](dataexports-table-dictionary.md "dataexports-table-dictionary.md").

**AS**

Optional.

Enables renaming of the column being selected. The new column name can't have
spaces or characters other than alphanumeric characters (a-z, A-Z, and 0-9) and
underscores ( \_ ). You can't use quotes when defining the column alias in order to use
other characters.

Aliasing can be useful when selecting an attribute of a MAP or STRUCT column to
rename the resulting column to match the schema of the CUR. For example, to match how
the CUR shows the `product_from_location` column, write the following query
in Data Exports with the CUR 2.0 table.

`SELECT product.from_location AS product_from_location FROM
 COST_AND_USAGE_REPORT`

This creates an export with a column named
`product_from_location`.

**FROM**

Required.

Specifies the table to be queried. There can only be one FROM statement per
query.

**WHERE**

Optional.

Filters the rows to only those that match your specified clause.

The WHERE clause supports the following operators:

- **=** Value must match the string or
  number.
- **!= and <>** Value must not match the
  specified string or number.
- **<, <=, >,** and **>=** Value must be less than, less than or equal to, greater than, or
  greater than or equal to the number.
- **AND** Both conditions that are specified must
  be true to match. You can use multiple **AND**
  keywords to specify two or more conditions.
- **OR** Either conditions that are specified must
  be true to match. You can use multiple **OR**
  keywords to specify two or more conditions.
- **NOT** The condition specified must not be true
  to match.
- **IN** Any of the values specified within the
  parentheses after the keyword must be true to match.
- Parentheses can be used to construct multi-conditional WHERE clauses

###### Note

When expressing strings as the value following an operator, use single quotes
`'` instead of double quotes. You don't need to escape the single
quotes. For example you can write the following WHERE statement:

`WHERE line_item_type = 'Discount' OR line_item_type =
 'Usage'`

**LIMIT**

Optional.

Limits the number of rows returned by the query to the value that you
specify.

## Table configurations

Table configurations are user-controlled properties that a user can set to change the
data or schema of a table before it's queried in Data Exports. The table configurations are
saved as a JSON statement and are either specified through user input in the AWS SDK/CLI
or user selections in the console.

For example, CUR 2.0 has table configurations to change data granularity (hourly, daily,
monthly), whether resource-level granular data is included, and whether split cost
allocation data is included. Not all tables have configurations. For more information on the
configurations available for each table, see the [Data Exports
table dictionary](dataexports-table-dictionary.md "dataexports-table-dictionary.md").

Each table configuration parameter has a default value that is assumed if a table
configuration is not specified by the user. Table configurations can't be changed after an
export is created.
