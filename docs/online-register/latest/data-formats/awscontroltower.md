

# Data retrieval APIs for AWS Control Tower
<a name="awscontroltower"></a>

AWS Control Tower provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="controltower-DescribeAccountFactoryConfig"></a>[DescribeAccountFactoryConfig](https://docs.aws.amazon.com/controltower/latest/userguide/account-factory.html) | Describe the current account factory configuration | Read | 
| <a name="controltower-DescribeCoreService"></a>[DescribeCoreService](https://docs.aws.amazon.com/controltower/latest/userguide/how-control-tower-works.html#what-shared) | Describe resources managed by core accounts in AWS Control Tower | Read | 
| <a name="controltower-DescribeGuardrail"></a>[DescribeGuardrail](https://docs.aws.amazon.com/controltower/latest/userguide/controls.html) | Describe a guardrail | Read | 
| <a name="controltower-DescribeGuardrailForTarget"></a>[DescribeGuardrailForTarget](https://docs.aws.amazon.com/controltower/latest/userguide/controls.html) | Describe a guardrail for a organizational unit | Read | 
| <a name="controltower-DescribeLandingZoneConfiguration"></a>[DescribeLandingZoneConfiguration](https://docs.aws.amazon.com/controltower/latest/userguide/step-two.html) | Describe the current Landing Zone configuration | Read | 
| <a name="controltower-DescribeManagedAccount"></a>[DescribeManagedAccount](https://docs.aws.amazon.com/controltower/latest/userguide/account-factory.html) | Describe an account created through account factory | Read | 
| <a name="controltower-DescribeManagedOrganizationalUnit"></a>[DescribeManagedOrganizationalUnit](https://docs.aws.amazon.com/controltower/latest/userguide/organizations.html) | Describe an AWS Organizations organizational unit managed by AWS Control Tower | Read | 
| <a name="controltower-DescribeRegisterOrganizationalUnitOperation"></a>[DescribeRegisterOrganizationalUnitOperation](https://docs.aws.amazon.com/controltower/latest/userguide/about-extending-governance.html) | Describe a Register Organizational Unit Operation  | Read | 
| <a name="controltower-DescribeSingleSignOn"></a>[DescribeSingleSignOn](https://docs.aws.amazon.com/controltower/latest/userguide/sso.html) | Describe the current AWS Control Tower IAM Identity Center configuration | Read | 
| <a name="controltower-GetAccountInfo"></a>[GetAccountInfo](https://docs.aws.amazon.com/controltower/latest/userguide/accounts.html) | Describe an account email and validate that it exists | Read | 
| <a name="controltower-GetAvailableUpdates"></a>[GetAvailableUpdates](https://docs.aws.amazon.com/controltower/latest/userguide/configuration-updates.html) | List available updates for the current AWS Control Tower deployment | Read | 
| <a name="controltower-GetBaseline"></a>[GetBaseline](https://docs.aws.amazon.com/controltower/latest/APIReference/API_GetBaseline.html) | Get Baseline details | Read | 
| <a name="controltower-GetBaselineOperation"></a>[GetBaselineOperation](https://docs.aws.amazon.com/controltower/latest/APIReference/API_GetBaselineOperation.html) | Get the current status of a particular Baseline operation | Read | 
| <a name="controltower-GetControlOperation"></a>[GetControlOperation](https://docs.aws.amazon.com/controltower/latest/APIReference/API_GetControlOperation.html) | Get the current status of a particular EnabledControl or DisableControl operation | Read | 
| <a name="controltower-GetEnabledBaseline"></a>[GetEnabledBaseline](https://docs.aws.amazon.com/controltower/latest/APIReference/API_GetEnabledBaseline.html) | Get an enabled Baseline | Read | 
| <a name="controltower-GetEnabledControl"></a>[GetEnabledControl](https://docs.aws.amazon.com/controltower/latest/APIReference/API_GetEnabledControl.html) | Get an enabled control from an organizational unit | Read | 
| <a name="controltower-GetGuardrailComplianceStatus"></a>[GetGuardrailComplianceStatus](https://docs.aws.amazon.com/controltower/latest/userguide/controls.html) | Get the current compliance status of a guardrail | Read | 
| <a name="controltower-GetHomeRegion"></a>[GetHomeRegion](https://docs.aws.amazon.com/controltower/latest/userguide/how-control-tower-works.html#region-how) | Get the home region of the AWS Control Tower setup | Read | 
| <a name="controltower-GetLandingZone"></a>[GetLandingZone](https://docs.aws.amazon.com/controltower/latest/APIReference/API_GetLandingZone.html) | Get the current status of the landing zone setup | Read | 
| <a name="controltower-GetLandingZoneDriftStatus"></a>[GetLandingZoneDriftStatus](https://docs.aws.amazon.com/controltower/latest/userguide/drift.html) | Get the current landing zone drift status | Read | 
| <a name="controltower-GetLandingZoneOperation"></a>[GetLandingZoneOperation](https://docs.aws.amazon.com/controltower/latest/APIReference/API_GetLandingZoneOperation.html) | Get the current status of a particular landing zone operation | Read | 
| <a name="controltower-GetLandingZoneStatus"></a>[GetLandingZoneStatus](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-with-control-tower.html#step-two) | Get the current status of the landing zone setup | Read | 
| <a name="controltower-ListBaselines"></a>[ListBaselines](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ListBaselines.html) | List Baselines | List | 
| <a name="controltower-ListControlOperations"></a>[ListControlOperations](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ListControlOperations.html) | List all control operations | List | 
| <a name="controltower-ListDirectoryGroups"></a>[ListDirectoryGroups](https://docs.aws.amazon.com/controltower/latest/userguide/sso.html) | List the current directory groups available through IAM Identity Center | List | 
| <a name="controltower-ListDriftDetails"></a>[ListDriftDetails](https://docs.aws.amazon.com/controltower/latest/userguide/drift.html) | List occurrences of drift in AWS Control Tower | Read | 
| <a name="controltower-ListEnabledBaselines"></a>[ListEnabledBaselines](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ListEnabledBaselines.html) | List enabled Baselines | List | 
| <a name="controltower-ListEnabledControls"></a>[ListEnabledControls](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ListEnabledControls.html) | List all enabled controls in a specified organizational unit | List | 
| <a name="controltower-ListEnabledGuardrails"></a>[ListEnabledGuardrails](https://docs.aws.amazon.com/controltower/latest/userguide/controls.html) | List currently enabled guardrails | List | 
| <a name="controltower-ListExtendGovernancePrecheckDetails"></a>[ListExtendGovernancePrecheckDetails](https://docs.aws.amazon.com/controltower/latest/userguide/about-extending-governance.html) | List Precheck details for an Organizational Unit  | List | 
| <a name="controltower-ListExternalConfigRuleCompliance"></a>[ListExternalConfigRuleCompliance](https://docs.aws.amazon.com/controltower/latest/userguide/review-compliance.html) | List the compliance of external AWS Config rules | Read | 
| <a name="controltower-ListGuardrailViolations"></a>[ListGuardrailViolations](https://docs.aws.amazon.com/controltower/latest/userguide/controls.html) | List existing guardrail violations | List | 
| <a name="controltower-ListGuardrails"></a>[ListGuardrails](https://docs.aws.amazon.com/controltower/latest/userguide/controls.html) | List all available guardrails | List | 
| <a name="controltower-ListGuardrailsForTarget"></a>[ListGuardrailsForTarget](https://docs.aws.amazon.com/controltower/latest/userguide/controls.html) | List guardrails and their current state for a organizational unit | List | 
| <a name="controltower-ListLandingZoneOperations"></a>[ListLandingZoneOperations](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ListLandingZoneOperations.html) | List all landing zone operations | List | 
| <a name="controltower-ListLandingZones"></a>[ListLandingZones](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ListLandingZones.html) | List all landing zones | List | 
| <a name="controltower-ListManagedAccounts"></a>[ListManagedAccounts](https://docs.aws.amazon.com/controltower/latest/userguide/account-factory.html) | List accounts managed through AWS Control Tower | List | 
| <a name="controltower-ListManagedAccountsForGuardrail"></a>[ListManagedAccountsForGuardrail](https://docs.aws.amazon.com/controltower/latest/userguide/account-factory.html) | List managed accounts with a specified guardrail applied | List | 
| <a name="controltower-ListManagedAccountsForParent"></a>[ListManagedAccountsForParent](https://docs.aws.amazon.com/controltower/latest/userguide/account-factory.html) | List managed accounts under an organizational unit | List | 
| <a name="controltower-ListManagedOrganizationalUnits"></a>[ListManagedOrganizationalUnits](https://docs.aws.amazon.com/controltower/latest/userguide/organizations.html) | List organizational units managed by AWS Control Tower | List | 
| <a name="controltower-ListManagedOrganizationalUnitsForGuardrail"></a>[ListManagedOrganizationalUnitsForGuardrail](https://docs.aws.amazon.com/controltower/latest/userguide/organizations.html) | List managed organizational units that have a specified guardrail applied | List | 
| <a name="controltower-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/controltower/latest/APIReference/API_ListTagsForResource.html) | List the tags for a resource | Read | 
| <a name="controltower-PerformPreLaunchChecks"></a>[PerformPreLaunchChecks](https://docs.aws.amazon.com/controltower/latest/userguide/getting-started-prereqs.html) | Perform validations in an account | Read | 