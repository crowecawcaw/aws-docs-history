

# RegionalEndpoint
<a name="API_RegionalEndpoint"></a>

Represents the endpoint configuration and state in a specific Region.

## Contents
<a name="API_RegionalEndpoint_Contents"></a>

 ** authType **   <a name="lambdaweb-Type-RegionalEndpoint-authType"></a>
The authorization type for the regional endpoint.  
Type: String  
Valid Values: `ApplicationManaged | IamAuth`   
Required: Yes

 ** revisionWeights **   <a name="lambdaweb-Type-RegionalEndpoint-revisionWeights"></a>
The revision weights for the regional endpoint.  
Type: Array of [RevisionWeight](API_RevisionWeight.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 2 items.  
Required: Yes

 ** state **   <a name="lambdaweb-Type-RegionalEndpoint-state"></a>
The current state of the regional endpoint.  
Type: String  
Valid Values: `Pending | Active | Failed | Deleting`   
Required: Yes

 ** stateReason **   <a name="lambdaweb-Type-RegionalEndpoint-stateReason"></a>
The reason for the current state of the regional endpoint.  
Type: String  
Required: Yes

 ** domainName **   <a name="lambdaweb-Type-RegionalEndpoint-domainName"></a>
The domain name of the regional endpoint.  
Type: String  
Length Constraints: Minimum length of 4. Maximum length of 256.  
Pattern: `([a-z0-9-]+\.)+[a-z]+`   
Required: No

 ** scalingConfig **   <a name="lambdaweb-Type-RegionalEndpoint-scalingConfig"></a>
The scaling configuration for the regional endpoint. This field is absent if the endpoint has no scaling configuration.  
Type: [ScalingConfig](API_ScalingConfig.md) object  
Required: No

 ** throttleConfig **   <a name="lambdaweb-Type-RegionalEndpoint-throttleConfig"></a>
The throttling configuration for the regional endpoint. This field is absent if the endpoint has no throttling configuration.  
Type: [ThrottleConfig](API_ThrottleConfig.md) object  
Required: No

 ** updateStatus **   <a name="lambdaweb-Type-RegionalEndpoint-updateStatus"></a>
The status of the most recent update to the regional endpoint.  
Type: String  
Valid Values: `InProgress | Successful | Failed`   
Required: No

 ** updateStatusReason **   <a name="lambdaweb-Type-RegionalEndpoint-updateStatusReason"></a>
The reason for the current update status of the regional endpoint.  
Type: String  
Required: No

## See Also
<a name="API_RegionalEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-web-2025-03-07/RegionalEndpoint) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-web-2025-03-07/RegionalEndpoint) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-web-2025-03-07/RegionalEndpoint) 