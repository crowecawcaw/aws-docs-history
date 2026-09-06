

# Security considerations and best practices
<a name="url-redirection-security"></a>

Keep the following security considerations in mind when you configure host-to-client URL redirection.
+ Add URLs that contain sensitive data to the exception list to keep them in the remote session.
+ Redirected URLs might require separate authentication in the local browser.
+ Cookies and session data are not shared between the remote session and the local browser.
+ Use HTTPS patterns to help ensure encrypted communication.

**Best practices**
+ Verify that local devices can access redirected URLs. Check corporate firewall policies if needed.
+ If users connect through a proxy, verify that redirected URLs are accessible.
+ Start small: Begin with a limited set of trusted domains and expand based on user feedback.
+ Use HTTPS: Always prefer `https://` patterns over `http://` for security.
+ Be specific: Use specific paths rather than broad wildcards when possible.
+ Review regularly: Review and update URL patterns regularly to remove unused entries.
+ Test thoroughly: Validate configuration with pilot users before organization-wide deployment.