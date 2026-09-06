

# HTTP redirect issues
<a name="http-validation-redirect-issues"></a>

If you're using a redirect instead of serving the content directly, follow these steps to verify your configuration.

**To verify redirect configuration**

1. Copy the `RedirectFrom` URL and paste it into your browser's address bar.

1. In a new browser tab, paste the `RedirectTo` URL.

1. Compare the content at both URLs to ensure they match exactly.

1. Verify that the redirect returns a 302 status code.