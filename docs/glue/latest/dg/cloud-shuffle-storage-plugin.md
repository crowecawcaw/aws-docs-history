# Cloud Shuffle Storage Plugin for Apache Spark

The Cloud Shuffle Storage Plugin is an Apache Spark plugin compatible with the [`ShuffleDataIO` API](https://github.com/apache/spark/blob/master/core/src/main/java/org/apache/spark/shuffle/api/ShuffleDataIO.java "https://github.com/apache/spark/blob/master/core/src/main/java/org/apache/spark/shuffle/api/ShuffleDataIO.java") which allows storing shuffle data on cloud storage systems (such as Amazon S3). It helps you to supplement or replace local disk storage capacity for large shuffle operations, commonly triggered by transformations such as `join`, `reduceByKey`, `groupByKey` and `repartition` in your Spark applications, thereby reducing common failures or price/performance dislocation of your serverless data analytics jobs and pipelines.

###### AWS Glue

AWS Glue versions 3.0 and 4.0 comes with the plugin pre-installed and ready to enable shuffling to Amazon S3 without any extra steps. For more information, see [AWS Glue Spark shuffle plugin with Amazon S3](monitor-spark-shuffle-manager.md "monitor-spark-shuffle-manager.md") to enable the feature for your Spark applications.

###### Other Spark environments

The plugin requires the following Spark configurations to be set on other Spark environments:

- `--conf spark.shuffle.sort.io.plugin.class=com.amazonaws.spark.shuffle.io.cloud.ChopperPlugin`: This informs Spark to use this plugin for Shuffle IO.
- `--conf spark.shuffle.storage.path=s3://`bucket-name`/`shuffle-file-dir``: The path where your shuffle files will be stored.

###### Note

The plugin overwrites one Spark core class. As a result, the plugin jar needs to be loaded before Spark jars. You can do this using `userClassPathFirst` in on-prem YARN environments if the plugin is used outside AWS Glue.

## Bundling the plugin with your Spark applications

You can bundle the plugin with your Spark applications and Spark distributions (versions 3.1 and above) by adding the plugin dependency in your Maven `pom.xml` while developing your Spark applications locally. For more information on the plugin and Spark versions, see [Plugin versions](#cloud-shuffle-storage-plugin-versions "#cloud-shuffle-storage-plugin-versions").

```
<repositories>
   ...
    <repository>
        <id>aws-glue-etl-artifacts</id>
        <url>https://aws-glue-etl-artifacts.s3.amazonaws.com/release/ </url>
    </repository>
</repositories>
...
<dependency>
    <groupId>com.amazonaws</groupId>
    <artifactId>chopper-plugin</artifactId>
    <version>3.1-amzn-LATEST</version>
</dependency>
```

You can alternatively download the binaries from AWS Glue Maven artifacts directly and include them in your Spark application as follows.

```
#!/bin/bash
sudo wget -v https://aws-glue-etl-artifacts.s3.amazonaws.com/release/com/amazonaws/chopper-plugin/3.1-amzn-LATEST/chopper-plugin-3.1-amzn-LATEST.jar -P /usr/lib/spark/jars/
```

Example spark-submit

```
spark-submit --deploy-mode cluster \
--conf spark.shuffle.storage.s3.path=s3://<ShuffleBucket>/<shuffle-dir> \
--conf spark.driver.extraClassPath=`<Path to plugin jar>` \
--conf spark.executor.extraClassPath=`<Path to plugin jar>` \
--class <your test class name> s3://`<ShuffleBucket>`/`<Your application jar>` \
```

## Optional configurations

These are optional configuration values that control Amazon S3 shuffle behavior.

- `spark.shuffle.storage.s3.enableServerSideEncryption`: Enable/disable S3 SSE for shuffle and spill files. Default value is `true`.
- `spark.shuffle.storage.s3.serverSideEncryption.algorithm`: The SSE algorithm to be used. Default value is `AES256`.
- `spark.shuffle.storage.s3.serverSideEncryption.kms.key`: The KMS key ARN when SSE aws:kms is enabled.

Along with these configurations, you may need to set configurations such as `spark.hadoop.fs.s3.enableServerSideEncryption` and **other environment-specific configurations** to ensure appropriate encryption is applied for your use case.

## Plugin versions

This plugin is supported for the Spark versions associated with each AWS Glue version. The following table shows the AWS Glue version, Spark version and associated plugin version with Amazon S3 location for the plugin's software binary.

| AWS Glue version | Spark version | Plugin version  | Amazon S3 location                                                                                             |
| ---------------- | ------------- | --------------- | -------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| 3.0              | 3.1           | 3.1-amzn-LATEST | s3://aws-glue-etl-artifacts/release/com/amazonaws/chopper-plugin/3.1-amzn-0/chopper-plugin-3.1-amzn-LATEST.jar |
| 4.0              | 3.3           | 3.3-amzn-LATEST | s3://aws-glue-etl-artifacts/release/com/amazonaws/chopper-plugin/3.3-amzn-0/chopper-plugin-3.3-amzn-LATEST.jar | ## License The software binary for this plugin is licensed under the Apache-2.0 License. |
