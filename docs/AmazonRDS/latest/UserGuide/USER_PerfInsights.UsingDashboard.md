# Setting the SQL text limit for Amazon RDS for PostgreSQL DB

instances

Amazon RDS for PostgreSQL
handles text differently. You can set the text size limit with the DB instance parameter
`track_activity_query_size`. This parameter has the following characteristics:

Default text size

On Amazon RDS for PostgreSQL version 9.6, the default setting for the
`track_activity_query_size` parameter is 1,024 bytes. On Amazon RDS for PostgreSQL version 10 or higher, the default is 4,096 bytes.

Maximum text size

The limit for `track_activity_query_size` is 102,400 bytes for Amazon RDS for PostgreSQL version 12 and lower. The maximum is 1 MB for version 13 and higher.

If the engine returns 1 MB to Performance Insights, the console displays only the first 4 KB. If
you download the query, you get the full 1 MB. In this case, viewing and downloading return different
numbers of bytes. For more information about the `track_activity_query_size` DB instance
parameter, see [Run-time Statistics](https://www.postgresql.org/docs/current/runtime-config-statistics.html "https://www.postgresql.org/docs/current/runtime-config-statistics.html") in the PostgreSQL documentation.

To increase the SQL text size, increase the `track_activity_query_size` limit. To modify the
parameter, change the parameter setting in the parameter group that is associated with the Amazon RDS for PostgreSQL DB
instance.

###### To change the setting when the instance uses the default parameter group

1. Create a new DB instance parameter group for the appropriate DB engine and DB engine version.
2. Set the parameter in the new parameter group.
3. Associate the new parameter group with the DB instance.
   For information about setting a DB instance parameter, see [Modifying parameters in a DB parameter group
   in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").
