

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Verify API access
<a name="ma-verify-api-access"></a>

AMS uses the AWS API, with some AMS-specific operations that you can read about in the AMS API Reference.

AWS provides several SDKs that you can access at [Tools for Amazon Web Services](https://aws.amazon.com/tools/). If you don't want to use an SDK, you can make direct API calls. For information on authentication, see [Signing AWS API Requests.](https://docs.aws.amazon.com/general/latest/gr/signing_aws_api_requests.html) If you are not using an SDK, or making direct HTTP API requests, you can use the AMS CLIs for Change Management (CM) and SKMS.

Install the AMS CLIs

The AWS CLI is a prerequisite for using the AMS CLIs (Change Management and SKMS).

1. To install the AWS CLI, see [Installing the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html), and follow the appropriate instructions. Note that at the bottom of that page there are instructions for using different installers, [Linux](https://docs.aws.amazon.com/cli/latest/userguide/install-linux.html), [MS Windows](https://docs.aws.amazon.com/cli/latest/userguide/install-windows.html), [macOS](https://docs.aws.amazon.com/cli/latest/userguide/install-bundle.html), [Virtual Environment](https://docs.aws.amazon.com/cli/latest/userguide/awscli-%20install-virtualenv.html), [Bundled Installer](https://docs.aws.amazon.com/cli/latest/userguide/install-bundle.html) (Linux, macOS, or Unix). 

1. After the installation, run aws help to verify the installation.

1. Once the AWS CLI is installed, to install or upgrade the AMS CLI, download the AMS distributables zip file and unzip. You can access the AMS CLI distributables through the **Documentation** link in the left nav of the AMS console, or ask your cloud service delivery manager (CSDM) to send you the zip file. 

1. Open either the **Managed Cloud Distributables -> CLI -> Windows** or the **Managed Cloud Distributables -> CLI -> Linux / MacOS** directory, depending on your operating system, and:

1. For **Windows**, execute the appropriate installer (this method only works on Windows 32 or 64 bits systems):
   + 32 Bits: ManagedCloudAPI\_x86.msi
   + 64 Bits: ManagedCloudAPI\_x64.msi

1. For **Mac/Linux**, execute the file named: **MC\_CLI.sh** by running this command: sh MC\_CLI.sh. Note that the **amscm** and **amsskms** directories and their contents must be in the same directory as the **MC\_CLI.sh** file.

1. If your corporate credentials are used via federation with AWS (the AMS default configuration) you must install a credential management tool that can access your federation service. For example, you can use this AWS Security Blog [How to Implement Federated API and CLI Access Using SAML 2.0 and AD FS](https://aws.amazon.com/blogs/security/how-to-implement-federated-api-and-cli-access-using-saml-2-0-and-ad-fs/) for help configuring your credential management tooling.

1. After the installation, run `aws amscm help` and `aws amsskms help` to see commands and options. 