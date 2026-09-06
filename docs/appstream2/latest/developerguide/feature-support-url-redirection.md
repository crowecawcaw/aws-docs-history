

# Host-to-client URL redirection
<a name="feature-support-url-redirection"></a>

Host-to-client URL redirection opens URLs accessed on a WorkSpaces Applications streaming session in the web browser on the user's local device instead of on the streaming instance. This offloads resource-intensive web content such as video to the local device, which reduces latency and server-side resource consumption.

You control which URLs are redirected by configuring URL patterns. Only approved links open locally while all others remain in the remote session. You can also configure an exception list to exclude specific URLs from redirection even if they match a configured pattern.

When the feature is enabled, WorkSpaces Applications automatically installs the Amazon DCV URL redirection browser extension on Google Chrome and Microsoft Edge in the streaming session when a new session starts. The extension redirects URLs that users open in web browsers. Links opened from apps within the session do not require the browser extension for redirection.

**Topics**
+ [Prerequisites](url-redirection-prerequisites.md)
+ [Enable host-to-client URL redirection](url-redirection-enable.md)
+ [Configure URL patterns (allowlist)](url-redirection-configure-patterns.md)
+ [Configure the exception list (optional)](url-redirection-configure-exceptions.md)
+ [Troubleshooting](url-redirection-troubleshooting.md)
+ [Security considerations and best practices](url-redirection-security.md)