

# Revoking SELECT or EXECUTE privileges on SYS objects
<a name="Appendix.Oracle.CommonDBATasks.RevokePrivileges"></a>

To revoke privileges on a single object, use the Amazon RDS procedure `rdsadmin.rdsadmin_util.revoke_sys_object`. The procedure only revokes privileges that the master user has already been granted through a role or direct grant. 

The `revoke_sys_object` procedure has the following parameters. 



| Parameter name | Data type | Default | Required | Description | 
| --- | --- | --- | --- | --- | 
| `p_obj_name` | varchar2 | — | Yes | The name of the object to revoke privileges for. The object can be a directory, function, package, procedure, sequence, table, or view. Object names must be spelled exactly as they appear in `DBA_OBJECTS`. Most system objects are defined in uppercase, so we recommend that you try that first.  | 
| `p_revokee` | varchar2 | — | Yes | The name of the user or role to revoke privileges from.  | 
| `p_privilege` | varchar2 | null | Yes | The privilege to revoke. Valid values include `SELECT`, `EXECUTE`, and `ALL`. | 

The following example revokes select privileges on an object named `V_$SESSION` from a user named `USER1`.

```
begin
    rdsadmin.rdsadmin_util.revoke_sys_object(
        p_obj_name  => '{{V_$SESSION}}',
        p_revokee   => '{{USER1}}',
        p_privilege => '{{SELECT}}');
end;
/
```