# Tag a workflow

You can assign tags to each Amazon MWAA Serverless workflow to help you manage resources. This section provides an overview of the tag functions and shows you how to create tags.

## What is a tag?

A tag is a label that you assign to an AWS resource. Each tag consists of a key and
a value, both of which you define. Tags enable you to categorize your AWS resources by
attributes such as purpose, owner, and workflow. When you have many resources of the
same type, you can quickly identify a specific resource based on the tags you've
assigned to it. For example, you can define a set of tags for your Amazon MWAA Serverless
applications to help you track each application's owner and stack level. We recommend
that you use consistent set of tag keys for each resource type.

Tags are not automatically assigned to your resources. After you add a tag to a
resource, you can modify a tag’s value or remove the tag from the resource at any time.
Tags do not have any semantic meaning to Amazon MWAA Serverless and are interpreted
strictly as strings of characters. If you add a tag that has the same key as an existing
tag on that resource, the new value overwrites the earlier value.

You can control which user in your AWS account has permissions to manage tags through IAM
For tag-based access control policy examples, see
[ABAC with Amazon MWAA Serverless](security_iam_service-with-iam.md#security_iam_service-with-iam-tags "security_iam_service-with-iam.md#security_iam_service-with-iam-tags").

## Tagging your resources

Workflows are the only Amazon MWAA Serverless resources that you can tag. If you're using the
Amazon MWAA Serverless API, the AWS CLI, or an AWS SDK, you can apply tags to new workflows
using the `tags` parameter on the relevant API action. You can apply tags to
existing workflows using the `TagResource` API action.

You can use some resource-creating actions to specify tags for a resource when the
resource is created. In this case, if tags cannot be applied while the resource is being
created, the resource fails to be created. This mechanism ensures that resources you
intended to tag on creation are either created with specified tags or not created at
all.

The following table describes the Amazon MWAA Serverless resources that can be tagged.

| Resource | Supports tags | Supports tag propagation                                                           | Supports tagging on creation (Amazon MWAA Serverless API, AWS CLI, and<br>AWS SDK) | API for creation (tags can be added during creation) |
| -------- | ------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------- |
| Workflow | Yes           | No. Tags associated with a workflow do not propagate to tasks within the workflow. | Yes                                                                                | `CreateWorkflow`                                     |

## Tagging limitations

The following basic limitations apply to tags:

- Each workflow can have a maximum of 50 user-created tags.
- For each workflow, each tag key must be unique, and each tag key can have only
  one value.
- The maximum key length is 128 Unicode characters in UTF-8.
- The maximum value length is 256 Unicode characters in UTF-8.
- Allowed characters are letters, numbers, spaces representable in UTF-8, and
  the following characters: \_ . : / = + - @.
- A tag key cannot be an empty string. A tag value can be an empty string, but
  not null.
- Tag keys and values are case sensitive.
- Do not use `AWS:` or any upper or lowercase combination of such
  as a prefix for either keys or values. These are reserved only for AWS
  use.

## Working with tags using the AWS CLI and the

Amazon MWAA Serverless API

Use the following AWS CLI commands or Amazon MWAA Serverless API operations to add, update,
list, and delete the tags for your workflows.

| Resource                          | Supports tags            | Supports tag propagation                                                                                                                                                   |
| --------------------------------- | ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Add or overwrite one or more tags | `tag-resource`           | [`TagResource`](../../../mwaa-serverless/latest/APIReference/API_TagResource.md "../../../mwaa-serverless/latest/APIReference/API_TagResource.md")                         |
| List tags for a resource          | `list-tags-for-resource` | [`ListTagsForResource`](../../../mwaa-serverless/latest/APIReference/API_ListTagsForResource.md "../../../mwaa-serverless/latest/APIReference/API_ListTagsForResource.md") |
| Delete one or more tags           | `untag-resource`         | [`UntagResource`](../../../mwaa-serverless/latest/APIReference/API_UntagResource.md "../../../mwaa-serverless/latest/APIReference/API_UntagResource.md")                   |

The following examples show how to tag or untag resources using the AWS CLI.

**Tag an existing workflow**

The following command tags an existing workflow.

CLI

```

aws mwaa-serverless tag-resource --resource-arn `workflow-arn` --tags `your-tag-key`=`your-tag-value`

```

**Untag an existing workflow**

The following command deletes a tag from an existing workflow.

CLI

```

aws mwaa-serverless untag-resource --resource-arn `workflow-arn` --tag-keys `your-tag-key`

```

**List tags for a workflow**

The following command lists the tags associated with an existing workflow.

CLI

```

aws mwaa-serverless list-tags-for-resource --resource-arn `workflow-arn`

```
