

# Handling tokens safely
<a name="auth-handling-tokens"></a>
+  Send the access token only to `https://api.awsevents.com`. If you send it elsewhere, you disclose it to that party. 
+  Do not log tokens, put them in URLs, or store them where other code on the device can read them. A token identifies one attendee. Anything holding it can act on that attendee's schedule. 
+  In a browser application, keep both tokens in memory only. To survive a page reload, run the authorization request again rather than storing a token. 
+  Elsewhere, use the operating system keychain or a file only the user can read. Keep server-side tokens server side. Treat the refresh token as the more sensitive of the two. It can mint new access tokens long after the original expired. 