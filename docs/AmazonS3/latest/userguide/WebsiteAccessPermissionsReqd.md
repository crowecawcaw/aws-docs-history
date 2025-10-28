# Setting permissions for website

access

When you configure a bucket as a static website, if you want your website to be
public, you can grant public read access. To make your bucket publicly readable, you
must disable block public access settings for the bucket and write a bucket policy that
grants public read access. If your bucket contains objects that are not owned by the
bucket owner, you might also need to add an object access control list (ACL) that grants
everyone read access.

If you don't want to disable block public access settings for your bucket but you
still want your website to be public, you can create a Amazon CloudFront distribution to serve
your static website. For more information, see [Speeding up your website with
Amazon CloudFront](website-hosting-cloudfront-walkthrough.md "website-hosting-cloudfront-walkthrough.md") or [Use an
Amazon CloudFront distribution to serve a static website](../../../Route53/latest/DeveloperGuide/getting-started-cloudfront-overview.md "../../../Route53/latest/DeveloperGuide/getting-started-cloudfront-overview.md") in the
_Amazon Route 53 Developer Guide_.

###### Note

On the website endpoint, if a user requests an object that doesn't exist, Amazon S3
returns HTTP response code `404 (Not Found)`. If the object exists but
you haven't granted read permission on it, the website endpoint returns HTTP
response code `403 (Access Denied)`. The user can use the response code
to infer whether a specific object exists. If you don't want this behavior, you
should not enable website support for your bucket.

###### Topics

- [Step 1: Edit S3 Block Public
  Access settings](#block-public-access-static-site "#block-public-access-static-site")
- [Step 2: Add a bucket policy](#bucket-policy-static-site "#bucket-policy-static-site")
- [Object access control lists](#object-acl "#object-acl")

## Step 1: Edit S3 Block Public

Access settings

If you want to configure an existing bucket as a static website that has public
access, you must edit Block Public Access settings for that bucket. You might also
have to edit your account-level Block Public Access settings. Amazon S3 applies the most
restrictive combination of the bucket-level and account-level block public access
settings.

For example, if you allow public access for a bucket but block all public access
at the account level, Amazon S3 will continue to block public access to the bucket. In
this scenario, you would have to edit your bucket-level and account-level Block
Public Access settings. For more information, see [Blocking public access to your Amazon S3
storage](access-control-block-public-access.md "access-control-block-public-access.md").

By default, Amazon S3 blocks public access to your account and buckets. If you want to use a bucket to host a static website, you can use these steps to edit your block public access settings.

###### Warning

Before you complete these steps, review [Blocking public access to your Amazon S3
storage](access-control-block-public-access.md "access-control-block-public-access.md") to ensure that you understand and accept the risks involved with allowing public access. When you turn off block public access settings to make your bucket public, anyone on the internet can access your bucket. We recommend that you block all public access to your buckets.

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Choose the name of the bucket that you have configured as a static website.
3. Choose **Permissions**.
4. Under **Block public access (bucket settings)**, choose **Edit**.
5. Clear **Block _all_ public
   access**, and choose **Save changes**.

![The Amazon S3 console, showing the block public access bucket settings.](images/edit-public-access-clear.png)

Amazon S3 turns off the Block Public Access settings for your bucket. To create a public static website, you might also have to [edit the Block Public Access settings](../user-guide/block-public-access-account.md "../user-guide/block-public-access-account.md") for your account
before adding a bucket policy. If the Block Public Access settings for your account are currently turned on, you see a note under **Block public access (bucket settings)**.

## Step 2: Add a bucket policy

To make the objects in your bucket publicly readable, you must write a bucket
policy that grants everyone `s3:GetObject` permission.

After you edit S3 Block Public Access settings, you can add a bucket policy to grant public read access to your bucket. When you grant public read access, anyone on the internet can access your bucket.

###### Important

The following policy is an example only and allows full access to the contents of your bucket. Before you proceed with this step, review [How can I secure the files in my Amazon S3 bucket?](https://aws.amazon.com/premiumsupport/knowledge-center/secure-s3-resources/ "https://aws.amazon.com/premiumsupport/knowledge-center/secure-s3-resources/") to ensure that you understand the best practices for securing the files in your S3 bucket and risks involved in granting public access.

1. Under **Buckets**, choose the name of your bucket.
2. Choose **Permissions**.
3. Under **Bucket Policy**, choose **Edit**.
4. To grant public read access for your website, copy the following bucket policy, and paste it in the **Bucket policy editor**.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::`Bucket-Name`/*"
            ]
        }
    ]
}
```

5. Update the `Resource` to your bucket name.

In the preceding example bucket policy, `Bucket-Name` is a placeholder for the bucket name. To use this bucket policy with your own bucket, you must update this name to
match your bucket name. 6. Choose **Save changes**.

A message appears indicating that the bucket policy has been successfully added.

If you see an error that says `Policy has invalid resource`, confirm that the bucket
name in the bucket policy matches your bucket name. For information about adding a bucket
policy, see [How do I add an S3 bucket policy?](../user-guide/add-bucket-policy.md "../user-guide/add-bucket-policy.md")

If you get an error message and cannot save the bucket policy, check your account and bucket Block Public Access settings to confirm that you allow public access to the bucket.

## Object access control lists

You can use a bucket policy to grant public read permission to your objects.
However, the bucket policy applies only to objects that are owned by the bucket
owner. If your bucket contains objects that aren't owned by the bucket owner, the
bucket owner should use the object access control list (ACL) to grant public READ
permission on those objects.

S3 Object Ownership is an Amazon S3 bucket-level setting that you can use to both control ownership of the objects that are
uploaded to your bucket and to disable or enable ACLs. By default, Object Ownership is set to the Bucket owner enforced setting,
and all ACLs are disabled. When ACLs are disabled, the bucket owner owns all the objects in the bucket and manages access to them
exclusively by using access-management policies.

A majority of modern use cases in Amazon S3 no longer require the use of ACLs. We recommend that you keep ACLs disabled, except
in circumstances where you need to control access for each object individually. With ACLs disabled, you can use policies
to control access to all objects in your bucket, regardless of who uploaded the objects to your bucket.
For more information, see [Controlling ownership of objects and disabling ACLs
for your bucket](about-object-ownership.md "about-object-ownership.md").

###### Important

If your general purpose bucket uses the Bucket owner enforced setting for S3 Object Ownership, you must use policies to
grant access to your general purpose bucket and the objects in it. With the Bucket owner enforced setting enabled, requests to set
access control lists (ACLs) or update ACLs fail and return the `AccessControlListNotSupported` error code.
Requests to read ACLs are still supported.

To make an object publicly readable using an ACL, grant READ permission to the
`AllUsers` group, as shown in the following grant element. Add this
grant element to the object ACL. For information about managing ACLs, see [Access control list (ACL) overview](acl-overview.md "acl-overview.md").

```
<Grant>
  <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:type="Group">
    <URI>http://acs.amazonaws.com/groups/global/AllUsers</URI>
  </Grantee>
  <Permission>READ</Permission>
</Grant>
```
