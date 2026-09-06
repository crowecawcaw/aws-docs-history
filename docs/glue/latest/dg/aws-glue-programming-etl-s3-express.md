

# Using Amazon S3 Express One Zone with AWS Glue
<a name="aws-glue-programming-etl-s3-express"></a>

With AWS Glue version 5.1 and higher, you can read and write data in [Amazon S3 Express One Zone](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-high-performance.html#s3-express-one-zone) directory buckets from your ETL jobs. S3 Express One Zone is a high-performance, single-zone Amazon S3 storage class that delivers consistent, single-digit millisecond data access for latency-sensitive applications.

## Prerequisites
<a name="aws-glue-programming-etl-s3-express-prereqs"></a>

Before you can use S3 Express One Zone with AWS Glue, you must have the following:
+ An AWS Glue job running version 5.1 or higher.
+ An S3 directory bucket created in the same region as your AWS Glue job. Directory buckets do not support cross-region access. For more information, see [Creating directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-create.html) in the *Amazon S3 User Guide*.
+ The `s3express:CreateSession` permission on your IAM role. When S3 Express One Zone performs an action on a directory bucket, it calls `CreateSession` on your behalf.

## IAM permissions
<a name="aws-glue-programming-etl-s3-express-iam"></a>

Add the following permission to your AWS Glue job's IAM role to allow access to S3 Express One Zone directory buckets:

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3express:CreateSession",
            "Resource": "arn:aws:s3express:*:*:bucket/{{EXAMPLE-BUCKET}}--{{az-id}}--x-s3"
        }
    ]
}
```

Replace {{EXAMPLE-BUCKET}} with your directory bucket name and {{az-id}} with the Availability Zone ID (for example, `use1-az4`).

## Reading and writing data
<a name="aws-glue-programming-etl-s3-express-usage"></a>

AWS Glue version 5.1\+ supports accessing S3 Express One Zone directory buckets using both the `s3://` and `s3a://` URI schemes. No additional configuration is required.

The following example shows how to read and write data from an S3 Express One Zone directory bucket in a AWS Glue ETL job:

```
import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext

sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# S3 Express One Zone directory bucket path
express_path = "s3://EXAMPLE-BUCKET--use1-az4--x-s3/my-data/"

# Read data from S3 Express One Zone
df = spark.read.parquet(express_path)

# Write data to S3 Express One Zone
df.write.mode("overwrite").parquet(express_path + "output/")
```

You can also use DynamicFrames with S3 Express One Zone:

```
# Read with DynamicFrame
dynamicFrame = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [express_path]},
    format="parquet"
)

# Write with DynamicFrame
glueContext.write_dynamic_frame.from_options(
    frame=dynamicFrame,
    connection_type="s3",
    connection_options={"path": express_path + "output/"},
    format="parquet"
)
```