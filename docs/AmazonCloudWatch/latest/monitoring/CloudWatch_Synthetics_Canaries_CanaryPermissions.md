# Required roles and permissions for canaries

Each canary must be associated with an IAM role that has certain permissions attached. When you create
 a canary using the CloudWatch console, you can choose for CloudWatch Synthetics to create an IAM role for the canary. If you
 do, the role will have the permissions needed.

If you want to create the IAM role yourself, or create an IAM role that you can use when using the 
 AWS CLI or APIs to create a canary, the role must contain the permissions listed in this section.

All IAM roles for canaries must include the following trust policy statement.


JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "lambda.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```




Additionally, the canary's IAM role needs one of the following statements.

**Basic canary that doesn't use AWS KMS or need Amazon VPC access**


JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::`path/to/your/s3/bucket/canary/results/folder`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetBucketLocation"
 ],
 "Resource": [
 "arn:aws:s3:::`name/of/the/s3/bucket/that/contains/canary/results`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogStream",
 "logs:PutLogEvents",
 "logs:CreateLogGroup"
 ],
 "Resource": [
 "arn:aws:logs:`us-east-1`:`123456789012`:log-group:/aws/lambda/cwsyn-`canary_name`-*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:ListAllMyBuckets",
 "xray:PutTraceSegments"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Resource": "*",
 "Action": "cloudwatch:PutMetricData",
 "Condition": {
 "StringEquals": {
 "cloudwatch:namespace": "CloudWatchSynthetics"
 }
 }
 }
 ]
}`

```




**Canary that uses AWS KMS to encrypt canary artifacts but does not need Amazon VPC access**


JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::`path/to/your/S3/bucket/canary/results/folder`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetBucketLocation"
 ],
 "Resource": [
 "arn:aws:s3:::`name/of/the/S3/bucket/that/contains/canary/results`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogStream",
 "logs:PutLogEvents",
 "logs:CreateLogGroup"
 ],
 "Resource": [
 "arn:aws:logs:`us-east-1`:`123456789012`:log-group:/aws/lambda/cwsyn-`canary_name`-*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:ListAllMyBuckets",
 "xray:PutTraceSegments"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Resource": "*",
 "Action": "cloudwatch:PutMetricData",
 "Condition": {
 "StringEquals": {
 "cloudwatch:namespace": "CloudWatchSynthetics"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": "arn:aws:kms:`us-east-1`:`111122223333`:key/`KMS_key_id`",
 "Condition": {
 "StringEquals": {
 "kms:ViaService": [
 "s3.`us-east-1`.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```




**Canary that does not use AWS KMS but does need Amazon VPC access**


JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::`path/to/your/S3/bucket/canary/results/folder`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetBucketLocation"
 ],
 "Resource": [
 "arn:aws:s3:::`name/of/the/S3/bucket/that/contains/canary/results`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogStream",
 "logs:PutLogEvents",
 "logs:CreateLogGroup"
 ],
 "Resource": [
 "arn:aws:logs:`us-east-1`:`123456789012`:log-group:/aws/lambda/cwsyn-`canary_name`-*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:ListAllMyBuckets",
 "xray:PutTraceSegments"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Resource": "*",
 "Action": "cloudwatch:PutMetricData",
 "Condition": {
 "StringEquals": {
 "cloudwatch:namespace": "CloudWatchSynthetics"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:CreateNetworkInterface",
 "ec2:DescribeNetworkInterfaces",
 "ec2:DeleteNetworkInterface"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```




**Canary that uses AWS KMS to encrypt canary artifacts and also needs Amazon VPC access**

If you update a non-VPC canary to start using a VPC, you'll need to update the canary's role to include the 
 network interface permissions listed in the following policy.


JSON





```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::`path/to/your/S3/bucket/canary/results/folder`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetBucketLocation"
 ],
 "Resource": [
 "arn:aws:s3:::`name/of/the/S3/bucket/that/contains/canary/results`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogStream",
 "logs:PutLogEvents",
 "logs:CreateLogGroup"
 ],
 "Resource": [
 "arn:aws:logs:`us-east-1`:`123456789012`:log-group:/aws/lambda/cwsyn-`canary_name`-*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:ListAllMyBuckets",
 "xray:PutTraceSegments"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Resource": "*",
 "Action": "cloudwatch:PutMetricData",
 "Condition": {
 "StringEquals": {
 "cloudwatch:namespace": "CloudWatchSynthetics"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "ec2:CreateNetworkInterface",
 "ec2:DescribeNetworkInterfaces",
 "ec2:DeleteNetworkInterface"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": "arn:aws:kms:`us-east-1`:`111122223333`:key/`KMS_key_id`",
 "Condition": {
 "StringEquals": {
 "kms:ViaService": [
 "s3.`us-east-1`.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```
