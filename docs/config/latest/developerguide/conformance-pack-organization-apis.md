# Managing Conformance Packs for AWS Config Across all

Accounts in Your Organization

Use AWS Config to manage conformance packs across all AWS accounts within an organization. You
can do the following:

- Centrally deploy, update, and delete conformance packs across member accounts in
  an organization in AWS Organizations.
- Deploy a common set of AWS Config rules and remediation actions across all accounts and
  specify accounts where AWS Config rules and remediation actions should not be
  created.
- Use the management account in AWS Organizations to enforce governance by ensuring
  that the underlying AWS Config rules and remediation actions are not modifiable by your
  organization’s member accounts.

## Considerations

**For deployments across different regions**

The API call to deploy rules and conformance packs across accounts is AWS Region specific.
At the organization level, you need to change the context of your API call to a
different region if you want to deploy rules in other regions. For example, to deploy a
rule in US East (N. Virginia), change the region to US East (N. Virginia) and then call
`PutOrganizationConfigRule`.

**For accounts within an organization**

If a new account joins an organization, the rule or conformance pack is deployed to
that account. When an account leaves an organization, the rule or conformance pack is
removed.

If you deploy an organizational rule or conformance pack in an organization
administrator account, and then establish a delegated administrator and deploy an
organizational rule or conformance pack in the delegated administrator account, you
won't be able to see the organizational rule or conformance pack in the organization
administrator account from the delegated administrator account or see the organizational
rule or conformance pack in the delegated administrator account from organization
administrator account. The [DescribeOrganizationConfigRules](../APIReference/API_DescribeOrganizationConfigRules.md "../APIReference/API_DescribeOrganizationConfigRules.md") and [DescribeOrganizationConformancePacks](../APIReference/API_DescribeOrganizationConformancePacks.md "../APIReference/API_DescribeOrganizationConformancePacks.md") APIs can only see and interact with
the organization-related resource that were deployed from within the account calling
those APIs.

**Retry mechanism for new accounts added to an organization**

Deployment of existing organizational rules and conformance packs will only be retried
for 7 hours after an account is added to your organization if a recorder is not
available. You are expected to create a recorder if one doesn't exist within 7 hours of
adding an account to your organization.

**Organization management accounts, delegated administrators, and service-linked roles**

If you are using an organization management account and intend to use a delegated administrator for organizational deployment, be aware that AWS Config won't automatically create the service-linked role (SLR).
You must manually create the service-linked role (SLR) separately using IAM.

If you do not have an SLR for your management account, you will not be able to deploy resources to that account from a delegated administrator account.
You will still be able to deploy conformance packs to member accounts from management and delegated administrator accounts.
For more information, see [Using service-linked roles](../../../IAM/latest/UserGuide/using-service-linked-roles.md "../../../IAM/latest/UserGuide/using-service-linked-roles.md") in the _AWS Identity and Access Management (IAM) User Guide_.

## Deployment

To deploy with the AWS Management Console
To a deploy a conformance pack across an organization from the AWS console, use AWS Systems Manager. For more information, see
[Deploy AWS Config conformance packs](../../../systems-manager/latest/userguide/quick-setup-cpack.md "../../../systems-manager/latest/userguide/quick-setup-cpack.md") in the _AWS Systems Manager User Guide_.

To deploy with the AWS APIFor information on how to integrate AWS Config with AWS Organizations, see [AWS Config and AWS Organizations](../../../organizations/latest/userguide/services-that-can-integrate-config.md "../../../organizations/latest/userguide/services-that-can-integrate-config.md")
in the _AWS Organizations User Guide_. Ensure AWS Config recording is on before you use the following APIs to manage conformance pack
rules across all AWS accounts within an organization:

- [DeleteOrganizationConformancePack](../APIReference/API_DeleteOrganizationConformancePack.md "../APIReference/API_DeleteOrganizationConformancePack.md"), deletes the specified organization
  conformance pack and all of the config rules and remediation actions from all member
  accounts in that organization.
- [DescribeOrganizationConformancePacks](../APIReference/API_DescribeOrganizationConformancePacks.md "../APIReference/API_DescribeOrganizationConformancePacks.md"), returns a list of organization
  conformance packs.
- [DescribeOrganizationConformancePackStatuses](../APIReference/API_DescribeOrganizationConformancePackStatuses.md "../APIReference/API_DescribeOrganizationConformancePackStatuses.md"), provides organization
  conformance pack deployment status for an organization.
- [GetOrganizationConformancePackDetailedStatus](../APIReference/API_GetOrganizationConformancePackDetailedStatus.md "../APIReference/API_GetOrganizationConformancePackDetailedStatus.md"), returns detailed status
  for each member account within an organization for a given organization conformance
  pack.
- [PutOrganizationConformancePack](../APIReference/API_PutOrganizationConformancePack.md "../APIReference/API_PutOrganizationConformancePack.md"), deploys conformance packs across member
  accounts in an AWS Organization.

## Region Support

Deploying conformance packs across member accounts in an AWS Organization is
supported in the following Regions.

| Region Name               | Region         | Endpoint                            | Protocol |
| ------------------------- | -------------- | ----------------------------------- | -------- |
| US East (Ohio)            | us-east-2      | config.us-east-2.amazonaws.com      | HTTPS    |
| US East (N. Virginia)     | us-east-1      | config.us-east-1.amazonaws.com      | HTTPS    |
| US West (N. California)   | us-west-1      | config.us-west-1.amazonaws.com      | HTTPS    |
| US West (Oregon)          | us-west-2      | config.us-west-2.amazonaws.com      | HTTPS    |
| Africa (Cape Town)        | af-south-1     | config.af-south-1.amazonaws.com     | HTTPS    |
| Asia Pacific (Hong Kong)  | ap-east-1      | config.ap-east-1.amazonaws.com      | HTTPS    |
| Asia Pacific (Hyderabad)  | ap-south-2     | config.ap-south-2.amazonaws.com     | HTTPS    |
| Asia Pacific (Jakarta)    | ap-southeast-3 | config.ap-southeast-3.amazonaws.com | HTTPS    |
| Asia Pacific (Melbourne)  | ap-southeast-4 | config.ap-southeast-4.amazonaws.com | HTTPS    |
| Asia Pacific (Mumbai)     | ap-south-1     | config.ap-south-1.amazonaws.com     | HTTPS    |
| Asia Pacific (Osaka)      | ap-northeast-3 | config.ap-northeast-3.amazonaws.com | HTTPS    |
| Asia Pacific (Seoul)      | ap-northeast-2 | config.ap-northeast-2.amazonaws.com | HTTPS    |
| Asia Pacific (Singapore)  | ap-southeast-1 | config.ap-southeast-1.amazonaws.com | HTTPS    |
| Asia Pacific (Sydney)     | ap-southeast-2 | config.ap-southeast-2.amazonaws.com | HTTPS    |
| Asia Pacific (Tokyo)      | ap-northeast-1 | config.ap-northeast-1.amazonaws.com | HTTPS    |
| Canada (Central)          | ca-central-1   | config.ca-central-1.amazonaws.com   | HTTPS    |
| Canada West (Calgary)     | ca-west-1      | config.ca-west-1.amazonaws.com      | HTTPS    |
| Europe (Frankfurt)        | eu-central-1   | config.eu-central-1.amazonaws.com   | HTTPS    |
| Europe (Ireland)          | eu-west-1      | config.eu-west-1.amazonaws.com      | HTTPS    |
| Europe (London)           | eu-west-2      | config.eu-west-2.amazonaws.com      | HTTPS    |
| Europe (Milan)            | eu-south-1     | config.eu-south-1.amazonaws.com     | HTTPS    |
| Europe (Paris)            | eu-west-3      | config.eu-west-3.amazonaws.com      | HTTPS    |
| Europe (Spain)            | eu-south-2     | config.eu-south-2.amazonaws.com     | HTTPS    |
| Europe (Stockholm)        | eu-north-1     | config.eu-north-1.amazonaws.com     | HTTPS    |
| Europe (Zurich)           | eu-central-2   | config.eu-central-2.amazonaws.com   | HTTPS    |
| Israel (Tel Aviv)         | il-central-1   | config.il-central-1.amazonaws.com   | HTTPS    |
| Middle East (Bahrain)     | me-south-1     | config.me-south-1.amazonaws.com     | HTTPS    |
| Middle East (UAE)         | me-central-1   | config.me-central-1.amazonaws.com   | HTTPS    |
| South America (São Paulo) | sa-east-1      | config.sa-east-1.amazonaws.com      | HTTPS    |
| AWS GovCloud (US-East)    | us-gov-east-1  | config.us-gov-east-1.amazonaws.com  | HTTPS    |
| AWS GovCloud (US-West)    | us-gov-west-1  | config.us-gov-west-1.amazonaws.com  | HTTPS    |
