AWS Migration Hub will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Step 4: Set up the Strategy Recommendations

collector

This section describes how to use the command line `collector setup` commands
to configure the Migration Hub Strategy Recommendations application data collector. These configurations are stored
locally.

Before you can use `collector setup` commands, you must create a bash shell
session in the collector Docker container using the following `docker exec`
command.

```
docker exec -it application-data-collector bash
```

The `collector setup` command runs all of the following commands in succession
but you can run them individually:

- `collector setup --aws-configurations` – Set up AWS
  configurations.
- `collector setup --vcenter-configurations` – Set up vCenter
  configurations.

###### Note

vCenter configuration setup is only available if the collector is hosted on
vCenter. However, you can force vCenter configuration setup by using the command
`collector setup --vcenter-configurations`.

- `collector setup --remote-server-configurations` – Set up remote
  server configurations.
- `collector setup --version-control-configurations` – Set up
  version control configurations.

###### To set up all the collector configurations at the same time

1. Enter the following command.

```
collector setup
```

2. Enter the information for AWS configurations as described in [Set up AWS configurations](#cli-collector-setup-aws-config "#cli-collector-setup-aws-config").
3. Enter the information for vCenter configurations as described in [Set up vCenter
   configurations](#cli-collector-setup-vcenter-config "#cli-collector-setup-vcenter-config").
4. Enter the information for remote server configurations as described in [Set up remote server
   configurations](#cli-collector-setup-remote-server-config "#cli-collector-setup-remote-server-config").
5. Enter the information for version control configurations as described in [Set up version control
   configurations](#cli-collector-setup-git-source-config "#cli-collector-setup-git-source-config").
6. Prepare your Windows and Linux servers for collector data collection by following
   the instructions in [Prepare your remote Windows and
   Linux servers for data collection](#cli-collector-setup-remote-servers "#cli-collector-setup-remote-servers").

## Set up AWS configurations

To set up AWS configurations, when using the `collector setup`
command or the `collector setup --aws-configurations` command.

1. Enter **Y** for yes to the **Have you setup IAM permissions...** question. You set up these
   permissions when you created a user to access the collector using the
   `AWSMigrationHubStrategyCollector` managed policy following the
   steps in [Strategy Recommendations users and roles](setting-up.md#setting-up-iam-non-admin "setting-up.md#setting-up-iam-non-admin").
2. Enter your access key and secret key from the AWS account that has the user
   that you created to access the collector following the steps in [Strategy Recommendations users and roles](setting-up.md#setting-up-iam-non-admin "setting-up.md#setting-up-iam-non-admin").
3. Enter a Region, for example, `us-west-2`. Choose a Region that
   suits your needs from the Regions that Strategy Recommendations uses. For a list of these
   Regions, see [Strategy Recommendations
   endpoints](../../../general/latest/gr/migrationhubstrategy.md "../../../general/latest/gr/migrationhubstrategy.md") in the _AWS General Reference_.
4. Enter **Y** for yes to the **Upload collector related metrics to migration hub strategy
   service?** question. Metrics information helps AWS provide you
   with appropriate support.
5. Enter **Y** for yes to the **Upload collector related logs to migration hub strategy service?**
   question. Information from logs helps AWS provide you with appropriate
   support.

The following example shows what is displayed, including example entries for the AWS
configurations.

```

Have you setup IAM permissions in you AWS account as per the user guide? [Y/N]: Y
Choose one of the following options for providing user credentials:
1. Long term AWS credentials
2. Temporary AWS credentials
Enter your options [1-2]: 2
AWS session token:
AWS access key ID [None]:
AWS secret access Key [None]:
AWS region name [us-west-2]:
AWS configurations are saved successfully
Upload collector related metrics to migration hub strategy service? By default collector will upload metrics. [Y/N]: Y
Upload collector related logs to migration hub strategy service? By default collector will upload logs. [Y/N]: Y
Application data collector configurations are saved successfully
Start registering application data collector
Application data collector is registered successfully.

```

## Set up vCenter

configurations

To set up vCenter configurations, when using the `collector setup`
command or the `collector setup --vcenter-configurations` command:

1. Enter **Y** for yes to the **Would you like to authenticate using VMware vCenter credentials**
   question, if you want to authenticate using VMware vCenter credentials.

###### Note

Authenticating using VMware vCenter credentials requires that VMware tools
are installed on the target servers.

Enter the **Host Url**, which can be either the
vCenter IP address or URL. Then, enter the **Username** and **Password** for
VMware vCenter. 2. Enter **Y** for yes to the **Do you have Windows machines managed by VMware vCenter** question,
if you want to configure Windows servers.

Enter the **Username** and **Password** for Windows.

###### Note

If your Windows Remote Server belongs to an Active Directory domain, you
must enter the user name as
`domain-name`\`username`
when using the CLI to provide remote server configurations. For example, if
the name of your domain is exampledomain and your user name is
Administrator, then the user name you enter in the CLI is **exampledomain\Administrator**. 3. Enter **Y** for yes to the **Setup for Linux using VMware vCenter** question, if you want to
configure Linux servers.

Enter the **Username** and **Password** for Linux. 4. Enter **Y** for yes to the **Would you like to setup credentials for servers outside vCenter using NTLM
for Windows** and **SSH/Cert based for
Linux** questions, if you want to set up remote server credentials
for servers outside of vCenter. 5. For the **Would you like to use the same Windows
credentials used during vCenter setup** question, enter **Y** for yes if the credentials for the Windows machines
managed outside of vCenter are the same as the credentials provided when
configuring credentials for vCenter Windows machines. Otherwise, enter **N** for no.

If you answer **Y** for yes, the following
questions are asked.

    1. Enter **Y** for yes to the **Are you okay with collector accepting and locally
     storing server certificates on your behalf during first interaction
     with windows servers?** question.
    2. Enter **1** for the **Enter your options** question, if you want to configure
     for SSH authentication.


    If you choose to use SSH authentication, you must copy the generated
     key credentials to your Linux servers. For more information, see [Set up key-based authentication
     on Linux servers](#cli-collector-setup-linux-key "#cli-collector-setup-linux-key").

The following example shows what is displayed, including example entries for the
VMware vCenter configurations.

```
Your Linux remote server configurations are saved successfully.
collector setup —vcenter-configurations
Start setting up vCenter configurations for remote execution
Note: Authenticating using VMware vCenter credentials requires VMware tools to be installed on the target servers
Would you like to authenticate using VMware vCenter credentials? [Y/N]: y

NOTE: Your vSphere user must have Guest Operations privileges enabled.

Host Url for VMware vCenter: domain-name
Username for VMware vCenter: username
Password for VMware vCenter: password
Reenter password for VMware vCenter: password
Successfully stored vCenter credentials...
Do you have Windows machines managed by VMware vCenter? [Y/N]: y

NOTE: For the best experience, we recommend that you create a new Active Directory user in the Domain Admins group.

Username for Windows (Domain\User): username
Password for Windows: password
Reenter password for Windows: password
Successfully stored windows credentials...
You can verify your setup for vCenter windows machines is correct with "collector diag-check"
Do you have Linux machines managed by VMWare vCenter? [Y/N]: y
Username for Linux: username
Password for Linux: password
Reenter password for Linux: password
Successfully stored linux credentials...
You can verify your setup for vCenter linux machines is correct with "collector diag-check"
Would you like to setup credentials for servers not managed by vCenter using NTLM for windows and SSH/Cert based for Linux? [Y/N]: y
Setting up target server for remote execution:
Would you like to setup credentials for servers not managed by vCenter using NLTM for Windows [Y/N]: y
Would you like to use the same Windows credentials used during vCenter setup? [Y/N]: y
Are you okay with collector accepting and locally storing server certificates on your behalf during first interaction with windows servers? These certificates will be used by collector for secure communication with windows servers [Y/N]: y
Successfully stored windows server credentials...
Please note that all windows server certificates are stored in directory /opt/amazon/application-data-collector/remote-auth/windows/certs

Please note the IP address of the collector and run the script specified in the user documentation on all the windows servers in your inventory
You can verify your setup for remote windows machines is correct with "collector diag-check"
Would you like to setup credentials for servers not managed by vCenter using SSH/Cert based for Linux? [Y/N]: y
Choose one of the following options for remote authentication:
1. SSH based authentication
2. Certificate based authentication
Enter your options [1-2]: 1
Would you like to use the same Linux credentials used during vCenter setup? [Y/N]: y
Generating SSH key on this machine...
Successfully generated SSH key pair

SSH key pair path: /opt/amazon/application-data-collector/remote-auth/linux/keys/id_rsa_assessment
Please add the public key "id_rsa_assessment.pub" to the "$HOME/.ssh/authorized_keys" file in your remote machines.
You can verify your setup for remote linux machines is correct with "collector diag-check

```

## Set up remote server

configurations

To set up remote server configurations, when using the `collector
 setup` command or the `collector setup
 --remote-server-configurations` command:

1. Enter **Y** for yes to the **Would you like to setup credentials for servers not managed by vCenter
   using NLTM for Windows** question, if you want to configure Windows
   servers.

Enter the **Username** and **Password** for WinRM.

###### Note

If your Windows Remote Server belongs to an Active Directory domain, you
must enter the user name as
`domain-name`\`username`
when using the CLI to provide remote server configurations. For example, if
the name of your domain is exampledomain and your user name is
Administrator, then the user name you enter in the CLI is **exampledomain\Administrator**.

Enter **Y** for yes to the **Are you okay with collector accepting and locally storing server
certificates on your behalf during first interaction with windows
servers?** question. Windows Server certificates are stored in the
directory
`/opt/amazon/application-data-collector/remote-auth/windows/certs`.

You must copy the generated server credentials to your Windows servers. For
more information, see [Set up remote server configuration on
Windows servers](#cli-collector-setup-windows "#cli-collector-setup-windows"). 2. Enter **Y** for yes to the **Setup for Linux using SSH or Cert** question, if you want to
configure Linux servers. 3. Enter **1** for the **Enter
your options** question, if you want to configure for SSH key based
authentication.

If you choose to use SSH authentication, you must copy the generated key
credentials to your Linux servers. For more information, see [Set up key-based authentication
on Linux servers](#cli-collector-setup-linux-key "#cli-collector-setup-linux-key"). 4. Enter **2** for the **Enter
your options** question, if you want to configure for
certificate-based authentication.

For information about setting up certificate-based authentication, see [Set up certificate-based
authentication on Linux servers](#cli-collector-setup-linux-certificate "#cli-collector-setup-linux-certificate").

The following example shows what displayed, including example entries for the remote
server configurations.

```
Setting up target server for remote execution
Would you like to setup credentials for servers not managed by vCenter using NLTM for Windows [Y/N]: **y**

NOTE: For the best experience, we recommend that you create a new Active Directory user in the Domain Admins group.

Username for WinRM (Domain\User): username
Password for WinRM: password
Reenter password for WinRM: password
Are you okay with collector accepting and locally storing server certificates on your behalf during first interaction with windows servers? These certificates will be used by collector for secure communication with windows servers [Y/N]: **Y**
Successfully stored windows server credentials...
Please note that all windows server certificates are stored in directory /opt/amazon/application-data-collector/remote-auth/windows/certs

Please note the IP address of the collector and run the script specified in the user documentation on all the windows servers in your inventory
Would you like to setup credentials for servers not managed by vCenter using SSH/Cert based for Linux? [Y/N]: **Y**
Choose one of the following options for remote authentication:
1. SSH based authentication
2. Certificate based authentication
Enter your options [1-2]: **1**
User name for remote server: username
Generating SSH key on this machine...
SSH key pair path: /opt/amazon/application-data-collector/remote-auth/linux/keys/id_rsa_assessment
Please add the public key "id_rsa_assessment.pub" to the "$HOME/.ssh/authorized_keys" file in your remote machines.
Your Linux remote server configurations are saved successfully.

```

## Set up version control

configurations

To set up version control configurations, when using the `collector
 setup` command or the `collector setup
 --version-control-configurations` command:

1. Enter **Y** for yes to the **Set up source code analysis?** question.
2. Enter **1** for the **Enter
   your options** question, if you want to configure the Git server
   endpoint.

Enter **github.com** for the **GIT server endpoint:**. 3. Enter **2** for the **Enter
your options** question, if you want to configure a GitHub
Enterprise Server.

Enter the enterprise endpoint without https://, as follows: **GIT server endpoint:**
`git-enterprise-endpoint` 4. Enter your Git `username` and personal access
`token`. 5. Enter **Y** for yes to the **Do you have any csharp repositories that should be analyzed on a windows
machine?** question, if you want to analyze C# code.

###### Note

To analyze .NET repositories for Porting Assistant for .NET recommendations, you must
provide a Windows machine that is set up with the Porting Assistant for .NET porting assessment
tool. For more information, see [Getting started with Porting Assistant for .NET](../../../portingassistant/latest/userguide/porting-assistant-getting-started.md "../../../portingassistant/latest/userguide/porting-assistant-getting-started.md") in the
_Porting Assistant for .NET User Guide_. 6. For the **Would you like to reuse existing windows
credentials on this machine?** question. Enter **Y** for yes, if the Windows machine for C# source code
analysis uses the same credentials as the credentials previously provided as
part of setting up `--remote-server-configurations` or
`--vcenter-configurations`.

Enter **N** for no, if you want to enter new
credentials. 7. To use **VMWare vCenter Windows Machine** credentials, enter
**1** for **Choose one of
the following options for windows credentials**. 8. Enter the IP address for the Windows machine.

The following example shows what is displayed, including example entries for the
version control configurations.

```

Set up for source code analysis [Y/N]: y
Choose one of the following options for version control type:
1. GIT
2. GIT Enterprise
3. Azure DevOps - Git
Enter your options [1-3]: 3
Your server endpoint: dev.azure.com (http://dev.azure.com/)
Your DevOps Organization name: <Your organization name>
Personal access token [None]:
Your version control credentials are saved successfully.
Do you have any csharp repositories that should be analyzed on a windows machine? [Y/N]: y
Would you like to reuse existing windows credentials on this machine? [Y/N]: y
Choose one of the following options for windows credentials:
1. VMWare vCenter Windows Machine
2. Standard Windows Machine
Enter your options [1-2]:
1
Windows machine IP Address: <Your windows machine IP address>
Using VMWare vCenter Windows Machine credentials
Successfully stored windows server credentials...

```

## Prepare your remote Windows and

Linux servers for data collection

###### Note

This step isn’t necessary if you setup the Strategy Recommendations applications data collector
using vCenter credentials.

After you set up your remote server configurations, if you are using the
`collector setup command` or the `collector setup
 --remote-server-configurations` command, you must prepare your remote servers
so that the Strategy Recommendations applications data collector can collect data from them.

###### Note

You must make sure that the servers are reachable using their private IP address.
For further instructions on how to set up the environment through a virtual private
cloud (VPC) on AWS for remote running, see the [Amazon Virtual Private Cloud
User Guide](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md").

To prepare your remote Linux servers, see [Prepare remote Linux servers](#cli-collector-setup-linux "#cli-collector-setup-linux").

To prepare your remote Windows servers, see [Set up remote server configuration on
Windows servers](#cli-collector-setup-windows "#cli-collector-setup-windows").

### Prepare remote Linux servers

#### Set up key-based authentication

on Linux servers

If you choose to set up SSH key-based authentication for Linux when
configuring remote server configurations, you must perform the following steps
to set up key-based authentication on your servers so that data can be collected
by the Strategy Recommendations applications data collector.

###### To set up key-based authentication on your Linux servers

1. Copy the public key generated with the name **id_rsa_assessment.pub** from the following folder in the
   container:

**/opt/amazon/application-data-collector/remote-auth/linux/keys**. 2. Append the copied public key in the
`$HOME/.ssh/authorized_keys` file for all the remote
machines. If there is no file available, create it using the
`touch` or `vim` command. 3. Make sure that the home folder on the remote server has permission
level `755` or less. If it's `777`, it won't work.
You can use the `chmod` command to restrict
permissions.

#### Set up certificate-based

authentication on Linux servers

If you choose to set up certificate-based authentication for Linux when
configuring remote server configurations, you must perform the following steps
so that data can be collected by the Strategy Recommendations application data
collector.

We recommend this option if you already have Certificate Authority (CA) set up
for your application servers.

###### To set up certificate-based authentication on your Linux servers

1. Copy the user name that works with all your remote servers.
2. Copy the public key of the collector to the CA.

The public key for the collector can be found in the following
location:

**/opt/amazon/application-data-collector/remote-auth/linux/keys/id_rsa_assessment.pub**

This public key must be added to your CA for generating the
certificate. 3. Copy the certificate generated in the previous step to the following
location in the collector:

**/opt/amazon/application-data-collector/remote-auth/linux/keys**

The name of the certificate must be **id_rsa_assessment-cert.pub**. 4. Provide the certificate file name during the setup step.

### Set up remote server configuration on

Windows servers

If you choose to set up Windows when configuring remote server configurations in
the collector setup, you must perform the following steps so that data can be
collected by Strategy Recommendations.

###### To understand more about the PowerShell script that is executed on the remote

server, read this note.

The script enables PowerShell remote and disables all authentication methods
other than negotiate. This is used for Windows NT LAN Manager (NTLM) and sets
the "AllowUnencrypted" WSMan protocol to false to ensure that the newly created
listener accepts only encrypted traffic. Using the Microsoft provided script,
`New-SelfSignedCertificateEx.ps1`, it creates a
self-signed certificate.

Any WSMan Instance that has a HTTP listener is removed along with existing
HTTPS listeners. Then, it creates a new HTTPS listener. It also creates an
inbound firewall rule for TCP port 5986. In the final step, the WinRM service is
restarted.

###### To set up data collection through a remote connection on your Windows 2008

servers

1. Use the following command to check the version of PowerShell installed on
   your server.

```
$PSVersionTable
```

2. If the PowerShell version is not 5.1, then download and install WMF 5.1 by
   following the instructions at [Install and Configure WMF 5.1](https://docs.microsoft.com/en-us/powershell/scripting/windows-powershell/wmf/setup/install-configure?view=powershell-7.1 "https://docs.microsoft.com/en-us/powershell/scripting/windows-powershell/wmf/setup/install-configure?view=powershell-7.1") in the Microsoft
   documentation.
3. Use the following command in a new PowerShell window to ensure that
   PowerShell 5.1 is installed.

```
$PSVersionTable
```

4. Follow the next set of steps, which describe how to set up data collection
   through a remote connection on Windows 2012 and above.

###### To set up data collection through a remote connection on your Windows 2012

and newer servers

1. Download the setup script from the following URL:

[https://application-data-collector-release.s3.us-west-2.amazonaws.com/scripts/WinRMSetup.ps1](https://application-data-collector-release.s3.us-west-2.amazonaws.com/scripts/WinRMSetup.ps1 "https://application-data-collector-release.s3.us-west-2.amazonaws.com/scripts/WinRMSetup.ps1") 2. Download the `New-SelfSignedCertificateEx.ps1` from the
following URL and paste the script into the same folder in which you
downloaded `WinRMSetup.ps1`:

[https://github.com/Azure/azure-libraries-for-net/blob/master/Samples/Asset/New-SelfSignedCertificateEx.ps1](https://github.com/Azure/azure-libraries-for-net/blob/master/Samples/Asset/New-SelfSignedCertificateEx.ps1 "https://github.com/Azure/azure-libraries-for-net/blob/master/Samples/Asset/New-SelfSignedCertificateEx.ps1") 3. To complete the setup, run the downloaded PowerShell script on all
application servers.

```
.\WinRMSetup.ps1
```

###### Note

If Windows Remote Management (WinRM) is not set up properly on the Windows
Remote Server, an attempt to collect data from that server will fail. If this
happens, you must delete the certificate that corresponds to that server from
the following location on the container:

**/opt/amazon/application-data-collector/remote-auth/windows/certs/`ads-server-id`.cer**

After you delete the certificate, wait for the data collection process to be
retried.

### Next step

[Step 5: Use Strategy Recommendations in the Migration Hub
console to get recommendations](getting-started-get-recommendations.md "getting-started-get-recommendations.md")

## Verify that your collector and

servers are setup for data collection

Verify that your collector and servers are correctly setup for data collection by
using the following command.

```
collector diag-check
```

This command conducts a set of diagnostic checks on your server configurations and
provides input on failed checks.

When you use the command in `-a` mode, you get the output in a
**DiagnosticCheckResult.txt** file after the checks are
complete.

```
collector diag-check -a
```

You can perform a diagnostic check on the server configurations of a single server
with the IP address of that server.

The following examples show the output of a successful setup.

**Linux server**

```

            Provide your test server IP address: IP address
---------------------------------------------------------------
Start checking connectivity & credentials...
Connectivity and Credential Checks succeeded
---------------------------------------------------------------
Start checking permissions...
Permission Check succeeded
---------------------------------------------------------------
Start checking OS version...
OS version check succeeded
---------------------------------------------------------------
Start checking Linux Bash installation...
Linux Bash installation check succeeded
---------------------------------------------------------------
All diagnostic checks complete successfully.
This server is correctly set up and ready for data collection.

```

**Windows server**

```

            Windows PowerShell Version Check succeeded
Provide your test server IP address: IP address
---------------------------------------------------------------
Start checking connectivity & credentials...
Connectivity and Credential Checks succeeded
---------------------------------------------------------------
Start checking permissions...
Permission Check succeeded
---------------------------------------------------------------
Start checking OS version...
OS version check succeeded
---------------------------------------------------------------
Start checking Windows architecture type...
Windows Architecture Type Check succeeded
---------------------------------------------------------------
All diagnostic checks complete successfully.
This server is correctly set up and ready for data collection.

```

The following example shows an error message that is displayed when your remote server
credentials are incorrect.

```

Unable to authenticate the server credentials with IP address ${IPAddress}.
Ensure that your credentials are accurate and the server is configured correctly.
Use the following command to reset incorrect credentials.
collector setup —remote-server-configurations

```
