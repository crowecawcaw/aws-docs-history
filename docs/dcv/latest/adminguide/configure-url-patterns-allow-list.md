

# Configure URL patterns (allow list)
<a name="configure-url-patterns-allow-list"></a>

The allow list contains the URL patterns for the links that you want to open on the local device. A link that matches any pattern in the allow list is redirected. If the allow list is empty, no links are redirected.

**To configure the allow list**

1. Open a Command Prompt as the administrator and go to the Amazon DCV Server installation directory:

   ```
   C:\> cd "C:\Program Files\NICE\DCV\Server\bin"
   ```

1. Set the `host-to-client-allow-list` parameter to the URL patterns, separated by commas. For example:

   ```
   C:\Program Files\NICE\DCV\Server\bin> dcv.exe set-config --section url-redirection --key host-to-client-allow-list "'https://www.youtube.com/*,https://docs.aws.amazon.com/*,https://*.example.com/*,sftp://files.example.com/*,mailto:*@example.com'"
   ```

1. (Optional) Verify the value:

   ```
   C:\Program Files\NICE\DCV\Server\bin> dcv.exe get-config --section url-redirection --key host-to-client-allow-list
   ```

1. Start a new Amazon DCV session for the change to take effect. If you use an automatic console session, restart the Amazon DCV server. For more information, see [Stopping the server](https://docs.aws.amazon.com/dcv/latest/adminguide/manage-stop.html) and [Starting the server](https://docs.aws.amazon.com/dcv/latest/adminguide/manage-start.html).

**Note**  
Enter the patterns as a single comma-separated value, enclosed in single quotes inside double quotes, as shown in the example. `dcv set-config` rejects a value in list format, such as `"['https://www.youtube.com/*', 'https://*.example.com/*']"`.

## URL pattern syntax
<a name="url-pattern-syntax"></a>

Each URL pattern can include the protocol (`https://`, `http://`, `ftp://`, or `sftp://`). If a pattern doesn't include a protocol, Amazon DCV uses `https://`. A pattern applies only to links that use the same protocol. For security, use `https://` and `sftp://` patterns unless you have a specific reason to redirect `http://` or `ftp://` links.

Patterns support two wildcards:


**Wildcard syntax**  

| Wildcard | Matches | Example pattern | Example URLs matched | 
| --- | --- | --- | --- | 
| \* | Zero or more characters | https://www.youtube.com/\* | https://www.youtube.com/watch?v=abc, https://www.youtube.com/channel/xyz | 
| ? | Exactly one character | https://example.com/page? | https://example.com/page1, https://example.com/pageA | 

The following rules also apply:
+ A pattern that contains only a domain, such as `https://example.com`, matches only the domain itself. To match all pages on a domain, end the pattern with `/*`, for example `https://example.com/*`.
+ For `https://` and `http://` patterns, `www.` is optional in both directions:
  + `https://example.com/*` matches `https://example.com/page` and `https://www.example.com/page`.
  + `https://www.example.com/*` matches `https://www.example.com/page` and `https://example.com/page`.
  + `https://*.example.com/*` matches subdomains, such as `https://docs.example.com/page`, and also the bare domain, `https://example.com/page`.

  This doesn't apply to `ftp://` and `sftp://` patterns. For example, `sftp://*.example.com/*` doesn't match `sftp://example.com/file`.
+ Patterns are case-insensitive.
+ Patterns can't contain commas.

To redirect all HTTPS URLs, use `https://*`.

The following table shows example patterns.


**Example patterns**  

| Pattern | Redirects | 
| --- | --- | 
| https://www.youtube.com/\* | All pages on www.youtube.com and youtube.com | 
| https://\*.zoom.us/\* | All pages on any subdomain of zoom.us | 
| https://docs.aws.amazon.com/dcv/\* | Pages under docs.aws.amazon.com/dcv/ | 
| sftp://files.example.com/\* | All SFTP links to files.example.com | 
| mailto:\*@example.com | Email links where every recipient is in the example.com domain | 