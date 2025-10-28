# Required IAM permissions for Amazon ECR

public registries

When editing your Amazon ECR public registry settings, the IAM principal must have
permission to call the `ecr-public:PutRegistryPolicy` API for registry-level
operations.

###### Note

Setting a **Display name** for your Amazon ECR public registry doesn't
require any additional permissions.

The following IAM policy can be added as an inline policy to the principal
performing the public registry edit. Replace the example AWS account ID in this
example with your own account ID.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "ecr-public:PutRegistryCatalogData",
 "Resource": "arn:aws:ecr-public::`123456789012`:registry/*"
 }
 ]
}`

```
