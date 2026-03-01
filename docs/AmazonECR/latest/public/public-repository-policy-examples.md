# Public repository policy examples in Amazon ECR Public

The following examples show policy statements that you use to control the permissions
that users have to your public repositories.

###### Note

All public repositories are visible on the Amazon ECR Public Gallery. Using a repository
policy to deny access to view or pull from a public repository is not supported.

###### Important

Amazon ECR requires that users have permission to make calls to the
`ecr-public:GetAuthorizationToken` and `sts:GetServiceBearerToken` API through an IAM policy before they
can authenticate to a registry and push any images to an Amazon ECR
repository.

## Example: Allow an IAM user within your account

The following repository policy allows users within your account to push
images.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowPush",
 "Effect": "Allow",
 "Principal": {
 "AWS": [
 "arn:aws:iam::`111122223333`:user/`push-pull-user-1`",
 "arn:aws:iam::`111122223333`:user/`push-pull-user-2`"
 ]
 },
 "Action": [
 "ecr-public:BatchCheckLayerAvailability",
 "ecr-public:PutImage",
 "ecr-public:InitiateLayerUpload",
 "ecr-public:UploadLayerPart",
 "ecr-public:CompleteLayerUpload"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Example: Allow another account

The following repository policy allows a specific account to push images.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowCrossAccountPush",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action": [
 "ecr-public:BatchCheckLayerAvailability",
 "ecr-public:PutImage",
 "ecr-public:InitiateLayerUpload",
 "ecr-public:UploadLayerPart",
 "ecr-public:CompleteLayerUpload"
 ],
 "Resource": "*"
 }
 ]
}`

```
