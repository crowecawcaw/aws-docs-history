# Oracle triggers and PostgreSQL trigger procedure

With AWS DMS, you can migrate databases to AWS while replicating database code objects, such as triggers across source and target databases. Triggers are database objects that automatically run a defined procedure when an event occurs, such as inserting, updating, or deleting data in a table. Oracle triggers and PostgreSQL trigger procedures define the logic and actions to be performed when specific events occur in the database.

| Feature compatibility           | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                                   | Key differences                                                                |
| ------------------------------- | ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| Four star feature compatibility | Three star automation level        | [Triggers](chap-oracle-aurora-pg.tools.md#chap-oracle-aurora-pg.tools.actioncode.triggers "chap-oracle-aurora-pg.tools.md#chap-oracle-aurora-pg.tools.actioncode.triggers") | Different paradigm and syntax. System triggers aren’t supported by PostgreSQL. |

## Oracle usage

A trigger is a procedure that is stored in the database and fired when a specified event occurs. The associated event causing a trigger to run can either be tied to a specific database table, database view, database schema, or the database itself.

Triggers can be run after:

- Data Manipulation Language (DML) statements such as `DELETE`, `INSERT`, or `UPDATE`.
- Data Definition Language (DDL) statements such as `CREATE`, `ALTER`, or `DROP`.
- Database events and operations such as `SERVERERROR`, `LOGON`, `LOGOFF`, `STARTUP`, or `SHUTDOWN`.

### Trigger types

- **DML** triggers can be created on tables or views and fire when inserting, updating, or deleting data. Triggers can fire before or after DML command run.
- **INSTEAD OF** triggers can be created on a non-editable view. `INSTEAD OF` triggers provide an application-transparent method for modifying views that can’t be modified by DML statements.
- **SYSTEM Event** triggers are defined at the database or schema level including triggers that fire after specific events:
  - User log-on and log-off.
  - Database events (startup/shutdown), DataGuard events, server errors.

**Examples**

Create a trigger that runs after a row is deleted from the `PROJECTS` table, or if the primary key of a project is updated.

```
CREATE OR REPLACE TRIGGER PROJECTS_SET_NULL
  AFTER DELETE OR UPDATE OF PROJECTNO ON PROJECTS
  FOR EACH ROW
  BEGIN
    IF UPDATING AND :OLD.PROJECTNO != :NEW.PROJECTNO OR DELETING THEN
      UPDATE EMP SET EMP.PROJECTNO = NULL
      WHERE EMP.PROJECTNO = :OLD.PROJECTNO;
    END IF;
END;
/

Trigger created.

DELETE FROM PROJECTS WHERE PROJECTNO=123;

SELECT PROJECTNO FROM EMP WHERE PROJECTNO=123;

PROJECTNO
NULL
```

Create a SYSTEM/Schema trigger on a table. The trigger fires if a `DDL DROP` command runs for an object in the `HR` schema. It prevents dropping the object and raises an application error.

```
CREATE OR REPLACE TRIGGER PREVENT_DROP_TRIGGER
  BEFORE DROP ON HR.SCHEMA
  BEGIN
    RAISE_APPLICATION_ERROR (num => -20000,
    msg => 'Cannot drop object');
END;
/

Trigger created.

DROP TABLE HR.EMP

ERROR at line 1:
ORA-00604: error occurred at recursive SQL level 1
ORA-20000: Cannot drop object
ORA-06512: at line 2
```

For more information, see [CREATE TRIGGER Statement](https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/CREATE-TRIGGER-statement.html#GUID-AF9E33F1-64D1-4382-A6A4-EC33C36F237B "https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/CREATE-TRIGGER-statement.html#GUID-AF9E33F1-64D1-4382-A6A4-EC33C36F237B") in the _Oracle documentation_.

## PostgreSQL usage

A trigger is a procedure that is stored in the database and fired when a specified event occurs. DML triggers in PostgreSQL share much of the functionality that exists in Oracle triggers.

- DML triggers (triggers that fire based on table related events such as DML).
- Event triggers (triggers that fire after certain database events such as running DDL commands).

Unlike Oracle triggers, PostgreSQL triggers must call a function and don’t support anonymous blocks of PL/pgSQL code as part of the trigger body. The user-supplied function is declared with no arguments and has a return type of trigger.

**PostgreSQL CREATE TRIGGER synopsis**

```
CREATE [ CONSTRAINT ] TRIGGER name { BEFORE | AFTER | INSTEAD OF } { event [ OR ... ]}
  ON table_name
  [ FROM referenced_table_name ]
  [ NOT DEFERRABLE | [ DEFERRABLE ] [ INITIALLY IMMEDIATE | INITIALLY DEFERRED ] ]
  [ REFERENCING { { OLD | NEW } TABLE [ AS ] transition_relation_name } [ ... ] ]
  [ FOR [ EACH ] { ROW | STATEMENT } ]
  [ WHEN ( condition ) ]
  EXECUTE PROCEDURE function_name ( arguments )

where event can be one of:
  INSERT
  UPDATE [ OF column_name [, ... ] ]
  DELETE
  TRUNCATE
```

###### Note

REFERENCING is a new option introduced in PostgreSQL 10. You can use this option with the `AFTER` trigger to interact with the overall view of the `OLD` or the `NEW TABLE` changed rows.

There are some cases that can fire multiple triggers numerous times. This includes triggers that aren’t planned to run, such as:

- An `INSERT` with an `ON CONFLICT DO UPDATE` clause may cause both insert and update operations to fire.
- `UPDATE` or `DELETE` caused by foreign-key enforcement can fire triggers. For example, `ON UPDATE CASCADE` or `ON DELETE SET NULL` can fire triggers that are supposed to fire on `UPDATE` or `DELETE` commands on the table.

### PostgreSQL DML triggers

PostgreSQL triggers can run `BEFORE` or `AFTER` a DML operation.

- Fire before the operation is attempted on a row.
  - Before constraints are checked and the `INSERT`, `UPDATE`, or `DELETE` is attempted.
  - If the trigger fires before or instead of the event, the trigger can skip the operation for the current row or change the row being inserted (for `INSERT` and `UPDATE` operations only).

- After the operation was completed, after constraints are checked and the `INSERT`, `UPDATE`, or `DELETE` command completed. If the trigger fires after the event, all changes, including the effects of other triggers, are visible to the trigger.

PostgreSQL triggers can run `INSTEAD OF` a DML command when created on views.

PostgreSQL triggers can run `FOR EACH ROW` affected by the DML statement or `FOR EACH STATEMENT` running only once as part of a DML statement.

| When fired | Database event         | Row-level trigger         | Statement-level trigger           |
| ---------- | ---------------------- | ------------------------- | --------------------------------- |
| BEFORE     | INSERT, UPDATE, DELETE | Tables and foreign tables | Tables, views, and foreign tables |
| BEFORE     | TRUNCATE               | N/A                       | Tables                            |
| AFTER      | INSERT, UPDATE, DELETE | Tables and foreign tables | Tables, views, and foreign tables |
| AFTER      | TRUNCATE               | N/A                       | Tables                            |
| INSTEAD OF | INSERT, UPDATE, DELETE | Views                     | N/A                               |
| INSTEAD OF | TRUNCATE               | N/A                       | N/A                               |

### PostgreSQL event triggers

An event trigger runs when a specific event that is associated with the trigger occurs in the database. Supported events include: `ddl_command_start`, `ddl_command_end`, `table_rewrite` and `sql_drop`.

- `ddl_command_start` occurs before the run of a `CREATE`, `ALTER`, `DROP`, `SECURITY LABEL`, `COMMENT`, `GRANT`, `REVOKE`, or `SELECT INTO` command.
- `ddl_command_end` occurs after the command completed and before the transaction commits.
- `sql_drop` fired only for the DROP DDL command. Fires before `ddl_command_end` trigger fire.

For more information, see [Event Trigger Firing Matrix](https://www.postgresql.org/docs/13/event-trigger-matrix.html "https://www.postgresql.org/docs/13/event-trigger-matrix.html") in the _PostgreSQL documentation_.

**Examples**

Create a DML trigger. To create an equivalent version of the Oracle DML trigger in PostgreSQL, first create a function trigger which will store the run logic for the trigger.

```
CREATE OR REPLACE FUNCTION PROJECTS_SET_NULL()
  RETURNS TRIGGER
  AS $$
  BEGIN
  IF TG_OP = 'UPDATE' AND OLD.PROJECTNO != NEW.PROJECTNO OR
  TG_OP = 'DELETE' THEN
  UPDATE EMP
    SET PROJECTNO = NULL
    WHERE EMP.PROJECTNO = OLD.PROJECTNO;
    END IF;

    IF TG_OP = 'UPDATE' THEN RETURN NULL;
      ELSIF TG_OP = 'DELETE' THEN RETURN NULL;
      END IF;
  END; $$
LANGUAGE PLPGSQL;
```

Create the trigger.

```
CREATE TRIGGER TRG_PROJECTS_SET_NULL
  AFTER UPDATE OF PROJECTNO OR DELETE
  ON PROJECTS
  FOR EACH ROW
  EXECUTE PROCEDURE PROJECTS_SET_NULL();

CREATE TRIGGER
```

Test the trigger by deleting a row from the PROJECTS table.

```
DELETE FROM PROJECTS WHERE PROJECTNO=123;
SELECT PROJECTNO FROM EMP WHERE PROJECTNO=123;

projectno
(0 rows)
```

Create a DDL trigger that is an equivalent version of the Oracle DDL System/Schema level triggers (such as a trigger that prevent running a DDL DROP on objects in the HR schema).

Create an event trigger function.

Note that trigger functions are created with no arguments and must have a return type of `TRIGGER` or `EVENT_TRIGGER`.

```
CREATE OR REPLACE FUNCTION ABORT_DROP_COMMAND()
    RETURNS EVENT_TRIGGER
    AS $$
  BEGIN
    RAISE EXCEPTION 'The % Command is Disabled', tg_tag;
  END; $$
  LANGUAGE PLPGSQL;

CREATE FUNCTION
```

Create the event trigger, which will fire before the start of a DDL DROP command.

```
CREATE EVENT TRIGGER trg_abort_drop_command
  ON DDL_COMMAND_START
  WHEN TAG IN ('DROP TABLE', 'DROP VIEW',
    'DROP FUNCTION', 'DROP SEQUENCE',
    'DROP MATERIALIZED VIEW', 'DROP TYPE')
  EXECUTE PROCEDURE abort_drop_command();
```

Test the trigger by attempting to drop the EMPLOYEES table.

```
DROP TABLE EMPLOYEES;

ERROR: The DROP TABLE Command is Disabled
CONTEXT: PL/pgSQL function abort_drop_command() line 3 at RAISE
```

## Summary

| Trigger                                      | Oracle                                                                                                                                                                                                                                                                          | PostgreSQL                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Before update trigger, row level             | `<br>CREATE OR REPLACE TRIGGER check_update<br>BEFORE UPDATE ON projects<br>FOR EACH ROW<br>BEGIN<br>/*Trigger body*/<br>END;<br>/<br>`                                                                                                                                         | `<br>CREATE TRIGGER check_update<br>BEFORE UPDATE ON employees<br>FOR EACH ROW<br>EXECUTE PROCEDURE myproc();<br>`                                                                                                                                                                                                                                                                                                                                                                                             |
| Before update trigger, statement level       | `<br>CREATE OR REPLACE TRIGGER check_update<br>BEFORE UPDATE ON projects<br>BEGIN<br>/*Trigger body*/<br>END;<br>/<br>`                                                                                                                                                         | `<br>CREATE TRIGGER check_update<br>BEFORE UPDATE ON employees<br>FOR EACH STATEMENT<br>EXECUTE PROCEDURE myproc();<br>`                                                                                                                                                                                                                                                                                                                                                                                       |
| System / event trigger                       | `<br>CREATE OR REPLACE TRIGGER drop_trigger<br>BEFORE DROP ON hr.SCHEMA<br>BEGIN<br>RAISE_APPLICATION_ERROR (<br>num => -20000,<br>msg => 'Cannot drop object');<br>END;<br>/<br>`                                                                                              | `<br>CREATE EVENT TRIGGER trg_drops<br>ON ddl_command_start<br>EXECUTE PROCEDURE trg_drops();<br>`                                                                                                                                                                                                                                                                                                                                                                                                             |
| Referencing :old and :new values in triggers | Use ":NEW" and ":OLD" in trigger body:<br>`<br>CREATE OR REPLACE TRIGGER Upper-NewDeleteOld<br>BEFORE INSERT OR UPDATE<br>OF first_name ON employees<br>FOR EACH ROW<br>BEGIN<br>:NEW.first_name :=<br>UPPER(:NEW.first_name);<br>:NEW.salary := :OLD.salary;<br>END;<br>/<br>` | Use ".NEW" and ".OLD" in trigger procedure body:<br>`<br>CREATE OR REPLACE FUNCTION<br>log_ emp_name_upd()<br>RETURNS trigger<br>LANGUAGE plpgsql<br>AS $$<br>BEGIN<br>IF NEW.last_name <> OLD.last_name<br>THEN<br>INSERT INTO employee_audit (employee_<br>id,last_name,changed_on) VALUES<br>(OLD.id,OLD.last_name,now());<br>END IF;<br>RETURN NEW;<br>END;<br>$$<br>CREATE TRIGGER last_name_change_trg<br>BEFORE UPDATE ON employees FOR<br>EACH ROW EXECUTE PROCEDURE log_<br>last_emp_name_upd();<br>` |
| Database event level trigger                 | `<br>CREATE TRIGGER register_shutdown<br>ON DATABASE SHUTDOWN<br>BEGIN<br>Insert into logging values<br>('DB was shut down', sysdate);<br>commit;<br>END;<br>/<br>`                                                                                                             | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Drop a trigger                               | `<br>DROP TRIGGER last_name_change_trg;<br>`                                                                                                                                                                                                                                    | `<br>DROP TRIGGER last_name_change_trg on employees;<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Modify logic run by a trigger                | Can be used with create or replace<br>`<br>CREATE OR REPLACE TRIGGER<br>UpperNewDeleteOld<br>BEFORE INSERT OR UPDATE OF<br>first_name ON employees<br>FOR EACH ROW<br>BEGIN<br><<NEW CONTENT>><br>END;<br>/<br>`                                                                | Use CREATE OR REPLACE on the called function in the trigger (trigger stay the same)<br>`<br>CREATE or replace FUNCTION<br>UpperNewDeleteOld() RETURNS<br>trigger AS<br>$UpperNewDeleteOld$<br>BEGIN<br><<NEW CONTENT>><br>END;<br>$UpperNewDeleteOld$<br>LANGUAGE plpgsql;<br>`                                                                                                                                                                                                                                |
| Enable a trigger                             | `<br>ALTER TRIGGER UpperNewDeleteOld<br>ENABLE;<br>`                                                                                                                                                                                                                            | `<br>alter table employees enable trigger Upper-NewDeleteOld;<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Disable a trigger                            | `<br>ALTER TRIGGER UpperNewDeleteOld<br>DISABLE;<br>`                                                                                                                                                                                                                           | `<br>alter table employees disable trigger Upper-NewDeleteOld;<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                            |

For more information, see [CREATE TRIGGER](https://www.postgresql.org/docs/13/sql-createtrigger.html "https://www.postgresql.org/docs/13/sql-createtrigger.html") and [Trigger Functions](https://www.postgresql.org/docs/13/plpgsql-trigger.html "https://www.postgresql.org/docs/13/plpgsql-trigger.html") in the _PostgreSQL documentation_.
