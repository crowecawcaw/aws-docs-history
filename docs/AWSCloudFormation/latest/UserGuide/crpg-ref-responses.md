# Custom resource response objects

This topic describes the properties of the response object for a CloudFormation custom
 resource.

For an introduction to custom resources and how they work, see [Create custom provisioning logic with custom
 resources](template-custom-resources.md "template-custom-resources.md").


## Custom resource provider response fields


The following are properties that the custom resource provider includes when it sends
 the JSON file to the presigned URL. For more information about uploading objects by using
 presigned URLs, see [Uploading objects with presigned URLs](../../../AmazonS3/latest/userguide/PresignedUrlUploadObject.md "../../../AmazonS3/latest/userguide/PresignedUrlUploadObject.md") in the *Amazon Simple Storage Service User Guide*.


###### Note

The total size of the response body can't exceed 4096 bytes.




`Status`

The status value sent by the custom resource provider in response to an AWS CloudFormation-generated
 request.


Must be either `SUCCESS` or `FAILED`.


*Required*: Yes


*Type*: String



`Reason`

Describes the reason for a failure response.


*Required*: Required if `Status` is `FAILED`. It's
 optional otherwise.


*Type*: String



`PhysicalResourceId`
This value should be an identifier unique to the custom resource
 vendor, and can be up to 1 KB in size. The value must be a non-empty string and must be identical for all responses for
 the same resource.

The value returned for a `PhysicalResourceId` can change custom resource update operations. 
 If the value returned is the same, it is considered a normal update. If the value returned is different, AWS CloudFormation recognizes the update 
 as a replacement and sends a delete request to the old resource. For more information, 
 see [`AWS::CloudFormation::CustomResource`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudformation-customresource.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudformation-customresource.html").


*Required*: Yes


*Type*: String



`StackId`

The Amazon Resource Name (ARN) that identifies the stack that contains the custom
 resource. This response value should be copied *verbatim* from the request.


*Required*: Yes


*Type*: String



`RequestId`

A unique ID for the request. This response value should be copied *verbatim* from the request.


*Required*: Yes


*Type*: String



`LogicalResourceId`

The template developer-chosen name (logical ID) of the custom resource in the
 AWS CloudFormation template. This response value should be copied *verbatim* from the request.


*Required*: Yes


*Type*: String



`NoEcho`

Optional. Indicates whether to mask the output of the custom resource when retrieved by using the `Fn::GetAtt` function. 
 If set to `true`, all returned values are masked with asterisks (\*\*\*\*\*), *except for those stored in the `Metadata` section of the
 template*. AWS CloudFormation does not transform, modify, or redact any information you include in the `Metadata` section. The default value is `false`.


For more information about using `NoEcho` to mask sensitive
 information, see the [Do not embed
 credentials in your templates](best-practices.md#creds "best-practices.md#creds") best practice.


*Required*: No


*Type*: Boolean



`Data`

Optional. The custom resource provider-defined name-value pairs to send with the response. You can access the values
 provided here by name in the template with `Fn::GetAtt`.


###### Important

If the name-value pairs contain sensitive information, you should use the `NoEcho` field to mask the output of the custom resource. 
Otherwise, the values are visible through APIs that surface property values (such as `DescribeStackEvents`).


*Required*: No


*Type*: JSON object
