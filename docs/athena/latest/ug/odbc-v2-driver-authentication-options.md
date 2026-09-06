

# Authentication options
<a name="odbc-v2-driver-authentication-options"></a>

You can connect to Amazon Athena using the following authentication types. For all types, the connection string name is `AuthenticationType`, the parameter type is `Required`, and the default value is `IAM Credentials`. For information about the parameters for each authentication type, visit the corresponding link. For common authentication parameters, see [Common authentication parameters](odbc-v2-driver-common-authentication-parameters.md).



| Authentication type | Connection string example | 
| --- | --- | 
| [IAM credentials](odbc-v2-driver-iam-credentials.md) | AuthenticationType=IAM Credentials; | 
| [IAM profile](odbc-v2-driver-iam-profile.md) | AuthenticationType=IAM Profile; | 
| [AD FS](odbc-v2-driver-ad-fs.md) | AuthenticationType=ADFS; | 
| [Azure AD](odbc-v2-driver-azure-ad.md) | AuthenticationType=AzureAD; | 
| [Browser Azure AD](odbc-v2-driver-browser-azure-ad.md) | AuthenticationType=BrowserAzureAD; | 
| [Browser SAML](odbc-v2-driver-browser-saml.md) | AuthenticationType=BrowserSAML; | 
| [Browser SSO OIDC](odbc-v2-driver-browser-sso-oidc.md) | AuthenticationType=BrowserSSOOIDC; | 
| [Default credentials](odbc-v2-driver-default-credentials.md) | AuthenticationType=Default Credentials; | 
| [External credentials](odbc-v2-driver-external-credentials.md) | AuthenticationType=External Credentials; | 
| [Instance profile](odbc-v2-driver-instance-profile.md) | AuthenticationType=Instance Profile; | 
| [JWT](odbc-v2-driver-jwt.md) | AuthenticationType=JWT; | 
| [JWT Trusted identity propagation credentials provider](odbc-v2-driver-jwt-tip.md) | AuthenticationType=JWT\_TIP; | 
| [Browser trusted identity propagation credentials](odbc-v2-driver-browser-oidc-tip.md) | AuthenticationType=BrowserOidcTip; | 
| [Okta](odbc-v2-driver-okta.md) | AuthenticationType=Okta; | 
| [Ping](odbc-v2-driver-ping.md) | AuthenticationType=Ping; | 
| [SageMaker Browser IDC](odbc-v2-driver-sagemaker-idc.md) | AuthenticationType=SageMakerBrowserIdc; | 
| [SageMaker IAM](odbc-v2-driver-sagemaker-iam.md) | AuthenticationType=SageMakerIam; | 