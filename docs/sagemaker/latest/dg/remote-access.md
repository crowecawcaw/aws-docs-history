

# Connect your Remote IDE to SageMaker spaces with remote access
<a name="remote-access"></a>

You can remotely connect from your Remote IDE to Amazon SageMaker Studio spaces. You can use your customized local IDE setup, including AI-assisted development tools and custom extensions, with the scalable compute resources in Amazon SageMaker AI. This guide provides concepts and setup instructions for administrators and users.

A Remote IDE connection establishes a secure connection between your local IDE and SageMaker spaces. This connection lets you:
+ **Access SageMaker AI compute resources** — Run code on scalable SageMaker AI infrastructure from your local environment
+ **Maintain security boundaries** — Work within the same security framework as SageMaker AI
+ **Keep your familiar IDE experience** — Use compatible local extensions, themes, and configurations that support remote development

**Note**  
Not all IDE extensions are compatible with remote development. Extensions that require local GUI components, have architecture dependencies, or need specific client-server interactions may not work properly in the remote environment. Verify that your required extensions support remote development before use.

**Topics**
+ [Key concepts](#remote-access-key-concepts)
+ [Connection methods](#remote-access-connection-methods)
+ [Supported IDEs](#remote-access-supported-ides)
+ [IDE version requirements](#remote-access-ide-version-requirements)
+ [Operating system requirements](#remote-access-os-requirements)
+ [Local machine prerequisites](#remote-access-local-prerequisites)
+ [Image requirements](#remote-access-image-requirements)
+ [Instance requirements](#remote-access-instance-requirements)
+ [Set up remote access](remote-access-remote-setup.md)
+ [Set up Remote IDE](remote-access-local-ide-setup.md)
+ [Supported AWS Regions](remote-access-supported-regions.md)
+ [Installing Amazon SageMaker AI skills](remote-access-install-skills.md)

## Key concepts
<a name="remote-access-key-concepts"></a>
+ **Remote connection** — A secure tunnel between your Remote IDE and a SageMaker space. This connection enables interactive development and code execution using SageMaker AI compute resources.
+ [**Amazon SageMaker Studio space**](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-spaces.html) — A dedicated environment within Amazon SageMaker Studio where you can manage your storage and resources for your Studio applications.
+ **Deep link** — A button (direct URL) from the SageMaker UI that initiates a remote connection to your local IDE.

## Connection methods
<a name="remote-access-connection-methods"></a>

There are three main ways to connect your Remote IDE to SageMaker spaces:
+ **Deep link access** — You can connect directly to a specific space by using the **Open space with** button available in SageMaker AI. This uses URL patterns to establish a remote connection and open your SageMaker space in your Remote IDE.
+ [**AWS Toolkit for Visual Studio Code**](https://docs.aws.amazon.com/toolkit-for-vscode/latest/userguide/welcome.html) — You can authenticate with AWS Toolkit for Visual Studio Code. This allows you to connect to spaces and open a remotely connected window from your Remote IDE.
+ **SSH terminal connection** — You can connect via command line using SSH configuration.

## Supported IDEs
<a name="remote-access-supported-ides"></a>

Remote connection to Studio spaces supports:
+ [Visual Studio Code](https://code.visualstudio.com/)
+ [Kiro](https://kiro.dev/)
+ [Cursor](https://cursor.com/home)

## IDE version requirements
<a name="remote-access-ide-version-requirements"></a>

The following table lists the minimum version requirements for each supported Remote IDE.


| IDE | Minimum version | 
| --- | --- | 
| Visual Studio Code | [v1.90](https://code.visualstudio.com/updates/v1_90) or greater. We recommend using the [latest stable version](https://code.visualstudio.com/updates). | 
| Kiro | v0.10.78 or greater | 
| Cursor | v2.6.18 or greater | 

The AWS Toolkit extension is required to connect your Remote IDE to Studio spaces. For Kiro and Cursor, AWS Toolkit extension version v3.100 or greater is required.

## Operating system requirements
<a name="remote-access-os-requirements"></a>

You need one of the following operating systems to remotely connect to Studio spaces:
+ macOS 13\+
+ Windows 10
  + [Windows 10 support ends on October 14, 2025](https://support.microsoft.com/en-us/windows/windows-10-support-ends-on-october-14-2025-2ca8b313-1946-43d3-b55c-2b95b107f281)
+ Windows 11
+ Linux
  + For VS Code, install the official [Microsoft VS Code for Linux](https://code.visualstudio.com/docs/setup/linux), not an open-source version

## Local machine prerequisites
<a name="remote-access-local-prerequisites"></a>

Before connecting your Remote IDE to Studio spaces, ensure your local machine has the required dependencies and network access.

**Important**  
Environments with software installation restrictions may prevent users from installing required dependencies. The AWS Toolkit for Visual Studio Code automatically searches for these dependencies when initiating remote connections and will prompt for installation if any are missing. Coordinate with your IT department to ensure these components are available.

**Required local dependencies**

Your local machine must have the following components installed:
+ **[Remote-SSH Extension](https://code.visualstudio.com/docs/remote/ssh)** — Remote development extension for your IDE (available in the extension marketplace for VS Code, Kiro, and Cursor)
+ **[Session Manager plugin](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-install-plugin.html)** — Required for secure session management
+ **SSH Client** — Standard component on most machines ([OpenSSH recommended for Windows](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse))
+ **IDE CLI Command** — Typically included with IDE installation (for example, `code` for VS Code, `kiro` for Kiro, `cursor` for Cursor)

**Platform-specific requirements**
+ **Windows users** — PowerShell 5.1 or later is required for SSH terminal connections

**Network connectivity requirements**

Your local machine must have network access to [Session Manager endpoints](https://docs.aws.amazon.com/general/latest/gr/ssm.html). For example, in US East (N. Virginia) (us-east-1) these can be:
+ ssm.us-east-1.amazonaws.com
+ ssm.us-east-1.api.aws
+ ssmmessages.us-east-1.amazonaws.com
+ ec2messages.us-east-1.amazonaws.com

## Image requirements
<a name="remote-access-image-requirements"></a>

**SageMaker Distribution images**

When using SageMaker Distribution with remote access, use [SageMaker Distribution](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-distribution.html) version 2.7 or later.

**Custom images**

When you [Bring your own image (BYOI)](studio-updated-byoi.md) with remote access, ensure that you follow the [custom image specifications](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-byoi-specs.html) and ensure the following dependencies are installed:
+ `curl` or `wget` — Required for downloading AWS CLI components
+ `unzip` — Required for extracting AWS CLI installation files
+ `tar` — Required for archive extraction
+ `gzip` — Required for compressed file handling

## Instance requirements
<a name="remote-access-instance-requirements"></a>
+ **Memory** — 8GB or more
+ **Instance types** — Use instances with at least 8GB of memory. The following instance types are *not* supported due to insufficient memory (less than 8GB): `ml.t3.medium`, `ml.c7i.large`, `ml.c6i.large`, `ml.c6id.large`, and `ml.c5.large`. For a more complete list of instance types, see the [Amazon EC2 On-Demand Pricing page](https://aws.amazon.com/ec2/pricing/on-demand/).

**Topics**
+ [Key concepts](#remote-access-key-concepts)
+ [Connection methods](#remote-access-connection-methods)
+ [Supported IDEs](#remote-access-supported-ides)
+ [IDE version requirements](#remote-access-ide-version-requirements)
+ [Operating system requirements](#remote-access-os-requirements)
+ [Local machine prerequisites](#remote-access-local-prerequisites)
+ [Image requirements](#remote-access-image-requirements)
+ [Instance requirements](#remote-access-instance-requirements)
+ [Set up remote access](remote-access-remote-setup.md)
+ [Set up Remote IDE](remote-access-local-ide-setup.md)
+ [Supported AWS Regions](remote-access-supported-regions.md)
+ [Installing Amazon SageMaker AI skills](remote-access-install-skills.md)