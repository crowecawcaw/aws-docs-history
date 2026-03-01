# Creating access points with tags

You can tag access points when you create them. There is no additional charge for using tags on access points beyond the standard S3 API request rates. For more information, see [Amazon S3 pricing](../../../s3/pricing.md "../../../s3/pricing.md"). For more information about tagging access points, see [Using tags with S3 Access Points for general purpose buckets](access-points-tagging.md "access-points-tagging.md").

## Permissions

To create an access point with tags, you must have the following permissions:

- `s3:CreateBucket`
- `s3:TagResource`

## Troubleshooting errors

If you encounter an error when attempting to create an access point with tags, you can do the following:

- Verify that you have the required [Permissions](#access-points-create-tag-permissions "#access-points-create-tag-permissions") to create the access point and add a tag to it.
- Check your IAM user policy for any attribute-based access control (ABAC) conditions. You may be required to label your access points only with specific tag keys and values. For more information, see [Using tags for attribute-based access control (ABAC)](tagging.md#using-tags-for-abac "tagging.md#using-tags-for-abac").

## Steps

You can create an access point with tags applied by using the Amazon S3 console, the AWS Command Line Interface (AWS CLI), the Amazon S3 REST API, and AWS SDKs.

To create an access point with tags using the Amazon S3 console:

1. Sign in to Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Access Points (General Purpose Buckets)**.
3. Choose **create access point** to create a new access point.
4. On the **Create access point** page, **Tags** is an option when creating a new access point.
5. Enter a name for the access point. For more information, see [Access points naming rules, restrictions, and limitations](access-points-restrictions-limitations-naming-rules.md "access-points-restrictions-limitations-naming-rules.md").
6. Choose **Add new Tag** to open the **Tags** editor and enter a tag key-value pair. The tag key is required, but the value is optional.
7. To add another tag, select **Add new Tag** again. You can enter up to 50 tag key-value pairs.
8. After you complete specifying the options for your new access point, choose **Create access point**.

SDK for Java 2.x
This example shows you how to create an access point with tags by using the AWS SDK for Java 2.x. To use the command replace the `user input placeholders` with your own information.

```
CreateAccessPointRequest createAccessPointRequest = CreateAccessPointRequest.builder()
                .accountId(`111122223333`)
                .name(``my-access-point``)
                .bucket(``amzn-s3-demo-bucket``)
                .tags(Collections.singletonList(Tag.builder().key("`key1`").value("`value1`").build()))
                .build();
 awss3Control.createAccessPoint(createAccessPointRequest);

```

For information about the Amazon S3 REST API support for creating an access point with tags, see the following section in the _Amazon Simple Storage Service API Reference_:

- [CreateAccessPoint](../API/API_control_CreateAccessPoint.md "../API/API_control_CreateAccessPoint.md")
  To install the AWS CLI, see [Installing the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the _AWS Command Line Interface User Guide_.

The following CLI example shows you how to create an access point with tags by using the AWS CLI. To use the command replace the `user input placeholders` with your own information.

**Request:**

```
aws s3control create-access-point --name ``my-access-point`` \
--bucket ``amzn-s3-demo-bucket`` \
--account-id `111122223333` \ --profile personal \
--tags [{Key=`key1`,Value=`value1`},{Key=`key2`,Value=`value2`}] \
--region `region`

```
