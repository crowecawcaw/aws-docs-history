# Tagging your managed integrations resources

To help you manage and organize your resources, you can optionally assign your own metadata
to each of these resources in the form of tags. This section describes tags and shows you how to
create them.

## Tag basics

You can use tags to categorize your managed integrations resources in different ways (for example, by
purpose, owner, or environment). This is useful when you have many resources of the same type
— you can quickly identify a resource based on the tags you've assigned to it. Each tag
consists of a key and optional value, both of which you define. For example, you can define a
set of tags for your thing types that helps you track devices by type. We recommend that you
create a set of tag keys that meets your needs for each kind of resource. Using a consistent
set of tag keys makes it easier for you to manage your resources.

You can search for and filter resources based on the tags you add or apply. You can also use tags to control
access to your resources as described in [Using tags with IAM policies](tagging-iot-iam.md "tagging-iot-iam.md").

For ease of use, the Tag Editor in the AWS Management Console provides a central,
unified way to create and manage your tags. For more information, see [Working with
Tag Editor](../../../awsconsolehelpdocs/latest/gsg/tag-editor.md "../../../awsconsolehelpdocs/latest/gsg/tag-editor.md") in [Working with the AWS Management
Console](../../../awsconsolehelpdocs/latest/gsg/getting-started.md "../../../awsconsolehelpdocs/latest/gsg/getting-started.md").

You can also work with tags using the AWS CLI and the managed integrations API. You can associate tags
with managed things, provisioning profiles, credential lockers, and over-the-air (OTA) tasks
when you create them by using the `Tags` field in the following commands:

- [CreateManagedThing](../APIReference/API_CreateManagedThing.md "../APIReference/API_CreateManagedThing.md")
- [CreateProvisioningProfile](../APIReference/API_CreateProvisioningProfile.md "../APIReference/API_CreateProvisioningProfile.md")
- [CreateCredentialLocker](../APIReference/API_CreateCredentialLocker.md "../APIReference/API_CreateCredentialLocker.md")
- [CreateOtaTask](../APIReference/API_CreateOtaTask.md "../APIReference/API_CreateOtaTask.md")
- [CreateAccountAssociation](../APIReference/API_CreateAccountAssociation.md "../APIReference/API_CreateAccountAssociation.md")

You can add, modify, or delete tags for existing resources that support tagging by using
the following commands:

- [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md")
- [ListTagsForResource](../APIReference/API_ListTagsForResource.md "../APIReference/API_ListTagsForResource.md")
- [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md")

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
