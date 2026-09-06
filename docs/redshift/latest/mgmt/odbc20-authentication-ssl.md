

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Authentication methods
<a name="odbc20-authentication-ssl"></a>

To protect data from unauthorized access, Amazon Redshift data stores require all connections to be authenticated using user credentials.

The following table illustrates the required and optional connection options for each authentication method that can be used to connect to the Amazon Redshift ODBC driver version 2.x:


| Authentication Method | Required | Optional | 
| --- | --- | --- | 
|  Standard  |  +  Host <br />+  Port  <br />+  Database <br />+  UID <br />+  Password   |   | 
|  IAM Profile  |  +  Host <br />+  Port <br />+  Database <br />+  IAM <br />+  Profile   |  +  ClusterID <br />+  Region <br />+  AutoCreate <br />+  EndpointURL <br />+  StsEndpointURL <br />+  InstanceProfile    **ClusterID** and **Region** must be set in **Host** if they are not set separately.    | 
|  IAM Credentials  |  +  Host <br />+  Port  <br />+  Database <br />+  IAM <br />+  AccessKeyID <br />+  SecretAccessKey   |  +  ClusterID <br />+  Region <br />+  AutoCreate <br />+  EndpointURL <br />+  StsEndpointURL <br />+  SessionToken <br />+  UID    **ClusterID** and **Region** must be set in **Host** if they are not set separately.    | 
|  AD FS  |  +  Host <br />+  Port  <br />+  Database <br />+  IAM <br />+  plugin\_name <br />+  UID <br />+  Password <br />+  IdP\_Host <br />+  IdP\_Port   |  +  ClusterID <br />+  Region <br />+  AutoCreate <br />+  EndpointUrl <br />+  StsEndpointUrl <br />+  Preferred\_Role <br />+  loginToRp <br />+  SSL\_Insecure    **ClusterID** and **Region** must be set in **Host** if they are not set separately.    | 
|  Azure AD  |  +  Host <br />+  Port <br />+  Database <br />+  IAM <br />+  plugin\_name <br />+  UID <br />+  Password <br />+  IdP\_Tenant <br />+  Client\_ID <br />+  Client\_Secret   |  +  ClusterID <br />+  Region <br />+  AutoCreate <br />+  EndpointUrl <br />+  StsEndpointUrl <br />+  Preferred\_Role <br />+  dbgroups\_filter    **ClusterID** and **Region** must be set in **Host** if they are not set separately.    | 
|  JWT  |  +  Host <br />+  Port <br />+  Database <br />+  IAM <br />+  plugin\_name <br />+  web\_identity\_token   |  +  provider\_name   | 
|  Okta  |  +  Host <br />+  Port <br />+  Database <br />+  IAM <br />+  plugin\_name <br />+  UID <br />+  Password <br />+  IdP\_Host <br />+  App\_Name <br />+  App\_ID   |  +  ClusterID <br />+  Region <br />+  AutoCreate <br />+  EndpointUrl <br />+  StsEndpointUrl <br />+  Preferred\_Role    **ClusterID** and **Region** must be set in **Host** if they are not set separately.    | 
| Ping Federate |  +  Host <br />+  Port <br />+  Database <br />+  IAM <br />+  plugin\_name <br />+  UID <br />+  Password <br />+  IdP\_Host <br />+  IdP\_Port   |  +  ClusterID <br />+  Region <br />+  AutoCreate <br />+  EndpointUrl <br />+  StsEndpointUrl <br />+  Preferred\_Role <br />+  SSL\_Insecure <br />+  partner\_spid    **ClusterID** and **Region** must be set in **Host** if they are not set separately.    | 
|  Browser Azure AD  |  +  Host <br />+  Port <br />+  Database <br />+  IAM <br />+  plugin\_name <br />+  IdP\_Tenant <br />+  Client\_ID <br />+  UID   |  +  ClusterID <br />+  Region <br />+  AutoCreate <br />+  EndpointUrl <br />+  StsEndpointUrl <br />+  Preferred\_Role <br />+  dbgroups\_filter <br />+  IdP\_Response\_Timeout <br />+  listen\_port    **ClusterID** and **Region** must be set in **Host** if they are not set separately.    | 
|  Browser SAML  |  +  Host <br />+  Port <br />+  Database <br />+  IAM <br />+  plugin\_name <br />+  login\_url <br />+  UID   |  +  ClusterID <br />+  Region <br />+  AutoCreate <br />+  EndpointUrl <br />+  StsEndpointUrl <br />+  Preferred\_Role <br />+  dbgroups\_filter <br />+  IdP\_Response\_Timeout <br />+  listen\_port    **ClusterID** and **Region** must be set in **Host** if they are not set separately.    | 
|  Auth Profile  |  +  Host <br />+  Port <br />+  Database <br />+  AccessKeyID <br />+  SecretAccessKey   |   | 
|  Browser Azure AD OAUTH2  |  +  Host <br />+  Port  <br />+  Database <br />+  IAM <br />+  plugin\_name <br />+  IdP\_Tenant <br />+  Client\_ID <br />+  UID   |  +  ClusterID <br />+  Region <br />+  EndpointUrl <br />+  IdP\_Response\_Timeout <br />+  listen\_port <br />+  scope <br />+  provider\_name    **ClusterID** and **Region** must be set in **Host** if they are not set separately.    | 
|  AWS IAM Identity Center  |  +  Host <br />+  Database <br />+  plugin\_name <br />+  idc\_region <br />+  issuer\_url   |  +  idc\_client\_display\_name <br />+  idp\_response\_timeout <br />+  listen\_port   | 

## Using an external credentials service
<a name="odbc20-authentication-external"></a>

In addition to built-in support for AD FS, Azure AD, and Okta, the Windows version of the Amazon Redshift ODBC driver also provides support for other credentials services. The driver can authenticate connections using any SAML-based credential provider plugin of your choice. 

To configure an external credentials service on Windows:

1. Create an IAM profile that specifies the credential provider plugin and other authentication parameters as needed. The profile must be ASCII-encoded, and must contain the following key-value pair, where `PluginPath` is the full path to the plugin application: 

   ```
   plugin_name = {{PluginPath}}
   ```

   For example:

   ```
   plugin_name = C:\Users\kjson\myapp\CredServiceApp.exe 
   ```

   For information on how to create a profile, see [ Using a Configuration Profile ](https://docs.aws.amazon.com/redshift/latest/mgmt/options-for-providing-iam-credentials.html#using-configuration-profile) in the Amazon Redshift Cluster Management Guide.

1. Configure the driver to use this profile. The driver detects and uses the authentication settings specified in the profile.