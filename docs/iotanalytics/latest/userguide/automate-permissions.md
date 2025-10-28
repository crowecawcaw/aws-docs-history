End of support notice:
On December 15, 2025, AWS will end support for AWS IoT Analytics. After December 15, 2025, you will no longer
be able to access the AWS IoT Analytics console, or AWS IoT Analytics resources.
For more information, see
[AWS IoT Analytics end of support](iotanalytics-end-of-support.md "iotanalytics-end-of-support.md").

# Permissions

You must create two roles. One role grants permission to launch a SageMaker AI instance in order
to containerize a notebook. Another role is needed to execute a container.

You can create the first role automatically or manually. If you create your new SageMaker AI
instance with the AWS IoT Analytics console, you are given the option to automatically create a new role
which grants all privileges necessary to execute SageMaker AI instances and containerize notebooks.
Or, you may create a role with these privileges manually. To do this, create a role with the
`AmazonSageMakerFullAccess` policy attached and add the following policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ecr:BatchDeleteImage",
 "ecr:BatchGetImage",
 "ecr:CompleteLayerUpload",
 "ecr:CreateRepository",
 "ecr:DescribeRepositories",
 "ecr:GetAuthorizationToken",
 "ecr:InitiateLayerUpload",
 "ecr:PutImage",
 "ecr:UploadLayerPart"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject"
 ],
 "Resource": "arn:aws:s3:*:*:iotanalytics-notebook-containers/*"
 }
 ]
}`

```

You must manually create the second role which grants permission to execute a container.
You must do this even if you used the AWS IoT Analytics console to create the first role automatically.
Create a role with the following policy and trust policy attached.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetBucketLocation",
 "s3:PutObject",
 "s3:GetObject",
 "s3:PutObjectAcl"
 ],
 "Resource": "arn:aws:s3:*:*:aws-*-dataset-*/*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iotanalytics:*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ecr:GetAuthorizationToken",
 "ecr:GetDownloadUrlForLayer",
 "ecr:BatchGetImage",
 "ecr:BatchCheckLayerAvailability",
 "logs:CreateLogGroup",
 "logs:CreateLogStream",
 "logs:DescribeLogStreams",
 "logs:GetLogEvents",
 "logs:PutLogEvents"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetBucketLocation",
 "s3:ListBucket",
 "s3:ListAllMyBuckets"
 ],
 "Resource": "*"
 }
 ]
}`

```

The following is an example trust policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "",
 "Effect": "Allow",
 "Principal": {
 "Service": ["sagemaker.amazonaws.com", "iotanalytics.amazonaws.com"]
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```
