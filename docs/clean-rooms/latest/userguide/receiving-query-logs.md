# Receive query and job logs

You don't need to perform any actions outside of AWS Clean Rooms to set up query logs and job logs.
AWS Clean Rooms creates log groups for collaborations after each collaboration member [creates a membership](create-membership.md "create-membership.md").

Members who can query, members who can run queries and jobs, members who can receive
results, and members whose configuration tables are referenced in the query will receive a
query log or a job log.

The member who can query and member who can receive results will receive query logs for
each configured table that is referenced in the query. If they don’t own the configured table,
they won't be able to view the configured table ID (`configuredTableID`).

The member who can run queries and jobs and member who can receive results will receive
job logs for each configured table that is referenced in the job. If they don’t own the
configured table, they won't be able to view the configured table ID
(`configuredTableID`).

If a member has multiple configured table associations referenced in the query, they will
receive a query log for each configured table.

If a member has multiple configured table associations referenced in the job, they will
receive a job log for each configured table.

Logs are created for queries that contain unsupported and supported SQL in AWS Clean Rooms. For more
details, see the [AWS Clean Rooms
SQL Reference](../sql-reference/sql-reference.md "../sql-reference/sql-reference.md").

Logs are also created when queries or jobs reference configured tables that are not
associated to the collaboration.

Logs may contain
information about incorrect SQL.

Query and job logs indicate the status of a query but don't report whether query output
was delivered. They confirm that a query or job was submitted by the member who can query.
Query logs also confirm that the query contains supported SQL in AWS Clean Rooms and references
configured tables associated to the collaboration.

For example, a log isn't produced if the query was cancelled after AWS Clean Rooms validated
its compliance with analysis rules and during query processing.

If you delete the log group, you must re-create the log group manually with the same log
group name (collaboration ID of the collaboration). Or, you can turn the logging off and on in
your membership.

For more information about how to turn on analysis logging, see [Creating a collaboration](create-collaboration.md "create-collaboration.md").

For more information about Amazon CloudWatch Logs, see the [Amazon CloudWatch Logs User
Guide](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md").
