

# Policies containing the API operations for creating and using connections
<a name="workday-ldq-configuring-iam-permissions"></a>

The following sample policy describes the required AWS IAM permissions for creating and using connections. If you are creating a new role, create a policy that contains the following:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "glue:ListConnectionTypes",
                "glue:DescribeConnectionType",
                "glue:ListEntities",
                "glue:DescribeEntity",
                "glue:CreateConnection",
                "glue:GetConnection",
                "glue:TestConnection"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::123456789012:role/glue-role",
            "Condition": {
                "StringEquals": { "iam:PassedToService": "glue.amazonaws.com" }
            }
        }
    ]
}
```

If you don't want to use the preceding method, alternatively use the following managed IAM policies:
+ [AWSGlueServiceRole](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole) – Grants access to resources that various AWS Glue processes require to run on your behalf. These resources include AWS Glue, Amazon S3, IAM, CloudWatch Logs, and Amazon EC2. This policy is typically attached to roles specified when defining crawlers, jobs, and development endpoints.
+ [AWSGlueConsoleFullAccess](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AWSGlueConsoleFullAccess) – Grants full access to AWS Glue resources when you use the console. This policy is typically attached to users of the AWS Glue console.

The IAM role that your connection uses and the IAM role associated with your AWS Glue job also need permission to read the AWS Secrets Manager secret that stores your Workday credentials. For more information, see [Configuring Workday Live Data Query connections](workday-ldq-configuring-connections.md).