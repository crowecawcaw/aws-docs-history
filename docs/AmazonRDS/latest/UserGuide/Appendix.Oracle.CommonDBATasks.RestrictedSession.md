

# Enabling and disabling restricted sessions
<a name="Appendix.Oracle.CommonDBATasks.RestrictedSession"></a>

To enable and disable restricted sessions, use the Amazon RDS procedure `rdsadmin.rdsadmin_util.restricted_session`. The `restricted_session` procedure has the following parameters. 



| Parameter name | Data type | Default | Required | Description | 
| --- | --- | --- | --- | --- | 
| `p_enable` | boolean | true | No | Set to `true` to enable restricted sessions, `false` to disable restricted sessions.  | 

The following example shows how to enable and disable restricted sessions. 

```
/* Verify that the database is currently unrestricted. */

SELECT LOGINS FROM V$INSTANCE;
 
LOGINS
-------
ALLOWED

/* Enable restricted sessions */

EXEC rdsadmin.rdsadmin_util.restricted_session(p_enable => true);
 

/* Verify that the database is now restricted. */

SELECT LOGINS FROM V$INSTANCE;
 
LOGINS
----------
RESTRICTED
 

/* Disable restricted sessions */

EXEC rdsadmin.rdsadmin_util.restricted_session(p_enable => false);
 

/* Verify that the database is now unrestricted again. */

SELECT LOGINS FROM V$INSTANCE;
 
LOGINS
-------
ALLOWED
```