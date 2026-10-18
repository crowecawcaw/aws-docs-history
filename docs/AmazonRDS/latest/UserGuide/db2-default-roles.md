

# Amazon RDS for Db2 default roles
<a name="db2-default-roles"></a>

When RDS for Db2 provisions a database ([rdsadmin.create\_database](db2-sp-managing-databases.md#db2-sp-create-database)) or restores one ([rdsadmin.restore\_database](db2-sp-managing-databases.md#db2-sp-restore-database)), it creates a set of default principals: users, groups, and roles. RDS for Db2 grants its managed roles to `master_user_role` with the `ADMIN` option, and grants `master_user_role` to the master user. The master user can then grant these roles to other users, groups, or roles by using standard `GRANT` statements. The following table lists each principal and the role or privileges it receives.


| Principal | Type | Receives (role or privilege) | 
| --- | --- | --- | 
| MASTER\_USER\_ROLE | Role | See the system privilege and database role columns for RDS for Db2 in [Master user account privileges](UsingWithRDS.MasterAccounts.md). | 
| MASTER USER (ADMIN) | User (master) | MASTER\_USER\_ROLE | 
| MASTERDBA | Group | MASTER\_USER\_ROLE | 
| DBA | Role | DATAACCESS. The master user can add more authorizations or privileges to this role, and then grant the role to other users, groups, or roles. | 
| DBA\_RESTRICTED | Role | Empty role. The master user can add privileges to this role, and then grant the role to other users, groups, or roles. | 
| DEVELOPER | Role | DATAACCESS. The master user can add more authorizations or privileges to this role, and then grant the role to other users, groups, or roles. | 
| ROLE\_NULLID\_PACKAGES | Role | BIND and EXECUTE on NULLID.\* system packages. | 
| ROLE\_PROCEDURES | Role | EXECUTE on selected SYSIBM/SYSPROC procedures. | 
| ROLE\_TABLESPACES | Role | USE OF TABLESPACE on tablespaces created by RDS for Db2. | 