# Create custom provisioning logic with custom
 resources

Custom resources provide a way for you to write custom provisioning logic into your
 CloudFormation templates and have CloudFormation run it anytime you create, update (if you changed
 the custom resource), or delete a stack. This can be useful when your provisioning
 requirements involve complex logic or workflows that can't be expressed with CloudFormation's
 built-in resource types.

For example, you might want to include resources that aren't available as CloudFormation resource types. You can include those
 resources by using custom resources. That way, you can still manage all your related
 resources in a single stack.

To define a custom resource in your CloudFormation template, you use the [`AWS::CloudFormation::CustomResource`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudformation-customresource.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudformation-customresource.html") or [`Custom::`MyCustomResourceTypeName``](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudformation-customresource.html#aws-resource-cloudformation-customresource--remarks "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudformation-customresource.html#aws-resource-cloudformation-customresource--remarks")
 resource type. Custom resources require one property, the service token, which specifies
 where CloudFormation sends requests to, such as an Amazon SNS topic or a Lambda function.

The following topics provide information on how to use custom resources.

###### Topics

* [How custom resources work](#how-custom-resources-work "#how-custom-resources-work")
* [Response timeout](#response-timeout "#response-timeout")
* [Amazon SNS-backed custom resources](template-custom-resources-sns.md "template-custom-resources-sns.md")
* [Lambda-backed custom resources](template-custom-resources-lambda.md "template-custom-resources-lambda.md")
* [Custom resource reference](crpg-ref.md "crpg-ref.md")
###### Note

The CloudFormation registry and custom resources each offer their own benefits. Custom
 resources offer the following benefits:


* You don't need to register the resource.
* You can include an entire resource as part of a template without
 registering.
* Supports the `Create`, `Update`, and `Delete`
 operations
Advantages that registry based resources offer include the following:


* Supports the modeling, provisioning, and managing of third-party application
 resources
* Supports the `Create`, `Read`, `Update`,
 `Delete`, and `List` (`CRUDL`)
 operations
* Supports drift detection on private and third-party resource types
Unlike custom resources, registry based resources won't need to associate an Amazon SNS
 topic or a Lambda function to perform `CRUDL` operations. For more
 information, see [Managing extensions with the CloudFormation registry](registry.md "registry.md").


## How custom resources work


The general process for setting up a new custom resource includes the following steps.
 These steps involve two roles: the *custom resource provider* who owns the custom
 resource and the *template developer* who creates a template that includes
 a custom resource type. This can be the same person, but if not, the custom resource provider should
 work with the template developer.



1. The custom resource provider writes logic that determines how to handle requests from
 CloudFormation and perform actions on the custom resource.
2. The custom resource provider creates the Amazon SNS topic or Lambda function where CloudFormation can
 send requests to. The Amazon SNS topic or Lambda function must be in the same Region
 where the stack will be created.
3. The custom resource provider gives the Amazon SNS topic ARN or Lambda function ARN to the
 template developer.
4. The template developer defines the custom resource in their CloudFormation template.
 This includes a service token and any input data parameters. The service token
 and the structure of the input data are defined by the custom resource provider. The service
 token specifies the Amazon SNS topic ARN or Lambda function ARN and is always
 required, but the input data is optional depending on the custom
 resource.

Now, whenever anyone uses the template to create, update, or delete the custom
 resource, CloudFormation sends a request to the specified service token, and then waits for
 a response before proceeding with the stack operation. 


The following summarizes the flow for creating a stack from the template: 



1. CloudFormation sends a request to the specified service token. The request
 includes information such as the request type and a pre-signed Amazon Simple Storage Service URL,
 where the custom resource sends responses to. For more information about what's
 included in the request, see [Custom resource request objects](crpg-ref-requests.md "crpg-ref-requests.md").


The following sample data shows what CloudFormation includes in a
 `Create` request. In this example,
 `ResourceProperties` allows CloudFormation to create a custom payload
 to send to the Lambda function.



```
{
   "RequestType" : "Create",
   "ResponseURL" : "http://pre-signed-S3-url-for-response",
   "StackId" : "arn:aws:cloudformation:us-west-2:123456789012:stack/mystack/5b918d10-cd98-11ea-90d5-0a9cd3354c10",
   "RequestId" : "unique id for this create request",
   "ResourceType" : "Custom::TestResource",
   "LogicalResourceId" : "MyTestResource",
   "ResourceProperties" : {
      "Name" : "Value",
      "List" : [ "1", "2", "3" ]
   }
}
```
2. The custom resource provider processes the CloudFormation request and returns a response of
 `SUCCESS` or `FAILED` to the pre-signed URL. The
 custom resource provider provides the response in a JSON-formatted file and uploads it to the
 pre-signed S3 URL. For more information, see [Uploading objects with presigned URLs](../../../AmazonS3/latest/userguide/PresignedUrlUploadObject.md "../../../AmazonS3/latest/userguide/PresignedUrlUploadObject.md") in the *Amazon Simple Storage Service User Guide*.


In the response, the custom resource provider can also include name-value pairs that the
 template developer can access. For example, the response can include output data if
 the request succeeded or an error message if the request failed. For more
 information about responses, see [Custom resource response objects](crpg-ref-responses.md "crpg-ref-responses.md").


###### Important

If the name-value pairs contain sensitive information, you should use the `NoEcho` field to mask the output of the custom resource. 
Otherwise, the values are visible through APIs that surface property values (such as `DescribeStackEvents`).

For more information about using `NoEcho` to mask sensitive
 information, see the [Do not embed credentials in your templates](security-best-practices.md#creds "security-best-practices.md#creds") best
 practice.


The custom resource provider is responsible for listening and responding to the request. For
 example, for Amazon SNS notifications, the custom resource provider must listen and respond to
 notifications that are sent to a specific topic ARN. CloudFormation waits and
 listens for a response in the pre-signed URL location.


The following sample data shows what a custom resource might include in a
 response:



```
{
   "Status" : "SUCCESS",
   "PhysicalResourceId" : "TestResource1",
   "StackId" : "arn:aws:cloudformation:us-west-2:123456789012:stack/mystack/5b918d10-cd98-11ea-90d5-0a9cd3354c10",
   "RequestId" : "unique id for this create request",
   "LogicalResourceId" : "MyTestResource",
   "Data" : {
      "OutputName1" : "Value1",
      "OutputName2" : "Value2",
   }
}
```
3. After getting a `SUCCESS` response, CloudFormation proceeds with the
 stack operation. If a `FAILED` response or no response is returned,
 the operation fails. Any output data from the custom resource is stored in the
 pre-signed URL location. The template developer can retrieve that data by using the
 [Fn::GetAtt](resources-section-structure.md#resource-properties-getatt "resources-section-structure.md#resource-properties-getatt") function.

###### Note

If you use AWS PrivateLink, custom resources in the VPC must have access to CloudFormation-specific S3
 buckets. Custom resources must send responses to a pre-signed Amazon S3 URL. If they
 can't send responses to Amazon S3, CloudFormation won't receive a response and the stack
 operation fails. For more information, see [Access CloudFormation using an interface endpoint
 (AWS PrivateLink)](vpc-interface-endpoints.md "vpc-interface-endpoints.md").


## Response timeout


The default timeout for your custom resource is 3600 seconds (1 hour). If no response
 is received during this time, the stack operation fails.


You can adjust the timeout value based on how long you expect the response from the
 custom resource will take. For example, when provisioning a custom resource that invokes
 a Lambda function that's expected to respond within five minutes, you can set a timeout
 of five minutes in the stack template by specifying the `ServiceTimeout`
 property. For more information, see [Custom resource request objects](crpg-ref-requests.md "crpg-ref-requests.md"). This way, if there's an error in the Lambda
 function that causes it to get stuck, CloudFormation will fail the stack operation after
 five minutes instead of waiting the full hour. 


However, be careful not to set the timeout value too low. To avoid unexpected
 timeouts, make sure that your custom resource has enough time to perform the necessary
 actions and return a response.
