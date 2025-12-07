# AWS Config Updates

- **Dedicated resources for AWS Config and AWS CloudTrail:** AWS Config and AWS CloudTrail now use
  separate dedicated S3 buckets and SNS topics instead of shared resources. Customers have restricted flexibility to
  use a single or separate accounts for multiple integrations.
  - When upgrading to AWS Control Tower landing zone version 4.0, existing data and S3 buckets are not moved. AWS CloudTrail integration
    continues to use the existing S3 bucket with prefix `aws-controltower-logs`. The new AWS Config data post the
    update operation will be stored in a new S3 bucket with prefix `aws-controltower-config` that AWS Control
    Tower creates in the account designated for the CentralConfigBaseline.

  ###### Note

  Enabling AWS CloudTrail integration on landing zone 4.0 for the first time will create new S3 buckets each time with prefix `aws-controltower-cloudtrail`
  - Data Location Changes: Existing customers upgrading from previously shared to dedicated resources will have
    AWS Config and AWS CloudTrail data in different S3 buckets. Established customer workflows and tools may need updates
    to access data from new bucket locations.
  - AWS CloudTrail will continue to stay in the same existing bucket, but AWS Config data will be in a new S3 bucket
    created by AWS Control Tower.
  - Customers can set-up cross-bucket replication if they wish to centralize different logs to a single bucket.
    Please see [S3 documentation](../../../AmazonS3/latest/userguide/replication.md "../../../AmazonS3/latest/userguide/replication.md") for more information.

- **AWS Config integration on landing zone version 4.0:** When migrating to landing zone 4.0 with AWS Config integration enabled, customers would see the following changes -
  1.  The existing Audit account is registered as a delegated admin for AWS Config.
  2.  Service-Linked Config Aggregator is deployed into the Audit account (AWS Config central aggregator account for new
      customers and Audit account for existing customers). The new aggregator can aggregate data from any AWS Config Recorder
      in the organization, including non-Control Tower managed accounts.
  3.  Existing aggregators will be deleted - Organization aggregator in management account (`aws-controltower-ConfigAggregatorForOrganizations`)
      and account aggregator in Audit account (`aws-controltower-GuardRailsComplianceAggregator`) will be deleted.
  4.  Controls associated with the deleted aggregators will be automatically removed. Additionally, since AWS Config Rules
      and Configuration Aggregator will be service-linked resources, service control policy protection will no longer
      be required.
      1. [Disallow Changes to Tags Created by AWS Control Tower for AWS Config Resources](../controlreference/mandatory-controls.md#cloudwatch-disallow-config-changes "../controlreference/mandatory-controls.md#cloudwatch-disallow-config-changes")
      2. [Disallow Deletion of AWS Config Aggregation Authorizations Created by AWS Control Tower](../controlreference/mandatory-controls.md#config-aggregation-authorization-policy "../controlreference/mandatory-controls.md#config-aggregation-authorization-policy")
      3. [Disallow Changes to AWS Config Rules Set Up by AWS Control Tower](../controlreference/mandatory-controls.md#config-rule-disallow-changes "../controlreference/mandatory-controls.md#config-rule-disallow-changes")

- **New `ConfigBaseline` baseline:** There is now a separate `ConfigBaseline`
  at the OU level for detective controls support without requiring the comprehensive `AWSControlTowerBaseline`.
  See list of [baseline types at the OU level](types-of-baselines.md#ou-baseline-types "types-of-baselines.md#ou-baseline-types") for more information. For existing customers that are using the default landing zone,
  all service integrations are now optional, with the caveat of dependency requirements outlined in
  [Key changes](key-changes-lz-v4.md "key-changes-lz-v4.md").
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
