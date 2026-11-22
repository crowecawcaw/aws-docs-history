

# Connector

A connector to a third-party cloud provider.

## Contents
<a name="API_Connector_Contents"></a>

 ** Arn **   <a name="cwoa-Type-Connector-Arn"></a>
The Amazon Resource Name (ARN) of the connector.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1011.  
Pattern: `arn:aws([a-z0-9\-]+)?:([a-zA-Z0-9\-]+):([a-z0-9\-]+)?:([0-9]{12})?:(.+)`   
Required: Yes

 ** ConnectorConfiguration **   <a name="cwoa-Type-Connector-ConnectorConfiguration"></a>
The configuration for connecting to the third-party cloud provider.  
Type: [ConnectorConfiguration](API_ConnectorConfiguration.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** Provider **   <a name="cwoa-Type-Connector-Provider"></a>
The cloud provider that the connector connects to.  
Type: String  
Valid Values: `AZURE`   
Required: Yes

 ** RoleArn **   <a name="cwoa-Type-Connector-RoleArn"></a>
The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that CloudWatch assumes to obtain credentials for the third-party cloud provider.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 1011.  
Pattern: `arn:aws([a-z0-9\-]+)?:([a-zA-Z0-9\-]+):([a-z0-9\-]+)?:([0-9]{12})?:(.+)`   
Required: Yes

 ** CreatedTimeStamp **   <a name="cwoa-Type-Connector-CreatedTimeStamp"></a>
The time when the connector was created, in milliseconds since the Unix epoch.  
Type: Long  
Required: No

 ** Name **   <a name="cwoa-Type-Connector-Name"></a>
The name of the connector.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z][a-zA-Z0-9\-_.]*`   
Required: No

## See Also
<a name="API_Connector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/Connector) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/Connector) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/Connector) 