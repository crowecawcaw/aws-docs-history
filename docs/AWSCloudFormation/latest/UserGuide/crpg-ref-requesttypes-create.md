# Create request for CloudFormation custom

resources

When the template developer creates a stack containing a custom resource, CloudFormation sends a
request to the custom resource provider with `RequestType` set to
`Create`. This request happens specifically when the custom resource is being
created.

For an introduction to custom resources and how they work, see [Create custom provisioning logic with custom
resources](template-custom-resources.md "template-custom-resources.md").

## Request

Create requests contain the following fields:

`RequestType`

`Create`.

`RequestId`

A unique ID for the request.

`ResponseURL`

The response URL identifies a presigned S3 bucket that receives responses
from the custom resource provider to AWS CloudFormation.

`ResourceType`

The template developer-chosen resource type of the custom resource in the
CloudFormation template. Custom resource type names can be up to 60 characters long
and can include alphanumeric and the following characters:
`_@-`.

`LogicalResourceId`

The template developer-chosen name (logical ID) of the custom resource in the
AWS CloudFormation template.

`StackId`

The Amazon Resource Name (ARN) that identifies the stack that contains the custom
resource.

`ResourceProperties`

This field contains the contents of the `Properties`
object sent by the template developer. Its contents are defined by the custom resource provider.

### Example

```
{
   "RequestType" : "Create",
   "RequestId" : "unique id for this create request",
   "ResponseURL" : "pre-signed-url-for-create-response",
   "ResourceType" : "Custom::MyCustomResourceType",
   "LogicalResourceId" : "name of resource in template",
   "StackId" : "arn:aws:cloudformation:us-west-2:123456789012:stack/mystack/5b918d10-cd98-11ea-90d5-0a9cd3354c10",
   "ResourceProperties" : {
      "key1" : "string",
      "key2" : [ "list" ],
      "key3" : { "key4" : "map" }
   }
}
```

## Responses

### Success

When the create request is successful, a response must be sent to the Amazon S3 bucket
with the following fields:

`Status`

Must be `SUCCESS`.

`RequestId`

A unique ID for the request. This response value should be copied _verbatim_ from the request.

`LogicalResourceId`

The template developer-chosen name (logical ID) of the custom resource in the
AWS CloudFormation template. This response value should be copied _verbatim_ from the request.

`StackId`

The Amazon Resource Name (ARN) that identifies the stack that contains the custom
resource. This response value should be copied _verbatim_ from the request.

`PhysicalResourceId`
This value should be an identifier unique to the custom resource
vendor, and can be up to 1 KB in size. The value must be a non-empty string and must be identical for all responses for
the same resource.

The value returned for a `PhysicalResourceId` can change custom resource update operations.
If the value returned is the same, it is considered a normal update. If the value returned is different, AWS CloudFormation recognizes the update
as a replacement and sends a delete request to the old resource. For more information,
see [`AWS::CloudFormation::CustomResource`](../TemplateReference/aws-resource-cloudformation-customresource.md "../TemplateReference/aws-resource-cloudformation-customresource.md").

`NoEcho`

Optional. Indicates whether to mask the output of the custom resource when retrieved by using the `Fn::GetAtt` function.
If set to `true`, all returned values are masked with asterisks (\*\*\*\*\*), _except for those stored in the `Metadata` section of the
template_. AWS CloudFormation does not transform, modify, or redact any information you include in the `Metadata` section. The default value is `false`.

For more information about using `NoEcho` to mask sensitive
information, see the [Do not embed credentials in your templates](security-best-practices.md#creds "security-best-practices.md#creds") best
practice.

`Data`

Optional. The custom resource provider-defined name-value pairs to send with the response. You can access the values
provided here by name in the template with `Fn::GetAtt`.

###### Important

If the name-value pairs contain sensitive information, you should use the `NoEcho` field to mask the output of the custom resource.
Otherwise, the values are visible through APIs that surface property values (such as `DescribeStackEvents`).

#### Example

```
{
   "Status" : "SUCCESS",
   "RequestId" : "unique id for this create request (copied from request)",
   "LogicalResourceId" : "name of resource in template (copied from request)",
   "StackId" : "arn:aws:cloudformation:us-west-2:123456789012:stack/mystack/5b918d10-cd98-11ea-90d5-0a9cd3354c10 (copied from request)",
   "PhysicalResourceId" : "required vendor-defined physical id that is unique for that vendor",
   "Data" : {
      "keyThatCanBeUsedInGetAtt1" : "data for key 1",
      "keyThatCanBeUsedInGetAtt2" : "data for key 2"
   }
}
```

### Failed

When the create request fails, a response must be sent to the S3 bucket with the
following fields:

`Status`

Must be `FAILED`.

`Reason`

Describes the reason for a failure response.

`RequestId`

A unique ID for the request. This response value should be copied _verbatim_ from the request.

`LogicalResourceId`

The template developer-chosen name (logical ID) of the custom resource in the
AWS CloudFormation template. This response value should be copied _verbatim_ from the request.

`StackId`

The Amazon Resource Name (ARN) that identifies the stack that contains the custom
resource. This response value should be copied _verbatim_ from the request.

`PhysicalResourceId`
This value should be an identifier unique to the custom resource
vendor, and can be up to 1 KB in size. The value must be a non-empty string and must be identical for all responses for
the same resource.

The value returned for a `PhysicalResourceId` can change custom resource update operations.
If the value returned is the same, it is considered a normal update. If the value returned is different, AWS CloudFormation recognizes the update
as a replacement and sends a delete request to the old resource. For more information,
see [`AWS::CloudFormation::CustomResource`](../TemplateReference/aws-resource-cloudformation-customresource.md "../TemplateReference/aws-resource-cloudformation-customresource.md").

#### Example

```
{
   "Status" : "FAILED",
   "Reason" : "Required failure reason string",
   "RequestId" : "unique id for this create request (copied from request)",
   "LogicalResourceId" : "name of resource in template (copied from request)",
   "StackId" : "arn:aws:cloudformation:us-west-2:123456789012:stack/mystack/5b918d10-cd98-11ea-90d5-0a9cd3354c10 (copied from request)",
   "PhysicalResourceId" : "required vendor-defined physical id that is unique for that vendor"
}
```
