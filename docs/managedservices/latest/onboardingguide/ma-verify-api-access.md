# Verify API access

AMS uses the AWS API, with some AMS-specific operations that you can read about in the AMS API Reference.

AWS provides several SDKs that you can access at
[Tools for Amazon Web Services](https://aws.amazon.com/tools/ "https://aws.amazon.com/tools/"). If you don't want
to use an SDK, you can make direct API calls. For information on authentication, see
[Signing AWS API Requests.](../../../general/latest/gr/signing_aws_api_requests.md "../../../general/latest/gr/signing_aws_api_requests.md")
If you are not using an SDK, or making direct HTTP API requests, you can use the AMS CLIs for Change Management
(CM) and SKMS.

Install the AMS CLIs

The AWS CLI is a prerequisite for using the AMS CLIs (Change Management and SKMS).

1. To install the AWS CLI, see
   [Installing the AWS Command Line Interface](../../../cli/latest/userguide/cli-chap-install.md "../../../cli/latest/userguide/cli-chap-install.md"), and follow the
   appropriate instructions. Note that at the bottom of that page there are instructions for using different installers,
   [Linux](../../../cli/latest/userguide/install-linux.md "../../../cli/latest/userguide/install-linux.md"), [MS
   Windows](../../../cli/latest/userguide/install-windows.md "../../../cli/latest/userguide/install-windows.md"), [macOS](../../../cli/latest/userguide/install-bundle.md "../../../cli/latest/userguide/install-bundle.md"),
   [Virtual Environment](../../../cli/latest/userguide/awscli-%20install-virtualenv.md "../../../cli/latest/userguide/awscli-%20install-virtualenv.md"),
   [Bundled Installer](../../../cli/latest/userguide/install-bundle.md "../../../cli/latest/userguide/install-bundle.md") (Linux, macOS, or Unix).
2. After the installation, run aws help to verify the installation.
3. Once the AWS CLI is installed, to install or upgrade the AMS CLI, download the AMS distributables zip file and unzip. You can access the AMS CLI distributables through the
   **Documentation** link in the left nav of the AMS console, or ask your cloud service delivery manager (CSDM) to send you the zip file.
4. Open either the **Managed Cloud Distributables -> CLI -> Windows** or the
   **Managed Cloud Distributables -> CLI -> Linux / MacOS** directory, depending on your operating system, and:
5. For **Windows**, execute the appropriate installer (this method only works on Windows 32 or 64 bits systems):
   - 32 Bits: ManagedCloudAPI_x86.msi
   - 64 Bits: ManagedCloudAPI_x64.msi

6. For **Mac/Linux**, execute the file named: **MC_CLI.sh** by running
   this command: sh MC_CLI.sh. Note that the **amscm** and **amsskms** directories and their
   contents must be in the same directory as the **MC_CLI.sh** file.
7. If your corporate credentials are used via federation with AWS (the AMS default configuration) you must install a credential
   management tool that can access your federation service. For example, you can use this AWS Security Blog
   [How
   to Implement Federated API and CLI Access Using SAML 2.0 and AD FS](https://aws.amazon.com/blogs/security/how-to-implement-federated-api-and-cli-access-using-saml-2-0-and-ad-fs/ "https://aws.amazon.com/blogs/security/how-to-implement-federated-api-and-cli-access-using-saml-2-0-and-ad-fs/") for help configuring your credential management tooling.
8. After the installation, run `aws amscm help` and `aws amsskms help` to see commands and options.
