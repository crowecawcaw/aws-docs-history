

# Policies containing the API operations for creating and using connections
<a name="getresponse-configuring-iam-permissions"></a>

The following sample policy describes the required IAM permissions for creating, managing, and using GetResponse connections within AWS Glue ETL jobs. If you are creating a new role, create a policy that contains the following:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "secretsmanager:DescribeSecret",
        "secretsmanager:GetSecretValue",
        "secretsmanager:PutSecretValue",
        "glue:ListConnectionTypes",
        "glue:DescribeConnectionType",
        "glue:RefreshOAuth2Tokens",
        "glue:ListEntities",
        "glue:DescribeEntity"
      ],
      "Resource": "*"
    }
  ]
}
```

You can also use the following managed IAM policies to allow access:
+ [AWSGlueServiceRole](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole) – Grants access to resources that various AWS Glue processes require to run on your behalf.
+ [AWSGlueConsoleFullAccess](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AWSGlueConsoleFullAccess) – Grants full access to AWS Glue resources when using the AWS Management Console.

If providing Network Options when creating a GetResponse connection, the following actions must also be included in the IAM role:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:CreateNetworkInterface",
        "ec2:DescribeNetworkInterfaces",
        "ec2:DeleteNetworkInterface"
      ],
      "Resource": "*"
    }
  ]
}
```