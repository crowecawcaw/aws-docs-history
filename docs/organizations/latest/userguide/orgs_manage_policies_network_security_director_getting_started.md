# Getting started with

AWS Shield Network Security Director policies

Before you configure Network Security Director policies, ensure you understand the prerequisites and
implementation requirements. This topic guides you through the process of setting up and
managing these policies in your organization.

## Before you begin

Review the following requirements before implementing AWS Shield Network Security Director policies:

- Your account must be part of an AWS organization
- You must be signed in as either:
  - The management account for the organization
  - An AWS Organizations delegated administrator with permissions to manage AWS Shield Network
    Security Director policies

- You must enable trusted access for Network Security Director in your organization
- You must enable the Network Security Director policy type in the root of your organization

Additionally, verify that:

- AWS Shield Network Security Director is supported in the Regions where you want to apply
  policies
- You have the AWS Shield Network Security Director service-linked role
  configured in your management account. If you need to create this role, you can create it
  directly by running `aws iam create-service-linked-role --aws-service-name
network-director.amazonaws.com`.

## Implementation

steps

To implement Network Security Director policies effectively, follow these steps in sequence. Each step
ensures proper configuration and helps prevent common issues during setup. These steps can be performed
through the
AWS Organizations console, AWS Command Line Interface (AWS CLI), or AWS SDKs.

1. [Enable trusted
   access for AWS Shield Network Security Director](orgs_integrate_services.md#orgs_how-to-enable-disable-trusted-access "orgs_integrate_services.md#orgs_how-to-enable-disable-trusted-access").
2. [Enable
   AWS Shield Network Security Director policies for your organization](enable-policy-type.md "enable-policy-type.md").
3. [Create an AWS Shield Network
   Security Director
   policy](orgs_manage_policies_network_security_director_syntax.md "orgs_manage_policies_network_security_director_syntax.md").
4. [Attach the policy to your organization's root, OU, or
   account](orgs_policies_attach.md "orgs_policies_attach.md").
5. [View the combined effective
   Network Security Director policy that applies to an account](orgs_manage_policies_effective.md "orgs_manage_policies_effective.md").
