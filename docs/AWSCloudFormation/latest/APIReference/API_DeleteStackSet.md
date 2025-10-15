# DeleteStackSet

Deletes a StackSet. Before you can delete a StackSet, all its member stack instances must
 be deleted. For more information about how to complete this, see [DeleteStackInstances](API_DeleteStackInstances.md "API_DeleteStackInstances.md").


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




**StackSetName** 


The name or unique ID of the StackSet that you're deleting. You can obtain this value by
 running [ListStackSets](API_ListStackSets.md "API_ListStackSets.md").


Type: String


Required: Yes




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**OperationInProgress** 


Another operation is currently in progress for this StackSet. Only one operation can be performed for a stack
 set at a given time.


HTTP Status Code: 409




**StackSetNotEmpty** 


You can't yet delete this StackSet, because it still contains one or more stack instances. Delete all stack
 instances from the StackSet before deleting the StackSet.


HTTP Status Code: 409




## Examples


### DeleteStackSet


This example illustrates one usage of DeleteStackSet.


#### Sample Request



```

https://cloudformation.us-east-1.amazonaws.com/
 ?Action=DeleteStackSet
 &Version=2010-05-15
 &StackSetName=stack-set-example
 &X-Amz-Algorithm=AWS4-HMAC-SHA256
 &X-Amz-Credential=[Access key ID and scope]
 &X-Amz-Date=20170810T233349Z
 &X-Amz-SignedHeaders=content-type;host
 &X-Amz-Signature=[Signature]
```

#### Sample Response



```

<DeleteStackSetResponse xmlns="http://internal.amazon.com/coral/com.amazonaws.maestro.service.v20160713/">
  <DeleteStackSetResult/>
  <ResponseMetadata>
    <RequestId>792b1f2b-7946-11e7-a7db-afc00fexample</RequestId>
  </ResponseMetadata>
</DeleteStackSetResponse>
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DeleteStackSet "https://docs.aws.amazon.com/goto/cli2/cloudformation-2010-05-15/DeleteStackSet")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/DeleteStackSet "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudformation-2010-05-15/DeleteStackSet")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DeleteStackSet "https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DeleteStackSet")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DeleteStackSet "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudformation-2010-05-15/DeleteStackSet")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DeleteStackSet "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DeleteStackSet")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DeleteStackSet "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudformation-2010-05-15/DeleteStackSet")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DeleteStackSet "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudformation-2010-05-15/DeleteStackSet")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DeleteStackSet "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudformation-2010-05-15/DeleteStackSet")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DeleteStackSet "https://docs.aws.amazon.com/goto/boto3/cloudformation-2010-05-15/DeleteStackSet")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DeleteStackSet "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DeleteStackSet")
