# Update request for CloudFormation custom

resources

When the template developer makes changes to the properties of a custom resource within the
template and updates the stack, CloudFormation sends a request to the custom resource provider
with `RequestType` set to `Update`. This means that your custom resource
code doesn't have to detect changes in resources because it knows that its properties have
changed when the request type is `Update`.

For an introduction to custom resources and how they work, see [Create custom provisioning logic with custom
resources](template-custom-resources.md "template-custom-resources.md").

## Request

Update requests contain the following fields:

`RequestType`

`Update`.

`RequestId`

A unique ID for the request.

`ResponseURL`

The response URL identifies a presigned S3 bucket that receives responses
from the custom resource provider to AWS CloudFormation.

`ResourceType`

The template developer-chosen resource type of the custom resource in the
CloudFormation template. Custom resource type names can be up to 60 characters long
and can include alphanumeric and the following characters: `_@-`. You
can't change the type during an update.

`LogicalResourceId`

The template developer-chosen name (logical ID) of the custom resource in the
AWS CloudFormation template.

`StackId`

The Amazon Resource Name (ARN) that identifies the stack that contains the custom
resource.

`PhysicalResourceId`
A required custom resource provider-defined physical ID that is unique
for that provider.

The value returned for a `PhysicalResourceId` can change custom resource update operations.
If the value returned is the same, it is considered a normal update. If the value returned is different, AWS CloudFormation recognizes the update
as a replacement and sends a delete request to the old resource. For more information,
see [`AWS::CloudFormation::CustomResource`](../TemplateReference/aws-resource-cloudformation-customresource.md "../TemplateReference/aws-resource-cloudformation-customresource.md").

`ResourceProperties`

The new resource property values that are declared by the template developer in the
updated CloudFormation template.

`OldResourceProperties`

The resource property values that were previously declared by the template developer
in the CloudFormation template.

### Example

```
{
   "RequestType" : "Update",
   "RequestId" : "unique id for this update request",
   "ResponseURL" : "pre-signed-url-for-update-response",
   "ResourceType" : "Custom::MyCustomResourceType",
   "LogicalResourceId" : "name of resource in template",
   "StackId" : "arn:aws:cloudformation:us-west-2:123456789012:stack/mystack/5b918d10-cd98-11ea-90d5-0a9cd3354c10",
   "PhysicalResourceId" : "custom resource provider-defined physical id",
   "ResourceProperties" : {
      "key1" : "new-string",
      "key2" : [ "new-list" ],
      "key3" : { "key4" : "new-map" }
   },
   "OldResourceProperties" : {
      "key1" : "string",
      "key2" : [ "list" ],
      "key3" : { "key4" : "map" }
   }
}
```

## Responses

### Success

If the custom resource provider is able to successfully update the resource, CloudFormation expects the
status to be set to `SUCCESS` in the response.

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
   "RequestId" : "unique id for this update request (copied from request)",
   "LogicalResourceId" : "name of resource in template (copied from request)",
   "StackId" : "arn:aws:cloudformation:us-west-2:123456789012:stack/mystack/5b918d10-cd98-11ea-90d5-0a9cd3354c10 (copied from request)",
   "PhysicalResourceId" : "custom resource provider-defined physical id",
   "Data" : {
      "keyThatCanBeUsedInGetAtt1" : "data for key 1",
      "keyThatCanBeUsedInGetAtt2" : "data for key 2"
   }
}
```

### Failed

If the resource can't be updated with a new set of properties, CloudFormation expects the
status to be set to `FAILED`, along with a failure reason in the
response.

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
   "RequestId" : "unique id for this update request (copied from request)",
   "LogicalResourceId" : "name of resource in template (copied from request)",
   "StackId" : "arn:aws:cloudformation:us-west-2:123456789012:stack/mystack/5b918d10-cd98-11ea-90d5-0a9cd3354c10 (copied from request)",
   "PhysicalResourceId" : "custom resource provider-defined physical id"
}
```
