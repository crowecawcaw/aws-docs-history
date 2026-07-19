# API key concepts

An API key is a credential that associates a plain text key value with specific
Amazon Location Service resources and permitted actions. When your application includes an API key
in a request, Amazon Location Service authorizes the request based on the key's configuration
without requiring any other authentication.

**Key value**

The plain text string used to authenticate API requests. Key values
follow the format
`v1.public.`a1b2c3d4...``. You
include this value as the `key` parameter in API
requests.

**Restrictions**

Controls that define what an API key can do. Restrictions include
_allowed actions_ (which APIs the key can call)
and _allowed resources_ (which resources the key
can access). You configure restrictions when creating or updating a
key.

**Client restrictions**

Optional limits on where an API key can be used. You can restrict a
key to specific web domains (using the HTTP Referer header), Android
applications (using package name and signing certificate), or Apple
applications (using bundle ID).

**Expiration**

An optional timestamp after which the API key is automatically
deactivated. Use expiration to enforce regular key rotation or create
temporary keys. Keys without an expiration time remain active
indefinitely.

**Key state**

An API key is either _active_ (can be used to
make requests) or _inactive_ (deactivated, either
manually or by expiration). Inactive keys cannot authenticate
requests and can be deleted after 90 days.
