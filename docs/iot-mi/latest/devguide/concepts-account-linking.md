# OAuth 2.0 requirements for account linking

Every C2C connector relies on an OAuth 2.0 authorization server to authenticate end
users. Through this server, end users link their third-party accounts with the
customer's device platform. Account linking is the first step required by an end user to use
devices supported by your C2C connector. For more information on the different roles in
account linking and OAuth 2.0, see [Account linking roles](roles-account-linking.md "roles-account-linking.md").

While your C2C connector does not need to implement specific business logic to support
the authorization flow, the OAuth2.0 authorization server associated with your
C2C connector must meet the [OAuth configuration requirements](#oauth-config-requirements "#oauth-config-requirements").

###### Note

Managed integrations for AWS IoT Device Management only supports OAuth 2.0 with an authorization code flow. See [RFC
6749](https://datatracker.ietf.org/doc/html/rfc6749#section-1.3.1 "https://datatracker.ietf.org/doc/html/rfc6749#section-1.3.1") for more information.

Account linking is a process that allows managed integrations and the connector to access an end user’s devices by
using an access token. This token provides managed integrations for AWS IoT Device Management with the end user’s permission,
such that the connector can interact with the end user’s data through API calls. For more information, see [Account linking workflow](account-linking-flow.md "account-linking-flow.md").

We recommend that you don't log these sensitive tokens in any logs. If however they are stored in logs, we recommend that you use
CloudWatch Logs data protection policies to mask the tokens in the logs. For more information, see
[Help protect sensitive log data with masking](../../../AmazonCloudWatch/latest/logs/mask-sensitive-log-data.md "../../../AmazonCloudWatch/latest/logs/mask-sensitive-log-data.md").

Managed integrations for AWS IoT Device Management does not get an access token directly; it does so through the
Authorization Code Grant Type. First, managed integrations for AWS IoT Device Management must obtain an authorization code. It
then exchanges the code for an access token and refresh token. The refresh token is used to
request a new access token when the old access token expires. If both the access token and
refresh token are expired, you must perform the account-linking flow
again. You can do this with the `StartAccountAssociationRefresh` API operation.

###### Important

Issued access token must be scoped per user, but not per the OAuth client. The token
should not provide access to all devices of all users under the client.

The authorization server must do one of the following:

- Issue access tokens that contain extractable end-user (resource owner) ID, such as
  a JWT-token.
- Return the end-user ID for each issued access token.

## OAuth configuration requirements

The following table illustrates the required parameters from your OAuth authorization
server for managed integrations for AWS IoT Device Management to perform [account linking](account-linking-flow.md "account-linking-flow.md"):

OAuth Server Parameters| **Field** | **Required** | **Comment** |
| `clientId` | Yes | A public identifier for your application. It's used to initiate authentication flows and can be shared publicly. |
| `clientSecret` | Yes | A secret key used to authenticate the application with the authorization server, especially when exchanging an authorization code<br>for an access token. It should be kept confidential and not shared publicly. |
| `authorizationType` | Yes | The type of authorization supported by this authorization configuration.<br>Currently, "OAuth 2.0" is the only value supported. |
| `authUrl` | Yes | The authorization URL for the third-party cloud provider. |
| `tokenUrl` | Yes | The token URL for the third-party cloud provider. |
| `tokenEndpointAuthenticationScheme` | Yes | Authentication scheme of either “HTTP_BASIC” or “REQUEST_BODY_CREDENTIALS”.<br>HTTP_BASIC signals that the client credentials are included in the authorization<br>header, while the ladder signals they are included in the request body. |

The OAuth server that you use must be configured so that access token string values must be Base64 encoded with the UTF-8 character set.
