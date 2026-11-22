

# ConnectorSummary

Summary information about a connector.

## Contents
<a name="API_ConnectorSummary_Contents"></a>

 ** Arn **   <a name="cwoa-Type-ConnectorSummary-Arn"></a>
The Amazon Resource Name (ARN) of the connector.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1011.  
Pattern: `arn:aws([a-z0-9\-]+)?:([a-zA-Z0-9\-]+):([a-z0-9\-]+)?:([0-9]{12})?:(.+)`   
Required: Yes

 ** Provider **   <a name="cwoa-Type-ConnectorSummary-Provider"></a>
The cloud provider that the connector connects to.  
Type: String  
Valid Values: `AZURE`   
Required: Yes

 ** CreatedTimeStamp **   <a name="cwoa-Type-ConnectorSummary-CreatedTimeStamp"></a>
The time when the connector was created, in milliseconds since the Unix epoch.  
Type: Long  
Required: No

 ** Name **   <a name="cwoa-Type-ConnectorSummary-Name"></a>
The name of the connector.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z][a-zA-Z0-9\-_.]*`   
Required: No

## See Also
<a name="API_ConnectorSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/ConnectorSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/ConnectorSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/ConnectorSummary) 