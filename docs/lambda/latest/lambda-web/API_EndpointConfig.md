

# EndpointConfig
<a name="API_EndpointConfig"></a>

The configuration for a web function endpoint.

## Contents
<a name="API_EndpointConfig_Contents"></a>

 ** authType **   <a name="lambdaweb-Type-EndpointConfig-authType"></a>
The authorization type for the endpoint.  
Valid values:  
+  `ApplicationManaged` – Your application handles authorization.
+  `IamAuth` – Lambda uses IAM to authorize requests, which must be signed with Signature Version 4 (SigV4).
Type: String  
Valid Values: `ApplicationManaged | IamAuth`   
Required: Yes

 ** endpointName **   <a name="lambdaweb-Type-EndpointConfig-endpointName"></a>
The name of the endpoint. The name can contain letters, numbers, hyphens (-), and underscores (\_), and can't begin or end with a hyphen or an underscore. The name is limited to 64 characters in length.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: Yes

 ** endpointType **   <a name="lambdaweb-Type-EndpointConfig-endpointType"></a>
The type of endpoint. Determines how traffic is served and routed across Regions.  
Valid values:  
+  `HomeRegion` – Serves traffic from the Region where you created the web function.
+  `MultiRegion` – Replicates across the Regions that you choose and routes each request to the nearest one.
+  `PerRegion` – Creates a separate endpoint in each Region that you choose.
Type: String  
Valid Values: `HomeRegion | MultiRegion | PerRegion`   
Required: Yes

 ** autoDeploymentMode **   <a name="lambdaweb-Type-EndpointConfig-autoDeploymentMode"></a>
The auto-deployment mode for the endpoint. If you don't specify a value, the default is `Disabled`, and this default is returned in the response.  
Valid values:  
+  `LatestRevision` – The endpoint automatically serves the newest revision.
+  `Disabled` – Revision routing stays fixed until you change it.
Type: String  
Valid Values: `LatestRevision | Disabled`   
Required: No

 ** description **   <a name="lambdaweb-Type-EndpointConfig-description"></a>
A description of the endpoint.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Required: No

 ** regions **   <a name="lambdaweb-Type-EndpointConfig-regions"></a>
The list of Regions for the endpoint. Required when the endpoint type is `MultiRegion` or `PerRegion`: specify at least one Region other than the Region where you create the endpoint (the home Region). The home Region is added automatically if you don't include it; specifying only the home Region isn't allowed. When the endpoint type is `HomeRegion`, omit this field or specify only the home Region.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 100 items.  
Length Constraints: Minimum length of 1. Maximum length of 50.  
Pattern: `([a-z]{2,}-){2,}[0-9]`   
Required: No

 ** scalingConfig **   <a name="lambdaweb-Type-EndpointConfig-scalingConfig"></a>
The scaling configuration for the endpoint.  
Type: [ScalingConfig](API_ScalingConfig.md) object  
Required: No

 ** throttleConfig **   <a name="lambdaweb-Type-EndpointConfig-throttleConfig"></a>
The throttling configuration for the endpoint.  
Type: [ThrottleConfig](API_ThrottleConfig.md) object  
Required: No

## See Also
<a name="API_EndpointConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-web-2025-03-07/EndpointConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-web-2025-03-07/EndpointConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-web-2025-03-07/EndpointConfig) 