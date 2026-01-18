# Granting SELECT

or EXECUTE privileges to SYS objects

Usually you transfer privileges by using roles, which can contain many objects. To
grant privileges to a single object, use the Amazon RDS procedure
`rdsadmin.rdsadmin_util.grant_sys_object`. The procedure grants only
privileges that the master user has already been granted through a role or direct
grant.

The `grant_sys_object` procedure has the following parameters.

###### Important

For all parameter values, use uppercase unless you created the user with a
case-sensitive identifier. For example, if you run `CREATE USER
 myuser` or `CREATE USER MYUSER`, the data dictionary stores
`MYUSER`. However, if you use double quotes in `CREATE USER
 "MyUser"`, the data dictionary stores `MyUser`.

| Parameter name   | Data type | Default | Required | Description                                                                                                                                                                                                                                                                                                     |
| ---------------- | --------- | ------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `p_obj_name`     | varchar2  | —       | Yes      | The name of the object to grant privileges for. The object can<br>be a directory, function, package, procedure, sequence, table,<br>or view. Object names must be spelled exactly as they appear in<br>`DBA_OBJECTS`. Most system objects are defined in<br>uppercase, so we recommend that you try that first. |
| `p_grantee`      | varchar2  | —       | Yes      | The name of the object to grant privileges to. The object can<br>be a schema or a role.                                                                                                                                                                                                                         |
| `p_privilege`    | varchar2  | null    | Yes      | —                                                                                                                                                                                                                                                                                                               |
| `p_grant_option` | boolean   | false   | No       | Set to `true` to use the with grant option.                                                                                                                                                                                                                                                                     |

The following example grants select privileges on an object named
`V_$SESSION` to a user named `USER1`.

```
begin
    rdsadmin.rdsadmin_util.grant_sys_object(
        p_obj_name  => '`V_$SESSION`',
        p_grantee   => '`USER1`',
        p_privilege => '`SELECT`');
end;
/
```

The following example grants select privileges on an object named
`V_$SESSION` to a user named `USER1` with the grant
option.

```
begin
    rdsadmin.rdsadmin_util.grant_sys_object(
        p_obj_name     => '`V_$SESSION`',
        p_grantee      => '`USER1`',
        p_privilege    => '`SELECT`',
        p_grant_option => `true`);
end;
/
```

To be able to grant privileges on an object, your account must have those
privileges granted to it directly with the grant option, or via a role granted using
`with admin option`. In the most common case, you may want to grant
`SELECT` on a DBA view that has been granted to the
`SELECT_CATALOG_ROLE` role. If that role isn't already directly
granted to your user using `with admin option`, then you can't
transfer the privilege. If you have the DBA privilege, then you can grant the role
directly to another user.

The following example grants the `SELECT_CATALOG_ROLE` and
`EXECUTE_CATALOG_ROLE` to `USER1`. Since the `with
 admin option` is used, `USER1` can now grant access to SYS
objects that have been granted to `SELECT_CATALOG_ROLE`.

```
GRANT SELECT_CATALOG_ROLE TO `USER1` WITH ADMIN OPTION;
GRANT EXECUTE_CATALOG_ROLE to `USER1` WITH ADMIN OPTION;
```

Objects already granted to `PUBLIC` do not need to be re-granted. If
you use the `grant_sys_object` procedure to re-grant access, the
procedure call succeeds.
