# Managing vector bucket policies

Vector bucket policies are resource-based policies that you attach directly to vector buckets to control access to the bucket and its contents. You can add, view, edit, delete
vector bucket policies by using the Amazon S3 REST API, AWS SDKs, S3 Console, or the AWS Command Line Interface (AWS CLI). Bucket policies for vector buckets can grant permissions to
principals from other AWS accounts, making them useful for cross-account access
scenarios.

## Policy management operations

- [PutVectorBucketPolicy](../API/API_S3VectorBuckets_PutVectorBucketPolicy.md "../API/API_S3VectorBuckets_PutVectorBucketPolicy.md") – Add or update a bucket policy.
- [GetVectorBucketPolicy](../API/API_S3VectorBuckets_GetVectorBucketPolicy.md "../API/API_S3VectorBuckets_GetVectorBucketPolicy.md") – Retrieve the current bucket policy.
- [DeleteVectorBucketPolicy](../API/API_S3VectorBuckets_DeleteVectorBucketPolicy.md "../API/API_S3VectorBuckets_DeleteVectorBucketPolicy.md") – Remove the bucket policy.

## Adding a vector bucket policy

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Amazon S3**.
3. Choose **Vector buckets** and select the vector bucket name that you want to add a policy to.
4. Choose the **Permissions** tab.
5. Under **Vector bucket policy**, choose **Edit**.
6. In the policy editor, enter your policy JSON.
7. (Optional) Choose **Policy examples** to see sample policies that you can adapt to your needs.
8. After entering your policy, choose **Save changes**.

To add or update a bucket policy, use the following example command and
replace the `user input placeholders` with your own
information.

```
aws s3vectors put-vector-bucket-policy \
  --vector-bucket-name "`amzn-s3-demo-vector-bucket`" \
  --policy '{"Version": "2012-10-17",		 	 	 "Statement":[{"Effect":"Allow","Principal":{"AWS":"arn:aws:iam::`111122223333`:root"},"Action":"s3vectors:*","Resource":"arn:aws:s3vectors:``aws-region``:`111122223333`:bucket/`amzn-s3-demo-vector-bucket`"}]}'
```

## Viewing a vector bucket policy

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Amazon S3**.
3. Choose **Vector buckets** and select the vector bucket name that you want to view the policy for.
4. Choose the **Permissions** tab.

To retrieve a bucket policy, use the following example command and replace the
`user input placeholders` with your own
information.

```
aws s3vectors get-vector-bucket-policy \
  --vector-bucket-name "`amzn-s3-demo-vector-bucket`"
```

## Deleting a vector bucket policy

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Amazon S3**.
3. Choose **Vector buckets** and select the vector bucket name that you want to delete the policy for.
4. Choose the **Permissions** tab.
5. Under the **Vector bucket policy**, choose **Delete**.

To delete a bucket policy, use the following example command and replace the
`user input placeholders` with your own information.

```
aws s3vectors delete-vector-bucket-policy \
  --vector-bucket-name "`amzn-s3-demo-vector-bucket`"
```

For detailed information about creating and managing bucket policies, including policy
examples and best practices, see [S3 Vectors resource-based policy examples](s3-vectors-resource-based-policies.md "s3-vectors-resource-based-policies.md").
