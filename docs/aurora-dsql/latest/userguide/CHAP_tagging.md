

# Tagging resources in Aurora DSQL
<a name="CHAP_tagging"></a>

In AWS, tags are user-defined key-value pairs that you define and associate with Aurora DSQL resources such as clusters and CDC streams. Tags are optional. If you provide a key, the value is optional.

You can use the AWS Management Console, the AWS CLI, or the AWS SDKs to add, list, and delete tags on Aurora DSQL clusters and CDC streams. You can add tags during and after resource creation by using the AWS console. To tag a resource after creation with the AWS CLI, use the `TagResource` operation.

## Tagging clusters with a Name
<a name="SECTION_tagging-name"></a>

Aurora DSQL creates clusters with a globally unique identifier assigned as the Amazon Resource Name (ARN). If you want to assign a user friendly name to your cluster, we recommend that you use a Tag.

If you create a console with the Aurora DSQL console, Aurora DSQL automatically creates a tag. This tag has a key of **Name** and an automatically generated value that represents the name of the cluster. This value is configurable, so you can assign a more friendly name to your cluster. If a cluster has a Name tag with an associated value, you can see the value throughout the Aurora DSQL console.

## Tagging requirements
<a name="SECTION_tagging-requirements"></a>

Tags have the following requirements:
+ Keys can't be prefixed with `aws:`.
+ Keys must be unique per tag set.
+ A key must be between 1 and 128 allowed characters.
+ A value must be between 0 and 256 allowed characters.
+ Values do not need to be unique per tag set.
+ Allowed characters for keys and values are letters, digits, white space, and any of the following symbols: \_ . : / = \+ - @. 
+ Keys and values are case sensitive.

## Tagging CDC streams
<a name="SECTION_tagging-streams"></a>

CDC streams are independently taggable resources. You can add tags when you create a stream by passing the `--tags` parameter to `CreateStream`, and you can read, add, or remove tags on an existing stream by using `ListTagsForResource`, `TagResource`, and `UntagResource` with the stream ARN. Tags on a CDC stream are separate from tags on the parent cluster and from tags on the destination Amazon Kinesis data stream.

A CDC stream ARN has the format `arn:aws:dsql:{{region}}:{{account-id}}:cluster/{{cluster-id}}/stream/{{stream-id}}`. For more information about CDC streams, see [Change data capture (CDC) streams](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/cdc-streams.html).

## Tagging usage notes
<a name="SECTION_tagging-usage-notes"></a>

When using tags in Aurora DSQL, consider the following.
+ When using the AWS CLI or Aurora DSQL API operations, make sure to provide the Amazon Resource Name (ARN) for the Aurora DSQL resource to work with. For more information, see [ Amazon Resource Name (ARNs) format for Aurora DSQL resources](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/authentication-authorization.html#authentication-authorization-arn-format).
+ Each resource has one tag set, which is a collection of one or more tags assigned to the resource.
+ Each resource can have up to 50 tags per tag set.
+ If you delete a resource, any associated tags are deleted.
+ You can add tags when you create a resource, you can view and modify tags using the following API operations: `TagResource`, `UntagResource`, and `ListTagsForResource`.
+ You can use tags with IAM policies. You can use them to manage access to Aurora DSQL clusters and to control what actions can be applied to those resources. To learn more, see [Controlling access to AWS resources using tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html).
+ You can use tags for various other activities across AWS. To learn more, see [Common tagging strategies](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html#tag-strategies).