

# Configuring host-to-client URL redirection
<a name="config-url-redirection"></a>

Beginning with Amazon DCV Server 2026.0, host-to-client URL redirection opens links that users access in an Amazon DCV session on the user's local device instead of in the session. Redirecting resource-intensive web content, such as video, to the local device reduces latency and lowers resource consumption on the Amazon DCV server.

URL redirection supports the following types of links.


**Supported link types**  

| Link type | Opens on the local device in | 
| --- | --- | 
| https:// and http:// | The default web browser | 
| ftp:// and sftp:// | The default FTP or SFTP application | 
| mailto: | The default email application | 

You control which links are redirected by configuring URL patterns. Only approved links open on the local device, and all other links remain in the session. You can also configure an exception list to keep specific links in the session even if they match a configured pattern.

By default, URL redirection is not enabled. When URL redirection is enabled, the Amazon DCV URL Redirection browser extension is automatically installed on Google Chrome and Microsoft Edge in the session at the start of the next session. The extension redirects links that users open in web browsers. Links opened within other applications in the session, such as email clients, chat applications, and documents, don't require the browser extension. When an application opens a link with the session's default web browser, FTP or SFTP application, or email application, Amazon DCV checks the link against your URL patterns first. A matching link opens on the local device, and any other link opens in the session with the original default application.

While a client is connected, an application named **AWS DCV URL Redirector** appears in the session's **Default apps** settings. Amazon DCV doesn't make it the default application. You only need to select it in specific cases, such as [FTP links opened in Microsoft Edge](url-redirection-troubleshooting.md).

When no client is connected to the session, links open in the session as usual, and **AWS DCV URL Redirector** doesn't appear in **Default apps**.

**Topics**
+ [Prerequisites](url-redirection-prerequisites.md)
+ [Enable host-to-client URL redirection](enable-url-redirection.md)
+ [Configure URL patterns (allow list)](configure-url-patterns-allow-list.md)
+ [Configure the exception list (optional)](configure-exception-list.md)
+ [Configure mailto: redirection](configure-mailto-redirection.md)
+ [Configure the maximum URL length (optional)](configure-max-url-length.md)
+ [Disable host-to-client URL redirection](disable-url-redirection.md)
+ [Configure URL redirection using the Windows Registry Editor](configure-url-redirection-registry.md)
+ [URL redirection parameters](url-redirection-parameters.md)
+ [Troubleshooting](url-redirection-troubleshooting.md)
+ [Security considerations and best practices](url-redirection-security.md)