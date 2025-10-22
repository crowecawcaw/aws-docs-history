# Single sign-on access to SAML 2.0
 and OAuth 2.0 applications

IAM Identity Center enables you to provide your users with single sign-on access to SAML 2.0 or
 OAuth 2.0 applications. The following topics provide a high-level overview of SAML
 2.0 and OAuth 2.0.

###### Topics

* [SAML 2.0](#samlfederationconcept "#samlfederationconcept")
* [OAuth 2.0](#oidc-concept "#oidc-concept")

## SAML 2.0


SAML 2.0 is an industry standard used for securely exchanging SAML assertions
 that pass information about a user between a SAML authority (called an identity
 provider or IdP), and a SAML 2.0 consumer (called a service provider or SP).
 IAM Identity Center uses this information to provide federated single sign-on access for those
 users who are authorized to use applications within the AWS access portal. 


###### Note

IAM Identity Center does not support validating signatures of incoming SAML authentication requests from SAML applications.


## OAuth 2.0


OAuth 2.0 is a protocol that allows applications to access and share user data
 securely without sharing passwords. This capability provides a secure and
 standardized way for users to allow applications access to their resources.
 Access is facilitated by different OAuth 2.0 grant flows. 


IAM Identity Center enables applications that run on public clients to retrieve temporary
 credentials to access AWS accounts and services programmatically on behalf of
 their users. Public clients are typically desktops, laptops, or other mobile
 devices that are used to run applications locally. Examples of AWS
 applications that run on public clients include the AWS Command Line Interface (AWS CLI),
 AWS Toolkit, and AWS Software Development Kits (SDKs). To enable
 these applications to obtain credentials, IAM Identity Center supports portions of the
 following OAuth 2.0 flows: 



* Authorization Code Grant with Proof Key for Code Exchange (PKCE)
 ([RFC
 6749](https://www.rfc-editor.org/rfc/rfc6749#section-4.1 "https://www.rfc-editor.org/rfc/rfc6749#section-4.1") and [RFC 7636](https://www.rfc-editor.org/rfc/rfc7636 "https://www.rfc-editor.org/rfc/rfc7636"))
* Device Authorization Grant ([RFC
 8628](https://datatracker.ietf.org/doc/html/rfc8628 "https://datatracker.ietf.org/doc/html/rfc8628"))

###### Note

These grant types can be used only with AWS services that support this
 capability. These services may not support this grant type in all
 AWS Regions. Refer to the documentation of relevant AWS services for
 regional differences. 


OpenID Connect (OIDC) is an authentication protocol that is based on the OAuth
 2.0 Framework. OIDC specifies how to use OAuth 2.0 for authentication. Through
 the [IAM Identity Center OIDC service APIs](../OIDCAPIReference/API_Operations.md "../OIDCAPIReference/API_Operations.md"), an application registers an OAuth 2.0
 client and uses one of these flows to obtain an access token that provides
 permissions to IAM Identity Center protected APIs. An application specifies [access scopes](customermanagedapps-saml2-oauth2.md#scopes-oidc "customermanagedapps-saml2-oauth2.md#scopes-oidc") to declare its intended API user. After you, as the
 IAM Identity Center administrator, configure your identity source, your application end users
 must complete a sign-in process, if they have not already done so. Your end
 users must then provide their consent to allow the application to make API
 calls. These API calls are made using the users' permissions. In response, IAM Identity Center
 returns an access token to the application that contains the access scopes to
 which the users consented.


### Using an OAuth 2.0 grant flow


OAuth 2.0 grant flows are only available through AWS managed
 applications that support the flows. To use an OAuth 2.0 flow, your instance
 of IAM Identity Center and any supported AWS managed applications that you use must be
 deployed in a single AWS Region. Refer to the documentation for each
 AWS service to determine the regional availability of AWS managed
 applications and the instance of IAM Identity Center that you want to use.


To use an application that uses an OAuth 2.0 flow, the end user must enter
 the URL where the application will connect and register with your instance
 of IAM Identity Center. Depending on the application, as the administrator, you must
 provide your users with the **AWS access portal URL** or the
 **Issuer URL** of your instance of IAM Identity Center. You can find
 these two settings on the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon/ "https://console.aws.amazon.com/singlesignon/")
**Settings** page. For additional information about
 configuring a client application, refer to that application’s
 documentation.


The end user experience for signing into an application and providing
 consent depends on whether the application uses the [Authorization Code Grant with
 PKCE](#auth-code-grant-pkce "#auth-code-grant-pkce") or
 [Device Authorization Grant](#device-auth-grant "#device-auth-grant").


#### Authorization Code Grant with
 PKCE


This flow is used by applications that run on a device that has a
 browser. 



1. A browser window opens.
2. If the user has not authenticated, the browser redirects them
 to complete user authentication.
3. After authentication, the user is presented with a consent
 screen that displays the following information:




	* The name of the application
	* The access scopes that the application is requesting
	 consent to use
4. The user can cancel the consent process or they can give their
 consent and the application proceeds with access based on the
 user’s permissions.

#### Device Authorization Grant


This flow can be used by applications that run on a device with or
 without a browser. When the application initiates the flow, the
 application presents a URL and a user code that the user must verify
 later in the flow. The user code is necessary because the application
 that initiates the flow might be running on a different device than the
 device on which the user provides consent. The code ensures that the
 user is consenting to the flow they initiated on the other
 device.


###### Note

If you have clients using
 `device.sso.`region`.amazonaws.com`,
 you must update your authorization flow to use Proof Key for Code
 Exchange (PKCE). For more information, see [Configuring
 IAM Identity Center authentication with the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html "https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html") in the
 *AWS Command Line Interface User Guide*.



1. When the flow initiates from a device with a browser, a
 browser window opens. When the flow initiates from a device
 without a browser, the user must open a browser on a different
 device and go to the URL that the application presented.
2. In either case, if the user has not authenticated, the browser
 redirects them to complete user authentication.
3. After authentication, the user is presented with a consent
 screen that displays the following information:




	* The name of the application
	* The access scopes that the application is requesting
	 consent to use
	* The user code that the application presented to the
	 user
4. The user can cancel the consent process or they can give their
 consent and the application proceeds with access based on the
 user’s permissions.

### Access scopes


A *scope* defines the access for a
 service that can be accessed through an OAuth 2.0 flow. Scopes are a way for
 the service, also called a resource server, to group permissions related to
 actions and the service resources, and they specify the coarse-grained
 operations that OAuth 2.0 clients can request. When an OAuth 2.0 client
 registers with the [IAM Identity Center OIDC service](../OIDCAPIReference/Welcome.md "../OIDCAPIReference/Welcome.md"), the client specifies the scopes to declare
 its intended actions, for which the user must provide consent.


OAuth 2.0 clients use `scope` values as defined in [section
 3.3 of OAuth 2.0 (RFC 6749)](https://www.rfc-editor.org/rfc/rfc6749.html#section-3.3 "https://www.rfc-editor.org/rfc/rfc6749.html#section-3.3") to specify what permissions are
 being requested for an access token. Clients can specify a maximum of 25
 scopes when requesting an access token. When a user provides consent during
 an Authorization Code Grant with PKCE or Device Authorization Grant flow,
 IAM Identity Center encodes the scopes into the access token it returns.


AWS adds scopes to IAM Identity Center for supported AWS services. The following
 table lists the scopes that the IAM Identity Center OIDC service supports when you
 register a public client.


#### Access scopes supported by the
 IAM Identity Center OIDC service when registering a public client




| Scope | Description | Services supported by |
| --- | --- | --- |
| `sso:account:access` | Access IAM Identity Center managed accounts and permission sets. | IAM Identity Center |
| `codewhisperer:analysis` | Enable access to Amazon Q Developer code analysis. | AWS Builder ID and IAM Identity Center |
| `codewhisperer:completions` | Enable access to Amazon Q inline code suggestions. | AWS Builder ID and IAM Identity Center |
| `codewhisperer:conversations` | Enable access to Amazon Q chat. | AWS Builder ID and IAM Identity Center |
| `codewhisperer:taskassist` | Enable access to Amazon Q Developer Agent for software development. | AWS Builder ID and IAM Identity Center |
| `codewhisperer:transformations` | Enable access to Amazon Q Developer Agent for code transformation. | AWS Builder ID and IAM Identity Center |
| `codecatalyst:read_write` | Read and write to your Amazon CodeCatalyst resources, allowing access to all your existing resources. | AWS Builder ID and IAM Identity Center |
| `verified_access:application:connect` | Enable AWS Verified Access | AWS Verified Access |
| `redshift:connect` | Connect to Amazon Redshift | Amazon Redshift |
| `datazone:domain:access` | Access your DataZone Domain Execution Role | Amazon DataZone |
| `nosqlworkbench:datamodeladviser` | Create and read data models | NoSQL Workbench |
| `transform:read_write` | Enable access to AWS Transform Agent for code transformation | AWS Transform |
