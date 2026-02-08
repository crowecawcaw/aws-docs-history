# Customize your AWS Control Tower landing zone

Certain aspects of your AWS Control Tower landing zone are configurable in the console, such as
selection of Regions and optional controls. Other changes may be made outside the
console, with automation.

For example, you can create more extensive customizations of your landing zone with
the _Customizations for AWS Control Tower_ capability, a
GitOps-style customization framework that works with AWS CloudFormation templates and AWS Control Tower
lifecycle events.

## Benefits of Customizations for AWS Control Tower

(CfCT)

The package of functionality that we refer to as _Customizations for AWS Control Tower_ (CfCT) helps you create more extensive
customizations for your landing zone than you can create in the AWS Control Tower console. It
offers a GitOps-style, automated process. You can reshape your landing zone to meet your
business requirements.

This _infrastructure-as-code_ customization process
integrates AWS CloudFormation templates with AWS service control policies (SCPs) and AWS Control Tower
[lifecycle events](lifecycle-events.md "lifecycle-events.md"), so that your resource
deployments remain synchronized with your landing zone. For example, when you create a
new account with Account Factory, the resources attached to the account and the OU can
be deployed automatically.

###### Note

Unlike Account Factory and AFT, CfCT is not specifically intended to create new
accounts, but to customize accounts and OUs in your landing zone by deploying
resources that you specify.

###### Note

The target organizational unit (OU) configured in CfCT must have AWSControlTowerBaseline enabled
in AWS Control Tower. For details of AWSControlTowerBaseline, see: [Baseline types that apply at the OU level](types-of-baselines.md#ou-baseline-types "types-of-baselines.md#ou-baseline-types").

###### Benefits

- **Expand a customized and secure AWS
  environment** – You can expand your multi-account AWS Control Tower
  environment more quickly, and incorporate AWS best practices into a repeatable
  customization workflow.
- **Instantiate your requirements** – You
  can customize your AWS Control Tower landing zone for your business requirements, with
  the AWS CloudFormation templates and service control policies that express your policy
  intentions.
- **Automate further with AWS Control Tower lifecycle
  events** – Lifecycle events allow you to deploy resources
  based on completion of a previous series of events. You can rely on a lifecycle
  event to help you deploy resources to accounts and OUs, automatically.
- **Extend your network architecture** – You
  can deploy customized network architectures that improve and protect your
  connectivity, such as a transit gateway.

## Additional CfCT examples

- An example networking use case with _Customizations for
  AWS Control Tower_ (CfCT) is given in the AWS Architecture blog post,
  [Deploy consistent DNS with Service Catalog and AWS Control Tower customizations](https://aws.amazon.com/blogs//architecture/deploy-consistent-dns-with-aws-service-catalog-and-aws-control-tower-customizations/ "https://aws.amazon.com/blogs//architecture/deploy-consistent-dns-with-aws-service-catalog-and-aws-control-tower-customizations/").
- A specific example [related to CfCT and Amazon GuardDuty](https://github.com/aws-samples/aws-security-reference-architecture-examples/tree/main/aws_sra_examples/solutions/guardduty/guardduty_org/customizations_for_aws_control_tower "https://github.com/aws-samples/aws-security-reference-architecture-examples/tree/main/aws_sra_examples/solutions/guardduty/guardduty_org/customizations_for_aws_control_tower") is available on GitHub in the [`aws-samples` repository](https://github.com/aws-samples/aws-security-reference-architecture-examples "https://github.com/aws-samples/aws-security-reference-architecture-examples").
- Additional code examples regarding CfCT are available as part of the AWS
  Security Reference Architecture, in the [`aws-samples` repository](https://github.com/aws-samples/aws-security-reference-architecture-examples "https://github.com/aws-samples/aws-security-reference-architecture-examples"). Many of these examples
  contain sample `manifest.yaml` files in a directory named
  `customizations_for_aws_control_tower`.

For more information about the AWS Security Reference Architecture, see the [AWS Prescriptive Guidance pages](../../../prescriptive-guidance/latest/security-reference-architecture/welcome.md "../../../prescriptive-guidance/latest/security-reference-architecture/welcome.md").
