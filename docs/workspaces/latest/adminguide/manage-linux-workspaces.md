

# Manage your Linux WorkSpaces in WorkSpaces Personal
<a name="manage-linux-workspaces"></a>

Amazon WorkSpaces supports the following Linux operating systems for WorkSpaces Personal:
+ Ubuntu 22.04 LTS and Ubuntu 24.04 LTS
+ Red Hat Enterprise Linux 8 and Red Hat Enterprise Linux 9
+ Rocky Linux 8 and Rocky Linux 9

All Linux WorkSpaces use DCV for streaming and SSSD for Active Directory integration. They share the same configuration model and management procedures described on this page.

**Note**  
Amazon Linux 2 WorkSpaces use a different technology stack and are documented separately. See [Manage your Amazon Linux 2 WorkSpaces in WorkSpaces Personal](manage_linux_workspace.md). Amazon Linux 2 reaches end-of-life on June 30, 2026.

**Topics**
+ [Distribution-specific notes](#linux_distro_notes)
+ [Active Directory integration](#linux_ad_integration)
+ [Control DCV behavior on Linux WorkSpaces](#linux_wsp_control)
+ [Enable or disable clipboard redirection](#linux_dcv_clipboard)
+ [Enable or disable audio-in redirection](#linux_audio_in)
+ [Enable or disable video-in redirection](#linux_video_in)
+ [Enable or disable time zone redirection](#linux_dcv_time_zone)
+ [Enable or disable printer redirection](#linux_printer)
+ [Enable or disable disconnect session on screen lock](#linux_screenlock)
+ [Grant SSH access to Linux WorkSpaces administrators](#linux_ssh_access)
+ [Override the default shell](#linux_shell_override)
+ [Use smart cards for authentication on Linux WorkSpaces](#linux_smart_cards)

## Distribution-specific notes
<a name="linux_distro_notes"></a>

### Ubuntu
<a name="linux_distro_ubuntu"></a>

Your Ubuntu WorkSpaces bundle includes a subscription of Ubuntu Pro from Canonical. You can manage Ubuntu WorkSpaces with Group Policy by using ADsys. See the [Ubuntu Active Directory integration FAQ](https://ubuntu.com/blog/new-active-directory-integration-features-in-ubuntu-22-04-faq) for more information. You can also use other configuration and management solutions, such as [Landscape](https://ubuntu.com/landscape) and [Ansible](https://www.ansible.com/).

### Rocky Linux
<a name="linux_distro_rocky"></a>

You can manage Rocky Linux WorkSpaces with configuration and management solutions, such as [Ansible](https://www.ansible.com/).

**Note**  
You may not remove, modify, or obscure any copyright, trademark, or other proprietary or confidentiality notices that are contained in or on the Rocky Linux software.

### Red Hat Enterprise Linux
<a name="linux_distro_rhel"></a>

You can manage Red Hat Enterprise Linux WorkSpaces with configuration and management solutions, such as [Ansible](https://www.ansible.com/).

## Active Directory integration
<a name="linux_ad_integration"></a>

Linux WorkSpaces use SSSD (System Security Services Daemon) for Active Directory integration. SSSD assigns stable POSIX user IDs derived from the Active Directory SID, ensuring consistent file ownership across rebuilds and migrations.

The SSSD configuration is managed by the WorkSpaces provisioning system. Key characteristics:
+ All Linux WorkSpaces use DCV for streaming and SSSD for Active Directory integration.
+ Forest Trust is not supported. Use external trust instead.
+ Smart card authentication uses SSSD's PKINIT integration. See [Enable smart cards for Linux WorkSpaces](smart-cards.md#smart-cards-linux-workspaces).

## Control DCV behavior on Linux WorkSpaces
<a name="linux_wsp_control"></a>

The behavior of DCV is controlled by configuration settings in the `wsp.conf` file, which is located in the `/etc/wsp/` directory. To deploy and enforce changes to the policy, use a configuration management solution such as [Ansible](https://www.ansible.com/). Any changes take effect when the agent starts up.

**Note**  
If you make incorrect or unsupported changes to the `wsp.conf` file, policies may not be applied to newly established connections to your WorkSpace.

The following sections describe how to enable or disable certain features.

## Enable or disable clipboard redirection
<a name="linux_dcv_clipboard"></a>

By default, WorkSpaces supports clipboard redirection. Use the DCV configuration file to disable this feature, if needed.

**To enable or disable clipboard redirection for Linux WorkSpaces**

1. Open the `wsp.conf` file in an editor with elevated rights by using the following command.

   ```
   [domain\username@workspace-id ~]$ sudo vi /etc/wsp/wsp.conf
   ```

1. Add the following line to the end of the `[policies]` group.

   ```
   clipboard = {{X}}
   ```

   Where the possible values for {{X}} are:

   **enabled** — Clipboard redirection is enabled in both directions (default)

   **disabled** — Clipboard redirection is disabled in both directions

   **paste-only** — Clipboard redirection is enabled and only allows you to copy contents from the local client device and paste it to the remote host desktop

   **copy-only** — Clipboard redirection is enabled and only allows you to copy contents from the remote host desktop and paste it to the local client device

## Enable or disable audio-in redirection
<a name="linux_audio_in"></a>

By default, WorkSpaces supports audio-in redirection. Use the DCV configuration file to disable this feature, if needed.

**To enable or disable audio-in redirection for Linux WorkSpaces**

1. Open the `wsp.conf` file in an editor with elevated rights by using the following command.

   ```
   [domain\username@workspace-id ~]$ sudo vi /etc/wsp/wsp.conf
   ```

1. Add the following line to the end of the `[policies]` group.

   ```
   audio-in = {{X}}
   ```

   Where the possible values for {{X}} are:

   **enabled** — Audio-in redirection is enabled (default)

   **disabled** — Audio-in redirection is disabled

## Enable or disable video-in redirection
<a name="linux_video_in"></a>

By default, WorkSpaces supports video-in redirection. Use the DCV configuration file to disable this feature, if needed.

**Note**  
Video-in redirection is not supported on Red Hat Enterprise Linux WorkSpaces. This feature requires DKMS and the video loopback driver, which are not available in the standard Red Hat Enterprise Linux repository. Video-in is available on Ubuntu and Rocky Linux WorkSpaces.

**To enable or disable video-in redirection for Linux WorkSpaces**

1. Open the `wsp.conf` file in an editor with elevated rights by using the following command.

   ```
   [domain\username@workspace-id ~]$ sudo vi /etc/wsp/wsp.conf
   ```

1. Add the following line to the end of the `[policies]` group.

   ```
   video-in = {{X}}
   ```

   Where the possible values for {{X}} are:

   **enabled** — Video-in redirection is enabled (default)

   **disabled** — Video-in redirection is disabled

## Enable or disable time zone redirection
<a name="linux_dcv_time_zone"></a>

By default, the time within a WorkSpace is set to mirror the time zone of the client that is being used to connect to the WorkSpace. This behavior is controlled through time zone redirection. You might want to turn off time zone redirection for reasons such as the following:
+ Your company wants all employees to work in a certain time zone (even if some employees are in other time zones).
+ You have scheduled tasks in a WorkSpace that are meant to run at a certain time in a specific time zone.
+ Your users travel a lot and want to keep their WorkSpaces in one time zone for consistency and personal preference.

Use the DCV configuration file to configure this feature, if needed.

**To enable or disable time zone redirection for Linux WorkSpaces**

1. Open the `wsp.conf` file in an editor with elevated rights by using the following command.

   ```
   [domain\username@workspace-id ~]$ sudo vi /etc/wsp/wsp.conf
   ```

1. Add the following line to the end of the `[policies]` group.

   ```
   timezone-redirection = {{X}}
   ```

   Where the possible values for {{X}} are:

   **enabled** — Time zone redirection is enabled (default)

   **disabled** — Time zone redirection is disabled

## Enable or disable printer redirection
<a name="linux_printer"></a>

By default, WorkSpaces supports printer redirection. Use the DCV configuration file to disable this feature, if needed.

**To enable or disable printer redirection for Linux WorkSpaces**

1. Open the `wsp.conf` file in an editor with elevated rights by using the following command.

   ```
   [domain\username@workspace-id ~]$ sudo vi /etc/wsp/wsp.conf
   ```

1. Add the following line to the end of the `[policies]` group.

   ```
   remote-printing = {{X}}
   ```

   Where the possible values for {{X}} are:

   **enabled** — Printer redirection is enabled (default)

   **disabled** — Printer redirection is disabled

## Enable or disable disconnect session on screen lock
<a name="linux_screenlock"></a>

Enable disconnect session on screen lock to allow your users to end their WorkSpaces session when the lock screen is detected. To reconnect from the WorkSpaces client, users can use their passwords or their smart cards to authenticate themselves, depending on which type of authentication has been enabled for their WorkSpaces.

By default, WorkSpaces doesn't support disconnecting session on screen lock. Use the DCV configuration file to enable this feature, if needed.

**To enable or disable disconnect session on screen lock for Linux WorkSpaces**

1. Open the `wsp.conf` file in an editor with elevated rights by using the following command.

   ```
   [domain\username@workspace-id ~]$ sudo vi /etc/wsp/wsp.conf
   ```

1. Add the following line to the end of the `[policies]` group.

   ```
   disconnect-on-lock = {{X}}
   ```

   Where the possible values for {{X}} are:

   **enabled** — Disconnect on screen lock is enabled

   **disabled** — Disconnect on screen lock is disabled (default)

## Grant SSH access to Linux WorkSpaces administrators
<a name="linux_ssh_access"></a>

By default, only assigned users and accounts in the Domain Admins group can connect to Linux WorkSpaces by using SSH. To enable other users and accounts to connect using SSH, we recommend that you create a dedicated administrators group for your Linux WorkSpaces administrators in Active Directory.

**To enable sudo access for members of the `Linux_WorkSpaces_Admins` Active Directory group**

1. Edit the `sudoers` file by using `visudo`, as shown in the following example.

   ```
   [username@workspace-id ~]$ sudo visudo
   ```

1. Add the following line.

   ```
   %Linux_WorkSpaces_Admins ALL=(ALL) ALL
   ```

After you create the dedicated administrators group, follow these steps to enable login for members of the group.

**To enable login for members of the `Linux_WorkSpaces_Admins` Active Directory group**

1. Edit `/etc/security/access.conf` with elevated rights.

   ```
   [username@workspace-id ~]$ sudo vi /etc/security/access.conf
   ```

1. Add the following line.

   ```
   +:(Linux_WorkSpaces_Admins):ALL
   ```

With Linux WorkSpaces you do not need to add a domain name when specifying a username for SSH connection, and by default, password authentication is disabled. To connect via SSH, you need to either add your SSH public key to `$HOME/.ssh/authorized_keys` on your WorkSpace, or edit `/etc/ssh/sshd_config` to set PasswordAuthentication to `yes`. For more information about enabling SSH connections, see [Enable SSH connections for your Linux WorkSpaces in WorkSpaces Personal](connect-to-linux-workspaces-with-ssh.md).

## Override the default shell
<a name="linux_shell_override"></a>

To override the default shell for Linux WorkSpaces, we recommend that you edit the user's `~/.bashrc` file. For example, to use `Z shell` instead of `Bash` shell, add the following lines to `/home/{{username}}/.bashrc`.

```
export SHELL=$(which zsh)
[ -n "$SSH_TTY" ] && exec $SHELL
```

**Note**  
After making this change, you must either reboot the WorkSpace or log out of the WorkSpace (not just disconnect) and then log back in for the change to take effect.

## Use smart cards for authentication on Linux WorkSpaces
<a name="linux_smart_cards"></a>

Linux WorkSpaces allow the use of [Common Access Card (CAC)](https://www.cac.mil/Common-Access-Card) and [Personal Identity Verification (PIV)](https://piv.idmanagement.gov/) smart cards for authentication. All Linux WorkSpaces share the same smart card implementation using SSSD and PKINIT. For more information, see [Enable smart cards for Linux WorkSpaces](smart-cards.md#smart-cards-linux-workspaces).