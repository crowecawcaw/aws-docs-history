

# Best practices
<a name="auth-best-practices"></a>

This section outlines best practices for securing your Amazon Location Service applications and optimizing authentication usage. By implementing credential isolation, monitoring, and appropriate restrictions, you can minimize security risk and control costs. For guidance on choosing between API keys, Amazon Cognito, and AWS Identity and Access Management, see [Choosing an authentication method](auth-choose-method.md).

## Credential management
<a name="auth-bp-credential-management"></a>

Proper credential management reduces security risk and simplifies operations when you need to rotate or revoke access.
+ **Use separate credentials per application** – Create distinct API keys or IAM roles for each application or environment (development, staging, production). This limits the blast radius if a credential is compromised.
+ **Apply the principle of least privilege** – Grant only the minimum permissions required for each use case. Limit access to specific APIs and resources rather than using wildcards.
+ **Rotate credentials regularly** – Periodically rotate API keys and review IAM policies. Remove unused credentials promptly.
+ **Never expose credentials in source code** – Store API keys, Amazon Cognito identity pool IDs, and other sensitive values in environment variables, secrets managers, or secure configuration stores. Do not commit them to version control.

## API key optimization
<a name="auth-bp-apikeys"></a>

API keys provide a simple way to grant unauthenticated, read-only access to Maps, Places, and Routes resources. Follow these practices to minimize security risk and optimize usage.
+ **Restrict actions and resources** – When creating an API key, specify only the actions and resources the application needs. For example, a map-only application should only allow `geo-maps:*` actions on the maps provider resource.
+ **Apply client restrictions** – Configure domain referrer restrictions for web applications, or application identifier restrictions for Android and iOS apps. This prevents your key from being used on unauthorized origins. For more information, see [Restrict API key usage by request origin](#restrict-usage-by-origin).
+ **Set expiration times** – Use key expiration to enforce regular rotation. Create a new key before the old one expires, update your application, then deactivate the old key.
+ **Monitor per-key usage** – Use CloudWatch metrics with the `ApiKeyName` dimension to track usage for each key individually. Set alarms on unexpected spikes in `CallCount`.
+ **Delete unused keys** – Regularly audit your API keys and delete any that are no longer in use. An inactive key that has been deactivated can be deleted after 90 days.

## Restrict API key usage by request origin
<a name="restrict-usage-by-origin"></a>

You can configure API keys with client restrictions that limit access to specific domains or mobile applications. When restricting by domain, the service authorizes requests only when the HTTP Referer header matches the value that you provide. When restricting by Android or Apple application, the service authorizes requests only when the application identifier HTTP header fields match the values that you provide.

For more information about API key restrictions, see [ApiKeyRestrictions](https://docs.aws.amazon.com/location/latest/APIReference/API_geoapikeys_ApiKeyRestrictions.html) in the *Amazon Location Service API Reference*.

 **Android application identifiers:** 
+ `X-Android-Package`:

  A unique identifier for Android applications, defined in the app's `build.gradle` file, typically following a reverse-domain format.

  Example:

   `com.mydomain.appname` 
+ `X-Android-Cert`:

  The SHA-1 hash of the signing certificate used to sign the Android APK.

  Example:

   `BB:0D:AC:74:D3:21:E1:43:67:71:9B:62:91:AF:A1:66:6E:44:5D:75` 

 **Apple application identifiers:** 
+ `X-Apple-Bundle-Id`:

  A unique identifier for Apple (iOS, macOS, etc.) applications, defined in the app's `Info.plist`, typically following a reverse-domain format.

  Example:

   `com.mydomain.appname` 

## Amazon Cognito optimization
<a name="auth-bp-cognito"></a>

Amazon Cognito provides more granular access control than API keys and supports both authenticated and unauthenticated users.
+ **Scope down unauthenticated roles** – When using identity pools for anonymous access, attach IAM policies that allow only the specific Amazon Location actions and resources your application needs.
+ **Use condition keys for IP filtering** – Add `aws:SourceIp` conditions to your IAM policies to restrict access to known IP ranges when appropriate.
+ **Keep identity pools in the same Region** – Create the Amazon Cognito identity pool in the same AWS Region as your Amazon Location Service resources to avoid cross-Region latency and ensure proper access.
+ **Use authenticated identities when possible** – If your application has a sign-in flow, use Amazon Cognito user pools or federated identities to grant authenticated roles with specific permissions rather than relying on unauthenticated access.

## IAM optimization
<a name="auth-bp-iam"></a>

For server-side applications and internal tools, use AWS Identity and Access Management for full control over access.
+ **Use IAM roles instead of long-term credentials** – For applications running on AWS compute services (such as Amazon EC2, Lambda, or Amazon ECS), use IAM roles to provide temporary credentials automatically.
+ **Apply resource-level permissions** – Specify resource ARNs in your policies rather than using wildcards. For example, restrict access to specific tracker or geofence collection resources.
+ **Use policy conditions** – Add conditions such as `aws:RequestedRegion` to limit access to specific Regions, or `aws:PrincipalTag` for attribute-based access control.
+ **Enable CloudTrail** – Use AWS CloudTrail to log all Amazon Location Service API calls for auditing and compliance. Review logs regularly for unexpected access patterns.