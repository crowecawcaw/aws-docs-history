# Step 8: Cut Over to PostgreSQL

To move connections from your Oracle database to your PostgreSQL database, do the following:

1. End all Oracle database dependencies and activities, such as running scripts and client connections.

The following query should return no results:

```
SELECT MACHINE, COUNT(*) FROM V$SESSION GROUP BY MACHINE;
```

2. List any remaining sessions, and kill them.

```
SELECT SID, SERIAL#, STATUS FROM V$SESSION;

ALTER SYSTEM KILL 'sid, serial_number' IMMEDIATE;
```

3. Shut down all listeners on the Oracle database.
4. (Optional) Turn off automated jobs on the Oracle database. For your production database, check that this operation doesn’t influence the business logic.

```
ALTER SYSTEM SET JOB_QUEUE_PROCESSES=0
```

5. (Optional) Turn off time monitoring on queue messages on the Oracle database. For your production database, check that this operation doesn’t influence the business logic.

```
ALTER SYSTEM SET AQ_TM_PROCESSES=0
```

6. Let the AWS DMS task apply the final changes from the Oracle database on the PostgreSQL database.

```
ALTER SYSTEM CHECKPOINT;
```

7. In the AWS DMS console, stop the AWS DMS task by clicking **Stop** for the task, and confirm that you want to stop the task.
8. (Optional) Set up a rollback.

You can optionally set up a rollback task, in case you run into a show stopping issue, by creating a task going in the opposite direction. Because all tables should be in sync between both databases, you only need to set up a CDC task. Therefore, you do not have to disable any foreign key constraints. Now that the source and target databases are reversed, you must follow the instructions in the following sections:

    * [Using a PostgreSQL Database as a Source](../userguide/CHAP_Source.md "../userguide/CHAP_Source.md")
    * [Using an Oracle Database as a Target](../userguide/CHAP_Target.md "../userguide/CHAP_Target.md")





    	1. Disable triggers on the source Oracle database.



    	```
    	SELECT 'ALTER TRIGGER' || owner || '.' || trigger_name || 'DISABLE;'
    	   FROM DBA_TRIGGERS WHERE OWNER = 'schema_name';
    	```

    	You do not have to disable the foreign key constraints. During the CDC process, foreign key constraints are updated in the same order as they are updated by application users.
    	2. Create a new CDC-only AWS DMS task with the endpoints reversed (source PostgreSQL endpoint and target Oracle endpoint database). See [Step 7: Create and Run Your Migration Task](chap-rdsoracle2postgresql.steps.md "chap-rdsoracle2postgresql.steps.md").


    	For the rollback task, set **Migration type** to **Replicate data changes only** and **Target table preparation mode** to **Do nothing**.
    	3. Start the AWS DMS task to enable you to push changes back to the original source Oracle database from the new PostgreSQL database if rollback is necessary.

9. Connect to the PostgreSQL database, and enable triggers.

```
ALTER TABLE table_name ENABLE TRIGGER ALL;
```

10. If you set up a rollback, then complete the rollback setup.
    1.  Start the application services on new target PostgreSQL database (including scripts , client software, and so on).
    2.  Add CloudWatch monitoring on your new PostgreSQL database. For more information, see [Monitoring Amazon RDS](../../../AmazonRDS/latest/UserGuide/CHAP_Monitoring.md "../../../AmazonRDS/latest/UserGuide/CHAP_Monitoring.md").
