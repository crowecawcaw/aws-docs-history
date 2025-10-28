# Tag basics

A tag is a label that you assign to an AWS resource. Each tag consists of a _key_ and an
optional _value_, both of which you define.

Tags enable you to categorize your AWS resources by, for example, purpose, owner, or environment. When you
have many resources of the same type, you can quickly identify a specific resource based on the tags you've assigned
to it. For example, you can define a set of tags for your AWS Batch services to help you track each service's owner and
stack level. We recommend that you devise a consistent set of tag keys for each resource
type.

Tags are not automatically assigned to your resources. After you add a tag, you can edit tag keys and values or
remove tags from a resource at any time. If you delete a resource, any tags for the resource are also deleted.

Tags don't have any semantic meaning to AWS Batch and are interpreted strictly as a string of characters. You can
set the value of a tag to an empty string, but you can't set the value of a tag to null. If you add a tag that has
the same key as an existing tag on that resource, the new value overwrites the old value.

You can work with tags using the AWS Management Console, the AWS CLI, and the AWS Batch API.

If you're using AWS Identity and Access Management (IAM), you can control which users in your AWS account have permission to create,
edit, or delete tags.
