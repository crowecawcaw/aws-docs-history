# Amazon RDS for Db2 default roles

RDS for Db2 adds the following six roles and grants them to the
`master_user_role` with the `ADMIN` option. When the database
is provisioned, RDS for Db2 grants `master_user_role` to the master user. The
master user can in turn grant these roles to other users, groups, or roles with native
`GRANT` statements by connecting to the database.

- **DBA** – RDS for Db2 creates this empty role
  with `DATAACCESS` authorization. The master user can add more
  authorizations or privileges to this role, and then grant the role to other
  users, groups, or roles.
- **DBA_RESTRICTED** – RDS for Db2 creates this
  empty role. The master user can add privileges to this role, and then grant the
  role to other users, groups, or roles.
- **DEVELOPER** – RDS for Db2 creates this
  empty role with `DATAACCESS` authorization. The master user can add
  more authorizations or privileges to this role, and then grant the role to other
  users, groups, or roles.
- **ROLE_NULLID_PACKAGES** – RDS for Db2 grants
  `EXECUTE` privileges to this role on `ALL NULLID`
  packages that were bound by Db2 when `CREATE DATABASE` was
  run.
- **ROLE_PROCEDURES** – RDS for Db2 grants
  `EXECUTE` privileges to this role on all `SYSIBM`
  procedures.
- **ROLE_TABLESPACES** – RDS for Db2 grants
  `USAGE` privileges on tablespaces created by the `CREATE
DATABASE` command.
