# How Amazon Q Business connector

crawls Aurora (PostgreSQL) ACLs

When you connect a database data source to Amazon Q Business, Amazon Q Business crawls user and group information from a column in the source table.
You specify this column in the console or using the `configuration` parameter
as part of the `CreateDataSource` operation.

Activating ACL crawling allows the system to filter chat responses based on your end
users' document access levels.

Prerequisites:

- The group ACL column in the database should be a string containing a semicolon
  delimited list of groups.
- The user ACL column in the database should be a string containing a semicolon
  delimited list of users.
  A database data source has the following limitation:

- You can only specify an allow list for a database data source. You can't
  specify a deny list.
  For
  more information, see:

- [Authorization](connector-concepts.md#connector-authorization "connector-concepts.md#connector-authorization")
- [Identity crawler](connector-concepts.md#connector-identity-crawler "connector-concepts.md#connector-identity-crawler")
- [Understanding User Store](connector-principal-store.md "connector-principal-store.md")
