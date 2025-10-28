# Tagging fundamentals

A tag consists of a key-value pair.
The tag key is a general label.
The tag value is a description of the tag key.
This topic descibes the fundamentals of tagging Amazon Inspector resources.
When tagging Amazon Inspector resources, consider the following:

- You can tag [suppression rules](findings-managing-supression-rules.md "findings-managing-supression-rules.md") and [CIS scan configurations](scanning-cis-create-cis-scan-configuration.md "scanning-cis-create-cis-scan-configuration.md").
- You can add as many as 50 tags to each of your Amazon Inspector resources.
- Tag keys must be unique.
- A tag key can only have one tag value.
- Tag keys and tag values can have a maximum of 128 UTF-8 characters.
  The characters can be letters, numbers, spaces, or the following symbols: `_` `.` `:` `/` `=` `+` `-` `@`.
- You cannot use the `aws` prefix in any of your tags or modify tags with this prefix.
  Tags with the `aws` prefix are reserved for use by AWS.
- Tags assigned to an Amazon Inspector resource are only available in your AWS account and in the AWS Region where you created them.
- When you delete a resource, all tags associated with it are deleted, too.

For more information about tags, see [Best practices and strategies](../../../tag-editor/latest/userguide/tagging.md "../../../tag-editor/latest/userguide/tagging.md") in the _Tagging AWS Resources and Tag Editor User Guide_.

###### Note

Tags are not intended to store confidential or sensitive information.
Never use tags to store this type of data.
Tags can be accessible from other AWS services.
