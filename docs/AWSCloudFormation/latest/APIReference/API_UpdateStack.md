# UpdateStack

Updates a stack as specified in the template. After the call completes successfully, the
 stack update starts. You can check the status of the stack through the [DescribeStacks](API_DescribeStacks.md "API_DescribeStacks.md") action.

To get a copy of the template for an existing stack, you can use the [GetTemplate](API_GetTemplate.md "API_GetTemplate.md") action.

For more information about updating a stack and monitoring the progress of the update, see
 [Managing
 AWS resources as a single unit with CloudFormation stacks](../UserGuide/stacks.md "../UserGuide/stacks.md") in the
 *AWS CloudFormation User Guide*.


## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**Capabilities.member.N**


In some cases, you must explicitly acknowledge that your stack template contains certain
 capabilities in order for CloudFormation to update the stack.



* `CAPABILITY_IAM` and `CAPABILITY_NAMED_IAM`



Some stack templates might include resources that can affect permissions in your
 AWS account, for example, by creating new IAM users. For those stacks, you must
 explicitly acknowledge this by specifying one of these capabilities.


The following IAM resources require you to specify either the
 `CAPABILITY_IAM` or `CAPABILITY_NAMED_IAM` capability.




	+ If you have IAM resources, you can specify either capability.
	+ If you have IAM resources with custom names, you *must*
	 specify `CAPABILITY_NAMED_IAM`.
	+ If you don't specify either of these capabilities, CloudFormation returns an
	 `InsufficientCapabilities` error.
If your stack template contains these resources, we suggest that you review all
 permissions associated with them and edit their permissions if necessary.




	+ [AWS::IAM::AccessKey](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-accesskey.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-accesskey.html")
	+ [AWS::IAM::Group](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-group.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-group.html")
	+ [AWS::IAM::InstanceProfile](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-instanceprofile.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-instanceprofile.html")
	+ [AWS::IAM::ManagedPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-managedpolicy.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-managedpolicy.html")
	+ [AWS::IAM::Policy](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-policy.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-policy.html")
	+ [AWS::IAM::Role](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-role.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-role.html")
	+ [AWS::IAM::User](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-user.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-user.html")
	+ [AWS::IAM::UserToGroupAddition](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-usertogroupaddition.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-usertogroupaddition.html")
For more information, see [Acknowledging IAM resources in CloudFormation templates](../UserGuide/control-access-with-iam.md#using-iam-capabilities "../UserGuide/control-access-with-iam.md#using-iam-capabilities").
* `CAPABILITY_AUTO_EXPAND`



Some template contain macros. Macros perform custom processing on templates; this can
 include simple actions like find-and-replace operations, all the way to extensive
 transformations of entire templates. Because of this, users typically create a change set
 from the processed template, so that they can review the changes resulting from the macros
 before actually updating the stack. If your stack template contains one or more macros,
 and you choose to update a stack directly from the processed template, without first
 reviewing the resulting changes in a change set, you must acknowledge this capability.
 This includes the [AWS::Include](../UserGuide/transform-aws-include.md "../UserGuide/transform-aws-include.md")
 and [AWS::Serverless](../UserGuide/transform-aws-serverless.md "../UserGuide/transform-aws-serverless.md") transforms, which are macros hosted by CloudFormation.


If you want to update a stack from a stack template that contains macros
 *and* nested stacks, you must update the stack directly from the
 template using this capability.


###### Important

You should only update stacks directly from a stack template that contains macros if
 you know what processing the macro performs.

Each macro relies on an underlying Lambda service function for processing stack
 templates. Be aware that the Lambda function owner can update the function operation
 without CloudFormation being notified.


For more information, see [Perform custom processing
 on CloudFormation templates with template macros](../UserGuide/template-macros.md "../UserGuide/template-macros.md").

###### Note

Only one of the `Capabilities` and `ResourceType` parameters can
 be specified.


Type: Array of strings


Valid Values: `CAPABILITY_IAM | CAPABILITY_NAMED_IAM | CAPABILITY_AUTO_EXPAND`



Required: No




**ClientRequestToken** 


A unique identifier for this `UpdateStack` request. Specify this token if you
 plan to retry requests so that CloudFormation knows that you're not attempting to update a stack
 with the same name. You might retry `UpdateStack` requests to ensure that
 CloudFormation successfully received them.


All events triggered by a given stack operation are assigned the same client request
 token, which you can use to track operations. For example, if you execute a
 `CreateStack` operation with the token `token1`, then all the
 `StackEvents` generated by that operation will have
 `ClientRequestToken` set as `token1`.


In the console, stack operations display the client request token on the Events tab. Stack
 operations that are initiated from the console use the token format
 *Console-StackOperation-ID*, which helps you easily identify the stack
 operation . For example, if you create a stack using the console, each stack event would be
 assigned the same token in the following format:
 `Console-CreateStack-7f59c3cf-00d2-40c7-b2ff-e75db0987002`.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.


Pattern: `[a-zA-Z0-9][-a-zA-Z0-9]*`



Required: No




**DisableRollback** 


Preserve the state of previously provisioned resources when an operation fails.


Default: `False`



Type: Boolean


Required: No




**NotificationARNs.member.N**


Amazon Simple Notification Service topic Amazon Resource Names (ARNs) that CloudFormation
 associates with the stack. Specify an empty list to remove all notification topics.


Type: Array of strings


Array Members: Maximum number of 5 items.


Required: No




**Parameters.member.N**


A list of `Parameter` structures that specify input parameters for the stack.
 For more information, see the [Parameter](API_Parameter.md "API_Parameter.md") data
 type.


Type: Array of [Parameter](API_Parameter.md "API_Parameter.md") objects


Required: No




**ResourceTypes.member.N**


The template resource types that you have permissions to work with for this update stack
 action, such as `AWS::EC2::Instance`, `AWS::EC2::*`, or
 `Custom::MyCustomInstance`.


If the list of resource types doesn't include a resource that you're updating, the stack
 update fails. By default, CloudFormation grants permissions to all resource types. IAM uses this
 parameter for CloudFormation-specific condition keys in IAM policies. For more information, see
 [Control access with
 AWS Identity and Access Management](../UserGuide/control-access-with-iam.md "../UserGuide/control-access-with-iam.md").


###### Note

Only one of the `Capabilities` and `ResourceType` parameters can
 be specified.


Type: Array of strings


Length Constraints: Minimum length of 1. Maximum length of 256.


Required: No




**RetainExceptOnCreate** 


When set to `true`, newly created resources are deleted when the operation
 rolls back. This includes newly created resources marked with a deletion policy of
 `Retain`.


Default: `false`



Type: Boolean


Required: No




**RoleARN** 


The Amazon Resource Name (ARN) of an IAM role that CloudFormation assumes to update the
 stack. CloudFormation uses the role's credentials to make calls on your behalf. CloudFormation always
 uses this role for all future operations on the stack. Provided that users have permission to
 operate on the stack, CloudFormation uses this role even if the users don't have permission to
 pass it. Ensure that the role grants least privilege.


If you don't specify a value, CloudFormation uses the role that was previously associated with
 the stack. If no role is available, CloudFormation uses a temporary session that is generated from
 your user credentials.


Type: String


Length Constraints: Minimum length of 20. Maximum length of 2048.


Required: No




**RollbackConfiguration** 


The rollback triggers for CloudFormation to monitor during stack creation and updating
 operations, and for the specified monitoring period afterwards.


Type: [RollbackConfiguration](API_RollbackConfiguration.md "API_RollbackConfiguration.md") object


Required: No




**StackName** 


The name or unique stack ID of the stack to update.


Type: String


Required: Yes




**StackPolicyBody** 


Structure that contains a new stack policy body. You can specify either the
 `StackPolicyBody` or the `StackPolicyURL` parameter, but not
 both.


You might update the stack policy, for example, in order to protect a new resource that
 you created during a stack update. If you don't specify a stack policy, the current policy
 that is associated with the stack is unchanged.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 16384.


Required: No




**StackPolicyDuringUpdateBody** 


Structure that contains the temporary overriding stack policy body. You can specify either
 the `StackPolicyDuringUpdateBody` or the `StackPolicyDuringUpdateURL`
 parameter, but not both.


If you want to update protected resources, specify a temporary overriding stack policy
 during this update. If you don't specify a stack policy, the current policy that is associated
 with the stack will be used.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 16384.


Required: No




**StackPolicyDuringUpdateURL** 


Location of a file that contains the temporary overriding stack policy. The URL must point
 to a policy (max size: 16KB) located in an S3 bucket in the same Region as the stack. The
 location for an Amazon S3 bucket must start with `https://`. URLs from S3 static
 websites are not supported.


You can specify either the `StackPolicyDuringUpdateBody` or the
 `StackPolicyDuringUpdateURL` parameter, but not both.


If you want to update protected resources, specify a temporary overriding stack policy
 during this update. If you don't specify a stack policy, the current policy that is associated
 with the stack will be used.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 5120.


Required: No




**StackPolicyURL** 


Location of a file that contains the updated stack policy. The URL must point to a policy
 (max size: 16KB) located in an S3 bucket in the same Region as the stack. The location for an
 Amazon S3 bucket must start with `https://`. URLs from S3 static websites are not
 supported.


You can specify either the `StackPolicyBody` or the `StackPolicyURL`
 parameter, but not both.


You might update the stack policy, for example, in order to protect a new resource that
 you created during a stack update. If you don't specify a stack policy, the current policy
 that is associated with the stack is unchanged.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 5120.


Required: No




**Tags.member.N**


Key-value pairs to associate with this stack. CloudFormation also propagates these tags to
 supported resources in the stack. You can specify a maximum number of 50 tags.


If you don't specify this parameter, CloudFormation doesn't modify the stack's tags. If you
 specify an empty value, CloudFormation removes all associated tags.


Type: Array of [Tag](API_Tag.md "API_Tag.md") objects


Array Members: Maximum number of 50 items.


Required: No




**TemplateBody** 


Structure that contains the template body with a minimum length of 1 byte and a maximum
 length of 51,200 bytes.


Conditional: You must specify only one of the following parameters:
 `TemplateBody`, `TemplateURL`, or set the
 `UsePreviousTemplate` to `true`.


Type: String


Length Constraints: Minimum length of 1.


Required: No




**TemplateURL** 


The URL of a file that contains the template body. The URL must point to a template that's
 located in an Amazon S3 bucket or a Systems Manager document. The location for an Amazon S3 bucket must
 start with `https://`.


Conditional: You must specify only one of the following parameters:
 `TemplateBody`, `TemplateURL`, or set the
 `UsePreviousTemplate` to `true`.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 5120.


Required: No




**UsePreviousTemplate** 


Reuse the existing template that is associated with the stack that you are
 updating.


When using templates with the `AWS::LanguageExtensions` transform, provide the
 template instead of using `UsePreviousTemplate` to ensure new parameter values and
 Systems Manager parameter updates are applied correctly. For more information, see [AWS::LanguageExtensions transform](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/transform-aws-languageextensions.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/transform-aws-languageextensions.html").


Conditional: You must specify only one of the following parameters:
 `TemplateBody`, `TemplateURL`, or set the
 `UsePreviousTemplate` to `true`.


Type: Boolean


Required: No




## Response Elements


The following element is returned by the service.





**StackId** 


Unique identifier of the stack.


Type: String




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**InsufficientCapabilities** 


The template contains resources with capabilities that weren't specified in the Capabilities parameter.


HTTP Status Code: 400




**TokenAlreadyExists** 


A client request token already exists.


HTTP Status Code: 400




## Examples


### UpdateStack


This example illustrates one usage of UpdateStack.


#### Sample Request



```

https://cloudformation.us-east-1.amazonaws.com/
 ?Action=UpdateStack
 &StackName=MyStack
 &TemplateBody=[Template Document]
 &Parameters.member.1.ParameterKey=AvailabilityZone
 &Parameters.member.1.ParameterValue=us-east-1a
 &Version=2010-05-15
 &SignatureVersion=2
 &Timestamp=2010-07-27T22%3A26%3A28.000Z
 &AWSAccessKeyId=[AWS Access KeyID]
 &Signature=[Signature]
```

#### Sample Response



```

<UpdateStackResponse xmlns="http://cloudformation.amazonaws.com/doc/2010-05-15/">
  <UpdateStackResult>
    <StackId>arn:aws:cloudformation:us-east-1:123456789:stack/MyStack/aaf549a0-a413-11df-adb3-5081b3858e83</StackId>
  </UpdateStackResult>
  <ResponseMetadata>
    <RequestId>b9b4b068-3a41-11e5-94eb-example</RequestId>
  </ResponseMetadata>
</UpdateStackResponse>
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/UpdateStack "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/UpdateStack")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/UpdateStack "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/UpdateStack")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/UpdateStack "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/UpdateStack")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/UpdateStack "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/UpdateStack")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/UpdateStack "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/UpdateStack")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/UpdateStack "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/UpdateStack")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/UpdateStack "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/UpdateStack")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/UpdateStack "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/UpdateStack")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/UpdateStack "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/UpdateStack")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/UpdateStack "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/UpdateStack")
