# io/redo_log_flush

The `io/redo_log_flush` event occurs when a session is writing persistent data to Amazon Aurora storage.

###### Topics

- [Supported engine versions](#ams-waits.io-redologflush.context.supported "#ams-waits.io-redologflush.context.supported")
- [Context](#ams-waits.io-redologflush.context "#ams-waits.io-redologflush.context")
- [Likely causes of increased waits](#ams-waits.io-redologflush.causes "#ams-waits.io-redologflush.causes")
- [Actions](#ams-waits.io-redologflush.actions "#ams-waits.io-redologflush.actions")

## Supported engine versions

This wait event information is supported for the following engine versions:

- Aurora MySQL version 3

## Context

The `io/redo_log_flush` event is for a write input/output (I/O) operation in Aurora MySQL.

###### Note

In Aurora MySQL version 2, this wait event is named [io/aurora_redo_log_flush](ams-waits.md "ams-waits.md").

## Likely causes of increased waits

For data persistence, commits require a durable write to stable storage. If the database is doing too many commits, there is a wait event on the
write I/O operation, the `io/redo_log_flush` wait event.

For examples of the behavior of this wait event, see [io/aurora_redo_log_flush](ams-waits.md "ams-waits.md").

## Actions

We recommend different actions depending on the causes of your wait event.

###### Topics

- [Identify the problematic sessions and
  queries](#ams-waits.io-redologflush.actions.identify-queries "#ams-waits.io-redologflush.actions.identify-queries")
- [Group your write operations](#ams-waits.io-redologflush.actions.action0 "#ams-waits.io-redologflush.actions.action0")
- [Turn off
  autocommit](#ams-waits.io-redologflush.actions.action1 "#ams-waits.io-redologflush.actions.action1")
- [Use transactions](#ams-waits.io-redologflush.action2 "#ams-waits.io-redologflush.action2")
- [Use batches](#ams-waits.io-redologflush.action3 "#ams-waits.io-redologflush.action3")

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

The following examples trigger the `io/redo_log_flush` wait
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

To reduce the time spent waiting on the `io/redo_log_flush` wait event, group your write operations
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

You can make changes in batches, as shown in the following example. However, using batches that are too large can cause
performance issues, especially in read replicas or when doing point-in-time recovery (PITR).

```
INSERT INTO `sampleDB`.`sampleTable` (sampleCol2, sampleCol3) VALUES
('xxxx','xxxxx'),('xxxx','xxxxx'),...,('xxxx','xxxxx'),('xxxx','xxxxx');

UPDATE `sampleDB`.`sampleTable` SET sampleCol3='xxxxx' WHERE sampleCol1 BETWEEN xx AND xxx;

DELETE FROM `sampleDB`.`sampleTable` WHERE sampleCol1<xx;
```
