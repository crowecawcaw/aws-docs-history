# Private repository policies in Amazon ECR

Amazon ECR uses resource-based permissions to control access to repositories. Resource-based
permissions let you specify which users or roles have access to a repository and what
actions they can perform on the repository. By default, only the AWS account that created the
repository has access to the repository. You can apply a repository policy that allows additional
access to your repository.

###### Topics

- [Repository policies vs IAM policies](#repository-policy-vs-iam-policy "#repository-policy-vs-iam-policy")
- [Private repository policy examples in Amazon ECR](repository-policy-examples.md "repository-policy-examples.md")
- [Setting a private repository policy statement in Amazon ECR](set-repository-policy.md "set-repository-policy.md")

## Repository policies vs IAM policies

Amazon ECR repository policies are a subset of IAM policies that are scoped for, and
specifically used for, controlling access to individual Amazon ECR repositories. IAM
policies are generally used to apply permissions for the entire Amazon ECR service but can
also be used to control access to specific resources as well.

Both Amazon ECR repository policies and IAM policies are used when determining which
actions a specific user or role may perform on a repository. If a user or role is
allowed to perform an action through a repository policy but is denied permission
through an IAM policy (or vice versa) then the action will be denied. A user or role
only needs to be allowed permission for an action through either a repository policy or
an IAM policy but not both for the action to be allowed.

###### Important

Amazon ECR requires that users have permission to make calls to the
`ecr:GetAuthorizationToken` API through an IAM policy before they
can authenticate to a registry and push or pull any images from any Amazon ECR
repository. Amazon ECR provides several managed IAM policies to control user access at
varying levels. For more information, see [Amazon Elastic Container Registry Identity-based policy examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

You can use either of these policy types to control access to your repositories, as
shown in the following examples.

This example shows an Amazon ECR repository policy, which allows for a specific user to
describe the repository and the images within the repository.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ECRRepositoryPolicy",
 "Effect": "Allow",
 "Principal": {"AWS": "arn:aws:iam::`111122223333`:user/`username`"},
 "Action": [
 "ecr:DescribeImages",
 "ecr:DescribeRepositories"
 ],
 "Resource": "*"
 }
 ]
}`

```

This example shows an IAM policy that achieves the same goal as above, by scoping
the policy to a repository (specified by the full ARN of the repository) using the
resource parameter. For more information about Amazon Resource Name (ARN) format, see
[Resources](security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-resources "security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-resources").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowDescribeRepoImage",
 "Effect": "Allow",
 "Action": [
 "ecr:DescribeImages",
 "ecr:DescribeRepositories"
 ],
 "Resource": ["arn:aws:ecr:us-east-1:`111122223333`:repository/`repository-name`"]
 }
 ]
}`

```
