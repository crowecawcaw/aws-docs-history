# AWS Batch IAM execution role

The execution role grants the Amazon ECS container and AWS Fargate agents permission to make
AWS API calls on your behalf.

###### Note

The execution role is supported by Amazon ECS container agent version 1.16.0 and later.

The IAM execution role is required depending on the requirements of your task. You can
have multiple execution roles for different purposes and services associated with your
account.

###### Note

For information about the Amazon ECS instance role, see [Amazon ECS instance role](instance_IAM_role.md "instance_IAM_role.md"). For information about service roles, see [How AWS Batch works with IAM](security_iam_service-with-iam.md "security_iam_service-with-iam.md").

Amazon ECS provides the `AmazonECSTaskExecutionRolePolicy` managed policy. This policy
contains the required permissions for the common use cases described above. It might be
necessary to add inline policies to your execution role for the special use cases outlined
below.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ecr:GetAuthorizationToken",
 "ecr:BatchCheckLayerAvailability",
 "ecr:GetDownloadUrlForLayer",
 "ecr:BatchGetImage",
 "logs:CreateLogStream",
 "logs:PutLogEvents"
 ],
 "Resource": "*"
 }
 ]
}`

```
