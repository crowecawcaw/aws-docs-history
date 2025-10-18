# CreateHsm

Creates a new hardware security module (HSM) in the specified AWS CloudHSM
 cluster.


**Cross-account use:** No. You cannot perform this operation on an AWS CloudHSM cluster in a different Amazon Web Service account.


## Request Syntax



```
{
   "AvailabilityZone": "`string`",
   "ClusterId": "`string`",
   "IpAddress": "`string`"
}
```

## Request Parameters


For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").


The request accepts the following data in JSON format.





**[AvailabilityZone](#API_CreateHsm_RequestSyntax "#API_CreateHsm_RequestSyntax")**


The Availability Zone where you are creating the HSM. To find the cluster's
 Availability Zones, use [DescribeClusters](API_DescribeClusters.md "API_DescribeClusters.md").


Type: String


Pattern: `[a-z]{2}(-(gov))?-(east|west|north|south|central){1,2}-\d[a-z]`



Required: Yes




**[ClusterId](#API_CreateHsm_RequestSyntax "#API_CreateHsm_RequestSyntax")**


The identifier (ID) of the HSM's cluster. To find the cluster ID, use [DescribeClusters](API_DescribeClusters.md "API_DescribeClusters.md").


Type: String


Pattern: `cluster-[2-7a-zA-Z]{11,16}`



Required: Yes




**[IpAddress](#API_CreateHsm_RequestSyntax "#API_CreateHsm_RequestSyntax")**


The HSM's IP address. If you specify an IP address, use an available address from the
 subnet that maps to the Availability Zone where you are creating the HSM. If you don't specify
 an IP address, one is chosen for you from that subnet.


Type: String


Pattern: `\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}`



Required: No




## Response Syntax



```
{
   "Hsm": { 
      "AvailabilityZone": "***string***",
      "ClusterId": "***string***",
      "EniId": "***string***",
      "EniIp": "***string***",
      "EniIpV6": "***string***",
      "HsmId": "***string***",
      "HsmType": "***string***",
      "State": "***string***",
      "StateMessage": "***string***",
      "SubnetId": "***string***"
   }
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[Hsm](#API_CreateHsm_ResponseSyntax "#API_CreateHsm_ResponseSyntax")**


Information about the HSM that was created.


Type: [Hsm](API_Hsm.md "API_Hsm.md") object




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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudhsmv2-2017-04-28/CreateHsm "https://docs.aws.amazon.com/goto/cli2/cloudhsmv2-2017-04-28/CreateHsm")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudhsmv2-2017-04-28/CreateHsm "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudhsmv2-2017-04-28/CreateHsm")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudhsmv2-2017-04-28/CreateHsm "https://docs.aws.amazon.com/goto/SdkForCpp/cloudhsmv2-2017-04-28/CreateHsm")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudhsmv2-2017-04-28/CreateHsm "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudhsmv2-2017-04-28/CreateHsm")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudhsmv2-2017-04-28/CreateHsm "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudhsmv2-2017-04-28/CreateHsm")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudhsmv2-2017-04-28/CreateHsm "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudhsmv2-2017-04-28/CreateHsm")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudhsmv2-2017-04-28/CreateHsm "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudhsmv2-2017-04-28/CreateHsm")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudhsmv2-2017-04-28/CreateHsm "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudhsmv2-2017-04-28/CreateHsm")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudhsmv2-2017-04-28/CreateHsm "https://docs.aws.amazon.com/goto/boto3/cloudhsmv2-2017-04-28/CreateHsm")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudhsmv2-2017-04-28/CreateHsm "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudhsmv2-2017-04-28/CreateHsm")
