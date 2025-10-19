# UpdateStackSet

Updates the StackSet and associated stack instances in the specified accounts and
 AWS Regions.

Even if the StackSet operation created by updating the StackSet fails (completely or
 partially, below or above a specified failure tolerance), the StackSet is updated with your
 changes. Subsequent [CreateStackInstances](API_CreateStackInstances.md "API_CreateStackInstances.md") calls on the specified StackSet use
 the updated StackSet.

###### Note

The maximum number of organizational unit (OUs) supported by a
 `UpdateStackSet` operation is 50.

If you need more than 50, consider the following options:


* *Batch processing:* If you don't want to expose your OU
 hierarchy, split up the operations into multiple calls with less than 50 OUs
 each.
* *Parent OU strategy:* If you don't mind exposing the OU
 hierarchy, target a parent OU that contains all desired child OUs.

## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**Accounts.member.N**


[Self-managed permissions] The accounts in which to update associated stack instances. If
 you specify accounts, you must also specify the AWS Regions in which to update StackSet
 instances.


To update *all* the stack instances associated with this StackSet,
 don't specify the `Accounts` or `Regions` properties.


If the StackSet update includes changes to the template (that is, if the
 `TemplateBody` or `TemplateURL` properties are specified), or the
 `Parameters` property, CloudFormation marks all stack instances with a status of
 `OUTDATED` prior to updating the stack instances in the specified accounts and
 AWS Regions. If the StackSet update does not include changes to the template or parameters,
 CloudFormation updates the stack instances in the specified accounts and AWS Regions, while
 leaving all other stack instances with their existing stack instance status.


Type: Array of strings


Pattern: `^[0-9]{12}$`



Required: No




**AdministrationRoleARN** 


[Self-managed permissions] The Amazon Resource Name (ARN) of the IAM role to use to
 update this StackSet.


Specify an IAM role only if you are using customized administrator roles to control
 which users or groups can manage specific StackSets within the same administrator account. For
 more information, see [Grant
 self-managed permissions](../UserGuide/stacksets-prereqs-self-managed.md "../UserGuide/stacksets-prereqs-self-managed.md") in the *AWS CloudFormation User Guide*.


If you specified a customized administrator role when you created the StackSet, you must
 specify a customized administrator role, even if it is the same customized administrator role
 used with this StackSet previously.


Type: String


Length Constraints: Minimum length of 20. Maximum length of 2048.


Required: No




**AutoDeployment** 


[Service-managed permissions] Describes whether StackSets automatically deploys to AWS Organizations accounts that are added to a target organization or organizational unit (OU).
 For more information, see [Enable or disable automatic deployments for StackSets in AWS Organizations](../UserGuide/stacksets-orgs-manage-auto-deployment.md "../UserGuide/stacksets-orgs-manage-auto-deployment.md")
 in the *AWS CloudFormation User Guide*.


If you specify `AutoDeployment`, don't specify `DeploymentTargets`
 or `Regions`.


Type: [AutoDeployment](API_AutoDeployment.md "API_AutoDeployment.md") object


Required: No




**CallAs** 


[Service-managed permissions] Specifies whether you are acting as an account administrator
 in the organization's management account or as a delegated administrator in a
 member account.


By default, `SELF` is specified. Use `SELF` for StackSets with
 self-managed permissions.



* If you are signed in to the management account, specify
 `SELF`.
* If you are signed in to a delegated administrator account, specify
 `DELEGATED_ADMIN`.


Your AWS account must be registered as a delegated administrator in the management account. For more information, see [Register a
 delegated administrator](../UserGuide/stacksets-orgs-delegated-admin.md "../UserGuide/stacksets-orgs-delegated-admin.md") in the *AWS CloudFormation User Guide*.

Type: String


Valid Values: `SELF | DELEGATED_ADMIN`



Required: No




**Capabilities.member.N**


In some cases, you must explicitly acknowledge that your stack template contains certain
 capabilities in order for CloudFormation to update the StackSet and its associated stack
 instances.



* `CAPABILITY_IAM` and `CAPABILITY_NAMED_IAM`



Some stack templates might include resources that can affect permissions in your
 AWS account, for example, by creating new IAM users. For those stacks sets, you must
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
 macros, you must update the StackSet directly from the processed template, without first
 reviewing the resulting changes in a change set. To update the StackSet directly, you must
 acknowledge this capability. For more information, see [Perform custom processing
 on CloudFormation templates with template macros](../UserGuide/template-macros.md "../UserGuide/template-macros.md").


###### Important

StackSets with service-managed permissions do not currently support the use of
 macros in templates. (This includes the [AWS::Include](../UserGuide/transform-aws-include.md "../UserGuide/transform-aws-include.md") and [AWS::Serverless](../UserGuide/transform-aws-serverless.md "../UserGuide/transform-aws-serverless.md") transforms, which are macros hosted by CloudFormation.) Even if
 you specify this capability for a StackSet with service-managed permissions, if you
 reference a macro in your template the StackSet operation will fail.

Type: Array of strings


Valid Values: `CAPABILITY_IAM | CAPABILITY_NAMED_IAM | CAPABILITY_AUTO_EXPAND`



Required: No




**DeploymentTargets** 


[Service-managed permissions] The AWS Organizations accounts in which to update
 associated stack instances.


To update all the stack instances associated with this StackSet, do not specify
 `DeploymentTargets` or `Regions`.


If the StackSet update includes changes to the template (that is, if
 `TemplateBody` or `TemplateURL` is specified), or the
 `Parameters`, CloudFormation marks all stack instances with a status of
 `OUTDATED` prior to updating the stack instances in the specified accounts and
 AWS Regions. If the StackSet update doesn't include changes to the template or parameters,
 CloudFormation updates the stack instances in the specified accounts and Regions, while leaving
 all other stack instances with their existing stack instance status.


Type: [DeploymentTargets](API_DeploymentTargets.md "API_DeploymentTargets.md") object


Required: No




**Description** 


A brief description of updates that you are making.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**ExecutionRoleName** 


[Self-managed permissions] The name of the IAM execution role to use to update the stack
 set. If you do not specify an execution role, CloudFormation uses the
 `AWSCloudFormationStackSetExecutionRole` role for the StackSet operation.


Specify an IAM role only if you are using customized execution roles to control which
 stack resources users and groups can include in their StackSets.


If you specify a customized execution role, CloudFormation uses that role to update the stack.
 If you do not specify a customized execution role, CloudFormation performs the update using the
 role previously associated with the StackSet, so long as you have permissions to perform
 operations on the StackSet.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `[a-zA-Z_0-9+=,.@-]+`



Required: No




**ManagedExecution** 


Describes whether CloudFormation performs non-conflicting operations concurrently and queues
 conflicting operations.


Type: [ManagedExecution](API_ManagedExecution.md "API_ManagedExecution.md") object


Required: No




**OperationId** 


The unique ID for this StackSet operation.


The operation ID also functions as an idempotency token, to ensure that CloudFormation
 performs the StackSet operation only once, even if you retry the request multiple times. You
 might retry StackSet operation requests to ensure that CloudFormation successfully received
 them.


Repeating this StackSet operation with a new operation ID retries all stack instances
 whose status is `OUTDATED`.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.


Pattern: `[a-zA-Z0-9][-a-zA-Z0-9]*`



Required: No




**OperationPreferences** 


Preferences for how CloudFormation performs this StackSet operation.


Type: [StackSetOperationPreferences](API_StackSetOperationPreferences.md "API_StackSetOperationPreferences.md") object


Required: No




**Parameters.member.N**


A list of input parameters for the StackSet template.


Type: Array of [Parameter](API_Parameter.md "API_Parameter.md") objects


Required: No




**PermissionModel** 


Describes how the IAM roles required for StackSet operations are created. You cannot
 modify `PermissionModel` if there are stack instances associated with your stack
 set.



* With `self-managed` permissions, you must create the administrator and
 execution roles required to deploy to target accounts. For more information, see [Grant
 self-managed permissions](../UserGuide/stacksets-prereqs-self-managed.md "../UserGuide/stacksets-prereqs-self-managed.md").
* With `service-managed` permissions, StackSets automatically creates the
 IAM roles required to deploy to accounts managed by AWS Organizations. For more
 information, see [Activate trusted access for StackSets with AWS Organizations](../UserGuide/stacksets-orgs-activate-trusted-access.md "../UserGuide/stacksets-orgs-activate-trusted-access.md").

Type: String


Valid Values: `SERVICE_MANAGED | SELF_MANAGED`



Required: No




**Regions.member.N**


The AWS Regions in which to update associated stack instances. If you specify Regions,
 you must also specify accounts in which to update StackSet instances.


To update *all* the stack instances associated with this StackSet, do
 not specify the `Accounts` or `Regions` properties.


If the StackSet update includes changes to the template (that is, if the
 `TemplateBody` or `TemplateURL` properties are specified), or the
 `Parameters` property, CloudFormation marks all stack instances with a status of
 `OUTDATED` prior to updating the stack instances in the specified accounts and
 Regions. If the StackSet update does not include changes to the template or parameters,
 CloudFormation updates the stack instances in the specified accounts and Regions, while leaving
 all other stack instances with their existing stack instance status.


Type: Array of strings


Pattern: `^[a-zA-Z0-9-]{1,128}$`



Required: No




**StackSetName** 


The name or unique ID of the StackSet that you want to update.


Type: String


Required: Yes




**Tags.member.N**


The key-value pairs to associate with this StackSet and the stacks created from it.
 CloudFormation also propagates these tags to supported resources that are created in the stacks.
 You can specify a maximum number of 50 tags.


If you specify tags for this parameter, those tags replace any list of tags that are
 currently associated with this StackSet. This means:



* If you don't specify this parameter, CloudFormation doesn't modify the stack's
 tags.
* If you specify *any* tags using this parameter, you must specify
 *all* the tags that you want associated with this StackSet, even tags
 you've specified before (for example, when creating the StackSet or during a previous
 update of the StackSet.). Any tags that you don't include in the updated list of tags are
 removed from the StackSet, and therefore from the stacks and resources as well.
* If you specify an empty value, CloudFormation removes all currently associated
 tags.

If you specify new tags as part of an `UpdateStackSet` action, CloudFormation
 checks to see if you have the required IAM permission to tag resources. If you omit tags
 that are currently associated with the StackSet from the list of tags you specify, CloudFormation
 assumes that you want to remove those tags from the StackSet, and checks to see if you have
 permission to untag resources. If you don't have the necessary permission(s), the entire
 `UpdateStackSet` action fails with an `access denied` error, and the
 StackSet is not updated.


Type: Array of [Tag](API_Tag.md "API_Tag.md") objects


Array Members: Maximum number of 50 items.


Required: No




**TemplateBody** 


The structure that contains the template body, with a minimum length of 1 byte and a
 maximum length of 51,200 bytes.


Conditional: You must specify only one of the following parameters:
 `TemplateBody` or `TemplateURL`—or set
 `UsePreviousTemplate` to true.


Type: String


Length Constraints: Minimum length of 1.


Required: No




**TemplateURL** 


The URL of a file that contains the template body. The URL must point to a template
 (maximum size: 1 MB) that is located in an Amazon S3 bucket or a Systems Manager document. The
 location for an Amazon S3 bucket must start with `https://`. S3 static website URLs are
 not supported.


Conditional: You must specify only one of the following parameters:
 `TemplateBody` or `TemplateURL`—or set
 `UsePreviousTemplate` to true.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 5120.


Required: No




**UsePreviousTemplate** 


Use the existing template that's associated with the StackSet that you're updating.


Conditional: You must specify only one of the following parameters:
 `TemplateBody` or `TemplateURL`—or set
 `UsePreviousTemplate` to true.


Type: Boolean


Required: No




## Response Elements


The following element is returned by the service.





**OperationId** 


The unique ID for this StackSet operation.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.


Pattern: `[a-zA-Z0-9][-a-zA-Z0-9]*`





## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**InvalidOperation** 


The specified operation isn't valid.


HTTP Status Code: 400




**OperationIdAlreadyExists** 


The specified operation ID already exists.


HTTP Status Code: 409




**OperationInProgress** 


Another operation is currently in progress for this StackSet. Only one operation can be performed for a stack
 set at a given time.


HTTP Status Code: 409




**StackInstanceNotFound** 


The specified stack instance doesn't exist.


HTTP Status Code: 404




**StackSetNotFound** 


The specified StackSet doesn't exist.


HTTP Status Code: 404




**StaleRequest** 


Another operation has been performed on this StackSet since the specified operation was performed.


HTTP Status Code: 409




## Examples


### UpdateStackSet


This example illustrates one usage of UpdateStackSet.


#### Sample Request



```

https://cloudformation.us-east-1.amazonaws.com/
 ?Action=UpdateStackSet
 &Version=2010-05-15
 &StackSetName=stack-set-example
 &OperationPreferences.MaxConcurrentCount=2
 &OperationPreferences.FailureToleranceCount=1
 &UsePreviousTemplate=true
 &Tags.member.1.Key=new_key
 &Tags.member.1.Value=new_value
 &OperationId=bb1764f4-3dea-4c39-bd65-066aexample
 &X-Amz-Algorithm=AWS4-HMAC-SHA256
 &X-Amz-Credential=[Access key ID and scope]
 &X-Amz-Date=20170810T233349Z
 &X-Amz-SignedHeaders=content-type;host
 &X-Amz-Signature=[Signature]
```

#### Sample Response



```

<UpdateStackSetResponse xmlns="http://internal.amazon.com/coral/com.amazonaws.maestro.service.v20160713/">
  <UpdateStackSetResult>
    <OperationId>bb1764f4-3dea-4c39-bd65-066aexamplef</OperationId>
  </UpdateStackSetResult>
  <ResponseMetadata>
    <RequestId>32d4839e-7e24-11e7-b656-d39aexample</RequestId>
  </ResponseMetadata>
</UpdateStackSetResponse>
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/UpdateStackSet "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/UpdateStackSet")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/UpdateStackSet "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/UpdateStackSet")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/UpdateStackSet "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/UpdateStackSet")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/UpdateStackSet "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/UpdateStackSet")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/UpdateStackSet "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/UpdateStackSet")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/UpdateStackSet "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/UpdateStackSet")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/UpdateStackSet "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/UpdateStackSet")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/UpdateStackSet "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/UpdateStackSet")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/UpdateStackSet "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/UpdateStackSet")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/UpdateStackSet "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/UpdateStackSet")
