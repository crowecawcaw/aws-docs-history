# CreateStackInstances

Creates stack instances for the specified accounts, within the specified AWS Regions. A
 stack instance refers to a stack in a specific account and Region. You must specify at least
 one value for either `Accounts` or `DeploymentTargets`, and you must
 specify at least one value for `Regions`.

###### Note

The maximum number of organizational unit (OUs) supported by a
 `CreateStackInstances` operation is 50.

If you need more than 50, consider the following options:


* *Batch processing:* If you don't want to expose your OU
 hierarchy, split up the operations into multiple calls with less than 50 OUs
 each.
* *Parent OU strategy:* If you don't mind exposing the OU
 hierarchy, target a parent OU that contains all desired child OUs.

## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**Accounts.member.N**


[Self-managed permissions] The account IDs of one or more AWS accounts that you want to
 create stack instances in the specified Region(s) for.


You can specify `Accounts` or `DeploymentTargets`, but not
 both.


Type: Array of strings


Pattern: `^[0-9]{12}$`



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




**DeploymentTargets** 


[Service-managed permissions] The AWS Organizations accounts in which to create stack
 instances in the specified AWS Regions.


You can specify `Accounts` or `DeploymentTargets`, but not
 both.


Type: [DeploymentTargets](API_DeploymentTargets.md "API_DeploymentTargets.md") object


Required: No




**OperationId** 


The unique identifier for this StackSet operation.


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




**ParameterOverrides.member.N**


A list of StackSet parameters whose values you want to override in the selected stack
 instances.


Any overridden parameter values will be applied to all stack instances in the specified
 accounts and AWS Regions. When specifying parameters and their values, be aware of how
 CloudFormation sets parameter values during stack instance operations:



* To override the current value for a parameter, include the parameter and specify its
 value.
* To leave an overridden parameter set to its present value, include the parameter and
 specify `UsePreviousValue` as `true`. (You can't specify both a
 value and set `UsePreviousValue` to `true`.)
* To set an overridden parameter back to the value specified in the StackSet, specify a
 parameter list but don't include the parameter in the list.
* To leave all parameters set to their present values, don't specify this property at
 all.

During StackSet updates, any parameter values overridden for a stack instance aren't
 updated, but retain their overridden value.


You can only override the parameter *values* that are specified in the
 StackSet; to add or delete a parameter itself, use [UpdateStackSet](API_UpdateStackSet.md "API_UpdateStackSet.md")
 to update the StackSet template.


Type: Array of [Parameter](API_Parameter.md "API_Parameter.md") objects


Required: No




**Regions.member.N**


The names of one or more AWS Regions where you want to create stack instances using the
 specified AWS accounts.


Type: Array of strings


Pattern: `^[a-zA-Z0-9-]{1,128}$`



Required: Yes




**StackSetName** 


The name or unique ID of the StackSet that you want to create stack instances from.


Type: String


Required: Yes




## Response Elements


The following element is returned by the service.





**OperationId** 


The unique identifier for this StackSet operation.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.


Pattern: `[a-zA-Z0-9][-a-zA-Z0-9]*`





## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**InvalidOperation** 


The specified operation isn't valid.


HTTP Status Code: 400




**LimitExceeded** 


The quota for the resource has already been reached.


For information about resource and stack limitations, see [AWS CloudFormation quotas](../UserGuide/cloudformation-limits.md "../UserGuide/cloudformation-limits.md") in the
 *AWS CloudFormation User Guide*.


HTTP Status Code: 400




**OperationIdAlreadyExists** 


The specified operation ID already exists.


HTTP Status Code: 409




**OperationInProgress** 


Another operation is currently in progress for this StackSet. Only one operation can be performed for a stack
 set at a given time.


HTTP Status Code: 409




**StackSetNotFound** 


The specified StackSet doesn't exist.


HTTP Status Code: 404




**StaleRequest** 


Another operation has been performed on this StackSet since the specified operation was performed.


HTTP Status Code: 409




## Examples


### CreateStackInstances


This example illustrates one usage of CreateStackInstances.


#### Sample Request



```

https://cloudformation.us-east-1.amazonaws.com/
 ?Action=CreateStackInstances
 &Version=2010-05-15
 &StackSetName=stack-set-example
 &Regions.member.1=us-east-1
 &Regions.member.2=us-west-2
 &OperationPreferences.MaxConcurrentCount=5
 &OperationPreferences.FailureTolerancePercentage=10
 &Accounts.member.1=[account]
 &Accounts.member.2=[account]
 &OperationId=c424b651-2fda-4d6f-a4f1-20c0example
 &X-Amz-Algorithm=AWS4-HMAC-SHA256
 &X-Amz-Credential=[Access key ID and scope]
 &X-Amz-Date=20170810T233349Z
 &X-Amz-SignedHeaders=content-type;host
 &X-Amz-Signature=[Signature]
```

#### Sample Response



```

<CreateStackInstancesResponse xmlns="http://internal.amazon.com/coral/com.amazonaws.maestro.service.v20160713/">
  <CreateStackInstancesResult>
    <OperationId>c424b651-2fda-4d6f-a4f1-20c0fc62a6fe</OperationId>
  </CreateStackInstancesResult>
  <ResponseMetadata>
    <RequestId>97564c5e-813e-11e7-a9b2-5b163763e702</RequestId>
  </ResponseMetadata>
</CreateStackInstancesResponse>
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/CreateStackInstances "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/CreateStackInstances")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/CreateStackInstances "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/CreateStackInstances")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/CreateStackInstances "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/CreateStackInstances")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/CreateStackInstances "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/CreateStackInstances")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/CreateStackInstances "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/CreateStackInstances")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/CreateStackInstances "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/CreateStackInstances")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/CreateStackInstances "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/CreateStackInstances")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/CreateStackInstances "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/CreateStackInstances")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/CreateStackInstances "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/CreateStackInstances")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/CreateStackInstances "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/CreateStackInstances")
