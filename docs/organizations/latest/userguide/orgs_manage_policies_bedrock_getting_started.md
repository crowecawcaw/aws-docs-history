# Getting started with

Amazon Bedrock policies

Before you configure Amazon Bedrock policies, ensure you understand the prerequisites and
implementation requirements. This topic guides you through the process of setting up and
managing these policies in your organization.

## Before you begin

Review the following requirements before implementing Amazon Bedrock policies:

- Your account must be part of an AWS organization
- You must be signed in as either:
  - The management account for the organization
  - A delegated administrator account with permissions to manage Amazon Bedrock
    policies

- You must enable trusted access for Amazon Bedrock in your organization
- You must enable the Amazon Bedrock policy type in the root of your organization

## Implementation

steps

To implement Amazon Bedrock policies effectively, follow these steps in sequence. Each step
ensures proper configuration and helps prevent common issues during setup. The
management account or delegated administrator can perform these steps through the
AWS Organizations console, AWS Command Line Interface (AWS CLI), or AWS SDKs.

1. [Enable trusted
   access for Amazon Bedrock](orgs_integrate_services.md#orgs_how-to-enable-disable-trusted-access "orgs_integrate_services.md#orgs_how-to-enable-disable-trusted-access").
2. [Enable
   Amazon Bedrock policies for your organization](enable-policy-type.md "enable-policy-type.md").
3. [Create an Amazon Bedrock
   policy](orgs_manage_policies_bedrock_syntax.md "orgs_manage_policies_bedrock_syntax.md").
4. [Attach the Amazon Bedrock policy to your organization's root, OU, or
   account](orgs_policies_attach.md "orgs_policies_attach.md").
5. [View the combined effective
   Amazon Bedrock policy that applies to an account](orgs_manage_policies_effective.md "orgs_manage_policies_effective.md").

For all of these steps, you sign in as an AWS Identity and Access Management (IAM) user, assume an IAM
role, or sign in as the root user ([not
recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization's management account.
