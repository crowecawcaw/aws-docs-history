# The managed login sign-in endpoint:

`/login`

The login endpoint is an authentication server and a redirect destination from
[Authorize endpoint](authorization-endpoint.md "authorization-endpoint.md").
It's the entry point to managed login when you don't specify an identity provider.
When you generate a redirect to the login endpoint, it loads the login page and
presents the authentication options configured for the client to the user.

###### Note

The login endpoint is a component of managed login. In your app, invoke
federation and managed login pages that redirect to the login endpoint. Direct
access by users to the login endpoint isn't a best practice.

## GET /login

The `/login` endpoint only supports `HTTPS GET` for your
user's initial request. Your app invokes the page in a browser like Chrome or
Firefox. When you redirect to `/login` from the [Authorize endpoint](authorization-endpoint.md "authorization-endpoint.md"),
it passes along all the parameters that you provided in your initial request.
The login endpoint supports all the request parameters of the authorize
endpoint. You can also access the login endpoint directly. As a best practice,
originate all your users' sessions at `/oauth2/authorize`.

**Example – prompt the user to sign
in**

This example displays the login screen.

```
GET https://mydomain.auth.us-east-1.amazoncognito.com/login?
                response_type=code&
                client_id=ad398u21ijw3s9w3939&
                redirect_uri=https://YOUR_APP/redirect_uri&
                state=STATE&
                scope=openid+profile+aws.cognito.signin.user.admin

```

###### Example – response

The authentication server redirects to your app with the authorization
code and state. The server must return the code and state in the query
string parameters and not in the fragment.

```
HTTP/1.1 302 Found
                    Location: https://YOUR_APP/redirect_uri?code=AUTHORIZATION_CODE&state=STATE

```

## User-initiated sign-in request

After your user loads the `/login` endpoint, they can enter a user
name and password and choose **Sign in**. When they do this,
they generate an `HTTPS POST` request with the same header request
parameters as the `GET` request, and a request body with their
username, password, and a device fingerprint.
