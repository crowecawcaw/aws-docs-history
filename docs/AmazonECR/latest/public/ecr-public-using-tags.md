# Tag an Amazon ECR Public repository

To help you manage your Amazon ECR Public repositories, you can optionally assign your own
metadata to each repository by using _tags_. This topic provides an
overview about tags and how to create them.

## Tag basics

A tag is a label that you assign to an AWS resource. Each tag consists of a
_key_ and an optional _value_. You define both
of them.

You can use tags to categorize your AWS resources in different ways, for example, by
purpose, owner, or environment. This is useful when you have many resources of the same
type. This is because you can quickly identify a specific resource based on the tags
you've assigned to it. For example, you can define a set of tags for your account's
Amazon ECR Public repositories to track each repository's owner.

We recommend that you devise a set of tag keys that meets your specific needs. Using a
consistent set of tag keys can help you keep better track of your resources and find
specific resources quickly. That is, you can search and filter the resources based on
the specific tags that you add.

Tags don't have any semantic meaning to Amazon ECR and are interpreted strictly as a string of
characters. Tags aren't automatically assigned to your resources. You can edit tag keys
and values, and you can remove tags from a resource at any time. You can set the value
of a tag to an empty string. However, you can't set the value of a tag to null. If you
add a tag that has the same key as an existing tag on that resource, the new value
overwrites the old value. If you delete a resource, any tags for the resource are also
deleted.

You can work with tags using the AWS Management Console, the AWS CLI, and the Amazon ECR Public
API.

If you're using AWS Identity and Access Management (IAM), you can control which users in your AWS account have
permission to manage tags.

## Tagging your resources

You can tag new or existing Amazon ECR Public repositories.

If you're using the Amazon ECR console, you can apply tags to new resources when they're created
or to existing resources by using the **Tags** option on the navigation
pane at any time.

If you're using the Amazon ECR Public API, the AWS CLI, or an AWS SDK, you can apply tags
to new repositories using the `tags` parameter on the
`CreateRepository` API action or use the `TagResource` API
action to apply tags to existing resources. For more information, see [TagResource](../../../AmazonECRPublic/latest/APIReference/API_TagResource.md "../../../AmazonECRPublic/latest/APIReference/API_TagResource.md").

Additionally, if tags can't be applied when a repository is created, the repository creation
process is rolled back. This ensures that repositories are either created with tags or
not created at all and that no repositories are left untagged at any time. By tagging
repositories when they're created, you eliminate the need to run custom tagging scripts
after the repository is created.
