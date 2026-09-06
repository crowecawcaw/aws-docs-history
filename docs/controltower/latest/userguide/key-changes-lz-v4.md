

# Key changes
<a name="key-changes-lz-v4"></a>

**Note**  
 The definition of “registered” and “enrolled” have shifted with this new version of AWS Control Tower. When your account/OU has any AWS Control Tower resource enabled on it (e.g. control or baseline), it will be considered a governed resource. The definition will no longer be driven by the presence of the `AWSControlTowerBaseline` baseline. 
 Service-Linked Roles are retained across all landing zone versions and are no longer deleted when OUs become "unregistered" 
 Service-Linked Roles can only be deleted manually by customers after landing zone decommissioning 

**Upgrading from version 3.3 or earlier to version 4.0**  
 Do not disable service integrations (AWS Config, SecurityRoles) as part of the version upgrade. In landing zone versions 3.3 and earlier, AWS Config and SecurityRoles were always enabled implicitly. Version 4.0 surfaces these integrations as configurable options for the first time. After successfully upgrading to version 4.0, you can disable service integrations as desired. 
+  **Pre-requisite for Landing Zone 4.0: **When upgrading to version 4.0 via API, ensure the `AWSControlTowerCloudTrailRole` service role uses the new managed policy `AWSControlTowerCloudTrailRolePolicy` instead of the existing inline policy. Detach the current inline policy and attach the new managed policy as described in the [documentation](https://docs.aws.amazon.com/controltower/latest/userguide/access-control-managing-permissions.html#AWSControlTowerCloudTrailRolePolicy). 
+  **Optional Manifest:** Manifest field in the landing zone API is now optional. Customers can create Landing Zones without any service integrations. There is no impact for existing customers that are already using the manifest field. 
+  **Optional Organization Structure:** AWS Control Tower no longer enforces or manages the Security OU creation so customers can define and manage their own organization structure. However, AWS Control Tower will require all accounts that are configured for each AWS service integration to be under the same parent OU. There is no impact for customers that have already set-up the AWS Control Tower and have the Security OU. AWS Control Tower automatically deploys the resources and controls necessary to manage service integration accounts in the Security OU. For example, when AWS Config integration is enabled, AWS Config recording is enabled in all [service integration accounts](special-accounts.md). The AWS Control Tower Baseline and the AWS Config Baseline are not applicable to the Security OU and the service integration accounts. To change service integrations, update landing zone settings. 
**Note**  
 The organization structure setup for AWS Control Tower landing zone 4.0 has changed from previous landing zone versions. AWS Control Tower will no longer create the designated Security OU. The OU with the service integration accounts will be the designated Security OU. 
 If member accounts move into the OU where the accounts for each integration reside, enabled controls on that OU are drifted regardless of whether auto-enrollment is turned on or off. 

   **Baseline status for the Security OU:** The AWS Control Tower Baseline and the AWS Config Baseline cannot be applied to the Security OU. The Security OU displays a baseline status of "Not Applicable" for these baselines. This status is expected. The BackupBaseline can be applied to the Security OU. 

   AWS Control Tower manages service integration accounts through the landing zone, not through OU-level baselines. If a service integration account displays a baseline status of "Not Enabled" and the associated service integration is disabled, AWS Control Tower no longer manages that account. 

   Accounts in the Security OU that are not designated as service integration accounts do not receive baseline resources. To govern these accounts, move them to a managed OU and extend governance. 

   **IAM Identity Center permission sets for service integration accounts:** AWS Control Tower provisions IAM Identity Center permission sets for the Logging account and the SecurityRoles account. AWS Control Tower does not provision permission sets for the Config account or the Backup account. To access the Config or Backup account through IAM Identity Center, create permission sets manually using the IAM Identity Center resources that AWS Control Tower deployed. 
+  **Drift Notifications:** AWS Control Tower will stop sending drift notifications to the SNS topic for all customers on landing zone 4.0 and later, and will start sending drift notifications to EventBridge in the management account instead. To receive these notifications, create an EventBridge rule in the management account. Then configure a target, such as an SNS topic or a Lambda function. For more information about drift notifications and sample EventBridge events, see [Types of governance drift](https://docs.aws.amazon.com/controltower/latest/userguide/governance-drift.html). 
+  **Optional Service Integrations: **You now have the ability to enable/disable all AWS Control Tower integrations including AWS Config, AWS CloudTrail, SecurityRoles, and AWS Backup. These integrations also now have optionally required `enabled` flags in the API. The baselines that may apply to your landing zone or shared accounts now have dependencies on one another. The Integrations specific dependencies are: 
  + Enablement:
    +  `CentralSecurityRolesBaseline` → requires `CentralConfigBaseline` to be enabled 
    +  `IdentityCenterBaseline` → requires `CentralSecurityRolesBaseline` to be enabled 
    +  `BackupCentralVaultBaseline` → requires `CentralSecurityRolesBaseline` to be enabled 
    +  `BackupAdminBaseline` → requires `CentralSecurityRolesBaseline` to be enabled 
    +  `LogArchiveBaseline` → independent (no dependencies) 
    +  `CentralConfigBaseline` → independent (no dependencies) 
  + Disablement: 
    +  `CentralConfigBaseline` can only be disabled if `CentralSecurityRolesBaseline`, `IdentityCenterBaseline`, `BackupAdminBaseline` and `BackupCentralVaultBaseline` baselines are disabled first. 
    +  `CentralSecurityRolesBaseline` can only be disabled if `IdentityCenterBaseline`, `BackupAdminBaseline` and `BackupCentralVaultBaseline` baselines are disabled first. 
    +  `IdentityCenterBaseline` can be disabled independently. 
    +  `BackupAdminBaseline` and `BackupCentralVaultBaseline` baselines can be disabled independently 
    +  `LogArchiveBaseline` can be disabled independently 
**Scope of AWS Config service integration enablement**  
 Enabling the AWS Config service integration at the landing zone level deploys Config recording resources to service integration accounts only. To deploy AWS Config resources (Config Recorder, Delivery Channel) to member accounts, enable the AWS Config baseline on each managed OU individually.   
 Enabling the Config integration at the landing zone level is a prerequisite for enabling the Config baseline on OUs. The landing zone-level setting alone does not deploy Config resources to member accounts.   
 For more information, see [AWS Config Updates](config-updates-v4.md). 
**CentralizedLogging behavior change in version 4.0**  
 In landing zone versions 3.3 and earlier, disabling CentralizedLogging toggled the Organization CloudTrail to off and retained all deployed resources. In version 4.0, disabling CentralizedLogging deletes all associated resources from the logging account. These resources include the Config Recorder, Delivery Channel, and CloudTrail-related stack instances. After disablement, AWS Control Tower no longer manages the logging account.   
 To restore management of the logging account, re-enable CentralizedLogging or move the account to a managed OU and extend governance. 