# Key changes

###### Note

- The definition of “registered” and “enrolled” have shifted with this new version of AWS Control Tower. When your
  account/OU has any AWS Control Tower resource enabled on it (e.g. control or baseline), it will be considered a
  governed resource. The definition will no longer be driven by the presence of the `AWSControlTowerBaseline`
  baseline.
- Service-Linked Roles are retained across all landing zone versions and are no longer deleted when OUs become "unregistered"
- Service-Linked Roles can only be deleted manually by customers after landing zone decommissioning

- **Pre-requisite for Landing Zone 4.0:** When upgrading to version 4.0 via API, ensure the `AWSControlTowerCloudTrailRole` service role uses the
  new managed policy `AWSControlTowerCloudTrailRolePolicy` instead of the existing inline policy. Detach
  the current inline policy and attach the new managed policy as described in the [documentation](../../../access-control-managing-permissions.md#AWSControlTowerCloudTrailRolePolicy "../../../access-control-managing-permissions.md#AWSControlTowerCloudTrailRolePolicy").
- **Optional Manifest:** Manifest field in the landing zone API is now optional. Customers
  can create Landing Zones without any service integrations. There is no impact for existing customers that are
  already using the manifest field.
- **Optional Organization Structure:** AWS Control Tower no longer enforces or manages the
  Security OU creation so customers can define and manage their own organization structure. However, AWS Control Tower
  will require all accounts that are configured for each AWS service integration to be under the same parent OU.
  There is no impact for customers that have already set-up the AWS Control Tower and have the Security OU.
  AWS Control Tower automatically deploys the resources and controls necessary to manage service integration accounts
  in the Security OU. For example, when AWS Config integration is enabled, AWS Config recording is enabled in all
  service integration accounts. The AWS Control Tower Baseline and the AWS Config Baseline are not applicable to
  the Security OU and integration accounts. To change service integrations, update landing zone settings.

###### Note

    + The organization structure setup for AWS Control Tower landing zone 4.0 has changed from previous landing zone versions. AWS Control Tower will
     no longer create the designated Security OU. The OU with the service integration accounts will be the designated Security OU.
    + If member accounts move into the OU where the accounts for each integration reside, enabled controls on that
     OU are drifted regardless of whether auto-enrollment is turned on or off.

- **Drift Notifications:** AWS Control Tower will stop sending drift notifications to
  SNS topic for all customers on landing zone 4.0 without the `AWSControlTowerBaseline` enabled, and will start
  sending drift notifications to EventBridge in the management account instead. To review sample events and guidance
  on how to receive drift notifications through EventBridge, please check [this guide](governance-drift.md "governance-drift.md").
- **Optional Service Integrations:** You now have the ability to enable/disable all AWS Control Tower integrations including AWS Config, AWS CloudTrail, SecurityRoles,
  and AWS Backup. These integrations also now have optionally required `enabled` flags in the API. The baselines
  that may apply to your landing zone or shared accounts now have dependencies on one another. The Integrations specific dependencies are:
  - Enablement:
    - `CentralSecurityRolesBaseline` → requires `CentralConfigBaseline` to be enabled
    - `IdentityCenterBaseline` → requires `CentralSecurityRolesBaseline` to be enabled
    - `BackupCentralVaultBaseline` → requires `CentralSecurityRolesBaseline` to be enabled
    - `BackupAdminBaseline` → requires `CentralSecurityRolesBaseline` to be enabled
    - `LogArchiveBaseline` → independent (no dependencies)
    - `CentralConfigBaseline` → independent (no dependencies)

  - Disablement:
    - `CentralConfigBaseline` can only be disabled if `CentralSecurityRolesBaseline`,
      `IdentityCenterBaseline`, `BackupAdminBaseline` and `BackupCentralVaultBaseline`
      baselines are disabled first.
    - `CentralSecurityRolesBaseline` can only be disabled if `IdentityCenterBaseline`,
      `BackupAdminBaseline` and `BackupCentralVaultBaseline` baselines are disabled first.
    - `IdentityCenterBaseline` can be disabled independently.
    - `BackupAdminBaseline` and `BackupCentralVaultBaseline` baselines can be disabled independently
    - `LogArchiveBaseline` can be disabled independently
