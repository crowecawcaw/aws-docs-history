

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Install the AMS CLIs
<a name="install-cli"></a>

For an example of installing the AWS Managed Services (AMS) CLI to use with SAML, see [Appendix: ActiveDirectory Federation Services (ADFS) claim rule and SAML settings](apx-adfs-claim-rule-saml.md).

If you need temporary access, in order to get and install the AWS Managed Services (AMS) SDKs, see [Temporary AMS console access](https://docs.aws.amazon.com/managedservices/latest/userguide/access-console-temp.html). 
**Note**  
You must have administrator credentials for this procedure.

The AWS CLI is a prerequisite for using the AWS Managed Services (AMS) CLIs (Change Management and SKMS).

1. To install the AWS CLI, see [Installing the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/installing.html), and follow the appropriate instructions. Note that at the bottom of that page there are instructions for using different installers, [Linux](https://docs.aws.amazon.com/cli/latest/userguide/awscli-install-linux.html), [MS Windows](https://docs.aws.amazon.com/cli/latest/userguide/awscli-install-windows.html), [macOS](https://docs.aws.amazon.com/cli/latest/userguide/cli-install-macos.html), [Virtual Environment](https://docs.aws.amazon.com/cli/latest/userguide/awscli-install-virtualenv.html), [Bundled Installer (Linux, macOS, or Unix)](https://docs.aws.amazon.com/cli/latest/userguide/awscli-install-bundle.html).

   After the installation, run `aws help` to verify the installation.

1. Once the AWS CLI is installed, to install or upgrade the AMS CLI, download either the AMS **AMS CLI** or **AMS SDK** distributables zip file and unzip. You can access the AMS CLI distributables through the [**Developer's Resources**](https://console.aws.amazon.com/managedservices/developerResources) link in the left nav of the AMS console.

1. The README file provides instructions for any install.

   Open either:
   + CLI zip: Provides the AMS CLI only.
   + SDK zip: Provides all of the AMS APIs and the AMS CLI.

   For **Windows**, run the appropriate installer (only 32 or 64 bits systems):
   + 32 Bits: **ManagedCloudAPI\_x86.msi**
   + 64 Bits: **ManagedCloudAPI\_x64.msi**

   For **Mac/Linux**, run the file named: **AWSManagedServices\_InstallCLI.sh** by running this command: `sh AWSManagedServices_InstallCLI.sh`. Note that the **amscm** and **amsskms** directories and their contents must be in the same directory as the **AWSManagedServices\_InstallCLI.sh** file.

1. If your corporate credentials are used through federation with AWS (the AMS default configuration) you must install a credential management tool that can access your federation service. For example, you can use this AWS Security Blog [ How to Implement Federated API and CLI Access Using SAML 2.0 and AD FS](https://blogs.aws.amazon.com/security/post/Tx1LDN0UBGJJ26Q/How-to-Implement-Federated-API-and-CLI-Access-Using-SAML-2-0-and-AD-FS) for help configuring your credential management tooling.

1. After the installation, run `aws amscm help` and `aws amsskms help` to see commands and options.
**Note**  
The AMS CLI must be installed for these commands to work. To install the AMS API or CLI, go to the AMS console **Developers Resources** page. For reference material on the AMS CM API or AMS SKMS API, see the AMS Information Resources section in the User Guide. You may need to add a `--profile` option for authentication; for example, `aws amsskms {{ams-cli-command}} --profile SAML`. You may also need to add the `--region` option as all AMS commands run out of us-east-1; for example `aws amscm {{ams-cli-command}} --region=us-east-1`.