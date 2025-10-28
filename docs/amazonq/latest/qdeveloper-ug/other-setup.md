# Using Amazon Q Developer with other services

## AWS Identity and Access Management permissions for other services

For Amazon Q to provide recommendations in the context of another service, you must
enable the correct IAM permissions for either your IAM user or role. You must add the
`codewhisperer:GenerateRecommendations` permission, as outlined in the
sample IAM policy below:

###### Note

The `codewhisperer` prefix is a legacy name from a service that merged
with Amazon Q Developer. For more information, see
[Amazon Q Developer rename - Summary of changes](service-rename.md "service-rename.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AmazonQDeveloperPermissions",
 "Effect": "Allow",
 "Action": ["codewhisperer:GenerateRecommendations"],
 "Resource": "*"
 }
 ]
}`

```

It is best practice to use IAM policies to grant restrictive permissions to IAM
principals. For details about working with IAM, see [Security best practices](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM user guide_.
