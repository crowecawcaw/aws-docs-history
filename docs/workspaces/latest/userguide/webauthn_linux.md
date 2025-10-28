# Configure WebAuthn on Linux WorkSpaces

Linux WorkSpaces currently support Standard WebAuthn, which requires a browser extension to facilitate the redirection of WebAuthn prompts onto the client.

## Prerequisites

- Amazon WorkSpaces WSP host adapter version 2.1.0.1923 or higher
- Amazon WorkSpaces native clients for Windows, Linux and Mac that support WebAuthn.

For more information, see [Client version requirements](webauthn_support.md#webauthn-client-versions "webauthn_support.md#webauthn-client-versions").

- Root access (sudo) on the Linux WorkSpaces instance
- Internet access to download browser extensions

## Configuration Steps

###### 1. Verify WSP Host Adapter Version

- Use the following command to verify the version of WSP host adapter. If version is lower than 2.1.0.1923, reboot the WorkSpace, and the adapter will be updated automatically.

```
`$` apt show wsp-dcv-host-adapter
```

###### 2. Configure Native Messaging Host

- For each supported browser, create a symbolic link to the native messaging host manifest file:

**Google Chrome**

```
`$` sudo mkdir -p /etc/opt/chrome/native-messaging-hosts
sudo ln -s -f /usr/share/dcv/webauthn/com.dcv.webauthnredirection.nativemessagehost.json /etc/opt/chrome/native-messaging-hosts/
```

**Chromium**

```
`$` sudo mkdir -p /etc/chromium/native-messaging-hosts
sudo ln -s -f /usr/share/dcv/webauthn/com.dcv.webauthnredirection.nativemessagehost.json /etc/chromium/native-messaging-hosts/
```

**Microsoft Edge**

```
`$` sudo mkdir -p /etc/opt/edge/native-messaging-hosts
sudo ln -s -f /usr/share/dcv/webauthn/com.dcv.webauthnredirection.nativemessagehost.json /etc/opt/edge/native-messaging-hosts/
```

###### 3. Install the DCV WebAuthn Extension

1. Install the browser extension for WebAuthn redirection. This can be done manually or through enterprise policies.

**Installing Manually**

Download the extension from the respective browser stores:

    * [Microsoft Edge Add-ons](https://microsoftedge.microsoft.com/addons/detail/dcv-webauthn-redirection-/ihejeaahjpbegmaaegiikmlphghlfmeh "https://microsoftedge.microsoft.com/addons/detail/dcv-webauthn-redirection-/ihejeaahjpbegmaaegiikmlphghlfmeh")
    * [Chrome Web Store](https://chrome.google.com/webstore/detail/dcv-webauthn-redirection/mmiioagbgnbojdbcjoddlefhmcocfpmn "https://chrome.google.com/webstore/detail/dcv-webauthn-redirection/mmiioagbgnbojdbcjoddlefhmcocfpmn")

For manual installation:

    1. Connect to your Amazon DCV session.
    2. Open your preferred browser, and navigate to the relevant browser store (links above).
    3. Proceed by selecting **Get** (Microsoft Edge) or **Add to Chrome** (Google Chrome).
    4. Follow the on-screen instructions. A confirmation will appear once the extension is successfully added.

2. To enable seamless setup, you can configure the system to preinstall the DCV WebAuthn extension as follows:

**Google Chrome**

```
`$` sudo mkdir -p /usr/share/google-chrome/extensions/
echo '{"external_update_url": "https://clients2.google.com/service/update2/crx"}' | \
sudo tee /usr/share/google-chrome/extensions/mmiioagbgnbojdbcjoddlefhmcocfpmn.json
sudo chmod a+r /usr/share/google-chrome/extensions/mmiioagbgnbojdbcjoddlefhmcocfpmn.json
```

**Chromium, Brave browser**

```
`$` sudo mkdir -p /usr/share/chromium/extensions/
echo '{"external_update_url": "https://clients2.google.com/service/update2/crx"}' | \
sudo tee /usr/share/chromium/extensions/mmiioagbgnbojdbcjoddlefhmcocfpmn.json
sudo chmod a+r /usr/share/chromium/extensions/mmiioagbgnbojdbcjoddlefhmcocfpmn.json
```

**Microsoft Edge**

```
`$` sudo mkdir -p /usr/share/microsoft-edge/extensions/
echo '{"external_update_url": "https://edge.microsoft.com/extensionwebstorebase/v1/crx"}' | \
sudo tee /usr/share/microsoft-edge/extensions/ihejeaahjpbegmaaegiikmlphghlfmeh.json
sudo chmod a+r /usr/share/microsoft-edge/extensions/ihejeaahjpbegmaaegiikmlphghlfmeh.json
```

**4. Restart the browser.**

During the restart, the DCV WebAuthn extension should install automatically, and
WebAuthn devices will be available for redirection in your WorkSpaces session. If you encounter any issues,
please contact AWS Support
or refer to your WorkSpaces documentation for further troubleshooting.
