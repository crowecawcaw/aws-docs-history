# What is a tag?

A tag is a label that you assign to an AWS resource. Each tag consists of a key and
a value, both of which you define. Tags enable you to categorize your AWS resources by
attributes such as purpose, owner, and environment. When you have many resources of the
same type, quickly identify a specific resource based on the tags assigned
to it. For example, define a set of tags for your Amazon EMR Serverless
applications to help track each application's owner and stack level. We suggest
that you devise a consistent set of tag keys for each resource type.

Tags are not automatically assigned to your resources. After you add a tag to a
resource, modify a tag’s value or remove the tag from the resource at any time.
Tags do not have any semantic meaning to Amazon EMR Serverless and are interpreted
strictly as strings of characters. If you add a tag that has the same key as an existing
tag on that resource, the new value overwrites the earlier value.

If you use IAM, you can control which users in your AWS account have permission to
manage tags. For tag-based access control policy examples, refer to [Policies for tag-based access control](security-iam-TBAC.md "security-iam-TBAC.md").
