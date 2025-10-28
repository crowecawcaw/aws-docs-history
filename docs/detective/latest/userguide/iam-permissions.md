# Step 2: Adding the required IAM permissions to your

account in Detective

This topic explains the details of the AWS Identity and Access Management (IAM)
permissions policy that you must add to your IAM identity.

To enable Detective integration with Security Lake, you must attach the following AWS Identity and Access Management (IAM)
permissions policy to your IAM identity.

Attach the following inline policies to the role. Replace
`athena-results-bucket` with your Amazon S3 bucket name if you want to use
your own Amazon S3 bucket to store the Athena query results. If you want Detective to
automatically generate an Amazon S3 bucket to store the Athena query result, remove the entire
`S3ObjectPermissions` from the IAM policy.

If you do not have the required permissions to attach this policy to your IAM identity, contact your AWS administrator. If you have the required permissions but an issue occurs, see [Troubleshoot access denied error messages](../../../IAM/latest/UserGuide/troubleshoot_access-denied.md "../../../IAM/latest/UserGuide/troubleshoot_access-denied.md") in the IAM User Guide.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetBucketLocation",
 "s3:ListAllMyBuckets"
 ],
 "Resource": "*"
 },
 {
 "Sid": "S3ObjectPermissions",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "glue:GetDatabases",
 "glue:GetPartitions",
 "glue:GetTable",
 "glue:GetTables"
 ],
 "Resource": [
 "arn:aws:glue:*:`123456789012`:database/amazon_security_lake*",
 "arn:aws:glue:*:`123456789012`:table/amazon_security_lake*/amazon_security_lake*",
 "arn:aws:glue:*:`123456789012`:catalog"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "athena:BatchGetQueryExecution",
 "athena:GetQueryExecution",
 "athena:GetQueryResults",
 "athena:GetQueryRuntimeStatistics",
 "athena:GetWorkGroup",
 "athena:ListQueryExecutions",
 "athena:StartQueryExecution",
 "athena:StopQueryExecution",
 "lakeformation:GetDataAccess",
 "ram:ListResources"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ssm:GetParametersByPath"
 ],
 "Resource": [
 "arn:aws:ssm:*:`123456789012`:parameter/Detective/SLI"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "cloudformation:GetTemplateSummary",
 "iam:ListRoles"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "organizations:ListDelegatedAdministrators"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "organizations:ServicePrincipal": [
 "securitylake.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```

[Show moreShow less](# "#")
