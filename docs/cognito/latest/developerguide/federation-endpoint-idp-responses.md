# Managed login and federation error

responses

A sign-in process in managed login or federated sign-in might return an error. The
following are some conditions that can cause authentication to end with an error.

- A user performs an operation that your user pool can't fulfill.
- A Lambda trigger doesn't respond with expected syntax.
- Your identity provider (IdP) returns an error.
- Amazon Cognito couldn't validate attribute information that your user provided.
- Your IdP didn't send claims that map to required attributes.
  When Amazon Cognito encounters an error, it communicates it in one of the following
  ways.

1. Amazon Cognito sends a redirect URL with the error in the request parameters.
2. Amazon Cognito displays an error in managed login.
   Errors that Amazon Cognito appends to request parameters have the following format.

```
https://`<Callback URL>`/?error_description=`error+description`&error=`error+name`
```

When you help your users submit error information when they can't perform an
operation, request that they capture the URL _and_ the
text or a screenshot of the page.

###### Note

Amazon Cognito error descriptions are not fixed strings and you shouldn't use logic that
relies on a fixed pattern or format.

###### OIDC and social identity provider error messages

Your identity provider might return an error. When an OIDC or OAuth 2.0 IdP
returns an error that conforms to standards, Amazon Cognito redirects your user to the
callback URL and adds the provider error response to error request parameters. Amazon Cognito
adds the provider name and HTTP error code to the existing error strings.

The following URL is an example redirect from an IdP that returned an error to
Amazon Cognito.

```
https://`www.amazon.com`/?error_description=`LoginWithAmazon`+Error+-+`400`+`invalid_request+The+request+is+missing+a+required+parameter+%3A+client_secret`&error=`invalid_request`
```

Because Amazon Cognito only returns what it receives from a provider, your user might see a
subset of this information.

When your user encounters an issue with initial sign-in through your IdP, the IdP
delivers any error messages directly to your user. Amazon Cognito relays an error message to your
user when it generates a request to your IdP to validate your user's session. Amazon Cognito
relays OAuth and OIDC IdP error messages from the following endpoints.

`/token`

Amazon Cognito exchanges an IdP authorization code for an access token.

`/.well-known/openid-configuration`

Amazon Cognito discovers the path to your issuer endpoints.

`/.well-known/jwks.json`

To verify your user's JSON Web Tokens (JWTs), Amazon Cognito discovers the JSON Web
Keys (JWKs) that your IdP uses to sign tokens.

Because Amazon Cognito doesn't initiate outbound sessions to SAML 2.0 providers that might
return HTTP errors, your users' errors during a session with a SAML 2.0 IdP don't
include this form of provider error message.
