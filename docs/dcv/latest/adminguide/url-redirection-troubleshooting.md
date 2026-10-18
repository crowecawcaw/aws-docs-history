

# Troubleshooting
<a name="url-redirection-troubleshooting"></a>

**Links aren't redirected**
+ Verify that the `enabled` parameter is set to `true` and that the allow list contains at least one pattern. To check the values, run `dcv.exe get-config --section url-redirection`.
+ Verify that the Amazon DCV server and client meet the version requirements in [Prerequisites](url-redirection-prerequisites.md).
+ Start a new Amazon DCV session after you change the configuration.

**Links opened in the web browser aren't redirected**
+ Verify that the Amazon DCV URL Redirection extension is installed and turned on in Google Chrome or Microsoft Edge in the session. Amazon DCV installs the extension automatically when a session starts. If it isn't installed, for example because the server can't reach the browser's extension store or a browser policy blocks automatic installation, install it manually from the [Chrome Web Store](https://chromewebstore.google.com/detail/dfbpeicgigpfhpaliagackbnflannljf) or [Microsoft Edge Add-ons](https://microsoftedge.microsoft.com/addons/detail/mdkljmihenacedcpcheifaonefpfacnf).
+ If your organization manages browser extensions with a policy, verify that the policy allows the extension.
+ Verify that the link was opened in Google Chrome or Microsoft Edge. Links opened in other browsers aren't redirected.

**FTP links opened in Microsoft Edge aren't redirected**

If Microsoft Edge is the session user's default application for FTP links, Edge opens `ftp://` links itself instead of passing them to Amazon DCV. Edge often becomes the FTP default when it's set as the default browser. Other browsers, other applications, and `sftp://` links aren't affected.

To redirect FTP links from Edge, make **AWS DCV URL Redirector** the default application for FTP in the session:

1. Connect to the Amazon DCV session.

1. Open the default apps settings for the session's operating system:
   + Windows 11 and Windows Server 2025: open **Settings**, **Apps**, **Default apps**, and choose **Choose defaults by link type**.
   + Windows 10, Windows Server 2019, and Windows Server 2022: open **Settings**, **Apps**, **Default apps**, and choose **Choose default apps by protocol**.

1. For **FTP**, choose **AWS DCV URL Redirector**.

If FTP links have no default application, Windows asks which application to use the first time an FTP link opens. Choose **AWS DCV URL Redirector**.

**A specific link isn't redirected**
+ Verify that the pattern uses the same protocol as the link.
+ Verify that the pattern ends with `/*` if it must match pages on the domain.
+ Verify that the link doesn't also match a pattern in the exception list.
+ Verify that the URL isn't longer than the configured maximum URL length.
+ For `mailto:` links, verify that every recipient matches a `mailto:` pattern in the allow list.

**A link that matches the exception list is still redirected**
+ Verify that the exception pattern includes the same protocol as the link. A pattern without a protocol applies only to `https://` links, so `localhost` doesn't keep `http://localhost` links in the session.
+ For `mailto:` links, verify that the pattern has the form `mailto:name@domain`. Amazon DCV ignores a `mailto:` pattern that isn't valid and logs a warning in the `urlredirnativehost` log file.

**A redirected link doesn't open on the local device**
+ Verify that the local device has a default application for that type of link. For `ftp://` and `sftp://` links, the local device needs an FTP or SFTP application, which many devices don't have by default.

**Log files**

URL redirection log files are located in `C:\ProgramData\NICE\dcv\log` on the Amazon DCV server. The log file names start with `urlredirextensionhost` and `urlredirnativehost`.