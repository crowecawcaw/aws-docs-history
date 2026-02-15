# Configure System Integrity Protection for Amazon EC2 Mac instances

You can configure System Integrity Protection (SIP) settings for x86 Mac instances and
Apple silicon Mac instances. SIP is a critical macOS security feature that helps to
prevent unauthorized code execution and system-level modifications. For more information,
see [About System Integrity Protection](https://support.apple.com/en-us/102149 "https://support.apple.com/en-us/102149").

You can either enable or disable SIP completely, or you can selectively enable or disable
specific SIP settings. It is recommended that you disable SIP only temporarily to perform
necessary tasks, and then reenable it as soon as possible. Leaving SIP disabled could leave
your instance vulnerable to malicious code.

SIP configuration is supported in all AWS Regions where Amazon EC2 Mac instances are supported.

###### Topics

- [Considerations](#mac-sip-considerations "#mac-sip-considerations")
- [Default SIP configurations](#mac-sip-defaults "#mac-sip-defaults")
- [Check your SIP configuration](#mac-sip-check-settings "#mac-sip-check-settings")
- [Prerequisites for Apple silicon Mac instances](#mac-sip-prereqs "#mac-sip-prereqs")
- [Configure SIP settings](#mac-sip-configure "#mac-sip-configure")
- [Check SIP configuration task status](#mac-sip-state "#mac-sip-state")

## Considerations

- The following Amazon EC2 Mac instance types and macOS versions are supported:
  - **Mac1 | Mac2 | Mac2-m1ultra** — macOS
    Ventura (version 13.0 or later)
  - **Mac2-m2 | Mac2-m2pro** — macOS Ventura
    (version 13.2 or later)
  - **Mac-m4 | Mac-m4pro** — macOS Sequoia
    (version 15.6 or later)

###### Note

Beta and preview versions of macOS are not supported.

- You can specify a custom SIP configuration to selectively enable or disable
  individual SIP settings. If you implement a custom configuration, [connect to the instance and verify the
  settings](#mac-sip-check-settings "#mac-sip-check-settings") to ensure that your requirements are properly implemented
  and functioning as intended.

SIP configurations might change with macOS updates. We recommend that you
review custom SIP settings after any macOS version upgrade to ensure continued
compatibility and proper functionality of your security configurations.

- For x86 Mac instances, SIP settings are applied at the instance level. Any
  root volume attached to the instance will automatically inherit the configured
  SIP settings.

For Apple silicon Mac instances, SIP settings are applied at the volume level.
Root volumes attached to the instance do not inherit the SIP settings. If you
attach another root volume, you must reconfigure the SIP settings to the required
state.

- It can take up to 90 mins for SIP configuration tasks to complete. The instance
  remains unreachable while the SIP configuration task in progress.
- SIP configurations do not transfer to snapshots or AMIs that you subsequently
  create from the instance.
- Apple silicon Mac instances must have only one bootable volume, and each
  attached volume can have only one additional admin user.

## Default SIP configurations

The following table lists the default SIP configuration for x86 Mac instances
and Apple silicon Mac instances.

|                        | Apple silicon Mac instances | x86 Mac instances |
| ---------------------- | --------------------------- | ----------------- |
| Apple Internal         | Enabled                     | Disabled          |
| Filesystem Protections | Enabled                     | Disabled          |
| Base System            | Enabled                     | Enabled           |
| Debugging Restrictions | Enabled                     | Enabled           |
| Dtrace Restrictions    | Enabled                     | Enabled           |
| Kext Signing           | Enabled                     | Enabled           |
| Nvram Protections      | Enabled                     | Enabled           |

## Check your SIP configuration

We recommend that you check your SIP configuration before and after making changes
to ensure that it is configured as expected.

###### To check the SIP configuration for an Amazon EC2 Mac instance

[Connect to the instance using SSH](connect-to-mac-instance.md#mac-instance-ssh "connect-to-mac-instance.md#mac-instance-ssh"),
and then run the following command at the command line.

```
`$` csrutil status
```

The following is example output.

```
System Integrity Protection status: enabled.

Configuration:
    Apple Internal: enabled
    Kext Signing: disabled
    Filesystem Protections: enabled
    Debugging Restrictions: enabled
    DTrace Restrictions: enabled
    NVRAM Protections: enabled
    BaseSystem Verification: disabled
```

## Prerequisites for Apple silicon Mac instances

Before you can configure the SIP settings for Apple silicon Mac instances, you
must set a password and enable the secure token for the Amazon EBS root volume administrative
user (`ec2-user`).

###### Note

The password and secure token are set the first time you connect to an Apple
silicon Mac instance using the GUI. If you previously [connected to the instance using the GUI](connect-to-mac-instance.md#mac-instance-vnc "connect-to-mac-instance.md#mac-instance-vnc"), or if you are using an x86
Mac instance, you **do not** need to perform these
steps.

###### Note

All macOS usernames and passwords used for macOS authentication are required to be between 4 and 16 characters for use with SIP settings API calls.

###### To set a password and enable the secure token for the EBS root volume administrative user

1. [Connect to the instance using SSH](connect-to-mac-instance.md#mac-instance-ssh "connect-to-mac-instance.md#mac-instance-ssh").
2. Set the password for the `ec2-user` user.

```
`$` sudo /usr/bin/dscl . -passwd /Users/ec2-user
```

3. Enable the secure token for the `ec2-user` user. For `-oldPassword`,
   specify the same password from the previous step. For `-newPassword`, specify
   a different password. The following command assumes that you have your old and new passwords
   saved in `.txt` files.

```
`$` sysadminctl -oldPassword `cat old_password.txt` -newPassword `cat new_password.txt`
```

4. Verify that the secure token is enabled.

```
`$` sysadminctl -secureTokenStatus ec2-user
```

## Configure SIP settings

When you configure the SIP settings for your instance, you can either enable or
disable all SIP settings, or you can specify a custom configuration that selectively
enables or disables specific SIP settings.

###### Note

If you implement a custom configuration, [connect to the instance and verify the settings](#mac-sip-check-settings "#mac-sip-check-settings") to ensure that your
requirements are properly implemented and functioning as intended.

SIP configurations might change with macOS updates. We recommend that you
review custom SIP settings after any macOS version upgrade to ensure continued
compatibility and proper functionality of your security configurations.

To configure the SIP settings for your instance, you must create a SIP configuration
task. The SIP configuration task specifies the SIP settings for your instance.

When you create a SIP configuration for an Apple silicon Mac instance, you must specify
the following credentials:

- **Internal disk administrative user**
  - Username — Only the default administrative user (`aws-managed-user`)
    is supported and it is used by default. You can't specify a different
    administrative user.
  - Password — If you did not change the default password for
    `aws-managed-user`, specify the default password, which
    is _blank_. Otherwise, specify your password.

- **Amazon EBS root volume administrative user**
  - Username — If you did not change the default administrative
    user, specify `ec2-user`. Otherwise, specify the username
    for your administrative user.
  - Password — You must always specify the password.

Use the following methods to create a SIP configuration task.

Console

###### To create a SIP configuration task using the console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation panel, choose **Instances** and
   then select the Amazon EC2 Mac instance.
3. In the **Security** tab, choose **Modify
   Mac, Modify System Integrity Protection**.
4. To enable all SIP settings, select **Enable SIP**.
   To disable all SIP settings, clear **Enable SIP**.
5. To specify a custom configuration that selectively enables or disables
   specific SIP settings, select **Specify a custom SIP configuration**,
   and then select the SIP settings to enable, or clear the SIP settings
   to disable.
6. Specify the credentials for the root volume user and internal disk
   owner.
7. Choose **Create SIP modification task**.

AWS CLI

###### To create a SIP configuration task using the AWS CLI

Use the [create-mac-system-integrity-protection-modification-task](../../../cli/latest/reference/ec2/create-mac-system-integrity-protection-modification-task.md "../../../cli/latest/reference/ec2/create-mac-system-integrity-protection-modification-task.md") command.

###### Enable or disable all SIP settings

To completely enable or disable all SIP settings, use only the `--mac-system-integrity-protection-status`
parameter.

The following example command enables all SIP settings.

```
aws ec2 create-mac-system-integrity-protection-modification-task \
--instance-id `i-0abcdef9876543210` \
--mac-system-integrity-protection-status `enabled` \
--mac-credentials file://mac-credentials.json
```

###### Specify a custom SIP configuration

To specify a custom SIP configuration that selectively enables or disable specific
SIP settings, specify the `--mac-system-integrity-protection-status`
and `--mac-system-integrity-protection-configuration` parameters. In this
case, use `mac-system-integrity-protection-status` to specify the overall
SIP status, and use `mac-system-integrity-protection-configuration` to
selectively enable or disable individual SIP settings.

The following example command creates a SIP configuration task to enable all
SIP settings, except `NvramProtections` and `FilesystemProtections`.

```
aws ec2 create-mac-system-integrity-protection-modification-task \
--instance-id `i-0abcdef9876543210` \
--mac-system-integrity-protection-status `enabled` \
--mac-system-integrity-protection-configuration "`NvramProtections=disabled`, `FilesystemProtections=disabled`" \
--mac-credentials file://mac-credentials.json
```

The following example command creates a SIP configuration task to disable all SIP settings,
except `DtraceRestrictions`.

```
aws ec2 create-mac-system-integrity-protection-modification-task \
--instance-id `i-0abcdef9876543210` \
--mac-system-integrity-protection-status `disabled` \
--mac-system-integrity-protection-configuration "`DtraceRestrictions=enabled`" \
--mac-credentials file://mac-credentials.json
```

###### Contents of the `mac-credentials.json` file

The following is the contents of the `mac-credentials.json` file referenced
in the preceding examples.

```
{
  "internalDiskPassword":"*internal-disk-admin\_password*",
  "rootVolumeUsername":"*root-volume-admin\_username*",
  "rootVolumepassword":"*root-volume-admin\_password*"
}
```

## Check SIP configuration task status

Use one of the following methods to check the state of SIP configuration tasks.

Console

###### To view SIP configuration tasks using the console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation panel, choose **Instances** and
   then select the Amazon EC2 Mac instance.
3. In the **Security** tab, scroll down to the
   **Mac modification tasks** section.

AWS CLI

###### To check the state of SIP configuration tasks using the AWS CLI

Use the [describe-mac-modification-tasks](../../../cli/latest/reference/ec2/describe-mac-modification-tasks.md "../../../cli/latest/reference/ec2/describe-mac-modification-tasks.md") command.
