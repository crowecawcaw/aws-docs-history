# Common Amazon Cognito terms and concepts

Amazon Cognito provides credentials for web and mobile apps. It draws from and builds on terms that
are common in _identity and access management_. Many guides to
universal identity and access terms are available. Some examples are:

- [Terminology](https://bok.idpro.org/article/id/41/ "https://bok.idpro.org/article/id/41/") in the IDPro Body
  of Knowledge
- [AWS Identity Services](https://aws.amazon.com/identity/ "https://aws.amazon.com/identity/")
- [Glossary](https://csrc.nist.gov/glossary "https://csrc.nist.gov/glossary") from NIST CSRC
  The following lists describe terms that are unique to Amazon Cognito or have a specific context in
  Amazon Cognito.

###### Topics

- [General](#cognito-terms-general "#cognito-terms-general")
- [User pools](#cognito-terms-user-pools "#cognito-terms-user-pools")
- [Identity pools](#cognito-terms-identity-pools "#cognito-terms-identity-pools")

## General

The terms in this list aren't specific to Amazon Cognito and are widely recognized among identity
and access management practitioners. The following isn't an exhaustive list of terms, but a
guide to their specific Amazon Cognito context in this guide.

**Access token**

A JSON web token (JWT) that contains information about an entity's [authorization](#terms-authorization "#terms-authorization") to access information
systems.

**App, application**

Typically, a mobile application. In this guide, _app_ is often a shorthand for a web application or mobile app that connects
to Amazon Cognito.

**Attribute-based access control (ABAC)**

A model where an app determines access to resources based on the properties of a
user, like their job title or department. Amazon Cognito tools to enforce ABAC include ID tokens
in user pools and [principal tags](#term-afac "#term-afac") in identity
pools.

**Authentication**

The process of establishing an authentic identity for the purpose of access to an
information system. Amazon Cognito accepts proof of authentication from third-party identity
providers, and also serves as a provider of authentication to software
applications.

**Authorization**

The process of granting permissions to a resource. User pool [access tokens](#terms-accesstoken "#terms-accesstoken") contain information that applications
can use to permit users and systems to access resources.

**Authorization server**

An OAuth or OpenID Connect (OIDC) system that generates [JSON web tokens](#terms-jwt "#terms-jwt"). The Amazon Cognito user pools [managed authorization server](#terms-managedauthorizationserver "#terms-managedauthorizationserver") is the authorization-server component of the two
authentication and authorization methods in user pools. User pools also support API
challenge-response flows in [SDK
authentication](#terms-upapi "#terms-upapi").

**Confidential app, server-side app**

An application that users connect to remotely, with code on an application server
and access to secrets. This is typically a web application.

**Identity provider (IdP)**

A service that stores and verifies user identities. Amazon Cognito can request authentication
from [external providers](#terms-externalprovider "#terms-externalprovider") and be an IdP to
apps.

**JSON web token (JWT)**

A JSON-formatted document that contains claims about an authenticated user. ID
tokens authenticate users, access tokens authorize users, and refresh tokens update
credentials. Amazon Cognito receives tokens from [external
providers](#terms-externalprovider "#terms-externalprovider") and issues tokens to apps or AWS STS.

**Machine-to-machine (M2M) authorization**

The process of authorizing requests to API endpoints for non-user-interactive
machine entities, like a webserver application tier. User pools serve M2M authorization
in client-credentials grants with OAuth 2.0 scopes in [access tokens](#terms-accesstoken "#terms-accesstoken").

**Multi-factor authentication (MFA)**

The requirement that users provide additional authentication after providing their
username and password. Amazon Cognito user pools have MFA features for [local users](#terms-localuser "#terms-localuser").

**OAuth 2.0 (social) provider**

An IdP to a user pool or identity pool that provides [JWT](#terms-jwt "#terms-jwt") access and refresh tokens. Amazon Cognito user pools automate interactions with
social providers after users authenticate.

**OpenID Connect (OIDC) provider**

An IdP to a user pool or identity pool that extends the [OAuth](#terms-oauth "#terms-oauth") specification to provide ID tokens. Amazon Cognito user pools automate
interactions with OIDC providers after users authenticate.

**Passkey, WebAuthn**

A form of authentication where cryptographic keys, or passkeys, on a user's device
provides their proof of authentication. Users verify that they are present with
biometric or PIN code mechanisms in a hardware or software authenticator. Passkeys are
phishing-resistent and bound to specific websites/apps, offering a secure passwordless
experience. Amazon Cognito user pools support sign-in with passkeys.

**Passwordless**

A form of authentication where a user doesn't have to enter a password. Methods of
passwordless sign-in include one-time passwords (OTPs) sent to email addresses and phone
numbers, and passkeys. Amazon Cognito user pools support sign-in with OTPs and passkeys.

**Public app**

An application that is self-contained on a device, with code stored locally and no
access to secrets. This is typically a mobile app.

**Resource server**

An API with access control. Amazon Cognito user pools also use _resource
server_ to describe the component that defines the configuration for
interacting with an API.

**Role-based access control (RBAC)**

A model that grants access based on a user's functional designation. Amazon Cognito identity
pools implement RBAC with differentiation between IAM roles.

**Service provider (SP), relying party (RP)**

An application that relies on an IdP to assert that users are trustworthy. Amazon Cognito
acts as an SP to external IdPs, and as an IdP to app-based SPs.

**SAML provider**

An IdP to a user pool or identity pool that generates digitally signed assertion
documents that your user passes to Amazon Cognito.

**Universally Unique Identifier (UUID)**

A 128-bit label that is applied to an object. Amazon Cognito UUIDs are unique per user pool
or identity pool, but don't conform to a specific UUID format.

**User directory**

A collection of users and their attributes that serves that information to other
systems. Amazon Cognito user pools are user directories, and also tools for consolidation of users from
external user directories.

## User pools

When you see the terms in the following list in this guide, they refer to a specific
feature or configuration of user pools.

**Adaptive authentication**

A feature of [advanced security](#term-advancedsecurity "#term-advancedsecurity") that
detects potential malicious activity and applies additional security to [user profiles](#terms-userprofile "#terms-userprofile").

**App client**

A component that defines the settings for a user pool as an IdP to one app.

**Callback URL, redirect URI, return URL**

A setting in an [app client](#term-appclient "#term-appclient") and a parameter in
requests to the user pool's [authorization server](#terms-managedauthorizationserver "#terms-managedauthorizationserver"). The callback URL is the initial destination for
authenticated users in your [app](#term-app "#term-app").

**Choice-based authentication**

A form of API authentication with users pools where each user has a set of choices
for sign-in available to them. Their choices might include username and password with or
without MFA, passkey sign-in, or passwordless sign-in with email or SMS message one-time
passwords. Your application can shape the choice process for users by requesting a list
of authentication options or by declaring a preferred option.

Compare with [client-based
authentication](#terms-declarativeauthentication "#terms-declarativeauthentication").

**Client-based authentication**

A form of authentication with the user pools API and application back ends built
with AWS SDKs. In declarative authentication, your application determines
independently the login type that a user should perform and requests that type up
front.

Compare with [choice-based
authentication](#terms-choicebasedauthentication "#terms-choicebasedauthentication").

**Compromised credentials**

A feature of [advanced security](#term-advancedsecurity "#term-advancedsecurity") that
detects user passwords that attackers might know, and applies additional security to
[user profiles](#terms-userprofile "#terms-userprofile").

**Confirmation**

The process that determines that the prerequisites have been met to permit a new
user to sign in. Confirmation is typically done through email address or phone number
[verification](#terms-verification "#terms-verification").

**Custom authentication**

An extension of authentication processes with [Lambda
triggers](#terms-triggers "#terms-triggers") that define additional user challenges and responses.

**Device authentication**

An authentication process that replaces [MFA](#terms-mfa "#terms-mfa") with
sign-in that uses the ID of a trusted device.

**Domain, user pool domain**

A web domain that hosts your [managed login
pages](#terms-managedlogin "#terms-managedlogin") in AWS. You can set up DNS in a domain that you own or use an
identifying subdomain prefix in a domain that AWS owns.

**Essentials plan**

The [feature plan](#terms-featureplan "#terms-featureplan") with the latest
developments in user pools. The Essentials plan doesn't include the automated-learning
security features in the [Plus plan](#terms-plusplan "#terms-plusplan").

**External provider, third-party provider**

An IdP that has a trust relationship with a user pool. User pools serve as an
intermediate entity between external providers and your application, managing
authentication processes with SAML 2.0, OIDC, and social providers. User pools
consolidate external-provider authentication outcomes into a single IdP so that your
applications can process many users with a single OIDC relying-party library.

**Feature plan**

The group of features that you can select for a user pool. Feature plans have
differing costs in your AWS bill. New user pools default to the [Essentials plan](#terms-essentialsplan "#terms-essentialsplan").

###### Current plans

- [Lite plan](#terms-liteplan "#terms-liteplan")
- [Essentials plan](#terms-essentialsplan "#terms-essentialsplan")
- [Plus plan](#terms-plusplan "#terms-plusplan")

**Federated user, external user**

A user in a user pool who was authenticated by an [external provider](#terms-externalprovider "#terms-externalprovider").

**Hosted UI (classic), hosted UI pages**

The early version of the authentication front end, relying party, and identity
provider services on your user pool domain. The hosted UI has a basic set of features
and a simplified look and feel. You can apply Hosted UI branding with the upload of a
logo-image file and a file with a predetermined set of CSS styles. Compare to [managed login](#terms-managedlogin "#terms-managedlogin").

**Lambda trigger**

A function in AWS Lambda that a user pool can automatically invoke at key points in
user authentication processes. You can use Lambda triggers to customize authentication
outcomes.

**Local user**

A [user profile](#terms-userprofile "#terms-userprofile") in the user pool [user directory](#terms-userdirectory "#terms-userdirectory") that wasn't created by
authentication with an [external
provider](#terms-externalprovider "#terms-externalprovider").

**Linked user**

A user from an [external provider](#terms-externalprovider "#terms-externalprovider") whose
identity is merged with a [local user](#terms-localuser "#terms-localuser").

**Lite plan**

The [feature plan](#terms-featureplan "#terms-featureplan") with the features that
originally launched with user pools. The Lite plan doesn't include the new features in
the [Essentials plan](#terms-essentialsplan "#terms-essentialsplan") or the
automated-learning security features in the [Plus
plan](#terms-plusplan "#terms-plusplan").

**Managed authorization server, hosted UI authorization server, authorization
server**

A component of [managed login](#terms-managedlogin "#terms-managedlogin")
that hosts services for interaction with IdPs and apps on your [user pool domain](#terms-domain "#terms-domain"). The [hosted UI](#terms-hostedui "#terms-hostedui") differs from managed login in the user-interactive features it
offers, but has the same authorization-server capabilities.

**Managed login, managed login pages**

A set of webpages on your [user pool domain](#terms-domain "#terms-domain") that
host services for user authentication. These services include functions for operating as
an [IdP](#terms-idp "#terms-idp"), a [relying
party](#terms-relyingparty "#terms-relyingparty") for third-party IdPs, and a server of a user-interactive authentication
UI. When you set up a domain for your user pool, Amazon Cognito brings all managed login pages
online.

Your application import OIDC libraries that invoke users' browsers and direct them
to the managed login UI for sign-up, sign-in, password management, and other
authentication operations. After authentication, the OIDC libraries can process the
outcome of the authentication request.

**Managed login authentication**

Sign-in with the services on your [user pool
domain](#terms-domain "#terms-domain"), done with user-interactive browser pages or HTTPS API requests.
Applications handle managed login authentication with OpenID Connect (OIDC) libraries.
This process includes sign-in with [external
providers](#terms-externalprovider "#terms-externalprovider"), local-user sign-in with interactive managed login pages, and [M2M authorization](#terms-m2m "#terms-m2m"). Authentication with the classic [hosted UI](#terms-hostedui "#terms-hostedui") also fall under this term.

Compare to [AWS SDK authentication](#terms-upapi "#terms-upapi").

**Plus plan**

The [feature plan](#terms-featureplan "#terms-featureplan") with the latest
developments and advanced security features in user pools.

**SDK authentication, AWS SDK authentication**

A set of authentication and authorization API operations that you can add to your
application back end with an AWS SDK. This authentication model requires your own
custom-built login mechanism. The API can sign in [local
users](#terms-localuser "#terms-localuser") and [linked users](#terms-linkeduser "#terms-linkeduser").

Compare to [managed login
authentication](#terms-managedloginauthentication "#terms-managedloginauthentication").

**Threat protection, advanced security features**

In user pools, threat protection refers to technologies that are designed to
mitigate threats to your authentication and authorization mechanisms. Adaptive
authentication, compromised-credentials detection, and IP address blocklists are under
the category of threat protection.

**Token customization**

The outcome of a pre token generation [Lambda
trigger](#terms-triggers "#terms-triggers") that modifies a user's ID or access token at runtime.

**User pool, Amazon Cognito identity provider, `cognito-idp`, Amazon Cognito user pools**

An AWS resource with authentication and authorization services for applications
that work with OIDC IdPs.

**Verification**

The process of confirming that a user owns an email address or phone number. A user
pool sends a code to a user who has entered a new email address or phone number. When
they submit the code to Amazon Cognito, they verify their ownership of the message destination
and can receive additional messages from the user pool. Also, see [confirmation](#terms-confirmation "#terms-confirmation").

**User profile, user account**

An entry for a user in the [user
directory](#terms-userdirectory "#terms-userdirectory"). All users, including those from third-party IdPs, have a profile in
their user pool.

## Identity pools

When you see the terms in the following list in this guide, they refer to a specific
feature or configuration of identity pools.

**Attributes for access control**

An implementation of [attribute-based access
control](#terms-abac "#terms-abac") in identity pools. Identity pools apply user attributes as tags to user
credentials.

**Basic (classic) authentication**

An authentication process where you can customize the request for [user credentials](#terms-usercredentials "#terms-usercredentials").

**Developer authenticated identities**

An authentication process that authorizes identity pool [user credentials](#terms-usercredentials "#terms-usercredentials") with [developer credentials](#terms-developercredentials "#terms-developercredentials").

**Developer credentials**

The IAM API keys of an identity pool administrator.

**Enhanced authentication**

An authentication flow that selects an IAM role and applies principal tags
according to the logic that you define in your identity pool.

**Identity**

A [UUID](#terms-uuid "#terms-uuid") that links an app user and their [user credentials](#terms-usercredentials "#terms-usercredentials") to their profile in an
external [user directory](#terms-userdirectory "#terms-userdirectory") that has a trust
relationship with an identity pool.

**Identity pool, Amazon Cognito federated identities, Amazon Cognito identity,
`cognito-identity`**

An AWS resource with authentication and authorization services for applications
that use [temporary AWS
credentials](#terms-usercredentials "#terms-usercredentials").

**Unauthenticated identity**

A user who has not signed in with an identity pool IdP. You can permit users to
generate limited user credentials for a single IAM role before they
authentication.

**User credentials**

Temporary AWS API keys that users receive after identity pool
authentication.
