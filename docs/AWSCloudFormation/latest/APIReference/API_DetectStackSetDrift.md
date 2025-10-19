# DetectStackSetDrift

Detect drift on a StackSet. When CloudFormation performs drift detection on a StackSet, it
 performs drift detection on the stack associated with each stack instance in the StackSet. For
 more information, see [Performing drift detection on
 CloudFormation StackSets](../UserGuide/stacksets-drift.md "../UserGuide/stacksets-drift.md").


`DetectStackSetDrift` returns the `OperationId` of the StackSet
 drift detection operation. Use this operation id with [DescribeStackSetOperation](API_DescribeStackSetOperation.md "API_DescribeStackSetOperation.md") to monitor the progress of the drift detection
 operation. The drift detection operation may take some time, depending on the number of stack
 instances included in the StackSet, in addition to the number of resources included in each
 stack.

Once the operation has completed, use the following actions to return drift
 information:


* Use [DescribeStackSet](API_DescribeStackSet.md "API_DescribeStackSet.md") to return detailed information about the stack
 set, including detailed information about the last *completed* drift
 operation performed on the StackSet. (Information about drift operations that are in
 progress isn't included.)
* Use [ListStackInstances](API_ListStackInstances.md "API_ListStackInstances.md") to return a list of stack instances belonging
 to the StackSet, including the drift status and last drift time checked of each
 instance.
* Use [DescribeStackInstance](API_DescribeStackInstance.md "API_DescribeStackInstance.md") to return detailed information about a
 specific stack instance, including its drift status and last drift time checked.
You can only run a single drift detection operation on a given StackSet at one
 time.

To stop a drift detection StackSet operation, use [StopStackSetOperation](API_StopStackSetOperation.md "API_StopStackSetOperation.md").


## Request Parameters


 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").





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




**OperationId** 



*The ID of the StackSet operation.*



Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.


Pattern: `[a-zA-Z0-9][-a-zA-Z0-9]*`



Required: No




**OperationPreferences** 


The user-specified preferences for how CloudFormation performs a StackSet operation.


For more information about maximum concurrent accounts and failure tolerance, see [StackSet operation options](../UserGuide/stacksets-concepts.md#stackset-ops-options "../UserGuide/stacksets-concepts.md#stackset-ops-options").


Type: [StackSetOperationPreferences](API_StackSetOperationPreferences.md "API_StackSetOperationPreferences.md") object


Required: No




**StackSetName** 


The name of the StackSet on which to perform the drift detection operation.


Type: String


Pattern: `[a-zA-Z][-a-zA-Z0-9]*(?::[a-zA-Z0-9]{8}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{12})?`



Required: Yes




## Response Elements


The following element is returned by the service.





**OperationId** 


The ID of the drift detection StackSet operation.


You can use this operation ID with [DescribeStackSetOperation](API_DescribeStackSetOperation.md "API_DescribeStackSetOperation.md") to monitor
 the progress of the drift detection operation.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.


Pattern: `[a-zA-Z0-9][-a-zA-Z0-9]*`





## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**InvalidOperation** 


The specified operation isn't valid.


HTTP Status Code: 400




**OperationInProgress** 


Another operation is currently in progress for this StackSet. Only one operation can be performed for a stack
 set at a given time.


HTTP Status Code: 409




**StackSetNotFound** 


The specified StackSet doesn't exist.


HTTP Status Code: 404




## Examples


### DetectStackSetDrift


This example illustrates one usage of DetectStackSetDrift.


#### Sample Request



```
https://cloudformation.us-east-1.amazonaws.com/
 ?Action=DetectStackSetDrift
 &Version=2010-05-15
 &StackSetName=stack-set-example
 &OperationId=9cc082fa-df4c-45cd-b9a8-7e56example
 &X-Amz-Algorithm=AWS4-HMAC-SHA256
 &X-Amz-Credential=[Access key ID and scope]
 &X-Amz-Date=20191203T195756Z
 &X-Amz-SignedHeaders=content-type;host
 &X-Amz-Signature=[Signature]
```

#### Sample Response



```

<DetectStackSetDriftResponse xmlns="http://internal.amazon.com/coral/com.amazonaws.maestro.service.v20160713/">
  <DetectStackSetDriftResult>
    <OperationId>9cc082fa-df4c-45cd-b9a8-7e56example</OperationId>
  </DetectStackSetDriftResult>
  <ResponseMetadata>
    <RequestId>38309f0a-d5f5-4330-b6ca-8eb1example</RequestId>
  </ResponseMetadata>
</DetectStackSetDriftResponse>
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DetectStackSetDrift "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DetectStackSetDrift")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/DetectStackSetDrift "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/DetectStackSetDrift")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DetectStackSetDrift "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DetectStackSetDrift")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DetectStackSetDrift "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DetectStackSetDrift")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DetectStackSetDrift "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DetectStackSetDrift")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DetectStackSetDrift "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DetectStackSetDrift")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DetectStackSetDrift "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DetectStackSetDrift")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DetectStackSetDrift "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DetectStackSetDrift")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DetectStackSetDrift "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DetectStackSetDrift")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DetectStackSetDrift "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DetectStackSetDrift")
