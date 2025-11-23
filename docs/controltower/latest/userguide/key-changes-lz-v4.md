# Key Changes

- **Optional Service Integrations:** You now have the ability to enable/disable all
  AWS Control Tower integrations including AWS Config, AWS CloudTrail, SecurityRoles, and AWS Backup. These integrations also now have
  optionally required `enabled` flags in the API. The baselines that may apply to your landing zone or shared accounts
  now have dependencies on one another. The Integrations specific dependencies are:
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

- **AWS Config and AWS CloudTrail now use separate dedicated S3 buckets and SNS topics**
  instead of shared resources. Customers have restricted flexibility to use a single or separate accounts for
  multiple integrations.
  - Data Location Changes: Existing customers upgrading from previously shared to dedicated resources will have
    AWS Config and AWS CloudTrail data in different S3 buckets. Established customer workflows and tools may need updates
    to access data from new bucket locations.
  - AWS CloudTrail will continue to stay in the same existing bucket, but AWS Config data will be in a new S3 bucket
    created by AWS Control Tower.
  - Customers can set-up cross-bucket replication if they wish to centralize different logs to a single bucket.
    Please see [S3 documentation](../../../AmazonS3/latest/userguide/replication.md "../../../AmazonS3/latest/userguide/replication.md") for more information.

- **New `ConfigBaseline` baseline:** There is now a separate `ConfigBaseline`
  at the OU level for detective controls support without requiring the comprehensive `AWSControlTowerBaseline`.
  See list of [baseline types at the OU level](types-of-baselines.md#ou-baseline-types "types-of-baselines.md#ou-baseline-types") for more information. For existing customers that are using the default landing zone,
  all service integrations are now optional, with the caveat of dependency requirements outlined above.
- **Service-Linked Config Aggregator:** Replaces organization and account aggregators
  in the AWS Config central aggregator account.
  - When upgrading to landing zone 4.0 with AWS Config integration enabled, customers need to have
    `organizations:ListDelegatedAdministrators` permissions

  ```

  {
     "Version": "2012-10-17",
     "Statement": [
        {
           "Effect": "Allow",
           "Action": [
              "backup:UpdateGlobalSettings",
              "controltower:CreateLandingZone",
              "controltower:UpdateLandingZone",
              "controltower:ResetLandingZone",
              "controltower:DeleteLandingZone",
              "controltower:GetLandingZoneOperation",
              "controltower:GetLandingZone",
              "controltower:ListLandingZones",
              "controltower:ListLandingZoneOperations",
              "controltower:ListTagsForResource",
              "controltower:TagResource",
              "controltower:UntagResource",
              "servicecatalog:*",
              "organizations:*",
              "organizations:RegisterDelegatedAdministrator",
              "organizations:EnableAWSServiceAccess",
              "organizations:DeregisterDelegatedAdministrator",
              "organizations:ListDelegatedAdministrators",
              "sso:*",
              "sso-directory:*",
              "logs:*",
              "cloudformation:*",
              "kms:*",
              "iam:GetRole",
              "iam:CreateRole",
              "iam:GetSAMLProvider",
              "iam:CreateSAMLProvider",
              "iam:CreateServiceLinkedRole",
              "iam:ListRolePolicies",
              "iam:PutRolePolicy",
              "iam:ListAttachedRolePolicies",
              "iam:AttachRolePolicy",
              "iam:DeleteRole",
              "iam:DeleteRolePolicy",
              "iam:DetachRolePolicy"
           ],
           "Resource": "*"
        }
     ]
  }

  ```

When migrating to landing zone 4.0 with AWS Config integration enabled, customers would see the following changes -

    1. The existing Audit account is registered as a delegated admin for AWS Config.
    2. Service-Linked Config Aggregator is deployed into the Audit account (AWS Config central aggregator account for new
     customers and Audit account for existing customers). The new aggregator can aggregate data from any AWS Config Recorder
     in the organization, including non-Control Tower managed accounts.
    3. Existing aggregators will be deleted - Organization aggregator in management account (`aws-controltower-ConfigAggregatorForOrganizations`) and account aggregator in Audit account (`aws-controltower-GuardRailsComplianceAggregator`) will be deleted.
    4. Controls associated with the deleted aggregators will be automatically removed. Additionally, since AWS Config Rules
     and Configuration Aggregator will be service-linked resources, service control policy protection will no longer
     be required.





    	1. [Disallow Changes to Tags Created by AWS Control Tower for AWS Config Resources](../controlreference/mandatory-controls.md#cloudwatch-disallow-config-changes "../controlreference/mandatory-controls.md#cloudwatch-disallow-config-changes")
    	2. [Disallow Deletion of AWS Config Aggregation Authorizations Created by AWS Control Tower](../controlreference/mandatory-controls.md#config-aggregation-authorization-policy "../controlreference/mandatory-controls.md#config-aggregation-authorization-policy")
    	3. [Disallow Changes to AWS Config Rules Set Up by AWS Control Tower](../controlreference/mandatory-controls.md#config-rule-disallow-changes "../controlreference/mandatory-controls.md#config-rule-disallow-changes")

- **Optional Manifest:** Manifest field in the landing zone API is now optional. Customers
  can create Landing Zones without any service integrations. There is no impact for existing customers that are
  already using the manifest field.
- **Optional Organization Structure:** AWS Control Tower no longer enforces or manages the
  Security OU creation so customers can define and manage their own organization structure. However, AWS Control Tower
  will require all accounts that are configured for each AWS service integration to be under the same parent OU.
  There is no impact for customers that have already set-up the AWS Control Tower and have the Security OU.

###### Note

If member accounts move into the OU where the accounts for each integration reside, enabled controls on that
OU are drifted regardless of whether auto-enrollment is turned on or off.

- **Drift Notifications:** AWS Control Tower will stop sending drift notifications to
  SNS topic for all customers on landing zone 4.0 without the `AWSControlTowerBaseline` enabled, and will start
  sending drift notifications to EventBridge in the management account instead. To review sample events and guidance
  on how to receive drift notifications through EventBridge, please check [this guide](governance-drift.md "governance-drift.md").

###### Note

###### Key Notes:

- The definition of “registered” and “enrolled” have shifted with this new version of AWS Control Tower. When your
  account/OU has any AWS Control Tower resource enabled on it (e.g. control or baseline), it will be considered a
  governed resource. The definition will no longer be driven by the presence of the `AWSControlTowerBaseline`
  baseline.
- Service-Linked Roles are retained across all landing zone versions and are no longer deleted when OUs become "unregistered"
- Service-Linked Roles can only be deleted manually by customers after landing zone decommissioning
