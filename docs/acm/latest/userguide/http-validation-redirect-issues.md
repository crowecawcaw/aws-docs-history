# HTTP redirect issues

If you're using a redirect instead of serving the content directly, follow these steps
to verify your configuration.

###### To verify redirect configuration

1. Copy the `RedirectFrom` URL and paste it into your browser's address
   bar.
2. In a new browser tab, paste the `RedirectTo` URL.
3. Compare the content at both URLs to ensure they match exactly.
4. Verify that the redirect returns a 302 status code.
