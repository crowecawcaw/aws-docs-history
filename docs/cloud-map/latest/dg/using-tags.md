# Tagging your AWS Cloud Map resources

A tag is a label that you assign to an AWS resource. Each tag consists of a _key_ and an
optional _value_, both of which you define.

Tags enable you to categorize your AWS resources by, for example, purpose, owner, or environment. When you
have many resources of the same type, you can quickly identify a specific resource based on the tags you've assigned
to it. For example, you can define a set of tags for your AWS Cloud Map services to help you track each service's owner and
stack level. We recommend that you devise a consistent set of tag keys for each resource
type.

Tags are not automatically assigned to your resources. After you add a tag, you can edit tag keys and values or
remove tags from a resource at any time. If you delete a resource, any tags for the resource are also deleted.

Tags don't have any semantic meaning to AWS Cloud Map and are interpreted strictly as a string of characters. You can
set the value of a tag to an empty string, but you can't set the value of a tag to null. If you add a tag that has
the same key as an existing tag on that resource, the new value overwrites the old value.

You can work with tags using the AWS Management Console, the AWS CLI, and the AWS Cloud Map API.

If you're using AWS Identity and Access Management (IAM), you can control which users in your AWS account have permission to create,
edit, or delete tags.

## How resources are tagged

You can tag new or existing AWS Cloud Map namespaces and services.

If you're using the AWS Cloud Map console, you can apply tags to new resources when they are created or to existing
resources at any time using the **Tags** tab on the relevant resource page.

If you're using the AWS Cloud Map API, the AWS CLI, or an AWS SDK, you can apply tags to new resources using the
`tags` parameter on the relevant API action or to existing resources using the [TagResource](../api/API_TagResource.md "../api/API_TagResource.md") API action. For more
information, see [TagResource](../api/API_TagResource.md "../api/API_TagResource.md").

Some resource-creating actions enable you to specify tags for a resource when the resource is created. If tags
cannot be applied during resource creation, the resource creation process fails. This ensures that resources you
intended to tag on creation are either created with specified tags or not created at all. If you tag resources at the
time of creation, you don't need to run custom tagging scripts after resource creation.

The following table describes the AWS Cloud Map resources that can be tagged, and the resources that can be tagged on
creation.

| Tagging support for AWS Cloud Map resources | Resource | Supports tags                                                                            | Supports tag propagation | Supports tagging on creation (AWS Cloud Map API, AWS CLI, AWS SDK) |
| ------------------------------------------- | -------- | ---------------------------------------------------------------------------------------- | ------------------------ | ------------------------------------------------------------------ |
| AWS Cloud Map namespaces                    | Yes      | No. Namespace tags don't propagate to any other resources associated with the namespace. | Yes                      |
| AWS Cloud Map services                      | Yes      | No. Service tags don't propagate to any other resources associated with the service.     | Yes                      |

## Restrictions

The following basic restrictions apply to tags:

- Maximum number of tags for each resource – 50
- For each resource, each tag key must be unique, and each tag key can have only one value.
- Maximum key length – 128 Unicode characters in UTF-8
- Maximum value length – 256 Unicode characters in UTF-8
- If your tagging schema is used across multiple AWS services and resources, remember that other services
  might have restrictions on allowed characters. Generally allowed characters are letters, numbers, spaces
  representable in UTF-8, and the following characters: + - = . \_ : / @.
- Tag keys and values are case sensitive.
- Don't use `aws:`, `AWS:`, or any upper or lowercase combination of such as a prefix for
  either keys or values, as it is reserved for AWS use. You can't edit or delete tag keys or values with this
  prefix. Tags with this prefix don't count against your tags-per-resource limit.
