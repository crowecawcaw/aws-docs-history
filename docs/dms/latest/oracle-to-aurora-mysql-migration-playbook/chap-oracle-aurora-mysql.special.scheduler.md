

# Oracle DBMS\_SCHEDULER and MySQL events
<a name="chap-oracle-aurora-mysql.special.scheduler"></a>

With AWS DMS, you can schedule and automate database tasks using Oracle DBMS\_SCHEDULER and MySQL events. Oracle DBMS\_SCHEDULER is an enterprise job scheduler that provides a way to schedule and automate recurring database tasks. MySQL events are similar, allowing you to schedule statements or stored procedures to execute at a specific time or interval.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Three star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-compatibility-3.png)  | N/A | N/A | Different paradigm and syntax | 

## Oracle usage
<a name="chap-oracle-aurora-mysql.special.scheduler.oracle"></a>

The DBMS\_SCHEDULER package contains a collection of scheduling functions the can be called from PL/DSQL.

There are two main objects involved with creating scheduling jobs: a program and schedule. A program defines what to run, and a schedule defines when to run the program. The scheduler can run a database program unit such as a procedure or an external executable such as files system shell scripts.

There are three running methods for jobs: time-based scheduling, event-based jobs, and dependency jobs or chained jobs.

### Time-based scheduling
<a name="chap-oracle-aurora-mysql.special.scheduler.oracle.timebased"></a>

The following examples create a job with a program and a schedule.

1. Create a program that will call the `UPDATE_HR_SCHEMA_STATS` procedure in the `HR` schema.

1. Create a schedule that will set the interval of running the jobs that using it. This schedule will run the job every hour.

1. Create the job.

```
BEGIN
DBMS_SCHEDULER.CREATE_PROGRAM(
program_name => 'CALC_STATS',
program_action => 'HR.UPDATE_HR_SCHEMA_STATS',
program_type => 'STORED_PROCEDURE',
enabled => TRUE);
END;
/

BEGIN
DBMS_SCHEDULER.CREATE_SCHEDULE(
schedule_name => 'stats_schedule',
start_date => SYSTIMESTAMP,
repeat_interval => 'FREQ=HOURLY;INTERVAL=1',
comments => 'Every hour');
END;
/

BEGIN
DBMS_SCHEDULER.CREATE_JOB (
job_name => 'my_new_job3',
program_name => 'my_saved_program1',
schedule_name => 'my_saved_schedule1');
END;
/
```

Create a job without a program or a schedule:
+  `job_type: EXECUTABLE` — The job runs as an external script.
+  `job_action` — Defines the location of the external script.
+  `start_date` — Defines when the job will be turned on.
+  `repeat_interval` — Defines when the job will run. In the following example, the job runs every day at 23:00.

```
BEGIN
DBMS_SCHEDULER.CREATE_JOB(
job_name=>'HR. BACKUP',
job_type => 'EXECUTABLE',
job_action => '/home/usr/dba/rman/nightly_bck.sh',
start_date=> SYSDATE,
repeat_interval=>'FREQ=DAILY;BYHOUR=23',
comments => 'Nightly backups');
END;
/
```

After you created the job, you can update its attributes with the `SET_ATTRIBUTE` procedure.

```
BEGIN
DBMS_SCHEDULER.SET_ATTRIBUTE (
name => 'my_emp_job1',
attribute => 'repeat_interval',
value => 'FREQ=DAILY');
END;
/
```

### Event-based jobs
<a name="chap-oracle-aurora-mysql.special.scheduler.oracle.eventbased"></a>

The following example demonstrates how to create a schedule to start a job whenever the scheduler receives an event indicating a file arrived on the system before 9:00, and then create a job to use the schedule.

```
BEGIN
DBMS_SCHEDULER.CREATE_EVENT_SCHEDULE (
schedule_name => 'scott.file_arrival',
start_date => systimestamp,
event_condition => 'tab.user_data.object_owner = ''SCOTT''
and tab.user_data.event_name = ''FILE_ARRIVAL''
and extract hour from tab.user_data.event_timestamp < 9',
queue_spec => 'my_events_q');
END;
/

BEGIN
DBMS_SCHEDULER.CREATE_JOB (
job_name => my_job,
program_name => my_program,
start_date => '15-JUL-04 1.00.00AM US/Pacific',
event_condition => 'tab.user_data.event_name = ''LOW_INVENTORY''',
queue_spec => 'my_events_q'
enabled => TRUE,
comments => 'my event-based job');
END;
/
```

### Dependency jobs
<a name="chap-oracle-aurora-mysql.special.scheduler.oracle.dependency"></a>

1. Use `DBMS_SCHEDULER.CREATE_CHAIN` to create a chain.

1. Use` DBMS\_SCHEDULER.DEFINE\_CHAIN\_STEP` to define three steps for this chain. Referenced programs must be enabled.

1. Use `DBMS_SCHEDULER.DEFINE_CHAIN_RULE` to define corresponding rules for the chain.

1. Use `DBMS_SCHEDULER.ENABLE` to enable the chain.

1. Use `DBMS_SCHEDULER.CREATE_JOB` to create a chain job to start the chain daily at 1:00 p.m.

```
BEGIN
DBMS_SCHEDULER.CREATE_CHAIN (
chain_name => 'my_chain1',
rule_set_name => NULL,
evaluation_interval => NULL,
comments => NULL);
END;
/

BEGIN
DBMS_SCHEDULER.DEFINE_CHAIN_STEP('my_chain1', 'stepA', 'my_program1');
DBMS_SCHEDULER.DEFINE_CHAIN_STEP('my_chain1', 'stepB', 'my_program2');
DBMS_SCHEDULER.DEFINE_CHAIN_STEP('my_chain1', 'stepC', 'my_program3');
END;
/

BEGIN
DBMS_SCHEDULER.DEFINE_CHAIN_RULE ('my_chain1', 'TRUE', 'START stepA');
DBMS_SCHEDULER.DEFINE_CHAIN_RULE (
'my_chain1', 'stepA COMPLETED', 'Start stepB, stepC');
DBMS_SCHEDULER.DEFINE_CHAIN_RULE (
'my_chain1', 'stepB COMPLETED AND stepC COMPLETED', 'END');
END;
/

BEGIN
DBMS_SCHEDULER.ENABLE('my_chain1');
END;
/

BEGIN
DBMS_SCHEDULER.CREATE_JOB (
job_name => 'chain_job_1',
job_type => 'CHAIN',
job_action => 'my_chain1',
repeat_interval => 'freq=daily;byhour=13;byminute=0;bysecond=0',
enabled => TRUE);
END;
/
```

There are two additional objects associated with jobs.
+  `JOB CLASS` — When you have a number of jobs that has the same behavior and attributes, you may want to group them together into a bigger logical group called job class and you can give priority between job classes by allocating a high percentage of available resources.
+  `WINDOW` — When you want to prioritize your jobs based on schedule, you can create a window of time that the jobs can run during this window, for example, during non-peak time or at the end of the month.

For more information, see [Scheduling Jobs with Oracle Scheduler](https://docs.oracle.com/en/database/oracle/oracle-database/19/admin/scheduling-jobs-with-oracle-scheduler.html#GUID-D41660D0-D88F-4D9F-8CC8-63D040EDC4E6) in the *Oracle documentation*.

## MySQL usage
<a name="chap-oracle-aurora-mysql.special.scheduler.mysql"></a>

Aurora MySQL can use the `EVENT` objects to run scheduled events in the database. It can run a one-time event or a repeated event. In this case, it’s called cycled. A repeated event is a time-based trigger that runs SQL, runs commands, or calls a procedure.

To use this feature, make sure that the `event_scheduler` parameter in set to `ON`. This isn’t the default value.

If an `EVENT` terminates with errors, it is written to the error log. If there is a need to simulate the `dba_scheduler_job_log`, you can define the error log to use `TABLE` as the output.

For more information, see [Oracle Alert Log and MySQL Error Log](chap-oracle-aurora-mysql.configuration.logs.md).

### Examples
<a name="chap-oracle-aurora-mysql.special.scheduler.mysql.examples"></a>

Check that the event scheduler process is turned on.

```
select @@GLOBAL.event_scheduler
```

View all events.

```
select * from INFORMATION_SCHEMA.EVENTS;
```

Create a new event that runs a procedure every minute.

```
CREATE EVENT event_exec_myproc ON SCHEDULE EVERY 1 MINUTE
  DO CALL simpleproc1(5);
```

## Summary
<a name="chap-oracle-aurora-mysql.special.scheduler.summary"></a>


| Description | Oracle Scheduler | MySQL Events | 
| --- | --- | --- | 
| Create a job that runs as a stored procedure |  <pre>BEGIN<br />DBMS_SCHEDULER.CREATE_PROGRAM(<br />  program_name => 'CALC_STATS',<br />  program_action => 'HR.UPDATE_HR_SCHEMA_STATS',<br />  program_type => 'STORED_PROCEDURE',<br />  enabled => TRUE);<br />END;<br />/<br /><br />BEGIN<br />DBMS_SCHEDULER.CREATE_SCHEDULE(<br />  schedule_name => 'stats_schedule',<br />  start_date => SYSTIMESTAMP,<br />  repeat_interval => 'FREQQ=HOURLY;INTERVAL=1',<br />  comments => 'Every hour');<br />END;<br />/<br /><br />BEGIN<br />DBMS_SCHEDULER.CREATE_JOB (<br />  job_name => 'my_new_job3',<br />  program_name => 'my_saved_program1',<br />  schedule_name => 'my_saved_schedule1');<br />END;<br />/</pre>  |  <pre>CREATE EVENT stats_schedule<br />  ON SCHEDULE EVERY 1 HOUR<br />  DO CALL HR.UPDATE_HR_SCHEMA_STATS();</pre>  | 
| Create a job that runs external executables |  <pre>BEGIN<br />DBMS_SCHEDULER.CREATE_PROGRAM (<br />  program_name => 'oe.my_saved_program1',<br />  program_action => '/usr/local/bin/date',<br />  program_type => 'EXECUTABLE',<br />  comments => 'My comments here');<br />END;<br />/</pre>  | Use the following code to run an AWS Lambda function:<pre>CALL mysql.lambda_async(<br />  'arn:aws:lambda:us-west-2:123456789012:function:oe.my_saved_program1',<br />  '{"input1":"value"}')</pre><br />For more information, see [Invoking a Lambda function from an Amazon Aurora MySQL DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.Lambda.html) in the *User Guide for Aurora*.<br />The `lambda_async` function runs a Lambda function and gets a JSON object for the input values. | 
| Create an event-based job |  <pre>BEGIN<br />DBMS_SCHEDULER.CREATE_EVENT_SCHEDULE (<br />  schedule_name => 'scott.file_arrival',<br />  start_date => systimestamp,<br />  event_condition => 'tab.user_data.object_owner = ''SCOTT''<br />    and tab.user_data.event_name = ''FILE_ARRIVAL''<br />    and extract hour from tab.user_data.event_timestamp < 9',<br />     queue_spec => 'my_events_q');<br />END;<br />/<br /><br />BEGIN<br />DBMS_SCHEDULER.CREATE_JOB (<br />  job_name => my_job,<br />  program_name => my_program,<br />  start_date => '15-JUL-04 1.00.00AM US/Pacific',<br />  event_condition => 'tab.user_data.event_name = ''LOW_INVENTORY''',<br />  queue_spec => 'my_events_q' enabled => TRUE,<br />  comments => 'my event-based job');<br />END;<br />/</pre>  | For the `CREATE EVENT` syntax, only time intervals can be defined as triggers for the event.<br />If an event job is required, the best alternatives are:1.  Create triggers to run the commands (for DML events). <br />2.  Create an `EVENT` that runs every `X` time and check if the event occurred. The minimum interval is one second.  | 
| Create a chained job |  <pre>BEGIN<br />DBMS_SCHEDULER.CREATE_CHAIN (<br />  chain_name => 'my_chain1',<br />  rule_set_name => NULL,<br />  evaluation_interval => NULL,<br />  comments => NULL);<br />END;<br />/<br /><br />BEGIN<br />DBMS_SCHEDULER.DEFINE_CHAIN_STEP (<br />  'my_chain1', 'stepA', 'my_program1');<br />DBMS_SCHEDULER.DEFINE_CHAIN_STEP (<br />  'my_chain1', 'stepB', 'my_program2');<br />DBMS_SCHEDULER.DEFINE_CHAIN_STEP (<br />  'my_chain1', 'stepC', 'my_program3');<br />END;<br />/<br /><br />BEGIN<br />DBMS_SCHEDULER.DEFINE_CHAIN_RULE (<br />  'my_chain1', 'TRUE', 'START stepA');<br />DBMS_SCHEDULER.DEFINE_CHAIN_RULE (<br />  'my_chain1', 'stepA COMPLETED',<br />  'Start stepB, stepC');<br />DBMS_SCHEDULER.DEFINE_CHAIN_RULE (<br />  'my_chain1',<br />  'stepB COMPLETED AND stepC COMPLETED',<br />  'END');<br />END;<br />/<br /><br />BEGIN<br />DBMS_SCHEDULER.ENABLE('my_chain1');<br />END;<br />/<br /><br />BEGIN<br />DBMS_SCHEDULER.CREATE_JOB (<br />  job_name => 'chain_job_1',<br />  job_type => 'CHAIN',<br />  job_action => 'my_chain1',<br />  repeat_interval => 'freq=daily;<br />    byhour=13;<br />    byminute=0;<br />    bysecond=0',<br />  enabled => TRUE);<br />END;<br />/</pre>  | Create several `EVENTS` and manage them within a table to keep the results, or the last run status to determine when to execute the next event. | 

For more information, see [Using the Event Scheduler](https://dev.mysql.com/doc/refman/5.7/en/event-scheduler.html) and [Event Syntax](https://dev.mysql.com/doc/refman/5.7/en/events-syntax.html) in the *MySQL documentation*.