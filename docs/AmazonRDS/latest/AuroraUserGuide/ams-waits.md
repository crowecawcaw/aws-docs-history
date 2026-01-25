# io/aurora_redo_log_flush

The `io/aurora_redo_log_flush` event occurs when a session is writing
persistent data to Amazon Aurora storage.

###### Topics

- [Supported engine versions](#ams-waits.io-auredologflush.context.supported "#ams-waits.io-auredologflush.context.supported")
- [Context](#ams-waits.io-auredologflush.context "#ams-waits.io-auredologflush.context")
- [Likely causes of increased waits](#ams-waits.io-auredologflush.causes "#ams-waits.io-auredologflush.causes")
- [Actions](#ams-waits.io-auredologflush.actions "#ams-waits.io-auredologflush.actions")

## Supported engine versions

This wait event information is supported for the following engine versions:

- Aurora MySQL version 2

## Context

The `io/aurora_redo_log_flush` event is for a write input/output (I/O) operation in Aurora MySQL.

###### Note

In Aurora MySQL version 3, this wait event is named [io/redo_log_flush](ams-waits.md "ams-waits.md").

## Likely causes of increased waits

For data persistence, commits require a durable write to stable storage. If the
database is doing too many commits, there is a wait event on the write I/O operation,
the `io/aurora_redo_log_flush` wait event.

In the following examples, 50,000 records are inserted into an Aurora MySQL DB cluster using the db.r5.xlarge DB instance
class:

- In the first example, each session inserts 10,000 records row by row. By default, if a data manipulation language
  (DML) command isn't within a transaction, Aurora MySQL uses implicit commits. Autocommit is turned on. This means
  that for each row insertion there is a commit. Performance Insights shows that the connections spend most of their time waiting on the
  `io/aurora_redo_log_flush` wait event.

![Performance Insights example of the wait event](images/auredologflush_PI_example1.png)

This is caused by the simple insert statements used.

![Insert statements in Top SQL](images/auredologflush_top_SQL1.png)

The 50,000 records take 3.5 minutes to be inserted.

- In the second example, inserts are made in 1,000 batches, that is each connection performs 10 commits instead of
  10,000. Performance Insights shows that the connections don't spend most of their time on the `io/aurora_redo_log_flush`
  wait event.

![Performance Insights example of the wait event having less impact](images/auredologflush_PI_example2.png)

The 50,000 records take 4 seconds to be inserted.

## Actions

We recommend different actions depending on the causes of your wait event.

###### Topics

- [Identify the problematic sessions and
  queries](#ams-waits.io-auredologflush.actions.identify-queries "#ams-waits.io-auredologflush.actions.identify-queries")
- [Group your write operations](#ams-waits.io-auredologflush.actions.action0 "#ams-waits.io-auredologflush.actions.action0")
- [Turn off
  autocommit](#ams-waits.io-auredologflush.actions.action1 "#ams-waits.io-auredologflush.actions.action1")
- [Use transactions](#ams-waits.io-auredologflush.action2 "#ams-waits.io-auredologflush.action2")
- [Use batches](#ams-waits.io-auredologflush.action3 "#ams-waits.io-auredologflush.action3")

### Identify the problematic sessions and

queries

If your DB instance is experiencing a bottleneck, your first task is to find the sessions and queries that
cause it. For a useful AWS Database Blog post, see [Analyze Amazon Aurora
MySQL Workloads with Performance Insights](https://aws.amazon.com/blogs/database/analyze-amazon-aurora-mysql-workloads-with-performance-insights/ "https://aws.amazon.com/blogs/database/analyze-amazon-aurora-mysql-workloads-with-performance-insights/").

###### To identify sessions and queries causing a bottleneck

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Performance Insights**.
3. Choose your DB instance.
4. In **Database load**, choose **Slice by wait**.
5. At the bottom of the page, choose **Top SQL**.

The queries at the top of the list are causing the highest load on the database.

### Group your write operations

The following examples trigger the `io/aurora_redo_log_flush` wait
event. (Autocommit is turned on.)

```
INSERT INTO `sampleDB`.`sampleTable` (sampleCol2, sampleCol3) VALUES ('xxxx','xxxxx');
INSERT INTO `sampleDB`.`sampleTable` (sampleCol2, sampleCol3) VALUES ('xxxx','xxxxx');
INSERT INTO `sampleDB`.`sampleTable` (sampleCol2, sampleCol3) VALUES ('xxxx','xxxxx');
....
INSERT INTO `sampleDB`.`sampleTable` (sampleCol2, sampleCol3) VALUES ('xxxx','xxxxx');

UPDATE `sampleDB`.`sampleTable` SET sampleCol3='xxxxx' WHERE id=xx;
UPDATE `sampleDB`.`sampleTable` SET sampleCol3='xxxxx' WHERE id=xx;
UPDATE `sampleDB`.`sampleTable` SET sampleCol3='xxxxx' WHERE id=xx;
....
UPDATE `sampleDB`.`sampleTable` SET sampleCol3='xxxxx' WHERE id=xx;

DELETE FROM `sampleDB`.`sampleTable` WHERE sampleCol1=xx;
DELETE FROM `sampleDB`.`sampleTable` WHERE sampleCol1=xx;
DELETE FROM `sampleDB`.`sampleTable` WHERE sampleCol1=xx;
....
DELETE FROM `sampleDB`.`sampleTable` WHERE sampleCol1=xx;
```

To reduce the time spent waiting on the `io/aurora_redo_log_flush` wait event, group your write operations
logically into a single commit to reduce persistent calls to storage.

### Turn off

autocommit

Turn off autocommit before making large changes that aren't within a
transaction, as shown in the following example.

```
SET SESSION AUTOCOMMIT=OFF;
UPDATE `sampleDB`.`sampleTable` SET sampleCol3='xxxxx' WHERE sampleCol1=xx;
UPDATE `sampleDB`.`sampleTable` SET sampleCol3='xxxxx' WHERE sampleCol1=xx;
UPDATE `sampleDB`.`sampleTable` SET sampleCol3='xxxxx' WHERE sampleCol1=xx;
....
UPDATE `sampleDB`.`sampleTable` SET sampleCol3='xxxxx' WHERE sampleCol1=xx;
-- Other DML statements here
COMMIT;

SET SESSION AUTOCOMMIT=ON;
```

### Use transactions

You can use transactions, as shown in the following example.

```
BEGIN
INSERT INTO `sampleDB`.`sampleTable` (sampleCol2, sampleCol3) VALUES ('xxxx','xxxxx');
INSERT INTO `sampleDB`.`sampleTable` (sampleCol2, sampleCol3) VALUES ('xxxx','xxxxx');
INSERT INTO `sampleDB`.`sampleTable` (sampleCol2, sampleCol3) VALUES ('xxxx','xxxxx');
....
INSERT INTO `sampleDB`.`sampleTable` (sampleCol2, sampleCol3) VALUES ('xxxx','xxxxx');

DELETE FROM `sampleDB`.`sampleTable` WHERE sampleCol1=xx;
DELETE FROM `sampleDB`.`sampleTable` WHERE sampleCol1=xx;
DELETE FROM `sampleDB`.`sampleTable` WHERE sampleCol1=xx;
....
DELETE FROM `sampleDB`.`sampleTable` WHERE sampleCol1=xx;

-- Other DML statements here
END
```

### Use batches

You can make changes in batches, as shown in the following example. However, using
batches that are too large can cause performance issues, especially in read replicas
or when doing point-in-time recovery (PITR).

```
INSERT INTO `sampleDB`.`sampleTable` (sampleCol2, sampleCol3) VALUES
('xxxx','xxxxx'),('xxxx','xxxxx'),...,('xxxx','xxxxx'),('xxxx','xxxxx');

UPDATE `sampleDB`.`sampleTable` SET sampleCol3='xxxxx' WHERE sampleCol1 BETWEEN xx AND xxx;

DELETE FROM `sampleDB`.`sampleTable` WHERE sampleCol1<xx;
```
