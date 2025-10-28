# Related AWS services

AWS accounts work seamlessly with the following services:

- **IAM**

Your AWS account is closely integrated with AWS Identity and Access Management (IAM). You can use IAM
with your account to ensure that other people who work in your account have as much
access as they need to get their jobs done. You also use IAM to control access to
all of your AWS resources, not only account specific information. It's important
that you familiarize yourself with the major concepts and best practices of IAM
before you get too far along with setting up the structure of your AWS account.
For more information, see [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the
_IAM User Guide_.

- **AWS Organizations**

If your company is large or likely to grow, you might want to set up multiple
AWS accounts that reflect your company's specific structure. AWS Organizations provides the
underlying infrastructure and capabilities for you to build and manage your
multi-account environments. You can combine your existing accounts into an
organization that enables you to manage the accounts centrally. You can create
accounts that automatically are a part of your organization, and you can invite
other accounts to join your organization. You also can attach policies that affect
some or all of your accounts. For more information, see [When to use AWS Organizations](using-orgs.md "using-orgs.md").

- **AWS Control Tower**

AWS Control Tower provides a simplified way to set up and govern a secure,
multi-account AWS environment. AWS Control Tower automates the creation of your
multi-account environment using AWS Organizations, instantiating a set of initial accounts
and with some default guardrails and configurations for the environment. You can use
AWS Control Tower to provision new AWS accounts in a few steps while ensuring that the
accounts conform to your organizational policies. For more information, see [When to use AWS Control Tower](when-to-use-control-tower.md "when-to-use-control-tower.md").
