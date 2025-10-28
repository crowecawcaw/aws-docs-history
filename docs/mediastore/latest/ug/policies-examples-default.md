End of support notice: On November 13, 2025, AWS will discontinue support
for AWS Elemental MediaStore. After November 13, 2025, you will no longer be able to access the MediaStore console
or MediaStore resources. For more information, visit this
[blog post](https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/ "https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/").

# Example container policy: Default

When you create a container, AWS Elemental MediaStore automatically attaches the
following resource-based policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "MediaStoreFullAccess",
 "Action": [
 "mediastore:*"
 ],
 "Principal": {
 "AWS": "arn:aws:iam::`333333333333`:root"
 },
 "Effect": "Allow",
 "Resource": "arn:aws:mediastore:`us-east-2`:`333333333333`:container/`<container name>`/*",
 "Condition": {
 "Bool": {
 "aws:SecureTransport": "true"
 }
 }
 }
 ]
}`

```

The policy is built into the service, so you don’t have to create it. However, you can [edit the policy](policies-edit.md "policies-edit.md") on
the container if the permissions in the default policy don't align with the permissions that you want to use for the container.

The default policy that is assigned to all new containers allows access to all
MediaStore operations on the container. It specifies that this access has the
condition of requiring HTTPS for the operations.
