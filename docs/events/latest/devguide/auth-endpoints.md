

# Endpoints and values
<a name="auth-endpoints"></a>

 Sign-in uses the following endpoints and values. They are the same for every caller. The client ID is public and shared. The flow is protected by Proof Key for Code Exchange (PKCE), not a client secret, so there is no secret to hold. 


**Authentication endpoints and values**  

| Item | Value | 
| --- | --- | 
| Authorization endpoint | `https://oauth.awsevents.com/oauth2/authorize` | 
| Token endpoint | `https://oauth.awsevents.com/oauth2/token` | 
| Revocation endpoint | `https://oauth.awsevents.com/oauth2/revoke` | 
| Logout endpoint | `https://oauth.awsevents.com/logout` | 
| Builder ID sign-out endpoint | `https://idp.awsevents.com/oidc/logout` | 
| Client ID | `7vmom55m1qstvq8i71ph127bfq` | 
| Scope | `openid email events/access` | 
| Identity provider | `AWSBuilderID` | 
| Access token lifetime | 60 minutes | 
| Refresh token lifetime | 30 days | 

**Note**  
 Always send `identity_provider=AWSBuilderID` on the authorization request. Without it, the attendee sees an extra page that asks which provider to use. Builder ID is the only choice. 