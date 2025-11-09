# Querying data in DynamoDB

The following examples show some ways that you can use HiveQL to query data stored in
DynamoDB.

These examples refer to the _ddb_features_ table in the tutorial
([Step 5: Copy data to
DynamoDB](EMRforDynamoDB.Tutorial.md "EMRforDynamoDB.Tutorial.md")).

###### Topics

- [Using aggregate
  functions](#EMRforDynamoDB.Querying.AggregateFunctions "#EMRforDynamoDB.Querying.AggregateFunctions")
- [Using the GROUP BY and
  HAVING clauses](#EMRforDynamoDB.Querying.GroupByAndHaving "#EMRforDynamoDB.Querying.GroupByAndHaving")
- [Joining two DynamoDB
  tables](#EMRforDynamoDB.Querying.JoiningTwoTables "#EMRforDynamoDB.Querying.JoiningTwoTables")
- [Joining
  tables from different sources](#EMRforDynamoDB.Querying.JoiningTablesFromDifferentSources "#EMRforDynamoDB.Querying.JoiningTablesFromDifferentSources")

## Using aggregate

functions

HiveQL provides built-in functions for summarizing data values. For example, you
can use the `MAX` function to find the largest value for a selected
column. The following example returns the elevation of the highest feature in the
state of Colorado.

```
SELECT MAX(elev_in_ft)
FROM ddb_features
WHERE state_alpha = 'CO';
```

## Using the GROUP BY and

HAVING clauses

You can use the `GROUP BY` clause to collect data across multiple
records. This is often used with an aggregate function such as `SUM`,
`COUNT`, `MIN`, or `MAX`. You can also use the
`HAVING` clause to discard any results that do not meet certain
criteria.

The following example returns a list of the highest elevations from states that
have more than five features in the _ddb_features_ table.

```
SELECT state_alpha, max(elev_in_ft)
FROM ddb_features
GROUP BY state_alpha
HAVING count(*) >= 5;
```

## Joining two DynamoDB

tables

The following example maps another Hive table
(_east_coast_states_) to a table in DynamoDB. The
`SELECT` statement is a join across these two tables. The join is
computed on the cluster and returned. The join does not take place in DynamoDB.

Consider a DynamoDB table named EastCoastStates that contains the following
data:

```
**StateName StateAbbrev**

Maine           ME
New Hampshire   NH
Massachusetts   MA
Rhode Island    RI
Connecticut     CT
New York        NY
New Jersey      NJ
Delaware        DE
Maryland        MD
Virginia        VA
North Carolina  NC
South Carolina  SC
Georgia         GA
Florida         FL
```

Let's assume the table is available as a Hive external table named
east_coast_states:

```
CREATE EXTERNAL TABLE ddb_east_coast_states (state_name STRING, state_alpha STRING)
STORED BY 'org.apache.hadoop.hive.dynamodb.DynamoDBStorageHandler'
TBLPROPERTIES ("dynamodb.table.name" = "EastCoastStates",
"dynamodb.column.mapping" = "state_name:StateName,state_alpha:StateAbbrev");
```

The following join returns the states on the East Coast of the United States that
have at least three features:

```
SELECT ecs.state_name, f.feature_class, COUNT(*)
FROM ddb_east_coast_states ecs
JOIN ddb_features f on ecs.state_alpha = f.state_alpha
GROUP BY ecs.state_name, f.feature_class
HAVING COUNT(*) >= 3;
```

## Joining

tables from different sources

In the following example, s3_east_coast_states is a Hive table associated with a
CSV file stored in Amazon S3. The _ddb_features_ table is associated
with data in DynamoDB. The following example joins these two tables, returning the
geographic features from states whose names begin with "New."

```
create external table s3_east_coast_states (state_name STRING, state_alpha STRING)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
LOCATION 's3://`bucketname`/`path`/`subpath`/';
```

```
SELECT ecs.state_name, f.feature_name, f.feature_class
FROM s3_east_coast_states ecs
JOIN ddb_features f
ON ecs.state_alpha = f.state_alpha
WHERE ecs.state_name LIKE 'New%';
```
