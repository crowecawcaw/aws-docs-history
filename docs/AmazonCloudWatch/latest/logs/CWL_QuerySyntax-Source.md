# SOURCE

Including `SOURCE` in a query is a useful way to specify the
log groups and/or data sources to include in a query when you are using the
AWS CLI or API to create a query. The `SOURCE` command is supported
only in the AWS CLI and API, not in the CloudWatch console. When you use the CloudWatch
console to start a query, you use the console interface to specify the log
groups.

Query log groups

To use `SOURCE` to specify the log groups to query, you can use
the following keywords:

- `namePrefix` runs the query against log groups that
  have names that start with the string that you specify. If you omit
  this, all log groups are queried.

You can include as many as five prefixes in the list.

- `accountIdentifier` runs the query against log groups
  in the specified AWS account. This works only when you run the
  query in a monitoring account. If you omit this, the default is to
  query all linked source accounts and the current monitoring account.
  For more information about cross-account observability, see [CloudWatch cross-account observability](../monitoring/CloudWatch-Unified-Cross-Account.md "../monitoring/CloudWatch-Unified-Cross-Account.md").

You can include as many as 20 account identifiers in the
list.

- `logGroupClass` runs the query against log groups that
  are in the specified log class, either Standard or Infrequent
  Access. If you omit this, the default of Standard log class is used.
  For more information about log classes, see [Log classes](CloudWatch_Logs_Log_Classes.md "CloudWatch_Logs_Log_Classes.md").
  Because you can specify large numbers of log groups to query this way, we
  recommend that you use `SOURCE` only in queries that leverage
  field indexes that you have created. For more information about indexing
  fields in log groups, see [Create field indexes to improve query performance and reduce scan volume](CloudWatchLogs-Field-Indexing.md "CloudWatchLogs-Field-Indexing.md")

The following example selects all log groups in the account. If this is a
monitoring account then the log groups across monitoring and all the source
accounts will be selected. If the total number of log groups exceed 10,000
then you will see an error prompting you to reduce the number of log groups
by using a different log group selection method.

```
SOURCE logGroups()
```

The following example selects the log groups in the
`111122223333` source account. If you start a query
in a monitoring account in CloudWatch cross-account observability, log groups in
all source accounts and in the monitoring account are selected by
default.

```
SOURCE logGroups(accountIdentifiers:['111122223333'])
```

The next example selects log groups based on name prefixes.

```
SOURCE logGroups(namePrefix: ['namePrefix1', 'namePrefix2'])
```

The following example selects all log groups in the Infrequent Access log
class. If you don't include the `class` identifier, the query
applies only to log groups in the Standard log class, which is the default.

```
SOURCE logGroups(class: ['INFREQUENT_ACCESS'])
```

The next example selects log groups in the 111122223333 account
that start with specific name prefixes and are in the Standard log class.
The class is not mentioned in the command because Standard is the default
log class value.

```
SOURCE logGroups(accountIdentifiers:['111122223333'], namePrefix: ['namePrefix1', 'namePrefix2']
```

The final example displays how to use the `SOURCE` command with
the `start-query` AWS CLI command.

```
aws logs start-query
--region us-east-1
--start-time 1729728200
--end-time 1729728215
--query-string "SOURCE logGroups(namePrefix: ['Query']) | fields @message | limit 5"
```

Query data sources

To use `SOURCE` to specify the data sources to query, you can
use the `dataSource` keyword. You can include as many as ten data
sources in the list.

The following example selects the `amazon_vpc.flow` data
source.

```
SOURCE dataSource(['amazon_vpc.flow'])
```

The following example selects the `amazon_vpc.flow` data
source and limits the log groups based on a log group name prefix.

```
SOURCE dataSource(['amazon_vpc.flow']) logGroups(namePrefix: ['namePrefix1'])
```
