# IAM permissions required for enhanced scanning in Amazon ECR

Amazon ECR enhanced scanning requires an Amazon Inspector service-linked IAM role and that the
IAM principal enabling and using enhanced scanning has permissions to call the
Amazon Inspector APIs needed for scanning. The Amazon Inspector service-linked IAM role is created
automatically by Amazon Inspector when enhanced scanning is turned on for your private
registry. For more information, see [Using service-linked
roles for Amazon Inspector](../../../inspector/latest/user/using-service-linked-roles.md "../../../inspector/latest/user/using-service-linked-roles.md") in the _Amazon Inspector User Guide_.

The following IAM policy grants the required permissions for enabling and using
enhanced scanning. It includes the permission needed for Amazon Inspector to create the
service-linked IAM role as well as the Amazon Inspector API permissions needed to turned on
and off enhanced scanning and retrieve the scan findings.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "inspector2:Enable",
 "inspector2:Disable",
 "inspector2:ListFindings",
 "inspector2:ListAccountPermissions",
 "inspector2:ListCoverage"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:AWSServiceName": [
 "inspector2.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```
