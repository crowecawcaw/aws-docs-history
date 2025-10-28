# mysql.rds_kill_query_id

Ends a query running against the MariaDB server in order to terminate long-running or
problematic queries. You can identify the query ID and effectively stop a specific query
to address performance issues and maintain optimal database operation.

## Syntax

```
CALL mysql.rds_kill_query_id(*queryID*);
```

## Parameters

_queryID_

Integer. The identity of the query to be ended.

## Usage notes

To stop a query running against the MariaDB server, use the
`mysql.rds_kill_query_id` procedure and pass in the ID of that query.
To obtain the query ID, query the MariaDB [Information schema PROCESSLIST table](http://mariadb.com/kb/en/mariadb/information-schema-processlist-table/ "http://mariadb.com/kb/en/mariadb/information-schema-processlist-table/"), as shown following:

```
SELECT USER, HOST, COMMAND, TIME, STATE, INFO, QUERY_ID FROM
                INFORMATION_SCHEMA.PROCESSLIST WHERE USER = '<user name>';
```

The connection to the MariaDB server is retained.

## Examples

The following example ends a query with a query ID of 230040:

```
call mysql.rds_kill_query_id(230040);
```
