# GetResourcePolicy

 Retrieves the resource policy document attached to a given resource. 


**Cross-account use:** No. You cannot perform this operation on an AWS CloudHSM resource in a different AWS account.


## Request Syntax



```
{
   "ResourceArn": "`string`"
}
```

## Request Parameters


For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").


The request accepts the following data in JSON format.





**[ResourceArn](#API_GetResourcePolicy_RequestSyntax "#API_GetResourcePolicy_RequestSyntax")**


Amazon Resource Name (ARN) of the resource to which a policy is attached.


Type: String


Pattern: `arn:aws(-(us-gov))?:cloudhsm:([a-z]{2}(-(gov|isob|iso))?-(east|west|north|south|central){1,2}-[0-9]{1}):[0-9]{12}:(backup/backup|cluster/cluster|hsm/hsm)-[2-7a-zA-Z]{11,16}`



Required: No




## Response Syntax



```
{
   "Policy": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[Policy](#API_GetResourcePolicy_ResponseSyntax "#API_GetResourcePolicy_ResponseSyntax")**


The policy attached to a resource.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 20000.




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



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudhsmv2-2017-04-28/GetResourcePolicy "https://docs.aws.amazon.com/goto/cli2/cloudhsmv2-2017-04-28/GetResourcePolicy")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudhsmv2-2017-04-28/GetResourcePolicy "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudhsmv2-2017-04-28/GetResourcePolicy")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudhsmv2-2017-04-28/GetResourcePolicy "https://docs.aws.amazon.com/goto/SdkForCpp/cloudhsmv2-2017-04-28/GetResourcePolicy")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudhsmv2-2017-04-28/GetResourcePolicy "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudhsmv2-2017-04-28/GetResourcePolicy")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudhsmv2-2017-04-28/GetResourcePolicy "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudhsmv2-2017-04-28/GetResourcePolicy")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudhsmv2-2017-04-28/GetResourcePolicy "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudhsmv2-2017-04-28/GetResourcePolicy")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudhsmv2-2017-04-28/GetResourcePolicy "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudhsmv2-2017-04-28/GetResourcePolicy")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudhsmv2-2017-04-28/GetResourcePolicy "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudhsmv2-2017-04-28/GetResourcePolicy")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudhsmv2-2017-04-28/GetResourcePolicy "https://docs.aws.amazon.com/goto/boto3/cloudhsmv2-2017-04-28/GetResourcePolicy")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudhsmv2-2017-04-28/GetResourcePolicy "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudhsmv2-2017-04-28/GetResourcePolicy")
