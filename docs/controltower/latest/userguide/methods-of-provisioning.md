# Provision accounts within AWS Control Tower

AWS Control Tower provides several methods for creating and updating member accounts. Some
methods are primarily console-based, and some methods are primarily automated.

**Overview**

One standard way to create member accounts in AWS Control Tower is through Account Factory, a console-based
product that's part of the Service Catalog. Also, from the AWS Control Tower console, you
can use **Create account** as a method to provision new accounts, as well as **Enroll account** to enroll existing AWS
accounts into AWS Control Tower, if your landing zone is not in a state of drift.

With Account Factory, you can provision basic accounts, relying on the AWS Control Tower default
settings. You also can provision _customized_ accounts that meet requirements for
specialized use cases.

[Account Factory Customization (AFC)](af-customization-page.md "af-customization-page.md") is a way of provisioning customized accounts from the
AWS Control Tower console, and it automates the customization and deployment of your accounts. It
allows console-based, automated provisioning, after some one-time setup steps, which
eliminates the need to write scripts or set up pipelines. For more information, see
[Customize accounts with Account Factory
Customization (AFC)](af-customization-page.md "af-customization-page.md").

###### Automatic enrollment

You also can create AWS accounts _outside_ AWS Control Tower and move
them into an OU that's registered with AWS Control Tower, without creating inheritance drift,
if you opt into the **Automated account
enrollment** feature of your landing zone **Settings**. For
more information, see [Move and enroll accounts with auto-enrollment](account-auto-enrollment.md "account-auto-enrollment.md").

###### Console-based methods:

- Through the Account Factory console that is part of AWS Service Catalog, for basic or
  customized accounts. Review [Provision and manage accounts with Account Factory](account-factory.md "account-factory.md") for details and instructions.
- Through automated enrollment, by moving an account into an OU from the console. See [Move and enroll accounts with auto-enrollment](account-auto-enrollment.md "account-auto-enrollment.md")
- Through the **Enroll account** feature within AWS Control Tower, if
  your landing zone is not in a state of drift. See [Enroll an existing account from the AWS Control Tower console](quick-account-provisioning.md "quick-account-provisioning.md").
- In the AWS Control Tower console, you can use Account Factory to create, update, or enroll
  up to five accounts at the same time.

###### Automated methods:

- **Lambda code:** From your AWS Control Tower landing
  zone's management account, using Lambda code and appropriate IAM roles. See
  [Automated Account Provisioning with IAM Roles](roles-how.md#stacksets-and-roles "roles-how.md#stacksets-and-roles").
- **Terraform:** From the AWS Control Tower Account Factory
  for Terraform (AFT), which relies on Account Factory and a GitOps model to allow
  automation of account provisioning and updating. See [Provision accounts with AWS Control Tower Account Factory
  for Terraform (AFT)](taf-account-provisioning.md "taf-account-provisioning.md") .
- Through automated enrollment, by moving an existing account into an OU using APIs. See [Move and enroll accounts with auto-enrollment](account-auto-enrollment.md "account-auto-enrollment.md")
- **Account Factory customization in the AWS Control Tower
  console:** After the setup steps, future provisioning of customized
  accounts requires no additional configuration or pipeline maintenance. Accounts
  are provisioned by means of a AWS Service Catalog product called a _blueprint_. A blueprint can use CloudFormation templates, or Terraform
  templates.

###### Note

CloudFormation blueprints can deploy resources to multiple Regions. Terraform
blueprints can deploy resources to a single Region only. By default, that is
the home Region.
