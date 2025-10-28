# Deploy AWS Control Tower Account Factory for Terraform (AFT)

This section is for administrators of AWS Control Tower environments who wish to set up Account Factory
for Terraform (AFT) in their existing environment. It describes how to set up an Account Factory
for Terraform (AFT) environment with a new, dedicated AFT management account.

###### Note

A Terraform module deploys AFT. This module is available in the [AFT repository](https://github.com/aws-ia/terraform-aws-control_tower_account_factory/tree/main "https://github.com/aws-ia/terraform-aws-control_tower_account_factory/tree/main") on GitHub, and the entire AFT repository is considered the
module.

We recommend that you refer to the AFT modules on GitHub instead of cloning the AFT
repository. This way you can control and consume updates to the modules as they are
available.

For details about the latest releases of the AWS Control Tower Account Factory for Terraform (AFT) functionality, see [the Releases file](https://github.com/aws-ia/terraform-aws-control_tower_account_factory/releases "https://github.com/aws-ia/terraform-aws-control_tower_account_factory/releases") for this GitHub repository.

**Deployment prerequisites**

Before you configure and launch your AFT environment, you must have the following resources available:

- A home Region for your AWS Control Tower landing zone. For more information, see [How
  AWS Regions work with AWS Control Tower](region-how.md "region-how.md").
- An AWS Control Tower landing zone. For more information, see [Plan your
  AWS Control Tower landing zone](planning-your-deployment.md "planning-your-deployment.md").
- An AFT management account, which you can provision in AWS Control Tower, or provision by other means and enroll into AWS Control Tower.
- A Terraform version and distribution. For more information, see [Terraform and AFT versions](version-supported.md "version-supported.md").
- A VCS provider for tracking and managing changes to code and other files. By
  default, AFT uses AWS CodeCommit. For more information, see [What is AWS CodeCommit?](../../../codecommit/latest/userguide/welcome.md "../../../codecommit/latest/userguide/welcome.md") in the
  _AWS CodeCommit User Guide_.

If you're deploying AFT for the first time and you don't have an existing CodeCommit
repository, you must choose an external VCS provider, such as GitHub or BitBucket.
For more information, see [Alternatives for
version control of source code in AFT](aft-alternative-vcs.md "aft-alternative-vcs.md").

- A runtime environment where you can run the Terraform module that installs AFT.
- AFT feature options. For more information, see [Enable feature
  options](aft-feature-options.md "aft-feature-options.md").

## Configure and launch your AWS Control Tower Account Factory

for Terraform

The following steps assume that you're familiar with the Terraform workflow. You can
also learn more about deploying AFT by following the [Introduction to AFT](https://catalog.workshops.aws/control-tower/en-US/customization/aft "https://catalog.workshops.aws/control-tower/en-US/customization/aft") lab on the AWS Workshop Studio website.

**Step 1: Launch your AWS Control Tower landing zone**

Complete the steps in [Getting
started with AWS Control Tower](https://catalog.workshops.aws/control-tower/en-US/customization/aft "https://catalog.workshops.aws/control-tower/en-US/customization/aft"). This is where you create the AWS Control Tower
management account and set up your AWS Control Tower landing zone.

###### Note

Make sure to create a role for the AWS Control Tower management account that has
**AdministratorAccess** credentials. For more information, see
the following:

- [IAM
  Identities (users, user groups, and roles)](../../../IAM/latest/UserGuide/id.md "../../../IAM/latest/UserGuide/id.md") in the _AWS Identity and Access Management User Guide_
- [AdministratorAccess](../../../aws-managed-policy/latest/reference/AdministratorAccess.md "../../../aws-managed-policy/latest/reference/AdministratorAccess.md") in the _AWS
  Managed Policy Reference Guide_

**Step 2: Create a new organizational unit for AFT
(strongly recommended)**

We recommend that you create a separate OU in your AWS Control Tower landing zone . This OU is where
you provision the AFT management account. Create the new OU and the AFT management account from your AWS Control Tower
management account. For more information, see [Create a new OU](create-new-ou.md "create-new-ou.md").

**Step 3: Provision the AFT management account**

AFT requires that you provision an AWS account dedicated to AFT management
operations. Create the AFT management account when you are signed into the AWS Control Tower management account that is associated to your AWS Control Tower
landing zone. You can provision the AFT management account from the AWS Control Tower console by selecting **Create account** on the **Organization** page, or by other means. For more information, see [Provision accounts with AWS Service Catalog Account Factory](provision-as-end-user.md "provision-as-end-user.md").

###### Note

If you created a separate OU for AFT, make sure to select this OU when you create
the AFT management account.

It can take up to 30 minutes to fully provision the AFT management account.

**Step 4: Verify that the Terraform environment is available for
deployment**

This step assumes that you have experience with Terraform and have procedures in
place for executing Terraform. For more information, see [Command:
init](https://developer.hashicorp.com/terraform/cli/commands/init "https://developer.hashicorp.com/terraform/cli/commands/init") on the HashiCorp Developer website.

###### Note

AFT supports Terraform Version `1.6.0` or later.

**Step 5: Optional configurations**

- **Optionally set the virtual private cloud (VPC)
  configuration**

The AFT module includes a `aft_enable_vpc` parameter, which
specifies whether AWS Control Tower provisions account resources within a VPC in the
central AFT management account. By default, the parameter is set to
`true`. If you set this parameter to `false`, AWS Control Tower
deploys AFT _without_ the use of a VPC and private networking
resources, such as NAT Gateways or VPC endpoints. Disabling
`aft_enable_vpc` may help reduce the operating cost of AFT
_for some usage patterns_. Adding any VPC configurations
overrides the `aft_enable_vpc` parameter being set to
`false`.

###### Note

Re-enabling the `aft_enable_vpc` parameter (switching the value
from `false` to `true`) may require you to run the
`terraform apply` command twice in succession.

Instead of provisioning a new VPC, you can configure AFT to use an existing
VPC in your account. To use your own VPC, provide the following VPC
configuration parameters:

    + `aft_customer_vpc_id` - The ID of your existing VPC
    + `aft_customer_private_subnets` - A list of private subnet
     IDs in your VPC

Example configuration:

```

module "aft" {
  source = "github.com/aws-ia/terraform-aws-control_tower_account_factory"

  # VPC configuration
  aft_customer_vpc_id = "vpc-0123456789abcdef0"
  aft_customer_private_subnets = ["subnet-0123456789abcdef0", "subnet-0123456789abcdef1"]

  # Other AFT parameters...
}

```

###### Important

We don't recommend that you use the custom VPC option if you have an
existing AFT deployment. You may have dependencies on Lambda functions or
CodePipeline that depend on resources within the underlying existing
VPC.

- **Optionally configure the Terraform project
  name**

You can customize the Terraform project name used by AFT by setting the
`terraform_project_name` parameter. By default, AFT puts the
deployment in the "default" project in Terraform Cloud or Terraform
Enterprise.

Example configuration:

```

module "aft" {
  source = "github.com/aws-ia/terraform-aws-control_tower_account_factory"

  # Project name configuration
  terraform_project_name = "my-organization-aft"

  # Other AFT parameters...
}

```

###### Note

This parameter is only applicable to Terraform Enterprise or Terraform
Cloud deployments.

- **Optionally apply custom tags to AFT
  resources**

You can apply custom tags to all AFT resources by using the `tags`
parameter. These tags help with resource organization, cost allocation, and
access control.

Example configuration:

```

module "aft" {
  source = "github.com/aws-ia/terraform-aws-control_tower_account_factory"

  # Custom tags configuration
  tags = {
    Environment = "Production"
    CostCenter = "IT-12345"
    Project = "AFT-Deployment"
    Owner = "platform-team@example.com"
  }

  # Other AFT parameters...
}

```

These tags are applied to all resources created by the AFT module. AFT
automatically adds a `managed_by = "AFT"` tag to all resources, which
can't be overridden by custom tags.

###### Note

Custom tags can be added at any time, not just during initial
deployment.

- **Optionally apply an AWS KMS customer-managed encryption key (CMK) to CloudWatch log
  groups and SNS topics**

To enable KMS CMK encryption for log groups and SNS topics, set the
`cloudwatch_log_group_enable_cmk_encryption` and
`sns_topic_enable_cmk_encryption` variables.

If you opt into these settings, AFT uses the existing CMK,
_alias/aft_, to encrypt CloudWatch logs and SNS topics. This CMK
is created when AFT is deployed in the AFT management account, and it can be applied to log groups and SNS topics.

    + If the variable `cloudwatch_log_group_enable_cmk_encryption` is set
     to **true**, the CloudWatch log groups for AFT are encrypted using
     the CMK. If the variable is set to **false**, which is the
     default value, the logs are encrypted using [server side encryption with the CloudWatch logs default](../../../AmazonCloudWatch/latest/logs/encrypt-log-data-kms.md "../../../AmazonCloudWatch/latest/logs/encrypt-log-data-kms.md").
    + If the variable `sns_topic_enable_cmk_encryption` is set to
     **true**, notifications sent to the AFT SNS topics
     (*aft-notifications* and
     *aft-failure-notifications*) are encrypted using the CMK.
     If the variable is set to **false**, which is the default
     value, the SNS messages are encrypted with the AWS-managed key:
     *alias/aws/sns*. For more information, see [SSE key terms](../../../sns/latest/dg/sns-server-side-encryption.md#sse-key-terms "../../../sns/latest/dg/sns-server-side-encryption.md#sse-key-terms").

- **Optionally change your CodeBuild compute
  type**

During deployment, to change the compute type that AFT uses for CodeBuild, set the variable
`aft_codebuild_compute_type`.

For information about accepted compute types, see [About on-demand environment types](../../../codebuild/latest/userguide/build-env-ref-compute-types.md#environment.types "../../../codebuild/latest/userguide/build-env-ref-compute-types.md#environment.types"). The default compute type is
`BUILD_GENERAL1_MEDIUM`.

**Step 6: Call the Account Factory for Terraform module to deploy
AFT**

Call the AFT module with the role that you created for the AWS Control Tower management account
that has **AdministratorAccess** credentials. AWS Control Tower provisions a
Terraform module through the AWS Control Tower management account, which establishes all of the
infrastructure required to orchestrate AWS Control Tower Account Factory requests.

You can view the AFT module in the [AFT repository](https://github.com/aws-ia/terraform-aws-control_tower_account_factory/tree/main "https://github.com/aws-ia/terraform-aws-control_tower_account_factory/tree/main") on GitHub. The entire GitHub repository is considered the
AFT module. Refer to the [README file](https://github.com/aws-ia/terraform-aws-control_tower_account_factory/blob/main/README.md "https://github.com/aws-ia/terraform-aws-control_tower_account_factory/blob/main/README.md") for information about the inputs that are required to run the
AFT module and deploy AFT. Alternatively, you can view the AFT module in the [Terraform Registry](https://registry.terraform.io/modules/aws-ia/control_tower_account_factory/aws/latest "https://registry.terraform.io/modules/aws-ia/control_tower_account_factory/aws/latest").

If you have pipelines in your environment that are established for managing
Terraform, you can integrate the AFT module into your existing workflow. Otherwise, run
the AFT module from any environment that's authenticated with the required credentials.

Timeout causes deployment to fail. We recommend using AWS Security Token Service (STS) credentials to
ensure you have a timeout that's sufficient for a full deployment. The minimum timeout
for AWS STS credentials is 60 minutes. For more information, see [Temporary
security credentials in IAM](../../../IAM/latest/UserGuide/id_credentials_temp.md "../../../IAM/latest/UserGuide/id_credentials_temp.md") in the _AWS Identity and Access Management User
Guide_.

###### Note

You might wait up to 30 minutes for AFT to finish deploying through the Terraform
module.

**Step 7: Manage the Terraform state file**

A Terraform state file is generated when you deploy AFT. This artifact describes the
state of the resources that Terraform created. If you plan to update the AFT version,
make sure to preseve the Terraform state file, or set up a Terraform backend using Amazon S3
and DynamoDB. The AFT module doesn't manage a backend Terraform state.

###### Note

You're responsible for protecting the Terraform state file. Some input variables
might contain sensitive values, such as a private `ssh` key or Terraform
token. Depending on your deployment method, these values can be viewable as plain
text in the Terraform state file. For more information, see [Sensitive
data in State](https://www.terraform.io/docs/language/state/sensitive-data.html "https://www.terraform.io/docs/language/state/sensitive-data.html") on the HashiCorp website.
