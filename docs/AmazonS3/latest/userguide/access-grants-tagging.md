# Managing tags for S3 Access Grants

Tags in Amazon S3 Access Grants have similar characteristics to [object tags](object-tagging.md "object-tagging.md") in Amazon S3. Each
tag is a key-value pair. The resources in S3 Access Grants that you can tag are S3 Access Grants [instances](access-grants-instance.md "access-grants-instance.md"), [locations](access-grants-location.md "access-grants-location.md"), and
[grants](access-grants-grant.md "access-grants-grant.md").

###### Note

Tagging in S3 Access Grants uses different API operations than object tagging. S3 Access Grants uses the [TagResource](../API/API_control_TagResource.md "../API/API_control_TagResource.md"), [UntagResource](../API/API_control_UntagResource.md "../API/API_control_UntagResource.md"), and [ListTagsForResource](../API/API_control_ListTagsForResource.md "../API/API_control_ListTagsForResource.md") API operations, where a resource can
be either an S3 Access Grants instance, a registered location, or an access grant.

Similar to [object tags](object-tagging.md "object-tagging.md"), the following limitations apply:

- You can add tags to new S3 Access Grants resources when you create them, or you can add tags to existing resources.
- You can associate up to 10 tags with a resource. If multiple tags are associated with the same resource, they must have unique tag keys.
- A tag key can be up to 128 Unicode characters in length, and tag values can be up to 256
  Unicode characters in length. Tags are internally represented in UTF-16. In UTF-16,
  characters consume either 1 or 2 character positions.
- The keys and values are case sensitive.
  For more information about tag restrictions, see [User-defined tag
  restrictions](../../../awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.md "../../../awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.md") in the _AWS Billing User Guide_.

You can tag resources in S3 Access Grants by using the AWS Command Line Interface (AWS CLI), the Amazon S3 REST API, or the
AWS SDKs.

To install the AWS CLI, see [Installing the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the _AWS Command Line Interface User Guide_.

You can tag an S3 Access Grants resource when you create it or after you have created it. The following examples show how you tag or untag an S3 Access Grants instance. You can perform similar operations for registered locations and access grants.

To use the following example commands, replace the `user input placeholders` with your own information.

###### Example– Create an S3 Access Grants instance with tags

```
aws s3control create-access-grants-instance \
 --account-id `111122223333` \
 --profile `access-grants-profile` \
 --region `us-east-2` \
 --tags Key=`tagKey1`,Value=`tagValue1`
```

Response:

```
 {
    "CreatedAt": "`2023-10-25T01:09:46.719000+00:00`",
    "AccessGrantsInstanceId": "default",
    "AccessGrantsInstanceArn": "arn:aws:s3:`us-east-2`:`111122223333`:access-grants/default"
}
```

###### Example– Tag an already created S3 Access Grants instance

```
aws s3control tag-resource \
--account-id `111122223333` \
--resource-arn "arn:aws:s3:`us-east-2`:`111122223333`:access-grants/default" \
--profile `access-grants-profile` \
--region `us-east-2` \
--tags Key=`tagKey2`,Value=`tagValue2`
```

###### Example– List tags for the S3 Access Grants instance

```
aws s3control list-tags-for-resource \
--account-id `111122223333` \
--resource-arn "arn:aws:s3:`us-east-2`:`111122223333`:access-grants/default" \
--profile `access-grants-profile` \
--region `us-east-2`
```

Response:

```
{
    "Tags": [
        {
            "Key": "`tagKey1`",
            "Value": "`tagValue1`"
        },
        {
            "Key": "`tagKey2`",
            "Value": "`tagValue2`"
        }
    ]
}
```

###### Example– Untag the S3 Access Grants instance

```
aws s3control untag-resource \
 --account-id `111122223333` \
 --resource-arn "arn:aws:s3:`us-east-2`:`111122223333`:access-grants/default" \
 --profile `access-grants-profile` \
 --region `us-east-2` \
 --tag-keys "`tagKey2`"
```

You can use the Amazon S3 API to tag, untag, or list tags for an S3 Access Grants instance, registered
location, or access grant. For information about the REST API support for managing
S3 Access Grants tags, see the following sections in the
_Amazon Simple Storage Service API Reference_:

- [TagResource](../API/API_control_TagResource.md "../API/API_control_TagResource.md")
- [UntagResource](../API/API_control_UntagResource.md "../API/API_control_UntagResource.md")
- [ListTagsForResource](../API/API_control_ListTagsForResource.md "../API/API_control_ListTagsForResource.md")
