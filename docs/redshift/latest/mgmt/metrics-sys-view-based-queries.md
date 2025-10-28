Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Sys View-based Queries and Database Monitoring

This document describes the `SYS` views that provide data for the Queries and Database Monitoring page in the Amazon Redshift Console,
a tool for analyzing a query's components and performance. For information about the
Queries and Database Monitoring page, see [Query and Database Monitoring](metrics-enhanced-query-monitoring.md "metrics-enhanced-query-monitoring.md").

The **Queries and Database Monitoring** page has a functionality that displays information provided
by `SYS` views. The console view includes the query profiler, which shows the graphical
execution plan of a query. To switch to the `SYS`-based view, follow the steps here to grant the right access and
permissions for the new **Queries and Database Monitoring** page.

The `SYS`-based view feature of the **Queries and Database Monitoring**
page has the following functionality:

- **Increased security** — You need elevated privileges to monitor queries for other users
- **Seven-day query history** — Guaranteed access to seven days of query history
- **Query profiler** — A graphical tool for monitoring query performance. For more information,
  see [Query profiler](using-query-plan-profiler.md "using-query-plan-profiler.md")
  By default, you can only view your own queries. To view queries owned by other users, grant the `SYS:MONITOR` role
  to your account. To allow a user to end running queries, grant the user the `SYS:OPERATOR` privilege.

To grant the privilege to view queries owned by all users to a database user or role, run the following commands:

```
grant role sys:monitor to "IAM:`role-name`";
grant role sys:monitor to "IAM:`user-name`";
```

To automatically assign the `sys:monitor` role to an IAM
user or role for Amazon Redshift Serverless or provisioned, run the following commands:

```
 create role monitor;
grant role sys:monitor to role monitor;
```

To update the IAM role used for query monitoring, do the following:

1. Choose the **Tags** tab.
2. Choose **Manage tags**.
3. Add a tag with key `RedshiftDbRoles` and value `monitor`.
4. Save changes
   To add database credentials to a user, run the following command:

```
grant role sys:monitor to `<username>`
```

## Permissions

To use query monitoring, your IAM user needs permissions to access the Amazon Redshift data plane. Ensure that
your IAM user has the following permissions in their permissions policy:

```
{
    "Sid": "DataAPIPermissions",
    "Action": [
        "redshift-data:ExecuteStatement",
        "redshift-data:CancelStatement",
        "redshift-data:GetStatementResult",
        "redshift-data:DescribeStatement",
        "redshift-data:ListDatabases"
    ],
    "Effect": "Allow",
    "Resource": "arn:aws:redshift-serverless:us-west-2:123456789012:workgroup/01234567-89ab-cdef-0123-456789abcdef"
},
```

## Connect to the database

Before using the enhanced query monitoring feature, you must first connect to your database
for access to `SYS` view-based information. To connect to the database, use one of the following credentials:

- Username and password
- Temporary credentials associated with your IAM role
- A database user

Note the following about using enhanced query monitoring:

- For provisioned clusters, you must connect to a database, because enhanced
  query monitoring uses `SYS` views. These views have increased security, and require
  elevated privileges to access data about queries owned by other users.
- When using the `SYS` view-based queries and database monitoring page,
  only your `user_id` is visible if your
  user account doesn't have the database superuser role. Usernames are hidden from non-superusers.
- As part of the sys view-based queries and database monitoring page experience, the query execution process ID (`p_id`)
  appears under the column heading `session_id`.
