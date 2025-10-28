# FileSize

The FileSize ruletype allows you to ensure that files meet a certain file size criteria. This is useful for following use cases:

1. Ensure that producers are not sending empty or substantially smaller files for processing.
2. Ensure that your target buckets don’t have smaller files which may lead to performance issues.

FileSize gathers the following metrics:

1. Compliance: returns the % of files that meet the rule threshold you have established
2. File Count: the number of files that were scanned by the rule
3. Minimum file size in bytes
4. Maximum file size in bytes

```
Dataset.*.FileSize.Compliance: 1.00,
Dataset.*.FileCount: 8.00,
Dataset.*.MaximumFileSize: 327413121.00,
Dataset.*.MinimumFileSize: 204558920.00
```

Anomaly detection is not supported for these metrics.

**Validate size of files**

This rule will pass when file.dat is greater than 2 MB.

```
FileSize "s3://amzn-s3-demo-bucket/file.dat" > 2 MB
```

The supported unites include B(bytes), MB(mega bytes), GB(giga bytes) and TB(terra bytes).

**Validate size of files in folders**

```

FileSize "s3://bucket/" > 5 B
FileSize "s3://bucket/" < 2 GB
```

This rule will pass if 70% of the files in s3://amzn-s3-demo-bucket is between 2 GB and 1 TB.

```
FileSize "s3://amzn-s3-demo-bucket/" between 2 GB and 1 TB  with threshold > 0.7
```

**Inferring file names directly from data frames**

You don't always have to provide a file path. For instance, when you are authoring the rule in the Data Catalog, it may be hard to
find which folders the catalog tables are using. AWS Glue Data Quality can find the specific folders or files used to populate your data frame.

###### Note

This feature will only work when files are successfully read into the DynamicFrame or DataFrame.

```
FileSize < 10 MB with threshold > 0.7
```

**Optional File-based Rule Tags:**

Tags allow you to control the rule behaviour.

**recentFiles**

This tag limits the number of files processed by keeping the most recent file first.

```
FileSize "s3://amzn-s3-demo-bucket/" > 5 B with recentFiles = 1
```

**matchFileName**

This tag ensures that files don’t have duplicate names. Default behavior is false.

```
FileSize "s3://amzn-s3-demo-bucket/" > 5 B with matchFileName = "true"
```

There are a few considerations:

1. In AWS Glue ETL, you must have Evaluate DataQuality Transform immediately after the Amazon S3 or Data Catalog transform.
2. This rule will not work in AWS Glue Interactive Sessions.
