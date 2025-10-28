# Configure WebAuthn on Windows WorkSpaces

Windows WorkSpaces support two WebAuthn modes: Enhanced and Standard.

## Standard WebAuthn

Standard WebAuthn requires a browser extension to facilitate the redirection of WebAuthn prompts onto the client.
This version of WebAuthn is supported on WorkSpaces client apps on Windows, Mac and Linux.

### Enabling Standard WebAuthn

Your WorkSpaces administrator can enable and disable WebAuthn. Your browser will notify you that the required browser extension is installed for you when your administrator enables it.

###### To install the browser extension manually (optional)

1.  Sign into your WorkSpace.
2.  In your browser, open one of the following links, depending on the browser you're using:
    - For **Microsoft Edge**:
      https://microsoftedge.microsoft.com/addons/detail/dcv-webauthn-redirection-/ihejeaahjpbegmaaegiikmlphghlfmeh
    - For **Google Chrome**:
      https://chromewebstore.google.com/detail/dcv-webauthn-redirection/mmiioagbgnbojdbcjoddlefhmcocfpmn?pli=1

3.  Install the extension by choosing:

        * **Get** (for Microsoft Edge)
        * **Add to Chrome** (for Google Chrome).


        Then choose **Add extension**.

    Once the installation is complete, you'll see a confirmation message saying that you've
    successfully added the extension.

## Enhanced WebAuthn

Enhanced WebAuthn does not require a browser extension, which simplifies the initial setup,
and provides improved performance. It also introduces support for WebAuthn on native Windows applications,
enabling you to use WebAuthn authentication in both web browsers and Windows desktop applications.

### Key Benefits

Enhanced WebAuthn provides the following key benefits:

- No browser extension required
- Improved performance
- Support for WebAuthn in native Windows applications
- Seamless authentication experience across browsers and desktop applications

### Enabling Enhanced WebAuthn

- Ensure your WorkSpace is running the latest version of the Amazon DCV host agent (version 2.1.0.2000 or above) for Windows.
- Ensure your WorkSpaces client supports WebAuthn. For more information, see [Client version requirements](webauthn_support.md#webauthn-client-versions "webauthn_support.md#webauthn-client-versions").
- Contact your WorkSpaces administrator to enable WebAuthn for your WorkSpace.

###### Note

If you're upgrading from Standard WebAuthn to Enhanced WebAuthn, disable or uninstall the browser extension you previously installed for Standard WebAuthn.

### Using Enhanced WebAuthn

Once enabled, Enhanced WebAuthn works seamlessly on apps allowed by your administrator, without any additional configuration on your part.
You can use your WebAuthn devices for authentication in:

- Web browsers (Chrome, Edge)
- Native Windows applications that support WebAuthn
- Windows system dialogs requiring WebAuthn authentication

## Troubleshooting

If you encounter any issues with Standard WebAuthn or Enhanced WebAuthn:

- Ensure your WorkSpaces host agent and WorkSpaces client are up to date.
- For Standard WebAuthn, verify that the browser extension is installed and enabled.
- For Enhanced WebAuthn, confirm with your administrator that it's enabled for your WorkSpace.
- Try restarting your browser or your WorkSpace session.
- If problems persist, contact your WorkSpaces administrator or AWS Support.
