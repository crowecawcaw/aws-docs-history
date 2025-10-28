# Configuring Tez

You can customize Tez by setting values using the `tez-site` configuration
classification, which configures settings in the `tez-site.xml` configuration
file. For more information, see [TezConfiguration](https://tez.apache.org/releases/0.8.2/tez-api-javadocs/configs/TezConfiguration.html "https://tez.apache.org/releases/0.8.2/tez-api-javadocs/configs/TezConfiguration.html") in the Apache Tez documentation. To change Hive or Pig to
use the Tez execution engine, use the `hive-site` and
`pig-properties` configuration classifications as appropriate. Examples
are shown below.

## Example configuration

###### Example: Customizing the Tez root logging level and setting Tez as the

execution engine for Hive and Pig

The example `create-cluster` command shown below creates a cluster
with Tez, Hive, and Pig installed. The command references a file stored in Amazon S3,
`myConfig.json`, which specifies properties for the
`tez-site` classification that sets `tez.am.log.level`
to `DEBUG`, and sets the execution engine to Tez for Hive and Pig
using the `hive-site` and `pig-properties` configuration
classifications.

###### Note

Linux line continuation characters (\) are included for readability. They can be removed or used in Linux commands. For Windows, remove them or replace with a caret (^).

```
aws emr create-cluster --release-label `emr-7.10.0` \
--applications Name=Tez Name=Hive Name=Pig --ec2-attributes KeyName=`myKey` \
--instance-type m5.xlarge --instance-count 3 \
--configurations https://s3.amazonaws.com/amzn-s3-demo-bucket/myfolder/myConfig.json --use-default-roles
```

Example contents of `myConfig.json` are shown below.

```
[
    {
      "Classification": "tez-site",
      "Properties": {
        "tez.am.log.level": "DEBUG"
      }
    },
    {
      "Classification": "hive-site",
      "Properties": {
        "hive.execution.engine": "tez"
      }
    },
    {
      "Classification": "pig-properties",
      "Properties": {
        "exectype": "tez"
      }
    }
  ]

```

###### Note

With Amazon EMR version 5.21.0 and later, you can override cluster configurations and specify additional configuration classifications for each instance group in a running cluster. You do this by using the Amazon EMR console, the AWS Command Line Interface (AWS CLI), or the AWS SDK. For more information, see [Supplying a Configuration for an Instance Group in a Running Cluster](emr-configure-apps-running-cluster.md "emr-configure-apps-running-cluster.md").

## Tez asynchronous split opening

When there is a large number of small files in the table path, and a query
attempts to read them all, each small file that corresponds to each individual split
gets combined under one Tez _grouped split_. A single mapper then
processes the single Tez grouped split. Since the execution is synchronous, each
individual split under the grouped split gets processed one by one. This requires
`RecordReader` objects to synchronously process the splits.

Amazon EMR 6.15.0 introduces configurations that you can specify to asynchronously open the input splits in a Tez grouped split. The feature was initiated
by [TEZ-4397](https://issues.apache.org/jira/browse/TEZ-4397 "https://issues.apache.org/jira/browse/TEZ-4397"), but had regressions in OSS Hive. EMR Hive fixed the regressions and additional
bugs in Hive ACID table. This improvement results in faster performance of read queries when there are a large number of
input splits in a single Tez Grouped Split.

| Name                                    | Classification                                                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | ----------------------------------------------------------------------------------------------- |
| `tez.grouping.split.init.threads`       | `tez-site`                                                                                                           | Specifies the number of daemon threads that Tez uses to pre-initiate the `RecordReaders` and open splits. For ACID tables, the maximum supported value of `tez.grouping.split.init.threads` is `1`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `tez.grouping.split.init.recordreaders` | `tez-site`                                                                                                           | Specifies the number of `RecordReaders` to keep pre-initialised by the daemon threads. This can help when Tez grouped split contains a large number of `InputSplits`. Initialization of `RecordReaders` to process those input splits can be done asynchronously with daemon threads instead of sequential processing.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Configuration notes: |
| Subject matter                          | Details                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | ---                  | ---                                                                                             |
| Recommended configuration settings      | It is recommended to set the above configuration settings to the values you want in both `hive-site` and `tez-site`. |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Matching values      | The values of the configuration settings should be the same in both `hive-site` and `tez-site`. |
| LLAP recommendation                     | It isn't recommended to use this feature when LLAP is enabled.                                                       | ### Benchmarking for Tez asynchronous split opening We used the following environments and configurations for benchmarking the Tez asynchronous split opening capability: <br>• Benchmark environment – Amazon EMR cluster with 1 primary node that uses m5.16xlarge, and 16 core nodes that use m5.16xlarge. <br>• Benchmark configurations – To simulate the scenario for benchmarking where a large number of input splits are in a single Tez grouped split, `tez.grouping.split-count` is set to `1`. <br>• Table used for benchmarking – The table contains 200 partitions, with each partition containing a single file. The benchmark is done for when that table contains CSV files, and when that table contains parquet files. Hive query for benchmarking: `SELECT COUNT(*)` from the table ten times, and take the average runtime. <br>• Configurations to enable Tez async split opening – As follows: + `tez.grouping.split.init.threads` = `4` + `tez.grouping.split.init.recordreaders` = `10` |
| Dataset                                 | Feature disabled (baseline)                                                                                          | Feature enabled                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Improvement          |
| ---                                     | ---                                                                                                                  | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | ---                  |
| CSV dataset                             | 90.26 seconds                                                                                                        | 79.20 seconds                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 12.25%               |
| Parquet dataset                         | 54.67 seconds                                                                                                        | 42.23 seconds                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | 22.75%               |
