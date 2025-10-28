# Creating access points for directory buckets with tags

You can tag Amazon S3 Access Points for directory buckets when you create them. For additional information, see [Using tags with S3 Access Points for directory buckets](access-points-db-tagging.md "access-points-db-tagging.md").

## Permissions

To create an access point for directory buckets with tags, you must have the following permissions:

- `s3express:CreateAccessPoint`
- `s3express:TagResource`

## Troubleshooting errors

If you encounter an error when attempting to create an access point for directory buckets with tags, you can do the following:

- Verify that you have the required [Permissions](#access-points-db-create-tag-permissions "#access-points-db-create-tag-permissions") to create the access point for directory buckets and add a tag to it.
- Check your IAM user policy for any attribute-based access control (ABAC) conditions. You may be required to label your access points for directory buckets only with specific tag keys and values. For more information, see [Using tags for attribute-based access control (ABAC)](tagging.md#using-tags-for-abac "tagging.md#using-tags-for-abac").

## Steps

You can create an access point for directory buckets with tags applied by using the Amazon S3 console, the AWS Command Line Interface (AWS CLI), the Amazon S3 REST API, and AWS SDKs.

To create an access point for directory buckets with tags using the Amazon S3 console:

1. Sign in to Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Access Points (Directory Buckets)**.
3. Choose **create access point** to create a new access point.
4. Enter a name for the access point. For more information, see [Access points for directory buckets naming rules, restrictions, and
   limitations](access-points-directory-buckets-restrictions-limitations-naming-rules.md "access-points-directory-buckets-restrictions-limitations-naming-rules.md").
5. On the **Create access point** page, **Tags** is an option when creating a new access point.
6. Choose **Add new Tag** to open the Tags editor and enter a tag key-value pair. The tag key is required, but the value is optional.
7. To add another tag, select **Add new Tag** again. You can enter up to 50 tag key-value pairs.
8. After you complete specifying the options for your new access point, choose **Create access point**.

SDK for Java 2.x
This example shows you how to create an access point with tags by using the AWS SDK for Java 2.x. To use the command replace the `user input placeholders` with your own information.

```
CreateAccessPointRequest createAccessPointRequest = CreateAccessPointRequest.builder()
                .accountId(`111122223333`)
                .name(``my-access-point``)
                .bucket(``amzn-s3-demo-bucket`--`zone-id`--x-s3`)
                .tags(Collections.singletonList(Tag.builder().key("`key1`").value("`value1`").build()))
                .build();
 awss3Control.createAccessPoint(createAccessPointRequest);

```

For information about the Amazon S3 REST API support for creating a directory bucket with tags, see the following section in the _Amazon Simple Storage Service API Reference_:

- [CreateBucket](../API/API_CreateBucket.md "../API/API_CreateBucket.md")
  To install the AWS CLI, see [Installing the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the _AWS Command Line Interface User Guide_.

The following CLI example shows you how to create an access point for directory buckets with tags by using the AWS CLI. To use the command replace the `user input placeholders` with your own information.

When you create an access point for directory buckets you must provide configuration details and use the following naming convention:
`my-access-point`

**Request:**

```
aws s3control create-access-point \
--account-id `111122223333` \
--name ``my-access-point`` \
--bucket ``amzn-s3-demo-bucket`--`zone-id`--x-s3` \
--profile personal \
--tags Key=`key1`,Value=`value1` Key=`MyKey2`,Value=`value2` \
--region `region`

```
