

AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md)

# Tagging your Amazon Q Developer in chat applications resources
<a name="tagging-resources"></a>

A tag is a label that you assign to an AWS resource. Each tag consists of a key and an optional value, both of which you define. Tags help you manage, search for, and filter resources.

Tags help you categorize your AWS resources in different ways. For example, you can tag your resources by purpose, owner, or environment. This is useful when you have many resources of the same type. You can quickly identify a specific resource based on the tags you assigned to it. You can assign one or more tags to your AWS resources. Each tag has an associated value.

We recommend that you create a set of tag keys that meet your needs for each resource type. Use a consistent set of tags to more efficiently manage your AWS resources. You can search and filter the resources based on the tags you add.

Tags are interpreted strictly as a string of characters. They aren't automatically assigned to your resources. You can edit tag keys and values, as well as remove tags from a resource, at any time. You can set the value of a tag to an empty string. However, you can't set the value of a tag to null. If you add a tag that has the same key as an existing tag on that resource, the new value overwrites the previous value. If you delete a resource, any tags for the resource are also deleted.

## Managing tags
<a name="managing-tags"></a>

Tags consist of the `Key` and `Value` properties on a resource. You can use the Amazon Q Developer in chat applications console, the AWS CLI, or the Amazon Q Developer in chat applications API to add, edit, or delete the values for these properties. For more information about working with tags, see the following: 
+  [TagResource](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_TagResource.html), [UntagResource](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_UntagResource.html), and [ListTagsForResource](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_ListTagsForResource.html) API actions. 
+  [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chatbot/tag-resource.html), [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chatbot/untag-resource.html), and [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chatbot/list-tags-for-resource.html) in the *Amazon Q Developer in chat applications CLI Reference*. 
+  [Using Tag Editor](https://docs.aws.amazon.com/tag-editor/latest/userguide/tag-editor.html) in the * Resource Groups User Guide.* 

## Tagging restrictions
<a name="tagging-restrictions"></a>

The following basic restrictions apply to tags.


| Restriction | Description | 
| --- | --- | 
| Maximum number of tags per resource | 50 | 
| Maximum key length | 128 Unicode characters in UTF-8 | 
| Maximum value length | 256 Unicode characters in UTF-8 | 
| Prefix restriction | Don't use the `aws:` prefix in your tag names or values because it is reserved for AWS use. You can't edit or delete tag names or values with this prefix. Tags with this prefix don't count against the number of tags you can assign to a resource. | 
| Character restrictions | Tags may only contain Unicode letters, digits, white space, or these symbols: `_ . : / = + - @` | 