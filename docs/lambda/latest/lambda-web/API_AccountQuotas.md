

# AccountQuotas
<a name="API_AccountQuotas"></a>

The quotas that apply to web functions in your account in the current AWS Region.

## Contents
<a name="API_AccountQuotas_Contents"></a>

 ** maxEndpointsPerFunction **   <a name="lambdaweb-Type-AccountQuotas-maxEndpointsPerFunction"></a>
The maximum number of endpoints that a single web function can have.  
Type: Integer  
Valid Range: Minimum value of 0.  
Required: Yes

 ** maxRevisionsPerFunction **   <a name="lambdaweb-Type-AccountQuotas-maxRevisionsPerFunction"></a>
The maximum number of revisions that a single web function can have.  
Type: Integer  
Valid Range: Minimum value of 0.  
Required: Yes

 ** maxTotalArmVCpus **   <a name="lambdaweb-Type-AccountQuotas-maxTotalArmVCpus"></a>
The maximum total number of Arm vCPUs that you can allocate across all of your web functions in the current AWS Region.  
Type: Integer  
Valid Range: Minimum value of 0.  
Required: Yes

 ** maxTotalRateLimit **   <a name="lambdaweb-Type-AccountQuotas-maxTotalRateLimit"></a>
The maximum number of requests per second allowed across all of your web function endpoints in your account in the current AWS Region.  
Type: Integer  
Valid Range: Minimum value of 0.  
Required: Yes

## See Also
<a name="API_AccountQuotas_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-web-2025-03-07/AccountQuotas) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-web-2025-03-07/AccountQuotas) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-web-2025-03-07/AccountQuotas) 