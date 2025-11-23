# Execution roles

An execution role is an AWS Identity and Access Management (IAM) role with a permissions policy that grants Amazon MWAA Serverless permission to invoke the resources of other AWS
services on your behalf. This can include resources such as your Amazon S3 bucket, [AWS KMS key](../../../kms/latest/developerguide/concepts.md#aws-owned-cmk "../../../kms/latest/developerguide/concepts.md#aws-owned-cmk"), and CloudWatch Logs. Amazon MWAA Serverless needs one execution role per workflow. This topic describes how to use and configure the execution role to allow Amazon MWAA Serverless
to access other AWS resources that are required by the workflow.

Amazon MWAA Serverless workflows aquire permissions to use other AWS services from the execution role. You must grant following permissions to Amazon MWAA Serverless execution role to allow your workflos to use these AWS services:

- Amazon CloudWatch (CloudWatch) to send Amazon MWAA Serverless workflow task logs to customer provided log group.
- AWS Key Management Service (AWS KMS) for data encryption (using either an [AWS-owned key](../../../kms/latest/developerguide/concepts.md#aws-owned-cmk "../../../kms/latest/developerguide/concepts.md#aws-owned-cmk") or your [Customer managed key](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk")).

###### Note

In order for your workflow's execution role to access arbitrary KMS keys, a KMS key in a third-party account must allow this cross-account
access via its resource policy.

After you choose an encryption option, you cannot change your selection for an existing workflow.

## Create an execution role

You use the IAM console to create a new execution role. When you create a new execution role, do not reuse the name of a deleted execution role. Unique
names can help prevent conflicts and ensure proper resource management.

To create a new execution role, follow these steps:

1. Open the IAM console ([https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/")).
2. In the navigation pane, choose **Roles**.
3. Choose **Create role**.
4. For **Trusted entity type**, choose **AWS service**.
5. For **Service or use case**, choose **Amazon MWAA Serverless**. Then choose **Amazon MWAA Serverless workflow**.
6. Choose **Next**.
7. For Permissions policies, search for **your customer managed policy**.
8. Choose the check box to the left of the **policy**, then choose Next.
9. For Role Name, enter **role name**, then choose **Create role**.

You can change the execution role for your workflow at any time. If a new execution role is not already
associated with your workflow, use the steps on this page to create a new execution role policy, and associate the role to your workflow.

## Update an execution role

Amazon MWAA Serverless can't add or edit permission policies to an existing execution role. You must update your execution role with additional permission policies needed by
your workflow when you update that workflow. For example, if your DAG requires access to AWS Glue, Amazon MWAA Serverless can't automatically detect these permissions are
required by your workflow, or add the permissions to your execution role.

You can add permissions to an execution role in two ways:

- By modifying the JSON policy for your execution role inline. You can use the sample
  [JSON policy documents](../../../IAM/latest/UserGuide/reference_policies_grammar.md "../../../IAM/latest/UserGuide/reference_policies_grammar.md") on this page to either add
  to or replace the JSON policy of your execution role on the IAM console.
- By creating a JSON policy for an AWS service and attaching it to your execution role. You can use the steps on this page to associate a new
  JSON policy document for an AWS service to your execution role on the IAM console.

To view the execution role and update the JSON policy for the role on the IAM console:

1. Open the [IAM console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Choose the execution role name to open the permissions policy.
3. Choose **Edit policy**.
4. Choose the **JSON** tab.
5. Update your JSON policy.
6. Choose **Review policy**.
7. Choose **Save changes**.

Assuming the execution role is already associated with your workflow, Amazon MWAA Serverless can start using the added permission policies immediately.
This also means if you remove any required permissions from an execution role, your workflow might fail.

## Attach a JSON policy to use other AWS services

You can create a JSON policy for an AWS service and attach it to your execution role. For example, you can attach the following JSON policy to
grant read-only access to all resources in Amazon EC2.

JSON

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ec2:Describe*",
                "ec2:GetSecurityGroupsForVpc"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "elasticloadbalancing:Describe*",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "cloudwatch:ListMetrics",
                "cloudwatch:GetMetricStatistics",
                "cloudwatch:Describe*"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "autoscaling:Describe*",
            "Resource": "*"
        }
    ]
}

```

To attach a policy to your execution role:

1. Open the [IAM console](https://console.aws.amazon.com/iam "https://console.aws.amazon.com/iam").
2. Choose your execution role.
3. Choose **Attach policies**.
4. Choose **Create policy**.
5. Choose **JSON**.
6. Paste the JSON policy.
7. Choose **Next: Tags**, **Next: Review**.
8. Enter a descriptive name (such as `SecretsManagerReadPolicy`) and a description for the policy.
9. Choose **Create policy**.

## Sample JSON policies for an execution role

The sample permission policies in this section show the policy to create a new execution role that can be uses for your workflow. These policies contain
[Resource ARN](../../../IAM/latest/UserGuide/reference_policies_elements_resource.md "../../../IAM/latest/UserGuide/reference_policies_elements_resource.md") placeholders for Apache Airflow log groups, an
[Amazon S3 bucket](mwaas-s3-bucket.md "mwaas-s3-bucket.md").

### Sample policy for for Amazon S3 operations

The following example shows an execution role policy you can use for a S3 operations.

###### Note

CloudWatchLogsAccess and VPCAccess are required for all operations, while KMSAccess is optional.

JSON

```

    {
    "Version": "2012-10-17",
    "Statement": [
        {
        "Sid": "S3OperationSpecificPermissions",
        "Effect": "Allow",
        "Action": [
            "s3:*"
        ],
        "Resource": "*"
        },
        {
        "Sid": "CloudWatchLogsAccess",
        "Effect": "Allow",
        "Action": [
            "logs:CreateLogStream",
            "logs:PutLogEvents"
        ],
        "Resource": "*"
        },
        {
        "Sid": "KmsAccess",
        "Effect": "Allow",
        "Action": [
            "kms:Encrypt",
            "kms:Decrypt",
            "kms:GenerateDataKey",
            "kms:DescribeKey"
        ],
        "Resource": "arn:aws:kms:`us-east-1`:`111122223333`:key/`keyId`"
        }
    ]
    }

```

Next, you need to allow Amazon MWAA Serverless to assume this role in order to perform actions on your behalf. This can be done by adding the
`"airflow-serverless.amazonaws.com"` service principal to the list of trusted entities for this execution role
[using the IAM
console](../../../IAM/latest/UserGuide/id_roles_create_for-service.md#roles-creatingrole-service-console "../../../IAM/latest/UserGuide/id_roles_create_for-service.md#roles-creatingrole-service-console"), or by placing these service principals in the assume role policy document for this execution role via the IAM
[create-role](../../../cli/latest/reference/iam/create-role.md "../../../cli/latest/reference/iam/create-role.md") command using the AWS CLI.
A sample assume role policy document can be found below:

JSON

```

    {
    "Version": "2012-10-17",
    "Statement": [
        {
        "Sid": "AllowAirflowServerlessAssumeRole",
        "Effect": "Allow",
        "Principal": {
            "Service": "airflow-serverless.amazonaws.com"
        },
        "Action": "sts:AssumeRole"
        }
    ]
    }

```
