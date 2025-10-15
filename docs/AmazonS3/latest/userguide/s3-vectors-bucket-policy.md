# Managing vector bucket policies

###### Note

Amazon S3 Vectors is in preview release for Amazon Simple Storage Service and is subject to change.

Vector bucket policies are resource-based policies that you attach directly to vector buckets to control access to the bucket and its contents. You can add, view, edit, delete
 vector bucket policies. Bucket policies for vector buckets can grant permissions to 
 principals from other AWS accounts, making them useful for cross-account access
 scenarios.


## Policy management operations



* [PutVectorBucketPolicy](../API/API_S3VectorBuckets_PutVectorBucketPolicy.md "../API/API_S3VectorBuckets_PutVectorBucketPolicy.md") – Add or update a bucket policy.
* [GetVectorBucketPolicy](../API/API_S3VectorBuckets_GetVectorBucketPolicy.md "../API/API_S3VectorBuckets_GetVectorBucketPolicy.md") – Retrieve the current bucket policy.
* [DeleteVectorBucketPolicy](../API/API_S3VectorBuckets_DeleteVectorBucketPolicy.md "../API/API_S3VectorBuckets_DeleteVectorBucketPolicy.md") – Remove the bucket policy.

## Adding a vector bucket policy


To add or update a bucket policy, use the following example command and
 replace the `user input placeholders` with your own
 information.


```
aws s3vectors put-vector-bucket-policy \
  --vector-bucket-name "`amzn-s3-demo-vector-bucket`" \
  --policy '{"Version": "2012-10-17",		 	 	 "Statement":[{"Effect":"Allow","Principal":{"AWS":"arn:aws:iam::`111122223333`:root"},"Action":"s3vectors:*","Resource":"arn:aws:s3vectors:``aws-region``:`111122223333`:bucket/`amzn-s3-demo-vector-bucket`"}]}'
```

## Viewing a vector bucket policy


To retrieve a bucket policy, use the following example command and replace the
 `user input placeholders` with your own
 information.


```
aws s3vectors get-vector-bucket-policy \
  --vector-bucket-name "`amzn-s3-demo-vector-bucket`"
```

## Deleting a vector bucket policy


To delete a bucket policy, use the following example command and replace the
 `user input placeholders` with your own information.


```
aws s3vectors delete-vector-bucket-policy \
  --vector-bucket-name "`amzn-s3-demo-vector-bucket`"
```

For detailed information about creating and managing bucket policies, including policy
 examples and best practices, see [S3 Vectors resource-based policy examples](s3-vectors-resource-based-policies.md "s3-vectors-resource-based-policies.md").
