

# Data retrieval APIs for Amazon GuardDuty
<a name="amazonguardduty"></a>

Amazon GuardDuty provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="guardduty-DescribeMalwareScans"></a>[DescribeMalwareScans](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DescribeMalwareScans.html) | Retrieve details about malware scans | Read | 
| <a name="guardduty-DescribeOrganizationConfiguration"></a>[DescribeOrganizationConfiguration](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DescribeOrganizationConfiguration.html) | Retrieve details about the delegated administrator associated with a GuardDuty detector | Read | 
| <a name="guardduty-DescribePublishingDestination"></a>[DescribePublishingDestination](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DescribePublishingDestination.html) | Retrieve details about a publishing destination | Read | 
| <a name="guardduty-GetAdministratorAccount"></a>[GetAdministratorAccount](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetAdministratorAccount.html) | Retrieve details of the GuardDuty administrator account associated with a member account | Read | 
| <a name="guardduty-GetCoverageStatistics"></a>[GetCoverageStatistics](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetCoverageStatistics.html) | List Amazon GuardDuty coverage statistics for the specified GuardDuty account in a Region | Read | 
| <a name="guardduty-GetCustomDetectionRule"></a>[GetCustomDetectionRule](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetCustomDetectionRule.html) | Retrieve a GuardDuty custom detection rule | Read | 
| <a name="guardduty-GetCustomDetectionRuleAssociation"></a>[GetCustomDetectionRuleAssociation](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetCustomDetectionRuleAssociation.html) | Retrieve a GuardDuty custom detection rule association | Read | 
| <a name="guardduty-GetCustomDetectionRuleOrgConfiguration"></a>[GetCustomDetectionRuleOrgConfiguration](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetCustomDetectionRuleOrgConfiguration.html) | Retrieve the organization configuration for a GuardDuty custom detection rule | Read | 
| <a name="guardduty-GetDetector"></a>[GetDetector](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetDetector.html) | Retrieve GuardDuty detectors | Read | 
| <a name="guardduty-GetFilter"></a>[GetFilter](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetFilter.html) | Retrieve GuardDuty filters | Read | 
| <a name="guardduty-GetFindings"></a>[GetFindings](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetFindings.html) | Retrieve GuardDuty findings | Read | 
| <a name="guardduty-GetFindingsStatistics"></a>[GetFindingsStatistics](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetFindingsStatistics.html) | Retrieve a list of GuardDuty finding statistics | Read | 
| <a name="guardduty-GetIPSet"></a>[GetIPSet](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetIPSet.html) | Retrieve GuardDuty IPSets | Read | 
| <a name="guardduty-GetInvestigation"></a>[GetInvestigation](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetInvestigation.html) | Retrieve a GuardDuty investigation | Read | 
| <a name="guardduty-GetInvitationsCount"></a>[GetInvitationsCount](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetInvitationsCount.html) | Retrieve the count of all GuardDuty invitations sent to a specified account, which does not include the accepted invitation | Read | 
| <a name="guardduty-GetMalwareProtectionPlan"></a>[GetMalwareProtectionPlan](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetMalwareProtectionPlan.html) | Retrieve a Malware Protection plan details | Read | 
| <a name="guardduty-GetMalwareScan"></a>[GetMalwareScan](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetMalwareScan.html) | Retrieve a malware scan's details | Read | 
| <a name="guardduty-GetMalwareScanSettings"></a>[GetMalwareScanSettings](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetMalwareScanSettings.html) | Retrieve the malware scan settings | Read | 
| <a name="guardduty-GetMasterAccount"></a>[GetMasterAccount](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetMasterAccount.html) | Retrieve details of the GuardDuty administrator account associated with a member account | Read | 
| <a name="guardduty-GetMemberDetectors"></a>[GetMemberDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetMemberDetectors.html) | Describe which data sources are enabled for member accounts detectors | Read | 
| <a name="guardduty-GetMembers"></a>[GetMembers](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetMembers.html) | Retrieve the member accounts associated with an administrator account | Read | 
| <a name="guardduty-GetOrganizationStatistics"></a>[GetOrganizationStatistics](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetOrganizationStatistics.html) | Retrieve GuardDuty protection plan coverage statistics for member accounts in a Region | Read | 
| <a name="guardduty-GetRemainingFreeTrialDays"></a>[GetRemainingFreeTrialDays](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetRemainingFreeTrialDays.html) | Provide the number of days left for each data source used in the free trial period | Read | 
| <a name="guardduty-GetThreatEntitySet"></a>[GetThreatEntitySet](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetThreatEntitySet.html) | Retrieve GuardDuty ThreatEntitySets | Read | 
| <a name="guardduty-GetThreatIntelSet"></a>[GetThreatIntelSet](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetThreatIntelSet.html) | Retrieve GuardDuty ThreatIntelSets | Read | 
| <a name="guardduty-GetTrustedEntitySet"></a>[GetTrustedEntitySet](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetTrustedEntitySet.html) | Retrieve GuardDuty TrustedEntitySets | Read | 
| <a name="guardduty-GetUsageStatistics"></a>[GetUsageStatistics](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetUsageStatistics.html) | List Amazon GuardDuty usage statistics over the last 30 days for the specified detector ID | Read | 
| <a name="guardduty-ListCoverage"></a>[ListCoverage](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListCoverage.html) | List all the resource details for a given account in a Region | List | 
| <a name="guardduty-ListCustomDetectionRuleAssociations"></a>[ListCustomDetectionRuleAssociations](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListCustomDetectionRuleAssociations.html) | Retrieve a list of GuardDuty custom detection rule associations | List | 
| <a name="guardduty-ListCustomDetectionRuleOrgConfigurations"></a>[ListCustomDetectionRuleOrgConfigurations](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListCustomDetectionRuleOrgConfigurations.html) | Retrieve a list of organization configurations for GuardDuty custom detection rules | List | 
| <a name="guardduty-ListCustomDetectionRules"></a>[ListCustomDetectionRules](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListCustomDetectionRules.html) | Retrieve a list of GuardDuty custom detection rules | List | 
| <a name="guardduty-ListDetectors"></a>[ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) | Retrieve a list of GuardDuty detectors | List | 
| <a name="guardduty-ListFilters"></a>[ListFilters](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListFilters.html) | Retrieve a list of GuardDuty filters | List | 
| <a name="guardduty-ListFindings"></a>[ListFindings](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListFindings.html) | Retrieve a list of GuardDuty findings | List | 
| <a name="guardduty-ListIPSets"></a>[ListIPSets](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListIPSets.html) | Retrieve a list of GuardDuty IPSets | List | 
| <a name="guardduty-ListInvestigations"></a>[ListInvestigations](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListInvestigations.html) | Retrieve a list of GuardDuty investigations | List | 
| <a name="guardduty-ListInvitations"></a>[ListInvitations](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListInvitations.html) | Retrieve a list of all of the GuardDuty membership invitations that were sent to an AWS account | List | 
| <a name="guardduty-ListMalwareProtectionPlans"></a>[ListMalwareProtectionPlans](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListMalwareProtectionPlans.html) | Retrieve a list of Malware Protection plans | List | 
| <a name="guardduty-ListMalwareScans"></a>[ListMalwareScans](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListMalwareScans.html) | Retrieve a list of malware scans | List | 
| <a name="guardduty-ListMembers"></a>[ListMembers](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListMembers.html) | Retrieve a list of GuardDuty member accounts associated with an administrator account | List | 
| <a name="guardduty-ListOrganizationAdminAccounts"></a>[ListOrganizationAdminAccounts](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListOrganizationAdminAccounts.html) | List details about the organization delegated administrator for GuardDuty | List | 
| <a name="guardduty-ListPublishingDestinations"></a>[ListPublishingDestinations](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListPublishingDestinations.html) | Retrieve a list of publishing destinations | List | 
| <a name="guardduty-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListTagsForResource.html) | Retrieve a list of tags associated with a GuardDuty resource | Read | 
| <a name="guardduty-ListThreatEntitySets"></a>[ListThreatEntitySets](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListThreatEntitySets.html) | Retrieve a list of GuardDuty ThreatEntitySets | List | 
| <a name="guardduty-ListThreatIntelSets"></a>[ListThreatIntelSets](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListThreatIntelSets.html) | Retrieve a list of GuardDuty ThreatIntelSets | List | 
| <a name="guardduty-ListTrustedEntitySets"></a>[ListTrustedEntitySets](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListTrustedEntitySets.html) | Retrieve a list of GuardDuty TrustedEntitySets | List | 