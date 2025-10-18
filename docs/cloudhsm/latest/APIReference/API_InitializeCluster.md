# InitializeCluster

Claims an AWS CloudHSM cluster by submitting the cluster certificate issued by your
 issuing certificate authority (CA) and the CA's root certificate. Before you can claim a
 cluster, you must sign the cluster's certificate signing request (CSR) with your issuing CA.
 To get the cluster's CSR, use [DescribeClusters](API_DescribeClusters.md "API_DescribeClusters.md").


**Cross-account use:** No. You cannot perform this operation on an AWS CloudHSM cluster in a different AWS account.


## Request Syntax



```
{
   "ClusterId": "`string`",
   "SignedCert": "`string`",
   "TrustAnchor": "`string`"
}
```

## Request Parameters


For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").


The request accepts the following data in JSON format.





**[ClusterId](#API_InitializeCluster_RequestSyntax "#API_InitializeCluster_RequestSyntax")**


The identifier (ID) of the cluster that you are claiming. To find the cluster ID, use
 [DescribeClusters](API_DescribeClusters.md "API_DescribeClusters.md").


Type: String


Pattern: `cluster-[2-7a-zA-Z]{11,16}`



Required: Yes




**[SignedCert](#API_InitializeCluster_RequestSyntax "#API_InitializeCluster_RequestSyntax")**


The cluster certificate issued (signed) by your issuing certificate authority (CA). The
 certificate must be in PEM format and can contain a maximum of 5000 characters.


Type: String


Length Constraints: Maximum length of 20000.


Pattern: `[a-zA-Z0-9+-/=\s]*`



Required: Yes




**[TrustAnchor](#API_InitializeCluster_RequestSyntax "#API_InitializeCluster_RequestSyntax")**


The issuing certificate of the issuing certificate authority (CA) that issued (signed)
 the cluster certificate. You must use a self-signed certificate. The certificate used to sign the HSM CSR must be directly available, and thus must be the
 root certificate. The certificate must be in PEM format and can contain a
 maximum of 5000 characters.


Type: String


Length Constraints: Maximum length of 20000.


Pattern: `[a-zA-Z0-9+-/=\s]*`



Required: Yes




## Response Syntax



```
{
   "State": "***string***",
   "StateMessage": "***string***"
}
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in JSON format by the service.





**[State](#API_InitializeCluster_ResponseSyntax "#API_InitializeCluster_ResponseSyntax")**


The cluster's state.


Type: String


Valid Values: `CREATE_IN_PROGRESS | UNINITIALIZED | INITIALIZE_IN_PROGRESS | INITIALIZED | ACTIVE | UPDATE_IN_PROGRESS | MODIFY_IN_PROGRESS | ROLLBACK_IN_PROGRESS | PENDING_ROLLBACK | DELETE_IN_PROGRESS | DELETED | DEGRADED`





**[StateMessage](#API_InitializeCluster_ResponseSyntax "#API_InitializeCluster_ResponseSyntax")**


A description of the cluster's state.


Type: String


Length Constraints: Maximum length of 300.


Pattern: `.*`





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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudhsmv2-2017-04-28/InitializeCluster "https://docs.aws.amazon.com/goto/cli2/cloudhsmv2-2017-04-28/InitializeCluster")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudhsmv2-2017-04-28/InitializeCluster "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudhsmv2-2017-04-28/InitializeCluster")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudhsmv2-2017-04-28/InitializeCluster "https://docs.aws.amazon.com/goto/SdkForCpp/cloudhsmv2-2017-04-28/InitializeCluster")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudhsmv2-2017-04-28/InitializeCluster "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudhsmv2-2017-04-28/InitializeCluster")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudhsmv2-2017-04-28/InitializeCluster "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudhsmv2-2017-04-28/InitializeCluster")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudhsmv2-2017-04-28/InitializeCluster "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudhsmv2-2017-04-28/InitializeCluster")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudhsmv2-2017-04-28/InitializeCluster "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudhsmv2-2017-04-28/InitializeCluster")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudhsmv2-2017-04-28/InitializeCluster "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudhsmv2-2017-04-28/InitializeCluster")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudhsmv2-2017-04-28/InitializeCluster "https://docs.aws.amazon.com/goto/boto3/cloudhsmv2-2017-04-28/InitializeCluster")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudhsmv2-2017-04-28/InitializeCluster "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudhsmv2-2017-04-28/InitializeCluster")
