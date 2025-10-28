# Tag operations

Tags can help you categorize and allocate costs incurred by your Quick Sight resources. For more information about tags, see [User-defined cost allocation tags](../../../awsaccountbilling/latest/aboutv2/custom-tags.md "../../../awsaccountbilling/latest/aboutv2/custom-tags.md"). You can visualize costs of tagged resources that have consumption-based pricing in AWS cost and usage reports. For more information on cost and usage reports, see [What are AWS Cost and Usage Reports](../../../cur/latest/userguide/what-is-cur.md "../../../cur/latest/userguide/what-is-cur.md").

You can also use tags to scope user permissions by granting a user permission to access or change only resources with certain tag values. You can use the [TagResource](tag-resource.md "tag-resource.md") API operation with a resource that already has tags. If you specify a new tag key for the resource, this tag is appended to the list of tags associated with the resource. If you specify a tag key that is already associated with the resource, the new tag value that you specify replaces the previous value for that tag. You can tag a new Quick Sight managed user or IAM user at creation with a [RegisterUser](register-user.md "register-user.md") API call.

You can associate as many as 50 tags with a resource. Amazon Quick Sight supports tagging for a data sets, data sources, dashboards, users, and templates.

Tagging for Quick Sight works in a similar way to tagging for other AWS services. Quick Sight doesn't currently support the tag editor for AWS Resource Groups.

Tags that are used for Admin Pro, Author Pro, or Reader Pro users can't be used as cost allocation tags.

For more information about the Tag API operations, see the following topics.

###### Topics

- [ListTagsForResource](list-tags-for-resource.md "list-tags-for-resource.md")
- [TagResource](tag-resource.md "tag-resource.md")
- [UntagResource](untag-resource.md "untag-resource.md")

- [RegisterUser](register-user.md "register-user.md")
