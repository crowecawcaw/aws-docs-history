# PutResourcePolicy

Creates or updates an AWS CloudHSM resource policy. A resource policy helps you to define the IAM entity 
 (for example, an AWS account) that can manage your AWS CloudHSM resources. The following resources support 
 AWS CloudHSM resource policies: 


* Backup - The resource policy allows you to describe the backup and restore a cluster from the backup in another AWS account.
In order to share a backup, it must be in a 'READY' state and you must own it.

###### Important

While you can share a backup using the AWS CloudHSM PutResourcePolicy operation, we recommend using AWS Resource Access Manager
 (AWS RAM) instead. Using AWS RAM provides multiple benefits as it creates the policy for you, allows multiple resources to be shared at
 one time, and increases the discoverability of shared resources. If you use PutResourcePolicy and want consumers to be able to
 describe the backups you share with them, you must promote the backup to a standard AWS RAM
 Resource Share using the AWS RAM PromoteResourceShareCreatedFromPolicy API operation.

 For more information, see  [Working with shared backups](../userguide/sharing.md "../userguide/sharing.md") in the AWS CloudHSM User Guide


**Cross-account use:** No. You cannot perform this operation on an AWS CloudHSM resource in a different AWS account.


## Request Syntax



```
{
   "Policy": "`string`",
   "ResourceArn": "`string`"
}
```

## Request Parameters


For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").


The request accepts the following data in JSON format.





**[Policy](#API_PutResourcePolicy_RequestSyntax "#API_PutResourcePolicy_RequestSyntax")**


The policy you want to associate with a resource. 


For an example policy, see  [Working with shared backups](../userguide/sharing.md "../userguide/sharing.md") in the AWS CloudHSM User Guide


Type: String


Length Constraints: Minimum length of 1. Maximum length of 20000.


Required: No




**[ResourceArn](#API_PutResourcePolicy_RequestSyntax "#API_PutResourcePolicy_RequestSyntax")**


Amazon Resource Name (ARN) of the resource to which you want to attach a policy. 


Type: String


Pattern: `arn:aws(-(us-gov))?:cloudhsm:([a-z]{2}(-(gov|isob|iso))?-(east|west|north|south|central){1,2}-[0-9]{1}):[0-9]{12}:(backup/backup|cluster/cluster|hsm/hsm)-[2-7a-zA-Z]{11,16}`



Required: No




## Response Syntax



```
{
   "Policy": "***string***",
   "ResourceArn": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[Policy](#API_PutResourcePolicy_ResponseSyntax "#API_PutResourcePolicy_ResponseSyntax")**


The policy attached to a resource.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 20000.




**[ResourceArn](#API_PutResourcePolicy_ResponseSyntax "#API_PutResourcePolicy_ResponseSyntax")**


Amazon Resource Name (ARN) of the resource to which a policy is attached.


Type: String


Pattern: `arn:aws(-(us-gov))?:cloudhsm:([a-z]{2}(-(gov|isob|iso))?-(east|west|north|south|central){1,2}-[0-9]{1}):[0-9]{12}:(backup/backup|cluster/cluster|hsm/hsm)-[2-7a-zA-Z]{11,16}`





## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**CloudHsmAccessDeniedException** 


The request was rejected because the requester does not have permission to perform the
 requested operation.


HTTP Status Code: 400




**CloudHsmInternalFailureException** 


The request was rejected because of an AWS CloudHSM internal failure. The request can
 be retried.


HTTP Status Code: 500




**CloudHsmInvalidRequestException** 


The request was rejected because it is not a valid request.


HTTP Status Code: 400




**CloudHsmResourceNotFoundException** 


The request was rejected because it refers to a resource that cannot be
 found.


HTTP Status Code: 400




**CloudHsmServiceException** 


The request was rejected because an error occurred.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudhsmv2-2017-04-28/PutResourcePolicy "https://docs.aws.amazon.com/goto/cli2/cloudhsmv2-2017-04-28/PutResourcePolicy")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudhsmv2-2017-04-28/PutResourcePolicy "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudhsmv2-2017-04-28/PutResourcePolicy")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudhsmv2-2017-04-28/PutResourcePolicy "https://docs.aws.amazon.com/goto/SdkForCpp/cloudhsmv2-2017-04-28/PutResourcePolicy")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudhsmv2-2017-04-28/PutResourcePolicy "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudhsmv2-2017-04-28/PutResourcePolicy")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudhsmv2-2017-04-28/PutResourcePolicy "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudhsmv2-2017-04-28/PutResourcePolicy")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudhsmv2-2017-04-28/PutResourcePolicy "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudhsmv2-2017-04-28/PutResourcePolicy")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudhsmv2-2017-04-28/PutResourcePolicy "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudhsmv2-2017-04-28/PutResourcePolicy")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudhsmv2-2017-04-28/PutResourcePolicy "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudhsmv2-2017-04-28/PutResourcePolicy")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudhsmv2-2017-04-28/PutResourcePolicy "https://docs.aws.amazon.com/goto/boto3/cloudhsmv2-2017-04-28/PutResourcePolicy")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudhsmv2-2017-04-28/PutResourcePolicy "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudhsmv2-2017-04-28/PutResourcePolicy")
