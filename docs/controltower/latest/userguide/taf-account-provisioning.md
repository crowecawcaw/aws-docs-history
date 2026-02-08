# Provision accounts with AWS Control Tower Account Factory

for Terraform (AFT)

AWS Control Tower Account Factory for Terraform (AFT) adopts a GitOps model that automates the
process of account provisioning and updating in AWS Control Tower.

With AFT, you create an account request Terraform file, which contains the input that
invokes the AFT workflow. After account provisioning and updating finishes, the AFT workflow
continues by running the AFT account provisioning framework and account customizations
steps.

AFT doesn't impact workflow performance in AWS Control Tower. If you provision an account
through AFT or Account Factory, the same backend workflow occurs.

## Prerequisites

###### Note

AFT account provision must target an organizational unit (OU) with AWSControlTowerBaseline enabled
in AWS Control Tower. For details of AWSControlTowerBaseline, see: [Baseline types that apply at the OU level](types-of-baselines.md#ou-baseline-types "types-of-baselines.md#ou-baseline-types").

When you're getting started with AFT, you will create the following:

- In AWS Control Tower create the OU, and then the AFT management account, for your AFT environment. Make note of the
  account ID, so you can enter it in the `main.tf` file later, when you deploy
  AFT with the Terraform module. You can view this account ID on the AWS Control Tower **Control
  details** page. For more information, see the [Terraform documentation](https://developer.hashicorp.com/terraform/tutorials/aws/aws-control-tower-aft "https://developer.hashicorp.com/terraform/tutorials/aws/aws-control-tower-aft").
- One or more `git` repositories for your fully deployed AFT
  environment. For more information, see [Post-deployment
  steps for AFT](aft-post-deployment.md "aft-post-deployment.md").
- A fully deployed AFT environment. For more information, see [Overview of AWS Control Tower Account Factory for Terraform (AFT)](aft-overview.md "aft-overview.md") and [Deploy AWS Control Tower
  Account Factory for Terraform (AFT).](aft-getting-started.md "aft-getting-started.md") Also see the [Terraform documentation](https://developer.hashicorp.com/terraform/tutorials/aws/aws-control-tower-aft "https://developer.hashicorp.com/terraform/tutorials/aws/aws-control-tower-aft").

###### Tip

You can create the AFT management account from the AWS Control Tower console with **Create account**. For more information, see [Methods of provisioning](methods-of-provisioning.md "methods-of-provisioning.md").

Also, optionally, you can create an account template folder to help define your additional accounts, in the **aft-account-customizations** repository.

For accounts enrolled via Auto Enroll:

- New account creation through AFT continues to work normally.
- Existing account import requires additional steps:
  - Register OU to create the necessary provisioned products before importing.
  - Register OU will emit `CreateManagedAccount` and `UpdateManagedAccount` events, enabling AFT customizations.

For information about AWS Regions where AFT has deployment limitations, see [Limitations and quotas in AWS Control Tower](limits.md "limits.md") and [Control limitations](control-limitations.md "control-limitations.md").

The [Terraform documentation](https://developer.hashicorp.com/terraform/tutorials/aws/aws-control-tower-aft "https://developer.hashicorp.com/terraform/tutorials/aws/aws-control-tower-aft") contains a good overview of how to set up AWS Control Tower Account Factory for Terraform (AFT).
