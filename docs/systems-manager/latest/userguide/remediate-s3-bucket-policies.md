# S3 bucket policies for the unified Systems Manager

console

This topic includes the Amazon S3 bucket policies created by Systems Manager when you onboard an
organization or single account to the unified Systems Manager console.

###### Warning

Modifying the default bucket policy might allow member accounts in an organization
to discover one another, or read diagnosis outputs for instances in another account.
We recommend using extreme caution if you choose to modify this policy.

The diagnosis bucket is created with the following default bucket policy when
onboarding an organization to Systems Manager.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DenyHTTPRequests",
 "Effect": "Deny",
 "Principal": "*",
 "Action": "s3:*",
 "Resource": [
 "arn:aws:s3:::",
 "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
 ],
 "Condition": {
 "Bool": {
 "aws:SecureTransport": "false"
 }
 }
 },
 {
 "Sid": "DenyNonSigV4Requests",
 "Effect": "Deny",
 "Principal": "*",
 "Action": "s3:*",
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
 ],
 "Condition": {
 "StringNotEquals": {
 "s3:SignatureVersion": "AWS4-HMAC-SHA256"
 }
 }
 },
 {
 "Sid": "AllowAccessLog",
 "Effect": "Allow",
 "Principal": {
 "Service": "logging.s3.amazonaws.com"
 },
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`/access-logs/*",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`000000000000`"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:s3:::`amzn-s3-demo-bucket`"
 }
 }
 },
 {
 "Sid": "AllowCrossAccountRead",
 "Effect": "Allow",
 "Principal": "*",
 "Action": "s3:GetObject",
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`/actions/*/${aws:PrincipalAccount}/*",
 "Condition": {
 "StringEquals": {
 "aws:PrincipalOrgID": "`organization-id`"
 }
 }
 },
 {
 "Sid": "AllowCrossAccountWrite",
 "Effect": "Allow",
 "Principal": "*",
 "Action": [
 "s3:PutObject",
 "s3:DeleteObject"
 ],
 "Resource": "arn:aws:s3:::bucket-name/actions/*/${aws:PrincipalAccount}/*",
 "Condition": {
 "StringEquals": {
 "aws:PrincipalOrgID": "organization-id"
 },
 "ArnLike": {
 "aws:PrincipalArn": [
 "arn:aws:iam::*:role/AWS-SSM-DiagnosisExecutionRole-`operational-account-id-home-region`",
 "arn:aws:iam::*:role/AWS-SSM-DiagnosisAdminRole-`operational-account-id-home-region`",
 "arn:aws:iam::*:role/AWS-SSM-RemediationExecutionRole-`operational-account-id-home-region`",
 "arn:aws:iam::*:role/AWS-SSM-RemediationAdminRole-`operational-account-id-home-region`"
 ]
 }
 }
 },
 {
 "Sid": "AllowCrossAccountListUnderAccountOwnPrefix",
 "Effect": "Allow",
 "Principal": "*",
 "Action": "s3:ListBucket",
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "Condition": {
 "StringEquals": {
 "aws:PrincipalOrgID": "`organization-id`"
 },
 "StringLike": {
 "s3:prefix": "*/${aws:PrincipalAccount}/*"
 }
 }
 },
 {
 "Sid": "AllowCrossAccountGetConfigWithinOrganization",
 "Effect": "Allow",
 "Principal": "*",
 "Action": "s3:GetEncryptionConfiguration",
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "Condition": {
 "StringEquals": {
 "aws:PrincipalOrgID": "`organization-id`"
 }
 }
 }
 ]
}`

```

The diagnosis bucket is created with the following default bucket policy when
onboarding a single account to Systems Manager.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DenyHTTPRequests",
 "Effect": "Deny",
 "Principal": "*",
 "Action": "s3:*",
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
 ],
 "Condition": {
 "Bool": {
 "aws:SecureTransport": "false"
 }
 }
 },
 {
 "Sid": "DenyNonSigV4Requests",
 "Effect": "Deny",
 "Principal": "*",
 "Action": "s3:*",
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`",
 "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
 ],
 "Condition": {
 "StringNotEquals": {
 "s3:SignatureVersion": "AWS4-HMAC-SHA256"
 }
 }
 }
 ]
}`

```
