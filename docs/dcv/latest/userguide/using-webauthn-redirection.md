

# Using WebAuthn redirection
<a name="using-webauthn-redirection"></a>

Amazon DCV offers the WebAuthn Redirection feature, specifically designed for use with Google Chrome and Microsoft Edge browsers. This functionality enables authentication in session for web applications. This feature operates through a dedicated browser extension that, once installed, redirects the WebAuthn requests from the web application to the DCV client.

Authorization is required to use this feature. Otherwise, it is not available in the client. For more information, see Configuring Amazon DCV Authorization in the Amazon DCV Administrator Guide.

**Note**  
WebAuthn redirection is supported only on Windows, Linux, and macOS clients. It is not supported on the web browser client.

## Webauthn Redirection user interface
<a name="webauthn-user-interface"></a>

The extension opens a user interface used to monitor and control the Webauthn Redirection feature.

![Webauthn user interface.](https://docs.aws.amazon.com/dcv/latest/userguide/images/webauthn-redirect-active.png)

+ **Extension Icon:** Located in the main body of user interface, this icon displays the feature's current state.

  The icon will be one of the following:


<table>
<thead>
  <tr><th>Icon</th><th>Name</th><th>Usage</th></tr>
</thead>
<tbody>
  <tr><td> <img src="https://docs.aws.amazon.com/dcv/latest/userguide/images/inactive-icon.png" alt="Inactive icon" /> </td><td>Inactive</td><td>Redirection is inactive. This occurs when you disable the extension.</td></tr>
  <tr><td> <img src="https://docs.aws.amazon.com/dcv/latest/userguide/images/stable-icon.png" alt="Active icon" /> </td><td>Ok (Active)</td><td>Redirection is active and connected to the underlying Amazon DCV software on the host.</td></tr>
  <tr><td> <img src="https://docs.aws.amazon.com/dcv/latest/userguide/images/processing-icon.png" alt="Processing icon" /> </td><td>Processing</td><td>Redirection is executing an operation in progress or is attempting to connect to the underlying Amazon DCV sofware in the host.</td></tr>
  <tr><td> <img src="https://docs.aws.amazon.com/dcv/latest/userguide/images/error-icon.png" alt="Error icon" /> </td><td>Error</td><td>There is an error connecting to the underlying Amazon DCV software on the host.</td></tr>
</tbody>
</table>

+ **Status Message:** Located in the main body of user interface, the message will explain the current operational status.
+ **Redirection Toggle:** Located at the bottom of the user interface, this switch enables or disables the feature.
  + Enabling redirection allows WebAuthn requests to be intercepted by the extension and forwarded to the client.
  + Disabling redirection allows WebAuthn requests to be processed locally by the browser.