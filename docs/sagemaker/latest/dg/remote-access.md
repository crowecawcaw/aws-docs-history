# Connect your local Visual Studio Code to SageMaker spaces with remote

access

You can remotely connect from Visual Studio Code to Amazon SageMaker Studio spaces. You can use your
customized local VS Code setup, including AI-assisted development tools and custom
extensions, with the scalable compute resources in Amazon SageMaker AI. This guide provides concepts
and setup instructions for administrators and users.

A remote VS Code connection establishes a secure connection between your local VS Code
and SageMaker spaces. This connection lets you:

- **Access SageMaker AI compute resources** — Run code on
  scalable SageMaker AI infrastructure from your local environment
- **Maintain security boundaries** — Work within the
  same security framework as SageMaker AI
- **Keep your familiar Visual Studio Code experience** — Use
  compatible local extensions, themes, and configurations that support [Microsoft Remote
  Development](https://code.visualstudio.com/docs/remote/remote-overview "https://code.visualstudio.com/docs/remote/remote-overview")

###### Note

Not all VS Code extensions are compatible with remote development. Extensions that
require local GUI components, have architecture dependencies, or need specific
client-server interactions may not work properly in the remote environment. Verify that
your required extensions support Microsoft Remote Development before use.

###### Topics

- [Key concepts](#remote-access-key-concepts "#remote-access-key-concepts")
- [Connection methods](#remote-access-connection-methods "#remote-access-connection-methods")
- [Supported IDEs](#remote-access-supported-ides "#remote-access-supported-ides")
- [VS Code version
  requirement](#remote-access-vs-code-version-requirement "#remote-access-vs-code-version-requirement")
- [Operating system requirements](#remote-access-os-requirements "#remote-access-os-requirements")
- [Local machine prerequisites](#remote-access-local-prerequisites "#remote-access-local-prerequisites")
- [Image requirements](#remote-access-image-requirements "#remote-access-image-requirements")
- [Instance requirements](#remote-access-instance-requirements "#remote-access-instance-requirements")
- [Set up remote access](remote-access-remote-setup.md "remote-access-remote-setup.md")
- [Set up local Visual Studio Code](remote-access-local-ide-setup.md "remote-access-local-ide-setup.md")

## Key concepts

- **Remote connection** — A secure tunnel between
  your local VS Code and a SageMaker space. This connection enables interactive
  development and code execution in VS Code using SageMaker AI compute resources.
- [**Amazon SageMaker Studio space**](studio-updated-spaces.md "studio-updated-spaces.md") — A dedicated environment
  within Amazon SageMaker Studio where you can manage your storage and resources for your
  Studio applications.
- **Deep link** — A button (direct URL) from the
  SageMaker UI that initiates a remote connection to your local IDE.

## Connection methods

There are three main ways to connect your local VS Code to SageMaker spaces:

- **Deep link access** — You can connect directly
  to a specific space by using the **Open in VS Code** button
  available in SageMaker AI. This uses URL patterns to establish a remote connection and
  open your SageMaker space in VS Code.
- [**AWS Toolkit for Visual Studio Code**](../../../toolkit-for-vscode/latest/userguide/welcome.md "../../../toolkit-for-vscode/latest/userguide/welcome.md") — You can authenticate with
  AWS Toolkit for Visual Studio Code. This allows you to connect to spaces and open a remotely
  connected window from VS Code.
- **SSH terminal connection** — You can connect via
  command line using SSH configuration.

## Supported IDEs

Remote connection to Studio spaces supports:

- [Visual Studio Code](https://code.visualstudio.com/ "https://code.visualstudio.com/")

## VS Code version

requirement

VS Code version [v1.90](https://code.visualstudio.com/updates/v1_90 "https://code.visualstudio.com/updates/v1_90") or greater is required. We recommend using the [latest stable version of
VS Code](https://code.visualstudio.com/updates "https://code.visualstudio.com/updates").

## Operating system requirements

You need one of the following operating systems to remotely connect to Studio
spaces:

- macOS 13+
- Windows 10
  - [Windows 10 support ends on October 14, 2025](https://support.microsoft.com/en-us/windows/windows-10-support-ends-on-october-14-2025-2ca8b313-1946-43d3-b55c-2b95b107f281 "https://support.microsoft.com/en-us/windows/windows-10-support-ends-on-october-14-2025-2ca8b313-1946-43d3-b55c-2b95b107f281")

- Windows 11
- Linux
  - Install the official [Microsoft
    VS Code for Linux](https://code.visualstudio.com/docs/setup/linux "https://code.visualstudio.com/docs/setup/linux"), not an open-source version

## Local machine prerequisites

Before connecting your local Visual Studio Code to Studio spaces, ensure your local
machine has the required dependencies and network access.

###### Important

Environments with software installation restrictions may prevent users from
installing required dependencies. The AWS Toolkit for Visual Studio Code automatically searches for
these dependencies when initiating remote connections and will prompt for
installation if any are missing. Coordinate with your IT department to ensure these
components are available.

**Required local dependencies**

Your local machine must have the following components installed:

- **[Remote-SSH
  Extension](https://code.visualstudio.com/docs/remote/ssh "https://code.visualstudio.com/docs/remote/ssh")** — Standard VS Code Marketplace extension
  for remote development
- **[Session Manager plugin](../../../systems-manager/latest/userguide/session-manager-working-with-install-plugin.md "../../../systems-manager/latest/userguide/session-manager-working-with-install-plugin.md")** — Required for secure session
  management
- **SSH Client** — Standard component on most
  machines ([OpenSSH recommended for Windows](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse "https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse"))
- **[VS Code
  CLI Command](https://code.visualstudio.com/docs/configure/command-line "https://code.visualstudio.com/docs/configure/command-line")** — Typically included with VS Code
  installation

**Platform-specific requirements**

- **Windows users** — PowerShell 5.1 or later is
  required for SSH terminal connections

**Network connectivity requirements**

Your local machine must have network access to [Session Manager endpoints](../../../general/latest/gr/ssm.md "../../../general/latest/gr/ssm.md"). For example, in
US East (N. Virginia) (us-east-1) these can be:

- ssm.us-east-1.amazonaws.com
- ssm.us-east-1.api.aws
- ssmmessages.us-east-1.amazonaws.com
- ec2messages.us-east-1.amazonaws.com

## Image requirements

**SageMaker Distribution images**

When using SageMaker Distribution with remote access, use [SageMaker Distribution](sagemaker-distribution.md "sagemaker-distribution.md")
version 2.7 or later.

**Custom images**

When you [Bring your own image (BYOI)](studio-updated-byoi.md "studio-updated-byoi.md")
with remote access, ensure that you follow the [custom image
specifications](studio-updated-byoi-specs.md "studio-updated-byoi-specs.md") and ensure the following dependencies are installed:

- `curl` or `wget` — Required for downloading AWS CLI
  components
- `unzip` — Required for extracting AWS CLI installation files
- `tar` — Required for archive extraction
- `gzip` — Required for compressed file handling

## Instance requirements

- **Memory** — 8GB or more
- **Instance types** — Use instances with at least
  8GB of memory. The following instance types are _not_
  supported due to insufficient memory (less than 8GB): `ml.t3.medium`,
  `ml.c7i.large`, `ml.c6i.large`,
  `ml.c6id.large`, and `ml.c5.large`. For a more
  complete list of instance types, see the [Amazon EC2 On-Demand
  Pricing page](https://aws.amazon.com/ec2/pricing/on-demand/ "https://aws.amazon.com/ec2/pricing/on-demand/").

###### Topics

- [Set up remote access](remote-access-remote-setup.md "remote-access-remote-setup.md")
- [Set up local Visual Studio Code](remote-access-local-ide-setup.md "remote-access-local-ide-setup.md")
