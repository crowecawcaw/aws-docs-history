# Required roles and permissions for CloudWatch
 canaries

Both the users who create and manage canaries, and the canaries themselves, must have certain
permissions.


## AWS managed policies for
 CloudWatch Synthetics


To add permissions to users, groups, and roles, it is easier to use AWS 
 managed policies than to write policies yourself. It takes time and expertise to create IAM
 customer managed policies that provide your team with only the permissions they need. 
 To get started quickly, you can use our AWS managed policies. These policies cover 
 common use cases and are available in your AWS account. For more information about AWS
 managed policies, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies")
 AWS managed policies in the IAM User Guide.


AWS services maintain and update AWS managed policies. You can't change the 
 permissions in AWS managed policies. Services occasionally change the permissions in an 
 AWS managed policy. This type of update affects all identities 
 (users, groups, and roles) where the policy is attached.


### CloudWatch Synthetics updates to 
 AWS managed policies


View details about updates to AWS managed policies for CloudWatch Synthetics since this
 service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on 
 the CloudWatch Document history page. 




| Change | Description | Date |
| --- | --- | --- |
| Redundant actions removed from **CloudWatchSyntheticsFullAccess** | CloudWatch Synthetics removed the `s3:PutBucketEncryption` and `lambda:GetLayerVersionByArn` actions from **CloudWatchSyntheticsFullAccess** policy because those actions were redundant with other permissions in the policy. The removed actions did not provide any permissions, and there’s no net change to the permissions granted by the policy. | March 12, 2021 |
| CloudWatch Synthetics started tracking changes | CloudWatch Synthetics started tracking changes for its AWS managed policies. | March 10, 2021 | **CloudWatchSyntheticsFullAccess** Here are the contents of the `CloudWatchSyntheticsFullAccess` policy: JSON ``` `{ "Version":"2012-10-17", "Statement": [{ "Effect": "Allow", "Action": [ "synthetics:*" ], "Resource": "*" }, { "Effect": "Allow", "Action": [ "s3:CreateBucket", "s3:PutEncryptionConfiguration" ], "Resource": [ "arn:aws:s3:::cw-syn-results-*" ] }, { "Effect": "Allow", "Action": [ "iam:ListRoles", "s3:ListAllMyBuckets", "xray:GetTraceSummaries", "xray:BatchGetTraces", "apigateway:GET" ], "Resource": "*" }, { "Effect": "Allow", "Action": [ "s3:GetBucketLocation" ], "Resource": "arn:aws:s3:::*" }, { "Effect": "Allow", "Action": [ "s3:GetObject", "s3:ListBucket" ], "Resource": "arn:aws:s3:::cw-syn-*" }, { "Effect": "Allow", "Action": [ "s3:GetObjectVersion" ], "Resource": "arn:aws:s3:::aws-synthetics-library-*" }, { "Effect": "Allow", "Action": [ "iam:PassRole" ], "Resource": [ "arn:aws:iam::*:role/service-role/CloudWatchSyntheticsRole*" ], "Condition": { "StringEquals": { "iam:PassedToService": [ "lambda.amazonaws.com", "synthetics.amazonaws.com" ] } } }, { "Effect": "Allow", "Action": [ "iam:GetRole", "iam:ListAttachedRolePolicies" ], "Resource": [ "arn:aws:iam::*:role/service-role/CloudWatchSyntheticsRole*" ] }, { "Effect": "Allow", "Action": [ "cloudwatch:GetMetricData", "cloudwatch:GetMetricStatistics" ], "Resource": "*" }, { "Effect": "Allow", "Action": [ "cloudwatch:PutMetricAlarm", "cloudwatch:DeleteAlarms" ], "Resource": [ "arn:aws:cloudwatch:*:*:alarm:Synthetics-*" ] }, { "Effect": "Allow", "Action": [ "cloudwatch:DescribeAlarms" ], "Resource": [ "arn:aws:cloudwatch:*:*:alarm:*" ] }, { "Effect": "Allow", "Action": [ "logs:GetLogRecord", "logs:DescribeLogStreams", "logs:StartQuery", "logs:GetLogEvents", "logs:FilterLogEvents", "logs:GetLogGroupFields" ], "Resource": [ "arn:aws:logs:*:*:log-group:/aws/lambda/cwsyn-*" ], "Condition": { "StringEquals": { "aws:ResourceAccount": "${aws:PrincipalAccount}" } } }, { "Effect": "Allow", "Action": [ "lambda:CreateFunction", "lambda:AddPermission", "lambda:PublishVersion", "lambda:UpdateFunctionCode", "lambda:UpdateFunctionConfiguration", "lambda:GetFunctionConfiguration", "lambda:GetFunction", "lambda:DeleteFunction", "lambda:ListTags", "lambda:TagResource", "lambda:UntagResource" ], "Resource": [ "arn:aws:lambda:*:*:function:cwsyn-*" ] }, { "Effect": "Allow", "Action": [ "lambda:GetLayerVersion", "lambda:PublishLayerVersion", "lambda:DeleteLayerVersion" ], "Resource": [ "arn:aws:lambda:*:*:layer:cwsyn-*", "arn:aws:lambda:*:*:layer:Synthetics:*", "arn:aws:lambda:*:*:layer:Synthetics_Selenium:*", "arn:aws:lambda:*:*:layer:AWS-CW-Synthetics*:*" ] }, { "Effect": "Allow", "Action": [ "ec2:DescribeVpcs", "ec2:DescribeSubnets", "ec2:DescribeSecurityGroups" ], "Resource": [ "*" ] }, { "Effect": "Allow", "Action": [ "sns:ListTopics" ], "Resource": [ "*" ] }, { "Effect": "Allow", "Action": [ "sns:CreateTopic", "sns:Subscribe", "sns:ListSubscriptionsByTopic" ], "Resource": [ "arn:*:sns:*:*:Synthetics-*" ] }, { "Effect": "Allow", "Action": [ "kms:ListAliases" ], "Resource": "*" }, { "Effect": "Allow", "Action": [ "kms:DescribeKey" ], "Resource": "arn:aws:kms:*:*:key/*" }, { "Effect": "Allow", "Action": [ "kms:Decrypt" ], "Resource": "arn:aws:kms:*:*:key/*", "Condition": { "StringLike": { "kms:ViaService": [ "s3.*.amazonaws.com" ] } } } ] }` ``` **CloudWatchSyntheticsReadOnlyAccess** Here are the contents of the `CloudWatchSyntheticsReadOnlyAccess` policy: JSON ``` `{ "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [ "synthetics:Describe*", "synthetics:Get*", "synthetics:List*" ], "Resource": "*" } ] }` ```
