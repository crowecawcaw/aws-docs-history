# Asynchronous indexes in Aurora DSQL

The `CREATE INDEX ASYNC` command creates an index on one or more columns of a
specified table. This command is an asynchronous DDL operation that doesn't block other
transactions. When you run `CREATE INDEX ASYNC`, Aurora DSQL immediately returns a
`job_id`.

You can monitor the status of this asynchronous job using the `sys.jobs` system
view. While the index creation job is in progress, you can use these procedures and commands:

**`sys.wait_for_job(job_id)`'your_index_creation_job_id'``**

Blocks the current session until the specified job completes or fails. Returns a
Boolean value indicating success or failure.

**`DROP INDEX`**

Cancels an in-progress index build job.

When the asynchronous index creation completes, Aurora DSQL updates the system catalog to
mark the index as active.

###### Note

Note that concurrent transactions accessing objects in the same namespace during
this update might encounter concurrency errors.

When Aurora DSQL finishes an asynchronous index task, it updates the system catalog to show
that the index is active. If other transactions reference the objects in the same namespace at
this time, you might see a concurrency error.

## Syntax

`CREATE INDEX ASYNC` uses the following syntax.

```
CREATE [ UNIQUE ] INDEX ASYNC [ IF NOT EXISTS ] name ON table_name
     ( { column_name } [ NULLS { FIRST | LAST } ] )
     [ INCLUDE ( column_name [, ...] ) ]
     [ NULLS [ NOT ] DISTINCT ]
```

## Parameters

**`UNIQUE`**

Indicates to Aurora DSQL to check for duplicate values in the table when it creates the
index and each time you add data. If you specify this parameter, insert and update
operations that would result in duplicate entries generate an error.

**`IF NOT EXISTS`**

Indicates that Aurora DSQL shouldn't throw an exception if an index with the same name
already exists. In this situation, Aurora DSQL doesn't create the new index. Note that the
index you're trying to create could have a very different structure from the index
that exists. If you specify this parameter, the index name is required.

**`name`**

The name of the index. You can't include the name of your schema in this
parameter.

Aurora DSQL creates the index in the same schema as its parent table. The name of the
index must be distinct from the name of any other object, such as a table or index, in
the schema.

If you don't specify a name, Aurora DSQL generates a name automatically based on the
name of the parent table and indexed column. For example, if you run `CREATE
 INDEX ASYNC on table1 (col1, col2)`, Aurora DSQL automatically names the index
`table1_col1_col2_idx`.

**`NULLS FIRST | LAST`**

The sort order of null and non-null columns. `FIRST` indicates that
Aurora DSQL should sort null columns before non-null columns. `LAST` indicates
that Aurora DSQL should sort null columns after non-null columns.

**`INCLUDE`**

A list of columns to include in the index as non-key columns. You can't use a
non-key column in an index scan search qualiﬁcation. Aurora DSQL ignores the column in
terms of uniqueness for an index.

**`NULLS DISTINCT | NULLS NOT DISTINCT`**

Specifies whether Aurora DSQL should consider null values as distinct in a unique
index. The default is `DISTINCT`, meaning that a unique index can contain
multiple null values in a column. `NOT DISTINCT` indicates that an index
can't contain multiple null values in a column.

## Usage notes

Consider the following guidelines:

- The `CREATE INDEX ASYNC` command doesn't introduce locks. It also doesn't
  affect the base table that Aurora DSQL uses to create the index.
- During schema migration operations, the `sys.wait_for_job(job_id)`'your_index_creation_job_id'``
  procedure is useful. It ensures that subsequent DDL and DML operations target the newly
  created index.
- Every time Aurora DSQL runs a new asynchronous task, it checks the `sys.jobs`
  view and deletes tasks that have a status of `completed` or
  `failed` for more than 30 minutes. Thus, `sys.jobs` primarily
  shows in-progress tasks and doesn’t contain information about old tasks.
- If Aurora DSQL fails to build an asynchronous index, the index stays
  `INVALID`. For unique indexes, DML operations are subject to uniqueness
  constraints until you drop the index. We recommend that you drop invalid indexes and
  recreate them.

## Creating an index: example

The following example demonstrates how to create a schema, a table, and then an
index.

1. Create a table named `test.departments`.

```
CREATE SCHEMA test;

 CREATE TABLE test.departments (name varchar(255) primary key NOT null,
     manager varchar(255),
     size varchar(4));
```

2. Insert a row into the table.

```
INSERT INTO test.departments VALUES ('Human Resources', 'John Doe', '10')
```

3. Create an asynchronous index.

```
CREATE INDEX ASYNC test_index on test.departments(name, manager, size);
```

The `CREATE INDEX` command returns a job ID, as shown below.

```
job_id
--------------------------
jh2gbtx4mzhgfkbimtgwn5j45y
```

The `job_id` indicates that Aurora DSQL has submitted a new job to create the
index. You can use the procedure `sys.wait_for_job(job_id)`'your_index_creation_job_id'`` to block other
work on the session until the job finishes or times out.

## Querying the status of index creation:

example

Query the `sys.jobs` system view to check the creation status of your index,
as shown in the following example.

```
SELECT * FROM sys.jobs
```

Aurora DSQL returns a response similar to the following.

```
           job_id           |   status   | details
----------------------------+------------+---------
 vs3kcl3rt5ddpk3a6xcq57cmcy | completed  |
 ihbyw2aoirfnrdfoc4ojnlamoq | processing |
```

The status column can be one of the following values.

| `submitted`                                                              | `processing`                        | `failed`                                                                                                                                                                                                                                       | `completed` |
| ------------------------------------------------------------------------ | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| The task is submitted, but Aurora DSQL hasn't started to process it yet. | Aurora DSQL is processing the task. | The task failed. See the details column for more information. If Aurora DSQL failed<br>to build the index, Aurora DSQL doesn't automatically remove the index definition. You<br>must manually remove the index with the `DROP INDEX` command. | Aurora DSQL |

You can also query the state of the index via the catalog tables
`pg_index`and `pg_class`. Specifically, the attributes
`indisvalid` and `indisimmediate` can tell you what state your index
is in. While Aurora DSQL creates your index, it has an initial status of `INVALID`.
The `indisvalid` flag for the index returns `FALSE` or `f`,
which indicates that the index isn't valid. If the flag returns `TRUE` or
`t`, the index is ready.

```
SELECT relname AS index_name, indisvalid as is_valid, pg_get_indexdef(indexrelid) AS index_definition
from pg_index, pg_class
WHERE pg_class.oid = indexrelid AND indrelid = 'test.departments'::regclass;
```

```
    index_name    | is_valid |                                                 index_definition
------------------+----------+-------------------------------------------------------------------------------------------------------------------
 department_pkey  |     t    | CREATE UNIQUE INDEX department_pkey ON test.departments USING btree_index (title) INCLUDE (name, manager, size)
 test_index1      |     t    | CREATE INDEX test_index1 ON test.departments USING btree_index (name, manager, size)
```

## Unique index build failures

If your asynchronous unique index build job shows a failed state with the detail
`Found duplicate key while validating index for UCVs`, this indicates that a
unique index could not be built due to uniqueness constraint violations.

###### To resolve unique index build failures

1. Remove any rows in your primary table that have duplicate entries for the keys
   specified in your unique secondary index.
2. Drop the failed index.
3. Issue a new create index command.

## Detecting uniqueness violations in primary

tables

The following SQL query helps you identify duplicate values in a specified column of
your table. This is particularly useful when you need to enforce uniqueness on a column that
isn't currently set as a primary key or doesn't have a unique constraint, such as email
addresses in a user table.

The examples below demonstrate how to create a sample users table, populate it with
test data containing known duplicates, and then run the detection query.

**Define table schema**

```
-- Drop the table if it exists
DROP TABLE IF EXISTS users;

-- Create the users table with a simple integer primary key
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY,
    email VARCHAR(255),
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Insert sample data that includes sets of duplicate email
addresses**

```
-- Insert sample data with explicit IDs
INSERT INTO users (user_id, email, first_name, last_name) VALUES
    (1, 'john.doe@example.com', 'John', 'Doe'),
    (2, 'jane.smith@example.com', 'Jane', 'Smith'),
    (3, 'john.doe@example.com', 'Johnny', 'Doe'),
    (4, 'alice.wong@example.com', 'Alice', 'Wong'),
    (5, 'bob.jones@example.com', 'Bob', 'Jones'),
    (6, 'alice.wong@example.com', 'Alicia', 'Wong'),
    (7, 'bob.jones@example.com', 'Robert', 'Jones');
```

**Run duplicate detection query**

```
-- Query to find duplicates
WITH duplicates AS (
    SELECT email, COUNT(*) as duplicate_count
    FROM users
    GROUP BY email
    HAVING COUNT(*) > 1
)
SELECT u.*, d.duplicate_count
FROM users u
INNER JOIN duplicates d ON u.email = d.email
ORDER BY u.email, u.user_id;
```

**View all records with duplicate email addresses**

```
 user_id |         email          | first_name | last_name |         created_at         | duplicate_count
---------+------------------------+------------+-----------+----------------------------+-----------------
       4 | akua.mansa@example.com | Akua       | Mansa     | 2025-05-21 20:55:53.714432 |               2
       6 | akua.mansa@example.com | Akua       | Mansa     | 2025-05-21 20:55:53.714432 |               2
       1 | john.doe@example.com   | John       | Doe       | 2025-05-21 20:55:53.714432 |               2
       3 | john.doe@example.com   | Johnny     | Doe       | 2025-05-21 20:55:53.714432 |               2
(4 rows)
```

**If we were to try the index creation statement now, it would fail:**

```
postgres=> CREATE UNIQUE INDEX ASYNC idx_users_email ON users(email);
      job_id
----------------------------
 ve32upmjz5dgdknpbleeca5tri
(1 row)

postgres=> select * from sys.jobs;
           job_id           |  status   |                       details                       |  job_type   | class_id | object_id |      object_name       |       start_time       |      update_time
----------------------------+-----------+-----------------------------------------------------+-------------+----------+-----------+------------------------+------------------------+------------------------
 qpn6aqlkijgmzilyidcpwrpova | completed |                                                     | DROP        |     1259 |     26384 |                        | 2025-05-20 00:47:10+00 | 2025-05-20 00:47:32+00
 ve32upmjz5dgdknpbleeca5tri | failed    | Found duplicate key while validating index for UCVs | INDEX_BUILD |     1259 |     26396 | public.idx_users_email | 2025-05-20 00:49:49+00 | 2025-05-20 00:49:56+00
(2 rows)
```
