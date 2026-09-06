

# Creating an AWS DMS replication task with Neptune as the target
<a name="dms-neptune-replication"></a>

Once you have created your table mapping and graph mapping configurations, use the following process to load data from the source store into Neptune. Consult the AWS DMS documentation for more details about the APIs in question.

## Create an AWS DMS replication instance
<a name="dms-neptune-replication-instance"></a>

Create an AWS DMS replication instance in the VPC where your Neptune DB cluster is running (see [Working with an AWS DMS Replication Instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.html) and [CreateReplicationInstance](https://docs.aws.amazon.com/dms/latest/APIReference/API_CreateReplicationInstance.html) in the AWS DMS User Guide). You can use an AWS CLI command like the following to do that:

```
aws dms create-replication-instance \
    --replication-instance-identifier {{(the replication instance identifier)}} \
    --replication-instance-class {{(the size and capacity of the instance, like 'dms.t2.medium')}} \
    --allocated-storage {{(the number of gigabytes to allocate for the instance initially)}} \
    --engine-version {{(the DMS engine version that the instance should use)}} \
    --vpc-security-group-ids {{(the security group to be used with the instance)}}
```

## Create an AWS DMS endpoint for the source database
<a name="dms-neptune-source-endpoint"></a>

The next step is to create an AWS DMS endpoint for your source data store. You can use the AWS DMS [CreateEndpoint](https://docs.aws.amazon.com/dms/latest/APIReference/API_CreateEndpoint.html) API in the AWS CLI like this:

```
aws dms create-endpoint \
    --endpoint-identifier {{(source endpoint identifier)}} \
    --endpoint-type source \
    --engine-name {{(name of source database engine)}} \
    --username {{(user name for database login)}} \
    --password {{(password for login)}} \
    --server-name {{(name of the server)}} \
    --port {{(port number)}} \
    --database-name {{(database name)}}
```

## Set up an Amazon S3 bucket for Neptune to use for staging data
<a name="dms-neptune-s3-staging-bucket"></a>

If you do not have an Amazon S3 bucket that you can use for staging data, create one as explained in [Creating a Bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/CreatingABucket.html) in the Amazon S3 Getting-Started Guide, or [How Do I Create an S3 Bucket?](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket.html) in the Console User Guide.

You will need to create an IAM policy granting `GetObject`, `PutObject`, `DeleteObject` and `ListObject` permissions to the bucket if you do not already have one:

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "ListObjectsInBucket",
      "Effect": "Allow",
      "Action": [
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::{{amzn-s3-demo-bucket}}"
      ]
    },
    {
      "Sid": "AllObjectActions",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "s3:DeleteObject"
      ],
      "Resource": [
        "arn:aws:s3:::{{amzn-s3-demo-bucket}}/*"
      ]
    }
  ]
}
```

------

If your Neptune DB cluster has IAM authentication enabled, you will also need to include the following policy:

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "VisualEditor0",
      "Effect": "Allow",
      "Action": "neptune-db:*",
      "Resource": "arn:aws:neptune-db:{{us-east-1}}:{{111122223333}}:{{cluster-resource-id}}/*"
    }
  ]
}
```

------

Create an IAM role as a trust document to attach the policy to:

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "Service": "dms.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    },
    {
      "Sid": "neptune",
      "Effect": "Allow",
      "Principal": {
        "Service": "rds.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

------

After attaching the policy to the role, attach the role to your Neptune DB cluster. This will allow AWS DMS to use the bucket for staging the data being loaded.

## Create an Amazon S3 endpoint in the Neptune VPC
<a name="dms-neptune-s3-endpoint"></a>

Now create a VPC Gateway endpoint for your intermediary Amazon S3 bucket, in the VPC where your Neptune cluster is located. You can use the AWS Management Console or the AWS CLI to do this, as described in [Creating a gateway endpoint](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-gateway.html#create-gateway-endpoint).

## Create an AWS DMS target endpoint for Neptune
<a name="dms-neptune-target-endpoint"></a>

Create an AWS DMS endpoint for your target Neptune DB cluster. You can use the AWS DMS [CreateEndpoint](https://docs.aws.amazon.com/dms/latest/APIReference/API_CreateEndpoint.html) API with the `NeptuneSettings` parameter like this::

```
aws dms create-endpoint \
    --endpoint-identifier {{(target endpoint identifier)}} \
    --endpoint-type target \
    --engine-name neptune \
    --server-name {{(name of the server)}} \
    --port {{(port number)}} \
    --neptune-settings '{ \
      "ServiceAccessRoleArn": "{{(ARN of the service access role)}}", \
      "S3BucketName": "{{(name of S3 bucket to use for staging files when migrating)}}", \
      "S3BucketFolder": "{{(name of the folder to use in that S3 bucket)}}", \
      "ErrorRetryDuration": {{(number of milliseconds to wait between bulk-load retries)}}, \
      "MaxRetryCount": {{(the maximum number of times to retry a failing bulk-load job)}}, \
      "MaxFileSize": {{(maximum file size, in bytes, of the staging files written to S3)}}, \
      "IamAuthEnabled": {{(set to true if IAM authentication is enabled on the Neptune cluster)}} }'
```

The JSON object passed to the AWS DMS `CreateEndpoint` API in its `NeptuneSettings` parameter has the following fields:
+ **`ServiceAccessRoleArn`**   –   *(required)* The ARN of an IAM role that permits fine-grained access to the S3 bucket used to stage migration of the data into Neptune. This Role should also have permissions to access your Neptune DB cluster if IAM authorization is enabled on it.
+ **`S3BucketName`**   –   *(required)* For Full Load migration, the replication instance converts all RDS data into CSV, quad files and uploads them to this staging bucket in S3 and then bulk-loads them into Neptune.
+ **`S3BucketFolder`**   –   *(required)* The folder to use in the S3 staging bucket.
+ **`ErrorRetryDuration`**   –   *(optional)* The number of milliseconds to wait after a Neptune request fails before making a retry request. The default is 250.
+ **`MaxRetryCount`**   –   *(optional)* The maximum number of retry requests AWS DMS should make after a retryable failure. The default is 5.
+ **`MaxFileSize`**   –   *(optional)* The maximum size in bytes of each staging file saved to S3 during the migration. The default is 1,048,576 KB (1 GB).
+ **`IsIAMAuthEnabled`**   –   *(optional)* Set to `true` if IAM authentication is enabled on the Neptune DB cluster, or `false` if not. The default is `false`.

## Test connections to the new endpoints
<a name="dms-neptune-test-endpoints"></a>

You can test the connection to each of these new endpoints using the AWS DMS [TestConnection](https://docs.aws.amazon.com/dms/latest/APIReference/API_TestConnection.html) API like this:

```
aws dms test-connection \
    --replication-instance-arn {{(the ARN of the replication instance)}} \
    --endpoint-arn {{(the ARN of the endpoint you are testing)}}
```

## Create an AWS DMS replication task
<a name="dms-neptune-replication-task"></a>

Once you have completed the previous steps successfully, create a replication task for migrating data from your source data store to Neptune, using the AWS DMS [CreateReplicationTask](https://docs.aws.amazon.com/dms/latest/APIReference/API_CreateReplicationTask.html.html) API like this:

```
aws dms create-replication-task \
    --replication-task-identifier {{(name for the replication task)}} \
    --source-endpoint-arn {{(ARN of the source endpoint)}} \
    --target-endpoint-arn {{(ARN of the target endpoint)}} \
    --replication-instance-arn {{(ARN of the replication instance)}} \
    --migration-type full-load \
    --table-mappings {{(table-mapping JSON object or URI like 'file:///tmp/table-mappings,json')}} \
    --task-data {{(a GraphMappingConfig object or URI like 'file:///tmp/graph-mapping-config.json')}}
```

The `TaskData` parameter provides the [GraphMappingConfig](dms-neptune-graph-mapping.md) that specifies how the data being copied should be stored in Neptune.

## Start the AWS DMS replication task
<a name="dms-neptune-start-task"></a>

Now you can start the replication task:

```
aws dms start-replication-task
    --replication-task-arn {{(ARN of the replication task started in the previous step)}}
    --start-replication-task-type start-replication
```