

# Enforce conditional deletes on Amazon S3 buckets
<a name="conditional-delete-enforce"></a>

 By using Amazon S3 bucket policies, you can enforce `If-Match`header with conditional deletes for objects in general purpose buckets. If the `If-Match` header doesn’t exist, the request will be denied with an `403 Access Denied`. A bucket policy is a resource-based policy that you can use to grant access permissions to your bucket and the objects in it. Only the bucket owner can associate a policy with a bucket. For more information about bucket policies, see [Bucket policies for Amazon S3](bucket-policies.md). 

The following examples show how to use conditions in a bucket policy to force clients to use the `If-Match` HTTP header.

**Topics**
+ [Example 1: Only allow conditional deletes using the `If-Match` header with the `ETag` value](#conditional-writes-enforce-ex1)
+ [Example 2: Only allow conditional deletes using the `If-Match` header with the `*` value](#conditional-deletes-enforce-ex2)

## Example 1: Only allow conditional deletes using the `If-Match` header with the `ETag` value
<a name="conditional-writes-enforce-ex1"></a>

You can use this bucket policy to only allow conditional deletes using `DeleteObject` and `DeleteObjects` requests that include the `If-Match` header with the `ETag` value. The `Null` condition ensures the `If-Match` header is present, and the `s3:GetObject` permission is granted because conditional deletes with a specific ETag value require both `s3:DeleteObject` and `s3:GetObject` permissions. All non-conditional deletes would be denied and conditional deletes would pass.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowConditionalDeletes",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::{{111122223333}}:user/Alice"
            },
            "Action": "s3:DeleteObject",
            "Resource": "arn:aws:s3:::{{amzn-s3-demo-bucket}}/*",
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
                "AWS": "arn:aws:iam::{{111122223333}}:user/Alice"
            },
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::{{amzn-s3-demo-bucket}}/*"
        }
    ]
}
```

## Example 2: Only allow conditional deletes using the `If-Match` header with the `*` value
<a name="conditional-deletes-enforce-ex2"></a>

You can use this bucket policy to only allow conditional deletes using `DeleteObject` and `DeleteObjects` requests that include the `If-Match` header with the `*` value. The `Null` condition ensures the `If-Match` header is present. Because `s3:GetObject` is not granted, conditional deletes with a specific ETag value will fail – only `If-Match: *` (which checks object existence and requires only `s3:DeleteObject` permission) will succeed. All non-conditional deletes would be denied, and only `If-Match: *` conditional deletes would succeed.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowConditionalDeletes",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::{{111122223333}}:user/Alice"
            },
            "Action": "s3:DeleteObject",
            "Resource": "arn:aws:s3:::{{amzn-s3-demo-bucket}}/*",
            "Condition": {
                "Null": {
                    "s3:if-match": "false"
                }
            }
        }
    ]
}
```