

# AzureConnectorConfiguration

The configuration of a connector to Microsoft Azure.

## Contents
<a name="API_AzureConnectorConfiguration_Contents"></a>

 ** ClientIdentifier **   <a name="cwoa-Type-AzureConnectorConfiguration-ClientIdentifier"></a>
The application (client) ID of the Azure app registration. The app registration must have a federated identity credential that trusts the AWS OpenID Connect (OIDC) issuer for your account.  
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`   
Required: Yes

 ** TenantIdentifier **   <a name="cwoa-Type-AzureConnectorConfiguration-TenantIdentifier"></a>
The ID of the Microsoft Entra ID tenant.  
Type: String  
Length Constraints: Fixed length of 36.  
Pattern: `[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`   
Required: Yes

## See Also
<a name="API_AzureConnectorConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/AzureConnectorConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/AzureConnectorConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/AzureConnectorConfiguration) 