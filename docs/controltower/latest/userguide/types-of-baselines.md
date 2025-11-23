# Types of baselines

A _baseline_ in AWS Control Tower is a group of resources and
specific configurations that you can apply to a target. The most common baseline target may
be an organizational unit (OU). For example, you can enable a baseline with an OU selected
as a target, to register that OU into AWS Control Tower.

During landing zone setup, some baselines may be enabled on shared account automatically.
Certain baselines may be enabled and updated based on your landing zone settings
and configurations. AWS Control Tower creates and deploys the resources to the target in the way that
the baseline specifies.

When you enable a baseline on a target, the baseline is represented as an AWS resource,
called an `EnabledBaseline` resource.

AWS Control Tower includes two general types of baselines:

- Baselines that can be enabled on an OU.
- Baselines that can be enabled on shared account, during landing zone set up.

## Baseline types that apply at the OU level

###### Note

Only Baselines that apply at OU level can be directly enabled
with the `EnableBaseline` API.

- **Name**: `AWSControlTowerBaseline`

**Description**: Sets up resources and mandatory controls for
member accounts within the target OU, required for AWS Control Tower governance.

**Consideration**: This baseline retains the settings of the
landing zone **Region deny** control. In other words, if a
Region is not allowed at the landing zone level, that Region is not allowed for
that OU when you call the `EnableBaseline` API to register an OU.

###### Note

The OU-level Region deny control has no way to allow Regions that the
landing zone Region deny control does not allow.

For more information, see [How SCPs work with deny](../../../organizations/latest/userguide/orgs_manage_policies_scps_evaluation.md#how_scps_deny "../../../organizations/latest/userguide/orgs_manage_policies_scps_evaluation.md#how_scps_deny") in the AWS Organizations documentation.

**Recommendation**: We recommend that you confirm the Regions
in which your target OU may be running workloads, and check the results against
the landing zone Region deny control, before you call the
`EnableBaseline` API for the OU, or you could lose access to
resources in certain Regions.

- **Name**: `ConfigBaseline`

**Description**: This baseline sets up AWS Config related resources
for member accounts within the target OU required for Detective Controls enablement.
The resources set up are a subset of resources of AWSControlTowerBaseline.

**Consideration**: This baseline does not retain the settings of
the landing zone Region deny control. Region deny control will not be enabled
as part of enabling ConfigBaseline.

**Limitation**: AWSControlTowerBaseline and ConfigBaseline cannot
be enabled on the same OU. Only one of them is allowed on an OU.

- **Name**: `BackupBaseline`

**Description**: This baseline sets up resources and controls
for member accounts within the target OU. These are required so that integration
with AWS Backup can automate your data backup across AWS services, and centralize
your backup policy management.

**Consideration**: Before you enable the
`BackupBaseline` on a target OU, make sure that the
`AWSControlTowerBaseline` is enabled on the target OU. That is,
the target OU must be registered in AWS Control Tower.

    + You can choose to activate AWS Backup during the process of creating your
     AWS Control Tower landing zone, or during a landing zone update process.
    + The `BackupBaseline` is compatible with landing zone versions
     3.1 and later.
    + The `BackupBaseline` is not applied to the management
     account.

## Baseline types that may be applied on shared account

during landing zone set up

AWS Control Tower enables certain baselines on shared account, as
part of the landing zone setup and update process. Baselines for your landing zone may
change as you change your landing zone settings. For example, if you opt in for IAM Identity Center,
AWS Control Tower can enable the latest version of the `IdentityCenterBaseline`
baseline on your landing zone.

You can view the enabled baselines for your landing zone with the
`ListEnabledBaselines` API call.

###### Note

Starting with Landing Zone version 4.0, the AuditBaseline is replaced by two distinct
baselines: `CentralSecurityRolesBaseline` and `CentralConfigBaseline`.

- **Name**: `CentralConfigBaseline`

**Description**: Sets up central resources for compliance monitoring
and auditing within your organization using AWS Config.

- **Name**: `CentralSecurityRolesBaseline`

**Description**: Sets up central resources for security monitoring
within your organization.

- **Name**: `AuditBaseline`

**Description**: Sets up resources to monitor security and
compliance of accounts in your organization.

- **Name**: `LogArchiveBaseline`

**Description**: Sets up a central repository for logs of API
activities and resource configurations from accounts in your organization.

- **Name**: `IdentityCenterBaseline`

**Description**: Sets up shared resources for IAM Identity Center, which
prepares the `AWSControlTowerBaseline` to set up Identity Center
access for accounts.

**Consideration**: This baseline works only when you’ve
selected IAM Identity Center as your identity provider at the time you set up your landing
zone initially, or if you subsequently change your landing zone settings to
enable IAM Identity Center for your landing zone. If you’re using a different identity
provider, you won’t have access to enable this baseline.

- **Name**: `BackupCentralVaultBaseline`

**Description**: Sets up the central AWS Backup vault in your
organization.

- **Name**: `BackupAdminBaseline`

**Description**: Sets up delegated admin and the AWS Backup Audit
Manager.

## Enabled baselines and member accounts

When you enable a baseline on an OU, that configuration is inherited by the OU's
member accounts. Due to the fact of inheritance, we call it a _child enabled
baseline_ when we refer to the account. The baseline that's applied to the OU is called the
_parent enabled baseline_. The parent enabled baseline controls
the configuration of its child enabled baselines. It is similar to how a control, when enabled on an OU, applies to every account within the OU.

**View an account's baseline status**

AWS Control Tower does not allow you to target accounts directly with baselines. However, you
can track the enablement and drift status of each member account by means of their inherited child
enabled baselines. To view the status of your accounts, you can call the
[`ListEnabledBaselines`](../APIReference/API_ListEnabledBaselines.md "../APIReference/API_ListEnabledBaselines.md") API with the `includeChildren` feature
flag.

**Disable an account's baseline**

AWS Control Tower does not allow you to disable a child enabled baseline linked to a parent enabled baseline.
A child enabled baseline can be disabled if it is inheritance drifted and no longer linked to a parent enabled baseline.

## Baselines and versioning defaults

If your AWS Control Tower landing zone is already set up, and then you choose to enable a
landing zone baseline, AWS Control Tower enables the latest version of the baseline that is
compatible with your landing zone version. If you choose to enable a baseline for an OU
that is not already registered with AWS Control Tower, AWS Control Tower provides the latest compatible
version of the baseline for that OU, automatically.
