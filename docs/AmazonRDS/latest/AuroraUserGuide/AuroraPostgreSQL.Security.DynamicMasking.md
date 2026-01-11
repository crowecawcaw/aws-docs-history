# Configuring masking policy management role

The PostgreSQL column masking extension, `pg_columnmask`, allows you to delegate the management of
masking policies to a specific role, rather than requiring `rds_superuser` or table owner privileges.
This provides more granular control over who can create, alter, and drop masking policies.

To configure the role that will have masking policy management privileges, follow these steps:

1. Create the policy admin role – As an `rds_superuser`,
   create a new role responsible for managing masking policies:

```
CREATE ROLE mask_admin NOLOGIN;
```

2. Configure the PostgreSQL parameter – In your custom DB cluster parameter group,
   set the `pgcolumnmask.policy_admin_rolname` engine configuration parameter to the name of the role you created:

```
pgcolumnmask.policy_admin_rolname = mask_admin
```

This engine configuration parameters can be set in a DB cluster parameter group and
it does not require an instance reboot. For details on updating parameter, see [Modifying parameters in a DB cluster parameter group in Amazon Aurora](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md"). 3. Grant the role to users As an `rds_superuser`, grant the `mask_admin` role to the users
who should be able to manage masking policies:

```
CREATE USER alice LOGIN;
CREATE USER bob LOGIN;
GRANT mask_admin TO alice, bob;
```

Additionally, ensure that the users have USAGE privilege on the schemas where they will be managing masking policies:

```
GRANT USAGE ON SCHEMA hr TO alice, bob;
```

Now, when users `alice` and `bob` connect to the database, they can use the standard `pg_columnmask`
extension functions to create, alter, and drop masking policies on all tables in all the schemas where they have `USAGE` privilege on the schema.
