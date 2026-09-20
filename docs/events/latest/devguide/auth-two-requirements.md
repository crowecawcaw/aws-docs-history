

# Access token and event registration
<a name="auth-two-requirements"></a>

 To read the catalog of an event that requires registration, or to reach your own schedule, you need both of the following. Each fails in its own way. 
+  *A valid access token.* A missing, expired, or malformed token produces `401`. The `WWW-Authenticate` header names where to sign in. 
+  *Registration for that event.* A valid token from someone not registered for the event produces `403`. One token covers every event you are registered for. The same token can succeed for one event and return `403` for another. 

 Registration happens on the event's own site. You cannot fix a `403` by signing in again. 