

# ThrottleConfig
<a name="API_ThrottleConfig"></a>

The throttling configuration for a web function endpoint.

## Contents
<a name="API_ThrottleConfig_Contents"></a>

 ** rateLimit **   <a name="lambdaweb-Type-ThrottleConfig-rateLimit"></a>
The maximum request rate per second for the endpoint. The value must be one of the following supported values: `0`, `100`, `200`, `300`, `400`, `500`, `600`, `700`, `800`, `900`, `1000`, `2000`, `3000`, `4000`, `5000`, `6000`, `7000`, `8000`, `9000`, or `10000`. The maximum effective value is also bounded by your account-level maximum total rate limit. There is no default value. If you don't specify a value, the throttling configuration is absent from the response. On an update, omit `throttleConfig` to keep the current value, or specify an empty object to clear a previously set value.  
Type: Integer  
Valid Range: Minimum value of 0.  
Required: No

## See Also
<a name="API_ThrottleConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-web-2025-03-07/ThrottleConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-web-2025-03-07/ThrottleConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-web-2025-03-07/ThrottleConfig) 