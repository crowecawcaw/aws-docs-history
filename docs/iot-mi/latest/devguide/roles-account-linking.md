# Account linking roles

To create a C2C connector, you'll need an OAuth 2.0 authorization server and account
linking. For more information, see [Account linking workflow](account-linking-flow.md "account-linking-flow.md").

OAuth 2.0 defines the following four roles when implementing account linking:

1. Authorization server
2. Resource owner (End User)
3. Resource server
4. Client
   The following define each of these OAuth roles:

**Authorization Server**

The authorization server is the server that identifies and authenticates the
identity of an end user in a third-party cloud. The access tokens provided by this
server can link the AWS end user’s customer platform account and their third-party
platform account. This process is referred to as account linking.

The authorization server supports account linking by providing the
following:

- Displays a login page for the end user to log in to your system. This is
  typically referred to as an authorization endpoint.
- Authenticates the end user in your system.
- Generates an authorization code that identifies the end user.
- Passes the authorization code to managed integrations for AWS IoT Device Management.
- Accepts the authorization code from managed integrations for AWS IoT Device Management and returns an access
  token that managed integrations for AWS IoT Device Management can use to access the end user's data in your system.
  This is typically completed through a separate URI, called a token URI or
  endpoint.

###### Important

The authorization server must support the OAuth 2.0 Authorization Code flow to
be used with an managed integrations for AWS IoT Device Management Connector. managed integrations for AWS IoT Device Management also supports the
authorization code flow with [Proof Key for Code Exchange
(PKCE)](https://www.rfc-editor.org/rfc/rfc7636 "https://www.rfc-editor.org/rfc/rfc7636").

The authorization server must either:

- Issue access tokens that contain extractable end-user or resource owner ID,
  for example JWT-tokens
- Be able to return the end-user ID for each issued access token
  Otherwise, your connector will not be able to support the required
  `AWS.ActivateUser`operation. This will prevent connector usage with
  managed integrations.

If the connector developer or owner does not maintain their own authorization
server, the authorization server used must provide authorization for resources
managed by the connector developers third party platform. This means that any tokens
received by managed integrations from the authorization server must provide meaningful security
boundaries on devices (the resource). For example, an end users token does not allow
for commands on another end users device; the permissions provided by the token are
mapped to resources within the platform. Consider the _Lights
Incorporated_ example. When an end user starts the account linking flow
with their connector, they are redirected to the _Lights
Incorporated_ login page which fronts their authorization server. Once
they have logged in and granted permissions to the client, they provide a token that
gives the connector access to resources within their _Lights
Incorporated_ account.

**Resource owner (End User)**

As the resource owner, you allow an managed integrations for AWS IoT Device Management customer access to
resources associated with your account by performing account linking. For example,
consider the smart bulb an end user has onboarded to the _Lights
Incorporated_ mobile application. The resource owner refers to the end user
account that has purchased and onboarded the device. In our example the resource
owner is modeled as a _Lights Incorporated_
OAuth2.0 account. As the resource owner, this account provides permissions to issue
commands and manage the device.

**Resource server**

This is the server that hosts protected resources which require authorization to
access (device data). The AWS customer needs to access to protected resources on
behalf of an end user, and they do so through managed integrations for AWS IoT Device Management connectors post account
linking. Considering the smart bulb from before as an example, the resource server
is a cloud-based service owned by _Lights
Incorporated_ that manages the bulb after it has been onboarded. Through
the resource server, the resource owner can issue commands to the smart bulb, such
as turning it on and off. The protected resource only provides permissions to the
end user’s account and other accounts/entities they may have provided permission to.

**Client**

In this context, the client is your C2C connector. A client is defined as an
application that is granted access to resources within a resource server on behalf
of the end user. The account linking process represents the connector, the client,
requesting access to an end user’s resources within the third-party cloud.

Although the connector is the OAuth client, managed integrations for AWS IoT Device Management performs operations
on behalf of the connector. For example, managed integrations for AWS IoT Device Management makes requests to the
authorization server to get an access token. The connector is still considered the
client because it is the only component that ever accesses the protected resource
(device data) in the resource server.

Consider the smart bulb that has been onboarded by an end user. After account
linking has been completed between the customer platform and the _Lights Incorporated_ authorization server, the connector
itself will communicate with the resource server to retrieve information about the
end user's smart bulb. The connector can then receive commands from the end user. This
includes turning the light on or off on their behalf through the _Lights Incorporated_ resource server. Thus, we designate
the connector as the client.
