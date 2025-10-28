# Install the Nitro Enclaves CLI on

Windows

The AWS Nitro Enclaves CLI is packaged together with all of the components that are
required to run Nitro Enclaves on a Windows parent instance. The package includes kernel
drivers for the Enclave and vsock devices, a service provider interface for Winsock to
support vsock sockets, the vsock-proxy, and the AWS Nitro Enclaves CLI.

The following instructions are for installing and uninstalling the AWS Nitro Enclaves CLI
on or from a parent instance running Windows.

###### Note

You may get the following error when you install, uninstall, or update the Nitro
CLI: `Installation failed with code 3010`. This message indicates that a
reboot is required to complete the installation. This error is likely caused by a
component in use, such as a running enclave or a vsock-proxy process. To complete
the installation, shut down all applications running on the instance and reboot
it.

## Install Nitro CLI

To use the Nitro Enclaves on your parent instance, you must install the **AWSNitroEnclavesWindows** package using AWS Systems Manager
Distributor.

Before you can install a package using the AWS Systems Manager Distributor, you must first
[complete
the Distributor prerequisites](../../../systems-manager/latest/userguide/distributor-prerequisites.md "../../../systems-manager/latest/userguide/distributor-prerequisites.md").

After you have completed the prerequisites, install the **AWSNitroEnclavesWindows** package. For more information, see one of
the following in the _AWS Systems Manager User Guide_:

- [Installing or updating a package one time using the
  console](../../../systems-manager/latest/userguide/distributor-working-with-packages-deploy.md#distributor-deploy-pkg-console "../../../systems-manager/latest/userguide/distributor-working-with-packages-deploy.md#distributor-deploy-pkg-console")
- [Installing a package one time using the AWS CLI](../../../systems-manager/latest/userguide/distributor-working-with-packages-deploy.md#distributor-deploy-pkg-cli "../../../systems-manager/latest/userguide/distributor-working-with-packages-deploy.md#distributor-deploy-pkg-cli")

You must reload the path environment variable from the updated environment in any
PowerShell or command prompt already open on the instance. When you open a new
PowerShell or command prompt, Windows automatically updates the path variable.
