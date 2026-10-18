

# Configure the exception list (optional)
<a name="configure-exception-list"></a>

The exception list contains URL patterns for links that you don't want to redirect. Amazon DCV evaluates the exception list before the allow list. If a link matches an exception pattern, it opens in the session regardless of the allow list. Exception patterns use the same syntax as allow list patterns.

Include the protocol in every exception pattern, and add a pattern for each protocol that you want to cover. A pattern without a protocol applies only to `https://` links. For example, to keep all `localhost` links in the session, add both `https://localhost/*` and `http://localhost/*`. A `mailto:` pattern that isn't valid doesn't block anything. Amazon DCV logs a warning for it in the `urlredirnativehost` log file when it evaluates a `mailto:` link.

**To configure the exception list**

1. Open a Command Prompt as the administrator and go to the Amazon DCV Server installation directory:

   ```
   C:\> cd "C:\Program Files\NICE\DCV\Server\bin"
   ```

1. Set the `host-to-client-deny-list` parameter to the URL patterns, separated by commas. For example:

   ```
   C:\Program Files\NICE\DCV\Server\bin> dcv.exe set-config --section url-redirection --key host-to-client-deny-list "'https://*.internal.example.com/*,https://localhost/*,sftp://internal-files.example.com/*,mailto:*@internal.example.com'"
   ```

1. (Optional) Verify the value:

   ```
   C:\Program Files\NICE\DCV\Server\bin> dcv.exe get-config --section url-redirection --key host-to-client-deny-list
   ```

1. Start a new Amazon DCV session for the change to take effect. If you use an automatic console session, restart the Amazon DCV server. For more information, see [Stopping the server](https://docs.aws.amazon.com/dcv/latest/adminguide/manage-stop.html) and [Starting the server](https://docs.aws.amazon.com/dcv/latest/adminguide/manage-start.html).

**Note**  
Enter the patterns as a single comma-separated value, enclosed in single quotes inside double quotes, as shown in the example. `dcv set-config` rejects a value in list format, such as `"['https://www.youtube.com/*', 'https://*.example.com/*']"`.