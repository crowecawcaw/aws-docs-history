# Comparing Babelfish and SQL Server isolation levels

Below are a few examples on the nuances in how SQL Server and Babelfish implement the ANSI isolation levels.

###### Note

- Isolation level `REPEATABLE READ` and `SNAPSHOT` are the same in Babelfish.
- Isolation level `READ UNCOMMITTED` and `READ COMMITTED` are the same in Babelfish.
  The following example shows how to create the base table for all the examples mentioned below:

```
CREATE TABLE employee (
    id sys.INT NOT NULL PRIMARY KEY,
    name sys.VARCHAR(255)NOT NULL,
    age sys.INT NOT NULL
);
INSERT INTO employee (id, name, age) VALUES (1, 'A', 10);
INSERT INTO employee (id, name, age) VALUES (2, 'B', 20);
INSERT INTO employee (id, name, age) VALUES (3, 'C', 30);
```

###### Topics

- [Babelfish READ UNCOMMITTED compared with SQL Server READ UNCOMMITTED isolation level](#babelfish-transaction.examples.unc "#babelfish-transaction.examples.unc")
- [Babelfish READ COMMITTED compared with SQL Server READ COMMITTED isolation level](#babelfish-transaction.examples.com "#babelfish-transaction.examples.com")
- [Babelfish READ COMMITTED compared with SQL Server READ COMMITTED SNAPSHOT isolation level](#babelfish-transaction.examples.snapshot "#babelfish-transaction.examples.snapshot")
- [Babelfish REPEATABLE READ compared with SQL Server REPEATABLE READ isolation level](#babelfish-transaction.examples.read "#babelfish-transaction.examples.read")
- [Babelfish SERIALIZABLE compared with SQL Server SERIALIZABLE isolation level](#babelfish-transaction.examples.serialize "#babelfish-transaction.examples.serialize")

## Babelfish `READ UNCOMMITTED` compared with SQL Server `READ UNCOMMITTED` isolation level

The following table provides details on the dirty reads when concurrent transactions are executed. It shows observed results when using the `READ UNCOMMITTED` isolation level
in SQL Server compared to the Babelfish implementation.

| Transaction 1                                          | Transaction 2                                          | SQL Server `READ UNCOMMITTED`                                 | Babelfish `READ UNCOMMITTED`                                                                                    |
| ------------------------------------------------------ | ------------------------------------------------------ | ------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `BEGIN TRANSACTION`                                    | `BEGIN TRANSACTION`                                    | None                                                          | None                                                                                                            |
| `SET TRANSACTION ISOLATION<br>LEVEL READ UNCOMMITTED;` | `SET TRANSACTION ISOLATION<br>LEVEL READ UNCOMMITTED;` | None                                                          | None                                                                                                            |
| Idle in transaction                                    | `UPDATE employee SET age=0;`                           | Update successful.                                            | Update successful.                                                                                              |
| Idle in transaction                                    | `INSERT INTO employee VALUES (4, 'D', 40);`            | Insert successful.                                            | Insert successful.                                                                                              |
| `SELECT<br>• FROM employee;`                           | Idle in transaction                                    | Transaction 1 can see uncommitted changes from transaction 2. | Same as `READ COMMITTED` in Babelfish. Uncommitted changes from transaction 2 are not visible to transaction 1. |
| Idle in transaction                                    | `COMMIT`                                               | None                                                          | None                                                                                                            |
| `SELECT<br>• FROM employee;`                           | Idle in transaction                                    | Sees the changes committed by transaction 2.                  | Sees the changes committed by transaction 2.                                                                    |

## Babelfish `READ COMMITTED` compared with SQL Server `READ COMMITTED` isolation level

The following table provides details on the read-write blocking behavior when concurrent transactions are executed. It shows observed results when using the `READ COMMITTED` isolation level
in SQL Server compared to the Babelfish implementation.

| Transaction 1                                                               | Transaction 2                                        | SQL Server `READ COMMITTED`                                                                                | Babelfish `READ COMMITTED`                                       |
| --------------------------------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| `BEGIN TRANSACTION`                                                         | `BEGIN TRANSACTION`                                  | None                                                                                                       | None                                                             |
| `SET TRANSACTION ISOLATION<br>LEVEL READ COMMITTED;`                        | `SET TRANSACTION ISOLATION<br>LEVEL READ COMMITTED;` | None                                                                                                       | None                                                             |
| `SELECT<br>• FROM employee;`                                                | Idle in transaction                                  | None                                                                                                       | None                                                             |
| Idle in transaction                                                         | `UPDATE employee SET age=100 WHERE id = 1;`          | Update successful.                                                                                         | Update successful.                                               |
| `UPDATE employee SET age = 0 WHERE age IN (SELECT MAX(age) FROM employee);` | Idle in transaction                                  | Step blocked until transaction 2 commits.                                                                  | Transaction 2 changes is not visible yet. Updates row with id=3. |
| Idle in transaction                                                         | `COMMIT`                                             | Transaction 2 commits successfully. Transaction 1 is now unblocked and sees the update from transaction 2. | Transaction 2 commits successfully.                              |
| `SELECT<br>• FROM employee;`                                                | Idle in transaction                                  | Transaction 1 updates row with id = 1.                                                                     | Transaction 1 updates row with id = 3.                           |

## Babelfish `READ COMMITTED` compared with SQL Server `READ COMMITTED SNAPSHOT` isolation level

The following table provides details on the blocking behavior of the newly inserted rows when concurrent transactions are executed. It shows observed results when using the `READ COMMITTED SNAPSHOT` isolation level
in SQL Server compared to the `READ COMMITTED` Babelfish implementation.

| Transaction 1                                        | Transaction 2                                        | SQL Server `READ COMMITTED SNAPSHOT`                                                  | Babelfish `READ COMMITTED`                                                                                                        |
| ---------------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `BEGIN TRANSACTION`                                  | `BEGIN TRANSACTION`                                  | None                                                                                  | None                                                                                                                              |
| `SET TRANSACTION ISOLATION<br>LEVEL READ COMMITTED;` | `SET TRANSACTION ISOLATION<br>LEVEL READ COMMITTED;` | None                                                                                  | None                                                                                                                              |
| `INSERT INTO employee VALUES (4, 'D', 40);`          | Idle in transaction                                  | None                                                                                  | None                                                                                                                              |
| Idle in transaction                                  | `UPDATE employee SET age = 99;`                      | Step is blocked until transaction 1 commits. Inserted row is locked by transaction 1. | Updated three rows. The newly inserted row is not visible yet.                                                                    |
| `COMMIT`                                             | Idle in transaction                                  | Commit successful. Transaction 2 is now unblocked.                                    | Commit successful.                                                                                                                |
| Idle in transaction                                  | `SELECT<br>• FROM employee;`                         | All 4 rows have age=99.                                                               | Row with id = 4 has age value 40 since it was not visible to transaction 2 during update query. Other rows are updated to age=99. |

## Babelfish `REPEATABLE READ` compared with SQL Server `REPEATABLE READ` isolation level

The following table provides details on the read-write blocking behavior when concurrent transactions are executed. It shows observed results when using the `REPEATABLE READ` isolation level
in SQL Server compared to the `REPEATABLE READ` Babelfish implementation.

| Transaction 1                                         | Transaction 2                                         | SQL Server `REPEATABLE READ`                          | Babelfish `REPEATABLE READ`               |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------- |
| `BEGIN TRANSACTION`                                   | `BEGIN TRANSACTION`                                   | None                                                  | None                                      |
| `SET TRANSACTION ISOLATION<br>LEVEL REPEATABLE READ;` | `SET TRANSACTION ISOLATION<br>LEVEL REPEATABLE READ;` | None                                                  | None                                      |
| `SELECT<br>• FROM employee;`                          | Idle in transaction                                   | None                                                  | None                                      |
| `UPDATE employee SET name='A_TXN1' WHERE id=1;`       | Idle in transaction                                   | None                                                  | None                                      |
| Idle in transaction                                   | `SELECT<br>• FROM employee WHERE id != 1;`            | None                                                  | None                                      |
| Idle in transaction                                   | `SELECT<br>• FROM employee;`                          | Transaction 2 is blocked until transaction 1 commits. | Transaction 2 proceeds normally.          |
| `COMMIT`                                              | Idle in transaction                                   | None                                                  | None                                      |
| Idle in transaction                                   | `SELECT<br>• FROM employee;`                          | Update from transaction 1 is visible.                 | Update from transaction 1 is not visible. |
| `COMMIT`                                              | Idle in transaction                                   | None                                                  | None                                      |
| Idle in transaction                                   | `SELECT<br>• FROM employee;`                          | sees the update from transaction 1.                   | sees the update from transaction 1.       |

The following table provides details on the write-write blocking behavior when concurrent transactions are executed. It shows observed results when using the `REPEATABLE READ` isolation level
in SQL Server compared to the `REPEATABLE READ` Babelfish implementation.

| Transaction 1                                         | Transaction 2                                         | SQL Server `REPEATABLE READ`                            | Babelfish `REPEATABLE READ`                                                                               |
| ----------------------------------------------------- | ----------------------------------------------------- | ------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `BEGIN TRANSACTION`                                   | `BEGIN TRANSACTION`                                   | None                                                    | None                                                                                                      |
| `SET TRANSACTION ISOLATION<br>LEVEL REPEATABLE READ;` | `SET TRANSACTION ISOLATION<br>LEVEL REPEATABLE READ;` | None                                                    | None                                                                                                      |
| `UPDATE employee SET name='A_TXN1' WHERE id=1;`       | Idle in transaction                                   | None                                                    | None                                                                                                      |
| Idle in transaction                                   | `UPDATE employee SET name='A_TXN2' WHERE id=1;`       | Transaction 2 blocked.                                  | Transaction 2 blocked.                                                                                    |
| `COMMIT`                                              | Idle in transaction                                   | Commit successful and transaction 2 has been unblocked. | Commit successful and transaction 2 fails with error could not serialize access due to concurrent update. |
| Idle in transaction                                   | `COMMIT`                                              | Commit successful.                                      | Transaction 2 has already been aborted.                                                                   |
| Idle in transaction                                   | `SELECT<br>• FROM employee;`                          | Row with id=1 has name='A_TX2'.                         | Row with id=1 has name='A_TX1'.                                                                           |

The following table provides details on the phantom reads behavior when concurrent transactions are executed. It shows observed results when using the `REPEATABLE READ` isolation level
in SQL Server compared to the `REPEATABLE READ` Babelfish implementation.

| Transaction 1                                         | Transaction 2                                         | SQL Server `REPEATABLE READ`                  | Babelfish `REPEATABLE READ`                       |
| ----------------------------------------------------- | ----------------------------------------------------- | --------------------------------------------- | ------------------------------------------------- |
| `BEGIN TRANSACTION`                                   | `BEGIN TRANSACTION`                                   | None                                          | None                                              |
| `SET TRANSACTION ISOLATION<br>LEVEL REPEATABLE READ;` | `SET TRANSACTION ISOLATION<br>LEVEL REPEATABLE READ;` | None                                          | None                                              |
| `SELECT<br>• FROM employee;`                          | Idle in transaction                                   | None                                          | None                                              |
| Idle in transaction                                   | `INSERT INTO employee VALUES (4, 'NewRowName', 20);`  | Transaction 2 proceeds without any blocking.  | Transaction 2 proceeds without any blocking.      |
| Idle in transaction                                   | `SELECT<br>• FROM employee;`                          | Newly inserted row is visible.                | Newly inserted row is visible.                    |
| Idle in transaction                                   | `COMMIT`                                              | None                                          | None                                              |
| `SELECT<br>• FROM employee;`                          | Idle in transaction                                   | New row inserted by transaction 2 is visible. | New row inserted by transaction 2 is not visible. |
| `COMMIT`                                              | Idle in transaction                                   | None                                          | None                                              |
| `SELECT<br>• FROM employee;`                          | Idle in transaction                                   | Newly inserted row is visible.                | Newly inserted row is visible.                    |

The following table provides details when concurrent transactions are executed and the different final results when using the `REPEATABLE READ` isolation level
in SQL Server compared to the `REPEATABLE READ` Babelfish implementation.

| Transaction 1                                                                 | Transaction 2                                                               | SQL Server `REPEATABLE READ`                                                                                                               | Babelfish `REPEATABLE READ`                                                                                                                                                                |
| ----------------------------------------------------------------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `BEGIN TRANSACTION`                                                           | `BEGIN TRANSACTION`                                                         | None                                                                                                                                       | None                                                                                                                                                                                       |
| `SET TRANSACTION ISOLATION<br>LEVEL REPEATABLE READ;`                         | `SET TRANSACTION ISOLATION<br>LEVEL REPEATABLE READ;`                       | None                                                                                                                                       | None                                                                                                                                                                                       |
| `UPDATE employee SET age = 100 WHERE age IN (SELECT MIN(age) FROM employee);` | Idle in transaction                                                         | Transaction 1 updates row with id 1.                                                                                                       | Transaction 1 updates row with id 1.                                                                                                                                                       |
| Idle in transaction                                                           | `UPDATE employee SET age = 0 WHERE age IN (SELECT MAX(age) FROM employee);` | Transaction 2 is blocked since the SELECT statement tries to read rows locked by UPDATE query in transaction 1.                            | Transaction 2 proceeds without any blocking since read is never blocked, SELECT statement executes and finally row with id = 3 is updated since transaction 1 changes are not visible yet. |
| Idle in transaction                                                           | `SELECT<br>• FROM employee;`                                                | This step is executed after transaction 1 has committed. Row with id = 1 is updated by transaction 2 in previous step and is visible here. | Row with id = 3 is updated by Transaction 2.                                                                                                                                               |
| `COMMIT`                                                                      | Idle in transaction                                                         | Transaction 2 is now unblocked.                                                                                                            | Commit successful.                                                                                                                                                                         |
| Idle in transaction                                                           | `COMMIT`                                                                    | None                                                                                                                                       | None                                                                                                                                                                                       |
| `SELECT<br>• FROM employee;`                                                  | Idle in transaction                                                         | Both transaction execute update on row with id = 1.                                                                                        | Different rows are updated by transaction 1 and 2.                                                                                                                                         |

## Babelfish `SERIALIZABLE` compared with SQL Server `SERIALIZABLE` isolation level

The following table provides details on the range locks when concurrent transactions are executed. It shows observed results when using the `SERIALIZABLE` isolation level
in SQL Server compared to the `SERIALIZABLE` Babelfish implementation.

| Transaction 1                                      | Transaction 2                                      | SQL Server `SERIALIZABLE`                                           | Babelfish `SERIALIZABLE`                     |
| -------------------------------------------------- | -------------------------------------------------- | ------------------------------------------------------------------- | -------------------------------------------- |
| `BEGIN TRANSACTION`                                | `BEGIN TRANSACTION`                                | None                                                                | None                                         |
| `SET TRANSACTION ISOLATION<br>LEVEL SERILAIZABLE;` | `SET TRANSACTION ISOLATION<br>LEVEL SERILAIZABLE;` | None                                                                | None                                         |
| `SELECT<br>• FROM employee;`                       | Idle in transaction                                | None                                                                | None                                         |
| Idle in transaction                                | `INSERT INTO employee VALUES (4, 'D', 35);`        | Transaction 2 is blocked until transaction 1 commits.               | Transaction 2 proceeds without any blocking. |
| Idle in transaction                                | `SELECT<br>• FROM employee;`                       | None                                                                | None                                         |
| `COMMIT`                                           | Idle in transaction                                | Transaction 1 commits successfully. Transaction 2 is now unblocked. | Transaction 1 commits successfully.          |
| Idle in transaction                                | `COMMIT`                                           | None                                                                | None                                         |
| `SELECT<br>• FROM employee;`                       | Idle in transaction                                | Newly inserted row is visible.                                      | Newly inserted row is visible.               |

The following table provides details when concurrent transactions are executed and the different final results when using the `SERIALIZABLE` isolation level
in SQL Server compared to the `SERIALIZABLE` Babelfish implementation.

| Transaction 1                                      | Transaction 2                                      | SQL Server `SERIALIZABLE`                                           | Babelfish `SERIALIZABLE`                           |
| -------------------------------------------------- | -------------------------------------------------- | ------------------------------------------------------------------- | -------------------------------------------------- |
| `BEGIN TRANSACTION`                                | `BEGIN TRANSACTION`                                | None                                                                | None                                               |
| `SET TRANSACTION ISOLATION<br>LEVEL SERILAIZABLE;` | `SET TRANSACTION ISOLATION<br>LEVEL SERILAIZABLE;` | None                                                                | None                                               |
| Idle in transaction                                | `INSERT INTO employee VALUES (4, 'D', 40);`        | None                                                                | None                                               |
| `UPDATE employee SET age =99 WHERE id = 4;`        | Idle in transaction                                | Transaction 1 is blocked until transaction 2 commits.               | Transaction 1 proceeds without any blocking.       |
| Idle in transaction                                | `COMMIT`                                           | Transaction 2 commits successfully. Transaction 1 is now unblocked. | Transaction 2 commits successfully.                |
| `COMMIT`                                           | Idle in transaction                                | None                                                                | None                                               |
| `SELECT<br>• FROM employee;`                       | Idle in transaction                                | Newly inserted row is visible with age value = 99.                  | Newly inserted row is visible with age value = 40. |

The following table provides details when you `INSERT` into a table with unique constraint. It shows observed results when using the `SERIALIZABLE` isolation level
in SQL Server compared to the `SERIALIZABLE` Babelfish implementation.

| Transaction 1                                                              | Transaction 2                                      | SQL Server `SERIALIZABLE`                                           | Babelfish `SERIALIZABLE`                                                                                             |
| -------------------------------------------------------------------------- | -------------------------------------------------- | ------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `BEGIN TRANSACTION`                                                        | `BEGIN TRANSACTION`                                | None                                                                | None                                                                                                                 |
| `SET TRANSACTION ISOLATION<br>LEVEL SERILAIZABLE;`                         | `SET TRANSACTION ISOLATION<br>LEVEL SERILAIZABLE;` | None                                                                | None                                                                                                                 |
| Idle in transaction                                                        | `INSERT INTO employee VALUES (4, 'D', 40);`        | None                                                                | None                                                                                                                 |
| `INSERT INTO employee VALUES ((SELECT MAX(id)+1 FROM employee), 'E', 50);` | Idle in transaction                                | Transaction 1 is blocked until transaction 2 commits.               | Transaction 1 is blocked until transaction 2 commits.                                                                |
| Idle in transaction                                                        | `COMMIT`                                           | Transaction 2 commits successfully. Transaction 1 is now unblocked. | Transaction 2 commits successfully. Transaction 1 aborted with error duplicate key value violates unique constraint. |
| `COMMIT`                                                                   | Idle in transaction                                | Transaction 1 commits successfully.                                 | Transaction 1 commits fails with could not serialize access due to read or write dependencies among transactions.    |
| `SELECT<br>• FROM employee;`                                               | Idle in transaction                                | row (5, 'E', 50) is inserted.                                       | Only 4 rows exists.                                                                                                  |

In Babelfish, concurrent transactions running with Isolation Level serializable will fail with serialization anomaly error if the execution of these transaction is
inconsistent with all possible serial (one at a time) executions of those transactions.

The following tables provides details on serialization anomaly when concurrent transactions are executed. It shows observed results when using the `SERIALIZABLE` isolation level
in SQL Server compared to the `SERIALIZABLE` Babelfish implementation.

| Transaction 1                                      | Transaction 2                                      | SQL Server `SERIALIZABLE`                             | Babelfish `SERIALIZABLE`                                                                                              |
| -------------------------------------------------- | -------------------------------------------------- | ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `BEGIN TRANSACTION`                                | `BEGIN TRANSACTION`                                | None                                                  | None                                                                                                                  |
| `SET TRANSACTION ISOLATION<br>LEVEL SERILAIZABLE;` | `SET TRANSACTION ISOLATION<br>LEVEL SERILAIZABLE;` | None                                                  | None                                                                                                                  |
| `SELECT<br>• FROM employee;`                       | Idle in transaction                                | None                                                  | None                                                                                                                  |
| `UPDATE employee SET age=5 WHERE age=10;`          | Idle in transaction                                | None                                                  | None                                                                                                                  |
| Idle in transaction                                | `SELECT<br>• FROM employee;`                       | Transaction 2 is blocked until transaction 1 commits. | Transaction 2 proceeds without any blocking.                                                                          |
| Idle in transaction                                | `UPDATE employee SET age=35 WHERE age=30;`         | None                                                  | None                                                                                                                  |
| `COMMIT`                                           | Idle in transaction                                | Transaction 1 commits successfully.                   | Transaction 1 is committed first and is able to commit successfully.                                                  |
| Idle in transaction                                | `COMMIT`                                           | Transaction 2 commits successfully.                   | Transaction 2 commit fails with serialization error, the whole transaction has been rolled back. Retry transaction 2. |
| `SELECT<br>• FROM employee;`                       | Idle in transaction                                | Changes from both transactions are visible.           | Transaction 2 was rolled back. Only transaction 1 changes are seen.                                                   |

In Babelfish, serialization anomaly is only possible if all the concurrent transactions are executing at isolation level `SERIALIZABLE`. In the following table, lets take the above
example but set transaction 2 to isolation level `REPEATABLE READ` instead.

| Transaction 1                                      | Transaction 2                                         | SQL Server isolation levels                           | Babelfish isolation levels                   |
| -------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | -------------------------------------------- |
| `BEGIN TRANSACTION`                                | `BEGIN TRANSACTION`                                   | None                                                  | None                                         |
| `SET TRANSACTION ISOLATION<br>LEVEL SERILAIZABLE;` | `SET TRANSACTION ISOLATION<br>LEVEL REPEATABLE READ;` | None                                                  | None                                         |
| `SELECT<br>• FROM employee;`                       | Idle in transaction                                   | None                                                  | None                                         |
| `UPDATE employee SET age=5 WHERE age=10;`          | Idle in transaction                                   | None                                                  | None                                         |
| Idle in transaction                                | `SELECT<br>• FROM employee;`                          | Transaction 2 is blocked until transaction 1 commits. | Transaction 2 proceeds without any blocking. |
| Idle in transaction                                | `UPDATE employee SET age=35 WHERE age=30;`            | None                                                  | None                                         |
| `COMMIT`                                           | Idle in transaction                                   | Transaction 1 commits successfully.                   | Transaction 1 commits successfully.          |
| Idle in transaction                                | `COMMIT`                                              | Transaction 2 commits successfully.                   | Transaction 2 commits successfully.          |
| `SELECT<br>• FROM employee;`                       | Idle in transaction                                   | Changes from both transactions are visible.           | Changes from both transactions are visible.  |
