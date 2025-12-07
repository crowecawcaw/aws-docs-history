# CloudFormation custom resource request and response reference

CloudFormation manages custom resources through a request-response protocol that communicates with
your custom resource provider. Each request includes a request type (`Create`,
`Update`, or `Delete`) and follows this high-level workflow:

1. A template developer defines a custom resource with a `ServiceToken` and
   `ServiceTimeout` in the template and initiates a stack operation.
2. CloudFormation sends a JSON request to the custom resource provider through SNS or Lambda.
3. The custom resource provider processes the request and returns a JSON response to a presigned Amazon S3
   bucket URL before the timeout period expires.
4. CloudFormation reads the response and proceeds with the stack operation. If no response
   is received before the timeout period ends, the request is considered unsuccessful, and
   the stack operation fails.
   For more information, see [How custom resources work](template-custom-resources.md#how-custom-resources-work "template-custom-resources.md#how-custom-resources-work").

This section describes the structure, parameters, and expected responses for each request
type.

###### Note

The total size of the response body can't exceed 4096 bytes.

## Template setup

When defining a custom resource in a template, the template developer uses [AWS::CloudFormation::CustomResource](../TemplateReference/aws-resource-cloudformation-customresource.md "../TemplateReference/aws-resource-cloudformation-customresource.md") with the following
properties:

`ServiceToken`

An Amazon SNS topic ARN or Lambda function ARN from the same Region as the
stack.

_Required_: Yes

_Type_: String

`ServiceTimeout`

The maximum time, in seconds, before a custom resource operation times out. It
must be a value between 1 and 3600. Default: 3600 seconds (1 hour).

_Required_: No

_Type_: String

Additional resource properties are supported. Resource properties will be included as
`ResourceProperties` in the request. The custom resource provider must determine which
properties are valid and their acceptable values.

## Request object

Create
When the template developer creates a stack containing a custom resource, CloudFormation
sends a request with `RequestType` set to `Create`.

Create requests contain the following fields:

`RequestType`

`Create`.

_Required_: Yes

_Type_: String

`RequestId`

A unique ID for the request.

Combining the `StackId` with the
`RequestId` forms a value that you can use to uniquely identify a request on a particular
custom resource.

_Required_: Yes

_Type_: String

`StackId`

The Amazon Resource Name (ARN) that identifies the stack that contains the custom
resource.

Combining the `StackId` with the
`RequestId` forms a value that you can use to uniquely identify a request on a particular
custom resource.

_Required_: Yes

_Type_: String

`ResponseURL`

The response URL identifies a presigned S3 bucket that receives responses
from the custom resource provider to CloudFormation.

_Required_: Yes

_Type_: String

`ResourceType`

The template developer-chosen resource type of the custom resource in the
CloudFormation template. Custom resource type names can be up to 60
characters long and can include alphanumeric and the following
characters: `_@-`.

_Required_: Yes

_Type_: String

`LogicalResourceId`

The template developer-chosen name (logical ID) of the custom resource in the
CloudFormation template.

_Required_: Yes

_Type_: String

`ResourceProperties`

This field contains the contents of the `Properties`
object sent by the template developer. Its contents are defined by the custom resource provider.

_Required_: No

_Type_: JSON object

### Example

```
{
   "RequestType" : "Create",
   "RequestId" : "unique-request-id",
   "StackId" : "arn:aws:cloudformation:us-west-2:123456789012:stack/mystack/id",
   "ResponseURL" : "pre-signed-url-for-create-response",
   "ResourceType" : "Custom::MyCustomResourceType",
   "LogicalResourceId" : "resource-logical-id",
   "ResourceProperties" : {
      "key1" : "string",
      "key2" : [ "list" ],
      "key3" : { "key4" : "map" }
   }
}
```

Update
When the template developer makes changes to the properties of a custom resource
within the template and updates the stack, CloudFormation sends a request to the
custom resource provider with `RequestType` set to `Update`.
This means that your custom resource code doesn't have to detect changes in
resources because it knows that its properties have changed when the request type
is `Update`.

Update requests contain the following fields:

`RequestType`

`Update`.

_Required_: Yes

_Type_: String

`RequestId`

A unique ID for the request.

Combining the `StackId` with the
`RequestId` forms a value that you can use to uniquely identify a request on a particular
custom resource.

_Required_: Yes

_Type_: String

`StackId`

The Amazon Resource Name (ARN) that identifies the stack that contains the custom
resource.

Combining the `StackId` with the
`RequestId` forms a value that you can use to uniquely identify a request on a particular
custom resource.

_Required_: Yes

_Type_: String

`ResponseURL`

The response URL identifies a presigned S3 bucket that receives responses
from the custom resource provider to CloudFormation.

_Required_: Yes

_Type_: String

`ResourceType`

The template developer-chosen resource type of the custom resource in the
CloudFormation template. Custom resource type names can be up to 60
characters long and can include alphanumeric and the following
characters: `_@-`. You can't change the type during an
update.

_Required_: Yes

_Type_: String

`LogicalResourceId`

The template developer-chosen name (logical ID) of the custom resource in the
CloudFormation template.

_Required_: Yes

_Type_: String

`PhysicalResourceId`

A custom resource provider-defined physical ID that is unique
for that provider.

_Required_: Yes

_Type_: String

`ResourceProperties`

This field contains the contents of the `Properties`
object sent by the template developer. Its contents are defined by the custom resource provider.

_Required_: No

_Type_: JSON object

`OldResourceProperties`

Used only for `Update` requests. The resource property
values that were previously declared by the template developer in the
CloudFormation template.

_Required_: Yes

_Type_: JSON object

### Example

```
{
   "RequestType" : "Update",
   "RequestId" : "unique-request-id",
   "StackId" : "arn:aws:cloudformation:us-west-2:123456789012:stack/mystack/id",
   "ResponseURL" : "pre-signed-url-for-update-response",
   "ResourceType" : "Custom::MyCustomResourceType",
   "LogicalResourceId" : "resource-logical-id",
   "PhysicalResourceId" : "provider-defined-physical-id",
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

Delete
When the template developer deletes the stack or removes the custom resource from
the template and then updates the stack, CloudFormation sends a request with
`RequestType` set to `Delete`.

Delete requests contain the following fields:

`RequestType`

`Delete`.

_Required_: Yes

_Type_: String

`RequestId`

A unique ID for the request.

_Required_: Yes

_Type_: String

`StackId`

The Amazon Resource Name (ARN) that identifies the stack that contains the custom
resource.

_Required_: Yes

_Type_: String

`ResponseURL`

The response URL identifies a presigned S3 bucket that receives responses
from the custom resource provider to CloudFormation.

_Required_: Yes

_Type_: String

`ResourceType`

The template developer-chosen resource type of the custom resource in the
CloudFormation template. Custom resource type names can be up to 60
characters long and can include alphanumeric and the following
characters: `_@-`.

_Required_: Yes

_Type_: String

`LogicalResourceId`

The template developer-chosen name (logical ID) of the custom resource in the
CloudFormation template.

_Required_: Yes

_Type_: String

`PhysicalResourceId`

A custom resource provider-defined physical ID that is unique
for that provider.

_Required_: Yes

_Type_: String

`ResourceProperties`

This field contains the contents of the `Properties`
object sent by the template developer. Its contents are defined by the custom resource provider.

_Required_: No

_Type_: JSON object

### Example

```
{
   "RequestType" : "Delete",
   "RequestId" : "unique-request-id",
   "StackId" : "arn:aws:cloudformation:us-west-2:123456789012:stack/mystack/id",
   "ResponseURL" : "pre-signed-url-for-delete-response",
   "ResourceType" : "Custom::MyCustomResourceType",
   "LogicalResourceId" : "resource-logical-id",
   "PhysicalResourceId" : "provider-defined-physical-id",
   "ResourceProperties" : {
      "key1" : "string",
      "key2" : [ "list" ],
      "key3" : { "key4" : "map" }
   }
}
```

## Response object

The custom resource provider sends a response to the pre-signed URL for all request types. If the
custom resource provider doesn't send a response, CloudFormation waits until the operation times out.

The response must be a JSON object with the following fields:

`Status`

Must be either `SUCCESS` or `FAILED`.

_Required_: Yes

_Type_: String

`RequestId`

A unique ID for the request. Copy this value exactly as it appears in the
request.

_Required_: Yes

_Type_: String

`StackId`

The Amazon Resource Name (ARN) that identifies the stack that contains the custom
resource. Copy this value exactly as it appears in the
request.

_Required_: Yes

_Type_: String

`LogicalResourceId`

The template developer-chosen name (logical ID) of the custom resource in the
CloudFormation template. Copy this value exactly as it appears
in the request.

_Required_: Yes

_Type_: String

`PhysicalResourceId`

This value should be an identifier unique to the custom resource vendor, and
can be up to 1 KB in size. The value must be a non-empty string and must be
identical for all responses for the same resource.

When updating custom resources, the value returned for
`PhysicalResourceId` determines the update behavior. If the value
remains the same, CloudFormation considers it a normal update. If the value changes,
CloudFormation interprets the update as a replacement and sends a delete request to
the old resource. For more information, see [AWS::CloudFormation::CustomResource](../TemplateReference/aws-resource-cloudformation-customresource.md "../TemplateReference/aws-resource-cloudformation-customresource.md").

_Required_: Yes

_Type_: String

`Reason`

Describes the reason for a failure response.

Required if `Status` is `FAILED`. It's optional
otherwise.

_Required_: Conditional

_Type_: String

`NoEcho`

Indicates whether to mask the output of the custom resource when retrieved by
using the `Fn::GetAtt` function. If set to `true`, all
returned values are masked with asterisks (\*\*\*\*\*), _except for those
stored in the `Metadata` section of the template_.
CloudFormation does not transform, modify, or redact any information you include in
the `Metadata` section. The default value is `false`.

For more information about using `NoEcho` to mask sensitive
information, see the [Do not embed credentials in your templates](security-best-practices.md#creds "security-best-practices.md#creds") best
practice.

Available for `Create` and `Update` responses only. Not
supported for `Delete` responses.

_Required_: No

_Type_: Boolean

`Data`

The custom resource provider-defined name-value pairs to send with the response. You can
access the values provided here by name in the template with
`Fn::GetAtt`.

Available for `Create` and `Update` responses only. Not
supported for `Delete` responses.

###### Important

If the name-value pairs contain sensitive information, you should use the `NoEcho` field to mask the output of the custom resource.
Otherwise, the values are visible through APIs that surface property values (such as `DescribeStackEvents`).

_Required_: No

_Type_: JSON object

### Success Response Examples

#### `Create` and

`Update` Response

```
{
   "Status": "SUCCESS",
   "RequestId": "`unique-request-id`",
   "StackId": "`arn:aws:cloudformation:us-west-2:123456789012:stack/name/id`",
   "LogicalResourceId": "`resource-logical-id`",
   "PhysicalResourceId": "`provider-defined-physical-id`",
   "NoEcho": `true`,
   "Data": {
      "`key1`": "`value1`",
      "`key2`": "`value2`"
   }
}
```

#### `Delete`

Response

```
{
   "Status": "SUCCESS",
   "RequestId": "`unique-request-id`",
   "StackId": "`arn:aws:cloudformation:us-west-2:123456789012:stack/name/id`",
   "LogicalResourceId": "`resource-logical-id`",
   "PhysicalResourceId": "`provider-defined-physical-id`"
}
```

### Failed Response Example

```
{
   "Status": "FAILED",
   "RequestId": "`unique-request-id`",
   "StackId": "`arn:aws:cloudformation:us-west-2:123456789012:stack/name/id`",
   "LogicalResourceId": "`resource-logical-id`",
   "PhysicalResourceId": "`provider-defined-physical-id`",
   "Reason": "`Required failure reason string`"
}
```
