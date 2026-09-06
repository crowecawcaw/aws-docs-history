

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# How Amazon Q Business connector crawls Aurora (PostgreSQL) ACLs
<a name="aurora-postgresql-user-management"></a>

When you connect a database data source to Amazon Q Business, Amazon Q Business crawls user and group information from a column in the source table. You specify this column in the console or using the `configuration` parameter as part of the `CreateDataSource` operation.

Activating ACL crawling allows the system to filter chat responses based on your end users' document access levels.

Prerequisites:
+ The group ACL column in the database should be a string containing a semicolon delimited list of groups.
+  The user ACL column in the database should be a string containing a semicolon delimited list of users.

A database data source has the following limitation:
+ You can only specify an allow list for a database data source. You can't specify a deny list.

 For more information, see:
+ [Authorization](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-authorization)
+ [Identity crawler](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-concepts.html#connector-identity-crawler)
+ [Understanding User Store](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-principal-store.html)