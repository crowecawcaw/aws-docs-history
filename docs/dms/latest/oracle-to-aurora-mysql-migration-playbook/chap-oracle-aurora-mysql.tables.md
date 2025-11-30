# Oracle and MySQL triggers

Triggers are database objects that encapsulate procedural logic, facilitating data validation, auditing, and maintaining referential integrity constraints. System administrators, database developers, and data engineers may require triggers to enforce business rules, log data changes, or propagate updates across related tables. The following sections provide detailed guidance on creating, managing, and testing triggers within the context of AWS DMS.

| Feature compatibility            | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                                                                                             |
| -------------------------------- | ---------------------------------- | ------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Three star feature compatibility | Three star automation level        |                           | MySQL doesn’t support statement and system event triggers. Also, MySQL doesn’t support `CREATE OR REPLACE`. |

## Oracle usage

A trigger is a named program that is stored in the database and fired when a specified event occurs. The associated event causing a trigger to run can either be tied to a specific database table, database view, database schema, or the database itself.

Triggers can be run after:

- Data Manipulation Language (DML) statements such as `DELETE`, `INSERT`, or `UPDATE`.
- Data Definition Language (DDL) statements such as `CREATE`, `ALTER`, or `DROP`.
- Database events and operations such as `SERVERERROR`, `LOGON`, `LOGOFF`, `STARTUP`, or `SHUTDOWN`.

### Trigger types

- **DML** triggers can be created on tables or views and fire when inserting, updating, or deleting data. Triggers can fire before or after DML command run.
- **INSTEAD OF** triggers can be created on a non-editable view. `INSTEAD OF` triggers provide an application-transparent method for modifying views that can’t be modified by DML statements.
- **SYSTEM event** triggers are defined at the database or schema level including triggers that fire after specific events:
  - User log-on and log-off.
  - Database events such as startup or shutdown, DataGuard events, server errors.

### Examples

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

Create a `SYSTEM` or schema trigger on a table. The trigger fires if a `DDL DROP` command runs for an object in the `HR` schema. It prevents dropping the object and raises an application error.

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

## MySQL usage

MySQL supports triggers, but not all of the functionality provided by Oracle. Triggers are associated with users for privileges reasons and with specific tables. Triggers fire at the row level, and not at the statement level. You can modify MySQL triggers using a `FOLLOWS` or `PRECEDES` clause. Also, MySQL triggers can be chained using the `FOLLOWS` or `PRECEDES` clauses.

### Syntax

```
CREATE
[DEFINER = { user | CURRENT_USER }]
TRIGGER trigger_name
trigger_time trigger_event
ON tbl_name FOR EACH ROW
[trigger_order]
trigger_body
trigger_time: { BEFORE | AFTER }
trigger_event: { INSERT | UPDATE | DELETE }
trigger_order: { FOLLOWS | PRECEDES } other_trigger_name
```

### Examples

Create a trigger referencing the `OLD` and `NEW` values.

```
set delimiter /
CREATE OR REPLACE TRIGGER PROJECTS_SET_NULL
BEFORE UPDATE ON PROJECTS
FOR EACH ROW
BEGIN
IF OLD.PROJECTNO != NEW.PROJECTNO THEN
UPDATE EMP SET EMP.PROJECTNO = NULL
WHERE EMP.PROJECTNO = OLD.PROJECTNO;
END IF;
END;
/
set delimiter ;
UPDATE PROJECTS WHERE PROJECTNO=123;
SELECT PROJECTNO FROM EMP WHERE PROJECTNO=123;
PROJECTNO
----------
NULL
```

Drop a trigger.

```
DROP TRIGGER PROJECTS_SET_NULL
```

## Summary

| Trigger                                      | Oracle                                                                                                                                                                                                                                                                       | MySQL                                                                                                                                                                                                                |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Before update trigger, row level             | `<br>CREATE OR REPLACE TRIGGER check_update<br>BEFORE UPDATE ON projects<br>FOR EACH ROW<br>BEGIN<br>/*Trigger body*/<br>END;<br>/<br>`                                                                                                                                      | `<br>CCREATE TRIGGER check_update<br>BEFORE UPDATE ON projects<br>FOR EACH ROW<br>BEGIN<br>/*Trigger body*/<br>END;<br>/<br>`                                                                                        |
| Before update trigger, statement level       | `<br>CREATE OR REPLACE TRIGGER check_update<br>BEFORE UPDATE ON projects<br>BEGIN<br>/*Trigger body*/<br>END;<br>/<br>`                                                                                                                                                      | Not supported                                                                                                                                                                                                        |
| System or event trigger                      | `<br>CREATE OR REPLACE TRIGGER drop_trigger<br>BEFORE DROP ON hr.SCHEMA<br>BEGIN<br>RAISE_APPLICATION_ERROR (<br>num => -20000,<br>msg => 'Cannot drop object');<br>END;<br>/<br>`                                                                                           | Not supported                                                                                                                                                                                                        |
| Referencing :old and :new values in triggers | Use `:NEW` and `:OLD` in trigger body:<br>`<br>CREATE OR REPLACE TRIGGER Upper-NewDeleteOld<br>BEFORE INSERT OR UPDATE<br>OF first_name ON employees<br>FOR EACH ROW<br>BEGIN<br>:NEW.first_name := UPPER(:NEW.first_name);<br>:NEW.salary := :OLD.salary;<br>END;<br>/<br>` | Use `NEW` and `OLD` in trigger body:<br>`<br>CREATE TRIGGER UpperNewDeleteOld<br>BEFORE UPDATE ON empys<br>FOR EACH ROW SET<br>NEW.first_name = UPPER(NEW.first_name),<br>NEW.salary = OLD.salary;<br>END;<br>/<br>` |
| Database event level trigger                 | `<br>CREATE TRIGGER register_shutdown<br>ON DATABASE SHUTDOWN<br>BEGIN<br>Insert into logging values<br>('DB was shut down', sysdate);<br>commit;<br>END;<br>/<br>`                                                                                                          | Not supported                                                                                                                                                                                                        |
| Drop a trigger                               | `<br>DROP TRIGGER last_name_change_trg;<br>`                                                                                                                                                                                                                                 | `<br>DROP TRIGGER last_name_change_trg;<br>`                                                                                                                                                                         |
| Modify logic run by a trigger                | Can be used with create or replace<br>`<br>CREATE OR REPLACE TRIGGER<br>UpperNewDeleteOld<br>BEFORE INSERT OR UPDATE OF<br>first_name ON employees<br>FOR EACH ROW<br>BEGIN<br><<NEW CONTENT>><br>END;<br>/<br>`                                                             | Not supported                                                                                                                                                                                                        |
| Enable a trigger                             | `<br>ALTER TRIGGER UpperNewDeleteOld<br>ENABLE;<br>`                                                                                                                                                                                                                         | Not supported. Can be achieved by setting variables for each trigger to determine if it is turned off or turned on, and then checking the variable in an `IF` statement.                                             |
| Disable a trigger                            | `<br>ALTER TRIGGER UpperNewDeleteOld<br>DISABLE;<br>`                                                                                                                                                                                                                        | Not supported. Can be achieved by setting variables for each trigger to determine if it is turned off or turned on, and then checking the variable in an `IF` statement.                                             |

For more information, see [Trigger Syntax and Examples](https://dev.mysql.com/doc/refman/5.7/en/trigger-syntax.html "https://dev.mysql.com/doc/refman/5.7/en/trigger-syntax.html") and [CREATE TRIGGER Statement](https://dev.mysql.com/doc/refman/5.7/en/create-trigger.html "https://dev.mysql.com/doc/refman/5.7/en/create-trigger.html") in the _MySQL documentation_.
