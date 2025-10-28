# FileMatch

The FileMatch rule allows you to compare files against other files or checksums. This can be useful in a few scenarios:

1. Validating files received from external sources: You can use FileMatch to ensure that you have received the correct files
   from external sources by comparing against checksums. This helps validate the integrity of the data you're ingesting.
2. Comparing data in two different folders: FileMatch can be used to compare files between two folders.

This rule gathers one metric: the number of files that were scanned by the rule.

```
{"Dataset.*.FileCount":1}
```

**Validate file with a checksum:**

FileMatch accepts a file and a set checksums to ensure that at least one checksums match the file.

```
FileMatch "s3://amzn-s3-demo-bucket/file.json" in ["3ee0d8617ac041793154713e5ef8f319"] with hashAlgorithm = "MD5"
FileMatch "s3://amzn-s3-demo-bucket/file.json" in ["3ee0d8617ac041793154713e5ef8f319"] with hashAlgorithm = "SHA-1"
FileMatch "s3://amzn-s3-demo-bucket/file.json" in ["3ee0d8617ac041793154713e5ef8f319"] with hashAlgorithm = "SHA-256"
FileMatch "s3://amzn-s3-demo-bucket/file.json" in ["3ee0d8617ac041793154713e5ef8f319"]
```

The following standard algorithms are supported:

- MD5
- SHA-1
- SHA-256

If you do not supply an algorithm, the default is SHA-256.

**Validate all files in a folder with set of checksum:**

```
FileMatch "s3://amzn-s3-demo-bucket /" in ["3ee0d8617ac041793154713e5ef8f319", "7e8617ac041793154713e5ef8f319"] with hashAlgorithm = "MD5"
FileMatch "s3://amzn-s3-demo-bucket /internal-folder/" in ["3ee0d8617ac041793154713e5ef8f319", "7e8617ac041793154713e5ef8f319"]
```

**Compare files in different folders**

```
FileMatch "s3://original_bucket/" "s3://archive_bucket/"
FileMatch "s3://original_bucket/internal-folder/" "s3://original_bucket/other-folder/"
```

FileMatch will check the contents of the files in `original_bucket` and ensure they match what’s in
`archive_bucket`. The rule will fail if they don’t exactly match. It also can check the contents of internal
folders or individual files.

FileMatch can also check individual files against each other.

```
FileMatch "s3://amzn-s3-demo-bucket /file_old.json" "s3://amzn-s3-demo-bucket /file_new.json"
```

**Inferring file names directly from data frames**

You don't always have to provide a file path. For instance, when you are authoring the rule in the AWS Glue Data Catalog (backed by Amazon S3),
it may be hard to find which folders the catalog tables are using. AWS Glue Data Quality can find the specific folders or files used to
populate your data frame.

###### Note

This feature will only work when files are successfully read into the DynamicFrame or DataFrame.

```
FileMatch in ["3ee0d8617ac041793154713e5ef8f319"] with hashAlgorithm = "MD5"
FileMatch in ["3ee0d8617ac041793154713e5ef8f319"] with hashAlgorithm = "SHA-1"
FileMatch in ["3ee0d8617ac041793154713e5ef8f319"] with hashAlgorithm = "SHA-256"
FileMatch in ["3ee0d8617ac041793154713e5ef8f319"]
```

If the supplied checksum is different than what’s computed, FileMatch will alert you to the difference.

![The screenshot shows a rule with the DQ status of Rule failed. FileMatch explains the failure.](images/data-quality-file-match.png)

**Optional File-based Rule Tags:**

Tags allow you to control the rule behaviour.

**recentFiles**

This tag limits the number of files processed by keeping the most recent file first.

```
FileMatch "s3://amzn-s3-demo-bucket/file.json" in ["3ee0d8617ac04179sam4713e5ef8f319"] with recentFiles = 1
```

**matchFileName**

This tag ensures that files don’t have duplicate names. Default behavior is false.

```
FileMatch "s3://amzn-s3-demo-bucket/file.json" in ["3ee0d8617ac04179sam4713e5ef8f319"] with matchFileName = "true"
```

There are a few considerations:

1. In AWS Glue ETL, you must have the **EvaluateDataQuality** Transform immediately after an Amazon S3 or
   AWS Glue Data Catalog transform.

![The screenshot shows a rule with the DQ status of Rule failed. FileMatch explains the failure.](images/data-quality-file-match-transform.png) 2. This rule will not work in AWS Glue Interactive Sessions.
