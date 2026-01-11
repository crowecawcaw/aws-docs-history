# Declarative policies

Declarative policies allow you to centrally declare and enforce your desired configuration
for a given AWS service at scale across an organization. Once attached, the configuration
is always maintained when the service adds new features or APIs. Use declarative policies to
prevent noncompliant actions. For example, you can block public internet access to Amazon VPC
resources across your organization.

The key benefits of using declarative policies are:

- **Ease of use**: You can enforce the baseline
  configuration for an AWS service with a few selections in the AWS Organizations and
  AWS Control Tower consoles or with a few commands using the AWS CLI & AWS SDKs.
- **Set once and forget**: The baseline configuration
  for an AWS service is always maintained, even when the service introduces new
  features or APIs. The baseline configuration is also maintained when new accounts
  are added to an organization or when new principals and resources are
  created.
- **Transparency**: The account status report allows
  you to review the current status of all attributes supported by declarative policies
  for the accounts in scope. You can also create customizable error messages, which
  can help administrators redirect end users to internal wiki pages or provide a
  descriptive message that can help end users understand why an action failed.
  For a full list of supported AWS services and attributes, see [Supported
  AWS services and attributes](#orgs_manage_policies_declarative-supported-controls "#orgs_manage_policies_declarative-supported-controls").

###### Topics

- [How declarative policies
  work](#orgs_manage_policies_declarative-how-work "#orgs_manage_policies_declarative-how-work")
- [Custom error messages](#orgs_manage_policies_declarative-custom-message "#orgs_manage_policies_declarative-custom-message")
- [Account status report](#orgs_manage_policies_declarative-account-status-report "#orgs_manage_policies_declarative-account-status-report")
- [Supported services](#orgs_manage_policies_declarative-supported-controls "#orgs_manage_policies_declarative-supported-controls")
- [Getting started](orgs_manage_policies-declarative_getting-started.md "orgs_manage_policies-declarative_getting-started.md")
- [Best practices](orgs_manage_policies_declarative_best-practices.md "orgs_manage_policies_declarative_best-practices.md")
- [Generating the account status report](orgs_manage_policies_declarative_status-report.md "orgs_manage_policies_declarative_status-report.md")
- [Declarative policy syntax and
  examples](orgs_manage_policies_declarative_syntax.md "orgs_manage_policies_declarative_syntax.md")

## How declarative policies

work

Declarative policies are enforced in the service's control plane, which is an
important distinction from [authorization policies such as service control policies (SCPs) and resource control
policies (RCPs)](orgs_manage_policies_authorization_policies.md "orgs_manage_policies_authorization_policies.md"). While authorization policies regulate access to APIs,
declarative policies are applied directly at the service level to enforce durable
intent. This ensures that the baseline configuration is always enforced, even when new
features or APIs are introduced by the service.

The following table helps illustrate this distinction and provides some use
cases.

|                               | Service control policies                                                                                                                                                                                                                                                                                                                                                                  | Resource control policies                                                                                                                                                                                                                                                                                                                                                                                                  | Declarative policies                                                                                                                                                                                            |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Why?                          | To centrally define and enforce consistent access controls on<br>principals (such as IAM users and IAM roles) at scale.                                                                                                                                                                                                                                                                   | To centrally define and enforce consistent access controls on<br>resources at scale                                                                                                                                                                                                                                                                                                                                        | To centrally define and enforce the baseline configuration for<br>AWS services at scale.                                                                                                                        |
| How?                          | By controlling the maximum available access permissions of<br>principals at an API level.                                                                                                                                                                                                                                                                                                 | By controlling the maximum available access permissions for<br>resources at an API level.                                                                                                                                                                                                                                                                                                                                  | By enforcing the desired configuration of an AWS service without<br>using API actions.                                                                                                                          |
| Governs service-linked roles? | No                                                                                                                                                                                                                                                                                                                                                                                        | No                                                                                                                                                                                                                                                                                                                                                                                                                         | Yes                                                                                                                                                                                                             |
| Feedback mechanism            | Non-customizable access denied SCP error.                                                                                                                                                                                                                                                                                                                                                 | Non-customizable access denied RCP error.                                                                                                                                                                                                                                                                                                                                                                                  | Customizable error message. For more information, see [Custom error messages<br>for declarative policies](#orgs_manage_policies_declarative-custom-message "#orgs_manage_policies_declarative-custom-message"). |
| Example policy                | [Deny member accounts from leaving the organization](https://github.com/aws-samples/service-control-policy-examples/blob/main/Privileged-access-controls/Deny-member-accounts-from-leaving-your-AWS-organization.json "https://github.com/aws-samples/service-control-policy-examples/blob/main/Privileged-access-controls/Deny-member-accounts-from-leaving-your-AWS-organization.json") | [Restrict access to only HTTPS connections to your resources](https://github.com/aws-samples/resource-control-policy-examples/blob/main/Restrict-resource-access-patterns/Restrict-access-to-only-HTTPS-connections-to-your-resources.json "https://github.com/aws-samples/resource-control-policy-examples/blob/main/Restrict-resource-access-patterns/Restrict-access-to-only-HTTPS-connections-to-your-resources.json") | [Allowed<br>Images Settings](orgs_manage_policies_declarative_syntax.md#declarative-policy-ec2-ami-allowed-images "orgs_manage_policies_declarative_syntax.md#declarative-policy-ec2-ami-allowed-images")       |

After you have [created](orgs_policies_create.md#create-declarative-policy-procedure "orgs_policies_create.md#create-declarative-policy-procedure") and [attached](orgs_policies_attach.md "orgs_policies_attach.md") a
declarative policy, it is applied and enforced across your organization. Declarative
policies can be applied to an entire organization, organizational units (OUs), or
accounts. Accounts joining an organization will automatically inherit the declarative
policy in the organization. For more information, see [Understanding management policy
inheritance](orgs_manage_policies_inheritance_mgmt.md "orgs_manage_policies_inheritance_mgmt.md").

The _effective policy_ is the set of rules that are
inherited from the organization root and OUs along with those directly attached to the
account. The effective policy specifies the final set of rules that apply to the
account. For more information, see [Viewing effective management
policies](orgs_manage_policies_effective.md "orgs_manage_policies_effective.md").

If a declarative policy is [detached](orgs_policies_detach.md "orgs_policies_detach.md"), the
attribute state will roll back to its previous state before the declarative policy was
attached.

## Custom error messages

for declarative policies

Declarative policies allow you to create custom error messages. For example, if an API
operation fails due to a declarative policy, you can set the error message or provide a
custom URL, such as a link to an internal wiki or a link to a message that describes the
failure. If you do not specify a custom error message, AWS Organizations provides the following
default error message: `Example: This action is denied due to an organizational
 policy in effect`.

You can also audit the process of creating declarative policies, updating declarative
policies, and deleting declarative policies with AWS CloudTrail. CloudTrail can flag API operation
failures due to declarative policies. For more information, see [Logging
and monitoring](orgs_security_incident-response.md "orgs_security_incident-response.md").

###### Important

Do not include _personally identifiable information (PII)_ or
other sensitive information in a custom error message. PII includes general
information that can be used to identify or locate an individual. It covers records
such as financial, medical, educational, or employment. PII examples include
addresses, bank account numbers, and phone numbers.

## Account status

report for declarative policies

The _account status report_ allows you to review the current status
of all attributes supported by declarative policies for the accounts in scope. You can
choose the accounts and organizational units (OUs) to include in the report scope, or
choose an entire organization by selecting the root.

This report helps you assess readiness by providing a Region breakdown and if the
current state of an attribute is _uniform across accounts_ (through
the `numberOfMatchedAccounts`) or _inconsistent_ (through
the `numberOfUnmatchedAccounts`). You can also see the _most
frequent value_, which is the configuration value that is most frequently
observed for the attribute.

In Figure 1, there is a generated account status report, which shows uniformity across
accounts for the following attributes: VPC Block Public Access and Image Block Public
Access. This means that, for each attribute, all the accounts in scope have the same
configuration for that attribute.

The generated account status report shows inconsistent accounts for the following
attributes: Allowed Images Settings, Instance Metadata defaults, Serial Console Access,
and Snapshot Block Public Access. In this example, each attribute with an inconsistent
account is due to there being one account with a different configuration value.

If there is a most frequent value, that is displayed in its respective column. For
more detailed information of what each attribute controls, see [Declarative policy syntax and
example policies](orgs_manage_policies_declarative_syntax.md "orgs_manage_policies_declarative_syntax.md").

You can also expand an attribute to see a Region breakdown. In this example, Image
Block Public Access is expanded and in each Region, you can see that there is also
uniformity across accounts.

The choice to attach a declarative policy for enforcing a baseline configuration
depends on your specific use case. Use the account status report to help you assess your
readiness before attaching a declarative policy.

For more information, see [Generating the account
status report](orgs_manage_policies_declarative_status-report.md "orgs_manage_policies_declarative_status-report.md").

![Example account status report with uniformity across accounts for VPC Block Public Access and Image Block Public Access](images/declarative-status-report.png)

_Figure 1: Example account status report with uniformity across accounts for
VPC Block Public Access and Image Block Public Access._

## Supported

AWS services and attributes

### Supported

attributes for declarative policies for EC2

The following table displays the attributes supported for Amazon EC2 related
services.

| Declarative policies for EC2 | AWS service                                                                                       | Attribute                                                                                                                                                                                            | Policy effect                                                                                                                                                                                                                                                                   | Policy contents                                                                                                                                                                                                                                                              | More information |
| ---------------------------- | ------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| Amazon VPC                   | VPC Block Public Access                                                                           | Controls if resources in Amazon VPCs and subnets can reach the<br>internet through internet gateways (IGWs).                                                                                         | [View<br>policy](orgs_manage_policies_declarative_syntax.md#declarative-policy-vpc-block-public-access "orgs_manage_policies_declarative_syntax.md#declarative-policy-vpc-block-public-access")                                                                                 | For more information, see [Block public<br>access to VPCs and subnets](../../../vpc/latest/userguide/security-vpc-bpa.md "../../../vpc/latest/userguide/security-vpc-bpa.md") in the<br>_Amazon VPC User Guide_.                                                             |
| Amazon EC2                   | Serial Console Access                                                                             | Controls if the EC2 serial console is accessible.                                                                                                                                                    | [View<br>policy](orgs_manage_policies_declarative_syntax.md#declarative-policy-ec2-serial-console-access "orgs_manage_policies_declarative_syntax.md#declarative-policy-ec2-serial-console-access")                                                                             | For more information, see [Configure access to the EC2 Serial Console](../../../AWSEC2/latest/UserGuide/configure-access-to-serial-console.md "../../../AWSEC2/latest/UserGuide/configure-access-to-serial-console.md") in the<br>_Amazon Elastic Compute Cloud User Guide_. |
| Image Block Public Access    | Controls if Amazon Machine Images (AMIs) are publicly<br>sharable.                                | [View policy](orgs_manage_policies_declarative_syntax.md#declarative-policy-ec2-ami-block-public-access "orgs_manage_policies_declarative_syntax.md#declarative-policy-ec2-ami-block-public-access") | For more information, see [Understand block public access for AMIs](../../../AWSEC2/latest/UserGuide/block-public-access-to-amis.md "../../../AWSEC2/latest/UserGuide/block-public-access-to-amis.md") in the<br>_Amazon Elastic Compute Cloud User Guide_.                     |
| Allowed Images Settings      | Controls the discovery and use of Amazon Machine Images (AMI) in<br>Amazon EC2 with Allowed AMIs. | [View<br>policy](orgs_manage_policies_declarative_syntax.md#declarative-policy-ec2-ami-allowed-images "orgs_manage_policies_declarative_syntax.md#declarative-policy-ec2-ami-allowed-images")        | For more information, see [Amazon<br>Machine Images (AMIs)](../../../AWSEC2/latest/UserGuide/ec2-allowed-amis.md "../../../AWSEC2/latest/UserGuide/ec2-allowed-amis.md") in the _Amazon Elastic Compute Cloud User<br>Guide_.                                                   |
| Instance Metadata Defaults   | Controls IMDS defaults for all new EC2 instances<br>launches.                                     | [View<br>policy](orgs_manage_policies_declarative_syntax.md#declarative-policy-default-imds-version "orgs_manage_policies_declarative_syntax.md#declarative-policy-default-imds-version")            | For more information, see [Configure instance metadata options for new instances](../../../AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.md "../../../AWSEC2/latest/UserGuide/configuring-IMDS-new-instances.md")<br>in the _Amazon Elastic Compute Cloud User Guide_. |
| Amazon EBS                   | Snapshot Block Public Access                                                                      | Controls if Amazon EBS snapshots are publicly accessible.                                                                                                                                            | [View policy](orgs_manage_policies_declarative_syntax.md#declarative-policy-vpc-eb2-snapshots-block-public-access "orgs_manage_policies_declarative_syntax.md#declarative-policy-vpc-eb2-snapshots-block-public-access")                                                        | For more information, see [Block public access for Amazon EBS snapshots](../../../ebs/latest/userguide/block-public-access-snapshots.md "../../../ebs/latest/userguide/block-public-access-snapshots.md") in the<br>_Amazon Elastic Block Store User Guide_.                 |
