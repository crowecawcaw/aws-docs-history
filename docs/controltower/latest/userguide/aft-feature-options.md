# Enable feature options

AFT offers feature options based on best practices. You can opt-in to these features, by
means of feature flags, during AFT deployment. Refer to [Provision a new account with AFT](aft-provision-account.md "aft-provision-account.md") for more
information about AFT input configuration parameters.

These features are not enabled by default. You must explicitly enable each one in your
environment.

###### Topics

- [AWS CloudTrail data events](#cloudtrail-data-event-option "#cloudtrail-data-event-option")
- [AWS Enterprise Support plan](#enterprise-support-option "#enterprise-support-option")
- [Delete the AWS default VPC](#delete-default-vpc-option "#delete-default-vpc-option")

## AWS CloudTrail data events

When enabled, the AWS CloudTrail data events option configures these capabilities.

- Creates an Organization Trail in the AWS Control Tower management account, for
  CloudTrail
- Turns on logging for Amazon S3 and Lambda data events
- Encrypts and exports all the CloudTrail data events to an
  `aws-aft-logs-*` S3 bucket in the AWS Control Tower Log Archive account,
  with AWS KMS encryption
- Turns on the **Log file validation** setting

To enable this option, set the following feature flag to **True** in
your AFT deployment input configuration.

```
aft_feature_cloudtrail_data_events
```

**Prerequisite**

Before you enable this feature option, be sure that trusted access for AWS CloudTrail is
enabled in your organization.

###### To check the status of trusted access for CloudTrail :

1. Navigate to the AWS Organizations console.
2. Choose **Services > CloudTrail**.
3. Then select **Enable trusted access** in the upper right, if
   needed.

You may receive a warning message that advises you to use the AWS CloudTrail console, but in
this case, disregard the warning. AFT creates the trail as part of enabling this feature
option, after you allow trusted access. If trusted access is not enabled, you will
receive an error message when AFT attempts to create your trail for data events.

###### Note

This setting works at the organization level. Enabling this setting affects all
accounts in AWS Organizations, whether they are managed by AFT or not. All buckets in the
AWS Control Tower Log Archive account at the time of enabling are excluded from Amazon S3 data
events. Refer to [the AWS CloudTrail
User Guide](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md") to learn more about CloudTrail.

## AWS Enterprise Support plan

When this option is enabled, the AFT pipeline turns on the AWS Enterprise Support
plan for accounts provisioned by AFT.

AWS accounts by default come with the AWS Basic Support plan enabled. AFT provides
automated enrollment into the enterprise support level, for accounts that AFT
provisions. The provisioning process opens a support ticket for the account, requesting
it to be added to the AWS Enterprise Support plan.

To enable the Enterprise Support option, set the following feature flag to
**True** in your AFT deployment input configuration.

```
aft_feature_enterprise_support=false
```

Refer to [Compare AWS Support
Plans](https://aws.amazon.com/premiumsupport/plans/ "https://aws.amazon.com/premiumsupport/plans/") to learn more about AWS Support Plans.

###### Note

To allow this feature to operate, you must enroll the payer account into the
Enterprise Support plan.

## Delete the AWS default VPC

When you enable this option, AFT deletes all AWS default VPCs in the AFT management
account and in all AWS Regions, even if haven't deployed AWS Control Tower resources in those
AWS Regions.

AFT doesn't delete AWS default VPCs automatically for any AWS Control Tower accounts that
AFT provisions or for existing AWS accounts that you enroll in AWS Control Tower through AFT.

New AWS accounts are created with a VPC set up in each AWS Region, by default.
Your enterprise may have standard practices for creating VPCs, which require you to
delete the AWS default VPC and avoid enabling it, especially for the AFT management
account.

To enable this option, set the following feature flag to **True** in
your AFT deployment input configuration.

```
aft_feature_delete_default_vpcs_enabled
```

The following is an example of a AFT deployment input configuration.

```
module "aft" {
  source = "github.com/aws-ia/terraform-aws-control_tower_account_factory"
  ct_management_account_id    = var.ct_management_account_id
  log_archive_account_id      = var.log_archive_account_id
  audit_account_id            = var.audit_account_id
  aft_management_account_id   = var.aft_management_account_id
  ct_home_region              = var.ct_home_region
  tf_backend_secondary_region = var.tf_backend_secondary_region

  vcs_provider                                  = "github"
  account_request_repo_name                     = "${var.github_username}/learn-terraform-aft-account-request"
  account_provisioning_customizations_repo_name = "${var.github_username}/learn-terraform-aft-account-provisioning-customizations"
  global_customizations_repo_name               = "${var.github_username}/learn-terraform-aft-global-customizations"
  account_customizations_repo_name              = "${var.github_username}/learn-terraform-aft-account-customizations"

  # Optional Feature Flags
  aft_feature_delete_default_vpcs_enabled = true
  aft_feature_cloudtrail_data_events      = false
  aft_feature_enterprise_support          = false
}
```

Refer to [Default VPC and default subnets](../../../vpc/latest/userguide/default-vpc.md "../../../vpc/latest/userguide/default-vpc.md") to learn more about default VPCs.
