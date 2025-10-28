# Manage your Amazon Linux 2 WorkSpaces in WorkSpaces Personal

For workloads that require RPM Package Manager (RPM), we recommend using [Red
Hat Enterprise Linux](manage_rhel_workspace.md "manage_rhel_workspace.md") or [Rocky Linux](manage_rockylinux_workspace.md "manage_rockylinux_workspace.md").
Amazon Linux 2 may not provide the latest versions of some applications and libraries, such as
Firefox and glibc, that you may need.

Because Linux instances do not adhere to Group Policy, we recommend that you use a
configuration management solution to distribute and enforce policy. For example, you can use
[Ansible](https://www.ansible.com/ "https://www.ansible.com/").

###### Note

Local printer redirection is not available for Amazon Linux WorkSpaces.

## Control DCV behavior on Amazon Linux WorkSpaces

The behavior of DCV is controlled by configuration settings in the
`wsp.conf` file, which is located in the `/etc/wsp/`
directory. To deploy and enforce changes to the policy, use a configuration management
solution that supports Amazon Linux. Any changes take effect when the agent starts up.

###### Note

- If you make incorrect or unsupported changes to the `wsp.conf` file,
  policy changes may not be applied to the newly established connections on your WorkSpace.
- Amazon Linux WorkSpaces on DCV bundles currently have the following limitations:
  - Currently only available in the AWS GovCloud (US-West) and AWS GovCloud (US-East).
  - Video-in is not supported.
  - Disconnect session on screen lock is not supported.

The following sections describe how to enable or disable certain features.

## Configure clipboard redirection for DCV Amazon Linux WorkSpaces

By default, WorkSpaces supports clipboard redirection. Use the DCV configuration file to configure
this feature, if needed. This setting takes effect when you disconnect and reconnect the WorkSpace.

###### To configure clipboard redirection for DCV Amazon Linux WorkSpaces

1. Open the `wsp.conf` file in an editor with elevated
   rights by using the following command.

```
[domain\username@workspace-id ~]$ sudo vi /etc/wsp/wsp.conf
```

2. ```
   clipboard = `X`
   ```

```

Where the possible values for `X` are:


`enabled` — Clipboard redirection is enabled in both directions (default)


`disabled` — Clipboard redirection is disabled in both directions


`paste-only` — Clipboard redirection is enabled but only allows you to copy contents from the local client device and paste it to the remote host desktop


`copy-only` — Clipboard redirection is enabled but only allows you to copy contents from the remote host desktop and paste it to the local client device

## Enable or disable audio-in redirection for DCV Amazon Linux WorkSpaces


By default, WorkSpaces supports audio-in redirection. Use the DCV configuration file to disable
 this feature, if needed. This setting takes effect when you disconnect and reconnect to the WorkSpace.


###### To enable or disable audio-in redirection for DCV Amazon Linux WorkSpaces

1. Open the `wsp.conf` file in an editor with elevated
 rights by using the following command.



```

[domain\username@workspace-id ~]$ sudo vi /etc/wsp/wsp.conf

```
2. Add the following line to the end of the file.



```

audio-in = `X`

```

Where the possible values for `X` are:


`enabled` — Audio-in redirection is enabled (default)


`disabled` — Audio-in redirection is disabled

## Enable or disable time zone redirection for DCV Amazon Linux WorkSpaces


By default, the time within a Workspace is set to mirror the time zone of the client that
 is being used to connect to the WorkSpace. This behavior is controlled through time zone
 redirection. You might want to turn off time zone direction for reasons such as the following:



* Your company wants all employees to work in a certain time zone (even if some
 employees are in other time zones).
* You have scheduled tasks in a WorkSpace that are meant to run at a certain time in
 a specific time zone.
* Your users who travel a lot want to keep their WorkSpaces in one time zone for
 consistency and personal preference.

Use the DCV configuration file to configure this feature, if needed. This setting takes effect
 after you disconnect and reconnect to the WorkSpace.


###### To enable or disable time zone redirection for DCV Amazon Linux WorkSpaces

1. Open the `wsp.conf` file in an editor with elevated
 rights by using the following command.



```

[domain\username@workspace-id ~]$ sudo vi /etc/wsp-agent/wsp.conf

```
2. Add the following line to the end of the file.



```

timezone_redirect= `X`

```

Where the possible values for `X` are:


**enabled** — Time zone redirection is enabled (default)


**disabled** — Time zone redirection is disabled

## Control PCoIP Agent behavior on Amazon Linux WorkSpaces


The behavior of the PCoIP Agent is controlled by configuration settings in the
 `pcoip-agent.conf` file, which is located in the `/etc/pcoip-agent/`
 directory. To deploy and enforce changes to the policy, use a configuration management
 solution that supports Amazon Linux. Any changes take effect when the agent starts up. Restarting
 the agent ends any open connections and restarts the window manager. To apply any changes,
 we recommend rebooting the WorkSpace.


###### Note

If you make incorrect or unsupported changes to the `pcoip-agent.conf` file,
 you might cause your WorkSpace to stop working. If your WorkSpace stops working, you might need to
 either [connect to your WorkSpace using SSH](connect-to-linux-workspaces-with-ssh.md "connect-to-linux-workspaces-with-ssh.md")
 to roll back the changes, or you might have to [rebuild the WorkSpace](rebuild-workspace.md "rebuild-workspace.md").


The following sections describe how to enable or disable certain features. For a full listing of the
 available settings, run `man pcoip-agent.conf` from the terminal on any Amazon Linux WorkSpace.


## Configure clipboard redirection for PCoIP Amazon Linux WorkSpaces


By default, WorkSpaces supports clipboard redirection. Use the PCoIP Agent conf to disable
 this feature, if needed. This setting takes effect when you reboot the WorkSpace.


###### To configure clipboard redirection for PCoIP Amazon Linux WorkSpaces

1. Open the `pcoip-agent.conf` file in an editor with elevated
 rights by using the following command.



```

[domain\username@workspace-id ~]$ sudo vi /etc/pcoip-agent/pcoip-agent.conf

```
2. Add the following line to the end of the file.



```

pcoip.server_clipboard_state = `X`

```

Where the possible values for `X` are:


0 — Clipboard redirection is disabled in both directions


1 — Clipboard redirection is enabled in both directions


2 — Clipboard redirection is enabled client to agent only (allow copy and paste only from local client device
 to the remote host desktop)


3 — Clipboard redirection is enabled agent to client only (allow copy and paste only from the remote host desktop
 to the local client device)

###### Note

Clipboard redirection is implemented as a virtual channel. If virtual channels are disabled,
 clipboard redirection doesn't work. To enable virtual channels, see
 [PCoIP Virtual Channels](https://www.teradici.com/web-help/pcoip_agent/standard_agent/linux/20.07/admin-guide/configuring/configuring/#pcoip-virtual-channels "https://www.teradici.com/web-help/pcoip_agent/standard_agent/linux/20.07/admin-guide/configuring/configuring/#pcoip-virtual-channels") in the Teradici documentation.


## Enable or disable audio-in redirection for PCoIP Amazon Linux WorkSpaces


By default, WorkSpaces supports audio-in redirection. Use the PCoIP Agent conf to disable
 this feature, if needed. This setting takes effect when you reboot the WorkSpace.


###### To enable or disable audio-in redirection for PCoIP Amazon Linux WorkSpaces

1. Open the `pcoip-agent.conf` file in an editor with elevated
 rights by using the following command.



```

[domain\username@workspace-id ~]$ sudo vi /etc/pcoip-agent/pcoip-agent.conf

```
2. Add the following line to the end of the file.



```

pcoip.enable_audio = `X`

```

Where the possible values for `X` are:


0 — Audio-in redirection is disabled


1 — Audio-in redirection is enabled

## Enable or disable time zone redirection for PCoIP Amazon Linux WorkSpaces


By default, the time within a Workspace is set to mirror the time zone of the client that
 is being used to connect to the WorkSpace. This behavior is controlled through time zone
 redirection. You might want to turn off time zone direction for reasons such as the following:



* Your company wants all employees to work in a certain time zone (even if some
 employees are in other time zones).
* You have scheduled tasks in a WorkSpace that are meant to run at a certain time in
 a specific time zone.
* Your users who travel a lot want to keep their WorkSpaces in one time zone for
 consistency and personal preference.

If needed for Linux WorkSpaces, you can use the PCoIP Agent conf to disable this feature.
 This setting takes effect when you reboot the WorkSpace.


###### To enable or disable time zone redirection for PCoIP Amazon Linux WorkSpaces

1. Open the `pcoip-agent.conf` file in an editor with elevated
 rights by using the following command.



```

[domain\username@workspace-id ~]$ sudo vi /etc/pcoip-agent/pcoip-agent.conf

```
2. Add the following line to the end of the file.



```

pcoip.enable_timezone_redirect= `X`

```

Where the possible values for `X` are:


0 — Time zone redirection is disabled


1 — Time zone redirection is enabled

## Grant SSH access to Amazon Linux WorkSpaces administrators


By default, only assigned users and accounts in the Domain Admins group can connect to
 Amazon Linux WorkSpaces by using SSH.


We recommend that you create a dedicated administrators group for your Amazon Linux WorkSpaces
 administrators in Active Directory.


###### To enable sudo access for members of the Linux\_Workspaces\_Admins Active Directory
 group

1. Edit the `sudoers` file by using `visudo`, as
 shown in the following example.



```

[example\username@workspace-id ~]$ sudo visudo

```
2. Add the following line.



```

%example.com\\Linux_WorkSpaces_Admins ALL=(ALL) ALL

```

After you create the dedicated administrators group, follow these steps to enable
 login for members of the group.


###### To enable login for members of the Linux\_WorkSpaces\_Admins Active Directory
 group

1. Edit `/etc/security/access.conf` with elevated
 rights.



```

[example\username@workspace-id ~]$ sudo vi /etc/security/access.conf

```
2. Add the following line.



```

+:(example\Linux_WorkSpaces_Admins):ALL

```

For more information about enabling SSH connections, see [Enable SSH connections for
 your Linux WorkSpaces in WorkSpaces Personal](connect-to-linux-workspaces-with-ssh.md "connect-to-linux-workspaces-with-ssh.md").


## Override the default shell for Amazon Linux WorkSpaces


To override the default shell for Linux WorkSpaces, we recommend that you edit the
 user's `~/.bashrc` file. For example, to use `Z shell`
 instead of `Bash` shell, add the following lines to
 `/home/`username`/.bashrc`.



```

export SHELL=$(which zsh)
[ -n "$SSH_TTY" ] && exec $SHELL

```

###### Note

After making this change, you must either reboot the WorkSpace or log out of the
 WorkSpace (not just disconnect) and then log back in for the change to take effect.


## Protect custom repositories from unauthorized access


To control access to your custom repositories, we recommend using the security
 features built into Amazon Virtual Private Cloud (Amazon VPC) rather than using passwords. For example, use
 network access control lists (ACLs) and security groups. For more information about
 these features, see [Security](../../../vpc/latest/userguide/VPC_Security.md "../../../vpc/latest/userguide/VPC_Security.md") in the
 *Amazon VPC User Guide*.


If you must use passwords to protect your repositories, be sure to create your
 `yum` repository definition files as shown in [Repository Definition Files](https://docs.fedoraproject.org/en-US/Fedora_Core/3/html/Software_Management_Guide/sn-writing-repodefs.html "https://docs.fedoraproject.org/en-US/Fedora_Core/3/html/Software_Management_Guide/sn-writing-repodefs.html") in the Fedora documentation.


## Use the Amazon Linux Extras Library repository


With Amazon Linux, you can use the Extras Library to install application and software updates
 on your instances. For information about using the Extras Library, see [Extras Library
 (Amazon Linux)](../../../AWSEC2/latest/UserGuide/amazon-linux-ami-basics.md#extras-library "../../../AWSEC2/latest/UserGuide/amazon-linux-ami-basics.md#extras-library") in the *Amazon EC2 User Guide for Linux
 Instances*.


###### Note

If you are using the Amazon Linux repository, your Amazon Linux WorkSpaces must have internet
 access, or you must configure virtual private cloud (VPC) endpoints to this
 repository and to the main Amazon Linux repository. For more information, see [Provide internet access for WorkSpaces Personal](amazon-workspaces-internet-access.md "amazon-workspaces-internet-access.md").


## Use smart cards for authentication on Linux WorkSpaces


Linux WorkSpaces on DCV bundles allow the use of
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


You can configure the device proxy server settings for your Linux WorkSpaces through
 Group Policy by following the steps in  [Configure device proxy and internet connectivity settings](https://docs.microsoft.com/windows/security/threat-protection/microsoft-defender-atp/configure-proxy-internet "https://docs.microsoft.com/windows/security/threat-protection/microsoft-defender-atp/configure-proxy-internet") in the Microsoft
 documentation.


For more information about configuring the proxy settings in the WorkSpaces Windows
 client application, see  [Proxy Server](../userguide/amazon-workspaces-windows-client.md#windows_proxy_server "../userguide/amazon-workspaces-windows-client.md#windows_proxy_server") in the *Amazon WorkSpaces User Guide*.


For more information about configuring the proxy settings in the WorkSpaces macOS
 client application, see  [Proxy Server](../userguide/amazon-workspaces-osx-client.md#osx_proxy_server "../userguide/amazon-workspaces-osx-client.md#osx_proxy_server") in the *Amazon WorkSpaces User Guide*.


For more information about configuring the proxy settings in the WorkSpaces Web Access
 client application, see  [Proxy Server](../userguide/amazon-workspaces-web-access.md#web-access-proxy "../userguide/amazon-workspaces-web-access.md#web-access-proxy") in the *Amazon WorkSpaces User Guide*.


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
```
