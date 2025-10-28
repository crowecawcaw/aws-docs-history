**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Display tags for Amazon Pinpoint resources programmatically

The following examples show how to use the [AWS CLI](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md") and
the [Amazon Pinpoint REST API](../apireference.md "../apireference.md") to display a list of all the tags
(keys and values) that are associated with an Amazon Pinpoint resource. You can also use any
supported AWS SDK to display the tags associated with a resource.

## Display tags by using the API

To use the Amazon Pinpoint REST API to display all the tags that are associated with a
specific resource, send a GET request to the [Tags](../apireference/rest-api-tags.md "../apireference/rest-api-tags.md") URI and include the Amazon
Resource Name (ARN) of the resource in the URI. The ARN should be URL encoded. For
example, the following request retrieves all the tags that are associated with a
specified campaign (`resource-arn`):

```
GET /v1/tags/`resource-arn` HTTP/1.1
Host: pinpoint.us-east-1.amazonaws.com
Content-Type: application/json
Accept: application/json
Cache-Control: no-cache
```

The JSON response to the request includes a `tags` object. The
`tags` object lists all the tag keys and values that are associated
with the campaign.

To display all the tags that are associated with more than one resource of the
same type, send a GET request to the appropriate URI for that type of resource. For
example, the following request retrieves information about all the campaigns in the
specified project (`application-id`):

```
GET /v1/apps/`application-id`/campaigns HTTP/1.1
Host: pinpoint.us-east-1.amazonaws.com
Content-Type: application/json
Accept: application/json
Cache-Control: no-cache
```

The JSON response to the request lists all the campaigns in the project. The
`tags` object of each campaign lists all the tag keys and values that
are associated with the campaign.

## Display tags by using the AWS CLI

To use the AWS CLI to display a list of the tags that are associated with a
specific resource, run the `list-tags-for-resource` command and specify
the Amazon Resource Name (ARN) of the resource for the `resource-arn`
parameter, as shown in the following example.

Linux, macOS, or Unix

```
`$` aws pinpoint list-tags-for-resource \
  --resource-arn `resource-arn`
```

Windows Command Prompt

```
`C:\>` aws pinpoint list-tags-for-resource ^
     --resource-arn `resource-arn`
```

To display a list of all the Amazon Pinpoint resources that have tags, and all the tags that
are associated with each of those resources, use the [get-resources](../../../resourcegroupstagging/latest/APIReference/API_GetResources.md "../../../resourcegroupstagging/latest/APIReference/API_GetResources.md") command of the AWS Resource Groups Tagging API. Set the
`resource-type-filters` parameter to `mobiletargeting`, as
shown in the following example.

Linux, macOS, or Unix

```
`$` aws resourcegroupstaggingapi get-resources \
     --resource-type-filters "mobiletargeting"
```

Windows Command Prompt

```
`C:\>` aws resourcegroupstaggingapi get-resources ^
     --resource-type-filters "mobiletargeting"
```

The output of the command is a list of ARNs for all the Amazon Pinpoint resources that have
tags. The list includes all the tag keys and values that are associated with each
resource.
