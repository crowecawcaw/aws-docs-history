

# NetworkConnectorSummary
<a name="API_NetworkConnectorSummary"></a>

Summary information about a network connector returned by `ListNetworkConnectors`. Contains identifying fields and current state. To retrieve full configuration details, use `GetNetworkConnector`.

## Contents
<a name="API_NetworkConnectorSummary_Contents"></a>

 ** Arn **   <a name="lambdacore-Type-NetworkConnectorSummary-Arn"></a>
The ARN of the network connector.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 140.  
Pattern: `(arn:aws[a-zA-Z-]*:lambda:(eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:network-connector:[a-zA-Z0-9-_]+(:[1-9]|[1-9][0-9]+)?)`   
Required: Yes

 ** Id **   <a name="lambdacore-Type-NetworkConnectorSummary-Id"></a>
The unique identifier of the network connector.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 140.  
Required: Yes

 ** Name **   <a name="lambdacore-Type-NetworkConnectorSummary-Name"></a>
The name of the network connector.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 140.  
Pattern: `(arn:aws[a-zA-Z-]*:lambda:(eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:network-connector:[a-zA-Z0-9-_]+(:[1-9]|[1-9][0-9]+)?)|[a-zA-Z0-9_-]{1,64}`   
Required: Yes

 ** Type **   <a name="lambdacore-Type-NetworkConnectorSummary-Type"></a>
The type of the network connector (`VPC_EGRESS`).  
Type: String  
Valid Values: `VPC_EGRESS`   
Required: Yes

 ** LastModified **   <a name="lambdacore-Type-NetworkConnectorSummary-LastModified"></a>
The date and time when the connector was last modified.  
Type: Timestamp  
Required: No

 ** State **   <a name="lambdacore-Type-NetworkConnectorSummary-State"></a>
The current state of the network connector.  
Type: String  
Valid Values: `PENDING | ACTIVE | INACTIVE | FAILED | DELETING | DELETE_FAILED`   
Required: No

## See Also
<a name="API_NetworkConnectorSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-core-2026-04-30/NetworkConnectorSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-core-2026-04-30/NetworkConnectorSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-core-2026-04-30/NetworkConnectorSummary) 