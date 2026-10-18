

# ScalingConfig
<a name="API_ScalingConfig"></a>

The scaling configuration for a web function endpoint.

## Contents
<a name="API_ScalingConfig_Contents"></a>

 ** maxEnvironments **   <a name="lambdaweb-Type-ScalingConfig-maxEnvironments"></a>
The maximum number of concurrent execution environments for the endpoint. Minimum value of 2, maximum value of 10000. There is no default value. If you don't specify a value, the scaling configuration is absent from the response. On an update, omit `scalingConfig` to keep the current value, or specify an empty object to clear a previously set value.  
Type: Integer  
Valid Range: Minimum value of 2. Maximum value of 10000.  
Required: No

## See Also
<a name="API_ScalingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-web-2025-03-07/ScalingConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-web-2025-03-07/ScalingConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-web-2025-03-07/ScalingConfig) 