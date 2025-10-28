# Working with user devices in your

user pool

When you sign in local user pool users with the Amazon Cognito user pools API, you can associate your users’
activity logs from [threat
protection](cognito-user-pool-settings-threat-protection.md "cognito-user-pool-settings-threat-protection.md") with each of their devices and, optionally, allow your users to skip
multi-factor authentication (MFA) if they’re on a trusted device. Amazon Cognito includes a device key in
the response to any sign-in that doesn’t already include device information. The device key is
in the format ``Region`_`UUID``.
With a device key, a Secure Remote Password (SRP) library, and a user pool that permits device
authentication, you can prompt users in your app to trust the current device and no longer
prompt for an MFA code at sign-in.

###### Topics

- [Setting up
  remembered devices](#amazon-cognito-user-pools-setting-up-remembered-devices "#amazon-cognito-user-pools-setting-up-remembered-devices")
- [Getting a device
  key](#user-pools-remembered-devices-getting-a-device-key "#user-pools-remembered-devices-getting-a-device-key")
- [Signing in with a
  device](#user-pools-remembered-devices-signing-in-with-a-device "#user-pools-remembered-devices-signing-in-with-a-device")
- [Viewing, updating
  and forgetting devices](#user-pools-remembered-devices-viewing-updating-forgetting "#user-pools-remembered-devices-viewing-updating-forgetting")

## Setting up

remembered devices

With Amazon Cognito user pools, you can associate each of your users' devices with a unique device
identifier: a device key. When you present the device key and perform device authentication at
sign-in, you can configure your application with a _trusted
device_ authentication flow. In this flow, your application can present a choice
to users to sign in without MFA until a later time, as determined by the security requirements
of your app or the preferences of your users. At the end of that time period, your application
must change the device status to _not remembered_ and the
user must sign in with MFA until they confirm that they want to remember a device. For
example, your application might prompt your users to trust a device for 30, 60, or 90 days.
You can store this date in a custom attribute and on that date, change the remembered status
of their device. You must then re-prompt your user to submit an MFA code and set the device to
be remembered again after successful authentication.

1. Remembered devices can override MFA only in user pools with MFA active.

When your user signs in with a remembered device, you must perform an additional device
authentication during their authentication flow. For more information, see [Signing in with a
device](#user-pools-remembered-devices-signing-in-with-a-device "#user-pools-remembered-devices-signing-in-with-a-device").

Configure your user pool to remember devices in the **Sign-in** menu of
your user pool, under **Device tracking**. When setting up the remembered
devices functionality through the Amazon Cognito console, you have three options:
**Always**, **User Opt-In**, and
**No**.

**Don't remember**

Your user pool doesn't prompt users to remember devices when they sign in.

**Always remember**

When your app confirms a user's device, your user pool always remembers the device
and doesn't return MFA challenges on future successful device sign-ins.

**User opt-in**

When your app confirms a user's device, your user pool doesn't automatically
suppress MFA challenges. You must prompt your user to choose whether they want to
remember the device.

When you choose **Always remember** or **User Opt-In**,
Amazon Cognito generates a device-identifier key and secret every time a user signs in from an
unidentified device. The device key is the initial identifier that your app sends to your user
pool when your user performs device authentication.

With each confirmed user device, whether remembered automatically or opted-in, you can use
the device-identifier key and secret to authenticate a device on every user sign-in.

You can also configure remembered-device settings for your user pool in a [CreateUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md "../../../cognito-user-identity-pools/latest/APIReference/API_CreateUserPool.md") or [UpdateUserPool](../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.md "../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.md") API request. For more information, see the [DeviceConfiguration](../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.md#CognitoUserPools-UpdateUserPool-request-DeviceConfiguration "../../../cognito-user-identity-pools/latest/APIReference/API_UpdateUserPool.md#CognitoUserPools-UpdateUserPool-request-DeviceConfiguration") property.

The Amazon Cognito user pools API has additional operations for remembered devices.

1. [ListDevices](../../../cognito-user-identity-pools/latest/APIReference/API_ListDevices.md "../../../cognito-user-identity-pools/latest/APIReference/API_ListDevices.md") and [AdminListDevices](../../../cognito-user-identity-pools/latest/APIReference/API_AdminListDevices.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminListDevices.md") return a list of the device keys and their metadata for a
   user.
2. [GetDevice](../../../cognito-user-identity-pools/latest/APIReference/API_GetDevice.md "../../../cognito-user-identity-pools/latest/APIReference/API_GetDevice.md") and [AdminGetDevice](../../../cognito-user-identity-pools/latest/APIReference/API_AdminGetDevice.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminGetDevice.md") return the device key and metadata for a single device.
3. [UpdateDeviceStatus](../../../cognito-user-identity-pools/latest/APIReference/API_UpdateDeviceStatus.md "../../../cognito-user-identity-pools/latest/APIReference/API_UpdateDeviceStatus.md") and [AdminUpdateDeviceStatus](../../../cognito-user-identity-pools/latest/APIReference/API_AdminUpdateDeviceStatus.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminUpdateDeviceStatus.md") set a user's device as remembered
   or not remembered.
4. [ForgetDevice](../../../cognito-user-identity-pools/latest/APIReference/API_ForgetDevice.md "../../../cognito-user-identity-pools/latest/APIReference/API_ForgetDevice.md") and [AdminForgetDevice](../../../cognito-user-identity-pools/latest/APIReference/API_AdminForgetDevice.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminForgetDevice.md") remove a user's confirmed device from
   their profile.

API operations with names that begin with `Admin` are for use in server-side
apps and must be authorized with IAM credentials. For more information, see [Understanding API, OIDC, and managed login pages
authentication](authentication-flows-public-server-side.md#user-pools-API-operations "authentication-flows-public-server-side.md#user-pools-API-operations").

## Getting a device

key

Any time that your user signs in with the user pools API and doesn’t include a device key
in the authentication parameters as `DEVICE_KEY`, Amazon Cognito returns a new device key in
the response. In your public client-side app, place the device key in app storage so that you
can include it in future requests. In your confidential server-side app, set a browser cookie
or another client-side token with your user’s device key.

Before your user can sign in with their trusted device, your app must confirm the device
key and provide additional information. Generate a [ConfirmDevice](../../../cognito-user-identity-pools/latest/APIReference/API_ConfirmDevice.md "../../../cognito-user-identity-pools/latest/APIReference/API_ConfirmDevice.md") request to Amazon Cognito that confirms your user’s device with the device
key, a friendly name, password verifier, and a salt. If you configured your user pool for
opt-in device authentication, Amazon Cognito responds to your `ConfirmDevice` request with a
prompt that your user must choose whether to remember the current device. Respond with your
user’s selection in an [UpdateDeviceStatus](../../../cognito-user-identity-pools/latest/APIReference/API_UpdateDeviceStatus.md "../../../cognito-user-identity-pools/latest/APIReference/API_UpdateDeviceStatus.md") request.

When you confirm your user’s device but don’t set it as remembered, Amazon Cognito stores the
association but proceeds with non-device sign-in when you provide the device key. Devices can
generate logs that are useful for user security and troubleshooting. A confirmed but
unremembered device doesn’t take advantage of the sign-in feature, but does take advantage of
the security monitoring logs feature. When you activate threat protection for your
app client and encode a device fingerprint into your request, Amazon Cognito associates user events with
the confirmed device.

###### To get a new device key

1. Start your user’s sign-in session with an [InitiateAuth](../../../cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.md "../../../cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.md") API request.
2. Respond to all authentication challenges with [RespondToAuthChallenge](../../../cognito-user-identity-pools/latest/APIReference/API_RespondToAuthChallenge.md "../../../cognito-user-identity-pools/latest/APIReference/API_RespondToAuthChallenge.md") until you receive JSON web tokens (JWTs) that mark your
   user’s sign-in session complete.
3. In your app, record the values that Amazon Cognito returns in `NewDeviceMetadata` in
   its `RespondToAuthChallenge` or `InitiateAuth` response:
   `DeviceGroupKey` and `DeviceKey`.
4. Generate a new SRP secret for your user: a salt and a password verifier. This function
   is available in SDKs that provide SRP libraries.
5. Prompt your user for a device name, or generate one from your user’s device
   characteristics.
6. Provide your user’s access token, device key, device name, and SRP secret in a [ConfirmDevice](../../../cognito-user-identity-pools/latest/APIReference/API_ConfirmDevice.md "../../../cognito-user-identity-pools/latest/APIReference/API_ConfirmDevice.md") API request. If your user pool is set to **Always
   remember** devices, your user’s registration is complete.
7. If Amazon Cognito responded to `ConfirmDevice` with
   `"UserConfirmationNecessary": true`, prompt your user to choose if they would
   like to remember the device. If they affirm that they want to remember the device,
   generate an [UpdateDeviceStatus](../../../cognito-user-identity-pools/latest/APIReference/API_UpdateDeviceStatus.md "../../../cognito-user-identity-pools/latest/APIReference/API_UpdateDeviceStatus.md") API request with your user’s access token, device key, and
   `"DeviceRememberedStatus": "remembered"`.
8. If you have instructed Amazon Cognito to remember the device, the next time they sign in,
   instead of an MFA challenge, they’re presented with a `DEVICE_SRP_AUTH`
   challenge.

## Signing in with a

device

After you configure a user’s device to be remembered, Amazon Cognito no longer requires them to
submit an MFA code when they sign in with the same device key. Device authentication only
replaces the MFA-authentication challenge with a device-authentication challenge. You can’t
sign users in with device authentication only. Your user must first complete authentication
with their password or a custom challenge. The following is the authentication process for a
user on a remembered device.

To perform device authentication in a flow that uses [Custom authentication
challenge Lambda triggers](user-pool-lambda-challenge.md "user-pool-lambda-challenge.md"), pass a `DEVICE_KEY` parameter in your [InitiateAuth](../../../cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.md "../../../cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.md") API request. After your user succeeds all challenges and the
`CUSTOM_CHALLENGE` challenge returns an `issueTokens` value of
`true`, Amazon Cognito returns one final `DEVICE_SRP_AUTH` challenge.

###### To sign in with a device

1. Retrieve your user’s device key from client storage.
2. Start your user’s sign-in session with an [InitiateAuth](../../../cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.md "../../../cognito-user-identity-pools/latest/APIReference/API_InitiateAuth.md") API request. Choose an `AuthFlow` of
   `USER_SRP_AUTH`, `REFRESH_TOKEN_AUTH`,
   `USER_PASSWORD_AUTH`, or `CUSTOM_AUTH`. In
   `AuthParameters`, add your user’s device key to the `DEVICE_KEY`
   parameter, and include the other required parameters for your selected sign-in
   flow.
   1. You can also pass `DEVICE_KEY` in the parameters of a
      `PASSWORD_VERIFIER` response to an authentication challenge.

3. Complete challenge responses until you receive a `DEVICE_SRP_AUTH`
   challenge in the response.
4. In a [RespondToAuthChallenge](../../../cognito-user-identity-pools/latest/APIReference/API_RespondToAuthChallenge.md "../../../cognito-user-identity-pools/latest/APIReference/API_RespondToAuthChallenge.md") API request, send a `ChallengeName` of
   `DEVICE_SRP_AUTH` and parameters for `USERNAME`,
   `DEVICE_KEY`, and `SRP_A`.
5. Amazon Cognito responds with a `DEVICE_PASSWORD_VERIFIER` challenge. This challenge
   response includes values for `SECRET_BLOCK` and `SRP_B`.
6. With your SRP library, generate and submit `PASSWORD_CLAIM_SIGNATURE`,
   `PASSWORD_CLAIM_SECRET_BLOCK`, `TIMESTAMP`, `USERNAME`,
   and `DEVICE_KEY` parameters. Submit these in an additional
   `RespondToAuthChallenge` request.
7. Complete additional challenges until you receive the user’s JWTs.

The following pseudocode demonstrates how to calculate values for your
`DEVICE_PASSWORD_VERIFIER` challenge response. For SRP authentication with a
device, generate a _new_ SRP secret for your user: a fresh
high-entropy password `DeviceSecret`, a salt, and the associated password verifier.
These values are distinct from the password, salt, and verifier used for the user's SRP
authentication. They are only used for device authentication and are only stored on the
device. Functions for generating the SRP secrets for users' devices are available in [SRP libraries](https://github.com/secure-remote-password/implementations "https://github.com/secure-remote-password/implementations") that
are available in various SDKs.

```
PASSWORD_CLAIM_SECRET_BLOCK = SECRET_BLOCK
TIMESTAMP = "Tue May 7 00:09:40 UTC 2025"
k = SHA256(N || g) as a non-negative integer in big-endian
u = SHA256(SRP_A || SRP_B) as a non-negative integer in big-endian
x = SHA256(salt || SHA256(DeviceGroupKey || DeviceKey || ":" || DeviceSecret)) as a non-negative integer in big-endian
S_USER = (SRP_B - k * g^x)^(a + u * x) % N
K_USER = HKDF_HMAC_SHA256(salt=u, ikm=S_USER, info="Caldera Derived Key", length=16 bytes)
PASSWORD_CLAIM_SIGNATURE = Base64(HMAC_SHA256(key=K_USER, message=(DeviceGroupKey || DeviceKey || PASSWORD_CLAIM_SECRET_BLOCK || TIMESTAMP)))
```

## Viewing, updating

and forgetting devices

You can implement the following features in your app with the Amazon Cognito API.

1. Display information about a user’s current device.
2. Display a list of all of your user’s devices.
3. Forget a device.
4. Update a device remembered state.

The access tokens that authorize the API requests in the following descriptions must
include the `aws.cognito.signin.user.admin` scope. Amazon Cognito adds a claim for this
scope to all access tokens that you generate with the Amazon Cognito user pools API. Third-party IdPs must
separately manage devices and MFA for their users who authenticate to Amazon Cognito. In managed login,
you can request the `aws.cognito.signin.user.admin` scope, but managed login
automatically adds device information to advanced security user logs, and doesn't offer to
remember devices.

###### Display information about a device

You can query information about a user’s device to determine if it is still in current
use. For example, you might want to deactivate remembered devices after they haven’t signed
in for 90 days.

- To display your user’s device information in a public-client app, submit your user’s
  access key and device key in a [GetDevice](../../../cognito-user-identity-pools/latest/APIReference/API_GetDevice.md "../../../cognito-user-identity-pools/latest/APIReference/API_GetDevice.md") API request.
- To display your user’s device information in a confidential-client app, sign an [AdminGetDevice](../../../cognito-user-identity-pools/latest/APIReference/API_AdminGetDevice.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminGetDevice.md") API request with AWS credentials and submit your user’s
  username, device key, and user pool.

###### Display a list of all your user’s devices

You can display a list of all your user’s devices and their properties. For example, you
might want to verify that the current device matches a remembered device.

- In a public-client app, submit your user’s access token in a [ListDevices](../../../cognito-user-identity-pools/latest/APIReference/API_ListDevices.md "../../../cognito-user-identity-pools/latest/APIReference/API_ListDevices.md") API request.
- In a confidential-client app, sign an [AdminListDevices](../../../cognito-user-identity-pools/latest/APIReference/API_AdminListDevices.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminListDevices.md") API request with AWS credentials and submit your user’s
  username and user pool.

###### Forget a device

You can delete a user’s device key. You might want to do this when you determine that
your user no longer uses a device, or when you detect unusual activity and want to prompt a
user to complete MFA again. To register the device again later, you must generate and store
a new device key.

- In a public-client app, submit your user’s device key and access token in [ForgetDevice](../../../cognito-user-identity-pools/latest/APIReference/API_ForgetDevice.md "../../../cognito-user-identity-pools/latest/APIReference/API_ForgetDevice.md") API request.
- In a confidential-client app, submit your user’s device key and access token in [AdminForgetDevice](../../../cognito-user-identity-pools/latest/APIReference/API_AdminForgetDevice.md "../../../cognito-user-identity-pools/latest/APIReference/API_AdminForgetDevice.md") API request.
