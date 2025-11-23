# Create a table with a resource-based policy

You can add a resource-based policy while you create a table by using the DynamoDB console,
[CreateTable](../APIReference/API_CreateTable.md "../APIReference/API_CreateTable.md") API, AWS CLI, [AWS
SDK](rbac-attach-resource-based-policy.md#rbac-attach-policy-java-sdk "rbac-attach-resource-based-policy.md#rbac-attach-policy-java-sdk"), or an CloudFormation template.

The following example creates a table named `MusicCollection`
using the `create-table` AWS CLI command. This command also includes the
`resource-policy` parameter that adds a resource-based policy to the table.
This policy allows the user `John` to perform the [RestoreTableToPointInTime](../APIReference/API_RestoreTableToPointInTime.md "../APIReference/API_RestoreTableToPointInTime.md"), [GetItem](../APIReference/API_GetItem.md "../APIReference/API_GetItem.md"), and [PutItem](../APIReference/API_PutItem.md "../APIReference/API_PutItem.md") API actions on the table.

Remember to replace the `italicized` text with your resource-specific information.

```
aws dynamodb create-table \
    --table-name `MusicCollection` \
    --attribute-definitions AttributeName=Artist,AttributeType=S AttributeName=SongTitle,AttributeType=S \
    --key-schema AttributeName=Artist,KeyType=HASH AttributeName=SongTitle,KeyType=RANGE \
    --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 \
    --resource-policy \
        "{
            \"Version\": \"2012-10-17\",
            \"Statement\": [
              {
                    \"Effect\": \"Allow\",
                    \"Principal\": {
                        \"AWS\": \"arn:aws:iam::`123456789012`:user/`John`\"
                    },
                    \"Action\": [
                        \"dynamodb:RestoreTableToPointInTime\",
                        \"dynamodb:GetItem\",
                        \"dynamodb:DescribeTable\"
                    ],
                    \"Resource\": \"arn:aws:dynamodb:us-west-2:`123456789012`:table/`MusicCollection`\"
                }
            ]
        }"
```

1. Sign in to the AWS Management Console and open the DynamoDB console at
   [https://console.aws.amazon.com/dynamodb/](https://console.aws.amazon.com/dynamodb/ "https://console.aws.amazon.com/dynamodb/").
2. On the dashboard, choose **Create table**.
3. In **Table details**, enter the table name, partition key, and
   sort key details.
4. In **Table settings**, choose **Customize
   settings**.
5. (Optional) Specify your options for **Table class**,
   **Capacity calculator**, **Read/write capacity
   settings**, **Secondary indexes**, **Encryption at
   rest**, and **Deletion protection**.
6. In **Resource-based policy**, add a policy to define the access
   permissions for the table and its indexes. In this policy, you specify who has access
   to these resources, and the actions they are allowed to perform on each resource. To
   add a policy, do one of the following:
   - Type or paste a JSON policy document. For details about the IAM policy
     language, see [Creating policies using the JSON editor](../../../IAM/latest/UserGuide/access_policies_create-console.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create-console.md#access_policies_create-json-editor") in the
     _IAM User Guide_.

   ###### Tip

   To see examples of resource-based policies in the Amazon DynamoDB Developer Guide, choose
   **Policy examples**.
   - Choose **Add new statement** to add a new statement and enter
     the information in the provided fields. Repeat this step for as many statements as
     you would like to add.

###### Important

Make sure that you resolve any security warnings, errors, or suggestions before
you save your policy.

The following IAM policy example allows the user
`John` to perform the [RestoreTableToPointInTime](../APIReference/API_RestoreTableToPointInTime.md "../APIReference/API_RestoreTableToPointInTime.md"), [GetItem](../APIReference/API_GetItem.md "../APIReference/API_GetItem.md"), and
[PutItem](../APIReference/API_PutItem.md "../APIReference/API_PutItem.md") API
actions on the table `MusicCollection`.

Remember to replace the `italicized` text with your resource-specific information.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`123456789012`:user/`username`"
 },
 "Action": [
 "dynamodb:RestoreTableToPointInTime",
 "dynamodb:GetItem",
 "dynamodb:PutItem"
 ],
 "Resource": "arn:aws:dynamodb:us-east-1:`123456789012`:table/`MusicCollection`"
 }
 ]
}`

```

7. (Optional) Choose **Preview external access** in the lower-right
   corner to preview how your new policy affects public and cross-account access to your
   resource. Before you save your policy, you can check whether it introduces new
   IAM Access Analyzer findings or resolves existing findings. If you don’t see an active
   analyzer, choose **Go to Access Analyzer** to [create an account analyzer](../../../IAM/latest/UserGuide/access-analyzer-getting-started.md#access-analyzer-enabling "../../../IAM/latest/UserGuide/access-analyzer-getting-started.md#access-analyzer-enabling") in IAM Access Analyzer. For more information, see
   [Preview
   access](../../../IAM/latest/UserGuide/access-analyzer-access-preview.md "../../../IAM/latest/UserGuide/access-analyzer-access-preview.md").
8. Choose **Create table**.

Using the AWS::DynamoDB::Table resource
The following CloudFormation template creates a table with a stream using the [AWS::DynamoDB::Table](../../../AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-table.md") resource. This template also includes
resource-based policies that are attached to both the table and the stream.

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "MusicCollectionTable": {
            "Type": "AWS::DynamoDB::Table",
            "Properties": {
                "AttributeDefinitions": [
                    {
                        "AttributeName": "Artist",
                        "AttributeType": "S"
                    }
                ],
                "KeySchema": [
                    {
                        "AttributeName": "Artist",
                        "KeyType": "HASH"
                    }
                ],
                "BillingMode": "PROVISIONED",
                "ProvisionedThroughput": {
                    "ReadCapacityUnits": 5,
                    "WriteCapacityUnits": 5
                },
                "StreamSpecification": {
                  "StreamViewType": "OLD_IMAGE",
                  "ResourcePolicy": {
                    "PolicyDocument": {
                      "Version": "2012-10-17",
                      "Statement": [
                        {
                            "Principal": {
                                "AWS": "arn:aws:iam::`111122223333`:user/`John`"
                            },
                            "Effect": "Allow",
                            "Action": [
                                "dynamodb:GetRecords",
                                "dynamodb:GetShardIterator",
                                "dynamodb:DescribeStream"
                            ],
                            "Resource": "*"
                        }
                      ]
                    }
                  }
                },
                "TableName": "MusicCollection",
                "ResourcePolicy": {
                    "PolicyDocument": {
                        "Version": "2012-10-17",
                        "Statement": [
                            {
                                "Principal": {
                                    "AWS": [
                                        "arn:aws:iam::`111122223333`:user/`John`"
                                    ]
                                },
                                "Effect": "Allow",
                                "Action": "dynamodb:GetItem",
                                "Resource": "*"
                            }
                        ]
                    }
                }
            }

        }
    }
}
```

Using the AWS::DynamoDB::GlobalTable resource
The following CloudFormation template creates a table with the [AWS::DynamoDB::GlobalTable](../../../AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-dynamodb-globaltable.md") resource and attaches a resource-based
policy to the table and its stream.

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "GlobalMusicCollection": {
            "Type": "AWS::DynamoDB::GlobalTable",
            "Properties": {
                "TableName": "MusicCollection",
                "AttributeDefinitions": [{
                    "AttributeName": "Artist",
                    "AttributeType": "S"
                }],
                "KeySchema": [{
                    "AttributeName": "Artist",
                    "KeyType": "HASH"
                }],
                "BillingMode": "PAY_PER_REQUEST",
                "StreamSpecification": {
                    "StreamViewType": "NEW_AND_OLD_IMAGES"
                },
                "Replicas": [
                    {
                        "Region": "us-east-1",
                        "ResourcePolicy": {
                            "PolicyDocument": {
                                "Version": "2012-10-17",
                                "Statement": [{
                                    "Principal": {
                                        "AWS": [
                                            "arn:aws:iam::`111122223333`:user/`John`"
                                        ]
                                    },
                                    "Effect": "Allow",
                                    "Action": "dynamodb:GetItem",
                                    "Resource": "*"
                                }]
                            }
                        },
                        "ReplicaStreamSpecification": {
                            "ResourcePolicy": {
                                "PolicyDocument": {
                                    "Version": "2012-10-17",
                                    "Statement": [{
                                        "Principal": {
                                            "AWS": "arn:aws:iam::`111122223333`:user/`John`"
                                        },
                                        "Effect": "Allow",
                                        "Action": [
                                            "dynamodb:GetRecords",
                                            "dynamodb:GetShardIterator",
                                            "dynamodb:DescribeStream"
                                        ],
                                        "Resource": "*"
                                    }]
                                }
                            }
                        }
                    }
                ]
            }
        }
    }
}
```
