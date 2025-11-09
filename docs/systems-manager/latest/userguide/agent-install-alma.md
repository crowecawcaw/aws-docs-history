AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Manually install SSM Agent on AlmaLinux

instances

Use the information in this section to help you manually install or reinstall
SSM Agent on an AlmaLinux instance.

###### Before you begin

Before you install SSM Agent on an AlmaLinux instance, note the
following:

- Ensure that Python 3 is installed on your AlmaLinux instance. This is
  required in order for SSM Agent to work properly.
- For important information that applies to installation of SSM Agent on
  all Linux-based operating systems, see [Manually installing and
  uninstalling SSM Agent on EC2 instances for Linux](manually-install-ssm-agent-linux.md "manually-install-ssm-agent-linux.md").

###### Topics

- [Quick installation commands for
  SSM Agent on AlmaLinux](#quick-install-alma "#quick-install-alma")
- [Create custom agent installation commands
  for AlmaLinux in your Region](#custom-url-alma "#custom-url-alma")

## Quick installation commands for

SSM Agent on AlmaLinux

Use the following steps to manually install SSM Agent on a single instance.
This procedure uses globally available installation files.

###### Before you begin

Before you install SSM Agent on a AlmaLinux instance, note the
following:

- Ensure that Python 3 is installed on your AlmaLinux instance. This
  is required in order for SSM Agent to work properly.

###### To install SSM Agent on AlmaLinux

1. Connect to your AlmaLinux instance using your preferred method,
   such as SSH.
2. Copy the command for your instance’s architecture and run it on
   the instance.

###### Note

Even though URLs in the following commands include an
`ec2-downloads-windows` directory, these
are the correct global installation files for AlmaLinux.

x86_64 instances

```
sudo dnf install -y https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/linux_amd64/amazon-ssm-agent.rpm
```

ARM64 instances

```
sudo dnf install -y https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/linux_arm64/amazon-ssm-agent.rpm
```

3. (Recommended) Run the following command to verify that the agent
   is running.

```
sudo systemctl status amazon-ssm-agent
```

In most cases, the command reports that the agent is running, as
shown in the following example.

```
● amazon-ssm-agent.service - amazon-ssm-agent
   Loaded: loaded (/etc/systemd/system/amazon-ssm-agent.service; enabled; vendo>
   Active: active (running) since Tue 2025-04-19 16:40:41 UTC; 9s ago
 Main PID: 4898 (amazon-ssm-agen)
    Tasks: 14 (limit: 4821)
   Memory: 34.6M
   CGroup: /system.slice/amazon-ssm-agent.service
           ├─4898 /usr/bin/amazon-ssm-agent
           └─4954 /usr/bin/ssm-agent-worker
            --truncated--
```

In rare cases, the command reports that the agent is installed but
not running, as shown in the following example.

```
● amazon-ssm-agent.service - amazon-ssm-agent
   Loaded: loaded (/etc/systemd/system/amazon-ssm-agent.service; enabled; vendo>
   Active: inactive (dead) since Tue 2025-04-19 16:42:05 UTC; 2s ago
            --truncated--
```

To activate the agent in these cases, run the following
commands.

```
sudo systemctl enable amazon-ssm-agent
```

```
sudo systemctl start amazon-ssm-agent
```

## Create custom agent installation commands

for AlmaLinux in your Region

When you install SSM Agent on multiple instances using a script or
template, we recommend using installation files that are stored in the
AWS Region you're working in.

For the following commands, we provide examples that use a publicly
accessible S3 bucket in the US East (Ohio) Region (`us-east-2`).

###### Tip

You can also replace a global URL in the procedure [Quick installation commands for
SSM Agent on AlmaLinux](#quick-install-alma "#quick-install-alma")
earlier in this topic with a custom Regional URL you construct.

In the following command, replace `region` with your own
information. For a list of supported `region` values, see the
**Region** column in [Systems Manager service endpoints](../../../general/latest/gr/ssm.md#ssm_region "../../../general/latest/gr/ssm.md#ssm_region") in the
_Amazon Web Services General Reference_.

**x86_64**

```
sudo dnf install -y https://s3.`region`.amazonaws.com/amazon-ssm-`region`/latest/linux_amd64/amazon-ssm-agent.rpm
```

See the following example.

```
sudo dnf install -y https://s3.us-east-2.amazonaws.com/amazon-ssm-us-east-2/latest/linux_amd64/amazon-ssm-agent.rpm
```

**ARM64**

```
sudo dnf install -y https://s3.`region`.amazonaws.com/amazon-ssm-`region`/latest/linux_arm64/amazon-ssm-agent.rpm
```

See the following example.

```
sudo dnf install -y https://s3.us-east-2.amazonaws.com/amazon-ssm-us-east-2/latest/linux_arm64/amazon-ssm-agent.rpm
```
