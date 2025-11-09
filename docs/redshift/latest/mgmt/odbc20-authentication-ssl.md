Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Authentication methods

To protect data from unauthorized access, Amazon Redshift data stores require all connections
to be authenticated using user credentials.

The following table illustrates the required and optional connection options for each
authentication method that can be used to connect to the Amazon Redshift ODBC driver version
2.x:

| Authentication Method   | Required                                                                                                                          | Optional                                                                                                                                                                                                                                                                         |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Standard                | • Host<br>• Port<br>• Database<br>• UID<br>• Password                                                                             |                                                                                                                                                                                                                                                                                  |
| IAM Profile             | • Host<br>• Port<br>• Database<br>• IAM<br>• Profile                                                                              | • ClusterID<br>• Region<br>• AutoCreate<br>• EndpointURL<br>• StsEndpointURL<br>• InstanceProfile<br>Note<br>**ClusterID\*<br>• and **Region**<br>must be set in **Host\*<br>• if they are not set<br>separately.                                                                |
| IAM Credentials         | • Host<br>• Port<br>• Database<br>• IAM<br>• AccessKeyID<br>• SecretAccessKey                                                     | • ClusterID<br>• Region<br>• AutoCreate<br>• EndpointURL<br>• StsEndpointURL<br>• SessionToken<br>• UID<br>Note<br>**ClusterID\*<br>• and **Region**<br>must be set in **Host\*<br>• if they are not set<br>separately.                                                          |
| AD FS                   | • Host<br>• Port<br>• Database<br>• IAM<br>• plugin_name<br>• UID<br>• Password<br>• IdP_Host<br>• IdP_Port                       | • ClusterID<br>• Region<br>• AutoCreate<br>• EndpointUrl<br>• StsEndpointUrl<br>• Preferred_Role<br>• loginToRp<br>• SSL_Insecure<br>Note<br>**ClusterID\*<br>• and **Region**<br>must be set in **Host\*<br>• if they are not set<br>separately.                                |
| Azure AD                | • Host<br>• Port<br>• Database<br>• IAM<br>• plugin_name<br>• UID<br>• Password<br>• IdP_Tenant<br>• Client_ID<br>• Client_Secret | • ClusterID<br>• Region<br>• AutoCreate<br>• EndpointUrl<br>• StsEndpointUrl<br>• Preferred_Role<br>• dbgroups_filter<br>Note<br>**ClusterID\*<br>• and **Region**<br>must be set in **Host\*<br>• if they are not set<br>separately.                                            |
| JWT                     | • Host<br>• Port<br>• Database<br>• IAM<br>• plugin_name<br>• web_identity_token                                                  | • provider_name                                                                                                                                                                                                                                                                  |
| Okta                    | • Host<br>• Port<br>• Database<br>• IAM<br>• plugin_name<br>• UID<br>• Password<br>• IdP_Host<br>• App_Name<br>• App_ID           | • ClusterID<br>• Region<br>• AutoCreate<br>• EndpointUrl<br>• StsEndpointUrl<br>• Preferred_Role<br>Note<br>**ClusterID\*<br>• and **Region**<br>must be set in **Host\*<br>• if they are not set<br>separately.                                                                 |
| Ping Federate           | • Host<br>• Port<br>• Database<br>• IAM<br>• plugin_name<br>• UID<br>• Password<br>• IdP_Host<br>• IdP_Port                       | • ClusterID<br>• Region<br>• AutoCreate<br>• EndpointUrl<br>• StsEndpointUrl<br>• Preferred_Role<br>• SSL_Insecure<br>• partner_spid<br>Note<br>**ClusterID\*<br>• and **Region**<br>must be set in **Host\*<br>• if they are not set<br>separately.                             |
| Browser Azure AD        | • Host<br>• Port<br>• Database<br>• IAM<br>• plugin_name<br>• IdP_Tenant<br>• Client_ID<br>• UID                                  | • ClusterID<br>• Region<br>• AutoCreate<br>• EndpointUrl<br>• StsEndpointUrl<br>• Preferred_Role<br>• dbgroups_filter<br>• IdP_Response_Timeout<br>• listen_port<br>Note<br>**ClusterID\*<br>• and **Region**<br>must be set in **Host\*<br>• if they are not set<br>separately. |
| Browser SAML            | • Host<br>• Port<br>• Database<br>• IAM<br>• plugin_name<br>• login_url<br>• UID                                                  | • ClusterID<br>• Region<br>• AutoCreate<br>• EndpointUrl<br>• StsEndpointUrl<br>• Preferred_Role<br>• dbgroups_filter<br>• IdP_Response_Timeout<br>• listen_port<br>Note<br>**ClusterID\*<br>• and **Region**<br>must be set in **Host\*<br>• if they are not set<br>separately. |
| Auth Profile            | • Host<br>• Port<br>• Database<br>• AccessKeyID<br>• SecretAccessKey                                                              |                                                                                                                                                                                                                                                                                  |
| Browser Azure AD OAUTH2 | • Host<br>• Port<br>• Database<br>• IAM<br>• plugin_name<br>• IdP_Tenant<br>• Client_ID<br>• UID                                  | • ClusterID<br>• Region<br>• EndpointUrl<br>• IdP_Response_Timeout<br>• listen_port<br>• scope<br>• provider_name<br>Note<br>**ClusterID\*<br>• and **Region**<br>must be set in **Host\*<br>• if they are not set<br>separately.                                                |
| AWS IAM Identity Center | • Host<br>• Database<br>• plugin_name<br>• idc_region<br>• issuer_url                                                             | • idc_client_display_name<br>• idp_response_timeout<br>• listen_port                                                                                                                                                                                                             |

## Using an external credentials

service

In addition to built-in support for AD FS, Azure AD, and Okta, the Windows version
of the Amazon Redshift ODBC driver also provides support for other credentials services.
The driver can authenticate connections using any SAML-based credential provider
plugin of your choice.

To configure an external credentials service on Windows:

1. Create an IAM profile that specifies the credential provider plugin and
   other authentication parameters as needed. The profile must be
   ASCII-encoded, and must contain the following key-value pair, where
   `PluginPath` is the full path to the plugin application:

```
plugin_name = `PluginPath`
```

For example:

```
plugin_name = C:\Users\kjson\myapp\CredServiceApp.exe
```

For information on how to create a profile, see [Using a Configuration Profile](options-for-providing-iam-credentials.md#using-configuration-profile "options-for-providing-iam-credentials.md#using-configuration-profile") in the Amazon Redshift Cluster
Management Guide. 2. Configure the driver to use this profile. The driver detects and uses the
authentication settings specified in the profile.
