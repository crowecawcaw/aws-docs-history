AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Configure the Migration Hub Orchestrator plugin

The Migration Hub Orchestrator plugin is a virtual appliance that you can install in your on-premises VMware
environment.

###### Important

The Migration Hub Orchestrator plugin must be able to communicate with the source and target environments
to orchestrate and automate migrations. The version of the plugin that is deployed in vCenter
supports VMware vCenter Server 6.0, 6.5, 6.7 and 7.0.

###### Tasks

- [Download and configure the plugin](#w32aac18b9 "#w32aac18b9")
- [Set up AWS configurations](#cli-plugin-setup-aws-config "#cli-plugin-setup-aws-config")
- [Set up vCenter configurations](#cli-plugin-setup-vcenter-config "#cli-plugin-setup-vcenter-config")
- [Set up source server
  configurations](#cli-plugin-setup-source-server-config "#cli-plugin-setup-source-server-config")
- [Enable the Migration Hub Orchestrator plugin to communicate
  with source servers](#cli-plugin-setup-source-servers "#cli-plugin-setup-source-servers")

## Download and configure the plugin

To deploy the plugin as a virtual machine (VM) in your VMware environment, download the
plugin Open Virtualization Archive (OVA) file using the following steps.

1. Sign in to the [https://console.aws.amazon.com/migrationhub/orchestrator/](https://console.aws.amazon.com/migrationhub/orchestrator/ "https://console.aws.amazon.com/migrationhub/orchestrator/").
2. In the left navigation pane, choose **Orchestrate**.
3. On the **Migration Hub Orchestrator** page, choose **Download
   plugin**.
4. After the plugin is downloaded to your on-premises VMware environment, you can deploy it
   in vCenter. Sign in to vCenter as a VMware administrator.

We recommend at least 8 GB of RAM and at least 4 CPUsfor the VM. 5. Deploy the OVA file that you downloaded. The OVA ﬁle includes the plugin and a CLI that
can be used to access the Migration Hub Orchestrator API. 6. Sign in to the plugin using an SSH client.

```
ssh ec2-user@PluginIPAddress
```

When prompted for a password, enter the default password,
**plugin@123**. You must change your password when you first sign
in.

###### Tip

If you would like to use the plugin for multiple virtual machines, you can export the OVA
file after you configure it, and import it to your desired source VM.

To configure the Migration Hub Orchestrator plugin using **plugin setup** commands, create a
bash shell session in the plugin Docker container using the following command.

```
docker exec -it mhub-orchestrator-plugin bash
```

The **plugin setup** command runs all of the following commands in
succession, but you can also run them individually:

- **plugin setup --aws-configurations**
- **plugin setup --vcenter-configurations**
- **plugin setup --remote-server-configurations**

Run the following command to set up all of the plugin configurations at the same time. Then,
enter the information for AWS configurations, vCenter configurations, and remote server
configurations.

```
plugin setup
```

## Set up AWS configurations

1. Run [aws configure](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configure/index.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configure/index.html") to create
   a profile. For more information, see [Setting up the AWS CLI](../../../cli/latest/userguide/getting-started-quickstart.md "../../../cli/latest/userguide/getting-started-quickstart.md").
2. Run the `plugin setup --aws-configurations` command.
3. Enter **Y** for yes to **Have you
   setup IAM permissions in your AWS account...**
4. Enter the name of the profile that you created by using `aws configure`
   for **IAM Profile name**.
5. Enter **Y** for yes to **Upload
   plugin related metrics to Migration Hub Orchestrator?** Metrics data helps AWS to provide you
   with support.
6. Enter **Y** for yes to **Upload
   plugin related logs to Migration Hub Orchestrator?** Log data helps AWS to provide you with
   support.

The following is an example.

```

plugin setup --aws-configurations
Have you setup IAM permissions in your AWS account as per the user guide? [Y/N]: Y
IAM Profile name: <profile-name>
Upload plugin related metrics to Migration Hub Orchestrator? By default plugin will upload metrics. [Y/N]: Y
Upload plugin related logs to Migration Hub Orchestrator? By default plugin will upload logs. [Y/N]: Y
Plugin configurations are saved successfully
Start registering plugin
Start registering plugin
Plugin is registered successfully.

```

## Set up vCenter configurations

Set up vCenter configurations using the `plugin setup` command or the
`plugin setup --vcenter-configurations` command.

1. Enter **Y** or **N** to
   **Would you like to authenticate using VMware vCenter
   credentials** based on your preference.

###### Note

Authenticating using VMware vCenter credentials requires that VMware tools are
installed on the target servers.

Enter the **Host Url**, which can be the vCenter IP
address or the URL. Then, enter the **Username** and
**Password** for VMware vCenter. 2. Enter **Y** for yes to **Do you have
Windows machines managed by VMware vCenter** if you want to configure Windows
servers. Then, enter the **Username** and **Password** for Windows.

###### Note

If your Windows Remote Server belongs to an Active Directory domain, you must enter
the username as
`domain-name`\`username` when using
the CLI to provide source server configurations. For example, if the name of your domain
is exampledomain and your username is Administrator, then the username you enter in the
CLI is **exampledomain\Administrator**. 3. Enter **Y** for yes to **Setup for
Linux using VMware vCenter** if you want to configure Linux servers. Then,
enter the **Username** and **Password** for Linux. 4. Enter **Y** for yes to the **Would
you like to setup credentials for servers outside vCenter using NTLM for
Windows** and **SSH/Cert based for Linux**
questions if you want to set up source server credentials for servers outside of
vCenter. 5. For **Would you like to use the same Windows credentials used
during vCenter setup**, enter **Y** for yes if the
credentials for the Windows machines that are managed outside of vCenter are the same as
the credentials provided when configuring credentials for vCenter Windows machines.
Otherwise, enter **N** for no.

If you answer **Y** for yes, the following questions are
asked.

    1. Enter **Y** for yes to **Are you
     okay with the plugin accepting and locally storing server certificates on your
     behalf during first interaction with windows servers?**.
    2. Enter **1** for **Enter your
     options** if you want to configure SSH authentication.


    If you choose to use SSH authentication, you must copy the generated key
     credentials to your Linux servers. For more information, see [Set up key-based authentication on Linux
     servers](#cli-plugin-setup-linux-key "#cli-plugin-setup-linux-key").

The following is an example.

```
Start setting up vCenter configurations for remote execution
Note: authenticating using VMware vCenter credentials requires VMware tools to be installed on the target servers
Would you like to authenticate using VMware vCenter credentials? [Y/N]: **Y**
Host Url for VMware vCenter: host-url
Username for VMware vCenter: username
Password for VMware vCenter:
Successfully stored vCenter credentials...
Setup for Windows using VMware vCenter? [Y/N]: **Y**
Username for Windows: username
Password for Windows:
Successfully stored vCenter windows credentials...
Setup for Linux using VMware vCenter? [Y/N]: **Y**
Username for Linux: username
Password for Linux:
Successfully stored vCenter linux credentials...
Would you like to setup credentials for servers outside vCenter using NTLM for windows and SSH/Cert based for linux? [Y/N]: **Y**
Would you like to use the same Windows credentials used during vCenter setup? [Y/N]: **Y**
Are you okay with plugin accepting and locally storing server certificates on your behalf during first interaction with windows servers? These certificates will be used by plugin for secure communication with windows servers [Y/N]:**Y**
Successfully stored windows server credentials...
Please note that all windows server certificates are stored in directory /opt/amazon/mhub-orchestrator-plugin/remote-auth/windows/certs

Please note the IP address of the plugin and run the script specified in the user documentation on all the windows servers in your inventory
Would you like to setup credentials for servers not managed by vCenter using SSH/Cert based for Linux? [Y/N]: Y
Choose one of the following options for remote authentication:
1. SSH based authentication
2. Certificate based authentication
Enter your options [1-2]: **1**
Would you like to use the same Linux credentials used during vCenter setup? [Y/N]: **Y**
Generating SSH key on this machine...
SSH key pair path: /opt/amazon/mhub-orchestrator-plugin/remote-auth/linux/keys/id_rsa_rubix
Please add the public key "id_rsa_rubix.pub" to the "$HOME/.ssh/authorized_keys" file in your remote machines.
Your Linux remote server configurations are saved successfully.

```

## Set up source server

configurations

Set up source server configurations using the `plugin setup` command or the
`plugin setup --remote-server-configurations` command.

1. Enter **Y** for yes to **Would you
   like to setup credentials for servers not managed by vCenter using NTLM for
   Windows** if you want to configure Windows servers. Enter the **Username** and **Password** for
   WinRM.

###### Note

If your Windows Remote Server belongs to an Active Directory domain, you must enter
the username as
`domain-name`\`username` when using
the CLI to provide source server configurations. For example, if the name of your domain
is exampledomain and your username is Administrator, then the user name you enter in the
CLI is **exampledomain\Administrator**.

Enter **Y** for yes to **Are you okay
with plugin accepting and locally storing server certificates on your behalf during
first interaction with windows servers?**. Windows Server certificates are
stored in the directory
`/opt/amazon/mhub-orchestrator-plugin/remote-auth/windows/certs`. You must
copy the generated server credentials to your Windows servers. For more information, see
[Set up the source server configuration on Windows
servers](#cli-plugin-setup-windows "#cli-plugin-setup-windows"). 2. Enter **Y** for yes to **Setup for
Linux using SSH or Cert** if you want to configure Linux servers. 3. Enter **1** for **Enter your
options** if you want to configure for SSH key based authentication. If you
choose to use SSH authentication, you must copy the generated key credentials to your
Linux servers. For more information, see [Set up key-based authentication on Linux
servers](#cli-plugin-setup-linux-key "#cli-plugin-setup-linux-key"). 4. Enter **2** for **Enter your
options** if you want to configure for certificate-based authentication. For
information about setting up certificate-based authentication, see [Set up certificate-based
authentication on Linux servers](#cli-plugin-setup-linux-certificate "#cli-plugin-setup-linux-certificate").

The following is an example.

```
Setting up target server for remote execution
Would you like to setup credentials for servers not managed by vCenter using NTLM for Windows [Y/N]: **Y**
Username for WinRM: username //Enter domain-name\username, if the server is in AD domain
Password for WinRM: password
Are you okay with plugin accepting and locally storing server certificates on your behalf during first interaction with windows servers? These certificates will be used by plugin for secure communication with windows servers [Y/N]: **Y**
Successfully stored windows server credentials...
Please note that all windows server certificates are stored in directory /opt/amazon/mhub-orchestrator-plugin/remote-auth/windows/certs

Please note the IP address of the plugin and run the script specified in the user documentation on all the windows servers in your inventory
Would you like to setup credentials for servers not managed by vCenter using SSH/Cert based for Linux? [Y/N]: **Y**
Choose one of the following options for remote authentication:
1. SSH based authentication
2. Certificate based authentication
Enter your options [1-2]: **1**
User name for remote server: username
Generating SSH key on this machine...
SSH key pair path: /opt/amazon/mhub-orchestrator-plugin/remote-auth/linux/keys/id_rsa_rubix
Please add the public key "id_rsa_rubix.pub" to the "$HOME/.ssh/authorized_keys" file in your remote machines.
Your Linux remote server configurations are saved successfully.

```

## Enable the Migration Hub Orchestrator plugin to communicate

with source servers

###### Note

This step isn’t necessary if you set up the Migration Hub Orchestrator plugin using vCenter
credentials.

After you set up your remote server configurations, if you are using the `plugin
 setup` or `plugin setup --remote-server-configurations` command, you must
prepare your remote servers so that the Migration Hub Orchestrator plugin can collect data from them.

###### Note

You must make sure that the servers are reachable using their private IP address. For
further instructions on how to set up the environment through a virtual private cloud (VPC)
on AWS for remote running, see the [Amazon Virtual Private Cloud User
Guide](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md").

### Prepare source Linux servers

#### Set up key-based authentication on Linux

servers

If you choose to set up SSH key-based authentication for Linux when configuring source
server configurations, you must perform the following steps to set up key-based
authentication on your servers so that the Migration Hub Orchestrator plugin can communicate with source
server.

###### To set up key-based authentication on your Linux servers

1. Copy the public key that was generated with the name **id_rsa_rubix.pub** from the following folder in the container:

**/opt/amazon/mhub-orchestrator-plugin/remote-auth/linux/keys**. 2. Append the copied public key in the `$HOME/.ssh/authorized_keys` file
for all of the remote machines. If there is no file available, create it using the
`touch` or `vim` command. 3. Ensure that the home folder on the source server has a permission level of
`755` or less. You can use the `chmod` command to restrict
permissions.

#### Set up certificate-based

authentication on Linux servers

If you choose to set up certificate-based authentication for Linux when configuring
source server configurations, you must perform the following steps so that the Migration Hub Orchestrator
plugin can communicate with the source server.

We recommend this option if you already have Certificate Authority (CA) set up for
your application servers.

###### To set up certificate-based authentication on your Linux servers

1. Copy the username that works with all of your remote servers.
2. Copy the public key of the plugin to the CA.

The public key for the plugin can be found in the following location:

**/opt/amazon/mhub-orchestrator-plugin/remote-auth/linux/keys/id_rsa_rubix.pub**

This public key must be added to your CA for generating the certificate. 3. Copy the certificate that was generated in the previous step to the following
location in the plugin:

**/opt/amazon/mhub-orchestrator-plugin/remote-auth/linux/keys**

The name of the certificate must be **id_rsa_rubix-cert.pub**. 4. Provide the certificate file name during setup.

### Set up the source server configuration on Windows

servers

If you choose to set up Windows when you set up the source server in the **plugin
setup**, you must perform the following steps so that the Migration Hub Orchestrator plugin can
communicate with the source server.

###### To understand more about the PowerShell script that's executed on the source server,

read this note.

The script enables PowerShell remote and disables all authentication methods other
than negotiate. This is used for Windows NT LAN Manager (NTLM) and sets the
"AllowUnencrypted" WSMan protocol to false to ensure that the newly created listener
accepts only encrypted traffic. Using the Microsoft provided script,
`New-SelfSignedCertificateEx.ps1`, it creates a self-signed
certificate.

Any WSMan Instance that has an HTTP listener is removed, along with existing HTTPS
listeners. Then, it creates a new HTTPS listener. It also creates an inbound firewall rule
for TCP port 5986. In the final step, the WinRM service is restarted.

###### To set up a remote connection on Windows 2008 servers

1. Use the following command to check the version of PowerShell installed on your
   server.

```
$PSVersionTable
```

2. If the PowerShell version is not 5.1, then download and install WMF 5.1 by following
   the instructions at [Install and Configure WMF 5.1](https://docs.microsoft.com/en-us/powershell/scripting/windows-powershell/wmf/setup/install-configure?view=powershell-7.1 "https://docs.microsoft.com/en-us/powershell/scripting/windows-powershell/wmf/setup/install-configure?view=powershell-7.1") in the Microsoft documentation.
3. Use the following command in a new PowerShell window to ensure that PowerShell 5.1
   is installed.

```
$PSVersionTable
```

###### To set up a remote connection on Windows 2012 and newer servers

1. Download the setup script from the following URL:

[Setup script](https://application-data-collector-release.s3.us-west-2.amazonaws.com/scripts/WinRMSetup.ps1 "https://application-data-collector-release.s3.us-west-2.amazonaws.com/scripts/WinRMSetup.ps1") 2. Download the `New-SelfSignedCertificateEx.ps1` from the following
URL and paste the script into the same folder in which you downloaded
`WinRMSetup.ps1`:

[https://github.com/Azure/azure-libraries-for-net/blob/master/Samples/Asset/New-SelfSignedCertificateEx.ps1](https://github.com/Azure/azure-libraries-for-net/blob/master/Samples/Asset/New-SelfSignedCertificateEx.ps1 "https://github.com/Azure/azure-libraries-for-net/blob/master/Samples/Asset/New-SelfSignedCertificateEx.ps1") 3. To complete the setup, run the downloaded PowerShell script on all application
servers.

```
.\WinRMSetup.ps1
```

###### Note

If Windows Remote Management (WinRM) is not set up properly on the Windows Remote
Server, an attempt to communicate will fail. If this happens, you must delete the
certificate that corresponds to that server from the following location on the
container:

**/opt/amazon/mhub-orchestrator-plugin/remote-auth/windows/certs/`ads-server-id`.cer**

After you delete the certificate, wait for the ongoing process to be retried.
