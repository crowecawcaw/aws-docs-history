# Configuring WebAuthn redirection on Windows hosts

WebAuthn can be enabled or disabled using the `webauthn-redirection` permission. For more information, see [Working with permissions files](security-authorization-file-create.md "security-authorization-file-create.md").

## Configuring WebAuthn Redirection

WebAuthn is enabled on DCV by default. You can enable or disable WebAuthn using the following registry:

```
HKEY_USERS\S-1-5-18\Software\GSettings\com\nicesoftware\dcv\webauthn

Key: enabled
Value: 1 to enable, 0 to disable
```

Additionally, you can configure which apps and processes are allowed to redirect the WebAuthn prompt using the process-compatibilitylist key by adding string values.

Example key:

```
HKEY_USERS\S-1-5-18\Software\GSettings\com\nicesoftware\dcv\webauthn\process-compatibilitylist
```

Default Value (String):

```
['chrome.exe','msedge.exe','island.exe','firefox.exe','dcvwebauthnnativemsghost.exe','msedgewebview2.exe','Microsoft.AAD.BrokerPlugin.exe']
```

With the above default values, applications like Google Chrome (‘chrome.exe’), Microsoft Edge (‘msedge.exe’), Island Browser (‘island.exe’),
and Mozilla Firefox (‘firefox.exe’) are supported for WebAuthn redirection. ‘dcvwebauthnnativemsghost.exe’ is required for browser extension-based
Standard WebAuthn, ‘msedgewebview2.exe' is required for embedded Microsoft Edge browsers and 'Microsoft.AAD.BrokerPlugin.exe' is required to enable
WebAuthn on Microsoft Teams and Microsoft Office365 apps.

You can add executables to the process compatibility list to add support for more apps and processes.

There are 2 modes for WebAuthn on Windows hosts:

### Enhanced WebAuthn Redirection

Starting with DCV 2025.0, you can use Enhanced WebAuthn on Windows DCV servers. Enhanced WebAuthn eliminates the need for a browser extension,
simplifying the initial setup and improving performance. It also introduces support for WebAuthn on native Windows applications, allowing users to
use WebAuthn authentication in both web browsers and Windows desktop applications.

###### Note

For upgrading from Standard WebAuthn to Enhanced WebAuthn, users will need to disable or uninstall the browser extension previously installed for Standard WebAuthn.

###### Note

Windows Server 2016 does not support system level WebAuthn. To use WebAuthn redirection on Windows Server 2016, you must use Standard WebAuthn.

**Using Enhanced WebAuthn**

Once enabled, Enhanced WebAuthn works seamlessly without any additional configuration on your part. You can use your WebAuthn devices for authentication in:

- Web browsers (Chrome, Edge)
- Native Windows applications that support WebAuthn
- Windows system dialogs requiring WebAuthn authentication

### Standard WebAuthn Redirection

Starting with DCV 2023.1, you can use Standard WebAuthn on Windows DCV servers. Standard WebAuthn redirection requires a browser extension to be installed on the remote server.
When the feature is enabled and the browser extension is installed, any WebAuthn requests initiated by the web applications running in the browser within the session are seamlessly
directed to the local client. Users can then use utilize devices like Windows Hello or YubiKey to finalize the authentication.

Supported browsers:

- Google Chrome 116 or later
- Microsoft Edge 116 or later

#### Setting up the WebAuthn redirection browser extension

Follow these procedures to set up Standard WebAuthn redirection.

##### Automatic Prompt on First Browser Launch

After installing the Amazon DCV Server 2023.1 with WebAuthn redirection enabled, users will be prompted to enable the browser extension when they first launch their browser. If they choose not to install
the extension or uninstall it later, WebAuthn redirection will not work. An administrator can enforce installation using the Group Policy.

##### Installing Using the Group Policy

For organizations looking to deploy the extension on a broader scale, you can utilize the Group Policy.

###### Using Microsoft Edge:

1. Download and install the [Microsoft Edge
   administrative template.](https://learn.microsoft.com/en-us/deployedge/configure-microsoft-edge#1-download-and-install-the-microsoft-edge-administrative-template "https://learn.microsoft.com/en-us/deployedge/configure-microsoft-edge#1-download-and-install-the-microsoft-edge-administrative-template")
2. Launch the Group Policy Management tool (gpmc.msc).
3. Navigate through: Forest > Domains > Your FQDN (e.g., example.com) > Group Policy Objects.
4. Select desired policy or create a new one then right-click on it and select "Edit".
5. Follow this path: Computer Configuration > Administrative Templates > Microsoft Edge > Extensions.
6. Access "Configure extension management settings", set it to "Enabled".
7. In the field for Configure extension management settings, enter the following:

```
{"ihejeaahjpbegmaaegiikmlphghlfmeh":{"installation_mode":"force_installed","update_url":"https://edge.microsoft.com/extensionwebstorebase/v1/crx"}}
```

8. Save the changes and reboot the server.

###### Using Google Chrome:

1. Obtain and implement the [Google Chrome administrative
   template](https://chromeenterprise.google/browser/download/#manage-policies-tab "https://chromeenterprise.google/browser/download/#manage-policies-tab")
2. Similar to the steps for Microsoft Edge, navigate through the Group Policy Management tool.
3. Proceed to: Computer Configuration > Administrative Templates > Google Chrome > Extensions.
4. Access "Configure extension management settings", set it to "Enabled".
5. In the field for Configure extension management settings, enter the following:

```
{"mmiioagbgnbojdbcjoddlefhmcocfpmn":{ "installation_mode":"force_installed","update_url":"https://clients2.google.com/service/update2/crx"}}
```

6. Save the changes and reboot the server.

##### Installing Manually

Extensions can be sourced from the respective browser stores:

- [Microsoft Edge Add-ons](https://microsoftedge.microsoft.com/addons/detail/dcv-webauthn-redirection-/ihejeaahjpbegmaaegiikmlphghlfmeh "https://microsoftedge.microsoft.com/addons/detail/dcv-webauthn-redirection-/ihejeaahjpbegmaaegiikmlphghlfmeh")
- [Chrome Web Store](https://chrome.google.com/webstore/detail/dcv-webauthn-redirection/mmiioagbgnbojdbcjoddlefhmcocfpmn "https://chrome.google.com/webstore/detail/dcv-webauthn-redirection/mmiioagbgnbojdbcjoddlefhmcocfpmn")

For manual installation:

1. Connect to your Amazon DCV session.
2. Open your preferred browser, and navigate to the relevant browser store (links above).
3. Proceed by selecting "Get" (Microsoft Edge) or "Add to Chrome" (Google Chrome).
4. Follow the on-screen instructions. A confirmation will appear once the extension is successfully added.

##### Using WebAuthn redirection in Incognito mode (Chrome only)

When using Incognito mode, the Amazon DCV WebAuthn Redirection Extension needs to be
specifically allowed to run within it, otherwise WebAuthn Redirection will not occur. To do this:

1. Open the extension settings.
2. Find **Allow in Incognito** in the details.
3. Toggle the switch to **On**.

## Webauthn Windows Troubleshooting

If you encounter any issues with WebAuthn or Enhanced WebAuthn:

- Ensure your DCV server and client are up to date.
- For Standard WebAuthn, verify that the browser extension is installed and enabled.
- For Enhanced WebAuthn, confirm that it’s enabled in the permissions file.
- Try restarting your browser or your DCV session.
- If problems persist, contact AWS Support.
