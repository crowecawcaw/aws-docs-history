# OAuth 2.0 grants

The Amazon Cognito user pool OAuth 2.0 authorization server issues tokens in response to three
types of OAuth 2.0 [authorization
grants](https://datatracker.ietf.org/doc/html/rfc6749#section-1.3 "https://datatracker.ietf.org/doc/html/rfc6749#section-1.3"). You can set the supported grant types for each app client in your
user pool. You can't enable _client credentials_ grants
in the same app client as either _implicit_ or
_authorization code_ grants. Requests for implicit
and authorization code grants begin at your [Authorize endpoint](authorization-endpoint.md "authorization-endpoint.md") and requests for client credentials grants start
at your [Token endpoint](token-endpoint.md "token-endpoint.md").

**Authorization code grant**

In response to your successful authentication request, the authorization
server appends an authorization code in a `code` parameter to
your callback URL. You must then exchange the code for ID, access, and
refresh tokens with the [Token endpoint](token-endpoint.md "token-endpoint.md"). To request an authorization code grant, set
`response_type` to `code` in your request. For an
example request, see [Example: authorization code
grant](authorization-endpoint.md#sample-authorization-code-grant "authorization-endpoint.md#sample-authorization-code-grant"). Amazon Cognito supports [Proof Key for Code Exchange
(PKCE)](using-pkce-in-authorization-code.md "using-pkce-in-authorization-code.md") in authorization code grants.

The authorization code grant is the most secure form of authorization
grant. It doesn't show token contents directly to your users. Instead, your
app is responsible for retrieving and securely storing your user's tokens.
In Amazon Cognito, an authorization code grant is the only way to get all three token
types—ID, access, and refresh—from the authorization server.
You can also get all three token types from authentication through the
Amazon Cognito user pools API, but the API doesn't issue access tokens with scopes other than
`aws.cognito.signin.user.admin`.

**Implicit grant**

In response to your successful authentication request, the authorization
server appends an access token in an `access_token` parameter,
and an ID token in an `id_token` parameter, to your callback URL.
An implicit grant requires no additional interaction with the [Token endpoint](token-endpoint.md "token-endpoint.md"). To request an
implicit grant, set `response_type` to `token` in your
request. The implicit grant only generates an ID and access token. For an
example request, see [Example: Token
(implicit) grant without openid scope](authorization-endpoint.md#sample-token-grant-without-openid-scope "authorization-endpoint.md#sample-token-grant-without-openid-scope").

The implicit grant is a legacy authorization grant. Unlike with the
authorization code grant, users can intercept and inspect your tokens. To
prevent token delivery through implicit grant, configure your app client to
support authorization code grant only.

**Client credentials**

Client credentials is an authorization-only grant for machine-to-machine
access. To receive a client credentials grant, bypass the [Authorize endpoint](authorization-endpoint.md "authorization-endpoint.md") and generate a request directly to the [Token endpoint](token-endpoint.md "token-endpoint.md"). Your app
client must have a client secret and support client credentials grants only.
In response to your successful request, the authorization server returns an
access token.

The access token from a client credentials grant is an authorization
mechanism that contains OAuth 2.0 scopes. Typically, the token contains
custom scope claims that authorize HTTP operations to access-protected APIs.
For more information, see [Scopes, M2M, and APIs with
resource servers](cognito-user-pools-define-resource-servers.md "cognito-user-pools-define-resource-servers.md").

Client credentials grants add costs to your AWS bill. For more
information, see [Amazon Cognito
Pricing](https://aws.amazon.com/cognito/pricing "https://aws.amazon.com/cognito/pricing").

**Refresh token**

You can request a refresh token grant directly from the [Token endpoint](token-endpoint.md "token-endpoint.md"). This grant
returns new ID and access tokens in exchange for a valid refresh
token.

For more perspective on these grants and their implementation, see How to use [OAuth 2.0 in Amazon Cognito: Learn about the different OAuth 2.0 grants](https://aws.amazon.com/blogs/security/how-to-use-oauth-2-0-in-amazon-cognito-learn-about-the-different-oauth-2-0-grants/ "https://aws.amazon.com/blogs/security/how-to-use-oauth-2-0-in-amazon-cognito-learn-about-the-different-oauth-2-0-grants/") in the
_AWS Security Blog_.
