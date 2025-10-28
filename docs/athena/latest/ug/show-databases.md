# SHOW DATABASES

Lists all databases defined in the metastore. You can use `DATABASES` or
`SCHEMAS`. They mean the same thing.

The programmatic equivalent of `SHOW DATABASES` is the [ListDatabases](../APIReference/API_ListDatabases.md "../APIReference/API_ListDatabases.md") Athena API action. The equivalent method in AWS SDK for Python (Boto3) is [list_databases](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena/client/list_databases.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena/client/list_databases.html").

## Synopsis

```
SHOW {DATABASES | SCHEMAS} [LIKE '`regular_expression`']
```

## Parameters

**[LIKE '`regular_expression`']**

Filters the list of databases to those that match the
`regular_expression` that you
specify. For wildcard character matching, you can use the combination
`.*`, which matches any character zero to unlimited
times.

## Examples

```
SHOW SCHEMAS;
```

```
SHOW DATABASES LIKE '.*analytics';
```
