

# Get data into S3 Express One Zone with EMR Serverless
<a name="upload-data"></a>

With Amazon EMR releases 7.2.0 and higher, use EMR Serverless with the [Amazon S3 Express One Zone](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-one-zone.html) storage class for improved performance when you run jobs and workloads. S3 Express One Zone is a a high-performance, single-zone Amazon S3 storage class that delivers consistent, single-digit millisecond data access for most latency-sensitive applications. At the time of its release, S3 Express One Zone delivers the lowest latency and highest performance cloud object storage in Amazon S3.

## Prerequisites
<a name="upload-data-prereqs"></a>
+ S3 Express One Zone permissions – When S3 Express One Zone initially performs an action like `GET`, `LIST`, or `PUT` on an S3 object, the storage class calls `CreateSession` on your behalf. Your IAM policy must allow the `s3express:CreateSession` permission so that the S3A connector can invoke the `CreateSession` API. For an example policy with this permission, refer to [Getting started with S3 Express One Zone](#upload-data-get-started).
+ S3A connector – To configure Spark to access data from an Amazon S3 bucket that uses the S3 Express One Zone storage class, use the Apache Hadoop connector S3A. To use the connector, ensure all S3 URIs use the `s3a` scheme. If they don’t, change the filesystem implementation that you use for `s3` and `s3n` schemes.

To change the `s3` scheme, specify the following cluster configurations: 

```
[
  {
    "Classification": "core-site",
    "Properties": {
      "fs.s3.impl": "org.apache.hadoop.fs.s3a.S3AFileSystem",
      "fs.AbstractFileSystem.s3.impl": "org.apache.hadoop.fs.s3a.S3A"
    }
  }
]
```

To change the `s3n` scheme, specify the following cluster configurations: 

```
[
  {
    "Classification": "core-site",
    "Properties": {
      "fs.s3n.impl": "org.apache.hadoop.fs.s3a.S3AFileSystem",
      "fs.AbstractFileSystem.s3n.impl": "org.apache.hadoop.fs.s3a.S3A"
    }
  }
]
```

## Getting started with S3 Express One Zone
<a name="upload-data-get-started"></a>

Follow these steps to get started with S3 Express One Zone.

1. [ Create a VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#create-interface-endpoint-aws). Add the endpoint ` com.amazonaws.us-west-2.s3express` to the VPC endpoint.

1. Follow [ Getting started with Amazon EMR Serverless](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/getting-started.html) to create an application with Amazon EMR release label 7.2.0 or higher.

1. [ Configure your application](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/vpc-access.html) to use the newly created VPC endpoint, a private subnet group, and a security group.

1. Add the `CreateSession` permission to your job execution role.

------
#### [ JSON ]

****  

   ```
   {
     "Version":"2012-10-17",		 	 	 
     "Statement": [
       {
         "Effect": "Allow",
         "Resource": [
           "*"
         ],
         "Action": [
           "s3express:CreateSession"
         ],
         "Sid": "AllowS3EXPRESSCreatesession"
       }
     ]
   }
   ```

------

1. Run your job. Note that use the `S3A` scheme to access S3 Express One Zone buckets.

   ```
   aws emr-serverless start-job-run \      
   --application-id {{<application-id>}} \          
   --execution-role-arn {{<job-role-arn>}} \
   --name {{<job-run-name>}} \
   --job-driver '{
    "sparkSubmit": {                                                                                                                                                                                      
    "entryPoint": "s3a://{{<DOC-EXAMPLE-BUCKET>}}/scripts/wordcount.py", 
    "entryPointArguments":["s3a://{{<DOC-EXAMPLE-BUCKET>}}/emr-serverless-spark/output"],
    "sparkSubmitParameters": "--conf spark.executor.cores=4 
    --conf spark.executor.memory=8g --conf spark.driver.cores=4 
    --conf spark.driver.memory=8g --conf spark.executor.instances=2 
    --conf spark.hadoop.fs.s3a.change.detection.mode=none 
    --conf spark.hadoop.fs.s3a.endpoint.region={{{<AWS_REGION>}}}
    --conf spark.hadoop.fs.s3a.select.enabled=false 
    --conf spark.sql.sources.fastS3PartitionDiscovery.enabled=false 
    }'
   ```