

# Signing an attendee out
<a name="auth-signing-out"></a>

 Discarding your copy of the tokens is not a sign-out. Three pieces of state are involved: your tokens, the AWS Builder ID browser session, and the session that brokers it. A complete sign-out clears all three. 

1. Revoke the refresh token, then delete both tokens from wherever you keep them:

   ```
   curl -X POST https://oauth.awsevents.com/oauth2/revoke \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "client_id=7vmom55m1qstvq8i71ph127bfq" \
     -d "token=$REFRESH_TOKEN"
   ```

    Revoking stops the refresh token and any new access token it can mint. It does not invalidate an access token already issued. That token is accepted until it expires, so discard every copy your application holds. 

1.  End both browser sessions. Build the URL in two parts. The inner URL ends the brokering session and returns to your application: 

   ```
   https://oauth.awsevents.com/logout
     ?client_id=7vmom55m1qstvq8i71ph127bfq
     &logout_uri=http://localhost:8484/logout
   ```

    Percent-encode that whole URL as the `redirect_uri` value on the Builder ID sign-out endpoint, and send the attendee there: 

   ```
   https://idp.awsevents.com/oidc/logout?redirect_uri={{encoded-url}}
   ```

    That one navigation clears both sessions and lands back on your application. The Builder ID endpoint has to come first: it accepts a redirect back to the sign-in domain, not to your application. `logout_uri` is exact-matched like `redirect_uri`, but against a separate list of sign-out URLs — `/logout` on the same reserved ports, in both host forms. 

**Important**  
 Both endpoints are required. Skip the Builder ID one and the attendee appears to sign out, then is signed straight back in without a prompt. You cannot force a prompt instead: `prompt=login` and `max_age=0` are dropped from authorization requests. It does not reproduce unless you test sign-out and sign-in in the same browser. 

 Offer both steps separately. Clearing your own tokens signs the attendee out of your application. The second step also ends their AWS Builder ID session in that browser, which is not always what they want. 

**Note**  
 An attendee can also end the Builder ID session themselves at `https://profile.aws.amazon.com`, which offers signing out of the current browser or signing out everywhere. Point them there when your application cannot drive the redirect chain, such as from a command line tool. 