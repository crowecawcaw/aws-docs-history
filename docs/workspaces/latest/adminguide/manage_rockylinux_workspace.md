# Manage your Rocky Linux WorkSpaces

You can manage Rocky Linux WorkSpaces with configuration and management solutions, such as
[Ansible](https://www.ansible.com/ "https://www.ansible.com/").

###### Note

You may not remove, modify, or obscure any copyright, trademark, or other proprietary
or confidentiality notices that are contained in or on the Rocky Linux software.

## Control DCV behavior on Rocky Linux WorkSpaces

The behavior of DCV is controlled by configuration settings in the
`wsp.conf` file, which is located in the `/etc/wsp/`
directory. To deploy and enforce changes to the policy, use a configuration management
solution that supports Rocky Linux. Any changes take effect when the agent starts up.

###### Note

If you make incorrect or unsupported changes to the `wsp.conf` policies may
not be applied to the new established connections to your WorkSpace.

The following sections describe how to enable or disable certain features.

## Enable or disable clipboard redirection for Rocky Linux WorkSpaces

By default, WorkSpaces supports clipboard redirection. Use the DCV configuration file to disable this feature, if needed.

###### To enable or disable clipboard redirection for Rocky Linux WorkSpaces

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

## Enable or disable audio-in redirection for Rocky Linux WorkSpaces

By default, WorkSpaces supports audio-in redirection. Use the DCV configuration file to disable this feature,
if needed.

###### To enable or disable audio-in redirection for Rocky Linux WorkSpaces

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

## Enable or disable video-in redirection for Rocky Linux WorkSpaces

By default, WorkSpaces supports video-in redirection. Use the DCV configuration file to disable this feature,
if needed.

###### To enable or disable video-in redirection for Rocky Linux WorkSpaces

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

## Enable or disable time zone redirection for Rocky Linux WorkSpaces

By default, the time within a Workspace is set to mirror the time zone of the client that is being used
to connect to the WorkSpace. This behavior is controlled through time zone redirection. You might want to
turn off time zone direction for reasons such as the following:

- Your company wants all employees to work in a certain time zone (even if some employees are in other time zones).
- You have scheduled tasks in a WorkSpace that are meant to run at a certain time in a specific time zone.
- Your users travel a lot and want to keep their WorkSpaces in one time zone for consistency and personal preference.

Use the DCV configuration file to configure this feature, if needed.

###### To enable or disable time zone redirection for Rocky Linux WorkSpaces

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

## Enable or disable printer redirection for Rocky Linux WorkSpaces

By default, WorkSpaces supports printer redirection. Use the DCV configuration file to disable this feature,
if needed.

###### To enable or disable printer redirection for Rocky Linux WorkSpaces

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

###### To enable or disable disconnect session on screen lock for Rocky Linux WorkSpaces

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

## Grant SSH access to Rocky Linux WorkSpaces administrators

By default, only assigned users and accounts in the Domain Admins group can connect to Rocky Linux WorkSpaces by using SSH.
To enable other users and accounts to connect to Rocky Linux WorkSpaces using SSH, we recommend that you create a dedicated
administrators group for your Rocky Linux WorkSpaces administrators in Active Directory.

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

With Rocky Linux WorkSpaces you do not need to add a domain name
when specifying username for SSH connection, and by default, password authentication is disabled.
To connect via SSH, you needs to either add your SSH public key to `$HOME/.ssh/authorized_keys` on your Rocky Linux WorkSpace, or
edit `/etc/ssh/sshd_config` to set PasswordAuthentication to `yes`. For more information about enabling SSH connections, see
[Enable SSH connections for your Linux WorkSpaces](connect-to-linux-workspaces-with-ssh.md "connect-to-linux-workspaces-with-ssh.md").

## Override the default shell for Rocky Linux WorkSpaces

To override the default shell for Rocky Linux WorkSpaces, we recommend that you edit the user's `~/.bashrc` file.
For example, to use `Z shell` instead of `Bash` shell, add the following lines to
`/home/username/.bashrc`.

```

export SHELL=$(which zsh)
[ -n "$SSH_TTY" ] && exec $SHELL

```

###### Note

After making this change, you must either reboot the WorkSpace or log out of the WorkSpace (not just disconnect)
and then log back in for the change to take effect.
