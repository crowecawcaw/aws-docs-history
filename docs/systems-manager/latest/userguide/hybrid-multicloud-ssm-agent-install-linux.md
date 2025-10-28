# Install SSM Agent on hybrid

Linux nodes

This topic describes how to install AWS Systems Manager SSM Agent on non-EC2 (Amazon Elastic Compute Cloud) Linux
machines in a [hybrid and multicloud](operating-systems-and-machine-types.md#supported-machine-types "operating-systems-and-machine-types.md#supported-machine-types") environment. For information about installing SSM Agent on EC2
instances for Linux, see [Manually installing and
uninstalling SSM Agent on EC2 instances for Linux](manually-install-ssm-agent-linux.md "manually-install-ssm-agent-linux.md").

Before you begin, locate the Activation Code and Activation ID that were generated
during the hybrid activation process, as described in [Create a hybrid activation to register
nodes with Systems Manager](hybrid-activation-managed-nodes.md "hybrid-activation-managed-nodes.md"). You specify the Code and ID in
the following procedure.

###### To install SSM Agent on non-EC2 machines in a hybrid and multicloud

environment

1. Log on to a server or VM in your hybrid and multicloud environment.
2. If you use an HTTP or HTTPS proxy, you must set the `http_proxy` or
   `https_proxy` environment variables in the current shell session.
   If you aren't using a proxy, you can skip this step.

For an HTTP proxy server, enter the following commands at the command
line:

```
export http_proxy=http://`hostname`:`port`
export https_proxy=http://`hostname`:`port`
```

For an HTTPS proxy server, enter the following commands at the command
line:

```
export http_proxy=http://`hostname`:`port`
export https_proxy=https://`hostname`:`port`
```

3. Copy and paste one of the following command blocks into SSH. Replace the
   placeholder values with the Activation Code and Activation ID generated during
   the hybrid activation process and with the identifier of the AWS Region you
   want to download SSM Agent from, then press `Enter`.

###### Important

Note the following important details:

    * Using `ssm-setup-cli` for non-EC2 installations
     maximizes the security of your Systems Manager installation and
     configuration.
    * `sudo` isn't necessary if you're a root user.
    * Download `ssm-setup-cli` from the same AWS Region as
     where your hybrid activation was created.
    * `ssm-setup-cli` supports a `manifest-url`
     option that determines the source where the agent is downloaded
     from. Don't specify a value for this option unless required by your
     organization.
    * When registering instances, only use the provided download link
     provided for `ssm-setup-cli`. `ssm-setup-cli`
     shouldn’t be stored separately for future use.
    * You can use the script provided [here](https://github.com/aws/amazon-ssm-agent/blob/mainline/Tools/src/setupcli_data_integrity_linux.sh "https://github.com/aws/amazon-ssm-agent/blob/mainline/Tools/src/setupcli_data_integrity_linux.sh") to validate the signature of
     `ssm-setup-cli`.

`region` represents the identifier for an AWS Region supported
by AWS Systems Manager, such as `us-east-2` for the US East (Ohio) Region. For a list of supported
`region` values, see the **Region** column in [Systems Manager service endpoints](../../../general/latest/gr/ssm.md#ssm_region "../../../general/latest/gr/ssm.md#ssm_region") in the
_Amazon Web Services General Reference_.

Additionally, `ssm-setup-cli` includes the following
options:

    * `version` - Valid values are `latest` and
     `stable`.
    * `downgrade` - Allows the SSM Agent to be downgraded to an
     earlier version. Specify `true` to install an earlier version
     of the agent.
    * `skip-signature-validation` - Skips the signature
     validation during the download and installation of the agent.

```
mkdir /tmp/ssm
curl https://amazon-ssm-`region`.s3.`region`.amazonaws.com/latest/linux_amd64/ssm-setup-cli -o /tmp/ssm/ssm-setup-cli
sudo chmod +x /tmp/ssm/ssm-setup-cli
sudo /tmp/ssm/ssm-setup-cli -register -activation-code "`activation-code`" -activation-id "`activation-id`" -region "`region`"
```

```
mkdir /tmp/ssm
curl https://amazon-ssm-`region`.s3.`region`.amazonaws.com/latest/linux_amd64/ssm-setup-cli -o /tmp/ssm/ssm-setup-cli
sudo chmod +x /tmp/ssm/ssm-setup-cli
sudo /tmp/ssm/ssm-setup-cli -register -activation-code "`activation-code`" -activation-id "`activation-id`" -region "`region`"
```

```
mkdir /tmp/ssm
curl https://amazon-ssm-`region`.s3.`region`.amazonaws.com/latest/debian_amd64/ssm-setup-cli -o /tmp/ssm/ssm-setup-cli
sudo chmod +x /tmp/ssm/ssm-setup-cli
sudo /tmp/ssm/ssm-setup-cli -register -activation-code "`activation-code`" -activation-id "`activation-id`" -region "`region`"
```

- **Using .deb packages**

```
mkdir /tmp/ssm
curl https://amazon-ssm-`region`.s3.`region`.amazonaws.com/latest/debian_amd64/ssm-setup-cli -o /tmp/ssm/ssm-setup-cli
sudo chmod +x /tmp/ssm/ssm-setup-cli
sudo /tmp/ssm/ssm-setup-cli -register -activation-code "`activation-code`" -activation-id "`activation-id`" -region "`region`"
```

- **Using Snap packages**

You don't need to specify a URL for the download, because the
`snap` command automatically downloads the agent from the
[Snap app
store](https://snapcraft.io/amazon-ssm-agent "https://snapcraft.io/amazon-ssm-agent") at [https://snapcraft.io](https://snapcraft.io "https://snapcraft.io").

On Ubuntu Server 20.04, 18.04, and 16.04 LTS, SSM Agent installer files,
including agent binaries and config files, are stored in the following
directory: `/snap/amazon-ssm-agent/current/`. If you
make changes to any configuration files in this directory, then you must
copy these files from the `/snap` directory to the
`/etc/amazon/ssm/` directory. Log and library
files haven't changed (`/var/lib/amazon/ssm`,
`/var/log/amazon/ssm`).

```
sudo snap install amazon-ssm-agent --classic
sudo systemctl stop snap.amazon-ssm-agent.amazon-ssm-agent.service
sudo /snap/amazon-ssm-agent/current/amazon-ssm-agent -register -code "`activation-code`" -id "`activation-id`" -region "`region`"
sudo systemctl start snap.amazon-ssm-agent.amazon-ssm-agent.service
```

###### Important

The _candidate_ channel in the Snap store
contains the latest version of SSM Agent; not the stable channel. If
you want to track SSM Agent version information on the candidate
channel, run the following command on your Ubuntu Server 18.04 and
16.04 LTS 64-bit managed nodes.

```
sudo snap switch --channel=candidate amazon-ssm-agent
```

The command downloads and installs SSM Agent onto the hybrid-activated machine in your
hybrid and multicloud environment. The command stops SSM Agent, and then registers the
machine with the Systems Manager service. The machine is now a managed node. Amazon EC2 instances
configured for Systems Manager are also managed nodes. In the Systems Manager console, however, your
hybrid-activated nodes are distinguished from Amazon EC2 instances with the prefix
"mi-".

Continue to [Install SSM Agent on hybrid
Windows Server nodes](hybrid-multicloud-ssm-agent-install-windows.md "hybrid-multicloud-ssm-agent-install-windows.md").

## Setting up private key auto

rotation

To strengthen your security posture, you can configure AWS Systems Manager Agent (SSM Agent)
to automatically rotate the private key for your hybrid and multicloud environment.
You can access this feature using SSM Agent version 3.0.1031.0 or later. Turn on this
feature using the following procedure.

###### To configure SSM Agent to rotate the private key for a hybrid and multicloud

environment

1. Navigate to `/etc/amazon/ssm/` on a Linux machine or
   `C:\Program Files\Amazon\SSM` for a Windows
   machine.
2. Copy the contents of `amazon-ssm-agent.json.template` to a new
   file named `amazon-ssm-agent.json`. Save
   `amazon-ssm-agent.json` in the same directory where
   `amazon-ssm-agent.json.template` is located.
3. Find `Profile`, `KeyAutoRotateDays`. Enter the
   number of days that you want between automatic private key rotations.
4. Restart SSM Agent.

Every time you change the configuration, restart SSM Agent.

You can customize other features of SSM Agent using the same procedure. For an
up-to-date list of the available configuration properties and their default values,
see [Config Property Definitions](https://github.com/aws/amazon-ssm-agent#config-property-definitions "https://github.com/aws/amazon-ssm-agent#config-property-definitions").

## Deregister and reregister a managed node (Linux)

You can deregister a hybrid-activated managed node by calling the [DeregisterManagedInstance](../APIReference/API_DeregisterManagedInstance.md "../APIReference/API_DeregisterManagedInstance.md") API operation from either the AWS CLI or Tools for Windows PowerShell.
Here's an example CLI command:

`aws ssm deregister-managed-instance --instance-id
 "mi-1234567890"`

To remove the remaining registration information for the agent, remove the
`IdentityConsumptionOrder` key in the
`amazon-ssm-agent.json` file. Then, depending on your
installation type, run one of the following commands.

On Ubuntu Server nodes where SSM Agent was installed using Snap packages:

```
sudo /snap/amazon-ssm-agent/current/amazon-ssm-agent -register -clear
```

On all other Linux installations:

```
amazon-ssm-agent -register -clear
```

###### Note

You can reregister an on-premises server, edge device, or VM using the same
activation code and ID as long as you haven't reached the instance limit for the
designated activation code and ID. You can verify the instance limit for an
activation code and ID by calling the [describe-activations](../../../cli/latest/reference/ssm/describe-activations.md "../../../cli/latest/reference/ssm/describe-activations.md") API using the AWS CLI. After you run the
command, verify that the value of `RegistrationCount` doesn't exceed
`RegistrationLimit`. If it does, you must use a different
activation code and ID.

###### To reregister a managed node on a non-EC2 Linux machine

1. Connect to your machine.
2. Run the following command. Be sure to replace the placeholder values with
   the Activation Code and Activation ID generated when you created a
   managed-node activation, and with the identifier of the Region you want to
   download the SSM Agent from.

```
echo "yes" | sudo /tmp/ssm/ssm-setup-cli -register -activation-code "`activation-code`" -activation-id "`activation-id`" -region "`region`
```

## Troubleshooting SSM Agent installation on non-EC2 Linux machines

Use the following information to help you troubleshoot problems installing
SSM Agent on hybrid-activated Linux machines in a [hybrid and multicloud](operating-systems-and-machine-types.md#supported-machine-types "operating-systems-and-machine-types.md#supported-machine-types") environment.

### You receive DeliveryTimedOut error

**Problem**: While configuring a machine in one
AWS account as a managed node for a separate AWS account, you receive
`DeliveryTimedOut` after running the commands to install SSM Agent
on the target machine.

**Solution**: `DeliveryTimedOut` is
the expected response code for this scenario. The command to install SSM Agent on
the target node changes the node ID of the source node. Because the node ID has
changed, the source node isn't able to reply to the target node that the command
failed, completed, or timed out while executing.

### Unable to load node associations

**Problem**: After running the install commands,
you see the following error in the SSM Agent error logs:

`Unable to load instance associations, unable to retrieve associations
 unable to retrieve associations error occurred in
 RequestManagedInstanceRoleToken: MachineFingerprintDoesNotMatch: Fingerprint
 doesn't match`

You see this error when the machine ID doesn't persist after a reboot.

**Solution**: To solve this problem, run the
following command. This command forces the machine ID to persist after a
reboot.

```
umount /etc/machine-id
systemd-machine-id-setup
```
