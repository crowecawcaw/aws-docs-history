# Tagging your AWS IoT resources

To help you manage and organize your thing groups, thing types, topic rules, jobs, scheduled
audits and security profiles you can optionally assign your own metadata to each of these
resources in the form of tags. This section describes tags and shows you how to create
them.

To help you manage your costs related to things, you can create [billing groups](tagging-iot-billing-groups.md "tagging-iot-billing-groups.md") that contain things. You can then
assign tags that contain your metadata to each of these billing groups. This section also
discusses billing groups and the commands available to create and manage them.

## Tag basics

You can use tags to categorize your AWS IoT resources in different ways (for example, by
purpose, owner, or environment). This is useful when you have many resources of the same type
— you can quickly identify a resource based on the tags you've assigned to it. Each tag
consists of a key and optional value, both of which you define. For example, you can define a
set of tags for your thing types that helps you track devices by type. We recommend that you
create a set of tag keys that meets your needs for each kind of resource. Using a consistent
set of tag keys makes it easier for you to manage your resources.

You can search for and filter resources based on the tags you add or apply. You can also
use billing group tags to categorize and track your costs. You can also use tags to control
access to your resources as described in [Using tags with IAM policies](tagging-iot-iam.md "tagging-iot-iam.md").

For ease of use, the Tag Editor in the AWS Management Console provides a central,
unified way to create and manage your tags. For more information, see [Working with
Tag Editor](../../../awsconsolehelpdocs/latest/gsg/tag-editor.md "../../../awsconsolehelpdocs/latest/gsg/tag-editor.md") in [Working with the AWS Management
Console](../../../awsconsolehelpdocs/latest/gsg/getting-started.md "../../../awsconsolehelpdocs/latest/gsg/getting-started.md").

You can also work with tags using the AWS CLI and the AWS IoT API. You can associate tags with
thing groups, thing types, topic rules, jobs, security profiles, policies, billing groups, and
the packages and versions associated with things when you create them by using the
`Tags` field in the following commands:

- [CreateBillingGroup](../apireference/API_CreateBillingGroup.md "../apireference/API_CreateBillingGroup.md")
- [CreateDestination](../../../iot-wireless/latest/apireference/API_CreateDestination.md "../../../iot-wireless/latest/apireference/API_CreateDestination.md")
- [CreateDeviceProfile](../../../iot-wireless/latest/apireference/API_CreateDeviceProfile.md "../../../iot-wireless/latest/apireference/API_CreateDeviceProfile.md")
- [CreateDynamicThingGroup](../apireference/API_CreateDynamicThingGroup.md "../apireference/API_CreateDynamicThingGroup.md")
- [CreateJob](../apireference/API_CreateJob.md "../apireference/API_CreateJob.md")
- [CreateOTAUpdate](../apireference/API_CreateOTAUpdate.md "../apireference/API_CreateOTAUpdate.md")
- [CreatePolicy](../apireference/API_CreatePolicy.md "../apireference/API_CreatePolicy.md")
- [CreateScheduledAudit](../apireference/API_CreateScheduledAudit.md "../apireference/API_CreateScheduledAudit.md")
- [CreateSecurityProfile](../apireference/API_CreateSecurityProfile.md "../apireference/API_CreateSecurityProfile.md")
- [CreateServiceProfile](../../../iot-wireless/latest/apireference/API_CreateServiceProfile.md "../../../iot-wireless/latest/apireference/API_CreateServiceProfile.md")
- [CreateStream](../apireference/API_CreateStream.md "../apireference/API_CreateStream.md")
- [CreateThingGroup](../apireference/API_CreateThingGroup.md "../apireference/API_CreateThingGroup.md")
- [CreateThingType](../apireference/API_CreateThingType.md "../apireference/API_CreateThingType.md")
- [CreateTopicRule](../apireference/API_CreateTopicRule.md "../apireference/API_CreateTopicRule.md")
- [CreateWirelessGateway](../../../iot-wireless/latest/apireference/API_CreateWirelessGateway.md "../../../iot-wireless/latest/apireference/API_CreateWirelessGateway.md")
- [CreateWirelessDevice](../../../iot-wireless/latest/apireference/API_CreateWirelessDevice.md "../../../iot-wireless/latest/apireference/API_CreateWirelessDevice.md")

You can add, modify, or delete tags for existing resources that support tagging by using
the following commands:

- [TagResource](../apireference/API_TagResource.md "../apireference/API_TagResource.md")
- [ListTagsForResource](../apireference/API_ListTagsForResource.md "../apireference/API_ListTagsForResource.md")
- [UntagResource](../apireference/API_UntagResource.md "../apireference/API_UntagResource.md")

You can edit tag keys and values, and you can remove tags from a resource at any time. You
can set the value of a tag to an empty string, but you can't set the value of a tag to null.
If you add a tag that has the same key as an existing tag on that resource, the new value
overwrites the old value. If you delete a resource, any tags associated with the resource are
also deleted.

### Tag restrictions and limitations

The following basic restrictions apply to tags:

- Maximum number of tags per resource — 50
- Maximum key length — 127 Unicode characters in UTF-8
- Maximum value length — 255 Unicode characters in UTF-8
- Tag keys and values are case sensitive.
- Do not use the `aws:` prefix in your tag names or values. It's reserved
  for AWS use. You can't edit or delete tag names or values with this prefix. Tags with
  this prefix don't count against your tags per resource limit.
- If your tagging schema is used across multiple services and resources, remember that
  other services might have restrictions on allowed characters. Allowed characters include
  letters, spaces, and numbers representable in UTF-8, and the following special
  characters: + - = . \_ : / @.
