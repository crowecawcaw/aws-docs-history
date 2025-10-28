NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Deploy permissions using a AWS CloudFormation template

Alternatively, see the [previous section](create-permissions-manually.md "create-permissions-manually.md") to deploy these permissions manually.

1. To configure the required IAM roles and policies, after replacing the described parameters,
   save the following AWS CloudFormation JSON template to a text file called `aws-mgn-connector-iam-principals.json`
   on your local system:
   1. Replace the example account number **111122223333** with your account number.
   2. Replace **ROLE-NAME** with the user role that serves as the trusted entity. This user role assumes the **MGNConnectorInstallerRole** role and can install the connector.
   3. Replace the example region **us-east-2** with the Region of the account.
   4. Replace **LOGS-BUCKET** with the S3 logs bucket name. Remove the relevant item from the statement if you have not set up outputting logs to S3.

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "IAM Roles for AWS Application Migration Connector",
    "Resources": {
        "MGNConnectorInstallerRole": {
            "Type": "AWS::IAM::Role",
            "Properties": {
                "AssumeRolePolicyDocument": {
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Effect": "Allow",
                            "Principal": {
                                "AWS": "arn:aws:iam::`111122223333`:`ROLE-NAME`"
                            },
                            "Action": "sts:AssumeRole"
                        }
                    ]
                },
                "Policies": [
                    {
                        "PolicyName": "MGNConnectorInstallerPolicy",
                        "PolicyDocument": {
                            "Version": "2012-10-17",
                            "Statement": [
                                {
                                    "Effect": "Allow",
                                    "Action": "mgn:TagResource",
                                    "Resource": "arn:aws:mgn:*:*:connector/*",
                                    "Condition": {
                                        "StringEquals": {
                                            "mgn:CreateAction": "CreateConnector"
                                        }
                                    }
                                },
                                {
                                    "Effect": "Allow",
                                    "Action": "mgn:CreateConnector",
                                    "Resource": "*"
                                }
                            ]
                        }
                    }
                ]
            }
        },
        "AWSApplicationMigrationConnectorManagementRole": {
            "Type": "AWS::IAM::Role",
            "Properties": {
                "AssumeRolePolicyDocument": {
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Effect": "Allow",
                            "Principal": {
                                "Service": "ssm.amazonaws.com"
                            },
                            "Action": "sts:AssumeRole"
                        }
                    ]
                },
                "ManagedPolicyArns": [
                    "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore"
                ],
                "Policies": [
                    {
                        "PolicyName": "MgnConnectorPolicy",
                        "PolicyDocument": {
                            "Version": "2012-10-17",
                            "Statement": [
                                {
                                    "Effect": "Allow",
                                    "Action": [
                                        "logs:CreateLogGroup",
                                        "logs:CreateLogStream",
                                        "logs:DescribeLogGroups",
                                        "logs:DescribeLogStreams",
                                        "logs:PutLogEvents"
                                    ],
                                    "Resource": "*"
                                },
                                {
                                    "Action": [
                                        "s3:GetObject"
                                    ],
                                    "Resource": [
                                        "arn:aws:s3:::`aws-application-migration-service-us-east-2`/latest/source-automation-client/linux/ssaf-client/ssaf_client",
                                        "arn:aws:s3:::`us-east-2`/*"
                                    ],
                                    "Effect": "Allow"
                                },
                                {
                                    "Action": [
                                        "s3:PutObject"
                                    ],
                                    "Resource": "arn:aws:s3:::`LOGS-BUCKET`/*",
                                    "Effect": "Allow"
                                },
                                {
                                    "Effect": "Allow",
                                    "Action": "sts:AssumeRole",
                                    "Resource": "arn:aws:iam::*:role/`AWSApplicationMigrationConnectorSharingRole_111122223333`"
                                },
                                {
                                    "Effect": "Allow",
                                    "Action": "secretsmanager:GetSecretValue",
                                    "Resource": "arn:aws:secretsmanager:*:*:secret:*",
                                    "Condition": {
                                        "Null": {
                                            "aws:ResourceTag/AWSApplicationMigrationServiceManaged": "false"
                                        }
                                    }
                                }
                            ]
                        }
                    }
                ]
            }
        }
    }
}

```

2. Create a stack:

Via AWS CloudFormation console

    1. **Stacks → Create stack → With new resources (standard)**
    2. Under **Specify template** select **Upload a template file**
    3. Click **Choose file** and select the template file `aws-mgn-connector-iam-principals.json` in the dialog.
    4. Click **Next**.
    5. In the following screen, choose a name for your CloudFormation stack (for example: `aws-mgn-connector-iam-principals-stack`) and click **Next**.
    6. Click **Next** again.
    7. Acknowledge the required capabilities and click on **Submit**.
    8. Wait for the stack to finish creation.

Via AWS CLI

    1. Using the following command:



    ```

    aws cloudformation deploy --stack-name aws-mgn-connector-iam-principals-stack --capabilities CAPABILITY_NAMED_IAM --region <AWS_REGION> --template-file <PATH_TO_TEMPLATE_FILE>

    ```
    2. Replace `<AWS_REGION>` with the AWS region you will be deploying in and `<PATH_TO_TEMPLATE_FILE>` with the CloudFormation template file path.
    3. Wait for the stack to finish creation.
