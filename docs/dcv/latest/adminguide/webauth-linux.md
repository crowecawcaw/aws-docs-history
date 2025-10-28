# Configuring WebAuthn redirection on Linux hosts

DCV Linux server currently support Standard WebAuthn. Standard WebAuthn requires a browser extension to facilitate the redirection of WebAuthn prompts onto the
client. WebAuthn can be enabled or disabled using the webauthn-redirection permission. For more information, see [Working with permissions files](security-authorization-file-create.md "security-authorization-file-create.md").

###### Prerequisites

- DCV server version 2025.0 or higher
- DCV native clients for Windows, Linux and Mac
- Root access (sudo) on the Linux server instance
- Internet access to download browser extensions

## Configuring WebAuthn Redirection

WebAuthn is enabled on DCV by default. You can enable or disable WebAuthn by enabling the “[webauthn]” setting in the DCV configuration file:

```
/etc/dcv/dcv.conf

[webauthn]
enabled=true
```

###### Configuring Webauthn for Linux

1. Create a symbolic link to the native messaging host manifest file for each supported browser.

Google Chrome
Use the following commands:

```
sudo mkdir -p /etc/opt/chrome/native-messaging-hosts
```

```
sudo ln -s -f /usr/share/dcv/webauthn/com.dcv.webauthnredirection.nativemessagehost.json /etc/opt/chrome/native-messaging-hosts/
```

Chromium
Use the following commands:

```
sudo mkdir -p /etc/chromium/native-messaging-hosts
```

```
sudo ln -s -f /usr/share/dcv/webauthn/com.dcv.webauthnredirection.nativemessagehost.json /etc/chromium/native-messaging-hosts/
```

Microsoft Edge
Use the following commands:

```
sudo mkdir -p /etc/opt/edge/native-messaging-hosts
```

```
sudo ln -s -f /usr/share/dcv/webauthn/com.dcv.webauthnredirection.nativemessagehost.json /etc/opt/edge/native-messaging-hosts/
```

2. Install the browser extension for WebAuthn redirection. This can be done manually or through enterprise policies.

Google Chrome
Use the following commands:

```
sudo mkdir -p /usr/share/google-chrome/extensions/
```

```
echo '{"external_update_url": "https://clients2.google.com/service/update2/crx"}' | \
```

```
sudo tee /usr/share/google-chrome/extensions/mmiioagbgnbojdbcjoddlefhmcocfpmn.json
```

```
sudo chmod a+r /usr/share/google-chrome/extensions/mmiioagbgnbojdbcjoddlefhmcocfpmn.json
```

Chromium
Use the following commands:

```
sudo mkdir -p /usr/share/chromium/extensions/
```

```
echo '{"external_update_url": "https://clients2.google.com/service/update2/crx"}' | \
```

```
sudo tee /usr/share/chromium/extensions/mmiioagbgnbojdbcjoddlefhmcocfpmn.json
```

```
sudo chmod a+r /usr/share/chromium/extensions/mmiioagbgnbojdbcjoddlefhmcocfpmn.json
```

Microsoft Edge
Use the following commands:

```
sudo mkdir -p /usr/share/microsoft-edge/extensions/
```

```
echo '{"external_update_url": "https://edge.microsoft.com/extensionwebstorebase/v1/crx"}' | \
```

```
sudo tee /usr/share/microsoft-edge/extensions/ihejeaahjpbegmaaegiikmlphghlfmeh.json
```

```
sudo chmod a+r /usr/share/microsoft-edge/extensions/ihejeaahjpbegmaaegiikmlphghlfmeh.json
```

3. Restart the browser.
