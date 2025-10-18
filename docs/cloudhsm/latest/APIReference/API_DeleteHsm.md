# DeleteHsm

Deletes the specified HSM. To specify an HSM, you can use its identifier (ID), the IP
 address of the HSM's elastic network interface (ENI), or the ID of the HSM's ENI. You need to
 specify only one of these values. To find these values, use [DescribeClusters](API_DescribeClusters.md "API_DescribeClusters.md").


**Cross-account use:** No. You cannot perform this operation on an AWS CloudHSM hsm in a different AWS account.


## Request Syntax



```
{
   "ClusterId": "`string`",
   "EniId": "`string`",
   "EniIp": "`string`",
   "HsmId": "`string`"
}
```

## Request Parameters


For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").


The request accepts the following data in JSON format.





**[ClusterId](#API_DeleteHsm_RequestSyntax "#API_DeleteHsm_RequestSyntax")**


The identifier (ID) of the cluster that contains the HSM that you are
 deleting.


Type: String


Pattern: `cluster-[2-7a-zA-Z]{11,16}`



Required: Yes




**[EniId](#API_DeleteHsm_RequestSyntax "#API_DeleteHsm_RequestSyntax")**


The identifier (ID) of the elastic network interface (ENI) of the HSM that you are
 deleting.


Type: String


Pattern: `eni-[0-9a-fA-F]{8,17}`



Required: No




**[EniIp](#API_DeleteHsm_RequestSyntax "#API_DeleteHsm_RequestSyntax")**


The IP address of the elastic network interface (ENI) of the HSM that you are
 deleting.


Type: String


Pattern: `\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}`



Required: No




**[HsmId](#API_DeleteHsm_RequestSyntax "#API_DeleteHsm_RequestSyntax")**


The identifier (ID) of the HSM that you are deleting.


Type: String


Pattern: `hsm-[2-7a-zA-Z]{11,16}`



Required: No




## Response Syntax



```
{
   "HsmId": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[HsmId](#API_DeleteHsm_ResponseSyntax "#API_DeleteHsm_ResponseSyntax")**


The identifier (ID) of the HSM that was deleted.


Type: String


Pattern: `hsm-[2-7a-zA-Z]{11,16}`





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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudhsmv2-2017-04-28/DeleteHsm "https://docs.aws.amazon.com/goto/cli2/cloudhsmv2-2017-04-28/DeleteHsm")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudhsmv2-2017-04-28/DeleteHsm "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudhsmv2-2017-04-28/DeleteHsm")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudhsmv2-2017-04-28/DeleteHsm "https://docs.aws.amazon.com/goto/SdkForCpp/cloudhsmv2-2017-04-28/DeleteHsm")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudhsmv2-2017-04-28/DeleteHsm "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudhsmv2-2017-04-28/DeleteHsm")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudhsmv2-2017-04-28/DeleteHsm "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudhsmv2-2017-04-28/DeleteHsm")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudhsmv2-2017-04-28/DeleteHsm "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudhsmv2-2017-04-28/DeleteHsm")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudhsmv2-2017-04-28/DeleteHsm "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudhsmv2-2017-04-28/DeleteHsm")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudhsmv2-2017-04-28/DeleteHsm "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudhsmv2-2017-04-28/DeleteHsm")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudhsmv2-2017-04-28/DeleteHsm "https://docs.aws.amazon.com/goto/boto3/cloudhsmv2-2017-04-28/DeleteHsm")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudhsmv2-2017-04-28/DeleteHsm "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudhsmv2-2017-04-28/DeleteHsm")
