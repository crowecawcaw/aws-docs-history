

# Terminating a session
<a name="Appendix.Oracle.CommonDBATasks.KillingSession"></a>

To terminate a session, use the Amazon RDS procedure `rdsadmin.rdsadmin_util.kill`. The `kill` procedure has the following parameters.



| Parameter name | Data type | Default | Required | Description | 
| --- | --- | --- | --- | --- | 
| `sid` | number | — | Yes | The session identifier. | 
| `serial` | number | — | Yes | The serial number of the session. | 
| `method` | varchar | null | No | Valid values are `'IMMEDIATE'` or `'PROCESS'`. If you specify `IMMEDIATE`, it has the same effect as running the following statement:<pre>ALTER SYSTEM KILL SESSION 'sid,serial#' IMMEDIATE</pre><br />If you specify `PROCESS`, you terminate the processes associated with a session. Only specify `PROCESS` if terminating the session using `IMMEDIATE` was unsuccessful. | 

To get the session identifier and the session serial number, query the `V$SESSION` view. The following example gets all sessions for the user {{AWSUSER}}.

```
SELECT SID, SERIAL#, STATUS FROM V$SESSION WHERE USERNAME = '{{AWSUSER}}';
```

The following example terminates a session.

```
BEGIN
    rdsadmin.rdsadmin_util.kill(
        sid    => {{sid}}, 
        serial => {{serial_number}},
        method => 'IMMEDIATE');
END;
/
```

The following example terminates the processes associated with a session.

```
BEGIN
    rdsadmin.rdsadmin_util.kill(
        sid    => {{sid}}, 
        serial => {{serial_number}},
        method => 'PROCESS');
END;
/
```