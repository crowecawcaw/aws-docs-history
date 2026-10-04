

# The managed login sign-in endpoint: `/login`
<a name="login-endpoint"></a>

The login endpoint is an authentication server and a redirect destination from [Authorize endpoint](authorization-endpoint.md). It's the entry point to managed login when you don't specify an identity provider. When you generate a redirect to the login endpoint, it loads the login page and presents the authentication options configured for the client to the user.

**Note**  
The login endpoint is a component of managed login. In your app, invoke federation and managed login pages that redirect to the login endpoint. Direct access by users to the login endpoint isn't a best practice.

## GET /login
<a name="get-login"></a>

The `/login` endpoint only supports `HTTPS GET` for your user's initial request. Your app invokes the page in a browser like Chrome or Firefox. When you redirect to `/login` from the [Authorize endpoint](authorization-endpoint.md), it passes along all the parameters that you provided in your initial request. The login endpoint supports all the request parameters of the authorize endpoint. You can also access the login endpoint directly. As a best practice, originate all your users' sessions at `/oauth2/authorize`.

**Example – prompt the user to sign in**

This example displays the login screen.

```
GET https://mydomain.auth.us-east-1.amazoncognito.com/login?
                response_type=code&
                client_id=1example23456789&
                redirect_uri=https://YOUR_APP/redirect_uri&
                state=STATE&
                scope=openid+profile+aws.cognito.signin.user.admin
```

**Example – response**  
The authentication server redirects to your app with the authorization code and state. The server must return the code and state in the query string parameters and not in the fragment.

```
HTTP/1.1 302 Found
                    Location: https://YOUR_APP/redirect_uri?code=AUTHORIZATION_CODE&state=STATE
```

## User-initiated sign-in request
<a name="post-login"></a>

After your user loads the `/login` endpoint, they can enter a user name and password and choose **Sign in**. When they do this, they generate an `HTTPS POST` request with the same header request parameters as the `GET` request, and a request body with their username, password, and a device fingerprint.

## Step-up authentication request
<a name="login-endpoint-step-up"></a>

The `/login` endpoint accepts the following URL parameters for step-up authentication. These parameters have the same behavior as on the [authorize endpoint](authorization-endpoint.md#authorization-endpoint-step-up). For more information about ACR levels and AMR values, see [Authentication levels with ACR and AMR claims](cognito-user-pools-step-up-authentication.md).

`acr_values`  
A space-separated, URL-encoded list of target ACR authentication level URIs, from highest to lowest. Amazon Cognito evaluates the list from left to right, enforces the first valid level that the user can satisfy, and ignores values that it doesn't recognize. This parameter behaves the same as the `TARGET_ACR_VALUES` API parameter. Requires the Essentials or Plus feature plan.

`max_age`  
A non-negative integer that specifies the maximum number of seconds since the user last authenticated. If the current time minus `auth_time` is greater than `max_age`, the user must authenticate again from scratch instead of only stepping up. This behavior is identical to the `MAX_AGE` API parameter.

For an example request that uses these parameters, see the [authorize endpoint](authorization-endpoint.md#authorization-endpoint-step-up).

Combine `acr_values` with `max_age` to require a specific authentication level with recent authentication for a sensitive operation.

The behavior on an insufficient feature plan differs from the API. The managed login `/login` endpoint silently ignores `acr_values` and proceeds with normal authentication, without an error. The API returns a `FeatureUnavailableInTierException`. For more information, see [Feature plan requirements](cognito-user-pools-step-up-authentication.md#cognito-user-pools-step-up-authentication-tiers).