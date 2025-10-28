# Tagging APIs in AWS Glue

## Data types

- [Tag structure](#aws-glue-api-tags-Tag "#aws-glue-api-tags-Tag")

## Tag structure

The `Tag` object represents a label that you can assign to
an AWS resource. Each tag consists of a key and an optional value,
both of which you define.

For more information about tags, and controlling access to resources
in AWS Glue, see [AWS Tags in AWS Glue](monitor-tags.md "monitor-tags.md") and [Specifying
AWS Glue Resource ARNs](glue-specifying-resource-arns.md "glue-specifying-resource-arns.md") in the developer guide.

###### Fields

- `key` – UTF-8 string, not less than 1 or more than 128 bytes long.

The tag key. The key is required when you create a tag on an object. The key
is case-sensitive, and must not contain the prefix aws.

- `value` – UTF-8 string, not more than 256 bytes long.

The tag value. The value is optional when you create a tag on an object. The
value is case-sensitive, and must not contain the prefix aws.

## Operations

- [TagResource action (Python: tag_resource)](#aws-glue-api-tags-TagResource "#aws-glue-api-tags-TagResource")
- [UntagResource action (Python: untag_resource)](#aws-glue-api-tags-UntagResource "#aws-glue-api-tags-UntagResource")
- [GetTags action (Python: get_tags)](#aws-glue-api-tags-GetTags "#aws-glue-api-tags-GetTags")

## TagResource action (Python: tag_resource)

Adds tags to a resource. A tag is a label you can assign to an AWS resource. In AWS Glue, you can tag only certain resources. For information
about what resources you can tag, see [AWS Tags in AWS Glue](monitor-tags.md "monitor-tags.md").

In addition to the tagging permissions to call tag related APIs, you also
need the `glue:GetConnection` permission to call tagging APIs
on connections, and the `glue:GetDatabase` permission to call
tagging APIs on databases.

###### Request

- `ResourceArn` – _Required:_ UTF-8 string, not less than 1 or more than 10240 bytes long, matching the [Custom string pattern #50](aws-glue-api-common.md#regex_50 "aws-glue-api-common.md#regex_50").

The ARN of the AWS Glue resource to which to add the tags. For
more information about AWS Glue resource ARNs, see the [AWS Glue ARN string pattern](aws-glue-api-common.md#aws-glue-api-regex-aws-glue-arn-id "aws-glue-api-common.md#aws-glue-api-regex-aws-glue-arn-id").

- `TagsToAdd` – _Required:_ A map array of key-value pairs, not more than 50 pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a UTF-8 string, not more than 256 bytes long.

Tags to add to this resource.

###### Response

- _No Response parameters._

###### Errors

- `ResourceNotFoundException`

## UntagResource action (Python: untag_resource)

Removes the specified tags from an integration resource.

###### Request

- `ResourceArn` – _Required:_ UTF-8 string, not less than 1 or more than 10240 bytes long, matching the [Custom string pattern #50](aws-glue-api-common.md#regex_50 "aws-glue-api-common.md#regex_50").

The Amazon Resource Name (ARN) for the integration resource.

- `TagsToRemove` – _Required:_ An array of UTF-8 strings, not more than 50 strings.

A list of metadata tags to be removed from the resource.

###### Response

- _No Response parameters._

###### Errors

- `ResourceNotFoundException`

## GetTags action (Python: get_tags)

Retrieves a list of tags associated with a resource.

###### Request

- `ResourceArn` – _Required:_ UTF-8 string, not less than 1 or more than 10240 bytes long, matching the [Custom string pattern #50](aws-glue-api-common.md#regex_50 "aws-glue-api-common.md#regex_50").

The Amazon Resource Name (ARN) of the resource for which to retrieve tags.

###### Response

- `Tags` – A map array of key-value pairs, not more than 50 pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a UTF-8 string, not more than 256 bytes long.

The requested tags.

###### Errors

- `InvalidInputException`
- `InternalServiceException`
- `OperationTimeoutException`
- `EntityNotFoundException`
