# Understanding the delegated administrator account and member account in Amazon Inspector

When using Amazon Inspector in a multi-account environment, the delegated administrator account has access to specific metadata.
The metadata includes standard scanning for Amazon EC2, Amazon ECR, and Lambda, and Lambda code scanning.
It also includes security finding results for member accounts.
This section provides information about which actions the delegated adminstrator account can make and member accounts can make.

## Delegated administrator actions

Generally, when the delegated administrator applies settings to their account,
those settings are applied to all of the other accounts in the organization. The
delegated administrator can also view and retrieve information for their own account
and any associated member. An Amazon Inspector delegated administrator account can perform the
following actions:

- Only the AWS Organizations management account can designate and remove a delegated administrator.
- When designating a delegated administrator, you must be in the same organization as the member accounts you want to manage.
- View and manage the status of Amazon Inspector for associated accounts, including
  activating and deactivating Amazon Inspector.
- Activate or deactivate scanning types for all member accounts in the
  organization.
- View aggregated finding data across the organization and finding details
  for all member accounts within the organization.
- Create and
  manage
  suppression rules that apply to findings for all accounts
  in the organization.
- Activate Amazon ECR enhanced scanning for all members of the
  organization.
- View resource coverage for the entire organization.
- Define the duration for automated re-scans of ECR container images for all member
  accounts in the organization. The delegated administrator’s scan duration
  setting overrides any setting that the member account previously set. All
  accounts in the organization share the Amazon ECR automated re-scan duration of
  the delegated administrators. You can't set different re-scan durations for
  individual accounts.
- Specify five custom paths for Amazon Inspector deep inspection for Amazon EC2 that will be
  used across all accounts in the organization. This is in addition to the
  five custom paths that a delegated administrator can set for their
  individual account. For more information about configuring deep inspection
  custom paths, see [Custom paths for Amazon Inspector deep inspection](deep-inspection.md#deep-inspection-paths "deep-inspection.md#deep-inspection-paths").
- Activate and deactivate Amazon Inspector deep inspection for member accounts.
- [Export SBOMs](sbom-export.md "sbom-export.md") for any member accounts in
  the organization.
- Set the Amazon EC2 scan mode for all member accounts in the organization. For
  more information, see [Managing scan mode](scanning-ec2.md#scan-mode "scanning-ec2.md#scan-mode").
- Create and manage CIS scan configurations for all accounts in the organization, except for any scan configurations created by member accounts.

###### Note

If a member account leaves the organization, the delegated administrator will no longer be
able to see scan configurations scheduled by that account.

- View CIS scan results for all accounts in the organization.

## Member account actions

A member account can view and retrieve information about their account in Amazon Inspector,
while settings for their account are managed by the delegated
administrator. Member accounts within an organization can perform
the following actions in Amazon Inspector:

- Activate Amazon Inspector for their own account.
- View resource coverage for their own account.
- View findings details for their own account.
- View the ECR container image automated re-scan duration setting for their own
  account.
- Specify five custom paths for Amazon Inspector deep inspection for EC2 that will be
  used for their individual account. These paths are scanned in addition to
  any custom paths that the delegated administrator has specified for the
  organization. For more information about configuring deep inspection paths,
  see [Custom paths for Amazon Inspector deep inspection](deep-inspection.md#deep-inspection-paths "deep-inspection.md#deep-inspection-paths").
- View the custom paths set by your delegated administrator for Amazon Inspector deep
  inspection.
- [Export SBOMs](sbom-export.md "sbom-export.md") for any resources
  associated with their account.
- View the scan mode for their account.
- Create and manage CIS scan configurations for their account.
- View the results of any CIS scans for resources in their account,
  including those scheduled by the delegated administrator.

###### Note

After activation, Amazon Inspector can be deactivated only by a delegated administrator
account.
