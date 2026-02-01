Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Amazon Redshift system-defined roles

Amazon Redshift provides a few system-defined roles that are defined with specific
permissions. System-specific roles start with a `sys:` prefix. Only users
with appropriate access can alter system-defined roles or create custom system-defined
roles. You can't use the `sys:` prefix for a custom system-defined role.

The following table summarizes the roles and their permissions.

| Role name       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `sys:monitor`   | This role has the permission to access catalog or system tables.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `sys:operator`  | This role has the permissions to access catalog or<br>system tables, analyze, vacuum, or cancel queries.                                                                                                                                                                                                                                                                                                                                                                                                           |
| `sys:dba`       | This role has the permissions to create schemas, create<br>tables, drop schemas, drop tables, and truncate tables. It has the<br>permissions to create or replace stored procedures, drop procedures, create<br>or replace functions, create or replace external functions, create views,<br>and drop views. Also, this role inherits all the permissions from the<br>sys:operator role.                                                                                                                           |
| `sys:superuser` | This role has all the supported system permissions defined in [System permissions for RBAC](r_roles-system-privileges.md "r_roles-system-privileges.md").                                                                                                                                                                                                                                                                                                                                                          |
| `sys:secadmin`  | • This role has the permissions to create users, alter<br>users, drop users, create roles, drop roles, and grant roles.<br>• This role has permissions to turn RLS ON or OFF on a relation and permissions to manage RLS and DDM policies (CREATE, DROP, ATTACH, DETACH, and ALTER). Also, note that EXPLAIN RLS, IGNORE RLS, and EXPLAIN MASKING permissions are granted to this role by default.<br>• This role can have access<br>to user tables only when the permission is explicitly granted to the<br>role. |

## System-defined roles and users for data sharing

Amazon Redshift creates roles and users for internal use that correspond to datashares and datashare consumers. Each internal role name and user name
has the reserved namespace prefix `ds:`. They have the following format:

| Name                      | Description                                               |
| ------------------------- | --------------------------------------------------------- |
| `ds:`sharename``          | A system role that corresponds with a datashare.          |
| `ds:`sharename_consumer`` | A system user that corresponds with a datashare consumer. |

A data sharing role is created for each datashare. It holds all permissions currently granted to the datashare. A data sharing user is created for each consumer of a
datashare. It is granted permission to a single data sharing role. A consumer added to multiple datashares will have a data sharing user created for each datashare.

These users and roles are required for data sharing to work properly. They cannot be modified or dropped and they cannot be accessed or used
for any tasks run by customers. You can safely ignore them. For more information about data sharing,
see [Sharing data across clusters in Amazon Redshift](datashare-overview.md "datashare-overview.md").

###### Note

You can't use the `ds:` prefix to create user-defined roles or users.
