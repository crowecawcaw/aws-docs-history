# Use aliases and comments in queries

Create queries that contain aliases. Use aliases to rename log fields or
when extracting values into fields. Use the keyword `as` to give
a log field or result an alias. You can use more than one alias in a query.
You can use aliases in the following commands:

- `fields`
- `parse`
- `sort`
- `stats`
  The following examples show how to create queries that contain aliases.

**Example**

The query contains an alias in the `fields` command.

```
fields @timestamp, @message, accountId as ID
| sort @timestamp desc
| limit 20
```

The query returns the values for the fields `@timestamp`,
`@message`, and `accountId`. The results are
sorted in descending order and limited to 20. The values for
`accountId` are listed under the alias `ID`.

**Example**

The query contains aliases in the `sort` and
`stats` commands.

```
stats count(*) by duration as time
| sort time desc
```

The query counts the number of times the field `duration`
occurs in the log group and sorts the results in descending order. The
values for `duration` are listed under the alias
`time`.

## Use comments

CloudWatch Logs Insights supports comments in queries. Use the hash character
(**#**) to set off comments. You can use comments
to ignore lines in queries or document queries.

**Example: Query**

When the following query is run, the second line is ignored.

```
fields @timestamp, @message, accountId
# | filter accountId not like "7983124201998"
| sort @timestamp desc
| limit 20
```
