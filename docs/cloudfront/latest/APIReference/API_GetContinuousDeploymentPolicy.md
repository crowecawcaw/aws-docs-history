# GetContinuousDeploymentPolicy

Gets a continuous deployment policy, including metadata (the policy's identifier and
 the date and time when the policy was last modified).


## Request Syntax



```
GET /2020-05-31/continuous-deployment-policy/`Id` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[Id](#API_GetContinuousDeploymentPolicy_RequestSyntax "#API_GetContinuousDeploymentPolicy_RequestSyntax")**


The identifier of the continuous deployment policy that you are getting.


Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ContinuousDeploymentPolicy>
   <ContinuousDeploymentPolicyConfig>
      <Enabled>***boolean***</Enabled>
      <StagingDistributionDnsNames>
         <Items>
            <DnsName>***string***</DnsName>
         </Items>
         <Quantity>***integer***</Quantity>
      </StagingDistributionDnsNames>
      <TrafficConfig>
         <SingleHeaderConfig>
            <Header>***string***</Header>
            <Value>***string***</Value>
         </SingleHeaderConfig>
         <SingleWeightConfig>
            <SessionStickinessConfig>
               <IdleTTL>***integer***</IdleTTL>
               <MaximumTTL>***integer***</MaximumTTL>
            </SessionStickinessConfig>
            <Weight>***float***</Weight>
         </SingleWeightConfig>
         <Type>***string***</Type>
      </TrafficConfig>
   </ContinuousDeploymentPolicyConfig>
   <Id>***string***</Id>
   <LastModifiedTime>***timestamp***</LastModifiedTime>
</ContinuousDeploymentPolicy>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[ContinuousDeploymentPolicy](#API_GetContinuousDeploymentPolicy_ResponseSyntax "#API_GetContinuousDeploymentPolicy_ResponseSyntax")**


Root level tag for the ContinuousDeploymentPolicy parameters.


Required: Yes




**[ContinuousDeploymentPolicyConfig](#API_GetContinuousDeploymentPolicy_ResponseSyntax "#API_GetContinuousDeploymentPolicy_ResponseSyntax")**


Contains the configuration for a continuous deployment policy.


Type: [ContinuousDeploymentPolicyConfig](API_ContinuousDeploymentPolicyConfig.md "API_ContinuousDeploymentPolicyConfig.md") object




**[Id](#API_GetContinuousDeploymentPolicy_ResponseSyntax "#API_GetContinuousDeploymentPolicy_ResponseSyntax")**


The identifier of the continuous deployment policy.


Type: String




**[LastModifiedTime](#API_GetContinuousDeploymentPolicy_ResponseSyntax "#API_GetContinuousDeploymentPolicy_ResponseSyntax")**


The date and time the continuous deployment policy was last modified.


Type: Timestamp




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDenied** 


Access denied.


HTTP Status Code: 403




**NoSuchContinuousDeploymentPolicy** 


The continuous deployment policy doesn't exist.


HTTP Status Code: 404




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetContinuousDeploymentPolicy "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetContinuousDeploymentPolicy")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/GetContinuousDeploymentPolicy "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/GetContinuousDeploymentPolicy")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetContinuousDeploymentPolicy "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetContinuousDeploymentPolicy")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetContinuousDeploymentPolicy "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetContinuousDeploymentPolicy")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetContinuousDeploymentPolicy "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetContinuousDeploymentPolicy")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetContinuousDeploymentPolicy "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetContinuousDeploymentPolicy")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetContinuousDeploymentPolicy "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetContinuousDeploymentPolicy")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetContinuousDeploymentPolicy "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetContinuousDeploymentPolicy")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetContinuousDeploymentPolicy "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetContinuousDeploymentPolicy")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetContinuousDeploymentPolicy "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetContinuousDeploymentPolicy")
