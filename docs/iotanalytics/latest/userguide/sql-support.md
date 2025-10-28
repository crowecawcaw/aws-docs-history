End of support notice:
On December 15, 2025, AWS will end support for AWS IoT Analytics. After December 15, 2025, you will no longer
be able to access the AWS IoT Analytics console, or AWS IoT Analytics resources.
For more information, see
[AWS IoT Analytics end of support](iotanalytics-end-of-support.md "iotanalytics-end-of-support.md").

# SQL expressions in AWS IoT Analytics

Datasets are generated using SQL expressions on data in a data store. AWS IoT Analytics uses the same SQL queries, functions and operators as Amazon Athena.

AWS IoT Analytics supports a subset of ANSI standard SQL syntax.

```
SELECT [ ALL | DISTINCT ] select_expression [, ...]
[ FROM from_item [, ...] ]
[[ INNER | OUTER ] LEFT | RIGHT | FULL | CROSS JOIN join_item [ ON join_condition ]]
[ WHERE condition ]
[ GROUP BY [ ALL | DISTINCT ] grouping_element [, ...] ]
[ HAVING condition ]
[ UNION [ ALL | DISTINCT ] union_query ]
[ ORDER BY expression [ ASC | DESC ] [ NULLS FIRST | NULLS LAST] [, ...] ]
[ LIMIT [ count | ALL ] ]
```

For a description of the parameters, see [Parameters](../../../athena/latest/ug/select.md#select-parameters "../../../athena/latest/ug/select.md#select-parameters") in the _Amazon Athena documentation_.

AWS IoT Analytics and Amazon Athena doesn't support the following:

- `WITH` clauses.
- `CREATE TABLE AS SELECT` statements
- `INSERT INTO` statements
- Prepared statements, you can't run `EXECUTE` with `USING`.
- `CREATE TABLE LIKE`
- `DESCRIBE INPUT` and `DESCRIBE OUTPUT`
- `EXPLAIN` statements
- User-defined functions (UDFs or UDAFs)
- Stored procedures
- Federated connectors

###### Topics

- [Supported SQL functionality in AWS IoT Analytics](supported-fuctionality.md "supported-fuctionality.md")
- [Troubleshoot common issues with SQL queries in
  AWS IoT Analytics](troubleshoot-queries.md "troubleshoot-queries.md")
