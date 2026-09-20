

# Signing an attendee in
<a name="auth-signing-in"></a>

 Sign-in is the OAuth 2.0 authorization code flow with PKCE. 

 Your application must run on the attendee's machine. It listens at `/callback` on one of six reserved loopback ports, `8484` through `8489`. Both host forms are registered for each, so nothing needs registering, and the following examples use `http://localhost:8484/callback`. `redirect_uri` is matched exactly, with no wildcards. Any other port fails for an application you build. Installed MCP clients have their own registered callbacks; see [Connecting a client](mcp-server.md#mcp-connecting). The authorization request and the token exchange must send the identical string. There is no hosted redirect URI, so you can distribute an application that signs attendees in, but it has to run locally. 

1.  Generate a PKCE code verifier from a cryptographically secure random source, 43 to 128 characters from the unreserved set, fresh for every sign-in attempt. Derive the code challenge by taking the SHA-256 digest of the verifier and encoding it as base64url with no padding. Generate a random `state` value and store it with the verifier. 

1. Redirect the attendee's browser to the authorization endpoint:

   ```
   https://oauth.awsevents.com/oauth2/authorize
     ?response_type=code
     &client_id=7vmom55m1qstvq8i71ph127bfq
     &redirect_uri=http://localhost:8484/callback
     &scope=openid+email+events/access
     &identity_provider=AWSBuilderID
     &code_challenge=$CODE_CHALLENGE
     &code_challenge_method=S256
     &state=$STATE
   ```

1.  The attendee signs in with their Builder ID. Their browser returns to your redirect URI with `code` and `state` query parameters. 

1.  Check that `state` matches what you stored, then exchange the code for tokens: 

   ```
   curl -X POST https://oauth.awsevents.com/oauth2/token \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "grant_type=authorization_code" \
     -d "client_id=7vmom55m1qstvq8i71ph127bfq" \
     -d "redirect_uri=http://localhost:8484/callback" \
     -d "code=$CODE" \
     -d "code_verifier=$CODE_VERIFIER"
   ```

**Note**  
 Send `code_challenge_method=S256` explicitly, and send the challenge base64url-encoded. A hex or standard-base64 challenge, or a verifier reused between attempts, fails the exchange with an error that does not say which value was wrong. 

 The response returns three tokens: 
+  *Access token* — a JSON Web Token (JWT) valid for 60 minutes. This is the only one you send to this API. 
+  *ID token* — describes who signed in, for your application's own use. This API does not accept it in place of the access token. 
+  *Refresh token* — opaque, valid for 30 days, and used only against the token endpoint. 