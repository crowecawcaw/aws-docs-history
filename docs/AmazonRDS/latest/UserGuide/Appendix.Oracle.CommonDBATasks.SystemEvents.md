# Setting and unsetting system diagnostic events

To set and unset diagnostic events at the session level, you can use the Oracle SQL statement `ALTER
 SESSION SET EVENTS`. However, to set events at the system level you can't use Oracle SQL. Instead,
use the system event procedures in the `rdsadmin.rdsadmin_util` package. The system event
procedures are available in the following engine versions:

- All Oracle Database 26ai versions
- All Oracle Database 21c versions
- 19.0.0.0.ru-2020-10.rur-2020-10.r1 and higher Oracle Database 19c versions

For more information, see [Version 19.0.0.0.ru-2020-10.rur-2020-10.r1](../OracleReleaseNotes/oracle-version-19-0.md#oracle-version-RU-RUR.19.0.0.0.ru-2020-10.rur-2020-10.r1 "../OracleReleaseNotes/oracle-version-19-0.md#oracle-version-RU-RUR.19.0.0.0.ru-2020-10.rur-2020-10.r1") in the
_Amazon RDS for Oracle Release Notes_

###### Important

Internally, the `rdsadmin.rdsadmin_util` package sets events by
using the `ALTER SYSTEM SET EVENTS` statement. This `ALTER
 SYSTEM` statement isn't documented in the Oracle Database
documentation. Some system diagnostic events can generate large amounts of
tracing information, cause contention, or affect database availability. We
recommend that you test specific diagnostic events in your nonproduction
database, and only set events in your production database under guidance of
Oracle Support.

## Listing allowed system diagnostic events

To list the system events that you can set, use the Amazon RDS procedure
`rdsadmin.rdsadmin_util.list_allowed_system_events`. This
procedure accepts no parameters.

The following example lists all system events that you can set.

```
SET SERVEROUTPUT ON
EXEC rdsadmin.rdsadmin_util.list_allowed_system_events;
```

The following sample output lists event numbers and their descriptions. Use
the Amazon RDS procedures `set_system_event` to set these events and
`unset_system_event` to unset them.

```
604   - error occurred at recursive SQL level
942   - table or view does not exist
1401  - inserted value too large for column
1403  - no data found
1410  - invalid ROWID
1422  - exact fetch returns more than requested number of rows
1426  - numeric overflow
1427  - single-row subquery returns more than one row
1476  - divisor is equal to zero
1483  - invalid length for DATE or NUMBER bind variable
1489  - result of string concatenation is too long
1652  - unable to extend temp segment by  in tablespace
1858  - a non-numeric character was found where a numeric was expected
4031  - unable to allocate  bytes of shared memory ("","","","")
6502  - PL/SQL: numeric or value error
10027 - Specify Deadlock Trace Information to be Dumped
10046 - enable SQL statement timing
10053 - CBO Enable optimizer trace
10173 - Dynamic Sampling time-out error
10442 - enable trace of kst for ORA-01555 diagnostics
12008 - error in materialized view refresh path
12012 - error on auto execute of job
12504 - TNS:listener was not given the SERVICE_NAME in CONNECT_DATA
14400 - inserted partition key does not map to any partition
31693 - Table data object  failed to load/unload and is being skipped due to error:
```

###### Note

The list of the allowed system events can change over time. To make sure
that you have the most recent list of eligible events, use
`rdsadmin.rdsadmin_util.list_allowed_system_events`.

## Setting system diagnostic events

To set a system event, use the Amazon RDS procedure
`rdsadmin.rdsadmin_util.set_system_event`. You can only set
events listed in the output of
`rdsadmin.rdsadmin_util.list_allowed_system_events`. The
`set_system_event` procedure accepts the following
parameters.

| Parameter name | Data type | Default | Required | Description                                                                                                                |
| -------------- | --------- | ------- | -------- | -------------------------------------------------------------------------------------------------------------------------- |
| `p_event`      | number    | —       | Yes      | The system event number. The value must be one of the<br>event numbers reported by<br>`list_allowed_system_events`.        |
| `p_level`      | number    | —       | Yes      | The event level. See the Oracle Database documentation or<br>Oracle Support for descriptions of different level<br>values. |

The procedure `set_system_event` constructs and runs the required
`ALTER SYSTEM SET EVENTS` statements according to the following
principles:

- The event type (`context` or `errorstack`) is
  determined automatically.
- A statement in the form `ALTER SYSTEM SET EVENTS
 '`event`LEVEL
`event_level`'` sets the context
  events. This notation is equivalent to `ALTER SYSTEM SET EVENTS
 '`event`TRACE NAME CONTEXT FOREVER,
 LEVEL`event_level`'`.
- A statement in the form `ALTER SYSTEM SET EVENTS
 '`event` ERRORSTACK
 (`event_level`)'` sets the error
  stack events. This notation is equivalent to `ALTER SYSTEM SET
 EVENTS '`event`TRACE NAME ERRORSTACK LEVEL
`event_level`'`.

The following example sets event 942 at level 3, and event 10442 at level 10.
Sample output is included.

```
SQL> SET SERVEROUTPUT ON
SQL> EXEC rdsadmin.rdsadmin_util.set_system_event(942,3);
Setting system event 942 with: alter system set events '942 errorstack (3)'

PL/SQL procedure successfully completed.

SQL> EXEC rdsadmin.rdsadmin_util.set_system_event(10442,10);
Setting system event 10442 with: alter system set events '10442 level 10'

PL/SQL procedure successfully completed.
```

## Listing system diagnostic events that are set

To list the system events that are currently set, use the Amazon RDS procedure
`rdsadmin.rdsadmin_util.list_set_system_events`. This procedure
reports only events set at system level by `set_system_event`.

The following example lists the active system events.

```
SET SERVEROUTPUT ON
EXEC rdsadmin.rdsadmin_util.list_set_system_events;
```

The following sample output shows the list of events, the event type, the
level at which the events are currently set, and the time when the event was
set.

```
942 errorstack (3) - set at 2020-11-03 11:42:27
10442 level 10 - set at 2020-11-03 11:42:41

PL/SQL procedure successfully completed.
```

## Unsetting system diagnostic events

To unset a system event, use the Amazon RDS procedure
`rdsadmin.rdsadmin_util.unset_system_event`. You can only unset
events listed in the output of
`rdsadmin.rdsadmin_util.list_allowed_system_events`. The
`unset_system_event` procedure accepts the following
parameter.

| Parameter name | Data type | Default | Required | Description                                                                                                         |
| -------------- | --------- | ------- | -------- | ------------------------------------------------------------------------------------------------------------------- |
| `p_event`      | number    | —       | Yes      | The system event number. The value must be one of the<br>event numbers reported by<br>`list_allowed_system_events`. |

The following example unsets events 942 and 10442. Sample output is
included.

```
SQL> SET SERVEROUTPUT ON
SQL> EXEC rdsadmin.rdsadmin_util.unset_system_event(942);
Unsetting system event 942 with: alter system set events '942 off'

PL/SQL procedure successfully completed.

SQL> EXEC rdsadmin.rdsadmin_util.unset_system_event(10442);
Unsetting system event 10442 with: alter system set events '10442 off'

PL/SQL procedure successfully completed.
```
