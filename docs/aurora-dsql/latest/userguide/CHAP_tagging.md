# Tagging resources in Aurora DSQL

In AWS, tags are user-defined key-value pairs that you define and associate with Aurora DSQL
resources such as clusters. Tags are optional. If you provide a key, the value is optional.

You can use the AWS Management Console, the AWS CLI, or the AWS SDKs to add, list, and delete tags
on Aurora DSQL clusters. You can add tags during and after
cluster creation using the AWS console. To tag a cluster after creation with the AWS CLI
use the `TagResource` operation.

## Tagging clusters with a Name

Aurora DSQL creates clusters with a globally unique identifier assigned as the Amazon Resource Name (ARN). If you want to
assign a user friendly name to your cluster, we recommend that you use a Tag.

If you create a console with the Aurora DSQL console, Aurora DSQL automatically creates a tag. This tag has a key of **Name**
and an automatically generated value that represents the name of the cluster. This value is configurable, so you can assign
a more friendly name to your cluster. If a cluster has a Name tag with an associated value,
you can see the value throughout the Aurora DSQL console.

## Tagging requirements

Tags have the following requirements:

- Keys can't be prefixed with `aws:`.
- Keys must be unique per tag set.
- A key must be between 1 and 128 allowed characters.
- A value must be between 0 and 256 allowed characters.
- Values do not need to be unique per tag set.
- Allowed characters for keys and values are letters, digits, white space, and
  any of the following symbols: \_ . : / = + - @.
- Keys and values are case sensitive.

## Tagging usage notes

When using tags in Aurora DSQL, consider the following.

- When using the AWS CLI or Aurora DSQL API operations, make sure to provide the
  Amazon Resource Name (ARN) for the Aurora DSQL resource to work with. For more information,
  see [Amazon Resource Name (ARNs) format for Aurora DSQL resources](authentication-authorization.md#authentication-authorization-arn-format "authentication-authorization.md#authentication-authorization-arn-format").
- Each resource has one tag set, which is a collection of one or more tags assigned to the resource.
- Each resource can have up to 50 tags per tag set.
- If you delete a resource, any associated tags are deleted.
- You can add tags when you create a resource, you can view and modify tags using the following API operations:
  `TagResource`, `UntagResource`, and `ListTagsForResource`.
- You can use tags with IAM policies. You can use them to manage access to
  Aurora DSQL clusters and to control what actions can be applied to those resources. To learn more,
  see [Controlling access to AWS resources using tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md").
- You can use tags for various other activities across AWS. To learn more, see [Common tagging strategies](../../../tag-editor/latest/userguide/best-practices-and-strats.md#tag-strategies "../../../tag-editor/latest/userguide/best-practices-and-strats.md#tag-strategies").
