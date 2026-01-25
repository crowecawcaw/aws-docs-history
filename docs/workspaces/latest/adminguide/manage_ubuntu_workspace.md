# Manage your Ubuntu WorkSpaces in WorkSpaces Personal

Your Ubuntu WorkSpaces bundle includes a subscription of Ubuntu Pro from Canonical. As with Windows and Amazon Linux WorkSpaces, Ubuntu WorkSpaces are domain joined, so you can use Active
Directory Users and Groups to:

- Administer your Ubuntu WorkSpaces
- Provide access to those WorkSpaces for users
  You can manage Ubuntu WorkSpaces with Group Policy by using ADsys. See the
  [Ubuntu Active Directory integration FAQ](https://ubuntu.com/blog/new-active-directory-integration-features-in-ubuntu-22-04-faq "https://ubuntu.com/blog/new-active-directory-integration-features-in-ubuntu-22-04-faq")
  for more information. You can also use other configuration and management solutions, such as
  [Landscape](https://ubuntu.com/landscape "https://ubuntu.com/landscape") and [Ansible](https://www.ansible.com/ "https://www.ansible.com/").

## Control DCV behavior on Ubuntu WorkSpaces

The behavior of DCV is controlled by configuration settings in the
`wsp.conf` file, which is located in the `/etc/wsp/`
directory. To deploy and enforce changes to the policy, use a configuration management
solution that supports Ubuntu. Any changes take effect when the agent starts up.

###### Note

If you make incorrect or unsupported changes to the `wsp.conf` policies may
not be applied to the new established connections to your WorkSpace.

The following sections describe how to enable or disable certain features.

## Enable or disable clipboard redirection for Ubuntu WorkSpaces

By default, WorkSpaces supports clipboard redirection. Use the DCV configuration file to disable this feature, if needed.

###### To enable or disable clipboard redirection for Ubuntu WorkSpaces

1. Open the `wsp.conf` file in an editor with elevated
   rights by using the following command.

```
[domain\username@workspace-id ~]$ sudo vi /etc/wsp/wsp.conf
```

2. Add the following line to the end of the `[policies]` group.

```
clipboard = `X`
```

Where the possible values for `X` are:

**enabled** — Clipboard redirection is enabled in both
directions (default)

**disabled** — Clipboard redirection is disabled in
both directions

**paste-only** — Clipboard redirection is enabled and
only allows you to copy contents from the local client device and paste it to the
remote host desktop

**copy-only** — Clipboard redirection is enabled
and only allows you to copy contents from the remote host desktop and paste it
to the local client device

## Enable or disable audio-in redirection for Ubuntu WorkSpaces

By default, WorkSpaces supports audio-in redirection. Use the DCV configuration file to disable this feature,
if needed.

###### To enable or disable audio-in redirection for Ubuntu WorkSpaces

1. Open the `wsp.conf` file in an editor with elevated
   rights by using the following command.

```
[domain\username@workspace-id ~]$ sudo vi /etc/wsp/wsp.conf
```

2. Add the following line to the end of the `[policies]` group.

```
audio-in = `X`
```

Where the possible values for `X` are:

**enabled** — Audio-in redirection is enabled (default)

**disabled** — Audio-in redirection is disabled

## Enable or disable video-in redirection for Ubuntu WorkSpaces

By default, WorkSpaces supports video-in redirection. Use the DCV configuration file to disable this feature,
if needed.

###### To enable or disable video-in redirection for Ubuntu WorkSpaces

1. Open the `wsp.conf` file in an editor with elevated
   rights by using the following command.

```
[domain\username@workspace-id ~]$ sudo vi /etc/wsp/wsp.conf
```

2. Add the following line to the end of the `[policies]` group.

```
video-in = `X`
```

Where the possible values for `X` are:

**enabled** — Video-in redirection is enabled (default)

**disabled** — Video-in redirection is disabled

## Enable or disable time zone redirection for Ubuntu WorkSpaces

By default, the time within a Workspace is set to mirror the time zone of the client that is being used
to connect to the WorkSpace. This behavior is controlled through time zone redirection. You might want to
turn off time zone direction for reasons such as the following:

- Your company wants all employees to work in a certain time zone (even if some employees are in other time zones).
- You have scheduled tasks in a WorkSpace that are meant to run at a certain time in a specific time zone.
- Your users travel a lot and want to keep their WorkSpaces in one time zone for consistency and personal preference.

Use the DCV configuration file to configure this feature, if needed.

###### To enable or disable time zone redirection for Ubuntu WorkSpaces

1. Open the `wsp.conf` file in an editor with elevated rights by using the following command.

```

[domain\username@workspace-id ~]$ sudo vi /etc/wsp/wsp.conf

```

2. Add the following line to the end of the `[policies]` group.

```

timezone-redirection = X

```

Where the possible values for `X` are:

**enabled** — Time zone redirection is enabled (default)

**disabled** — Time zone redirection is disabled

## Enable or disable printer redirection for Ubuntu WorkSpaces

By default, WorkSpaces supports printer redirection. Use the DCV configuration file to disable this feature,
if needed.

###### To enable or disable printer redirection for Ubuntu WorkSpaces

1. Open the `wsp.conf` file in an editor with elevated
   rights by using the following command.

```
[domain\username@workspace-id ~]$ sudo vi /etc/wsp/wsp.conf
```

2. Add the following line to the end of the `[policies]` group.

```
remote-printing = `X`
```

Where the possible values for `X` are:

**enabled** — Printer redirection is enabled (default)

**disabled** — Printer redirection is disabled

## Enable or disable disconnect session on screen lock for DCV

Enable disconnect session on screen lock to allow your users to end their WorkSpaces session when the lock screen is detected.
To reconnect from the WorkSpaces client, users can use their passwords or their smart cards to authenticate themselves,
depending on which type of authentication has been enabled for their WorkSpaces.

By default, WorkSpaces doesn’t support disconnecting session on screen lock. Use the DCV configuration file to enable this feature, if needed.

###### To enable or disable disconnect session on screen lock for Ubuntu WorkSpaces

1. Open the `wsp.conf` file in an editor with elevated rights by using the following command.

```
[domain\username@workspace-id ~]$ sudo vi /etc/wsp/wsp.conf
```

2. Add the following line to the end of the `[policies]` group.

```
disconnect-on-lock = X
```

Where the possible values for `X` are:

**enabled** — Disconnect on screen lock is enabled

**disabled** — Disconnect on screen lock is disabled (default)

## Grant SSH access to Ubuntu WorkSpaces administrators

By default, only assigned users and accounts in the Domain Admins group can connect to Ubuntu WorkSpaces by using SSH.
To enable other users and accounts to connect to Ubuntu WorkSpaces using SSH, we recommend that you create a dedicated
administrators group for your Ubuntu WorkSpaces administrators in Active Directory.

###### To enable sudo access for members of the `Linux_WorkSpaces_Admins` Active Directory group

1. Edit the `sudoers` file by using `visudo`, as shown in the following example.

```

[username@workspace-id ~]$ sudo visudo

```

2. Add the following line.

```

%Linux_WorkSpaces_Admins ALL=(ALL) ALL

```

After you create the dedicated administrators group, follow these steps to enable
login for members of the group.

###### To enable login for members of the `Linux_WorkSpaces_Admins` Active Directory group

1. Edit /`etc/security/access.conf` with elevated rights.

```

[username@workspace-id ~]$ sudo vi /etc/security/access.conf

```

2. Add the following line.

```

+:(Linux_WorkSpaces_Admins):ALL

```

With Ubuntu WorkSpaces you do not need to add a domain name
when specifying username for SSH connection, and by default, password authentication is disabled.
To connect via SSH, you needs to either add your SSH public key to `$HOME/.ssh/authorized_keys` on your Ubuntu WorkSpace, or
edit `/etc/ssh/sshd_config` to set PasswordAuthentication to `yes`. For more information about enabling SSH connections, see
[Enable SSH connections for your Linux WorkSpaces](connect-to-linux-workspaces-with-ssh.md "connect-to-linux-workspaces-with-ssh.md").

## Override the default shell for Ubuntu WorkSpaces

To override the default shell for Ubuntu WorkSpaces, we recommend that you edit the user's `~/.bashrc` file.
For example, to use `Z shell` instead of `Bash` shell, add the following lines to
`/home/username/.bashrc`.

```

export SHELL=$(which zsh)
[ -n "$SSH_TTY" ] && exec $SHELL

```

###### Note

After making this change, you must either reboot the WorkSpace or log out of the WorkSpace (not just disconnect)
and then log back in for the change to take effect.

## Use smart cards for authentication on Ubuntu WorkSpaces

Ubuntu WorkSpaces bundles allow the use of
[Common Access Card (CAC)](https://www.cac.mil/Common-Access-Card "https://www.cac.mil/Common-Access-Card")
and [Personal Identity Verification (PIV)](https://piv.idmanagement.gov/ "https://piv.idmanagement.gov/")
smart cards for authentication. For more information, see
[Use smart cards for authentication in WorkSpaces Personal](smart-cards.md "smart-cards.md").

## Configure device proxy server settings for internet

access

By default, the WorkSpaces client applications use the proxy server that’s
specified in the device operating system settings for HTTPS (port 443) traffic. The
Amazon WorkSpaces client applications use the HTTPS port for updates, registration, and
authentication.

###### Note

Proxy servers that require authentication with sign-in credentials are
not supported.

You can configure the device proxy server settings for your Ubuntu WorkSpaces through
Group Policy by following the steps in [Configure device proxy and internet connectivity settings](https://docs.microsoft.com/windows/security/threat-protection/microsoft-defender-atp/configure-proxy-internet "https://docs.microsoft.com/windows/security/threat-protection/microsoft-defender-atp/configure-proxy-internet") in the Microsoft
documentation.

For more information about configuring the proxy settings in the WorkSpaces Windows
client application, see [Proxy Server](../userguide/amazon-workspaces-windows-client.md#windows_proxy_server "../userguide/amazon-workspaces-windows-client.md#windows_proxy_server") in the _Amazon WorkSpaces User Guide_.

For more information about configuring the proxy settings in the WorkSpaces macOS
client application, see [Proxy Server](../userguide/amazon-workspaces-osx-client.md#osx_proxy_server "../userguide/amazon-workspaces-osx-client.md#osx_proxy_server") in the _Amazon WorkSpaces User Guide_.

For more information about configuring the proxy settings in the WorkSpaces Web Access
client application, see [Proxy Server](../userguide/amazon-workspaces-web-access.md#web-access-proxy "../userguide/amazon-workspaces-web-access.md#web-access-proxy") in the _Amazon WorkSpaces User Guide_.

### Proxying desktop traffic

For PCoIP WorkSpaces, the desktop client applications do not support the use of a proxy server nor TLS decryption and
inspection for port 4172 traffic in UDP (for desktop traffic). They require a direct connection to ports 4172.

For DCV WorkSpaces, the WorkSpaces Windows client application (version 5.1 and above) and macOS client application
(version 5.4 and above) support the use of HTTP proxy servers for port 4195 TCP traffic.
TLS decryption and inspection are not supported.

DCV does not support the use of proxy for desktop traffic over UDP. Only WorkSpaces Windows and macOS desktop client
applications and web access support the use of proxy, for TCP traffic.

###### Note

If you choose to use a proxy server, the API calls that the client application makes to the WorkSpaces services are also proxied.
Both API calls and desktop traffic should pass through the same proxy server.

### Recommendation on the use of proxy servers

We do not recommend the use of a proxy server with your WorkSpaces desktop traffic.

Amazon WorkSpaces desktop traffic is already encrypted, so proxies do not improve security. A proxy represents an additional
hop in the network path that could impact streaming quality by introducing latency. Proxies could also potentially reduce
throughput if a proxy is not properly sized to handle desktop streaming traffic. Furthermore, most proxies are not
designed for supporting long running WebSocket (TCP) connections and may affect streaming quality and stability.

If you must use a proxy, please locate your proxy server as close to the WorkSpace client as possible,
preferably in the same network, to avoid adding network latency, which could negatively impact streaming quality and responsiveness.
