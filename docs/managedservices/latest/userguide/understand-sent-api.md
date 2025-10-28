# Using the AMS API and CLI

The AWS Managed Services (AMS) API is similar to the APIs for other AWS services. You can read about
the AMS API in the [AMS API Reference](../ApiReference-cm/index.md "../ApiReference-cm/index.md").

## AMS API HTTP endpoints for REST calls

Besides the various SDKs, AMS provides a CLI; you can also invoke REST API calls against the AMS endpoint.

There are two AMS APIs (the endpoint for both resides in us-east-1):

- Change Management: Use this API to request access to or changes to your infrastructure, including creating and updating RFCs, deploying new instances,
  updating and deleting instances, getting information on CTs, and creating AMIs. The HTTP endpoint is:

`https://amscm.us-east-1.amazonaws.com`

- SKMS: Use this API to get information about your infrastructure, including VPCs, stacks, subnets, and AMIs. The HTTP endpoint is:

`https://amsskms.us-east-1.amazonaws.com`

## Installing or upgrading the AMS CLI

The AMS CLI is an easy way to interact with the AMS API and is used in the examples in this section. For usage conventions for the AWS CLI and AMS
CLI, see [Using the AWS command Line Interface](../../../cli/latest/userguide/cli-chap-using.md "../../../cli/latest/userguide/cli-chap-using.md").

For information on installing SAML, see
[AD FS claim rule and SAML settings](adfs-claim-rule-saml.md "adfs-claim-rule-saml.md").

To install or upgrade the AMS CLI, follow these instructions:

###### Note

You must have administrator credentials for this procedure.

The AWS CLI is a prerequisite for using the AWS Managed Services (AMS) CLIs (Change Management and SKMS).

1. To install the AWS CLI, see [Installing the AWS Command Line Interface](../../../cli/latest/userguide/installing.md "../../../cli/latest/userguide/installing.md"),
   and follow the appropriate instructions. Note that at the bottom of that page there are instructions for using different installers,
   [Linux](../../../cli/latest/userguide/awscli-install-linux.md "../../../cli/latest/userguide/awscli-install-linux.md"),
   [MS Windows](../../../cli/latest/userguide/awscli-install-windows.md "../../../cli/latest/userguide/awscli-install-windows.md"),
   [macOS](../../../cli/latest/userguide/cli-install-macos.md "../../../cli/latest/userguide/cli-install-macos.md"),
   [Virtual Environment](../../../cli/latest/userguide/awscli-install-virtualenv.md "../../../cli/latest/userguide/awscli-install-virtualenv.md"),
   [Bundled Installer (Linux, macOS, or Unix)](../../../cli/latest/userguide/awscli-install-bundle.md "../../../cli/latest/userguide/awscli-install-bundle.md").

After the installation, run `aws help` to verify the installation. 2. Once the AWS CLI is installed, to install or upgrade the AMS CLI, download either the AMS
**AMS CLI** or **AMS SDK** distributables zip file and unzip.
You can access the AMS CLI distributables through the
[**Developer's Resources**](https://console.aws.amazon.com/managedservices/developerResources "https://console.aws.amazon.com/managedservices/developerResources") link in the left nav
of the AMS console. 3. The README file provides instructions for any install.

Open either:

    * CLI zip: Provides the AMS CLI only.
    * SDK zip: Provides all of the AMS APIs and the AMS CLI.

For **Windows**, run the appropriate installer (only 32 or 64 bits systems):

    * 32 Bits: **ManagedCloudAPI\_x86.msi**
    * 64 Bits: **ManagedCloudAPI\_x64.msi**

For **Mac/Linux**, run the file named: **AWSManagedServices_InstallCLI.sh**
by running this command: `sh AWSManagedServices_InstallCLI.sh`.
Note that the **amscm** and **amsskms** directories and their contents
must be in the same directory as the **AWSManagedServices_InstallCLI.sh** file. 4. If your corporate credentials are used through federation with AWS (the AMS default configuration) you must install a credential
management tool that can access your federation service. For example, you can use this AWS Security Blog
[How to Implement Federated API and CLI Access Using SAML 2.0 and AD FS](https://blogs.aws.amazon.com/security/post/Tx1LDN0UBGJJ26Q/How-to-Implement-Federated-API-and-CLI-Access-Using-SAML-2-0-and-AD-FS "https://blogs.aws.amazon.com/security/post/Tx1LDN0UBGJJ26Q/How-to-Implement-Federated-API-and-CLI-Access-Using-SAML-2-0-and-AD-FS") for help configuring your credential management tooling. 5. After the installation, run `aws amscm help` and `aws amsskms help` to see commands and options.

###### Note

The AMS CLI must be installed for these commands to work. To install the AMS API or CLI, go to the AMS console **Developers Resources**
page. For reference material on the AMS CM API or AMS SKMS API, see the AMS Information Resources section in the User Guide. You may need to add a `--profile` option for
authentication; for example, `aws amsskms `ams-cli-command` --profile SAML`. You may also need to add the `--region` option as all AMS
commands run out of us-east-1; for example `aws amscm `ams-cli-command` --region=us-east-1`.
