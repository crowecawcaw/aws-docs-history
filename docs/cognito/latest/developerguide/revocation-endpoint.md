# The token revocation endpoint

Users who hold a refresh token in their session have something similar to a
browser cookie. They can renew their existing session as long as the refresh token
is valid. Instead of prompting a user to sign in after their ID or access token
expires, your application can use the refresh token to get new, valid tokens.
However, you might externally determine that a user's session should be ended, or
the user might elect to forget their current session. At that point, you can revoke
that refresh token so that they can no longer persist their session.

The `/oauth2/revoke` endpoint revokes a user's access token that Amazon Cognito
initially issued with the refresh token that you provide. This endpoint also revokes
the refresh token itself and all subsequent access and identity tokens from the same
refresh token. After the endpoint revokes the tokens, you can't use the revoked
access tokens to access APIs that Amazon Cognito tokens authenticate.

## POST /oauth2/revoke

The `/oauth2/revoke` endpoint only supports `HTTPS
 POST`. The user pool client makes requests to this endpoint directly and
not through the system browser.

### Request parameters in

header

**`Authorization`**

If your app client has a client secret, the application must
pass its `client_id` and `client_secret`
in the authorization header through Basic HTTP authorization.
The secret is [Basic](https://en.wikipedia.org/wiki/Basic_access_authentication#Client_side "https://en.wikipedia.org/wiki/Basic_access_authentication#Client_side")
`Base64Encode(client_id:client_secret)`.

**`Content-Type`**

Must always be
`'application/x-www-form-urlencoded'`.

#### Request parameters

in body

**`token`**

(Required) The refresh token that the client wants to
revoke. The request also revokes all access tokens that
Amazon Cognito issued with this refresh token.

Required.

**`client_id`**

(Optional) The app client ID for the token that you want
to revoke.

Required if the client is public and doesn't have a
secret.

## Revocation request examples

This revocation request revokes a refresh token for an app client that has no
client secret. Note the `client_id` parameter in the request
body.

```

POST /oauth2/revoke HTTP/1.1
Host: `mydomain.auth.us-east-1.amazoncognito.com`
Accept: application/json
Content-Type: application/x-www-form-urlencoded
token=`2YotnFZFEjr1zCsicMWpAA`&
client_id=`1example23456789`
```

This revocation request revokes a refresh token for an app client that
_has_ a client secret. Note the
`Authorization` header that contains an encoded client ID and
client secret, but no `client_id` in the request body.

```

POST /oauth2/revoke HTTP/1.1
Host: `mydomain.auth.us-east-1.amazoncognito.com`
Accept: application/json
Content-Type: application/x-www-form-urlencoded
Authorization: Basic `czZCaGRSa3F0MzpnWDFmQmF0M2JW`
token=`2YotnFZFEjr1zCsicMWpAA`
```

## Revocation error response

A successful response contains an empty body. The error response is a JSON
object with an `error` field and, in some cases, an
`error_description` field.

**Endpoint errors**

- If the token isn't present in the request or if the feature is
  disabled for the app client, you receive an HTTP 400 and error
  `invalid_request`.
- If the token that Amazon Cognito sent in the revocation request isn't a refresh
  token, you receive an HTTP 400 and error
  `unsupported_token_type`.
- If the client credentials aren't valid, you receive an HTTP 401 and
  error `invalid_client`.
- If the token has been revoked or if the client submitted a token that
  isn't valid, you receive an HTTP 200 OK.
