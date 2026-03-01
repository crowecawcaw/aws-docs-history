AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET is no longer open to new customers. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/ "https://aws.amazon.com/transform/"), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# Getting started with AWS App2Container

AWS App2Container is a tool that helps you break down the work of moving your applications
into containers, and configuring them to be hosted in AWS using the Amazon ECS, Amazon EKS, or
App Runner container management services.

The following sections demonstrate the initial setup of your containerization environment,
starting with prerequisites and initial workflow decisions. Then we take you step by
step through containerizing a basic application using App2Container. We generate the artifacts
that you can use to deploy it on Amazon ECS, Amazon EKS, or AWS App Runner, and then we clean up.

###### Note

To avoid creating billable AWS resources, we stop before the final deployment. You can
review the deployment artifacts that are created by the **generate app-deployment**
command to see what we would create.

For an overview of the command phases that includes summary information and command
reference links for all of the App2Container commands, see the [App2Container command reference](a2c-commands.md "a2c-commands.md").

###### Contents

- [Understand Docker containers](#understand-containers "#understand-containers")
- [Decide where containerization will run](#setup-worker-machine "#setup-worker-machine")
- [Prerequisites: Set up your servers](#start-containerize-prereq "#start-containerize-prereq")
- [Step 1: Install App2Container](#start-step1-install "#start-step1-install")
- [Step 2: Initialize App2Container](#start-step2-initialize "#start-step2-initialize")
- [Step 3: Analyze your application](#start-step3-analyze "#start-step3-analyze")
- [Step 4: Transform your application](#start-step4-transform "#start-step4-transform")
- [Step 5: Deploy your application](#start-step5-deploy "#start-step5-deploy")
- [Step 6: Clean up](#start-step6-cleanup "#start-step6-cleanup")

## Understand Docker containers

The following resources can help you get the most out of your application containers
by understanding what goes into them.

- To learn more about Docker containers on AWS, see [What is Docker?](https://aws.amazon.com/docker "https://aws.amazon.com/docker").
- Use the Docker command line reference to look up Docker commands. See
  [Use the
  Docker command line](https://docs.docker.com/engine/reference/commandline/cli/ "https://docs.docker.com/engine/reference/commandline/cli/").

## Decide where containerization will run

To use App2Container on the server where the applications are running, you must set up an
AWS profile, install App2Container, and install the Docker engine. If your server does not meet
the requirements to containerize your application and deploy it to AWS, or if you do not
want to install the Docker engine on the application server, you can set up and use a worker
machine. On the worker machine, you can run the steps to containerize your application and
deploy it to AWS, or you can set up connectivity between the worker machine and the
application servers to run remote commands from the worker machine, targeting the
application servers.

The following are example situations where you might decide to set up
a worker machine:

- Your application servers are running in an on-premises data center and
  they do not have internet access.
- Your application server is running on a Windows operating system that
  does not support containers. For more information, see [Supported applications](supported-applications.md "supported-applications.md").
- You prefer to use a dedicated server to run the containerization and
  deployment steps.
- You want to consolidate your work by using a worker machine to run commands
  for all of your application servers.

When you set up a worker machine to handle the steps to containerize and deploy
your applications, it must have the same operating system platform as your application
server (Linux or Windows), and the operating system must support containers. We
recommend that you launch an Amazon EC2 instance as the worker machine, using an Amazon
Machine Image (AMI) that is optimized for Amazon ECS.

## Prerequisites: Set up your servers

Before you use App2Container for the first time, make sure that your application environment meets
all of the requirements that are listed for your operating system (OS) platform in the [Supported applications](supported-applications.md "supported-applications.md") section
of this guide.

Choose the tab that matches your operating system (OS) platform to continue:

Linux
To run on a Linux platform, App2Container has the following additional requirements
for the servers where you run App2Container commands. This includes application servers
and the worker machine, if you have one configured.

- There are one or more Java applications running on each application
  server whose inventory is the subject of the **analyze**
  or **remote analyze** command.
- You have root access on the servers.
- The servers have **tar** and at least 20 GB of free
  space.

Windows
To run on a Windows platform, App2Container has the following additional requirements
for the servers where you run App2Container commands. This includes application servers
and the worker machine, if you have one configured.

- There are one or more applications running in IIS on each application
  server whose inventory is the subject of the **analyze**
  or **remote analyze** command.
- You are logged in as the Administrator user on the servers.
- The servers have Windows PowerShell version 5.1 or PowerShell version
  6 or later and at least 20-30 GB of free space.

Complete the following tasks before you use App2Container for the first time.

- [Sign up for AWS](#sign-up-for-aws "#sign-up-for-aws")
- [Grant permissions to run AWS App2Container commands](#setup-grant-permissions "#setup-grant-permissions")
- [Enable remote access for a worker machine (optional)](#setup-remote-access "#setup-remote-access")
- [Configure your AWS profile](#setup-aws-profile "#setup-aws-profile")
- [Install the Docker engine](#setup-install-docker "#setup-install-docker")

### Sign up for AWS

When you sign up for Amazon Web Services (AWS), your AWS account is automatically
signed up for all services in AWS. You are charged only for the services that you
use.

If you do not have an AWS account already, use the following procedure to create
one.

###### To create an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

### Grant permissions to run AWS App2Container commands

App2Container needs access to AWS services in order to run most of its commands. There are
two very different sets of permissions needed to run **app2container**
commands.

- The general purpose IAM user, group, or role can run all of the commands
  _except_ commands that are run with the
  `--deploy` option.
- For deployment, App2Container must be able to create or update AWS objects for
  container management services (Amazon ECR with Amazon ECS, Amazon EKS, or AWS App Runner), and to
  create CI/CD pipelines with AWS CodePipeline. This requires elevated permissions that
  should only be used for deployment.

We recommend that you create general purpose IAM resources, and if you plan to use
App2Container to deploy your containers or create pipelines, that you create separate IAM
resources for deployment.

For instructions on how to set up your IAM resources for App2Container, and policy examples
that include resources and actions that App2Container needs access to, see [Identity and access management in App2Container](iam-a2c.md "iam-a2c.md").

###### Note

You can use an instance profile to pass an IAM role to an Amazon EC2 instance. App2Container
detects if there is an instance profile associated with the application server or
worker machine when you run the **init** command. If it detects an
instance profile, the **init** command prompts if you want to use
it.

To find out more about using instance profiles, see [Using
instance profiles](../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.md") in the _IAM User Guide_.

### Enable remote access for a worker machine (optional)

To enable your worker machine to run remote commands for your application servers, you
must ensure that the worker machine can connect.

For the required setup to enable remote access, choose the operating system tab that
matches your application server.

Linux
For Linux application servers, you can use SSH key-based or SSH
certificate-based connections. You must ensure that there is network
connectivity between the worker machine and the application server, and
verify that your worker machine can connect.

###### Certificate-based connections

By default, App2Container trusts the certificate, and does not verify its
validity before connecting to your application server. To change this
behavior, set the `acceptCerts` attribute to
`false` in the `init.json`
file.

Windows
To connect to a Windows application server from a Windows Server 2016,
2019, or 2022 worker machine, use the WinRM protocol. Your application server must
meet the requirements that are listed for Windows in the [Supported applications](supported-applications.md "supported-applications.md") section of this user
guide.

###### Note

App2Container does not support applications running on Windows client operating systems, such as Windows 7 or Windows 10.

1. ###### Worker machine

To ensure that you can run PowerShell scripts on the worker
machine, set the PowerShell Execution Policy to one of the following
values:

_RemoteSigned_

Example:

```
`PS>` `Set-ExecutionPolicy RemoteSigned`
```

_Unrestricted_

Example:

```
`PS>` `Set-ExecutionPolicy Unrestricted`
```

2. ###### Application servers

Complete the following steps on each application server to enable
remote access from the worker machine.

    1. Ensure network connectivity to the application server over
     WinRM port 5986.
    2. Download the WinRMSetup.ps1 PowerShell script to your
     application server from the following location: [WinRMSetup.ps1](https://app2container-release-us-east-1.s3.us-east-1.amazonaws.com/latest/windows/WinRMSetup.ps1 "https://app2container-release-us-east-1.s3.us-east-1.amazonaws.com/latest/windows/WinRMSetup.ps1").


    ###### Note

    Checksum files for this script can be downloaded using
     the following links:



    	* [WinRMSetup.ps1.sha256](https://app2container-release-us-east-1.s3.us-east-1.amazonaws.com/latest/windows/WinRMSetup.ps1.sha256 "https://app2container-release-us-east-1.s3.us-east-1.amazonaws.com/latest/windows/WinRMSetup.ps1.sha256")
    	* [WinRMSetup.ps1.md5](https://app2container-release-us-east-1.s3.us-east-1.amazonaws.com/latest/windows/WinRMSetup.ps1.md5 "https://app2container-release-us-east-1.s3.us-east-1.amazonaws.com/latest/windows/WinRMSetup.ps1.md5")
    3. Download the [New-SelfsignedCertificateEx.ps1](https://github.com/Azure/azure-libraries-for-net/blob/master/Samples/Asset/New-SelfSignedCertificateEx.ps1 "https://github.com/Azure/azure-libraries-for-net/blob/master/Samples/Asset/New-SelfSignedCertificateEx.ps1") PowerShell
     script from the Microsoft Technet gallery. The
     WinRMSetup.ps1 PowerShell script from step 2 uses it to
     generate a self-signed certificate.


    ###### Note

    This script must run from the same directory where the
     WinRMSetup.ps1 PowerShell script from step 2 is
     located.
    4. Run the WinRMSetup.ps1 PowerShell script on the
     application server. The script ensures that WinRM is
     enabled, and generates self-signed certificates that are
     used to secure the connection from the worker
     machine.

### Configure your AWS profile

AWS App2Container requires command line access to AWS resources for containerization and
deployment commands. It uses information from your AWS profile to configure access to
AWS resources for your account. To run App2Container commands, you must install and configure
a command line tool on the application servers and worker machines where you run the
commands.

###### Note

- AWS Tools for Windows PowerShell is required for running App2Container commands in PowerShell on a
  Windows server.
- Tools for Windows PowerShell comes pre-installed on Windows-based Amazon Machine Images (AMIs).
  If your application server or worker machine is an Amazon EC2 instance that was
  launched from one of these AMIs, you can skip to configuring your AWS
  profile. See [Shared
  credentials](../../../powershell/latest/userguide/shared-credentials-in-aws-powershell.md "../../../powershell/latest/userguide/shared-credentials-in-aws-powershell.md") in the _AWS Tools for PowerShell User Guide_ for more
  details.

To install the AWS Command Line Interface (AWS CLI) or AWS Tools for Windows PowerShell command line tools, and to configure
your AWS profile, follow the instructions on the tab that matches your command line
tool.

AWS CLI
To install the AWS CLI and set up your AWS profile, follow these
steps:

1. Install the AWS CLI according to the instructions in the
   _AWS Command Line Interface User Guide_. For more information, see
   [Installing
   the AWS CLI](../../../cli/latest/userguide/cli-chap-getting-set-up.md "../../../cli/latest/userguide/cli-chap-getting-set-up.md").
2. To configure your AWS default profile, use the **aws
   configure** command. For more information, see [Configuration
   basics](../../../cli/latest/userguide/cli-configure-quickstart.md "../../../cli/latest/userguide/cli-configure-quickstart.md") in the
   _AWS Command Line Interface User Guide_.

Tools for Windows PowerShell
To install Tools for Windows PowerShell and set up your AWS profile, follow these steps:

1. Install the Tools for Windows PowerShell according to the instructions in the
   _AWS Tools for PowerShell User Guide_. For more information see
   [Installing
   the AWS Tools for Windows PowerShell](../../../powershell/latest/userguide/pstools-getting-set-up.md "../../../powershell/latest/userguide/pstools-getting-set-up.md").
2. To set up your AWS default profile, use the [Initialize-AWSDefaultConfiguration](../../../powershell/latest/reference/items/Initialize-AWSDefaultConfiguration.md "../../../powershell/latest/reference/items/Initialize-AWSDefaultConfiguration.md") cmdlet. For more
   information about shared credentials in Tools for Windows PowerShell, see [Shared credentials](../../../powershell/latest/userguide/shared-credentials-in-aws-powershell.md "../../../powershell/latest/userguide/shared-credentials-in-aws-powershell.md") in the
   _AWS Tools for PowerShell User Guide_.

After you containerize your applications, you can also use the AWS CLI or Tools for Windows PowerShell to
deploy them on AWS, though we recommend using the `--deploy` option with
the **generate app-deployment** and **generate pipeline**
commands to do your deployment.

### Install the Docker engine

App2Container uses the Docker engine (Docker CE) to create container images and generate
Dockerfiles that run the containers hosted on Amazon ECS, Amazon EKS, or AWS App Runner. You must install the Docker engine on the application server or worker
machine that you'll use to containerize the application using the
**containerize** command.

Linux
Use the following procedure to install Docker on Linux.

###### To install the Docker engine

1. ###### Install Docker version 17.07 or later

Choose your Linux distribution from the following options, and
follow instructions to download and install the Docker engine, using the
links provided.

 

_Amazon Linux_

To download and install the Docker engine on Amazon Linux
instances, see [Docker basics
for Amazon ECS](../../../AmazonECS/latest/developerguide/docker-basics.md "../../../AmazonECS/latest/developerguide/docker-basics.md") in the
_Amazon Elastic Container Service Developer Guide_. This works
with any Amazon Linux instance.

_RHEL_

Recent versions of RHEL do not natively support the
Docker engine. However, you can still download and install
the Docker engine on RHEL to create containers that will be
hosted and run on Amazon ECS, Amazon EKS, or AWS App Runner. To do this,
follow the instructions given for CentOS on the Docker
website: [Install Docker engine](https://docs.docker.com/engine/install/ "https://docs.docker.com/engine/install/").

_All other supported distributions (CentOS, Ubuntu)_

To download and install the Docker engine for other
supported Linux distributions, follow the instructions
for your Linux distribution on the Docker website:
[Install Docker engine](https://docs.docker.com/engine/install/ "https://docs.docker.com/engine/install/"). 2. ###### Verify the Docker installation

To verify that your Docker installation was successful, run the
following command.

```
`$` `docker run -it hello-world`
```

When the command runs, it pulls the latest hello-world application
from the Docker repository, if applicable. When the application has
finished downloading, it displays a "Hello" message followed by
information on how this command verified your installation of
Docker.

Windows
Use the following procedure to install Docker on Windows.

###### To install the Docker engine

1. ###### Install Docker version 17.07 or later

To download and install the Docker engine on Windows, see [Get started: Prep Windows for containers (Install Docker
section)](https://docs.microsoft.com/en-us/virtualization/windowscontainers/quick-start/set-up-environment?tabs=Windows-Server#install-docker "https://docs.microsoft.com/en-us/virtualization/windowscontainers/quick-start/set-up-environment?tabs=Windows-Server#install-docker"). 2. ###### Verify the Docker installation

To verify that your Docker installation was successful, run the
following command.

```
`PS>` `docker run -it hello-world`
```

When the command runs, it pulls the latest hello-world application
from the Docker repository, if applicable. When the application has
finished downloading, it displays a "Hello" message followed by
information on how this command verified your installation of
Docker.

## Step 1: Install App2Container

To get started with App2Container, the first step is to download and install the
application. To help ensure a successful installation, you can verify the
integrity and authenticity of the binary file before installing it.

###### Tip

For Amazon EC2 instances, you can perform Step 1, Step 2, Step 3, and Step 4 by using an
AWS Systems Manager Automation runbook. For more information, see [App2Container Automation runbook](automation-runbook.md "automation-runbook.md").

If you prefer, you can replatform your applications running on Amazon EC2 to containers and
deploy them to Amazon ECS on AWS Fargate with a console-based experience by using the
_Replatform applications to Amazon ECS_ template in the [Migration Hub Orchestrator console](https://console.aws.amazon.com/migrationhub/orchestrator "https://console.aws.amazon.com/migrationhub/orchestrator"). For more
information, see the [_AWS Migration Hub Orchestrator User Guide_](../../../migrationhub-orchestrator/latest/userguide/replatform-to-ecs.md "../../../migrationhub-orchestrator/latest/userguide/replatform-to-ecs.md").

Choose the tab that matches your operating system (OS) platform to continue:

Linux
App2Container for Linux is packaged as a tar.gz archive. The archive contains
an interactive shell script that installs App2Container on your server. If you
use an application server and a worker machine, you must install
App2Container on both.

###### To download and install App2Container for Linux

1. Download the installation file in one of the following ways:
   - Use the **curl** command to download the App2Container
     installation package from Amazon S3.

   ```
   `$` `curl -o AWSApp2Container-installer-linux.tar.gz https://app2container-release-us-east-1.s3.us-east-1.amazonaws.com/latest/linux/AWSApp2Container-installer-linux.tar.gz`
   ```

   - Use your browser to download the installer from the following URL: [https://app2container-release-us-east-1.s3.us-east-1.amazonaws.com/latest/linux/AWSApp2Container-installer-linux.tar.gz](https://app2container-release-us-east-1.s3.us-east-1.amazonaws.com/latest/linux/AWSApp2Container-installer-linux.tar.gz "https://app2container-release-us-east-1.s3.us-east-1.amazonaws.com/latest/linux/AWSApp2Container-installer-linux.tar.gz").

2. Extract the package to a local folder on the server.

```
`$` `sudo tar xvf AWSApp2Container-installer-linux.tar.gz`
```

3. Run the install script that you extracted from the package and follow the prompts.

```
`$` `sudo ./install.sh`
```

To check the downloaded tar.gz installer archive for integrity, you can validate the
SHA256 hash of the local file against the published hash file.

###### Verify the integrity of the download

1. ###### Generate hashes to verify

From the directory where you downloaded your tar.gz installer, run the
following command to generate the hash of the downloaded tar.gz file.

```
`$` `sha256sum AWSApp2Container-installer-linux.tar.gz`
`9482952019adb6df96c7be773aa20ecb8de559083b99c270c67c34da56dd8dee AWSApp2Container-installer-linux.tar.gz`
```

2. ###### Verify hashes against the public file

Download the App2Container hash file from Amazon S3 with the following link, and compare
the contents to the hash that you generated in step 1:

    * Download the App2Container hash file from Amazon S3:[AWSApp2Container-installer-linux.tar.gz.sha256](https://app2container-release-us-east-1.s3.us-east-1.amazonaws.com/latest/linux/AWSApp2Container-installer-linux.tar.gz.sha256 "https://app2container-release-us-east-1.s3.us-east-1.amazonaws.com/latest/linux/AWSApp2Container-installer-linux.tar.gz.sha256").

To verify the authenticity of the download, run the
following commands to download the certificate and signature files,
and verify the signature.

###### Verify the authenticity of the download

1. Download the App2Container certificate:

```
curl -o app2container.cert https://app2container-keys.s3.us-east-1.amazonaws.com/latest/app2container.cert
```

2. Download the App2Container signature file:

```
curl -o app2container.sig https://app2container-release-us-east-1.s3.us-east-1.amazonaws.com/latest/linux/app2container.sig
```

3. Verify the signature:

```
openssl dgst -sha256 -verify app2container.cert -signature app2container.sig /usr/bin/app2container
```

Windows
App2Container for Windows is packaged as a zip archive. The package contains a PowerShell
script that installs App2Container. If you use an application server and a worker
machine, you must install App2Container on both.

###### To download and install App2Container for Windows

1. Download the App2Container installation package, [AWSApp2Container-installer-windows.zip](https://app2container-release-us-east-1.s3.us-east-1.amazonaws.com/latest/windows/AWSApp2Container-installer-windows.zip "https://app2container-release-us-east-1.s3.us-east-1.amazonaws.com/latest/windows/AWSApp2Container-installer-windows.zip").
2. Extract the package to a local folder on the server and navigate to
   that folder.

###### Note

App2Container automatically enables NTFS long paths for all supported Windows
versions so that you can use file paths longer than 260 characters.
For more information about this setting, see [How
to enable NTFS Long Paths in Windows 10 / Windows Server
2016 / 2019 or newer](https://www.tgrmn.com/web/docs/enable-longpaths-windows.pdf "https://www.tgrmn.com/web/docs/enable-longpaths-windows.pdf") (PDF). 3. Run the install script from the folder where you extracted it, and follow the prompts.

```
`PS>` `.\install.ps1`
```

4. (Optional) To verify the authenticity of the download, use the `Get-AuthenticodeSignature`
   PowerShell command as follows to get the Authenticode Signature of the App2Container executable.

```
`PS>` `Get-AuthenticodeSignature `C:\Users\Administrator\app2container\AWSApp2Container\bin\app2container.exe``
```

To check the downloaded zip archive for integrity, you can validate the
SHA256 hash of the local file against the published hash file.

###### To verify the integrity of the download

1. ###### Generate hashes to verify

From the directory where you downloaded your zip archive, run the
following command to generate the hash of the downloaded archive file.

```
`PS>` `Get-FileHash C:\Users\Administrator\Downloads\AWSApp2Container-installer-windows.zip -Algorithm SHA256`
```

2. ###### Verify hashes against the public file

Download the App2Container hash file from Amazon S3 with the following link, and compare
the contents to the hash that you generated in step 1:

    * Download the App2Container hash file from Amazon S3:[AWSApp2Container-installer-windows.zip.sha256](https://app2container-release-us-east-1.s3.us-east-1.amazonaws.com/latest/windows/AWSApp2Container-installer-windows.zip.sha256 "https://app2container-release-us-east-1.s3.us-east-1.amazonaws.com/latest/windows/AWSApp2Container-installer-windows.zip.sha256").

## Step 2: Initialize App2Container

The containerization process consists of several distinct phases. This step focuses
on the initialization phase, during which you initialize App2Container's global settings, and
configure remote command settings if you are using a worker machine.

The **init** command performs one-time initialization tasks for App2Container. This interactive command prompts
for the information required to set up the local App2Container environment. Run this command before you run any other
App2Container commands. For more information, see the **[init](cmd-init.md "cmd-init.md")** command reference page.

If you are using a worker machine to run commands remotely on application
servers, you must also run the **remote configure** command on the worker
machine. For more information, see the **[remote configure](cmd-remote-configure.md "cmd-remote-configure.md")** command reference page.

Choose the tab that matches your operating system (OS) platform to continue:

Linux
On each server where you installed App2Container, run the [init](cmd-init.md "cmd-init.md")
command as follows.

```
`$` `sudo app2container init`
```

You are prompted to provide the following information. Choose
_<enter>_ to accept the default value.

- Workspace directory path – A local directory where App2Container can store
  artifacts during the containerization process. The default is
  `/root/app2container`.
- AWS profile – Contains information needed to run App2Container, such as your
  AWS access keys. For more information about AWS profiles, see
  [Configure your AWS profile](#setup-aws-profile "#setup-aws-profile").

###### Note

If App2Container detects an instance profile for your server, the
**init** command prompts if you want to use it. If you
don't specify any value, App2Container uses your AWS default profile.

- Amazon S3 bucket – You can optionally provide the name of an Amazon S3 bucket
  where you can extract artifacts using the **extract** command. The
  **containerize** command uses the extracted components to create the
  application container if the Amazon S3 bucket is configured. The default is no bucket.
- You can optionally upload logs and command-generated artifacts automatically to
  App2Container support when an app2container command crashes or encounters internal errors.
- Permission to collect usage metrics – You can optionally allow App2Container
  to collect information about the host operating system, application type,
  and the **app2container** commands that you run. The default
  is to allow the collection of metrics.
- Whether to enforce signed images – You can optionally require that images
  are signed using Docker Content Trust (DCT). The default is no.

Windows
On each server where you installed App2Container, run the [init](cmd-init.md "cmd-init.md")
command as follows.

```
`PS>` `app2container init`
```

You are prompted to provide the following information. Choose
_<enter>_ to accept the default value.

- Workspace directory path – A local directory where App2Container can store
  artifacts during the containerization process. The default is
  `C:\Users\Administrator\AppData\Local\app2container`.
- AWS profile – Contains information needed to run App2Container, such as your
  AWS access keys. For more information about AWS profiles, see
  [Configure your AWS profile](#setup-aws-profile "#setup-aws-profile").

###### Note

If App2Container detects an instance profile for your server, the
**init** command prompts if you want to use it. If you
don't specify any value, App2Container uses your AWS default profile.

- Amazon S3 bucket – You can optionally provide the name of an Amazon S3 bucket
  where you can extract artifacts using the **extract** command. The
  **containerize** command uses the extracted components to create the
  application container if the Amazon S3 bucket is configured. The default is no bucket.
- You can optionally upload logs and command-generated artifacts automatically to
  App2Container support when an app2container command crashes or encounters internal errors.
- Permission to collect usage metrics – You can optionally allow App2Container
  to collect information about the host operating system, application type,
  and the **app2container** commands that you run. The default
  is to allow the collection of metrics.
- Whether to enforce signed images – You can optionally require that images
  are signed using Docker Content Trust (DCT). The default is no.

## Step 3: Analyze your application

After you have completed setup and initialization tasks on your servers, you can
begin to analyze your applications. During the analysis phase, you take inventory of
the applications running on your application servers, and analyze specific applications
within your inventory.

Choose the tab that matches your operating system (OS) platform to continue:

Linux
On the application server, follow these steps to prepare to
containerize the applications.

###### Prepare for containerization

1. Run the [inventory](cmd-inventory.md "cmd-inventory.md") command as follows to
   list the Java applications that are running on your server.

```
`$` `sudo app2container inventory`
```

The output includes a JSON object collection with one entry for each application. Each
application object will include key/value pairs as shown in the following example.

```
"`java-app-id`": {
    "processId": `pid`,
    "cmdline": "/user/bin/java ...",
    "applicationType": "`java-apptype`"
}
```

2. Locate the application ID for the application to containerize in the JSON output of the
   **inventory** command, and then run the [analyze](cmd-analyze.md "cmd-analyze.md")
   command as follows, replacing `java-app-id` with the
   application ID that you located.

```
`$` `sudo app2container analyze --application-id `java-app-id``
```

The output is a JSON file, `analysis.json`, stored in the workspace
directory that you specified when you ran the **init** command. 3. (Optional) You can edit the information in the `containerParameters`
section of `analysis.json` as needed before continuing to the
next step.

Windows
On the application server, follow these steps to prepare to
containerize your applications.

###### Prepare for containerization

1. Run the [inventory](cmd-inventory.md "cmd-inventory.md") command as follows to
   list the ASP.NET applications that are running on your server.

```
`PS>` `app2container inventory`
```

The output includes a JSON object collection with one entry for each application. Each
application object will include key/value pairs as shown in the following example.

```
"`iis-app-id`": {
    "siteName": `My site name`,
    "bindings": "`http/*:80:`",
    "applicationType": "iis",
    "discoveredWebApps": [
        "`app1`",
        "`app2`"
    ]
}
```

2. Locate the application ID for the application to containerize in the JSON output of the
   **inventory** command, and then run the [analyze](cmd-analyze.md "cmd-analyze.md")
   command as follows, replacing `iis-app-id` with the
   application ID that you located.

```
`PS>` `app2container analyze --application-id `iis-app-id``
```

The output is a JSON file, `analysis.json`, stored in the workspace
directory that you specified when you ran the **init** command. 3. (Optional) You can edit the information in the `containerParameters`
section of `analysis.json` as needed before continuing to the
next step.

## Step 4: Transform your application

Now that your application has gone through the analysis phase, it's ready for
containerization. The transform phase creates the containers that your application
runs in after you deploy it to Amazon ECS, Amazon EKS, or App Runner, if eligible. For more
information about how App2Container integrates with container management services and other
products, see [Product and service integrations for AWS App2Container](a2c-integrations.md "a2c-integrations.md").

Choose the tab that matches your operating system (OS) platform to continue:

Linux
The transform phase depends on whether you are running all steps on the application
server, or are using the application server for the analysis and a worker machine for
containerization and deployment.

###### To containerize the application on the application server

If you are using an application server for all steps, run the [containerize](cmd-containerize.md "cmd-containerize.md") command as follows.

```
`$` `sudo app2container containerize --application-id `java-app-id``
```

The output is a set of deployment files that are stored in the workspace directory
that you specified when you ran the **init** command.

###### To containerize the application on a worker machine

If you are using a worker machine for containerization and deployment, use the
following procedure to transform the application.

1. On the application server, run the [extract](cmd-extract.md "cmd-extract.md")
   command as follows.

```
`$` `sudo app2container extract --application-id `java-app-id``
```

2. If you specified an Amazon S3 bucket when you ran the **init**
   command, the archive is extracted to that location. Otherwise, you can manually
   copy the resulting archive file to the worker machine.
3. On the worker machine, run the [containerize](cmd-containerize.md "cmd-containerize.md")
   command as follows.

```
`$` `sudo app2container containerize --input-archive /`path`/`extraction-file`.tar`
```

The output is a set of deployment artifacts that are stored in the workspace
directory that you specified when you ran the **init**
command.

Windows
The transform phase depends on whether you are running all steps on the application
server or using the application server for the analysis and a worker machine for
containerization and deployment.

###### To containerize the application on the application server

If you are using an application server for all steps, run the [containerize](cmd-containerize.md "cmd-containerize.md") command as follows.

```
`PS>` `app2container containerize --application-id `iis-app-id``
```

The output is a set of deployment files stored in the workspace directory that
you specified when you ran the **init** command.

###### To containerize the application on a worker machine

If you are using a worker machine for containerization and deployment, use the
following procedure to transform the application.

1. On the application server, run the [extract](cmd-extract.md "cmd-extract.md")
   command as follows.

```
`PS>` `app2container extract --application-id `iis-app-id``
```

2. If you specified an Amazon S3 bucket when you ran the **init**
   command, the archive is extracted to that location. Otherwise, you can manually
   copy the resulting archive file to the worker machine.
3. On the worker machine, run the [containerize](cmd-containerize.md "cmd-containerize.md")
   command as follows.

```
`PS>` `app2container containerize --input-archive `drive`:\`path`\`extraction-file`.zip`
```

The output is a set of deployment artifacts that are stored in the workspace
directory that you specified when you ran the **init**
command.

## Step 5: Deploy your application

After your application has gone through containerization, it's ready to deploy to
Amazon ECS, Amazon EKS, or App Runner, if eligible. When you run the **generate app-deployment**
command, App2Container creates an Amazon ECR repository where it stores your application container
artifacts for deployment. It also creates deployment configuration files that you can
deploy as follows:

- You can customize the deployment files, and have complete control over
  the deployment by running the AWS commands for your destination
  container management environment. When you run the **generate app-deployment**
  command without the `--deploy` option, App2Container returns instructions
  that you can use to deploy manually.
- If you're sure that you won't need to customize your deployment files,
  App2Container can optionally deploy your application containers directly to the
  container management environment that you have configured. To choose this
  option, run the **generate app-deployment** command with
  the `--deploy` option. You can verify the settings that App2Container
  used for the deployment by reviewing the deployment configuration files.

The deployment phase includes the option to create a deployment pipeline using
the **generate pipeline** command. That step is not covered here, in
order to prevent any unexpected charges for AWS resources. For more information,
see [app2container generate pipeline command](cmd-generate-pipeline.md "cmd-generate-pipeline.md") in
the command reference section.

Choose the tab that matches your operating system (OS) platform to continue:

Linux
Run the [generate app-deployment](cmd-generate-appdeploy.md "cmd-generate-appdeploy.md") command as follows
to deploy the application on AWS.

```
`$` `sudo app2container generate app-deployment --application-id `java-app-id``
```

You have now created deployment artifacts for your application! You can find
the deployment artifacts that the **generate app-deployment**
command created for you in the local directory for your application.

Windows
Run the [generate app-deployment](cmd-generate-appdeploy.md "cmd-generate-appdeploy.md") command as follows
to deploy the application on AWS.

```
`PS>` `app2container generate app-deployment --application-id `iis-smarts-51d2dbf8``
```

You have now created deployment artifacts for your application! You can find the
deployment artifacts that the **generate app-deployment** command
created for you in the local directory for your application.

###### Applications using Windows authentication

For applications using Windows authentication, you can use the `gMSAParameters` inside of
the `deployment.json` file to set the gMSA-related artifacts automatically during
generation of your CloudFormation template.

Perform the actions in the list below once per Active Directory domain before you update the gMSA parameters.

- Set up a secret in SecretsManager that stores the Domain credentials with the following key
  value pairs:

| Key      | Value                            |
| -------- | -------------------------------- |
| Username | <DomainNetBIOSName>\<DomainUser> |
| Password | <DomainUserPassword>             |

- For the VPC with the Domain Controller, verify that the DHCP options are set to reach the
  Domain Controller. The options for `DomainName` and `DomainNameServers` must
  be set correctly. See [DHCP options sets](../../../vpc/latest/userguide/VPC_DHCP_Options.md "../../../vpc/latest/userguide/VPC_DHCP_Options.md")
  for more information about how to set DHCP options.

## Step 6: Clean up

If you explored deployment options outside of the steps that we covered
for this tutorial, make sure that you tear down any application stacks that
might have been created, and verify that you have removed any artifacts that
were created in the process.

Choose the tab that matches your operating system (OS) platform to continue:

Linux
To remove App2Container from your application server or worker machine, delete the
`/usr/local/app2container` folder where it is installed, and then
remove this folder from your path.

To clean up your AWS profile, use the
**aws configure set** command. For more information, see [Set and
view configuration settings](../../../cli/latest/userguide/cli-configure-files.md#cli-configure-files-methods "../../../cli/latest/userguide/cli-configure-files.md#cli-configure-files-methods") in the _AWS Command Line Interface User Guide_.

Windows
To remove App2Container from your application server or worker machine, delete the
`C:\Users\Administrator\app2container` folder where it is installed, and then
remove this folder from your path.

To clean up your AWS profile, see [Removing
Credential Profiles](../../../powershell/latest/userguide/shared-credentials-in-aws-powershell.md#removing-credential-profiles "../../../powershell/latest/userguide/shared-credentials-in-aws-powershell.md#removing-credential-profiles") in the _AWS Tools for PowerShell User Guide_.
