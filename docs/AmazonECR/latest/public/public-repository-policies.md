# Public repository policies in Amazon ECR Public

Amazon ECR uses resource-based permissions to control access to public repositories. When a
public repository is created, it is publicly visible on the Amazon ECR Public Gallery and anyone
can pull images from the repository. By default however, only the repository owner has
access to push to the repository. With resource-based permissions, you specify which users,
or roles have access to push to a public repository and what additional actions they can
perform on it. You can apply a policy document to allow additional permissions to your
repository.

###### Note

All public repositories are visible on the Amazon ECR Public Gallery. Using a repository
policy to deny access to view or pull from a public repository is not supported.

## Repository policies vs IAM policies

Amazon ECR public repository policies are a subset of IAM policies that are both scoped
for and specifically used for controlling access to individual Amazon ECR repositories. In
general, you use IAM policies to apply permissions for the entire Amazon ECR service.
However, you can also use IAM policies to control access to specific resources.

For determining which actions a specific IAM user or role might perform on a
repository, you use both Amazon ECR repository policies and IAM policies. If a user or role
is allowed to perform an action through a repository policy but is denied permission
through an IAM policy, the action is denied. Similarly, if a user or role is denied
permission through an IAM policy even though that identity is allowed to perform an
action, the action is denied. You can grant a user or role permission for an action
through either a repository policy or an IAM policy, but you can't grant permission
both ways.

###### Important

Amazon ECR requires that users have permission to make calls to the
`ecr-public:GetAuthorizationToken` and `sts:GetServiceBearerToken` API through an IAM policy before they
can authenticate to a registry and push any images to an Amazon ECR
repository.

You can use either of these policy types to control access to your public
repositories, as shown in the following examples.

This example shows an Amazon ECR public repository policy, which allows for a specific
IAM user to describe the repository and the images within the repository.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "ECR Public Repository Policy",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:user/`username`"
 },
 "Action": [
 "ecr-public:DescribeImages",
 "ecr-public:DescribeRepositories"
 ],
 "Resource": "*"
 }]
}`

```

This example shows an IAM policy that achieves the same goal as the preceding
example. In this example, the policy is scoped to a public repository (specified by the
full Amazon Resource Name (ARN) of the public repository) using the resource parameter.
For more information about ARN format, see [Resources](security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-resources "security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-resources").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid": "ECR Public Repository Policy",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:user/`username`"
 },
 "Action": [
 "ecr-public:DescribeImages",
 "ecr-public:DescribeRepositories"
 ],
 "Resource": [
 "arn:aws:ecr-public::`111122223333`:repository/`repository-name`"
 ]
 }]
}`

```

###### Topics

- [Setting a repository policy statement in Amazon ECR Public](set-public-repository-policy.md "set-public-repository-policy.md")
- [Deleting a public repository policy statement in Amazon ECR Public](delete-public-repository-policy.md "delete-public-repository-policy.md")
- [Public repository policy examples in Amazon ECR Public](public-repository-policy-examples.md "public-repository-policy-examples.md")
