# Customize how users log in to their WorkSpaces in WorkSpaces Personal

Customize your users' access to WorkSpaces by using uniform resource identifiers
(URIs) to provide a simplified login experience that integrates with existing workflows
in your organization. For example, you can automatically generate login URIs that
register your users by using their WorkSpaces registration code. As a result:

- Users can bypass the manual registration process.
- Their usernames are automatically entered on their WorkSpaces client login page.
- If multi-factor authentication (MFA) is used in your organization, their usernames and MFA
  codes are automatically entered on their client login page.
  URI access works with both Region-based registration codes (for example, `WSpdx+ABC12D`) and fully
  qualified domain name (FQDN) based registration codes (for example, `desktop.example.com`). For more
  information about creating and using FQDN-based registration codes, see
  [Cross-Region redirection for WorkSpaces Personal](cross-region-redirection.md "cross-region-redirection.md").

You can configure URI access to WorkSpaces for client applications on the following supported
devices:

- Windows computers
- macOS computers
- Ubuntu Linux 18.04, 20.04, and 22.04 computers
- iPads
- Android devices
  To use URIs to access their WorkSpaces, users must first install the client application for their device by
  opening [https://clients.amazonworkspaces.com/](https://clients.amazonworkspaces.com/ "https://clients.amazonworkspaces.com/")

and following the directions.

URI access is supported on the Firefox and Chrome browsers on Windows and macOS computers, on the Firefox browser
on Ubuntu Linux 18.04, 20.04, and 22.04 computers, and on the Internet Explorer and Microsoft Edge browsers on Windows computers. For
more information about WorkSpaces clients, see [WorkSpaces Clients](../userguide/amazon-workspaces-clients.md "../userguide/amazon-workspaces-clients.md") in the
_Amazon WorkSpaces User Guide_.

###### Note

On Android devices, URI access works only with the Firefox browser, not with the Google Chrome browser.

To configure URI access to WorkSpaces, use any of the URI formats described in the
following table.

###### Note

If the data component of your URI includes any of the following reserved characters, we
recommend that you use percent-encoding in the data component to avoid ambiguity:

`@ : / ? & =`

For example, if you have usernames that include any of these characters, you
should percent-encode those usernames in your URI. For more information, see [Uniform Resource Identifier
(URI): Generic Syntax](https://www.rfc-editor.org/rfc/rfc3986.txt "https://www.rfc-editor.org/rfc/rfc3986.txt").

| Supported syntax                                   | Description                                                                                                                                                                                                                                        |
| -------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| workspaces://                                      | Opens the WorkSpaces client application. (Note: Using workspaces:// by itself<br>is not currently supported in the Linux client application.)                                                                                                      |
| workspaces://@registrationcode                     | Registers a user by using their WorkSpaces registration code. Also displays<br>the client login page.                                                                                                                                              |
| workspaces://username@registrationcode             | Registers a user by using their WorkSpaces registration code. Also<br>automatically enters the username in the **username**<br>field on the client login page.                                                                                     |
| workspaces://username@registrationcode?MFACode=mfa | Registers a user by using their WorkSpaces registration code. Also<br>automatically enters the username in the **username**<br>field and the multi-factor authentication (MFA) code in the<br>\*_MFA code_<br>• field on the client login<br>page. |
| workspaces://@registrationcode?MFACode=mfa         | Registers a user by using their WorkSpaces registration code. Also<br>automatically enters the multi-factor authentication (MFA) code in the<br>\*_MFA code_<br>• field on the client login<br>page.                                               |

###### Note

If users open a URI link when they are already connected to a WorkSpace from a Windows client,
a new WorkSpaces session opens and their original WorkSpaces session remains open. If
users open a URI link when they are connected to a WorkSpace from a macOS, iPad, or
Android client, no new session opens; only their original WorkSpaces session remains
open.
