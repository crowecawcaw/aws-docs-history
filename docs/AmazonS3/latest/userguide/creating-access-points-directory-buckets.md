# Creating access points for directory buckets

Like Directory buckets, access points can be created in Availability Zones or in Dedicated Local Zones. The access point must be created in the same zone as the directory bucket associated with it.

An access point is associated with exactly one Amazon S3 directory bucket. If you want to use a directory bucket in
your AWS account, you must first create a directory bucket. For more information about creating directory
buckets, see [Creating directory buckets in an Availability Zone](directory-bucket-create.md "directory-bucket-create.md") or [Creating a directory bucket in a Local Zone](create-directory-bucket-LZ.md "create-directory-bucket-LZ.md").

You can also create a cross-account access point that's associated with a bucket in another
AWS account, as long as you know the bucket name and the bucket owner's account ID.
However, creating cross-account access points doesn't grant you access to data in the bucket until you
are granted permissions from the bucket owner. The bucket owner must grant the access point
owner's account (your account) access to the bucket through the bucket policy. For more
information, see [Granting permissions for cross-account access points](access-points-policies.md#access-points-cross-account "access-points-policies.md#access-points-cross-account").

You can create an access point for any directory bucket with the AWS Management Console, AWS CLI, REST API, or AWS SDKs. Each access point is associated with a single directory bucket, and
you can create hundreds of access points per bucket. When creating an access point, you choose the name of the access point and the directory bucket to associate it with.
The access point name consists of a base name that you provide and suffix
that includes the Zone ID of your bucket location, followed by `--xa-s3`. For example,
``myaccesspoint`-`zoneID`--xa-s3`. you can also restrict access to the access point through a Virtual Private Cloud (VPC). Then, you can immediately begin reading and writing
data through your access point by using its name, just like you use a directory bucket name.

You can use the access point scope to restrict access to the directory bucket through the access point to
specific prefixes or API operations. If you don't add a scope to the access point, all prefixes in the directory bucket and all API operations can be performed on objects in
the bucket when accessed through the access point. After you create the access point, you can add, modify, or delete scope using the AWS CLI, AWS SDKs, or REST API. For more information, see [Manage the scope of your access points for directory buckets](access-points-directory-buckets-manage-scope.md "access-points-directory-buckets-manage-scope.md").

After you create the access point, you can configure your access point IAM resource policy. For more information, see [Viewing, editing or deleting access point policies](access-points-directory-buckets-policy.md "access-points-directory-buckets-policy.md").

###### Note

You can also create an access point for a directory bucket from the directory bucket screen. When you do this, the directory bucket name is
provided and you don't need to choose a bucket when creating the access point. For more information, see [Listing directory buckets](directory-buckets-objects-ListExamples.md "directory-buckets-objects-ListExamples.md").

###### To create an access point for directory buckets

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the navigation bar on the top of the page, choose the name of the currently
   displayed AWS Region. Next, choose the Region in which you want to create an
   access point. The access point must be created in the same Region as the associated
   bucket.
3. In the left navigation pane, choose **Access points for directory buckets**.
4. On the **Access Points** page, choose **Create
   access point**.
5. You can create an access point for a directory bucket in your account or in another account. To create an access point for a directory bucket in another account:

###### Note

If you're using a bucket in a different AWS account, the bucket owner must
update the bucket policy to authorize requests from the access point. For an example
bucket policy, see [Granting permissions for cross-account access points](access-points-directory-buckets-policies.md#access-points-directory-buckets-cross-account "access-points-directory-buckets-policies.md#access-points-directory-buckets-cross-account").

    1. In the **Directory bucket** field, choose **Specify a bucket in another account**.
    2. In the **Bucket owner account ID** field, enter the AWS account ID that owns the bucket.
    3. In the **Bucket name** field, enter the name of the bucket, including the base name and the zone ID. For example, ``bucket-base-name`--`zone-id`--x-s3`.

6. To create an access point for a directory bucket in your account:
   1. In the **Directory bucket** field, choose **Choose a bucket in this account**.
   2. In the **Bucket name** field, enter the name of the bucket, including the base name and the zone ID.
      For example, ``bucket-base-name`--`zone-id`--x-s3`. To choose the bucket from a list, choose **Browse S3** and choose the directory bucket.

7. In **Access point name**, in the **Base name** field, enter the base name
   for the access point. The zone ID and full access point name appear. For more information about naming access points, see [Naming rules for access points for directory buckets](access-points-directory-buckets-restrictions-limitations-naming-rules.md#access-points-directory-buckets-names "access-points-directory-buckets-restrictions-limitations-naming-rules.md#access-points-directory-buckets-names").
8. In **Network origin**, choose either **virtual private cloud (VPC)** or **Internet**.
   If you choose **virtual private cloud (VPC)**, in the **VPC ID** field, enter the ID of the VPC that you want to use with the access point.
9. (Optional) In **Access point scope**, to apply a scope to this access point, choose **Limit the scope of this access point using prefixes or permissions**.
   1. To limit access to prefixes in the directory bucket, in **Prefixes**, enter one or more prefixes. To add another prefix, choose **Add prefix**. To remove a prefix, choose **Remove**.

   ###### Note

   An access point scope has a character limit of 512 total characters for all prefixes. You can see the quantity of characters remaining below **Add prefix**. 2. In **Permissions**, choose one or more API operations that the access point will allow. To remove a data operation, choose the **X** next to the data operation name.

10. To not apply a scope to the access point and allow access to all prefixes in the directory bucket and all API operations through the access point, in **Access point scope**, choose **Apply access to the entire bucket**.
11. Choose **Create access point for directory bucket**. The access point name and other information about it appear in the **Access points for directory buckets** list.
    The following example command creates an access point named
    `example-ap` for the bucket
    ``amzn-s3-demo-bucket`--`zone-id`--x-s3` in the account`111122223333`.

```
aws s3control create-access-point --name `example-ap`--`zoneID`--xa-s3 --account-id `111122223333` --bucket ``amzn-s3-demo-bucket`--`zone-id`--x-s3`
```

To restrict access to the access point through a VPC, include the `--vpc` parameter and the VPC ID.

```
aws s3control create-access-point --name `example-ap`--`zoneID`--xa-s3 --account-id `111122223333` --bucket ``amzn-s3-demo-bucket`--`zone-id`--x-s3` --vpc `vpc-id`
```

When you create an access point for a cross-account bucket, include the `--bucket-account-id` parameter. The following example
command creates an access point in the AWS account
`111122223333`, for
the bucket
``amzn-s3-demo-bucket`--`zone-id`--x-s3`,
 owned by the AWS account `444455556666`.

```
aws s3control create-access-point --name `example-ap`--`zoneID`--xa-s3 --account-id `111122223333` --bucket ``amzn-s3-demo-bucket`--`zone-id`--x-s3` --bucket-account-id `444455556666`
```

For more information and examples, see [create-access-point](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/create-access-point.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3control/create-access-point.html") in the AWS CLI Command Reference.

The following example command creates an access point named
`example-ap` for the bucket
``amzn-s3-demo-bucket`--`zone-id`--x-s3` in the account`111122223333`and access restricted through the VPC`vpc-id` (optional).

```

PUT /v20180820/accesspoint/`example-ap`--`zoneID`--xa-s3 HTTP/1.1
Host: s3express-control.`region`.amazonaws.com
x-amz-account-id: `111122223333`
<?xml version="1.0" encoding="UTF-8"?>
<CreateAccessPointRequest>
   <Bucket>``amzn-s3-demo-bucket`--`zone-id`--x-s3`s</Bucket>
   <BucketAccountId>`111122223333`</BucketAccountId>
   <VpcConfiguration>
       <VpcId>`vpc-id`</VpcId>
   </VpcConfiguration>
</CreateAccessPointRequest>

```

Response:

```

HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<CreateAccessPointResult>
   <AccessPointArn>
       "arn:aws:s3express:region:111122223333:accesspoint/example-ap--zoneID--xa-s3"
   </AccessPointArn>
   <Alias>example-ap--zoneID--xa-s3</Alias>
</CreateAccessPointResult>

```

You can use the AWS SDKs to create an access point. For more information, see [list of supported SDKs](../API/API_control_CreateAccessPoint.md#API_control_CreateAccessPoint_SeeAlso "../API/API_control_CreateAccessPoint.md#API_control_CreateAccessPoint_SeeAlso") in the Amazon Simple Storage Service API Reference.
