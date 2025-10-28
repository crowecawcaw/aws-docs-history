# S3 Vectors resource-based policy examples

###### Note

Amazon S3 Vectors is in preview release for Amazon Simple Storage Service and is subject to change.

Resource-based policies are attached to a resource. You can create resource-based policies
for vector buckets. Resource-based policies for S3 Vectors use the standard AWS policy
format in JSON that you attach directly to vector buckets to control access to the bucket
and its contents.

Unlike identity-based policies that are attached to users, groups, or roles,
resource-based policies are attached to the resource itself (the vector bucket) and can
grant permissions to principals from other AWS accounts. This makes them ideal for
scenarios where you need to share vector data across organizational boundaries or
implement fine-grained access controls based on the specific resource being accessed.

Resource-based policies are evaluated in combination with identity-based policies, and the
effective permissions are determined by the union of all applicable policies. This means
that a principal needs permission from both the identity-based policy (attached to their
user/role) and the resource-based policy (attached to the bucket) to perform an action,
unless the resource-based policy explicitly grants the permission.

## Example 1: Cross-account

access policy

This policy demonstrates how to grant specific permissions to users from different
AWS accounts:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CrossAccountBucketAccess",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam:`123456789012`:role/Admin"
            },
            "Action": [
                "s3vectors:CreateIndex",
                "s3vectors:ListIndexes",
                "s3vectors:QueryVectors",
                "s3vectors:PutVectors",
                "s3vectors:DeleteIndex"
            ],
            "Resource": [
                "arn:aws:s3vectors:``aws-region``:`111122223333`:bucket/`amzn-s3-demo-vector-bucket`/*",
                "arn:aws:s3vectors:``aws-region``:`111122223333`:bucket/`amzn-s3-demo-vector-bucket`"
            ]
        }
    ]
}
```

## Example 2: Deny

vector index level actions

This policy demonstrates how to deny specific vector index level actions to an IAM
role:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DenyIndexLevelActions",
            "Effect": "Deny",
            "Principal": {
                "AWS": "arn:aws:iam:`123456789012`:role/`External-Role-Name`"
            },
            "Action": [
                "s3vectors:QueryVectors",
                "s3vectors:PutVectors",
                "s3vectors:DeleteIndex",
                "s3vectors:GetVectors",
                "s3vectors:GetIndex",
                "s3vectors:DeleteVectors",
                "s3vectors:CreateIndex",
                "s3vectors:ListVectors"
            ],
            "Resource": "arn:aws:s3vectors:``aws-region``:`111122223333`:bucket/`amzn-s3-demo-vector-bucket`/*"
        }
    ]
}
```

## Example 3: Deny

modification operations at both vector index and bucket levels

This policy demonstrates how to deny modification requests for both vector index and
bucket-level actions by specifying multiple resources:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DenyModificationActionsAtBucketandIndexLevels",
            "Effect": "Deny",
            "Principal": {
                "AWS": "arn:aws:iam:`123456789012`:role/`External-Role-Name`"
            },
            "Action": [
                "s3vectors:CreateVectorBucket",
                "s3vectors:DeleteVectorBucket",
                "s3vectors:PutVectorBucketPolicy",
                "s3vectors:DeleteVectorBucketPolicy",
                "s3vectors:CreateIndex",
                "s3vectors:DeleteIndex",
                "s3vectors:PutVectors",
                "s3vectors:DeleteVectors"
            ],
            "Resource": [
                "arn:aws:s3vectors:``aws-region``:`111122223333`:bucket/`amzn-s3-demo-vector-bucket`/*",
                "arn:aws:s3vectors:``aws-region``:`111122223333`:bucket/`amzn-s3-demo-vector-bucket`"
            ]
        }
    ]
}
```
