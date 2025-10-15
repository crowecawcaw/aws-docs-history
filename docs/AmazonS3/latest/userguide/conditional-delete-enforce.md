# Enforce conditional deletes on Amazon S3 buckets


 By using Amazon S3 bucket policies, you can enforce `If-Match`header 
 with conditional deletes for objects in general purpose buckets. 
 If the `If-Match` header doesn’t exist, 
 the request will be denied with an `403 Access Denied`.
 A bucket policy is a resource-based policy that you can use to grant access permissions 
 to your bucket and the objects in it. Only the bucket owner can associate a policy with a bucket. 
 For more information about bucket policies, see [Bucket policies for Amazon S3](bucket-policies.md "bucket-policies.md").
 

The following examples show how to use conditions in a bucket policy to force clients
 to use the `If-Match` HTTP header.

###### Topics

* [Example 1: Only allow conditional deletes using the If-Match header with the ETag value](#conditional-writes-enforce-ex1 "#conditional-writes-enforce-ex1")
* [Example 2: Only allow conditional deletes using the If-Match header with the \* value](#conditional-deletes-enforce-ex2 "#conditional-deletes-enforce-ex2")

## Example 1: Only allow conditional deletes using the `If-Match` header with the `ETag` value


You can use this bucket policy to only allow conditional deletes using
 `DeleteObject` and `DeleteObjects` requests that include
 the `If-Match` header with the `ETag` value. All
 non-conditional deletes would be denied and conditional deletes would pass. 



```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowConditionalDeletes",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::`111122223333`:user/Alice"
            },
            "Action": "s3:DeleteObject",
            "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`/*",
            "Condition": {
                "Null": {
                    "s3:if-match": "false"
                }
            }
        },
         {
            "Sid": "AllowGetObjectBecauseConditionalDeleteIfMatchETag",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::`111122223333`:user/Alice"
            },
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`/*"
        }
    ]
}
```

## Example 2: Only allow conditional deletes using the `If-Match` header with the `*` value


You can use this bucket policy to only allow conditional deletes using
 `DeleteObject` and `DeleteObjects` requests that
 include the `If-Match` header with `*` value. All
 non-conditional deletes would be denied and conditional deletes would pass. 



```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowConditionalDeletes",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::`111122223333`:user/Alice"
            },
            "Action": "s3:DeleteObject",
            "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`/*",
            "Condition": {
                "Null": {
                    "s3:if-match": "false"
                }
            }
        }
    ]
}
```
