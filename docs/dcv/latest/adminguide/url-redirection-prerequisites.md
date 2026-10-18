

# Prerequisites
<a name="url-redirection-prerequisites"></a>

Before you enable URL redirection, make sure that your environment meets the following requirements.

**Amazon DCV Server**
+ Amazon DCV Server 2026.0 or later on one of the following Windows operating systems:
  + Windows 10
  + Windows 11
  + Windows Server 2019
  + Windows Server 2022
  + Windows Server 2025
+ URL redirection isn't supported on Linux and macOS Amazon DCV servers.

**Amazon DCV clients**
+ Windows client 2026.0 or later
+ macOS client 2026.0 or later
+ Linux client 2026.0 or later
+ Web browser client included with Amazon DCV Server 2026.0 or later

**Web browsers in the session**
+ Google Chrome or Microsoft Edge. Links that users open in Mozilla Firefox or other web browsers aren't redirected. Links that other applications open are redirected regardless of which browser is the default.

  Amazon DCV automatically installs the Amazon DCV URL Redirection browser extension when URL redirection is enabled. The browser downloads the extension from the Chrome Web Store or Microsoft Edge Add-ons, so the Amazon DCV server must be able to reach them. If your organization manages browser extensions with a policy, allow the extension in that policy. The following table lists the extension IDs.


**Browser extension IDs**  

| Browser | Extension | 
| --- | --- | 
| Google Chrome | [Amazon DCV URL Redirection Extension](https://chromewebstore.google.com/detail/dfbpeicgigpfhpaliagackbnflannljf) (ID: dfbpeicgigpfhpaliagackbnflannljf) | 
| Microsoft Edge | [Amazon DCV URL Redirection Extension](https://microsoftedge.microsoft.com/addons/detail/mdkljmihenacedcpcheifaonefpfacnf) (ID: mdkljmihenacedcpcheifaonefpfacnf) | 

**Extensions**
+ The Amazon DCV extensions feature must be enabled. It is enabled by default. For more information, see the `extensions` parameters in the [Amazon DCV Server parameter reference](https://docs.aws.amazon.com/dcv/latest/adminguide/config-param-ref.html).

**Local device**
+ A default application for each type of link that you redirect: a web browser for `https://` and `http://` links, an FTP or SFTP application for `ftp://` and `sftp://` links, and an email application for `mailto:` links.