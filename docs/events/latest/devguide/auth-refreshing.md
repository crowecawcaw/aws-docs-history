

# Keeping the attendee signed in
<a name="auth-refreshing"></a>

 When the access token expires, exchange the refresh token for a new one, rather than a fresh sign-in: 

```
curl -X POST https://oauth.awsevents.com/oauth2/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=refresh_token" \
  -d "client_id=7vmom55m1qstvq8i71ph127bfq" \
  -d "refresh_token=$REFRESH_TOKEN"
```

 Schedule the next refresh against the response's `expires_in`, not a hardcoded constant. If the response carries a new refresh token, replace the one you stored. The previous one may not work again. 

 Treat a `401` as "refresh once, then retry the request." If the retry also returns `401`, the refresh token is no longer good. Start sign-in again rather than retrying in a loop. 

**Note**  
 A refresh provides a new valid access token. It does not extend the Builder ID sign-in session, which has its own lifetime. A long-running application will eventually need an interactive sign-in, however recently it refreshed. 