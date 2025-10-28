# Automate customizations outside the AWS Control Tower

console

Some customizations are not available through the AWS Control Tower console, but they can be
implemented in other ways. For example:

- You can customize accounts during provisioning, in a GitOps-style workflow,
  with [Account
  Factory for Terraform (AFT)](taf-account-provisioning.md "taf-account-provisioning.md").

AFT is deployed with a Terraform module, available in the [AFT repository](https://github.com/aws-ia/terraform-aws-control_tower_account_factory/tree/main "https://github.com/aws-ia/terraform-aws-control_tower_account_factory/tree/main").

- You can customize your AWS Control Tower landing zone with [Customizations for
  AWS Control Tower](cfct-overview.md "cfct-overview.md") (CfCT), a package of functionality that is
  built upon AWS CloudFormation templates and service control policies (SCPs). You can
  deploy the custom templates and policies to individual accounts and
  organizational units (OUs) within your organization.

Source code for CfCT is available in a [GitHub repository](https://github.com/aws-solutions/aws-control-tower-customizations "https://github.com/aws-solutions/aws-control-tower-customizations").

- You can customize your AWS Control Tower landing zone with Landing Zone Accelerator
  (LZA) on AWS. The LZA solution is architected to align with AWS best
  practices and conform to multiple global compliance frameworks. We recommend
  that you deploy AWS Control Tower as the foundational landing zone, and then enhance the
  landing zone capabilities with LZA, as needed. For more information, see [AWS Control Tower and Landing zone accelerator](about-lza.md "about-lza.md").
