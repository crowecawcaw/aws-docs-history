# Configuring Amazon DCV authentication

By default, clients are required to authenticate against the server where Amazon DCV is hosted before connecting to a Amazon DCV session. If the client
fails to authenticate, this is probably because it was prevented from connecting to the session. Client authentication requirements can be disabled
to allow clients to connect to a session without authenticating against the server.

Amazon DCV supports the following authentication methods:

- `system` — This is the default authentication method. Client
  authentication is delegated to the underlying operating system. For Windows Amazon DCV servers,
  authentication is delegated to WinLogon. For Linux Amazon DCV servers, authentication is
  delegated to PAM. Clients provide their system credentials when connecting to a Amazon DCV session.
  Verify that your clients have the appropriate sign-in credentials for the Amazon DCV server.
- `none` — No client authentication is required when connecting to a Amazon DCV session. The Amazon DCV server grants access to all clients
  that attempt to connect to a session.
  Make sure that your clients are aware of the authentication method used by the Amazon DCV server. They should also make sure that they have the
  information required to connect to the session.

###### Topics

- [Configuring authentication on Windows](#set-authentication-windows "#set-authentication-windows")
- [Configuring authentication on Linux](#set-authentication-linux "#set-authentication-linux")
- [Configuring authentication with external
  authenticators](#set-authentication-external "#set-authentication-external")
- [Use External Authentication](external-authentication.md "external-authentication.md")

## Configuring authentication on Windows

To change the Amazon DCV server's authentication method, you must configure the `authentication` parameter using the Windows
Registry Editor.

###### To change the authentication method on Windows

1. Open the Windows Registry Editor.
2. Navigate to the **HKEY_USERS\S-1-5-18\Software\GSettings\com\nicesoftware\dcv\security\*\* key and select the
   **authentication\*\* parameter.

If there's no `authentication` parameter in the registry key, create one:

    1. In the navigation pane, open the context (right-click) menu for the **authentication** key. Then, choose
     **New**, **string value**.
    2. For **Name**, enter `authentication` and press **Enter**.

3. Open the **authentication** parameter. For **Value data**, enter either `system` or
   `none`.
4. Choose **OK** and close the Windows Registry Editor.

### Windows Credentials Provider

With Windows Credentials Provider, users can bypass the Windows login if they can authenticate against the DCV server.

Windows Credentials Provider is only supported if the DCV `authentication` parameter is set to `system`. If the DCV
`authentication` parameter is set to `none`, users must manually sign in to Windows after they have been automatically
authenticated against the DCV server.

By default, Windows Credentials Provider is enabled when you install the Amazon DCV server.

###### To disable Windows Credentials Provider

1. Open the Windows Registry Editor.
2. Navigate to the **HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Authentication\Credential
   Providers\{8A2C93D0-D55F-4045-99D7-B27F5E263407}** key.
3. Choose **Edit**, **New**, **DWORD Value**.
4. For the name, enter `Disabled`.
5. Open the value. For **Value data**, enter `1` and choose **OK**.
6. Close the Windows Registry Editor.

###### To re-enable Windows Credentials Provider

1. Open the Windows Registry Editor.
2. Navigate to the **HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Authentication\Credential
   Providers\{8A2C93D0-D55F-4045-99D7-B27F5E263407}** key.
3. Open the **Disabled** value. For **Value data**, enter `0` and choose
   **OK**.
4. Close the Windows Registry Editor.

## Configuring authentication on Linux

To change the Amazon DCV server's authentication method, you must configure the `authentication` parameter in the
`dcv.conf` file.

###### To change the authentication method on Linux

1. Navigate to `/etc/dcv/` and open the `dcv.conf` with your preferred text editor.
2. Locate the `authentication` parameter in the `[security]` section. Then, replace the existing value with either
   `system` or `none`.

If there's no `authentication` parameter in the `[security]` section, add it using the following format.

```
[security]
authentication=`method`
```

3. Save and close the file.

### PAM service

On Linux, when Amazon DCV `authentication` parameter is set to `system`, the authentication is performed by executing a PAM
service.

By default, the Privileged Access Management (PAM) service executed by Amazon DCV server is `/etc/pam.d/dcv`.

If you want to change the steps performed by PAM when authenticating a user through Amazon DCV, you can set the `pam-service`
parameter in the `authentication` section of `dcv.conf`.

###### To change the PAM service

1. As root, navigate to the `/etc/pam.d` directory and create a new file, for instance `dcv-custom`.
2. Edit the `dcv-custom` file using your preferred text editor. Refer to your system documentation for the syntax of PAM service
   files.
3. Navigate to `/etc/dcv/` and open the `dcv.conf` with your preferred text editor.
4. Locate the `pam-service` parameter in the `[authentication]` section. Then, replace the existing service name with
   the new PAM service name.

If there's no `pam-service` parameter in the `[authentication]` section, add it manually using the following
format:

```
[authentication]
pam-service=`service_name`
```

###### Note

The PAM service name must match the name of the file you created in `/etc/pam.d`. 5. Save and close the file.

## Configuring authentication with external

authenticators

DCV can be configured to use an external authenticator. For more information on this process
and its requirements, see [Use External Authentication](external-authentication.md "external-authentication.md").
