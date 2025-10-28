# Organize Lightsail for Research resources with tags

With Amazon Lightsail for Research, you can assign tags to your resources. Each tag is a label that consists
of a **key** and an optional **value** that can make it efficient to manage your resources. A key without a
value is referred to as a key-only tag, and a key with a value is referred to as a key-value
tag. Although there are no inherent types of tags, they let you categorize your resources by
purpose, owner, environment, or other criteria. This is useful when you have many resources
of the same type. You can quickly identify a specific resource based on the tags you've
assigned to it. For example, you can define a set of tags that help you track each
resource’s project, or priority.

The following resources can be tagged in the Amazon Lightsail for Research console:

- Virtual computers
- Storage disks
- Snapshots
  The following restrictions apply to tags:

- The maximum number of tags per resource is 50.
- For each resource, each tag key must be unique. Each tag key can have only one
  value.
- The maximum **key** length is 128 Unicode characters
  in UTF-8.
- The maximum **value** length is 256 Unicode
  characters in UTF-8.
- If your tagging schema is used across multiple services and resources, remember
  that other services might have restrictions on allowed characters. Generally allowed
  characters are: letters, numbers, and spaces, and the following characters: `+

* = . \_ : / @`

- Tag keys and values are case-sensitive.
- Don't use the `aws:` prefix for keys or values. That prefix is reserved
  for AWS use.

###### Topics

- [Tag Lightsail for Research resources](create-tags.md "create-tags.md")
- [Remove tags from Lightsail for Research resources](delete-tags.md "delete-tags.md")
