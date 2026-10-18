

# Security considerations and best practices
<a name="url-redirection-security"></a>
+ Use specific URL patterns. Add only the domains and paths that must open on the local device, instead of broad patterns such as `https://*`.
+ Use the exception list for internal domains and other links that must remain in the session, such as `https://*.internal.example.com/*` and `https://localhost/*`.
+ Use `https://` and `sftp://` patterns. Traffic for `http://` and `ftp://` links isn't encrypted.
+ Redirected links are opened from the local device and its network. Links to resources that are reachable only from the Amazon DCV server's network might not open on the local device.
+ Don't include credentials in `ftp://` or `sftp://` links. A redirected link passes credentials to the local device.
+ Keep the default maximum URL length unless you need to redirect longer URLs. Attackers can use very long URLs in maliciously crafted links.