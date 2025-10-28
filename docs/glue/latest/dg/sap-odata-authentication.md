# SAP Authentication

The SAP connector supports both CUSTOM (this is SAP BASIC authentication) and OAUTH authentication methods.

## Custom Authentication

AWS Glue supports Custom (Basic Authentication) as a method for establishing connections to your SAP systems, allowing the use of a username and password for secure access. This auth type works well for automation scenarios as it allows using username and password up front with the permissions of a particular user in the SAP OData instance. AWS Glue is able to use the username and password to authenticate SAP OData APIs. In AWS Glue, basic authorization is implemented as custom authorization.

For public SAP OData documentation for Basic Auth flow, see [HTTP Basic Authentication](https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM/d599f15995d348a1b45ba5603e2aba9b/5c8bca0af1654b05a83193b2922dcee2.html "https://help.sap.com/docs/SAP_SUCCESSFACTORS_PLATFORM/d599f15995d348a1b45ba5603e2aba9b/5c8bca0af1654b05a83193b2922dcee2.html").

## OAuth 2.0 Authentication

AWS Glue also supports OAuth 2.0 as a secure authentication mechanism for establishing connections to your SAP systems. This enables seamless integration while ensuring compliance with modern authentication standards and enhancing the security of data access.

## AUTHORIZATION_CODE Grant Type

The grant type determines how AWS Glue communicates with SAP OData to request access to your data. SAP OData supports only the `AUTHORIZATION_CODE` grant type.
This grant type is considered "three-legged" OAuth as it relies on redirecting users to the third-party authorization server to authenticate the user. It is used when creating connections via the AWS Glue console.

Users may still opt to create their own connected app in SAP OData and provide their own client ID and client secret when creating connections through the AWS Glue console. In this scenario, they will still be redirected to SAP OData to login and authorize AWS Glue to access their resources.

This grant type results in a refresh token and access token. The access token is short lived, and may be refreshed automatically without user interaction using the refresh token.

For public SAP OData documentation on creating a connected app for Authorization Code OAuth flow, see [Authentication Using OAuth 2.0](https://help.sap.com/docs/ABAP_PLATFORM_NEW/e815bb97839a4d83be6c4fca48ee5777/2e5104fd87ff452b9acb247bd02b9f9e.html "https://help.sap.com/docs/ABAP_PLATFORM_NEW/e815bb97839a4d83be6c4fca48ee5777/2e5104fd87ff452b9acb247bd02b9f9e.html").
