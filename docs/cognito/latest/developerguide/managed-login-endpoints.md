# User-interactive managed login and classic

hosted UI endpoints

Amazon Cognito activates the managed login endpoints in this section when you add a domain to
your user pool. They are webpages where your users can complete the core authentication
operations of a user pool. They include pages for password management, multi-factor
authentication (MFA), and attribute
verification.

The webpages that make up managed login are a front-end web application for
interactive user sessions with your customers. Your app must invoke managed login in
your users' browsers. Amazon Cognito doesn't support programmatic access to the webpages in this
chapter. Those federation endpoints in the [Identity provider and relying party
endpoints](federation-endpoints.md "federation-endpoints.md") that return a JSON response can be queried directly
in your app code. The [Authorize endpoint](authorization-endpoint.md "authorization-endpoint.md") redirects either to managed login or to an IdP
sign-in page and also must be opened in users' browsers.

All user pool endpoints accept traffic from IPv4 and IPv6 source IP addresses.

The topics in this guide describe frequently-used managed login and classic hosted UI
endpoints in detail. The difference between managed login and the hosted UI is visible,
not functional. Except for `/passkeys/add`, all paths are shared between the
two versions of managed login branding.

Amazon Cognito makes the webpages that follow available when you assign a domain to your user
pool.

| Managed login endpoints                                  | Endpoint URL                                                                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                        | How it's accessed |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------- |
| https://`Your user pool<br>domain`/login                 | Signs in user pool local and federated users.                                                                                                                                                                                                                                                                | Redirect from endpoints like [Authorize endpoint](authorization-endpoint.md "authorization-endpoint.md"), `/logout`, and<br>`/confirmforgotPassword`. See [Login endpoint](login-endpoint.md "login-endpoint.md"). |
| https://`Your user pool<br>domain`/logout                | Signs out user pool users.                                                                                                                                                                                                                                                                                   | Direct link. See [Logout endpoint](logout-endpoint.md "logout-endpoint.md").                                                                                                                                       |
| https://`Your user pool<br>domain`/confirmUser           | Confirms users who have selected an email link to verify their user<br>account.                                                                                                                                                                                                                              | User selected link in an email message.                                                                                                                                                                            |
| https://`Your user pool<br>domain`/signup                | Signs up a new user. The `/login` page directs your user<br>to `/signup` when they select **Sign<br>up**.                                                                                                                                                                                                    | Direct link with same parameters as<br>`/oauth2/authorize`.                                                                                                                                                        |
| https://`Your user pool<br>domain`/confirm               | After your user pool sends a confirmation code to a user who signed<br>up, prompts your user for the code.                                                                                                                                                                                                   | Redirect-only from `/signup`.                                                                                                                                                                                      |
| https://`Your user pool<br>domain`/forgotPassword        | Prompts your user for their user name and sends a password-reset<br>code. The `/login` page directs your user to<br>`/forgotPassword` when they select **Forgot your<br>password?**.                                                                                                                         | 1. From \*_Forgot password_<br>• link at<br>`/login`.<br>2. Direct link with same parameters as<br>`/oauth2/authorize`.                                                                                            |
| https://`Your user pool<br>domain`/confirmforgotPassword | Prompts your user for their password-reset code and a new password.<br>The `/forgotPassword` page directs your user to<br>`/confirmforgotPassword` when they select **Reset<br>your password**.                                                                                                              | Redirect-only from `/forgotPassword`.                                                                                                                                                                              |
| https://`Your user pool<br>domain`/resendcode            | Sends a new confirmation code to a user who has signed up in your<br>user pool.                                                                                                                                                                                                                              | Redirect-only from \*_Send a new code_<br>• link at<br>`/confirm`.                                                                                                                                                 |
| https://`Your user pool<br>domain`/passkeys/add          | Registers a new [passkey](amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-passkey "amazon-cognito-user-pools-authentication-flow-methods.md#amazon-cognito-user-pools-authentication-flow-methods-passkey"). Only available in managed login. | • In the sign-up flow after confirmation in app clients that<br>support passkey authentication.<br>• Direct link with same parameters as<br>`/oauth2/authorize`.                                                   |

###### Topics

- [The managed login sign-in endpoint:
  /login](login-endpoint.md "login-endpoint.md")
- [The managed login sign-out endpoint:
  /logout](logout-endpoint.md "logout-endpoint.md")
