# Install SSM Agent on hybrid

Windows Server nodes

This topic describes how to install AWS Systems Manager SSM Agent on Windows Server machines in a
[hybrid and multicloud](operating-systems-and-machine-types.md#supported-machine-types "operating-systems-and-machine-types.md#supported-machine-types") environment. For information about installing SSM Agent on EC2 instances for
Windows Server, see [Manually installing and
uninstalling SSM Agent on EC2 instances for Windows Server](manually-install-ssm-agent-windows.md "manually-install-ssm-agent-windows.md").

Before you begin, locate the Activation Code and Activation ID that were generated
during the hybrid activation process, as described in [Create a hybrid activation to register
nodes with Systems Manager](hybrid-activation-managed-nodes.md "hybrid-activation-managed-nodes.md"). You specify the Code and ID in
the following procedure.

###### To install SSM Agent on non-EC2 Windows Server machines in a hybrid and multicloud

environment

1. Log on to a server or VM in your hybrid and multicloud environment.
2. If you use an HTTP or HTTPS proxy, you must set the `http_proxy` or
   `https_proxy` environment variables in the current shell session.
   If you aren't using a proxy, you can skip this step.

For an HTTP proxy server, set this variable:

```
http_proxy=http://`hostname`:`port`
https_proxy=http://`hostname`:`port`
```

For an HTTPS proxy server, set this variable:

```
http_proxy=http://`hostname`:`port`
https_proxy=https://`hostname`:`port`
```

For PowerShell, configure the WinINet proxy settings:

```
[System.Net.WebRequest]::DefaultWebProxy

$proxyServer = "http://hostname:port"
$proxyBypass = "169.254.169.254"
$WebProxy = New-Object System.Net.WebProxy($proxyServer,$true,$proxyBypass)

[System.Net.WebRequest]::DefaultWebProxy = $WebProxy

```

###### Note

WinINet proxy configuration is required for PowerShell operations. For
more information, see [SSM Agent proxy settings and Systems Manager
services](configure-proxy-ssm-agent-windows.md#ssm-agent-proxy-services "configure-proxy-ssm-agent-windows.md#ssm-agent-proxy-services"). 3. Open Windows PowerShell in elevated (administrative)
mode. 4. Copy and paste the following command block into Windows
PowerShell. Replace each `example resource
 placeholder` with your own information. For example, the
Activation Code and Activation ID generated when you create a hybrid activation,
and with the identifier of the AWS Region you want to download SSM Agent
from.

###### Important

Note the following important details:

    * Using `ssm-setup-cli` for non-EC2 installations
     maximizes the security of your Systems Manager installation and
     configuration.
    * `ssm-setup-cli` supports a `manifest-url`
     option that determines the source where the agent is downloaded
     from. Don't specify a value for this option unless required by your
     organization.
    * You can use the script provided [here](https://github.com/aws/amazon-ssm-agent/blob/mainline/Tools/src/setupcli_data_integrity_windows.ps1 "https://github.com/aws/amazon-ssm-agent/blob/mainline/Tools/src/setupcli_data_integrity_windows.ps1") to validate the signature of
     `ssm-setup-cli`.
    * When registering instances, only use the provided download link
     provided for `ssm-setup-cli`. `ssm-setup-cli`
     shouldn’t be stored separately for future use.

`region` represents the identifier for an AWS Region supported
by AWS Systems Manager, such as `us-east-2` for the US East (Ohio) Region. For a list of supported
`region` values, see the **Region** column in [Systems Manager service endpoints](../../../general/latest/gr/ssm.md#ssm_region "../../../general/latest/gr/ssm.md#ssm_region") in the
_Amazon Web Services General Reference_.

Additionally, `ssm-setup-cli` includes the following
options:

    * `version` - Valid values are `latest` and
     `stable`.
    * `downgrade` - Reverts the agent to an earlier
     version.
    * `skip-signature-validation` - Skips the signature
     validation during the download and installation of the agent.

64-bit

```
[System.Net.ServicePointManager]::SecurityProtocol = 'TLS12'
$code = "`activation-code`"
$id = "`activation-id`"
$region = "`us-east-1`"
$dir = $env:TEMP + "\ssm"
New-Item -ItemType directory -Path $dir -Force
cd $dir
(New-Object System.Net.WebClient).DownloadFile("https://amazon-ssm-$region.s3.$region.amazonaws.com/latest/windows_amd64/ssm-setup-cli.exe", $dir + "\ssm-setup-cli.exe")
./ssm-setup-cli.exe -register -activation-code="$code" -activation-id="$id" -region="$region"
Get-Content ($env:ProgramData + "\Amazon\SSM\InstanceData\registration")
Get-Service -Name "AmazonSSMAgent"
```

5. Press `Enter`.

###### Note

If the command fails, verify that you are running the latest version of
AWS Tools for PowerShell.

The command does the following:

- Downloads and installs SSM Agent onto the machine.
- Registers the machine with the Systems Manager service.
- Returns a response to the request similar to the following:

```

    Directory: C:\Users\ADMINI~1\AppData\Local\Temp\2


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----       07/07/2018   8:07 PM                ssm
{"ManagedInstanceID":"mi-008d36be46EXAMPLE","Region":"us-east-2"}

Status      : Running
Name        : AmazonSSMAgent
DisplayName : Amazon SSM Agent
```

The machine is now a _managed node_. These managed
nodes are now identified with the prefix "mi-". You can view managed nodes on the
**Managed node** page in Fleet Manager, by using the AWS CLI command
[describe-instance-information](../../../cli/latest/reference/ssm/describe-instance-information.md "../../../cli/latest/reference/ssm/describe-instance-information.md"), or by using the API command
[DescribeInstanceInformation](../APIReference/API_DescribeInstanceInformation.md "../APIReference/API_DescribeInstanceInformation.md").

## Setting up private key

auto rotation

To strengthen your security posture, you can configure AWS Systems Manager Agent (SSM Agent)
to automatically rotate the private key for a hybrid and multicloud environment. You
can access this feature using SSM Agent version 3.0.1031.0 or later. Turn on this
feature using the following procedure.

###### To configure SSM Agent to rotate the private key for a hybrid and multicloud

environment

1. Navigate to `/etc/amazon/ssm/` on a Linux machine or
   `C:\Program Files\Amazon\SSM` for a Windows Server machine.
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

## Deregister and reregister a managed node (Windows Server)

You can deregister a managed node by calling the [DeregisterManagedInstance](../APIReference/API_DeregisterManagedInstance.md "../APIReference/API_DeregisterManagedInstance.md") API operation from either the AWS CLI or Tools for Windows PowerShell.
Here's an example CLI command:

`aws ssm deregister-managed-instance --instance-id
 "mi-1234567890"`

To remove the remaining registration information for the agent, remove the
`IdentityConsumptionOrder` key in the
`amazon-ssm-agent.json` file. Then run the following
command:

`amazon-ssm-agent -register -clear`

###### Note

You can reregister an on-premises server, edge device, or VM using the same
activation code and ID as long as you haven't reached the instance limit for the
designated activation code and ID. You can verify the instance limit for an
activation code and ID by calling the [describe-activations](../../../cli/latest/reference/ssm/describe-activations.md "../../../cli/latest/reference/ssm/describe-activations.md") API using the AWS CLI. After you run the
command, verify that the value of `RegistrationCount` doesn't exceed
`RegistrationLimit`. If it does, you must use a different
activation code and ID.

###### To reregister a managed node on a Windows Server hybrid

machine

1. Connect to your machine.
2. Run the following command. Be sure to replace the placeholder values with
   the Activation Code and Activation ID generated when you created a hybrid
   activation, and with the identifier of the Region you want to download the
   SSM Agent from.

```
$dir = $env:TEMP + "\ssm"
cd $dir
Start-Process ./ssm-setup-cli.exe -ArgumentList @(
    "-register",
    "-activation-code=$code",
    "-activation-id=$id",
    "-region=$region"
) -Wait -NoNewWindow
```
