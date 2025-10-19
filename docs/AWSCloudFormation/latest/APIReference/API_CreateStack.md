# CreateStack

Creates a stack as specified in the template. After the call completes successfully, the
 stack creation starts. You can check the status of the stack through the [DescribeStacks](API_DescribeStacks.md "API_DescribeStacks.md") operation.

For more information about creating a stack and monitoring stack progress, see [Managing AWS
 resources as a single unit with CloudFormation stacks](../UserGuide/stacks.md "../UserGuide/stacks.md") in the
 *AWS CloudFormation User Guide*.


## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**Capabilities.member.N**


In some cases, you must explicitly acknowledge that your stack template contains certain
 capabilities in order for CloudFormation to create the stack.



* `CAPABILITY_IAM` and `CAPABILITY_NAMED_IAM`



Some stack templates might include resources that can affect permissions in your
 AWS account; for example, by creating new IAM users. For those stacks, you must
 explicitly acknowledge this by specifying one of these capabilities.


The following IAM resources require you to specify either the
 `CAPABILITY_IAM` or `CAPABILITY_NAMED_IAM` capability.




	+ If you have IAM resources, you can specify either capability.
	+ If you have IAM resources with custom names, you *must*
	 specify `CAPABILITY_NAMED_IAM`.
	+ If you don't specify either of these capabilities, CloudFormation returns an
	 `InsufficientCapabilities` error.
If your stack template contains these resources, we recommend that you review all
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
 before actually creating the stack. If your stack template contains one or more macros,
 and you choose to create a stack directly from the processed template, without first
 reviewing the resulting changes in a change set, you must acknowledge this capability.
 This includes the [AWS::Include](../UserGuide/transform-aws-include.md "../UserGuide/transform-aws-include.md")
 and [AWS::Serverless](../UserGuide/transform-aws-serverless.md "../UserGuide/transform-aws-serverless.md") transforms, which are macros hosted by CloudFormation.


If you want to create a stack from a stack template that contains macros
 *and* nested stacks, you must create the stack directly from the
 template using this capability.


###### Important

You should only create stacks directly from a stack template that contains macros if
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


A unique identifier for this `CreateStack` request. Specify this token if you
 plan to retry requests so that CloudFormation knows that you're not attempting to create a stack
 with the same name. You might retry `CreateStack` requests to ensure that
 CloudFormation successfully received them.


All events initiated by a given stack operation are assigned the same client request
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


Set to `true` to disable rollback of the stack if stack creation failed. You
 can specify either `DisableRollback` or `OnFailure`, but not
 both.


Default: `false`



Type: Boolean


Required: No




**EnableTerminationProtection** 


Whether to enable termination protection on the specified stack. If a user attempts to
 delete a stack with termination protection enabled, the operation fails and the stack remains
 unchanged. For more information, see [Protect CloudFormation
 stacks from being deleted](../UserGuide/using-cfn-protect-stacks.md "../UserGuide/using-cfn-protect-stacks.md") in the *AWS CloudFormation User Guide*. Termination
 protection is deactivated on stacks by default.


For [nested stacks](../UserGuide/using-cfn-nested-stacks.md "../UserGuide/using-cfn-nested-stacks.md"),
 termination protection is set on the root stack and can't be changed directly on the nested
 stack.


Type: Boolean


Required: No




**NotificationARNs.member.N**


The Amazon SNS topic ARNs to publish stack related events. You can find your Amazon SNS topic ARNs
 using the Amazon SNS console or your Command Line Interface (CLI).


Type: Array of strings


Array Members: Maximum number of 5 items.


Required: No




**OnFailure** 


Determines what action will be taken if stack creation fails. This must be one of:
 `DO_NOTHING`, `ROLLBACK`, or `DELETE`. You can specify
 either `OnFailure` or `DisableRollback`, but not both.


###### Note

Although the default setting is `ROLLBACK`, there is one exception. This
 exception occurs when a StackSet attempts to deploy a stack instance and the stack instance
 fails to create successfully. In this case, the `CreateStack` call overrides the
 default setting and sets the value of `OnFailure` to `DELETE`.


Default: `ROLLBACK`



Type: String


Valid Values: `DO_NOTHING | ROLLBACK | DELETE`



Required: No




**Parameters.member.N**


A list of `Parameter` structures that specify input parameters for the stack.
 For more information, see the [Parameter](API_Parameter.md "API_Parameter.md") data
 type.


Type: Array of [Parameter](API_Parameter.md "API_Parameter.md") objects


Required: No




**ResourceTypes.member.N**


The template resource types that you have permissions to work with for this create stack
 action, such as `AWS::EC2::Instance`, `AWS::EC2::*`, or
 `Custom::MyCustomInstance`. Use the following syntax to describe template
 resource types: `AWS::*` (for all AWS resources), `Custom::*` (for all
 custom resources), `Custom::*logical\_ID*` (for a specific custom resource),
 `AWS::*service\_name*::*` (for all resources of a particular
 AWS service), and
 `AWS::*service\_name*::*resource\_logical\_ID*` (for a specific AWS resource).


If the list of resource types doesn't include a resource that you're creating, the stack
 creation fails. By default, CloudFormation grants permissions to all resource types. IAM uses
 this parameter for CloudFormation-specific condition keys in IAM policies. For more information,
 see [Control access with
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


The Amazon Resource Name (ARN) of an IAM role that CloudFormation assumes to create the
 stack. CloudFormation uses the role's credentials to make calls on your behalf. CloudFormation always
 uses this role for all future operations on the stack. Provided that users have permission to
 operate on the stack, CloudFormation uses this role even if the users don't have permission to
 pass it. Ensure that the role grants least privilege.


If you don't specify a value, CloudFormation uses the role that was previously associated with
 the stack. If no role is available, CloudFormation uses a temporary session that's generated from
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


The name that's associated with the stack. The name must be unique in the Region in which
 you are creating the stack.


###### Note

A stack name can contain only alphanumeric characters (case sensitive) and hyphens. It
 must start with an alphabetical character and can't be longer than 128 characters.


Type: String


Required: Yes




**StackPolicyBody** 


Structure that contains the stack policy body. For more information, see [Prevent updates to stack resources](../UserGuide/protect-stack-resources.md "../UserGuide/protect-stack-resources.md") in the *AWS CloudFormation User Guide*.
 You can specify either the `StackPolicyBody` or the `StackPolicyURL`
 parameter, but not both.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 16384.


Required: No




**StackPolicyURL** 


Location of a file that contains the stack policy. The URL must point to a policy (maximum
 size: 16 KB) located in an S3 bucket in the same Region as the stack. The location for an Amazon S3
 bucket must start with `https://`. URLs from S3 static websites are not
 supported.


You can specify either the `StackPolicyBody` or the `StackPolicyURL`
 parameter, but not both.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 5120.


Required: No




**Tags.member.N**


Key-value pairs to associate with this stack. CloudFormation also propagates these tags to the
 resources created in the stack. A maximum number of 50 tags can be specified.


Type: Array of [Tag](API_Tag.md "API_Tag.md") objects


Array Members: Maximum number of 50 items.


Required: No




**TemplateBody** 


Structure that contains the template body with a minimum length of 1 byte and a maximum
 length of 51,200 bytes.


Conditional: You must specify either `TemplateBody` or
 `TemplateURL`, but not both.


Type: String


Length Constraints: Minimum length of 1.


Required: No




**TemplateURL** 


The URL of a file that contains the template body. The URL must point to a template (max
 size: 1 MB) that's located in an Amazon S3 bucket or a Systems Manager document. The location for
 an Amazon S3 bucket must start with `https://`. URLs from S3 static websites are not
 supported.


Conditional: You must specify either the `TemplateBody` or the
 `TemplateURL` parameter, but not both.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 5120.


Required: No




**TimeoutInMinutes** 


The amount of time that can pass before the stack status becomes
 `CREATE_FAILED`; if `DisableRollback` is not set or is set to
 `false`, the stack will be rolled back.


Type: Integer


Valid Range: Minimum value of 1.


Required: No




## Response Elements


The following element is returned by the service.





**StackId** 


Unique identifier of the stack.


Type: String




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AlreadyExists** 


The resource with the name requested already exists.


HTTP Status Code: 400




**InsufficientCapabilities** 


The template contains resources with capabilities that weren't specified in the Capabilities parameter.


HTTP Status Code: 400




**LimitExceeded** 


The quota for the resource has already been reached.


For information about resource and stack limitations, see [AWS CloudFormation quotas](../UserGuide/cloudformation-limits.md "../UserGuide/cloudformation-limits.md") in the
 *AWS CloudFormation User Guide*.


HTTP Status Code: 400




**TokenAlreadyExists** 


A client request token already exists.


HTTP Status Code: 400




## Examples


### CreateStack


This example illustrates one usage of CreateStack.


#### Sample Request



```

https://cloudformation.us-east-1.amazonaws.com/
 ?Action=CreateStack
 &StackName=MyStack
 &TemplateBody=[Template Document]
 &NotificationARNs.member.1=arn:aws:sns:us-east-1:1234567890:my-topic
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

<CreateStackResponse xmlns="http://cloudformation.amazonaws.com/doc/2010-05-15/">
  <CreateStackResult>
    <StackId>arn:aws:cloudformation:us-east-1:123456789:stack/MyStack/aaf549a0-a413-11df-adb3-5081b3858e83</StackId>
  </CreateStackResult>
  <ResponseMetadata>
    <RequestId>b9b4b068-3a41-11e5-94eb-example</RequestId>
  </ResponseMetadata>
</CreateStackResponse>
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/CreateStack "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/CreateStack")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/CreateStack "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/CreateStack")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/CreateStack "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/CreateStack")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/CreateStack "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/CreateStack")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/CreateStack "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/CreateStack")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/CreateStack "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/CreateStack")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/CreateStack "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/CreateStack")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/CreateStack "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/CreateStack")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/CreateStack "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/CreateStack")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/CreateStack "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/CreateStack")
