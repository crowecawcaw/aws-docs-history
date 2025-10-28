# Setup CSE-KMS

You can enable client-side encryption using AWS KMS (CSE-KMS) in two primary scopes:

- The first is cluster-wide configuration:

```
[
  {
    "Classification":"core-site",
    "Properties": {
       "fs.s3a.encryption.algorithm": "CSE-KMS",
       "fs.s3a.encryption.key":"${KMS_KEY_ID}",
    }
  }
]
```

###### Note

If the AWS KMS key region is different than the S3 bucket/EMR region, you must set the following additional
configuration: `fs.s3a.encryption.cse.kms.region=${KMS_REGION}`.

- The second is job or application-specific configuration. CSE-KMS can be setup for a specific Spark application as
  follows:

```
spark-submit --conf spark.hadoop.fs.s3a.encryption.algorithm=CSE-KMS --conf spark.hadoop.fs.s3a.encryption.key=${`KMS_KEY_ID`}
```
