# Oracle and MySQL cursors

With AWS DMS, you can efficiently migrate data from Oracle and MySQL databases to other database services or engines, including handling complex data types, such as cursors. A cursor is a database object that allows traversal over rows from a query, facilitating operations like looping through result sets.

| Feature compatibility           | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                                            | Key differences                                                                                                               |
| ------------------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| Four star feature compatibility | Three star automation level        | [Cursors](chap-oracle-aurora-mysql.tools.md#chap-oracle-aurora-mysql.tools.actioncode.cursors "chap-oracle-aurora-mysql.tools.md#chap-oracle-aurora-mysql.tools.actioncode.cursors") | Minor differences in syntax may require some code rewrite. MySQL doesn’t support `%ISOPEN`, `%ROWTYPE`, and `%BULK_ROWCOUNT`. |

## Oracle usage

PL/SQL cursors are pointers to data sets on which application logic can iterate. The data sets hold rows returned by SQL statements. You can refer to the active data set in named cursors from within a program.

There are two types of PL/SQL cursors:

- **Implicit cursors** are session cursors constructed and managed by PL/SQL automatically without being created or defined by a user. PL/SQL opens an implicit cursor each time you run a `SELECT` or DML statement. Implicit cursors are also called SQL cursors.
- **Explicit cursors** are session cursors created, constructed, and managed by a user. Cursors are declared and defined by naming it and associating it with a query. Unlike an implicit cursor, you can reference an explicit cursor using its name. An explicit cursor is called a named cursor.

### Examples

The following examples demonstrate cursor usage:

1. Define an explicit PL/SQL cursor named `c1`.
2. The cursor runs an SQL statement to return rows from the database.
3. The PL/SQL loop reads data from the cursor, row by row, and stores the values into two variables: `v_lastname` and `v_jobid`.
4. The loop uses the `%NOTFOUND` attribute to terminate when the last row is read from the database.

```
DECLARE
  CURSOR c1 IS
    SELECT last_name, job_id FROM employees
    WHERE REGEXP_LIKE (job_id, 'S[HT]_CLERK')
    ORDER BY last_name;
    v_lastname employees.last_name%TYPE; -- variable to store last_name
    v_jobid employees.job_id%TYPE; -- variable to store job_id
  BEGIN
    OPEN c1;
    LOOP -- Fetches 2 columns into variables
      FETCH c1 INTO v_lastname, v_jobid;
      EXIT WHEN c1%NOTFOUND;
    END LOOP;
  CLOSE c1;
END;
```

1. Define an implicit PL/SQL cursor using a `FOR` Loop.
2. The cursor runs a query and stores values returned into a record.
3. A loop iterates over the cursor data set and prints the result.

```
BEGIN
FOR item IN
  (SELECT last_name, job_id FROM employees WHERE job_id LIKE '%MANAGER%'
    AND manager_id > 400 ORDER BY last_name) LOOP
    DBMS_OUTPUT.PUT_LINE('Name = ' || item.last_name || ', Job = ' || item.job_id);
  END LOOP;
END;
/
```

For more information, see [Explicit Cursor Declaration and Definition](https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/explicit-cursor-declaration-and-definition.html#GUID-38C5DBA3-9DEC-4AF2-9B5E-7B721D11A77C "https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/explicit-cursor-declaration-and-definition.html#GUID-38C5DBA3-9DEC-4AF2-9B5E-7B721D11A77C") and [Implicit Cursor Attribute](https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/implicit-cursor-attribute.html#GUID-5A938EE7-E8D2-468C-B60F-81898F110BE1 "https://docs.oracle.com/en/database/oracle/oracle-database/19/lnpls/implicit-cursor-attribute.html#GUID-5A938EE7-E8D2-468C-B60F-81898F110BE1") in the _Oracle documentation_.

## MySQL usage

Aurora MySQL supports cursors only within stored routines, functions and stored procedures.

Unlike Oracle, which offers an array of cursor types, Aurora MySQL Cursors have the following characteristics:

- **Not sensitive** — The server can choose to either make a copy of its result table or to access the source data as the cursor progresses.
- **Read-only** — Cursors can’t be updated.
- **Not scrollable** — Cursors can only be traversed in one direction and cannot skip rows. The only supported cursor advance operation is `FETCH NEXT`.

Cursor declarations must appear before handler declarations and after variable and condition declarations.

Similar to Oracle, cursors are declared with the `DECLARE CURSOR`, opened with `OPEN`, fetched with `FETCH`, and closed with `CLOSE`.

### Declare Cursor

```
DECLARE <Cursor Name> CURSOR FOR <Cursor SELECT Statement>
```

The `DECLARE CURSOR` statement instantiates a cursor object and associates it with a `SELECT` statement. This `SELECT` is then used to retrieve the cursor rows.

To fetch the rows, use the `FETCH` statement. As mentioned before, only `FETCH NEXT` is supported. The number of output variables specified in the `FETCH` statement must match the number of columns retrieved by the cursor.

Aurora MySQL cursors have additional characteristics:

- `SELECT INTO` is not allowed in a cursor.
- Stored routines can have multiple cursor declarations, but all cursors declared in a given code block must have a unique name.
- Cursors can be nested.

### Open cursor

```
OPEN <Cursor Name>;
```

The `OPEN` command populates the cursor with the data, either dynamically or in a temporary table, and readies the first row for consumption by the `FETCH` statement.

### Fetch cursor

```
FETCH [[NEXT] FROM] <Cursor Name> INTO <Variable 1> [,<Variable n>]
```

The `FETCH` statement retrieves the current pointer row, assigns the column values to the variables listed in the `FETCH` statement, and advances the cursor pointer by one row. If the row is not available, meaning the cursor has been exhausted, a No Data condition is raised with an `SQLSTATE` value of '0200000'. To catch this condition, or the alternative NOT FOUND condition, you must create a condition handler.

###### Note

Carefully plan your error handling flow. The same condition might be raised by `SELECT` statements or cursors other than the one you intended. Place operations within `BEGIN …​ END` blocks to associate each cursor with its own handler.

### Close cursor

```
CLOSE <Cursor Name>;
```

The `CLOSE` statement closes an open cursor. If the cursor with the specified name does not exist, an error is raised. If a cursor is not explicitly closed, Aurora MySQL closes it automatically at the end of the `BEGIN …​ END` block in which it was declared.

### Examples

The following example uses a cursor to iterate over source rows and merges into an `OrderItems` table.

Create an `OrderItems` table.

```
CREATE TABLE OrderItems(OrderID INT NOT NULL,
  Item VARCHAR(20) NOT NULL,
  Quantity SMALLINT NOT NULL,
  PRIMARY KEY(OrderID, Item));
```

Create and populate the `SourceTable`.

```
CREATE TABLE SourceTable (
  OrderID INT,
  Item VARCHAR(20),
  Quantity SMALLINT,
  PRIMARY KEY (OrderID, Item));

INSERT INTO SourceTable (
  OrderID, Item, Quantity)
VALUES (1, 'M8 Bolt', 100),
  (2, 'M8 Nut', 100),
  (3, 'M8 Washer', 200);
```

Create a procedure to loop through `SourceTable` and insert rows.

```
CREATE PROCEDURE LoopItems()
BEGIN
  DECLARE done INT DEFAULT FALSE;
  DECLARE var_OrderID INT;
  DECLARE var_Item VARCHAR(20);
  DECLARE var_Quantity SMALLINT;
  DECLARE ItemCursor CURSOR FOR SELECT OrderID, Item, Quantity FROM SourceTable;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
  OPEN ItemCursor;
  CursorStart: LOOP
  FETCH NEXT FROM ItemCursor INTO var_OrderID, var_Item, var_Quantity;
  IF Done THEN LEAVE CursorStart;
  END IF;
    INSERT INTO OrderItems (OrderID, Item, Quantity)
      VALUES (var_OrderID, var_Item, var_Quantity);
  END LOOP;
  CLOSE ItemCursor;
END;
```

Run the stored procedure.

```
CALL LoopItems();
```

Select all rows from the `OrderItems` table.

```
SELECT * FROM OrderItems;

OrderID  Item       Quantity
1        M8 Bolt    100
2        M8 Nut     100
3        M8 Washer  200
```

## Summary

| Action                                                                                                                                                | Oracle                                                                                                                                                                                       | Aurora MySQL                                                                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Declare a bound explicit cursor                                                                                                                       | `<br>CURSOR c1 IS<br>SELECT<br>• FROM employees;<br>`                                                                                                                                        | `<br>DECLARE c1 CURSOR<br>FOR SELECT *<br>FROM employees;<br>`                                                                                                     |
| Open a cursor                                                                                                                                         | `<br>OPEN c1;<br>`                                                                                                                                                                           | `<br>OPEN c1;<br>`                                                                                                                                                 |
| Move the cursor to the next row and fetch into a record variable (`rowvar` was declared in the `DECLARE` section)                                     | `<br>FETCH c1 INTO rowvar;<br>`                                                                                                                                                              | `<br>FETCH NEXT FROM c1 INTO rowvar;<br>`                                                                                                                          |
| Move the cursor to the next row and fetch into multiple scalar data types (`emp_id`, `emp_name`, and `salary` were declared in the `DECLARE` section) | `<br>FETCH c1<br>INTO emp_id, emp_name, salary;<br>`                                                                                                                                         | `<br>FETCH NEXT FROM c1 INTO emp_id,<br>emp_name, salary;<br>`                                                                                                     |
| Iterate through an implicit cursor using a loop                                                                                                       | `<br>FOR item IN (<br>SELECT last_name, job_id FROM employees<br>WHERE job_id LIKE '%CLERK%'<br>AND manager_id > 120 ORDER BY last_name )<br>LOOP<br><< do something<br>>><br>END LOOP;<br>` | N/A                                                                                                                                                                |
| Declare a cursor with variables                                                                                                                       | `<br>CURSOR c1 (key NUMBER)<br>IS SELECT<br>• FROM employees<br>WHERE id = key;<br>`                                                                                                         | `<br>SET @sqltext1 := CONCAT<br>('DECLARE c1 CURSOR FOR<br>SELECT<br>• FROM employees WHERE<br>id =',key);<br>PREPARE stmt1 FROM @sqltext1;<br>EXECUTE stmt1;<br>` |
| Open a cursor with variables                                                                                                                          | `<br>OPEN c1(2);<br>`                                                                                                                                                                        | Use regular `OPEN` after declaring the `CURSOR` using `EXECUTE` and `PREPARE` with variables                                                                       |
| Exit a loop after no data found                                                                                                                       | `<br>EXIT WHEN c1%NOTFOUND;<br>`                                                                                                                                                             | `<br>DECLARE CONTINUE HANDLER<br>FOR NOT FOUND SET done = TRUE;<br>And in the fetching loop insert:<br>IF done THEN LEAVE;<br>`                                    |
| Detect if a cursor has rows remaining in its dataset                                                                                                  | `<br>%FOUND<br>`                                                                                                                                                                             | N/A                                                                                                                                                                |
| Determine how many rows were affected from any DML statement                                                                                          | `<br>%BULK_ROWCOUNT<br>`                                                                                                                                                                     | Use counters                                                                                                                                                       |
| Determine which DML run failed with the relevant error code                                                                                           | `<br>%BULK_EXCEPTIONS<br>`                                                                                                                                                                   | N/A                                                                                                                                                                |
| Detect if the cursor is open                                                                                                                          | `<br>%ISOPEN<br>`                                                                                                                                                                            | N/A                                                                                                                                                                |
| Detect if the cursor has no rows remaining in its dataset                                                                                             | `<br>%NOTFOUND<br>`                                                                                                                                                                          | N/A                                                                                                                                                                |
| Return the number of rows affected by a cursor                                                                                                        | `<br>%ROWCOUNT<br>`                                                                                                                                                                          | N/A                                                                                                                                                                |

For more information, see [Cursors](https://dev.mysql.com/doc/refman/5.7/en/cursors.html "https://dev.mysql.com/doc/refman/5.7/en/cursors.html") in the _MySQL documentation_.
