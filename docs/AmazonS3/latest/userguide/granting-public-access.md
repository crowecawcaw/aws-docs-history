

# Granting public access to your Amazon S3 data
<a name="granting-public-access"></a>

Amazon S3 provides multiple ways to grant public access to your data. You can grant public access through a bucket policy, through object tags combined with a bucket policy, or through object access control lists (ACLs). The mechanism you use depends on your goal. For example, to make an entire bucket publicly accessible, you can use a bucket policy. To make only specific objects accessible, you can add a tag to those objects and make them public with a bucket policy.

By default, Amazon S3 blocks public access. New buckets have Block Public Access turned on and have Object Ownership set to Bucket owner enforced, which disables ACLs. Before any object in a bucket can be publicly accessible, you must turn off the Block Public Access settings for the bucket and the account. For more information, see [Blocking public access to your Amazon S3 storage](access-control-block-public-access.md).

If you want to grant temporary access to a single object, you can use a presigned URL. A presigned URL gives limited time access to a single object, and you can control how long the URL remains valid by setting its expiration time. For more information, see [Sharing objects with presigned URLs](ShareObjectPreSignedURL.md).

**Important**  
When you turn off Block Public Access and grant public access, anyone on the internet can access your objects. Grant public access only when a specific use case requires it.

**Topics**
+ [Granting public access to an entire bucket](#granting-public-access-bucket)
+ [Granting public access to specific objects with object tags](#granting-public-access-tags)
+ [Granting public access to an individual object with an ACL](#granting-public-access-acl)

## Granting public access to an entire bucket
<a name="granting-public-access-bucket"></a>

You can grant public access to an entire bucket with a bucket policy. This is useful when all the objects that you want to make public can be stored together, such as the files for a static website. Store those objects in a bucket that holds only public content, and keep private data in a separate bucket. We recommend this approach because it keeps a clear boundary between public and private data.

To make the objects in a bucket publicly readable, turn off Block Public Access for the bucket and add a bucket policy that grants everyone the `s3:GetObject` permission.

**Example**  
The following bucket policy grants public read access to every object in the bucket.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/*"
        }
    ]
}
```

## Granting public access to specific objects with object tags
<a name="granting-public-access-tags"></a>

You can grant public access to specific objects in a bucket by applying an object tag to them and adding a bucket policy that grants read access to any object with that tag. We recommend this approach when you must keep both private and public objects in the same bucket.

With object tags, a single condition in the bucket policy matches every object that has the tag, so one statement can make a large number of objects public. This approach avoids listing individual object keys in the policy, which can contain characters that a policy does not accept and can exceed the bucket policy size limit.

To grant public access to specific objects, turn off Block Public Access for the bucket, apply an object tag such as `public=true` to each object that you want to make public, and add a bucket policy that grants `s3:GetObject` to objects with that tag. For more information about tagging objects, see [Tagging your objects](object-tagging.md).

**Note**  
Object tags incur additional charges, both to apply them and to store them. For more information, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/).

**Example**  
The following bucket policy grants public read access to every object that has the `public=true` tag.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadTaggedObjects",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::amzn-s3-demo-bucket/*",
            "Condition": {
                "StringEquals": {
                    "s3:ExistingObjectTag/public": "true"
                }
            }
        }
    ]
}
```

## Granting public access to an individual object with an ACL
<a name="granting-public-access-acl"></a>

Object ACLs are a legacy way to grant access, and new buckets disable them by default. We recommend that you keep ACLs disabled, and use Amazon S3 resource-based policies (bucket policies and access point policies) or IAM policies instead, unless you must control access for each object individually. Policies provide simpler and more flexible access control. For more information, see [Controlling ownership of objects and disabling ACLs for your bucket](about-object-ownership.md).

**Important**  
Enabling ACLs applies to the entire bucket, not only the object that you make public. After ACLs are enabled, another account that uploads an object can own it, so you might not control every object in your bucket.

To make an object public with an ACL, turn off Block Public Access for the bucket and enable ACLs by changing the Object Ownership setting from Bucket owner enforced to Bucket owner preferred. Then apply the `public-read` ACL to the object, which grants read access to everyone, so anyone can read the object. For more information, see [Managing access with ACLs](acls.md).