# Oracle DBMS_SCHEDULER and PostgreSQL scheduled Lambda

With AWS DMS, you can schedule and automate database tasks using Oracle DBMS_SCHEDULER and PostgreSQL scheduled Lambda. Oracle DBMS_SCHEDULER is a job scheduler that allows defining and executing recurring or one-time jobs. PostgreSQL scheduled Lambda lets you invoke AWS Lambda functions on a schedule.

| Feature compatibility          | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences |
| ------------------------------ | ---------------------------------- | ------------------------- | --------------- |
| One star feature compatibility | No automation                      | N/A                       | N/A             |

## Oracle usage

The DBMS_SCHEDULER package contains a collection of scheduling functions the can be executed or called from PL/DSQL, Create a job and attributes.

When creating a job there two main objects that should be created too: `PROGRAM` and `SCHEDULE`.

A program will define what will run when the job called it.

Scheduler can run database program unit (for example, a procedure) or external executable (filesystem sh scripts, and so on).

There are three running methods of jobs: Time Base Scheduling, Event-Based jobs, and Dependency Jobs (Chained).

**Time base scheduling**

Examples of the commands that will create a job with program and schedule:

1. Create a program that will call the procedure `UPDATE_HR_SCHEMA_STATS` in `HR` schema.
2. Create a schedule that will set the interval of running the jobs that using it. This schedule will run the job every 1 hour.
3. Create the job itself.

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

Create a job without program or schedule:

1. `job_type` — `EXECUTABLE` define that our job will run an external script.
2. `job_action` — Define the location of the external script.
3. `start_date` — Define since when the job will be enabled.
4. `repeat_interval` — Define when the job will run, in this example every day at huor 23 (11:00PM).

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

After the job is created, its attribute can be updated with `SET_ATTRIBUTE` procedure.

```
BEGIN
DBMS_SCHEDULER.SET_ATTRIBUTE (
name => 'my_emp_job1',
attribute => 'repeat_interval',
value => 'FREQ=DAILY');
END;
/
```

**Event-based jobs**

Example of creating a schedule that can be used to start a job whenever the scheduler receives an event indicating that a file arrived on the system before 9AM and then create a job that will use this schedule

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

**Dependency jobs (Chained)**

1. Use `DBMS_SCHEDULER.CREATE_CHAIN` to create a chain.
2. Use` DBMS\_SCHEDULER.DEFINE\_CHAIN\_STEP` to define three steps for this chain. Referenced programs must be enabled.
3. Use `DBMS_SCHEDULER.DEFINE_CHAIN_RULE` to define corresponding rules for the chain.
4. Use `DBMS_SCHEDULER.ENABLE` to enable the chain.
5. Use `DBMS_SCHEDULER.CREATE_JOB` to create a chain job to start the chain daily at 1:00 p.m.

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

There are two additional subjects to maintain your jobs.

1. `JOB CLASS` — when you have a number of jobs that has the same behavior and attributes, maybe you will want to group them together into bigger logical group called “Job Class” and you can give priority between job classes by allocating a high percentage of available resources.
2. `WINDOW` — when you want to prioritize your jobs based on schedule, you can create a window of time that the jobs can run during this window, for example, during non-peak time or at the end of the month.

For more information, see [Scheduling Jobs with Oracle Scheduler](https://docs.oracle.com/en/database/oracle/oracle-database/19/admin/scheduling-jobs-with-oracle-scheduler.html#GUID-D41660D0-D88F-4D9F-8CC8-63D040EDC4E6 "https://docs.oracle.com/en/database/oracle/oracle-database/19/admin/scheduling-jobs-with-oracle-scheduler.html#GUID-D41660D0-D88F-4D9F-8CC8-63D040EDC4E6") in the _Oracle documentation_.

## PostgreSQL usage

Aurora PostgreSQL can be combined with Amazon CloudWatch and Lambda to get similar functionality, see [Sending an Email from Aurora PostgreSQL using Lambda Integration](chap-oracle-aurora-pg.sql.md#chap-oracle-aurora-pg.sql.mail.pg "chap-oracle-aurora-pg.sql.md#chap-oracle-aurora-pg.sql.mail.pg").
