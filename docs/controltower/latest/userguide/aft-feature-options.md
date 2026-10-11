

# Enable feature options
<a name="aft-feature-options"></a>

AFT offers feature options based on best practices. You can opt-in to these features, by means of feature flags, during AFT deployment. Refer to [Provision a new account with AFT](aft-provision-account.md) for more information about AFT input configuration parameters.

These features are not enabled by default. You must explicitly enable each one in your environment.

**Topics**
+ [AWS CloudTrail data events](#cloudtrail-data-event-option)
+ [AWS Enterprise Support plan](#enterprise-support-option)
+ [Delete the AWS default VPC](#delete-default-vpc-option)
+ [Export Terraform plan output to Amazon S3](#plan-output-export-option)

## AWS CloudTrail data events
<a name="cloudtrail-data-event-option"></a>

When enabled, the AWS CloudTrail data events option configures these capabilities.
+ Creates an Organization Trail in the AWS Control Tower management account, for CloudTrail
+ Turns on logging for Amazon S3 and Lambda data events
+ Encrypts and exports all the CloudTrail data events to an `aws-aft-logs-*` S3 bucket in the AWS Control Tower Log Archive account, with AWS KMS encryption
+ Turns on the **Log file validation** setting

To enable this option, set the following feature flag to **True** in your AFT deployment input configuration.

```
aft_feature_cloudtrail_data_events
```

**Prerequisite**

Before you enable this feature option, be sure that trusted access for AWS CloudTrail is enabled in your organization. 

**To check the status of trusted access for CloudTrail :**

1. Navigate to the AWS Organizations console.

1. Choose **Services > CloudTrail**.

1. Then select **Enable trusted access** in the upper right, if needed.

You may receive a warning message that advises you to use the AWS CloudTrail console, but in this case, disregard the warning. AFT creates the trail as part of enabling this feature option, after you allow trusted access. If trusted access is not enabled, you will receive an error message when AFT attempts to create your trail for data events.

**Note**  
This setting works at the organization level. Enabling this setting affects all accounts in AWS Organizations, whether they are managed by AFT or not. All buckets in the AWS Control Tower Log Archive account at the time of enabling are excluded from Amazon S3 data events. Refer to [the AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) to learn more about CloudTrail.

## AWS Enterprise Support plan
<a name="enterprise-support-option"></a>

When this option is enabled, the AFT pipeline turns on the AWS Enterprise Support plan for accounts provisioned by AFT.

AWS accounts by default come with the AWS Basic Support plan enabled. AFT provides automated enrollment into the enterprise support level, for accounts that AFT provisions. The provisioning process opens a support ticket for the account, requesting it to be added to the AWS Enterprise Support plan.

To enable the Enterprise Support option, set the following feature flag to **True** in your AFT deployment input configuration.

```
aft_feature_enterprise_support=false
```

Refer to [Compare AWS Support Plans](https://aws.amazon.com/premiumsupport/plans/) to learn more about AWS Support Plans.

**Note**  
To allow this feature to operate, you must enroll the payer account into the Enterprise Support plan.

## Delete the AWS default VPC
<a name="delete-default-vpc-option"></a>

 When you enable this option, AFT deletes all AWS default VPCs in the AFT management account and in all AWS Regions, even if haven't deployed AWS Control Tower resources in those AWS Regions. 

 AFT doesn't delete AWS default VPCs automatically for any AWS Control Tower accounts that AFT provisions or for existing AWS accounts that you enroll in AWS Control Tower through AFT. 

New AWS accounts are created with a VPC set up in each AWS Region, by default. Your enterprise may have standard practices for creating VPCs, which require you to delete the AWS default VPC and avoid enabling it, especially for the AFT management account. 

To enable this option, set the following feature flag to **True** in your AFT deployment input configuration.

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

Refer to [Default VPC and default subnets](https://docs.aws.amazon.com/vpc/latest/userguide/default-vpc.html) to learn more about default VPCs.

**Note**  
Default VPC deletion is best-effort per AWS Region. If a Region's endpoint is temporarily unreachable, AFT skips that Region and continues deleting default VPCs in the remaining Regions. Skipped Regions are retried on the next customization pipeline run. To check whether any Regions were skipped, search the `aft-delete-default-vpc` Lambda function logs for the message `Skipping default VPC deletion in region`.

## Export Terraform plan output to Amazon S3
<a name="plan-output-export-option"></a>

When you deploy AFT, AFT creates a dedicated, encrypted plan-output Amazon S3 bucket in the AFT management account. AFT creates this bucket on every AFT deployment, regardless of your Terraform distribution. The bucket stores the JSON output of plan-only customization runs. For more information about plan-only runs, see [Re-invoke customizations](aft-account-customization-options.md#aft-re-invoke-customizations).

The plan-output bucket has the following properties:
+ Encrypted with the AFT AWS KMS key
+ Versioning enabled
+ Public access blocked
+ Write access limited to the AFT customizations build role

Whether AFT exports the plan JSON to this bucket depends on your Terraform distribution:
+ Community Edition (open source): AFT exports the plan JSON to the bucket by default on every plan-only run.
+ HCP Terraform (Terraform Cloud) and Terraform Enterprise: You can view the plan results in the HCP Terraform run UI. To also export the plan JSON to the bucket, set the following variable to `true` in your AFT deployment input configuration.

```
aft_plan_output_export_enabled = true
```

AFT retains exported plans for 30 days by default. To change the retention duration, set the `aft_plan_output_retention_days` variable in your AFT deployment input configuration.

```
aft_plan_output_retention_days = 30
```

**Note**  
The `aft_plan_output_export_enabled` variable affects only the HCP Terraform (Terraform Cloud) and Terraform Enterprise distributions. On the Community Edition (open source) distribution, AFT exports the plan JSON by default, and this variable has no effect.