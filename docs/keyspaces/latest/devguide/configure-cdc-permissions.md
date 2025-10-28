# Configure permissions to work with CDC streams in Amazon Keyspaces

To enable CDC streams, the principal, for example
an IAM user or role, needs the following permissions.

For more information about AWS Identity and Access Management, see [AWS Identity and Access Management for Amazon Keyspaces](security-iam.md "security-iam.md").

## Permissions to enable a CDC stream for a table

To enable a CDC stream for an Amazon Keyspaces table, the principal first needs permissions to
create or alter a table and second the permissions to create the service linked role
[AWSServiceRoleForAmazonKeyspacesCDC](using-service-linked-roles-CDC-streams.md#service-linked-role-permissions-CDC-streams "using-service-linked-roles-CDC-streams.md#service-linked-role-permissions-CDC-streams").
Amazon Keyspaces uses the service linked role
to publish CloudWatch metrics into your account on your behalf

The following IAM policy is an example of this.

```
{
    "Version":"2012-10-17",
    "Statement":[
        {
            "Effect":"Allow",
            "Action":[
                "cassandra:Create",
                "cassandra:CreateMultiRegionResource",
                "cassandra:Alter",
                "cassandra:AlterMultiRegionResource"
            ],
            "Resource":[
                "arn:aws:cassandra:`us-east-1`:`111122223333`:/keyspace/`my_keyspace`/*",
                "arn:aws:cassandra:`us-east-1`:`111122223333`:/keyspace/system*"
            ]
        },
        {
            "Sid": "KeyspacesCDCServiceLinkedRole",
            "Effect": "Allow",
            "Action": "iam:CreateServiceLinkedRole",
            "Resource": "arn:aws:iam::*:role/aws-service-role/cassandra-streams.amazonaws.com/AWSServiceRoleForAmazonKeyspacesCDC",
            "Condition": {
              "StringLike": {
                "iam:AWSServiceName": "cassandra-streams.amazonaws.com"
              }
            }
        }
    ]
}
```

To disable a stream, only `ALTER TABLE` permissions are required.

## Permissions to view a CDC stream

To view or list CDC streams, the principal needs read permissions for the system keyspace. For
more information, see [system_schema_mcs](working-with-keyspaces.md#keyspace_system_schema_mcs "working-with-keyspaces.md#keyspace_system_schema_mcs").

The following IAM policy is an example of this.

```
{
   "Version":"2012-10-17",
   "Statement":[
      {
         "Effect":"Allow",
         "Action":"cassandra:Select",
         "Resource":[
             "arn:aws:cassandra:`us-east-1`:`111122223333`:/keyspace/system*"
         ]
      }
   ]
}
```

To view or list CDC streams with the AWS CLI or the Amazon Keyspaces API, the principal needs
additional permissions for the actions `cassandra:ListStreams` and
`cassandra:GetStream`.

The following IAM policy is an example of this.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "cassandra:Select",
        "cassandra:ListStreams",
        "cassandra:GetStream"
      ],
      "Resource": "*"
    }
  ]
}
```

## Permissions to read a CDC stream

To read CDC streams, the principal needs the following permissions.

```
{
   "Version":"2012-10-17",
   "Statement":[
      {
         "Effect":"Allow",
         "Action":[
            "cassandra:GetStream",
            "cassandra:GetShardIterator",
            "cassandra:GetRecords"
         ],
         "Resource":[
            "arn:aws:cassandra:`us-east-1`:`111122223333`:/keyspace/`my_keyspace`/table/`my_table`/stream/`stream_label`"
         ]
      }
   ]
}
```

## Permissions to process Amazon Keyspaces CDC streams with the Kinesis Client Library (KCL)

To process Amazon Keyspaces CDC streams with KCL, the IAM principal needs the following permissions.

- `Amazon Keyspaces` – Read-only access to a specified Amazon Keyspaces CDC stream.
- `DynamoDB` – Permissions to create `shard lease` tables, read and write access to the tables, and
  read-access to the index as required for KCL stream processing.
- `CloudWatch` – Permissions to publish metric data from Amazon Keyspaces CDC streams
  processing with KCL into the namespace of your KCL client application in
  your CloudWatch account. For more information about monitoring, see [Monitor
  the Kinesis Client Library with Amazon CloudWatch](../../../https:/docs.aws.amazon.com/streams/latest/dev/monitoring-with-kcl.md "../../../https:/docs.aws.amazon.com/streams/latest/dev/monitoring-with-kcl.md").

```
{
   "Version":"2012-10-17",
   "Statement":[
      {
         "Effect":"Allow",
         "Action":[
            "cassandra:GetStream",
            "cassandra:GetShardIterator",
            "cassandra:GetRecords"
         ],
         "Resource":[
            "arn:aws:cassandra:`us-east-1`:`111122223333`:/keyspace/`my_keyspace`/table/`my_table`/stream/`stream_label`"
         ]
      },
      {
         "Effect":"Allow",
         "Action":[
            "dynamodb:CreateTable",
            "dynamodb:DescribeTable",
            "dynamodb:UpdateTable",
            "dynamodb:GetItem",
            "dynamodb:UpdateItem",
            "dynamodb:PutItem",
            "dynamodb:DeleteItem",
            "dynamodb:Scan"
         ],
         "Resource":[
            "arn:aws:dynamodb:`us-east-1`:`111122223333`:table/`KCL_APPLICATION_NAME`"
         ]
      },
      {
         "Effect":"Allow",
         "Action":[
            "dynamodb:CreateTable",
            "dynamodb:DescribeTable",
            "dynamodb:GetItem",
            "dynamodb:UpdateItem",
            "dynamodb:PutItem",
            "dynamodb:DeleteItem",
            "dynamodb:Scan"
         ],
         "Resource":[
            "arn:aws:dynamodb:`us-east-1`:`111122223333`:table/`KCL_APPLICATION_NAME`-WorkerMetricStats",
            "arn:aws:dynamodb:`us-east-1`:`111122223333`:table/`KCL_APPLICATION_NAME`-CoordinatorState"
         ]
      },
      {
         "Effect":"Allow",
         "Action":[
            "dynamodb:Query"
         ],
         "Resource":[
            "arn:aws:dynamodb:`us-east-1`:`111122223333`:table/`KCL_APPLICATION_NAME`/index/*"
         ]
      },
      {
         "Effect":"Allow",
         "Action":[
            "cloudwatch:PutMetricData"
         ],
         "Resource":"*"
      }
   ]
}
```
