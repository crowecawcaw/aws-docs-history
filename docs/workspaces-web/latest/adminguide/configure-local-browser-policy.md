# Configuring local browser policy for WebAuthn

In addition to enabling WebAuthn redirection in your portal settings, the local browser policy must be
configured to allow WebAuthn redirection between the user's local device and the remote
browser session and vice versa. This configuration is typically managed by IT administrators for enterprise
environments, or by individual users for BYOD scenarios.

The browser policy must include the WorkSpaces Secure Browser content domain for your region. Add the following
origin to the `WebAuthenticationRemoteDesktopAllowedOrigins` policy based on your
region:

`https://<region>.content.workspaces-web.com`

For example, in us-west-2: `https://us-west-2.content.workspaces-web.com`

The specific configuration method depends on whether you are managing browsers in an
enterprise environment or configuring individual devices for BYOD users. For more information
about the browser policy, see the [Chrome Enterprise policy documentation](https://chromeenterprise.google/policies/?policy=WebAuthenticationRemoteDesktopAllowedOrigins "https://chromeenterprise.google/policies/?policy=WebAuthenticationRemoteDesktopAllowedOrigins") and [Microsoft Edge policy documentation](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-policies#webauthenticationremotedesktopallowedorigins "https://learn.microsoft.com/en-us/deployedge/microsoft-edge-policies#webauthenticationremotedesktopallowedorigins").

###### Note

Browser restart may be required for the policy to take effect.
