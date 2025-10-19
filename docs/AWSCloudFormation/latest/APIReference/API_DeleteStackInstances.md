# DeleteStackInstances

Deletes stack instances for the specified accounts, in the specified AWS Regions.

###### Note

The maximum number of organizational unit (OUs) supported by a
 `DeleteStackInstances` operation is 50.

If you need more than 50, consider the following options:


* *Batch processing:* If you don't want to expose your OU
 hierarchy, split up the operations into multiple calls with less than 50 OUs
 each.
* *Parent OU strategy:* If you don't mind exposing the OU
 hierarchy, target a parent OU that contains all desired child OUs.

## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





**Accounts.member.N**


[Self-managed permissions] The account IDs of the AWS accounts that you want to delete
 stack instances for.


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


[Service-managed permissions] The AWS Organizations accounts from which to delete
 stack instances.


You can specify `Accounts` or `DeploymentTargets`, but not
 both.


Type: [DeploymentTargets](API_DeploymentTargets.md "API_DeploymentTargets.md") object


Required: No




**OperationId** 


The unique identifier for this StackSet operation.


The operation ID also functions as an idempotency token, to ensure that CloudFormation
 performs the StackSet operation only once, even if you retry the request multiple times. You
 can retry StackSet operation requests to ensure that CloudFormation successfully received
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




**Regions.member.N**


The AWS Regions where you want to delete StackSet instances.


Type: Array of strings


Pattern: `^[a-zA-Z0-9-]{1,128}$`



Required: Yes




**RetainStacks** 


Removes the stack instances from the specified StackSet, but doesn't delete the stacks.
 You can't reassociate a retained stack or add an existing, saved stack to a new stack
 set.


For more information, see [StackSet operation options](../UserGuide/stacksets-concepts.md#stackset-ops-options "../UserGuide/stacksets-concepts.md#stackset-ops-options").


Type: Boolean


Required: Yes




**StackSetName** 


The name or unique ID of the StackSet that you want to delete stack instances for.


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


### DeleteStackInstances


This example illustrates one usage of DeleteStackInstances.


#### Sample Request



```

https://cloudformation.us-east-1.amazonaws.com/
 ?Action=DeleteStackInstances
 &Regions.member.1=us-east-1
 &Regions.member.2=us-west-1
 &Version=2010-05-15
 &StackSetName=stack-set-example
 &RetainStacks=false
 &OperationPreferences.MaxConcurrentCount=2
 &OperationPreferences.FailureToleranceCount=1
 &Accounts.member.1=[account]
 &Accounts.member.2=[account]
 &OperationId=a0f49354-a1eb-42b7-9e5d-c0897example
 &X-Amz-Algorithm=AWS4-HMAC-SHA256
 &X-Amz-Credential=[Access key ID and scope]
 &X-Amz-Date=20170810T233349Z
 &X-Amz-SignedHeaders=content-type;host
 &X-Amz-Signature=[Signature]
```

#### Sample Response



```

<DeleteStackInstancesResponse xmlns="http://internal.amazon.com/coral/com.amazonaws.maestro.service.v20160713/">
  <DeleteStackInstancesResult>
    <OperationId>a0f49354-a1eb-42b7-9e5d-c08977e317a0</OperationId>
  </DeleteStackInstancesResult>
  <ResponseMetadata>
    <RequestId>0f3c3dcc-7945-11e7-a4ac-9503729bf9ee</RequestId>
  </ResponseMetadata>
</DeleteStackInstancesResponse>
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DeleteStackInstances "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DeleteStackInstances")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/DeleteStackInstances "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/DeleteStackInstances")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DeleteStackInstances "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DeleteStackInstances")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DeleteStackInstances "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DeleteStackInstances")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DeleteStackInstances "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DeleteStackInstances")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DeleteStackInstances "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DeleteStackInstances")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DeleteStackInstances "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DeleteStackInstances")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DeleteStackInstances "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DeleteStackInstances")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DeleteStackInstances "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DeleteStackInstances")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DeleteStackInstances "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DeleteStackInstances")
