# Automate tasks in AWS Control Tower

Many customers prefer to automate tasks in AWS Control Tower, such as account provisioning,
control assignment, and auditing. You can set up these automated actions with calls to:

- [AWS Service Catalog APIs](../../../servicecatalog/latest/dg/service-catalog-api-overview.md "../../../servicecatalog/latest/dg/service-catalog-api-overview.md")
- [AWS Organizations APIs](../../../organizations/latest/APIReference/Welcome.md "../../../organizations/latest/APIReference/Welcome.md")
- [AWS Control Tower APIs](../APIReference/Welcome.md "../APIReference/Welcome.md")
- [the AWS CLI](../../../cli/latest/reference/servicecatalog/index.md "../../../cli/latest/reference/servicecatalog/index.md")
  The [Additional information and links](related-information.md "related-information.md") page
  contains links to many excellent technical blog posts that can help you automate tasks in
  AWS Control Tower. The sections that follow provide links to areas in this _AWS Control Tower User Guide_ that can assist you with automating tasks.

**Automating control tasks**

You can automate tasks related to applying and removing controls (also known as _guardrails_) through the AWS Control Tower API. For details, see the [AWS Control Tower API
Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

For more information about how to perform control operations with AWS Control Tower APIs, see the blog post [AWS Control Tower releases API, pre-defined controls to your organizational units](https://aws.amazon.com//blogs/mt/aws-control-tower-releases-api-pre-defined-controls-to-your-organizational-units/ "https://aws.amazon.com//blogs/mt/aws-control-tower-releases-api-pre-defined-controls-to-your-organizational-units/").

**Automating landing zone tasks**

The AWS Control Tower landing zone APIs help you automate certain tasks related to your landing zone. For details, see the [AWS Control Tower API
Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

**Automating OU registration**

The AWS Control Tower baseline APIs help you automate certain tasks, such as registering an OU. For details, see the [AWS Control Tower API
Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

**Automated account closure**

You can automate the closure of AWS Control Tower member accounts with an AWS Organizations API. For more information, see [Close an AWS Control Tower member account through
AWS Organizations](delete-account.md#close-account-with-orgs-api "delete-account.md#close-account-with-orgs-api").

**Automated account provisioning and updating**

_AWS Control Tower Account Factory Customization (AFC)_ helps you create accounts from the AWS Control Tower console, with customized CloudFormation templates that we refer to as blueprints. This process is automated in the sense that you can create new accounts and update accounts repeatedly, after setting up a single blueprint, without maintaining pipelines.

_AWS Control Tower Account Factory for Terraform_ (AFT) follows a GitOps model to automate
the processes of account provisioning and account updating in AWS Control Tower. For more
information, see [Provision accounts with AWS Control Tower Account Factory
for Terraform (AFT)](taf-account-provisioning.md "taf-account-provisioning.md") .

_Customizations for AWS Control Tower_ (CfCT) helps you customize
your AWS Control Tower landing zone and stay aligned with AWS best practices. Customizations are
implemented with AWS CloudFormation templates, service control policies (SCPs), and resource control policies (RCPs). For more
information, see [Customizations for AWS Control Tower (CfCT) overview](cfct-overview.md "cfct-overview.md") .

For more information and a video about automated account provisioning, see [Walkthrough: Automated account provisioning in AWS Control Tower](automated-provisioning-walkthrough.md "automated-provisioning-walkthrough.md") and [Automated
provisioning with IAM roles](roles-how.md#automated-provisioning "roles-how.md#automated-provisioning").

Also see [Update accounts by script](configuration-updates.md#update-accounts-by-script "configuration-updates.md#update-accounts-by-script").

**Programmatic auditing of accounts**

For more information about auditing accounts programmatically, see [Programmatic
roles and trust relationships for the AWS Control Tower audit account](roles-how.md#stacksets-and-roles "roles-how.md#stacksets-and-roles").

**Automating other tasks**

For information about how to increase certain AWS Control Tower service quotas with an
automated request method, view this video: [Automate Service Limit
Increases](https://www.youtube.com/watch?v=3WUShZ4lZGE "https://www.youtube.com/watch?v=3WUShZ4lZGE").

For technical blogs that cover automation and integration use cases, see [Automation and integration](related-information.md#automation-and-integration "related-information.md#automation-and-integration").

Two open source samples are available on GitHub to help you with certain automation tasks
related to security.

- The sample called [aws-control-tower-org-setup-sample](https://github.com/aws-samples/aws-control-tower-org-setup-sample "https://github.com/aws-samples/aws-control-tower-org-setup-sample") shows how to automate setting up the
  Audit account as the delegated administrator for security-related services.
- The sample called [aws-control-tower-account-setup-using-step-functions](https://github.com/aws-samples/aws-control-tower-account-setup-using-step-functions "https://github.com/aws-samples/aws-control-tower-account-setup-using-step-functions") shows how to
  automate security best practices using Step Functions, when provisioning and
  configuring new accounts. This sample includes adding principals to
  organizationally-shared AWS Service Catalog portfolios and associating
  organization-wide AWS IAM Identity Center groups to new accounts automatically. It also illustrates
  how to delete the default VPC in every Region.
  The _AWS Security Reference Architecture_ includes code
  examples for automating tasks related to AWS Control Tower. For more information, see the [AWS
  Prescriptive Guidance pages](../../../prescriptive-guidance/latest/security-reference-architecture/welcome.md "../../../prescriptive-guidance/latest/security-reference-architecture/welcome.md") and the [associated GitHub repository](https://github.com/aws-samples/aws-security-reference-architecture-examples/tree/main/aws_sra_examples "https://github.com/aws-samples/aws-security-reference-architecture-examples/tree/main/aws_sra_examples").

For information about using AWS Control Tower with AWS CloudShell, an AWS service that facilitates
working in the AWS CLI, see [AWS CloudShell and
the AWS CLI](using-aws-with-cloudshell.md "using-aws-with-cloudshell.md").

Because AWS Control Tower is an orchestration layer for AWS Organizations, many other AWS services
are available by means of APIs and the AWS CLI. For more information, see [Related AWS services](related-information.md#related-aws-services "related-information.md#related-aws-services").
