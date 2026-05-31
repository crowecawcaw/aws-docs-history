# Best practices for API keys

Follow these best practices to secure your API keys and manage their lifecycle.

## Manage API keys

API keys include a plain text _value_ that gives access to one
or more resources or APIs in your AWS account. If someone copies your API key,
they can access those same resources and APIs. To minimize the potential impact,
review the following best practices:

- **Limit the API key**

To avoid the situation above, it is best to limit your API key. When you
create the key, you can specify the domain, Android app or Apple app where
the key can be used.

- **Manage API key lifetimes**

You can create API keys that work indefinitely. However, if you want to
create a temporary API key, rotate API keys on a regular basis, or revoke an
existing API key, you can use _API key
expiration_.

    + You can set the expiration time for an API key when you create or
     update it.
    + When an API key reaches its expiration time, the key is
     automatically deactivated. Inactive keys can no longer be used to
     make requests.
    + You can change a temporary key to a permanent key by removing the
     expiration time.
    + You can delete an API key 90 days after deactivating it.
    + If you attempt to deactivate an API key that has been used within
     the last seven days, you'll be prompted to confirm that you want to
     make the change.
    + If you are using the Amazon Location Service API or the AWS CLI, set the
     `ForceUpdate` parameter to `true`,
     otherwise you'll receive an error.

## Restrict API key usage by request origin

You can configure API keys with client restrictions that limit access to specific
domains or mobile applications. When restricting by domain, requests will be
authorized only if the HTTP Referer header matches the value that you provide. When
restricting by Android or Apple application, requests will be authorized only if the
application identifier HTTP header fields match the values that you provide.

For more information, see [ApiKeyRestrictions](../APIReference/API_geoapikeys_ApiKeyRestrictions.md "../APIReference/API_geoapikeys_ApiKeyRestrictions.md") in the _Amazon Location Service API
Reference_.

**Android application identifiers:**

- `X-Android-Package`:

A unique identifier for Android applications, defined in the app's
`build.gradle` file, typically following a reverse-domain
format.

Example:

`com.mydomain.appname`

- `X-Android-Cert`:

The SHA-1 hash of the signing certificate used to sign the Android
APK.

Example:

`BB:0D:AC:74:D3:21:E1:43:67:71:9B:62:91:AF:A1:66:6E:44:5D:75`

**Apple application identifiers:**

- `X-Apple-Bundle-Id` :

A unique identifier for Apple (iOS, macOS, etc.) applications, defined in
the app's `Info.plist`, typically following a reverse-domain
format.

Example:

`com.mydomain.appname`
