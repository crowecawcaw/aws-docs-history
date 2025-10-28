# Prerequisites

Before using the **eb migrate** command, ensure your environment meets these
requirements:

**IIS installation and version**

The server that you're migrating from must run Internet Information Services (IIS)
version 7.0 or later. IIS 10.0 on Windows Server 2016 or later provides the most
compatible environment for migration.

To verify your IIS version run the following command:

```
`PS C:\migrations_workspace>` `Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\InetStp\"`
`...
SetupString : IIS 10.0
VersionString : Version 10.0
...`
```

**Windows Server requirements**

Your source environment should run Windows Server 2016 or later for optimal
compatibility. Elastic Beanstalk supports these Windows Server versions as target platforms:

- Windows Server 2025
- Windows Server 2022
- Windows Server 2019
- Windows Server 2016

**EB CLI installation**

- _Default workflow (without the `--remote`
  option)_:
  - Python and the Elastic Beanstalk Command Line Interface (EB CLI) must be installed on the
    server that contains the application that you want to migrate to Elastic Beanstalk. While it
    is not required, we recommend installing the EB CLI inside a
    `virtualenv` sandbox as described in [Install the EB CLI in a virtual
    environment](eb-cli3.md#eb-cli3-install-virtualenv "eb-cli3.md#eb-cli3-install-virtualenv").

- _Using the `--remote` option_:
  - Python and
    the Elastic Beanstalk Command Line Interface (EB CLI) must be installed on your bastion host. While it
    is not required, we recommend installing the EB CLI inside a `virtualenv`
    sandbox as described in [Install the EB CLI in a virtual
    environment](eb-cli3.md#eb-cli3-install-virtualenv "eb-cli3.md#eb-cli3-install-virtualenv").

**Required permissions**

You need the following credentials and permissions:

- Administrator privileges on the source IIS server or on the bastion host (if using
  the `--remote` option).
- AWS credentials with permissions to create and manage Elastic Beanstalk resources

**Web Deploy 3.6**

Microsoft Web Deploy tool (version 3.6 or later) must be installed on your source
server or on the bastion host (if using the `--remote` option). This tool is
used by **eb migrate** to package your applications.

To verify the installation run the following command:

:

```
`PS C:\migrations_workspace>` `Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\IIS Extensions\MSDeploy\3" -Name InstallPath`
`InstallPath : C:\Program Files\IIS\Microsoft Web Deploy V3\
...`
```

For installation instructions, see [Installing and Configuring Web Deploy on IIS 8.0 or Later](https://learn.microsoft.com/en-us/iis/install/installing-publishing-technologies/installing-and-configuring-web-deploy-on-iis-80-or-later "https://learn.microsoft.com/en-us/iis/install/installing-publishing-technologies/installing-and-configuring-web-deploy-on-iis-80-or-later") on the Microsoft
Windows product documentation website.

**Network requirements**

- _Default workflow (without the `--remote`
  option)_:
  - Your source server must have outbound internet access to AWS services.

- _Using the `--remote` option_:
  - Your source server must have outbound internet access to AWS services.
  - Configure the proper security group ingress rules that allow for an outgoing
    network connection from your bastion host and an incoming connection into the remote
    machine. Ensure the IP of the bastion host is allow-listed via TCP on port 22 to
    access the remote machine.
  - Ensure your SSH client is installed and running on your remote machine as well as
    your bastion host.
  - Ensure that your firewall configuration contains the appropriate rules that open
    up port 22 or allow connection to the client.
  - Test your connection by manually SSH-ing into the remote host from the bastion
    host before attempting migration.
