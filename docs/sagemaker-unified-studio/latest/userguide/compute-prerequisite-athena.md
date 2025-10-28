# Gaining access to Amazon Athena resources

To add Amazon SageMaker Unified Studio connections to existing compute resources,
you must get access information from the admin that owns the resources.
To do this, first get your project ID from the **Project overview** page of the project you want to add resources to.
Then, send the project ID to the owner of the Amazon Athena resources. The Amazon Athena admin uses the project ID to complete some steps so that you receive access details from them,
and then you can input the access information in Amazon SageMaker Unified Studio.

You and the admin must complete different steps depending on whether the resources are
in the same account as the account you are accessing Amazon SageMaker Unified Studio in.

## Gaining access to resources in the same account

In some cases, the Amazon Athena workgroup you want to add to your Amazon SageMaker Unified Studio project might be in the same account as your project. Complete the following steps:

1. Send the project ID to the Amazon Athena admin. You can find this on the **Project overview** page of your Amazon SageMaker Unified Studio project.
2. The admin then adds 1 of the following tags to the Amazon Athena workgroup that you want to add to Amazon SageMaker Unified Studio.
   - Option 1: Add a tag to allow only a specific Amazon SageMaker Unified Studio project to access it: `AmazonDataZoneProject=`projectID``.
   - Option 2: Add a tag to allow all Amazon SageMaker Unified Studio projects in this account to access it: `for-use-with-all-datazone-projects=true`.

## Gaining access to resources in a different account

In some cases, the Amazon Athena workgroup you want to add to your Amazon SageMaker Unified Studio project might be in a different AWS account than your project. Complete the following steps:

1.  Send the following information to the Amazon Athena admin from the **Project overview** page of your Amazon SageMaker Unified Studio project:
    - The Amazon SageMaker Unified Studio project role ARN
    - The Amazon SageMaker Unified Studio project ID
    - The Amazon SageMaker Unified Studio project domain ID

2.  The admin must create an access role for Amazon SageMaker Unified Studio that can be used to query Amazon Athena. The role should have the following permissions:

        * [AmazonAthenaFullAccess](../../../aws-managed-policy/latest/reference/AmazonAthenaFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonAthenaFullAccess.md")
        * SQL Workbench permissions



        ```

        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "SQLWorkBenchActionsWithoutResourceType",
                    "Effect": "Allow",
                    "Action": [
                        "sqlworkbench:PutTab",
                        "sqlworkbench:DeleteTab",
                        "sqlworkbench:DriverExecute",
                        "sqlworkbench:GetUserInfo",
                        "sqlworkbench:ListTabs",
                        "sqlworkbench:GetAutocompletionMetadata",
                        "sqlworkbench:GetAutocompletionResource",
                        "sqlworkbench:PassAccountSettings",
                        "sqlworkbench:ListQueryExecutionHistory",
                        "sqlworkbench:GetQueryExecutionHistory",
                        "sqlworkbench:CreateConnection",
                        "sqlworkbench:PutQCustomContext",
                        "sqlworkbench:GetQCustomContext",
                        "sqlworkbench:DeleteQCustomContext",
                        "sqlworkbench:GetQSqlRecommendations",
                        "sqlworkbench:GetQSqlPromptQuotas",
                        "sqlworkbench:GetSchemaInference"
                    ],
                    "Resource": "*"
                }
            ]
        }

        ```
        * [Optional] Amazon S3 permissions when using specific Amazon Athena workgroup output directory bucket:



        ```

        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "AthenaBucketOut",
                    "Effect": "Allow",
                    "Action": [
                        "s3:Get*",
                        "s3:Put*",
                        "s3:List*"
                    ],
                    "Resource": "arn:aws:s3:::`your-bucket-name`/athena/*"
                }
            ]
        }

        ```

    The trust policy is as follows:

```

# trust policy of access role
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "`project-role-arn`"
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {
                    "sts:ExternalId": "`project-id`"
                }
            }
        },
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "`project-role-arn`"
            },
            "Action": [
                "sts:SetSourceIdentity"
            ],
            "Condition": {
                "StringLike": {
                    "sts:SourceIdentity": "${aws:PrincipalTag/datazone:userId}"
                }
            }
        },
       {
            "Effect": "Allow",
            "Principal": {
                "AWS": "`project-role-arn`"
            },
            "Action": "sts:TagSession",
            "Condition": {
                "StringEquals": {
                    "aws:RequestTag/AmazonDataZoneProject": "`project-id`",
                    "aws:RequestTag/AmazonDataZoneDomain": "`domain-id`"
                }
            }
        }
    ]
}

```

3. The admin then sends you the Access role ARN.

You can then use the access credentials to add the compute connection in Amazon SageMaker Unified Studio. For more information, see [Connecting to an existing Amazon Athena resource](adding-a-existing-athena-connection.md "adding-a-existing-athena-connection.md").
