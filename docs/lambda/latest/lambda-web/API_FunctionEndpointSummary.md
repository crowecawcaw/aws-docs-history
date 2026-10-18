

# FunctionEndpointSummary
<a name="API_FunctionEndpointSummary"></a>

A summary of a web function endpoint.

## Contents
<a name="API_FunctionEndpointSummary_Contents"></a>

 ** authType **   <a name="lambdaweb-Type-FunctionEndpointSummary-authType"></a>
The authorization type for the endpoint.  
Type: String  
Valid Values: `ApplicationManaged | IamAuth`   
Required: Yes

 ** autoDeploymentMode **   <a name="lambdaweb-Type-FunctionEndpointSummary-autoDeploymentMode"></a>
The auto-deployment mode for the endpoint.  
Type: String  
Valid Values: `LatestRevision | Disabled`   
Required: Yes

 ** createdAt **   <a name="lambdaweb-Type-FunctionEndpointSummary-createdAt"></a>
The date and time the endpoint was created.  
Type: Timestamp  
Required: Yes

 ** domainName **   <a name="lambdaweb-Type-FunctionEndpointSummary-domainName"></a>
The domain name of the endpoint.  
Type: String  
Length Constraints: Minimum length of 4. Maximum length of 256.  
Pattern: `([a-z0-9-]+\.)+[a-z]+`   
Required: Yes

 ** endpointArn **   <a name="lambdaweb-Type-FunctionEndpointSummary-endpointArn"></a>
The Amazon Resource Name (ARN) of the endpoint.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Required: Yes

 ** endpointName **   <a name="lambdaweb-Type-FunctionEndpointSummary-endpointName"></a>
The name of the endpoint.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Required: Yes

 ** endpointType **   <a name="lambdaweb-Type-FunctionEndpointSummary-endpointType"></a>
The type of the endpoint.  
Type: String  
Valid Values: `HomeRegion | MultiRegion | PerRegion`   
Required: Yes

 ** regions **   <a name="lambdaweb-Type-FunctionEndpointSummary-regions"></a>
The list of Regions for the endpoint.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 100 items.  
Length Constraints: Minimum length of 1. Maximum length of 50.  
Pattern: `([a-z]{2,}-){2,}[0-9]`   
Required: Yes

 ** revisionWeights **   <a name="lambdaweb-Type-FunctionEndpointSummary-revisionWeights"></a>
The revision weights for the endpoint.  
Type: Array of [RevisionWeight](API_RevisionWeight.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 2 items.  
Required: Yes

 ** state **   <a name="lambdaweb-Type-FunctionEndpointSummary-state"></a>
The current state of the endpoint.  
Type: String  
Valid Values: `Pending | Active | Failed | Deleting`   
Required: Yes

 ** stateReason **   <a name="lambdaweb-Type-FunctionEndpointSummary-stateReason"></a>
The reason for the current state of the endpoint.  
Type: String  
Required: Yes

 ** updatedAt **   <a name="lambdaweb-Type-FunctionEndpointSummary-updatedAt"></a>
The date and time the endpoint was last updated.  
Type: Timestamp  
Required: Yes

 ** description **   <a name="lambdaweb-Type-FunctionEndpointSummary-description"></a>
A description of the endpoint.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 256.  
Required: No

 ** scalingConfig **   <a name="lambdaweb-Type-FunctionEndpointSummary-scalingConfig"></a>
The scaling configuration for the endpoint. This field is absent if the endpoint has no scaling configuration.  
Type: [ScalingConfig](API_ScalingConfig.md) object  
Required: No

 ** throttleConfig **   <a name="lambdaweb-Type-FunctionEndpointSummary-throttleConfig"></a>
The throttling configuration for the endpoint. This field is absent if the endpoint has no throttling configuration.  
Type: [ThrottleConfig](API_ThrottleConfig.md) object  
Required: No

 ** updateStatus **   <a name="lambdaweb-Type-FunctionEndpointSummary-updateStatus"></a>
The status of the most recent update to the endpoint.  
Type: String  
Valid Values: `InProgress | Successful | Failed`   
Required: No

 ** updateStatusReason **   <a name="lambdaweb-Type-FunctionEndpointSummary-updateStatusReason"></a>
The reason for the current update status of the endpoint.  
Type: String  
Required: No

## See Also
<a name="API_FunctionEndpointSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-web-2025-03-07/FunctionEndpointSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-web-2025-03-07/FunctionEndpointSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-web-2025-03-07/FunctionEndpointSummary) 