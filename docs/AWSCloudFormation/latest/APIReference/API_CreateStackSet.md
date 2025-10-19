# CreateStackSet

Creates a StackSet.


## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**AdministrationRoleARN** 


The Amazon Resource Name (ARN) of the IAM role to use to create this StackSet.


Specify an IAM role only if you are using customized administrator roles to control
 which users or groups can manage specific StackSets within the same administrator account. For
 more information, see [Grant
 self-managed permissions](../UserGuide/stacksets-prereqs-self-managed.md "../UserGuide/stacksets-prereqs-self-managed.md") in the *AWS CloudFormation User Guide*.


Valid only if the permissions model is `SELF_MANAGED`.


Type: String


Length Constraints: Minimum length of 20. Maximum length of 2048.


Required: No




**AutoDeployment** 


Describes whether StackSets automatically deploys to AWS Organizations accounts that
 are added to the target organization or organizational unit (OU). For more information, see
 [Enable or disable automatic deployments for StackSets in AWS Organizations](../UserGuide/stacksets-orgs-manage-auto-deployment.md "../UserGuide/stacksets-orgs-manage-auto-deployment.md")
 in the *AWS CloudFormation User Guide*.


Required if the permissions model is `SERVICE_MANAGED`. (Not used with
 self-managed permissions.)


Type: [AutoDeployment](API_AutoDeployment.md "API_AutoDeployment.md") object


Required: No




**CallAs** 


Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.


By default, `SELF` is specified. Use `SELF` for StackSets with
 self-managed permissions.



* To create a StackSet with service-managed permissions while signed in to the management account, specify `SELF`.
* To create a StackSet with service-managed permissions while signed in to a delegated
 administrator account, specify `DELEGATED_ADMIN`.


Your AWS account must be registered as a delegated admin in the management account. For more information, see [Register a
 delegated administrator](../UserGuide/stacksets-orgs-delegated-admin.md "../UserGuide/stacksets-orgs-delegated-admin.md") in the *AWS CloudFormation User Guide*.

StackSets with service-managed permissions are created in the management account, including StackSets that are created by delegated administrators.


Valid only if the permissions model is `SERVICE_MANAGED`.


Type: String


Valid Values: `SELF | DELEGATED_ADMIN`



Required: No




**Capabilities.member.N**


In some cases, you must explicitly acknowledge that your StackSet template contains
 certain capabilities in order for CloudFormation to create the StackSet and related stack
 instances.



* `CAPABILITY_IAM` and `CAPABILITY_NAMED_IAM`



Some stack templates might include resources that can affect permissions in your
 AWS account; for example, by creating new IAM users. For those StackSets, you must
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
	+ [AWS::IAM::Policy](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-policy.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-policy.html")
	+ [AWS::IAM::Role](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-role.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-role.html")
	+ [AWS::IAM::User](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-user.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-user.html")
	+ [AWS::IAM::UserToGroupAddition](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-usertogroupaddition.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-usertogroupaddition.html")
For more information, see [Acknowledging IAM resources in CloudFormation templates](../UserGuide/control-access-with-iam.md#using-iam-capabilities "../UserGuide/control-access-with-iam.md#using-iam-capabilities").
* `CAPABILITY_AUTO_EXPAND`



Some templates reference macros. If your StackSet template references one or more
 macros, you must create the StackSet directly from the processed template, without first
 reviewing the resulting changes in a change set. To create the StackSet directly, you must
 acknowledge this capability. For more information, see [Perform custom processing
 on CloudFormation templates with template macros](../UserGuide/template-macros.md "../UserGuide/template-macros.md").


###### Important

StackSets with service-managed permissions don't currently support the use of macros
 in templates. (This includes the [AWS::Include](../UserGuide/transform-aws-include.md "../UserGuide/transform-aws-include.md") and [AWS::Serverless](../UserGuide/transform-aws-serverless.md "../UserGuide/transform-aws-serverless.md") transforms, which are macros hosted by CloudFormation.) Even if
 you specify this capability for a StackSet with service-managed permissions, if you
 reference a macro in your template the StackSet operation will fail.

Type: Array of strings


Valid Values: `CAPABILITY_IAM | CAPABILITY_NAMED_IAM | CAPABILITY_AUTO_EXPAND`



Required: No




**ClientRequestToken** 


A unique identifier for this `CreateStackSet` request. Specify this token if
 you plan to retry requests so that CloudFormation knows that you're not attempting to create
 another StackSet with the same name. You might retry `CreateStackSet` requests to
 ensure that CloudFormation successfully received them.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.


Pattern: `[a-zA-Z0-9][-a-zA-Z0-9]*`



Required: No




**Description** 


A description of the StackSet. You can use the description to identify the StackSet's
 purpose or other important information.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**ExecutionRoleName** 


The name of the IAM execution role to use to create the StackSet. If you do not specify
 an execution role, CloudFormation uses the `AWSCloudFormationStackSetExecutionRole`
 role for the StackSet operation.


Specify an IAM role only if you are using customized execution roles to control which
 stack resources users and groups can include in their StackSets.


Valid only if the permissions model is `SELF_MANAGED`.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `[a-zA-Z_0-9+=,.@-]+`



Required: No




**ManagedExecution** 


Describes whether CloudFormation performs non-conflicting operations concurrently and queues
 conflicting operations.


Type: [ManagedExecution](API_ManagedExecution.md "API_ManagedExecution.md") object


Required: No




**Parameters.member.N**


The input parameters for the StackSet template.


Type: Array of [Parameter](API_Parameter.md "API_Parameter.md") objects


Required: No




**PermissionModel** 


Describes how the IAM roles required for StackSet operations are created. By default,
 `SELF-MANAGED` is specified.



* With `self-managed` permissions, you must create the administrator and
 execution roles required to deploy to target accounts. For more information, see [Grant
 self-managed permissions](../UserGuide/stacksets-prereqs-self-managed.md "../UserGuide/stacksets-prereqs-self-managed.md").
* With `service-managed` permissions, StackSets automatically creates the
 IAM roles required to deploy to accounts managed by AWS Organizations. For more
 information, see [Activate trusted access for StackSets with AWS Organizations](../UserGuide/stacksets-orgs-activate-trusted-access.md "../UserGuide/stacksets-orgs-activate-trusted-access.md").

Type: String


Valid Values: `SERVICE_MANAGED | SELF_MANAGED`



Required: No




**StackId** 


The stack ID you are importing into a new StackSet. Specify the Amazon Resource Name (ARN)
 of the stack.


Type: String


Required: No




**StackSetName** 


The name to associate with the StackSet. The name must be unique in the Region where you
 create your StackSet.


###### Note

A stack name can contain only alphanumeric characters (case-sensitive) and hyphens. It
 must start with an alphabetic character and can't be longer than 128 characters.


Type: String


Required: Yes




**Tags.member.N**


The key-value pairs to associate with this StackSet and the stacks created from it.
 CloudFormation also propagates these tags to supported resources that are created in the stacks. A
 maximum number of 50 tags can be specified.


If you specify tags as part of a `CreateStackSet` action, CloudFormation checks to
 see if you have the required IAM permission to tag resources. If you don't, the entire
 `CreateStackSet` action fails with an `access denied` error, and the
 StackSet is not created.


Type: Array of [Tag](API_Tag.md "API_Tag.md") objects


Array Members: Maximum number of 50 items.


Required: No




**TemplateBody** 


The structure that contains the template body, with a minimum length of 1 byte and a
 maximum length of 51,200 bytes.


Conditional: You must specify either the `TemplateBody` or the
 `TemplateURL` parameter, but not both.


Type: String


Length Constraints: Minimum length of 1.


Required: No




**TemplateURL** 


The URL of a file that contains the template body. The URL must point to a template
 (maximum size: 1 MB) that's located in an Amazon S3 bucket or a Systems Manager document. The
 location for an Amazon S3 bucket must start with `https://`. S3 static website URLs are
 not supported.


Conditional: You must specify either the `TemplateBody` or the
 `TemplateURL` parameter, but not both.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 5120.


Required: No




## Response Elements


The following element is returned by the service.





**StackSetId** 


The ID of the StackSet that you're creating.


Type: String




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**CreatedButModified** 


The specified resource exists, but has been changed.


HTTP Status Code: 409




**LimitExceeded** 


The quota for the resource has already been reached.


For information about resource and stack limitations, see [AWS CloudFormation quotas](../UserGuide/cloudformation-limits.md "../UserGuide/cloudformation-limits.md") in the
 *AWS CloudFormation User Guide*.


HTTP Status Code: 400




**NameAlreadyExists** 


The specified name is already in use.


HTTP Status Code: 409




## Examples


### CreateStackSet


This example illustrates one usage of CreateStackSet.


#### Sample Request



```

https://cloudformation.us-east-1.amazonaws.com/
 ?Action=CreateStackSet
 &TemplateURL=https://s3.amazonaws.com/cloudformation-stackset-sample-templates-us-east-1/EnableAWSConfig.yml
 &Version=2010-05-15
 &StackSetName=stack-set-example
 &ClientRequestToken=61806005-bde9-46f1-949d-6791example
 &X-Amz-Algorithm=AWS4-HMAC-SHA256
 &X-Amz-Credential=[Access key ID and scope]
 &X-Amz-Date=20170810T233349Z
 &X-Amz-SignedHeaders=content-type;host
 &X-Amz-Signature=[Signature]
```

#### Sample Response



```

<CreateStackSetResponse xmlns="http://internal.amazon.com/coral/com.amazonaws.maestro.service.v20160713/">
  <CreateStackSetResult>
    <StackSetId>stack-set-example:22f04391-472b-4e36-b11a-727example</StackSetId>
  </CreateStackSetResult>
  <ResponseMetadata>
    <RequestId>ad9647cb-7949-11e7-ac43-9938example</RequestId>
  </ResponseMetadata>
</CreateStackSetResponse>
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/CreateStackSet "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/CreateStackSet")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/CreateStackSet "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/CreateStackSet")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/CreateStackSet "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/CreateStackSet")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/CreateStackSet "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/CreateStackSet")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/CreateStackSet "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/CreateStackSet")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/CreateStackSet "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/CreateStackSet")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/CreateStackSet "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/CreateStackSet")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/CreateStackSet "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/CreateStackSet")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/CreateStackSet "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/CreateStackSet")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/CreateStackSet "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/CreateStackSet")
