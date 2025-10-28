# IAM permissions for pushing an image to an Amazon ECR

private repository

Users need IAM permissions to push images to Amazon ECR private repositories.
Following the best practice of granting least privilege, you can grant access to a
specific repository. You can also grant access to all repositories.

A user must authenticate to each Amazon ECR registry they want to push images to by
requesting an authorization token. Amazon ECR provides several AWS managed policies to
control user access at varying levels. For more information, see [AWS managed policies for Amazon Elastic Container Registry](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

You can also create a your own IAM policies. The following IAM policy grants
the required permissions for pushing an image to a specific repository. To limit the
permissions for a specific repository, use the full Amazon Resource Name (ARN) of
the repository.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ecr:CompleteLayerUpload",
 "ecr:UploadLayerPart",
 "ecr:InitiateLayerUpload",
 "ecr:BatchCheckLayerAvailability",
 "ecr:PutImage",
 "ecr:BatchGetImage"
 ],
 "Resource": "arn:aws:ecr:us-east-1:`111122223333`:repository/`repository-name`"
 },
 {
 "Effect": "Allow",
 "Action": "ecr:GetAuthorizationToken",
 "Resource": "*"
 }
 ]
}`

```

The following IAM policy grants the required permissions for pushing an image to
all repositories.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ecr:CompleteLayerUpload",
 "ecr:GetAuthorizationToken",
 "ecr:UploadLayerPart",
 "ecr:InitiateLayerUpload",
 "ecr:BatchCheckLayerAvailability",
 "ecr:PutImage"
 ],
 "Resource": "arn:aws:ecr:us-west-2:111122223333:repository/*"
 }
 ]
}`

```
