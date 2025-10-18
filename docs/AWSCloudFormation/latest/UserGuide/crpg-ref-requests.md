# Custom resource request objects

This topic describes the properties of the request object for a CloudFormation custom
 resource.

For an introduction to custom resources and how they work, see [Create custom provisioning logic with custom
 resources](template-custom-resources.md "template-custom-resources.md").


## Template developer request properties


The template developer uses the CloudFormation resource, [AWS::CloudFormation::CustomResource](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudformation-customresource.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudformation-customresource.html"), to specify a custom
 resource in a template.


In `AWS::CloudFormation::CustomResource`, all properties are defined by the
 custom resource provider. There is only one required property: `ServiceToken`.




`ServiceTimeout`

The maximum time, in seconds, that can elapse before a custom resource
 operation times out.


The value must be an integer from 1 to 3600. The default value is 3600 seconds
 (1 hour).


*Required*: No


*Type*: String



`ServiceToken`

The service token, such as an Amazon SNS topic ARN or Lambda function ARN. The
 service token must be from the same Region as the stack.


*Required*: Yes


*Type*: String




All other fields in the resource properties are optional and are sent, verbatim, to the
 custom resource provider in the request's `ResourceProperties` field. The provider defines both
 the names and the valid contents of these fields.


## Custom resource provider request fields


These fields are sent in JSON requests from CloudFormation to the custom resource provider in the SNS topic
 that the provider has configured for this purpose.




`RequestType`

The request type is set by the CloudFormation stack operation (create-stack,
 update-stack, or delete-stack) that was initiated by the template developer for the
 stack that contains the custom resource.


Must be one of: `Create`, `Update`, or
 `Delete`. For more information, see [Custom resource request types](crpg-ref-requesttypes.md "crpg-ref-requesttypes.md").


*Required*: Yes


*Type*: String



`ResponseURL`

The response URL identifies a presigned S3 bucket that receives responses
 from the custom resource provider to AWS CloudFormation.


*Required*: Yes


*Type*: String



`StackId`

The Amazon Resource Name (ARN) that identifies the stack that contains the custom
 resource.


Combining the `StackId` with the
 `RequestId` forms a value that you can use to uniquely identify a request on a particular
 custom resource.


*Required*: Yes


*Type*: String



`RequestId`

A unique ID for the request.


Combining the `StackId` with the
 `RequestId` forms a value that you can use to uniquely identify a request on a particular
 custom resource.


*Required*: Yes


*Type*: String



`ResourceType`

The template developer-chosen resource type of the custom resource in the
 CloudFormation template. Custom resource type names can be up to 60 characters long
 and can include alphanumeric and the following characters:
 `_@-`.


*Required*: Yes


*Type*: String



`LogicalResourceId`

The template developer-chosen name (logical ID) of the custom resource in the
 AWS CloudFormation template. This is provided to facilitate
 communication between the custom resource provider and the template developer.


*Required*: Yes


*Type*: String



`PhysicalResourceId`
A required custom resource provider-defined physical ID that is unique
 for that provider.

The value returned for a `PhysicalResourceId` can change custom resource update operations. 
 If the value returned is the same, it is considered a normal update. If the value returned is different, AWS CloudFormation recognizes the update 
 as a replacement and sends a delete request to the old resource. For more information, 
 see [`AWS::CloudFormation::CustomResource`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudformation-customresource.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudformation-customresource.html").


*Required*: Always sent with `Update` and `Delete`
 requests; never sent with `Create`.


*Type*: String



`ResourceProperties`

This field contains the contents of the `Properties`
 object sent by the template developer. Its contents are defined by the custom resource provider.


*Required*: No


*Type*: JSON object



`OldResourceProperties`

Used only for `Update` requests. Contains the resource
 properties that were declared previous to the update request.


*Required*: Yes


*Type*: JSON object
