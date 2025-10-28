#

Policies containing the API operations for creating and using connections

The following sample policy describes the required AWS permissions for creating and
using connections. If you are creating a new role, create a policy that contains the
following:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "glue:ListConnectionTypes",
 "glue:DescribeConnectionType",
 "glue:RefreshOAuth2Tokens",
 "glue:ListEntities",
 "glue:DescribeEntity"
 ],
 "Resource": "*"
 }
 ]
}`

```

If you don't want to use the preceding method, alternatively, use the following
managed IAM policies:

- [AWSGlueServiceRole](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole") – Grants access to resources that
  various AWS Glue processes require to run on your behalf. These resources include
  AWS Glue, Amazon S3, IAM, CloudWatch Logs, and Amazon EC2. If you follow the naming convention for
  resources specified in this policy, AWS Glue processes have the required
  permissions. This policy is typically attached to roles specified when defining
  crawlers, jobs, and development endpoints.
- [AWSGlueConsoleFullAccess](https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AWSGlueConsoleFullAccess "https://console.aws.amazon.com/iam/home#policies/arn:aws:iam::aws:policy/AWSGlueConsoleFullAccess") – Grants full access to AWS Glue
  resources when an identity that the policy is attached to uses the AWS
  Management Console. If you follow the naming convention for resources specified
  in this policy, users have full console capabilities. This policy is typically
  attached to users of the AWS Glue console.
