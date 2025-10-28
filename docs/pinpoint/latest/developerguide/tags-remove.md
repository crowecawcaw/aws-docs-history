**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Remove tags from Amazon Pinpoint resources programmatically

The following examples show how to remove a tag (both the key and value) from an
Amazon Pinpoint resource by using the [AWS CLI](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md") and the [Amazon Pinpoint REST API](../apireference.md "../apireference.md"). You can also use any supported AWS SDK
to remove a tag from a resource.

To remove a tag from multiple Amazon Pinpoint resources in a single operation, use the resource
groups tagging operations of the AWS CLI or the [AWS Resource Groups Tagging
API](../../../resourcegroupstagging/latest/APIReference/Welcome.md "../../../resourcegroupstagging/latest/APIReference/Welcome.md"). To remove only a specific tag value (not a tag key) from a resource,
[update the tag for the resource](tags-update.md "tags-update.md").

## Remove tags by using the API

To remove a tag from a resource by using the Amazon Pinpoint REST API, send a DELETE request
to the [Tags](../apireference/rest-api-tags.md "../apireference/rest-api-tags.md") URI. In the URI,
include the Amazon Resource Name (ARN) of the resource that you want to remove a tag
from, followed by the `tagKeys` parameter and the tag to remove. For
example:

```
https://`endpoint`/v1/tags/`resource-arn`?tagKeys=`key`
```

Where:

- `endpoint` is the Amazon Pinpoint endpoint for the AWS
  Region that hosts the resource.
- `resource-arn` is the ARN of the resource that
  you want to remove a tag from.
- `key` is the tag that you want to remove from the
  resource.

All the parameters should be URL encoded.

To remove multiple tag keys and their associated values from a resource, append
the `tagKeys` parameter and argument for each additional tag to remove,
separated by an ampersand (&). For example:

```
https://`endpoint`/v1/tags/`resource-arn`?tagKeys=`key1`&tagKeys=`key2`
```

All the parameters should be URL encoded.

## Remove tags by using the AWS CLI

To remove a tag from a resource by using the AWS CLI, run the
`untag-resource` command. Include the `tag-keys` parameter
and argument, as shown in the following example.

Linux, macOS, or Unix

```
`$` aws pinpoint untag-resource \
  --resource-arn `resource-arn` \
  --tag-keys `key1` `key2`
```

Windows Command Prompt

```
`C:\>` aws pinpoint untag-resource ^
     --resource-arn `resource-arn` ^
     --tag-keys `key1` `key2`
```

In the preceding example, make the following changes:

- Replace `resource-arn` with the ARN of the resource
  that you want to remove tags from.
- Replace `key1` and `key2`
  with the keys of the tags that you want to remove from the resource.
