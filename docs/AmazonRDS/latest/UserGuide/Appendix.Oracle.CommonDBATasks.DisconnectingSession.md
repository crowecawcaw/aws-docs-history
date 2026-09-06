

# Disconnecting a session
<a name="Appendix.Oracle.CommonDBATasks.DisconnectingSession"></a>

To disconnect the current session by ending the dedicated server process, use the Amazon RDS procedure `rdsadmin.rdsadmin_util.disconnect`. The `disconnect` procedure has the following parameters. 



| Parameter name | Data type | Default | Required | Description | 
| --- | --- | --- | --- | --- | 
| `sid` | number | — | Yes | The session identifier. | 
| `serial` | number | — | Yes | The serial number of the session. | 
| `method` | varchar | 'IMMEDIATE' | No | Valid values are `'IMMEDIATE'` or `'POST_TRANSACTION'`. | 

The following example disconnects a session.

```
begin
    rdsadmin.rdsadmin_util.disconnect(
        sid    => {{sid}}, 
        serial => {{serial_number}});
end;
/
```

To get the session identifier and the session serial number, query the `V$SESSION` view. The following example gets all sessions for the user `AWSUSER`.

```
SELECT SID, SERIAL#, STATUS FROM V$SESSION WHERE USERNAME = '{{AWSUSER}}';
```

The database must be open to use this method. For more information about disconnecting a session, see [ALTER SYSTEM](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/ALTER-SYSTEM.html) in the Oracle documentation. 