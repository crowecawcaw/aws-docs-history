End of support notice: On November 13, 2025, AWS will discontinue support
for AWS Elemental MediaStore. After November 13, 2025, you will no longer be able to access the MediaStore console
or MediaStore resources. For more information, visit this
[blog post](https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/ "https://aws.amazon.com/blogs/media/support-for-aws-elemental-mediastore-ending-soon/").

# Editing a container policy

You can edit the permissions in the default container policy, or you can create a new
policy that replaces the default policy. It takes up to five minutes for the new policy
to take effect.

###### To edit a container policy (console)

1. Open the MediaStore console at [https://console.aws.amazon.com/mediastore/](https://console.aws.amazon.com/mediastore/ "https://console.aws.amazon.com/mediastore/").
2. On the **Containers** page, choose the container
   name.
3. Choose **Edit policy**. For examples that show
   how to set different permissions, see [Example container policies](policies-examples.md "policies-examples.md").
4. Make the appropriate changes, and then choose **Save**.

###### To edit a container policy (AWS CLI)

1. Create a file that defines the container policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "PublicReadOverHttps",
 "Effect": "Allow",
 "Action": ["mediastore:GetObject", "mediastore:DescribeObject"],
 "Principal": "*",
 "Resource": "arn:aws:mediastore:`us-west-2`:`111122223333`:container/`ExampleLiveDemo`/*",
 "Condition": {
 "Bool": {
 "aws:SecureTransport": "true"
 }
 }
 }
 ]
}`

```

2. In the AWS CLI, use the `put-container-policy` command:

```
aws mediastore put-container-policy --container-name `ExampleLiveDemo` --policy `file://ExampleContainerPolicy.json` --region `us-west-2`
```

This command has no return value.
