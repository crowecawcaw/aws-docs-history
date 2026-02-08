# Copying data between DynamoDB and

HDFS

If you have data in a DynamoDB table, you can use Hive to copy the data to the Hadoop
Distributed File System (HDFS).

You might do this if you are running a MapReduce job that requires data from
DynamoDB. If you copy the data from DynamoDB into HDFS, Hadoop can process it, using all
of the available nodes in the Amazon EMR cluster in parallel. When the MapReduce job is
complete, you can then write the results from HDFS to DDB.

In the following examples, Hive will read from and write to the following HDFS
directory: `/user/hadoop/hive-test`

###### Note

The examples in this section are written with the assumption you followed the
steps in [Tutorial: Working with Amazon DynamoDB and Apache
Hive](EMRforDynamoDB.md "EMRforDynamoDB.md") and you have an external table in
DynamoDB named _ddb_features_.

###### Topics

- [Copying data
  using the Hive default format](#EMRforDynamoDB.CopyingData.HDFS.DefaultFormat "#EMRforDynamoDB.CopyingData.HDFS.DefaultFormat")
- [Copying
  data with a user-specified format](#EMRforDynamoDB.CopyingData.HDFS.UserSpecifiedFormat "#EMRforDynamoDB.CopyingData.HDFS.UserSpecifiedFormat")
- [Copying data
  without a column mapping](#EMRforDynamoDB.CopyingData.HDFS.NoColumnMapping "#EMRforDynamoDB.CopyingData.HDFS.NoColumnMapping")
- [Accessing the data
  in HDFS](#EMRforDynamoDB.CopyingData.HDFS.ViewingData "#EMRforDynamoDB.CopyingData.HDFS.ViewingData")

## Copying data

using the Hive default format

###### Example From DynamoDB to HDFS

Use an `INSERT OVERWRITE` statement to write directly to
HDFS.

```
INSERT OVERWRITE DIRECTORY 'hdfs:///user/hadoop/hive-test'
SELECT * FROM ddb_features;
```

The data file in HDFS looks like this:

```
920709`^A`Soldiers Farewell Hill`^A`Summit`^A`NM`^A`32.3564729`^A`-108.33004616135
1178153`^A`Jones Run`^A`Stream`^A`PA`^A`41.2120086`^A`-79.25920781260
253838`^A`Sentinel Dome`^A`Summit`^A`CA`^A`37.7229821`^A`-119.584338133
264054`^A`Neversweet Gulch`^A`Valley`^A`CA`^A`41.6565269`^A`-122.83614322900
115905`^A`Chacaloochee Bay`^A`Bay`^A`AL`^A`30.6979676`^A`-87.97388530
```

Each field is separated by an SOH character (start of heading, 0x01). In
the file, SOH appears as `^A`.

###### Example From HDFS to DynamoDB

1. Create an external table that maps to the unformatted data in
   HDFS.

```
CREATE EXTERNAL TABLE hdfs_features_unformatted
    (feature_id       BIGINT,
    feature_name      STRING ,
    feature_class     STRING ,
    state_alpha       STRING,
    prim_lat_dec      DOUBLE ,
    prim_long_dec     DOUBLE ,
    elev_in_ft        BIGINT)
LOCATION 'hdfs:///user/hadoop/hive-test';
```

2. Copy the data to DynamoDB.

```
INSERT OVERWRITE TABLE ddb_features
SELECT * FROM hdfs_features_unformatted;
```

## Copying

data with a user-specified format

If you want to use a different field separator character, you can create an
external table that maps to the HDFS directory. You might use this technique for
creating data files with comma-separated values (CSV).

###### Example From DynamoDB to HDFS

1. Create a Hive external table that maps to HDFS. When you do this,
   ensure that the data types are consistent with those of the DynamoDB
   external table.

```
CREATE EXTERNAL TABLE hdfs_features_csv
    (feature_id       BIGINT,
    feature_name      STRING ,
    feature_class     STRING ,
    state_alpha       STRING,
    prim_lat_dec      DOUBLE ,
    prim_long_dec     DOUBLE ,
    elev_in_ft        BIGINT)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION 'hdfs:///user/hadoop/hive-test';
```

2. Copy the data from DynamoDB.

```
INSERT OVERWRITE TABLE hdfs_features_csv
SELECT * FROM ddb_features;
```

The data file in HDFS looks like this:

```
920709,Soldiers Farewell Hill,Summit,NM,32.3564729,-108.3300461,6135
1178153,Jones Run,Stream,PA,41.2120086,-79.2592078,1260
253838,Sentinel Dome,Summit,CA,37.7229821,-119.58433,8133
264054,Neversweet Gulch,Valley,CA,41.6565269,-122.8361432,2900
115905,Chacaloochee Bay,Bay,AL,30.6979676,-87.9738853,0
```

###### Example From HDFS to DynamoDB

With a single HiveQL statement, you can populate the DynamoDB table using the
data from HDFS:

```
INSERT OVERWRITE TABLE ddb_features
SELECT * FROM hdfs_features_csv;
```

## Copying data

without a column mapping

You can copy data from DynamoDB in a raw format and write it to HDFS without
specifying any data types or column mapping. You can use this method to create
an archive of DynamoDB data and store it in HDFS.

###### Note

If your DynamoDB table contains attributes of type Map, List, Boolean or
Null, then this is the only way you can use Hive to copy data from DynamoDB to
HDFS.

###### Example From DynamoDB to HDFS

1. Create an external table associated with your DynamoDB table. (There
   is no `dynamodb.column.mapping` in this HiveQL
   statement.)

```
CREATE EXTERNAL TABLE ddb_features_no_mapping
    (item MAP<STRING, STRING>)
STORED BY 'org.apache.hadoop.hive.dynamodb.DynamoDBStorageHandler'
TBLPROPERTIES ("dynamodb.table.name" = "Features");
```

2. Create another external table associated with your HDFS
   directory.

```
CREATE EXTERNAL TABLE hdfs_features_no_mapping
    (item MAP<STRING, STRING>)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
LINES TERMINATED BY '\n'
LOCATION 'hdfs:///user/hadoop/hive-test';
```

3. Copy the data from DynamoDB to HDFS.

```
INSERT OVERWRITE TABLE hdfs_features_no_mapping
SELECT * FROM ddb_features_no_mapping;
```

The data file in HDFS looks like this:

```
Name`^C`{"s":"Soldiers Farewell Hill"}`^B`State`^C`{"s":"NM"}`^B`Class`^C`{"s":"Summit"}`^B`Elevation`^C`{"n":"6135"}`^B`Latitude`^C`{"n":"32.3564729"}`^B`Id`^C`{"n":"920709"}`^B`Longitude`^C`{"n":"-108.3300461"}
Name`^C`{"s":"Jones Run"}`^B`State`^C`{"s":"PA"}`^B`Class`^C`{"s":"Stream"}`^B`Elevation`^C`{"n":"1260"}`^B`Latitude`^C`{"n":"41.2120086"}`^B`Id`^C`{"n":"1178153"}`^B`Longitude`^C`{"n":"-79.2592078"}
Name`^C`{"s":"Sentinel Dome"}`^B`State`^C`{"s":"CA"}`^B`Class`^C`{"s":"Summit"}`^B`Elevation`^C`{"n":"8133"}`^B`Latitude`^C`{"n":"37.7229821"}`^B`Id`^C`{"n":"253838"}`^B`Longitude`^C`{"n":"-119.58433"}
Name`^C`{"s":"Neversweet Gulch"}`^B`State`^C`{"s":"CA"}`^B`Class`^C`{"s":"Valley"}`^B`Elevation`^C`{"n":"2900"}`^B`Latitude`^C`{"n":"41.6565269"}`^B`Id`^C`{"n":"264054"}`^B`Longitude`^C`{"n":"-122.8361432"}
Name`^C`{"s":"Chacaloochee Bay"}`^B`State`^C`{"s":"AL"}`^B`Class`^C`{"s":"Bay"}`^B`Elevation`^C`{"n":"0"}`^B`Latitude`^C`{"n":"30.6979676"}`^B`Id`^C`{"n":"115905"}`^B`Longitude`^C`{"n":"-87.9738853"}
```

Each field begins with an STX character (start of text, 0x02) and ends
with an ETX character (end of text, 0x03). In the file, STX appears as
`^B` and ETX appears as
`^C`.

###### Example From HDFS to DynamoDB

With a single HiveQL statement, you can populate the DynamoDB table using the
data from HDFS:

```
INSERT OVERWRITE TABLE ddb_features_no_mapping
SELECT * FROM hdfs_features_no_mapping;
```

## Accessing the data

in HDFS

HDFS is a distributed file system, accessible to all of the nodes in the Amazon EMR
cluster. If you use SSH to connect to the leader node, you can use
command line tools to access the data that Hive wrote to HDFS.

HDFS is not the same thing as the local file system on the leader node.
You cannot work with files and directories in HDFS using standard Linux commands
(such as `cat`, `cp`, `mv`, or
`rm`). Instead, you perform these tasks using the `hadoop
 fs` command.

The following steps are written with the assumption you have copied data from
DynamoDB to HDFS using one of the procedures in this section.

1. If you are currently at the Hive command prompt, exit to the Linux
   command prompt.

```
hive> exit;
```

2. List the contents of the /user/hadoop/hive-test directory in HDFS.
   (This is where Hive copied the data from DynamoDB.)

```
hadoop fs -ls /user/hadoop/hive-test
```

The response should look similar to this:

```
Found 1 items
-rw-r--r-- 1 hadoop hadoop 29504 2016-06-08 23:40 /user/hadoop/hive-test/000000_0
```

The file name (_000000_0_) is
system-generated. 3. View the contents of the file:

```
hadoop fs -cat /user/hadoop/hive-test/000000_0
```

###### Note

In this example, the file is relatively small (approximately 29
KB). Be careful when you use this command with files that are very
large or contain non-printable characters. 4. (Optional) You can copy the data file from HDFS to the local file
system on the leader node. After you do this, you can use
standard Linux command line utilities to work with the data in the
file.

```
hadoop fs -get /user/hadoop/hive-test/000000_0
```

This command will not overwrite the file.

###### Note

The local file system on the leader node has limited
capacity. Do not use this command with files that are larger than
the available space in the local file system.
