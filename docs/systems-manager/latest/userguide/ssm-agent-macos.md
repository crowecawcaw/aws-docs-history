# Working with SSM Agent on EC2 instances for

macOS

AWS Systems Manager (SSM Agent) processes Systems Manager requests and configures your machine as specified
in the request. Use the following procedures to install, configure, or uninstall
SSM Agent for macOS.

###### Note

SSM Agent is preinstalled, by default, on Amazon Machine Images (AMIs) for macOS. You
don't need to install SSM Agent on an Amazon Elastic Compute Cloud (Amazon EC2) instance for macOS unless
you have uninstalled it.

The source code for SSM Agent is available on [GitHub](https://github.com/aws/amazon-ssm-agent "https://github.com/aws/amazon-ssm-agent") so that you can
adapt the agent to meet your needs. We encourage you to submit [pull
requests](https://github.com/aws/amazon-ssm-agent/blob/mainline/CONTRIBUTING.md "https://github.com/aws/amazon-ssm-agent/blob/mainline/CONTRIBUTING.md") for changes that you would like to have included. However, AWS
doesn't provide support for running modified copies of this software.

###### Note

To view details about the different versions of SSM Agent, see the [release
notes](https://github.com/aws/amazon-ssm-agent/blob/mainline/RELEASENOTES.md "https://github.com/aws/amazon-ssm-agent/blob/mainline/RELEASENOTES.md").

Before you manually install SSM Agent on a macOS operating system, review the
following information.

- SSM Agent is installed by default on the EC2 instances and Amazon Machine Images
  supported by Systems Manager. For more information, see the [list of supported operating systems for macOS](operating-systems-and-machine-types.md#prereqs-os-mac "operating-systems-and-machine-types.md#prereqs-os-mac").

SSM Agent doesn't need to be manually installed on macOS EC2 instances unless
it has been uninstalled.

- EC2 instances for macOS are not supported in all AWS Regions. For lists of
  Regions where x86-based and M1 EC2 instances for macOS are supported, see
  [macOS
  workloads](https://aws.amazon.com/ec2/faqs/#macos_workloads "https://aws.amazon.com/ec2/faqs/#macos_workloads") in the Amazon EC2 FAQs.
- An updated version of SSM Agent is released whenever new tools are added to Systems Manager or
  updates are made to existing tools. Failing to use the latest version of the agent can
  prevent your managed node from using various Systems Manager tools and features. For that reason, we
  recommend that you automate the process of keeping SSM Agent up to date on your machines. For
  information, see [Automating updates to SSM Agent](ssm-agent-automatic-updates.md "ssm-agent-automatic-updates.md"). Subscribe to the [SSM Agent
  Release Notes](https://github.com/aws/amazon-ssm-agent/blob/mainline/RELEASENOTES.md "https://github.com/aws/amazon-ssm-agent/blob/mainline/RELEASENOTES.md") page on GitHub to get notifications about SSM Agent
  updates.

###### Topics

- [Manually installing and
  uninstalling SSM Agent on EC2 instances for macOS](manually-install-ssm-agent-macos.md "manually-install-ssm-agent-macos.md")
