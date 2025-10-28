# Setting up permissions for cross-account

ECR to ECR PTC

The Amazon ECR to Amazon ECR (ECR to ECR) pull through cache feature enables automatic
synchronization of images between Regions, AWS accounts, or both. With ECR to ECR PTC,
you can push images to your primary Amazon ECR registry and configure a pull through cache
rule to cache images in downstream Amazon ECR registries.

## IAM policies

required for cross-account ECR to ECR pull through cache

To cache images between Amazon ECR registries across different AWS accounts,
create an IAM role in the downstream account and configure the policies in this
section to provide the following permissions:

- Amazon ECR needs permissions to pull images from the upstream Amazon ECR registry on
  your behalf. You can grant these permissions by creating an IAM role and
  then specifying it in your pull through cache rule.
- The upstream registry owner must also grant the cache registry owner with
  the required permissions to pull the images in to the resource
  policies.

###### Policies

- [Creating an IAM role to
  define the pull through cache permissions](#ecr-policies-for-cross-account-ecr-to-ecr-pull-through-cache "#ecr-policies-for-cross-account-ecr-to-ecr-pull-through-cache")
- [Creating a Trust policy for the IAM role](#ecr-creating-a-trust-policy-for-the-iam-role "#ecr-creating-a-trust-policy-for-the-iam-role")
- [Creating a resource policy in the upstream Amazon ECR registry](#ecr-creating-registry-permissions-policy-in-upstream-registry "#ecr-creating-registry-permissions-policy-in-upstream-registry")

### Creating an IAM role to

define the pull through cache permissions

The following example shows a permissions policy that grants an IAM role
permission to pull images from the upstream Amazon ECR registry on your behalf. When
Amazon ECR assumes the role, it receives the permissions specified in this
policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "ecr:GetDownloadUrlForLayer",
 "ecr:GetAuthorizationToken",
 "ecr:BatchImportUpstreamImage",
 "ecr:BatchGetImage",
 "ecr:GetImageCopyStatus",
 "ecr:InitiateLayerUpload",
 "ecr:UploadLayerPart",
 "ecr:CompleteLayerUpload",
 "ecr:PutImage"
 ],
 "Resource": "*"
 }
 ]
}`

```

### Creating a Trust policy for the IAM role

The following example shows a trust policy that identifies Amazon ECR pull through
cache as the AWS service principal that can assume the role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "pullthroughcache.ecr.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

### Creating a resource policy in the upstream Amazon ECR registry

The upstream Amazon ECR registry owner must also add a registry policy
or a repository policy to grant the downstream registry owner the required
permissions to perform the following actions.

```
{
    "Effect": "Allow",
    "Principal": {
        "AWS": "arn:aws:iam::`444455556666`:root"
    },
    "Action": [
        "ecr:BatchGetImage",
        "ecr:GetDownloadUrlForLayer",
        "ecr:BatchImportUpstreamImage",
        "ecr:GetImageCopyStatus"
    ],
    "Resource": "arn:aws:ecr:`region:111122223333`:repository/*"
}
```
