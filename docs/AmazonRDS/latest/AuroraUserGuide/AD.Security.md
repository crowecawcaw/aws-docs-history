# Using AD security groups for Aurora PostgreSQL access

control

From Aurora PostgreSQL 14.10 and 15.5 versions, Aurora PostgreSQL access control can be managed
using AWS Directory Service for Microsoft Active Directory (AD) security groups. Earlier
versions of Aurora PostgreSQL support Kerberos based authentication with AD only for individual
users. Each AD user had to be explicitly provisioned to DB cluster to get access.

Instead of explicitly provisioning each AD user to DB cluster based on business needs, you can
leverage AD security groups as explained below:

- AD users are members of various AD security groups in an Active Directory. These
  are not dictated by DB cluster administrator, but are based on business requirements, and
  are handled by an AD administrator.
- DB cluster administrators create DB roles in DB instances based on business
  requirements. These DB roles may have different permissions or privileges.
- DB cluster administrators configure a mapping from AD security groups to DB roles on a
  per DB cluster basis.
- DB users can access DB clusters using their AD credentials. Access is based on AD
  security group membership. AD users gain or lose access automatically based on their
  AD group memberships.

## Prerequisites

Ensure that you have the following before setting up the extension for AD Security
groups:

- Set up Kerberos authentication for PostgreSQL DB clusters. For more
  information, see [Setting up Kerberos authentication for PostgreSQL DB
  clusters](postgresql-kerberos-setting-up.md "postgresql-kerberos-setting-up.md").

###### Note

For AD security groups, skip Step 7: Create PostgreSQL users for your
Kerberos principals in this setup procedure.

###### Important

If you enable AD security groups on an Aurora PostgreSQL cluster that
already has Kerberos authentication enabled, you might encounter
authentication issues. This occurs when you add `pg_ad_mapping`
to the `shared_preload_libraries` parameter and restart your
database. When using cluster endpoints, login attempts using an AD user that
isn't a database user with the `rds_ad` role can fail. This can
also potentially cause engine crashes. To resolve this issue, disable and
then re-enable Kerberos authentication on your cluster. This workaround is
required for existing instances but doesn't affect instances created after
April 2025.

- Managing a DB cluster in a Domain. For more information, see [Managing a DB cluster in a Domain](postgresql-kerberos-managing.md "postgresql-kerberos-managing.md").

## Setting up the pg_ad_mapping

extension

Aurora PostgreSQL is now providing `pg_ad_mapping` extension to manage the
mapping between AD security groups and DB roles in Aurora PostgreSQL cluster. For more
information about the functions provided by `pg_ad_mapping`, see [Using functions from the
pg_ad_mapping extension](#AD.Security.Groups.functions "#AD.Security.Groups.functions").

To set up the `pg_ad_mapping` extension on your Aurora PostgreSQL DB cluster,
you first add `pg_ad_mapping` to the shared libraries on the custom DB
cluster parameter group for your Aurora PostgreSQL DB cluster. For information about
creating a custom DB cluster parameter group, see [Parameter groups for Amazon Aurora](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").
Next, you install the `pg_ad_mapping` extension. The procedures in this
section show you how. You can use the AWS Management Console or the AWS CLI.

You must have permissions as the `rds_superuser` role to perform all these
tasks.

The steps following assume that your Aurora PostgreSQL DB cluster is associated with a
custom DB cluster parameter group.

###### To set up the `pg_ad_mapping` extension

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose your Aurora PostgreSQL DB cluster's
   Writer instance.
3. Open the **Configuration** tab for your Aurora PostgreSQL
   DB cluster writer instance. Among the Instance details, find the
   **Parameter group** link.
4. Choose the link to open the custom parameters associated with your
   Aurora PostgreSQL DB cluster.
5. In the **Parameters** search field, type
   `shared_pre` to find the
   `shared_preload_libraries` parameter.
6. Choose **Edit parameters** to access the property
   values.
7. Add `pg_ad_mapping` to the list in the
   **Values** field. Use a comma to separate items in
   the list of values.

![Image of the shared_preload_libaries parameter with pgAudit added.](images/apg_shared_preload_pgadmapping.png) 8. Reboot the writer instance of your Aurora PostgreSQL DB cluster so that
your change to the `shared_preload_libraries` parameter takes
effect. 9. When the instance is available, verify that `pg_ad_mapping`
has been initialized. Use `psql` to connect to the writer
instance of your Aurora PostgreSQL DB cluster, and then run the following
command.

```
`SHOW shared_preload_libraries;`
`shared_preload_libraries
--------------------------
rdsutils,pg_ad_mapping
(1 row)`
```

10. With `pg_ad_mapping` initialized, you can now create the
    extension. You need to create the extension after initializing the
    library to start using the functions provided by this extension.

```
CREATE EXTENSION pg_ad_mapping;
```

11. Close the `psql` session.

```
`labdb=>` `\q`
```

###### To setup pg_ad_mapping

To setup pg_ad_mapping using the AWS CLI, you call the [modify-db-parameter-group](../../../cli/latest/reference/rds/modify-db-parameter-group.md "../../../cli/latest/reference/rds/modify-db-parameter-group.md") operation to add this parameter in
your custom parameter group, as shown in the following procedure.

1. Use the following AWS CLI command to add `pg_ad_mapping` to
   the `shared_preload_libraries` parameter.

```
aws rds modify-db-parameter-group \
   --db-parameter-group-name `custom-param-group-name` \
   --parameters "ParameterName=shared_preload_libraries,ParameterValue=pg_ad_mapping,ApplyMethod=pending-reboot" \
   --region `aws-region`
```

2. Use the following AWS CLI command to reboot the writer instance of your
   Aurora PostgreSQL DB cluster so that the pg_ad_mapping is
   initialized.

```
aws rds reboot-db-instance \
    --db-instance-identifier `writer-instance` \
    --region `aws-region`
```

3. When the instance is available, you can verify that
   `pg_ad_mapping` has been initialized. Use
   `psql` to connect to the writer instance of your
   Aurora PostgreSQL DB cluster, and then run the following command.

```
`SHOW shared_preload_libraries;`
`shared_preload_libraries
--------------------------
rdsutils,pg_ad_mapping
(1 row)`
```

With pg_ad_mapping initialized, you can now create the
extension.

```
CREATE EXTENSION pg_ad_mapping;
```

4. Close the `psql` session so that you can use the
   AWS CLI.

```
`labdb=>` `\q`
```

## Retrieving Active Directory Group SID in

PowerShell

A security identifier (SID) is used to uniquely identify a security principal or
security group. Whenever a security group or account is created in Active Directory a
SID is assigned to it. To fetch the AD security group SID from the active directory, you
can use the Get-ADGroup cmdlet from windows client machine which is joined with that
Active Directory domain. The Identity parameter specifies the Active Directory group
name to get the corresponding SID.

The following example returns the SID of AD group
`adgroup1`.

```

`C:\Users\Admin>` `Get-ADGroup -Identity adgroup1 | select SID`
            `SID
-----------------------------------------------
S-1-5-21-3168537779-1985441202-1799118680-1612`

```

## Mapping DB role with AD security

group

You need to explicitly provision the AD security groups in the database as a
PostgreSQL DB role. An AD user, who is part of at least one provisioned AD security
group will get access to the database. You shouldn’t grant `rds_ad role` to
AD group security based DB role. Kerberos authentication for security group will get
triggered by using the domain name suffix like
`user1@example.com`. This DB role can't use Password or IAM
authentication to gain access to database.

###### Note

AD users who have a corresponding DB role in the database with `rds_ad`
role granted to them, can't login as part of the AD security group. They will get
access through DB role as an individual user.

For example, accounts-group is a security group in AD where you would like to
provision this security group in the Aurora PostgreSQL as accounts-role.

| AD Security Group | PosgreSQL DB role |
| ----------------- | ----------------- |
| accounts-group    | accounts-role     |

When mapping the DB role with the AD security group, you must ensure that DB role has
the LOGIN attribute set and it has CONNECT privilege to the required login
database.

```
`postgres =>` `alter role `accounts-role` login;`
        `ALTER ROLE`
``postgres =>` grant connect on database `accounts-db` to `accounts-role`;`
```

Admin can now proceed to create the mapping between AD security group and PostgreSQL
DB role.

```
`admin=>``select pgadmap_set_mapping(`'accounts-group'`, `'accounts-role'`, `<SID>`, `<Weight>`);`
```

For information on retrieving SID of AD security group, see [Retrieving Active Directory Group SID in
PowerShell](#AD.Security.Groups.retrieving "#AD.Security.Groups.retrieving").

There might be cases where an AD user belongs to multiple groups, in that case, AD
user will inherit the privileges of the DB role, which was provisioned with the highest
weight. If the two roles have the same weight, AD user will inherit the privileges of
the DB role corresponding to the mapping that was added recently. The recommendation is
to specify weights that reflect the relative permissions/privileges of individual DB
roles. Higher the permissions or privileges of a DB role, higher the weight that should
be associated with the mapping entry. This will avoid the ambiguity of two mappings
having the same weight.

The following table shows a sample mapping from AD security groups to Aurora PostgreSQL DB
roles.

| AD Security Group | PosgreSQL DB role | Weight |
| ----------------- | ----------------- | ------ |
| accounts-group    | accounts-role     | 7      |
| sales-group       | sales-role        | 10     |
| dev-group         | dev-role          | 7      |

In the following example, `user1` will inherit the privileges of sales-role
since it has the higher weight while `user2` will inherit the privileges of
`dev-role` as the mapping for this role was created after
`accounts-role`, which share the same weight as
`accounts-role`.

| Username | Security Group membership  |
| -------- | -------------------------- |
| user1    | accounts-group sales-group |
| user2    | accounts-group dev-group   |

The psql commands to establish, list, and clear the mappings are shown below.
Currently, it isn't possible to modify a single mapping entry. The existing entry needs
to be deleted and the mapping recreated.

```

`admin=>``select pgadmap_set_mapping('accounts-group', 'accounts-role', 'S-1-5-67-890', 7);`
`admin=>``select pgadmap_set_mapping('sales-group', 'sales-role', 'S-1-2-34-560', 10);`
`admin=>``select pgadmap_set_mapping('dev-group', 'dev-role', 'S-1-8-43-612', 7);`

`admin=>``select * from pgadmap_read_mapping();`
            `ad_sid | pg_role | weight | ad_grp
-------------+----------------+--------+---------------
S-1-5-67-890 | accounts-role | 7 | accounts-group
S-1-2-34-560 | sales-role | 10 | sales-group
S-1-8-43-612 | dev-role | 7 | dev-group
(3 rows)`

```

## AD user identity logging/auditing

Use the following command to determine the database role inherited by current or
session user:

```

`postgres=>``select session_user, current_user;`
            `session_user | current_user
-------------+--------------
dev-role | dev-role

(1 row)`

```

To determine the AD security principal identity, use the following command:

```

`postgres=>``select principal from pg_stat_gssapi where pid = pg_backend_pid();`
            `principal
-------------------------
 user1@example.com

(1 row)`

```

Currently, AD user identity isn't visible in the audit logs. The
`log_connections` parameter can be enabled to log DB session
establishment. For more information, see [log_connections](../../../prescriptive-guidance/latest/tuning-postgresql-parameters/log-connections.md "../../../prescriptive-guidance/latest/tuning-postgresql-parameters/log-connections.md"). The output for this includes the AD user identity, as
shown below. The backend PID associated with this output can then help attribute actions
back to the actual AD user.

```
`pgrole1@postgres:[615]:LOG: connection authorized: user=pgrole1 database=postgres application_name=psql GSS (authenticated=yes, encrypted=yes, principal=Admin@EXAMPLE.COM)`
```

## Limitations

- Microsoft Entra ID known as Azure Active Directory isn't supported.

## Using functions from the

`pg_ad_mapping` extension

`pg_ad_mapping` extension provided support to the following
functions:

### pgadmap_set_mapping

This function establishes the mapping between AD security group and Database role
with an associated weight.

#### Syntax

```
pgadmap_set_mapping(
ad_group,
db_role,
ad_group_sid,
weight)

```

#### Arguments

| Parameter    | Description                                                                                                                                                                                                                                                                                 |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ad_group     | Name of AD Group. Value cannot be null or empty<br>string.                                                                                                                                                                                                                                  |
| db_role      | Database role to be mapped to the specified AD Group. Value<br>cannot be null or empty string.                                                                                                                                                                                              |
| ad_group_sid | Security identifier that is used to uniquely identify the AD<br>group. Value starts with 'S-1-' and cannot be null or empty<br>string. For more information, see [Retrieving Active Directory Group SID in<br>PowerShell](#AD.Security.Groups.retrieving "#AD.Security.Groups.retrieving"). |
| weight       | Weight associated with the database role. The role with<br>highest weight gets precedence when user is a member of multiple<br>groups. Default value of weight is 1.                                                                                                                        |

#### Return type

`None`

#### Usage notes

This function adds a new mapping from AD security group to database role. It
can only be executed on the primary DB instance of the DB cluster by a user
having rds_superuser privilege.

#### Examples

```
`postgres=>` select pgadmap_set_mapping('accounts-group','accounts-role','S-1-2-33-12345-67890-12345-678',10);
            `pgadmap_set_mapping

(1 row)`
```

### pgadmap_read_mapping

This function lists the mappings between AD security group and DB role that were
set using `pgadmap_set_mapping` function.

#### Syntax

```
pgadmap_read_mapping()

```

#### Arguments

`None`

#### Return type

| Parameter    | Description                                                                                                                                                                                                                                                                                                          |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ad_group_sid | Security identifier that is used to uniquely identify the AD<br>group. Value starts with 'S-1-' and cannot be null or empty<br>string. For more information, see [Retrieving Active Directory Group SID in<br>PowerShell](#AD.Security.Groups.retrieving "#AD.Security.Groups.retrieving").accounts-role@example.com |
| db_role      | Database role to be mapped to the specified AD Group. Value<br>cannot be null or empty string.                                                                                                                                                                                                                       |
| weight       | Weight associated with the database role. The role with<br>highest weight gets precedence when user is a member of multiple<br>groups. Default value of weight is 1.                                                                                                                                                 |
| ad_group     | Name of AD Group. Value cannot be null or empty<br>string.                                                                                                                                                                                                                                                           |

#### Usage notes

Call this function to list all the available mappings between AD security
group and DB role.

#### Examples

```
`postgres=>` select * from pgadmap_read_mapping();
            `ad_sid | pg_role | weight | ad_grp
------------------------------------+---------------+--------+------------------
S-1-2-33-12345-67890-12345-678 | accounts-role | 10 | accounts-group
(1 row)

(1 row)`
```

### pgadmap_reset_mapping

This function resets one or all the mappings that were set using
`pgadmap_set_mapping` function.

#### Syntax

```
pgadmap_reset_mapping(
ad_group_sid,
db_role,
weight)

```

#### Arguments

| Parameter    | Description                                                            |
| ------------ | ---------------------------------------------------------------------- |
| ad_group_sid | Security identifier that is used to uniquely identify the AD<br>group. |
| db_role      | Database role to be mapped to the specified AD Group.                  |
| weight       | Weight associated with the database role.                              |

If no arguments are provided, all AD group to DB role mappings are reset.
Either all arguments need to be provided or none.

#### Return type

`None`

#### Usage notes

Call this function to delete a specific AD group to DB role mapping or to
reset all mappings. This function can only be executed on the primary DB instance of
the DB cluster by a user having `rds_superuser` privilege.

#### Examples

```
`postgres=>` `select * from pgadmap_read_mapping();`
            `ad_sid | pg_role | weight | ad_grp
--------------------------------+--------------+-------------+-------------------
 S-1-2-33-12345-67890-12345-678 | accounts-role| 10 | accounts-group
 S-1-2-33-12345-67890-12345-666 | sales-role | 10 | sales-group

(2 rows)`
`postgres=>` `select pgadmap_reset_mapping('S-1-2-33-12345-67890-12345-678', 'accounts-role', 10);`
                `pgadmap_reset_mapping
(1 row)`
`postgres=>` `select * from pgadmap_read_mapping();`
            `ad_sid | pg_role | weight | ad_grp
--------------------------------+--------------+-------------+---------------
 S-1-2-33-12345-67890-12345-666 | sales-role | 10 | sales-group

(1 row)`
`postgres=>` `select pgadmap_reset_mapping();`
`pgadmap_reset_mapping
(1 row)`
`postgres=>` `select * from pgadmap_read_mapping();`
            `ad_sid | pg_role | weight | ad_grp
--------------------------------+--------------+-------------+--------------
 (0 rows)`

```
