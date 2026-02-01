Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Configuring authentication and

SSL

To protect data from unauthorized access, Amazon Redshift data stores require all connections to
be authenticated using user credentials. Some data stores also require connections to be
made over the Secure Sockets Layer (SSL) protocol, either with or without one-way
authentication.

The Amazon Redshift JDBC driver version 2.x provides full support for these authentication
protocols.

The SSL version that the driver supports depends on the JVM version that you are
using. For information about the SSL versions that are supported by each version of
Java, see [Diagnosing TLS, SSL, and HTTPS](https://blogs.oracle.com/java-platform-group/diagnosing-tls,-ssl,-and-https "https://blogs.oracle.com/java-platform-group/diagnosing-tls,-ssl,-and-https") on the Java Platform Group Product
Management Blog.

The SSL version used for the connection is the highest version that is supported by
both the driver and the server, which is determined at connection time.

Configure the Amazon Redshift JDBC driver version 2.x to authenticate your connection
according to the security requirements of the Redshift server that you are connecting
to.

You must always provide your Redshift username and password to authenticate the
connection. Depending on whether SSL is enabled and required on the server, you might
also need to configure the driver to connect through SSL. Or you might use one-way SSL
authentication so that the client (the driver itself) verifies the identity of the
server.

You provide the configuration information to the driver in the connection URL. For
more information about the syntax of the connection URL, see [Building the connection URL](jdbc20-build-connection-url.md "jdbc20-build-connection-url.md").

_SSL_ indicates TLS/SSL, both Transport Layer Security and Secure
Sockets Layer. The driver supports industry-standard versions of TLS/SSL.

## Configuring IAM

authentication

If you are connecting to a Amazon Redshift server using IAM authentication, set the
following properties as part of your data source connection string.

For more
information on IAM authentication, see [Identity and access management in
Amazon Redshift](redshift-iam-authentication-access-control.md "redshift-iam-authentication-access-control.md").

To use IAM authentication, use one of the following connection string
formats:

| Connection string                                     | Description                                                                                                                                                                                                        |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `jdbc:redshift:iam:// [host]:[port]/[db]`             | A regular connection string. The driver infers the ClusterID<br>and Region from the host.                                                                                                                          |
| `jdbc:redshift:iam:// [cluster-id]:<br>[region]/[db]` | The driver retrieves host information, given the ClusterID and<br>Region.                                                                                                                                          |
| `jdbc:redshift:iam:// [host]/[db]`                    | The driver defaults to port 5439, and infers ClusterID and<br>Region from the host. Depending on the port you selected when<br>creating, modifying or migrating the cluster, allow access to<br>the selected port. |

## Specifying profiles

If you are using IAM authentication, you can specify any additional required or
optional connection properties under a profile name. By doing this, you can avoid
putting certain information directly in the connection string. You specify the
profile name in your connection string using the Profile property.

Profiles can be added to the AWS credentials file. The default location for this
file is: `~/.aws/credentials`

You can change the default value by setting the path in the following environment
variable: `AWS_CREDENTIAL_PROFILES_FILE`

For more information about profiles, see [Working with AWS
Credentials](../../../sdk-for-java/v1/developer-guide/credentials.md "../../../sdk-for-java/v1/developer-guide/credentials.md") in the _AWS SDK for Java_.

## Using instance profile

credentials

If you are running an application on an Amazon EC2 instance that is associated with an
IAM role, you can connect using the instance profile credentials.

To do this, use one of the IAM connection string formats in the preceding table,
and set the dbuser connection property to the Amazon Redshift username that you are connecting
as.

For more information about instance profiles, see [Access Management](../../../IAM/latest/UserGuide/access.md "../../../IAM/latest/UserGuide/access.md") in the
_IAM User Guide_.

## Using credential providers

The driver also supports credential provider plugins from the following services:

- AWS IAM Identity Center
- Active Directory Federation Service (ADFS)
- JSON Web Tokens (JWT) Service
- Microsoft Azure Active Directory (AD) Service and Browser Microsoft Azure
  Active Directory (AD) Service
- Okta Service
- PingFederate Service
- Browser SAML for SAML services such as Okta, Ping, or ADFS

If you use one of these services, the connection URL needs to specify the
following properties:

- Plugin_Name – The fully-qualified
  class path for your credentials provider plugin class.
- IdP_Host: – The host for the service
  that you are using to authenticate into Amazon Redshift.
- IdP_Port – The port that the host
  for the authentication service listens at. Not required for Okta.
- User – The username for the idp_host
  server.
- Password – The password associated
  with the idp_host username.
- DbUser – The Amazon Redshift username you are
  connecting as.
- SSL_Insecure – Indicates whether the
  IDP server certificate should be verified.
- Client_ID – The client ID associated
  with the username in the Azure AD portal. Only used for Azure AD.
- Client_Secret – The client secret
  associated with the client ID in the Azure AD portal. Only used for Azure
  AD.
- IdP_Tenant – The Azure AD tenant ID
  for your Amazon Redshift application. Only used for Azure AD.
- App_ID – The Okta app ID for your
  Amazon Redshift application. Only used for Okta.
- App_Name – The optional Okta app
  name for your Amazon Redshift application. Only used for Okta.
- Partner_SPID – The optional partner
  SPID (service provider ID) value. Only used for PingFederate.
- Idc_Region – The AWS Region where
  the AWS IAM Identity Center instance is located. Only used for AWS IAM Identity Center.
- Issuer_Url – The AWS IAM Identity Center
  server's instance endpoint. Only used for AWS IAM Identity Center.

If you are using a browser plugin for one of these services, the connection URL
can also include:

- Login_URL –The URL for the resource
  on the identity provider's website when using the Security Assertion Markup
  Language (SAML) or Azure AD services through a browser plugin. This
  parameter is required if you are using a browser plugin.

- Listen_Port – The port that the
  driver uses to get the SAML response from the identity provider when using
  the SAML, Azure AD, or AWS IAM Identity Center services through a browser plugin.

- IdP_Response_Timeout – The amount of
  time, in seconds, that the driver waits for the SAML response from the
  identity provider when using the SAML, Azure AD, or AWS IAM Identity Center services
  through a browser plugin.

For information on additional connection string properties, see [Options for JDBC driver version 2.x
configuration](jdbc20-configuration-options.md "jdbc20-configuration-options.md").
