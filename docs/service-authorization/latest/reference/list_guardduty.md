

# Actions, resources, and condition keys for Amazon GuardDuty
<a name="list_guardduty"></a>

Amazon GuardDuty (service prefix: `guardduty`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/guardduty/latest/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_managing_access.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/guardduty/guardduty.json) for this service.

**Topics**
+ [API operations defined by Amazon GuardDuty](#list_guardduty-operations)
+ [Actions defined by Amazon GuardDuty](#list_guardduty-actions-as-permissions)
+ [Resource types defined by Amazon GuardDuty](#list_guardduty-resources-for-iam-policies)
+ [Condition keys for Amazon GuardDuty](#list_guardduty-policy-keys)

## API operations defined by Amazon GuardDuty
<a name="list_guardduty-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_guardduty-actions-as-permissions).




- **   AcceptAdministratorInvitation  **
  - **IAM action:**  [guardduty:AcceptAdministratorInvitation](#list_guardduty-action-AcceptAdministratorInvitation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AcceptInvitation  **
  - **IAM action:**  [guardduty:AcceptInvitation](#list_guardduty-action-AcceptInvitation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ArchiveFindings  **
  - **IAM action:**  [guardduty:ArchiveFindings](#list_guardduty-action-ArchiveFindings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateCustomDetectionRuleAssociation  **
  - **IAM action:**  [guardduty:CreateCustomDetectionRuleAssociation](#list_guardduty-action-CreateCustomDetectionRuleAssociation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [guardduty:TagResource](#list_guardduty-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateCustomDetectionRuleOrgConfiguration  **
  - **IAM action:**  [guardduty:CreateCustomDetectionRuleOrgConfiguration](#list_guardduty-action-CreateCustomDetectionRuleOrgConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateDetector  **
  - **IAM action:**  [guardduty:CreateDetector](#list_guardduty-action-CreateDetector)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [guardduty:TagResource](#list_guardduty-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateFilter  **
  - **IAM action:**  [guardduty:CreateFilter](#list_guardduty-action-CreateFilter)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [guardduty:TagResource](#list_guardduty-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateIPSet  **
  - **IAM action:**  [guardduty:CreateIPSet](#list_guardduty-action-CreateIPSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [guardduty:TagResource](#list_guardduty-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateInvestigation  **
  - **IAM action:**  [guardduty:CreateInvestigation](#list_guardduty-action-CreateInvestigation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateMalwareProtectionPlan  **
  - **IAM action:**  [guardduty:CreateMalwareProtectionPlan](#list_guardduty-action-CreateMalwareProtectionPlan)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [guardduty:TagResource](#list_guardduty-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** malware-protection-plan.guardduty.amazonaws.com / **Access level:** Write

- **   CreateMembers  **
  - **IAM action:**  [guardduty:CreateMembers](#list_guardduty-action-CreateMembers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreatePublishingDestination  **
  - **IAM action:**  [guardduty:CreatePublishingDestination](#list_guardduty-action-CreatePublishingDestination)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [guardduty:TagResource](#list_guardduty-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateSampleFindings  **
  - **IAM action:**  [guardduty:CreateSampleFindings](#list_guardduty-action-CreateSampleFindings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateThreatEntitySet  **
  - **IAM action:**  [guardduty:CreateThreatEntitySet](#list_guardduty-action-CreateThreatEntitySet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [guardduty:TagResource](#list_guardduty-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateThreatIntelSet  **
  - **IAM action:**  [guardduty:CreateThreatIntelSet](#list_guardduty-action-CreateThreatIntelSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [guardduty:TagResource](#list_guardduty-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateTrustedEntitySet  **
  - **IAM action:**  [guardduty:CreateTrustedEntitySet](#list_guardduty-action-CreateTrustedEntitySet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [guardduty:TagResource](#list_guardduty-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeclineInvitations  **
  - **IAM action:**  [guardduty:DeclineInvitations](#list_guardduty-action-DeclineInvitations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCustomDetectionRuleAssociation  **
  - **IAM action:**  [guardduty:DeleteCustomDetectionRuleAssociation](#list_guardduty-action-DeleteCustomDetectionRuleAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCustomDetectionRuleOrgConfiguration  **
  - **IAM action:**  [guardduty:DeleteCustomDetectionRuleOrgConfiguration](#list_guardduty-action-DeleteCustomDetectionRuleOrgConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDetector  **
  - **IAM action:**  [guardduty:DeleteDetector](#list_guardduty-action-DeleteDetector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFilter  **
  - **IAM action:**  [guardduty:DeleteFilter](#list_guardduty-action-DeleteFilter) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteIPSet  **
  - **IAM action:**  [guardduty:DeleteIPSet](#list_guardduty-action-DeleteIPSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteInvitations  **
  - **IAM action:**  [guardduty:DeleteInvitations](#list_guardduty-action-DeleteInvitations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMalwareProtectionPlan  **
  - **IAM action:**  [guardduty:DeleteMalwareProtectionPlan](#list_guardduty-action-DeleteMalwareProtectionPlan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMembers  **
  - **IAM action:**  [guardduty:DeleteMembers](#list_guardduty-action-DeleteMembers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePublishingDestination  **
  - **IAM action:**  [guardduty:DeletePublishingDestination](#list_guardduty-action-DeletePublishingDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteThreatEntitySet  **
  - **IAM action:**  [guardduty:DeleteThreatEntitySet](#list_guardduty-action-DeleteThreatEntitySet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteThreatIntelSet  **
  - **IAM action:**  [guardduty:DeleteThreatIntelSet](#list_guardduty-action-DeleteThreatIntelSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTrustedEntitySet  **
  - **IAM action:**  [guardduty:DeleteTrustedEntitySet](#list_guardduty-action-DeleteTrustedEntitySet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeMalwareScans  **
  - **IAM action:**  [guardduty:DescribeMalwareScans](#list_guardduty-action-DescribeMalwareScans) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeOrganizationConfiguration  **
  - **IAM action:**  [guardduty:DescribeOrganizationConfiguration](#list_guardduty-action-DescribeOrganizationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribePublishingDestination  **
  - **IAM action:**  [guardduty:DescribePublishingDestination](#list_guardduty-action-DescribePublishingDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DisableOrganizationAdminAccount  **
  - **IAM action:**  [guardduty:DisableOrganizationAdminAccount](#list_guardduty-action-DisableOrganizationAdminAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateFromAdministratorAccount  **
  - **IAM action:**  [guardduty:DisassociateFromAdministratorAccount](#list_guardduty-action-DisassociateFromAdministratorAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateFromMasterAccount  **
  - **IAM action:**  [guardduty:DisassociateFromMasterAccount](#list_guardduty-action-DisassociateFromMasterAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateMembers  **
  - **IAM action:**  [guardduty:DisassociateMembers](#list_guardduty-action-DisassociateMembers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableOrganizationAdminAccount  **
  - **IAM action:**  [guardduty:EnableOrganizationAdminAccount](#list_guardduty-action-EnableOrganizationAdminAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAdministratorAccount  **
  - **IAM action:**  [guardduty:GetAdministratorAccount](#list_guardduty-action-GetAdministratorAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCoverageStatistics  **
  - **IAM action:**  [guardduty:GetCoverageStatistics](#list_guardduty-action-GetCoverageStatistics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCustomDetectionRule  **
  - **IAM action:**  [guardduty:GetCustomDetectionRule](#list_guardduty-action-GetCustomDetectionRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCustomDetectionRuleAssociation  **
  - **IAM action:**  [guardduty:GetCustomDetectionRuleAssociation](#list_guardduty-action-GetCustomDetectionRuleAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCustomDetectionRuleOrgConfiguration  **
  - **IAM action:**  [guardduty:GetCustomDetectionRuleOrgConfiguration](#list_guardduty-action-GetCustomDetectionRuleOrgConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDetector  **
  - **IAM action:**  [guardduty:GetDetector](#list_guardduty-action-GetDetector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFilter  **
  - **IAM action:**  [guardduty:GetFilter](#list_guardduty-action-GetFilter) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFindings  **
  - **IAM action:**  [guardduty:GetFindings](#list_guardduty-action-GetFindings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFindingsStatistics  **
  - **IAM action:**  [guardduty:GetFindingsStatistics](#list_guardduty-action-GetFindingsStatistics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIPSet  **
  - **IAM action:**  [guardduty:GetIPSet](#list_guardduty-action-GetIPSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetInvestigation  **
  - **IAM action:**  [guardduty:GetInvestigation](#list_guardduty-action-GetInvestigation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetInvitationsCount  **
  - **IAM action:**  [guardduty:GetInvitationsCount](#list_guardduty-action-GetInvitationsCount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMalwareProtectionPlan  **
  - **IAM action:**  [guardduty:GetMalwareProtectionPlan](#list_guardduty-action-GetMalwareProtectionPlan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMalwareScan  **
  - **IAM action:**  [guardduty:GetMalwareScan](#list_guardduty-action-GetMalwareScan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMalwareScanSettings  **
  - **IAM action:**  [guardduty:GetMalwareScanSettings](#list_guardduty-action-GetMalwareScanSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMasterAccount  **
  - **IAM action:**  [guardduty:GetMasterAccount](#list_guardduty-action-GetMasterAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMemberDetectors  **
  - **IAM action:**  [guardduty:GetMemberDetectors](#list_guardduty-action-GetMemberDetectors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMembers  **
  - **IAM action:**  [guardduty:GetMembers](#list_guardduty-action-GetMembers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOrganizationStatistics  **
  - **IAM action:**  [guardduty:GetOrganizationStatistics](#list_guardduty-action-GetOrganizationStatistics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRemainingFreeTrialDays  **
  - **IAM action:**  [guardduty:GetRemainingFreeTrialDays](#list_guardduty-action-GetRemainingFreeTrialDays) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetThreatEntitySet  **
  - **IAM action:**  [guardduty:GetThreatEntitySet](#list_guardduty-action-GetThreatEntitySet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetThreatIntelSet  **
  - **IAM action:**  [guardduty:GetThreatIntelSet](#list_guardduty-action-GetThreatIntelSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTrustedEntitySet  **
  - **IAM action:**  [guardduty:GetTrustedEntitySet](#list_guardduty-action-GetTrustedEntitySet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetUsageStatistics  **
  - **IAM action:**  [guardduty:GetUsageStatistics](#list_guardduty-action-GetUsageStatistics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   InviteMembers  **
  - **IAM action:**  [guardduty:InviteMembers](#list_guardduty-action-InviteMembers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListCoverage  **
  - **IAM action:**  [guardduty:ListCoverage](#list_guardduty-action-ListCoverage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCustomDetectionRuleAssociations  **
  - **IAM action:**  [guardduty:ListCustomDetectionRuleAssociations](#list_guardduty-action-ListCustomDetectionRuleAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCustomDetectionRuleOrgConfigurations  **
  - **IAM action:**  [guardduty:ListCustomDetectionRuleOrgConfigurations](#list_guardduty-action-ListCustomDetectionRuleOrgConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCustomDetectionRules  **
  - **IAM action:**  [guardduty:ListCustomDetectionRules](#list_guardduty-action-ListCustomDetectionRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDetectors  **
  - **IAM action:**  [guardduty:ListDetectors](#list_guardduty-action-ListDetectors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFilters  **
  - **IAM action:**  [guardduty:ListFilters](#list_guardduty-action-ListFilters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFindings  **
  - **IAM action:**  [guardduty:ListFindings](#list_guardduty-action-ListFindings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListIPSets  **
  - **IAM action:**  [guardduty:ListIPSets](#list_guardduty-action-ListIPSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListInvestigations  **
  - **IAM action:**  [guardduty:ListInvestigations](#list_guardduty-action-ListInvestigations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListInvitations  **
  - **IAM action:**  [guardduty:ListInvitations](#list_guardduty-action-ListInvitations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMalwareProtectionPlans  **
  - **IAM action:**  [guardduty:ListMalwareProtectionPlans](#list_guardduty-action-ListMalwareProtectionPlans) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMalwareScans  **
  - **IAM action:**  [guardduty:ListMalwareScans](#list_guardduty-action-ListMalwareScans) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMembers  **
  - **IAM action:**  [guardduty:ListMembers](#list_guardduty-action-ListMembers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListOrganizationAdminAccounts  **
  - **IAM action:**  [guardduty:ListOrganizationAdminAccounts](#list_guardduty-action-ListOrganizationAdminAccounts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPublishingDestinations  **
  - **IAM action:**  [guardduty:ListPublishingDestinations](#list_guardduty-action-ListPublishingDestinations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [guardduty:ListTagsForResource](#list_guardduty-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListThreatEntitySets  **
  - **IAM action:**  [guardduty:ListThreatEntitySets](#list_guardduty-action-ListThreatEntitySets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListThreatIntelSets  **
  - **IAM action:**  [guardduty:ListThreatIntelSets](#list_guardduty-action-ListThreatIntelSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTrustedEntitySets  **
  - **IAM action:**  [guardduty:ListTrustedEntitySets](#list_guardduty-action-ListTrustedEntitySets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   SendObjectMalwareScan  **
  - **IAM action:**  [guardduty:SendObjectMalwareScan](#list_guardduty-action-SendObjectMalwareScan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartMalwareScan  **
  - **IAM action:**  [guardduty:StartMalwareScan](#list_guardduty-action-StartMalwareScan)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** malware-protection.guardduty.amazonaws.com / **Access level:** Write

- **   StartMonitoringMembers  **
  - **IAM action:**  [guardduty:StartMonitoringMembers](#list_guardduty-action-StartMonitoringMembers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopMonitoringMembers  **
  - **IAM action:**  [guardduty:StopMonitoringMembers](#list_guardduty-action-StopMonitoringMembers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [guardduty:TagResource](#list_guardduty-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UnarchiveFindings  **
  - **IAM action:**  [guardduty:UnarchiveFindings](#list_guardduty-action-UnarchiveFindings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UntagResource  **
  - **IAM action:**  [guardduty:UntagResource](#list_guardduty-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateCustomDetectionRuleAssociation  **
  - **IAM action:**  [guardduty:UpdateCustomDetectionRuleAssociation](#list_guardduty-action-UpdateCustomDetectionRuleAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCustomDetectionRuleOrgConfiguration  **
  - **IAM action:**  [guardduty:UpdateCustomDetectionRuleOrgConfiguration](#list_guardduty-action-UpdateCustomDetectionRuleOrgConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDetector  **
  - **IAM action:**  [guardduty:UpdateDetector](#list_guardduty-action-UpdateDetector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFilter  **
  - **IAM action:**  [guardduty:UpdateFilter](#list_guardduty-action-UpdateFilter) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFindingsFeedback  **
  - **IAM action:**  [guardduty:UpdateFindingsFeedback](#list_guardduty-action-UpdateFindingsFeedback) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateIPSet  **
  - **IAM action:**  [guardduty:UpdateIPSet](#list_guardduty-action-UpdateIPSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateMalwareProtectionPlan  **
  - **IAM action:**  [guardduty:UpdateMalwareProtectionPlan](#list_guardduty-action-UpdateMalwareProtectionPlan)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** malware-protection-plan.guardduty.amazonaws.com / **Access level:** Write

- **   UpdateMalwareScanSettings  **
  - **IAM action:**  [guardduty:UpdateMalwareScanSettings](#list_guardduty-action-UpdateMalwareScanSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateMemberDetectors  **
  - **IAM action:**  [guardduty:UpdateMemberDetectors](#list_guardduty-action-UpdateMemberDetectors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateOrganizationConfiguration  **
  - **IAM action:**  [guardduty:UpdateOrganizationConfiguration](#list_guardduty-action-UpdateOrganizationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePublishingDestination  **
  - **IAM action:**  [guardduty:UpdatePublishingDestination](#list_guardduty-action-UpdatePublishingDestination) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateThreatEntitySet  **
  - **IAM action:**  [guardduty:UpdateThreatEntitySet](#list_guardduty-action-UpdateThreatEntitySet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateThreatIntelSet  **
  - **IAM action:**  [guardduty:UpdateThreatIntelSet](#list_guardduty-action-UpdateThreatIntelSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateTrustedEntitySet  **
  - **IAM action:**  [guardduty:UpdateTrustedEntitySet](#list_guardduty-action-UpdateTrustedEntitySet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon GuardDuty
<a name="list_guardduty-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AcceptAdministratorInvitation](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_AcceptAdministratorInvitation.html)  **
  - **Description:** Grants permission to accept invitations to become a GuardDuty member account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [AcceptInvitation](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_AcceptInvitation.html)  **
  - **Description:** Grants permission to accept invitations to become a GuardDuty member account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ArchiveFindings](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ArchiveFindings.html)  **
  - **Description:** Grants permission to archive GuardDuty findings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateCustomDetectionRuleAssociation](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CreateCustomDetectionRuleAssociation.html)  **
  - **Description:** Grants permission to create a GuardDuty custom detection rule association
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_guardduty-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_guardduty-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCustomDetectionRuleOrgConfiguration](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CreateCustomDetectionRuleOrgConfiguration.html)  **
  - **Description:** Grants permission to create the organization configuration for a GuardDuty custom detection rule
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateDetector](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CreateDetector.html)  **
  - **Description:** Grants permission to create a detector
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_guardduty-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_guardduty-aws_TagKeys)
  - **Access level:** Write

- **   [CreateFilter](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CreateFilter.html)  **
  - **Description:** Grants permission to create GuardDuty filters. A filters defines finding attributes and conditions used to filter findings
  - **Resource types (\*required):** [filter\*](#list_guardduty-resource-filter)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_guardduty-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_guardduty-aws_TagKeys)
  - **Access level:** Write

- **   [CreateIPSet](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CreateIPSet.html)  **
  - **Description:** Grants permission to create an IPSet
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_guardduty-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_guardduty-aws_TagKeys)
  - **Access level:** Write

- **   [CreateInvestigation](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CreateInvestigation.html)  **
  - **Description:** Grants permission to create a GuardDuty investigation
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateMalwareProtectionPlan](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CreateMalwareProtectionPlan.html)  **
  - **Description:** Grants permission to create a new Malware Protection plan
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_guardduty-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_guardduty-aws_TagKeys)
  - **Access level:** Write

- **   [CreateMembers](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CreateMembers.html)  **
  - **Description:** Grants permission to create GuardDuty member accounts, where the account used to create a member becomes the GuardDuty administrator account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreatePublishingDestination](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CreatePublishingDestination.html)  **
  - **Description:** Grants permission to create a publishing destination
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_guardduty-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_guardduty-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSampleFindings](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CreateSampleFindings.html)  **
  - **Description:** Grants permission to create sample findings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateThreatEntitySet](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CreateThreatEntitySet.html)  **
  - **Description:** Grants permission to create GuardDuty ThreatEntitySets, where a ThreatEntitySet consists of known malicious IP addresses and/or domains used by GuardDuty to generate findings
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_guardduty-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_guardduty-aws_TagKeys)
  - **Access level:** Write

- **   [CreateThreatIntelSet](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CreateThreatIntelSet.html)  **
  - **Description:** Grants permission to create GuardDuty ThreatIntelSets, where a ThreatIntelSet consists of known malicious IP addresses used by GuardDuty to generate findings
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_guardduty-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_guardduty-aws_TagKeys)
  - **Access level:** Write

- **   [CreateTrustedEntitySet](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_CreateTrustedEntitySet.html)  **
  - **Description:** Grants permission to create a TrustedEntitySet
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_guardduty-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_guardduty-aws_TagKeys)
  - **Access level:** Write

- **   [DeclineInvitations](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DeclineInvitations.html)  **
  - **Description:** Grants permission to decline invitations to become a GuardDuty member account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteCustomDetectionRuleAssociation](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DeleteCustomDetectionRuleAssociation.html)  **
  - **Description:** Grants permission to delete a GuardDuty custom detection rule association
  - **Resource types (\*required):** [customdetectionruleassociation\*](#list_guardduty-resource-customdetectionruleassociation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCustomDetectionRuleOrgConfiguration](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DeleteCustomDetectionRuleOrgConfiguration.html)  **
  - **Description:** Grants permission to delete the organization configuration for a GuardDuty custom detection rule
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteDetector](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DeleteDetector.html)  **
  - **Description:** Grants permission to delete GuardDuty detectors
  - **Resource types (\*required):** [detector\*](#list_guardduty-resource-detector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFilter](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DeleteFilter.html)  **
  - **Description:** Grants permission to delete GuardDuty filters
  - **Resource types (\*required):** [filter\*](#list_guardduty-resource-filter)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteIPSet](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DeleteIPSet.html)  **
  - **Description:** Grants permission to delete GuardDuty IPSets
  - **Resource types (\*required):** [ipset\*](#list_guardduty-resource-ipset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteInvitations](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DeleteInvitations.html)  **
  - **Description:** Grants permission to delete invitations to become a GuardDuty member account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteMalwareProtectionPlan](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DeleteMalwareProtectionPlan.html)  **
  - **Description:** Grants permission to delete a Malware Protection plan
  - **Resource types (\*required):** [malwareprotectionplan\*](#list_guardduty-resource-malwareprotectionplan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteMembers](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DeleteMembers.html)  **
  - **Description:** Grants permission to delete GuardDuty member accounts
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeletePublishingDestination](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DeletePublishingDestination.html)  **
  - **Description:** Grants permission to delete a publishing destination
  - **Resource types (\*required):** [publishingDestination\*](#list_guardduty-resource-publishingDestination)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteThreatEntitySet](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DeleteThreatEntitySet.html)  **
  - **Description:** Grants permission to delete GuardDuty ThreatEntitySets
  - **Resource types (\*required):** [threatentityset\*](#list_guardduty-resource-threatentityset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteThreatIntelSet](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DeleteThreatIntelSet.html)  **
  - **Description:** Grants permission to delete GuardDuty ThreatIntelSets
  - **Resource types (\*required):** [threatintelset\*](#list_guardduty-resource-threatintelset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTrustedEntitySet](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DeleteTrustedEntitySet.html)  **
  - **Description:** Grants permission to delete GuardDuty TrustedEntitySets
  - **Resource types (\*required):** [trustedentityset\*](#list_guardduty-resource-trustedentityset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeMalwareScans](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DescribeMalwareScans.html)  **
  - **Description:** Grants permission to retrieve details about malware scans
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeOrganizationConfiguration](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DescribeOrganizationConfiguration.html)  **
  - **Description:** Grants permission to retrieve details about the delegated administrator associated with a GuardDuty detector
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribePublishingDestination](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DescribePublishingDestination.html)  **
  - **Description:** Grants permission to retrieve details about a publishing destination
  - **Resource types (\*required):** [publishingDestination\*](#list_guardduty-resource-publishingDestination)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DisableOrganizationAdminAccount](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DisableOrganizationAdminAccount.html)  **
  - **Description:** Grants permission to disable the organization delegated administrator for GuardDuty
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DisassociateFromAdministratorAccount](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DisassociateFromAdministratorAccount.html)  **
  - **Description:** Grants permission to disassociate a GuardDuty member account from its GuardDuty administrator account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DisassociateFromMasterAccount](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DisassociateFromMasterAccount.html)  **
  - **Description:** Grants permission to disassociate a GuardDuty member account from its GuardDuty administrator account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DisassociateMembers](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DisassociateMembers.html)  **
  - **Description:** Grants permission to disassociate GuardDuty member accounts from their administrator GuardDuty account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [EnableOrganizationAdminAccount](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_EnableOrganizationAdminAccount.html)  **
  - **Description:** Grants permission to enable an organization delegated administrator for GuardDuty
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetAdministratorAccount](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetAdministratorAccount.html)  **
  - **Description:** Grants permission to retrieve details of the GuardDuty administrator account associated with a member account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetCoverageStatistics](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetCoverageStatistics.html)  **
  - **Description:** Grants permission to list Amazon GuardDuty coverage statistics for the specified GuardDuty account in a Region
  - **Resource types (\*required):** [detector\*](#list_guardduty-resource-detector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCustomDetectionRule](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetCustomDetectionRule.html)  **
  - **Description:** Grants permission to retrieve a GuardDuty custom detection rule
  - **Resource types (\*required):** [customdetectionrule\*](#list_guardduty-resource-customdetectionrule)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetCustomDetectionRuleAssociation](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetCustomDetectionRuleAssociation.html)  **
  - **Description:** Grants permission to retrieve a GuardDuty custom detection rule association
  - **Resource types (\*required):** [customdetectionruleassociation\*](#list_guardduty-resource-customdetectionruleassociation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCustomDetectionRuleOrgConfiguration](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetCustomDetectionRuleOrgConfiguration.html)  **
  - **Description:** Grants permission to retrieve the organization configuration for a GuardDuty custom detection rule
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetDetector](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetDetector.html)  **
  - **Description:** Grants permission to retrieve GuardDuty detectors
  - **Resource types (\*required):** [detector\*](#list_guardduty-resource-detector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetFilter](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetFilter.html)  **
  - **Description:** Grants permission to retrieve GuardDuty filters
  - **Resource types (\*required):** [filter\*](#list_guardduty-resource-filter)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetFindings](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetFindings.html)  **
  - **Description:** Grants permission to retrieve GuardDuty findings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetFindingsStatistics](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetFindingsStatistics.html)  **
  - **Description:** Grants permission to retrieve a list of GuardDuty finding statistics
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetIPSet](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetIPSet.html)  **
  - **Description:** Grants permission to retrieve GuardDuty IPSets
  - **Resource types (\*required):** [ipset\*](#list_guardduty-resource-ipset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetInvestigation](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetInvestigation.html)  **
  - **Description:** Grants permission to retrieve a GuardDuty investigation
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetInvitationsCount](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetInvitationsCount.html)  **
  - **Description:** Grants permission to retrieve the count of all GuardDuty invitations sent to a specified account, which does not include the accepted invitation
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetMalwareProtectionPlan](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetMalwareProtectionPlan.html)  **
  - **Description:** Grants permission to retrieve a Malware Protection plan details
  - **Resource types (\*required):** [malwareprotectionplan\*](#list_guardduty-resource-malwareprotectionplan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMalwareScan](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetMalwareScan.html)  **
  - **Description:** Grants permission to retrieve a malware scan's details
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetMalwareScanSettings](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetMalwareScanSettings.html)  **
  - **Description:** Grants permission to retrieve the malware scan settings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetMasterAccount](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetMasterAccount.html)  **
  - **Description:** Grants permission to retrieve details of the GuardDuty administrator account associated with a member account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetMemberDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetMemberDetectors.html)  **
  - **Description:** Grants permission to describe which data sources are enabled for member accounts detectors
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetMembers](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetMembers.html)  **
  - **Description:** Grants permission to retrieve the member accounts associated with an administrator account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetOrganizationStatistics](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetOrganizationStatistics.html)  **
  - **Description:** Grants permission to retrieve GuardDuty protection plan coverage statistics for member accounts in a Region
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetRemainingFreeTrialDays](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetRemainingFreeTrialDays.html)  **
  - **Description:** Grants permission to provide the number of days left for each data source used in the free trial period
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetThreatEntitySet](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetThreatEntitySet.html)  **
  - **Description:** Grants permission to retrieve GuardDuty ThreatEntitySets
  - **Resource types (\*required):** [threatentityset\*](#list_guardduty-resource-threatentityset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetThreatIntelSet](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetThreatIntelSet.html)  **
  - **Description:** Grants permission to retrieve GuardDuty ThreatIntelSets
  - **Resource types (\*required):** [threatintelset\*](#list_guardduty-resource-threatintelset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTrustedEntitySet](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetTrustedEntitySet.html)  **
  - **Description:** Grants permission to retrieve GuardDuty TrustedEntitySets
  - **Resource types (\*required):** [trustedentityset\*](#list_guardduty-resource-trustedentityset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetUsageStatistics](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetUsageStatistics.html)  **
  - **Description:** Grants permission to list Amazon GuardDuty usage statistics over the last 30 days for the specified detector ID
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [InviteMembers](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_InviteMembers.html)  **
  - **Description:** Grants permission to invite other AWS accounts to enable GuardDuty and become GuardDuty member accounts
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ListCoverage](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListCoverage.html)  **
  - **Description:** Grants permission to list all the resource details for a given account in a Region
  - **Resource types (\*required):** [detector\*](#list_guardduty-resource-detector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListCustomDetectionRuleAssociations](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListCustomDetectionRuleAssociations.html)  **
  - **Description:** Grants permission to retrieve a list of GuardDuty custom detection rule associations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCustomDetectionRuleOrgConfigurations](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListCustomDetectionRuleOrgConfigurations.html)  **
  - **Description:** Grants permission to retrieve a list of organization configurations for GuardDuty custom detection rules
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCustomDetectionRules](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListCustomDetectionRules.html)  **
  - **Description:** Grants permission to retrieve a list of GuardDuty custom detection rules
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html)  **
  - **Description:** Grants permission to retrieve a list of GuardDuty detectors
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListFilters](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListFilters.html)  **
  - **Description:** Grants permission to retrieve a list of GuardDuty filters
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListFindings](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListFindings.html)  **
  - **Description:** Grants permission to retrieve a list of GuardDuty findings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListIPSets](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListIPSets.html)  **
  - **Description:** Grants permission to retrieve a list of GuardDuty IPSets
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListInvestigations](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListInvestigations.html)  **
  - **Description:** Grants permission to retrieve a list of GuardDuty investigations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListInvitations](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListInvitations.html)  **
  - **Description:** Grants permission to retrieve a list of all of the GuardDuty membership invitations that were sent to an AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMalwareProtectionPlans](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListMalwareProtectionPlans.html)  **
  - **Description:** Grants permission to retrieve a list of Malware Protection plans
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMalwareScans](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListMalwareScans.html)  **
  - **Description:** Grants permission to retrieve a list of malware scans
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMembers](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListMembers.html)  **
  - **Description:** Grants permission to retrieve a list of GuardDuty member accounts associated with an administrator account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListOrganizationAdminAccounts](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListOrganizationAdminAccounts.html)  **
  - **Description:** Grants permission to list details about the organization delegated administrator for GuardDuty
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPublishingDestinations](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListPublishingDestinations.html)  **
  - **Description:** Grants permission to retrieve a list of publishing destinations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to retrieve a list of tags associated with a GuardDuty resource
  - **Resource types (\*required):** [customdetectionruleassociation](#list_guardduty-resource-customdetectionruleassociation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [detector](#list_guardduty-resource-detector) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [filter](#list_guardduty-resource-filter) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ipset](#list_guardduty-resource-ipset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [malwareprotectionplan](#list_guardduty-resource-malwareprotectionplan) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [publishingDestination](#list_guardduty-resource-publishingDestination) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [threatentityset](#list_guardduty-resource-threatentityset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [threatintelset](#list_guardduty-resource-threatintelset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [trustedentityset](#list_guardduty-resource-trustedentityset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListThreatEntitySets](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListThreatEntitySets.html)  **
  - **Description:** Grants permission to retrieve a list of GuardDuty ThreatEntitySets
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListThreatIntelSets](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListThreatIntelSets.html)  **
  - **Description:** Grants permission to retrieve a list of GuardDuty ThreatIntelSets
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTrustedEntitySets](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListTrustedEntitySets.html)  **
  - **Description:** Grants permission to retrieve a list of GuardDuty TrustedEntitySets
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [SendObjectMalwareScan](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_SendObjectMalwareScan.html)  **
  - **Description:** Grants permission to initiate a new object malware scan
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SendSecurityTelemetry](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_SendSecurityTelemetry.html)  **
  - **Description:** Grants permission to send security telemetry for a specific GuardDuty account in a Region
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartMalwareScan](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_StartMalwareScan.html)  **
  - **Description:** Grants permission to initiate a new malware scan
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartMonitoringMembers](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_StartMonitoringMembers.html)  **
  - **Description:** Grants permission to a GuardDuty administrator account to monitor findings from GuardDuty member accounts
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StopMonitoringMembers](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_StopMonitoringMembers.html)  **
  - **Description:** Grants permission to disable monitoring findings from member accounts
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add tags to a GuardDuty resource
  - **Resource types (\*required):** [customdetectionruleassociation](#list_guardduty-resource-customdetectionruleassociation) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_guardduty-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_guardduty-aws_TagKeys)
  - **Resource types (\*required):** [detector](#list_guardduty-resource-detector) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_guardduty-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_guardduty-aws_TagKeys)
  - **Resource types (\*required):** [filter](#list_guardduty-resource-filter) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_guardduty-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_guardduty-aws_TagKeys)
  - **Resource types (\*required):** [ipset](#list_guardduty-resource-ipset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_guardduty-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_guardduty-aws_TagKeys)
  - **Resource types (\*required):** [malwareprotectionplan](#list_guardduty-resource-malwareprotectionplan) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_guardduty-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_guardduty-aws_TagKeys)
  - **Resource types (\*required):** [publishingDestination](#list_guardduty-resource-publishingDestination) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_guardduty-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_guardduty-aws_TagKeys)
  - **Resource types (\*required):** [threatentityset](#list_guardduty-resource-threatentityset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_guardduty-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_guardduty-aws_TagKeys)
  - **Resource types (\*required):** [threatintelset](#list_guardduty-resource-threatintelset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_guardduty-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_guardduty-aws_TagKeys)
  - **Resource types (\*required):** [trustedentityset](#list_guardduty-resource-trustedentityset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_guardduty-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_guardduty-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UnarchiveFindings](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UnarchiveFindings.html)  **
  - **Description:** Grants permission to unarchive GuardDuty findings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UntagResource](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from a GuardDuty resource
  - **Resource types (\*required):** [customdetectionruleassociation](#list_guardduty-resource-customdetectionruleassociation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_guardduty-aws_TagKeys)
  - **Resource types (\*required):** [detector](#list_guardduty-resource-detector) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_guardduty-aws_TagKeys)
  - **Resource types (\*required):** [filter](#list_guardduty-resource-filter) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_guardduty-aws_TagKeys)
  - **Resource types (\*required):** [ipset](#list_guardduty-resource-ipset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_guardduty-aws_TagKeys)
  - **Resource types (\*required):** [malwareprotectionplan](#list_guardduty-resource-malwareprotectionplan) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_guardduty-aws_TagKeys)
  - **Resource types (\*required):** [publishingDestination](#list_guardduty-resource-publishingDestination) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_guardduty-aws_TagKeys)
  - **Resource types (\*required):** [threatentityset](#list_guardduty-resource-threatentityset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_guardduty-aws_TagKeys)
  - **Resource types (\*required):** [threatintelset](#list_guardduty-resource-threatintelset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_guardduty-aws_TagKeys)
  - **Resource types (\*required):** [trustedentityset](#list_guardduty-resource-trustedentityset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_guardduty-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateCustomDetectionRuleAssociation](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateCustomDetectionRuleAssociation.html)  **
  - **Description:** Grants permission to update a GuardDuty custom detection rule association
  - **Resource types (\*required):** [customdetectionruleassociation\*](#list_guardduty-resource-customdetectionruleassociation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCustomDetectionRuleOrgConfiguration](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateCustomDetectionRuleOrgConfiguration.html)  **
  - **Description:** Grants permission to update the organization configuration for a GuardDuty custom detection rule
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateDetector](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateDetector.html)  **
  - **Description:** Grants permission to update GuardDuty detectors
  - **Resource types (\*required):** [detector\*](#list_guardduty-resource-detector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFilter](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateFilter.html)  **
  - **Description:** Grants permission to updates GuardDuty filters
  - **Resource types (\*required):** [filter\*](#list_guardduty-resource-filter)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFindingsFeedback](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateFindingsFeedback.html)  **
  - **Description:** Grants permission to update findings feedback to mark GuardDuty findings as useful or not useful
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateIPSet](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateIPSet.html)  **
  - **Description:** Grants permission to update GuardDuty IPSets
  - **Resource types (\*required):** [ipset\*](#list_guardduty-resource-ipset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateMalwareProtectionPlan](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateMalwareProtectionPlan.html)  **
  - **Description:** Grants permission to update the Malware Protection plan
  - **Resource types (\*required):** [malwareprotectionplan\*](#list_guardduty-resource-malwareprotectionplan)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateMalwareScanSettings](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateMalwareScanSettings.html)  **
  - **Description:** Grants permission to update the malware scan settings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateMemberDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateMemberDetectors.html)  **
  - **Description:** Grants permission to update which data sources are enabled for member accounts detectors
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateOrganizationConfiguration](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateOrganizationConfiguration.html)  **
  - **Description:** Grants permission to update the delegated administrator configuration associated with a GuardDuty detector
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdatePublishingDestination](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdatePublishingDestination.html)  **
  - **Description:** Grants permission to update a publishing destination
  - **Resource types (\*required):** [publishingDestination\*](#list_guardduty-resource-publishingDestination)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateThreatEntitySet](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateThreatEntitySet.html)  **
  - **Description:** Grants permission to update GuardDuty ThreatEntitySets
  - **Resource types (\*required):** [threatentityset\*](#list_guardduty-resource-threatentityset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateThreatIntelSet](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateThreatIntelSet.html)  **
  - **Description:** Grants permission to updates the GuardDuty ThreatIntelSets
  - **Resource types (\*required):** [threatintelset\*](#list_guardduty-resource-threatintelset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateTrustedEntitySet](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateTrustedEntitySet.html)  **
  - **Description:** Grants permission to update GuardDuty TrustedEntitySets
  - **Resource types (\*required):** [trustedentityset\*](#list_guardduty-resource-trustedentityset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon GuardDuty
<a name="list_guardduty-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [customdetectionrule](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_managing_access.html#guardduty-resources)  | arn:${Partition}:guardduty::aws:detection-rule/custom/${RuleId} |   | 
|  [customdetectionruleassociation](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_managing_access.html#guardduty-resources)  | arn:${Partition}:guardduty:${Region}:${Account}:detection-rule/custom/${RuleId}/association/${AssociationId} | [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_) | 
|  [detector](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_managing_access.html#guardduty-resources)  | arn:${Partition}:guardduty:${Region}:${Account}:detector/${DetectorId} | [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_) | 
|  [filter](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_managing_access.html#guardduty-resources)  | arn:${Partition}:guardduty:${Region}:${Account}:detector/${DetectorId}/filter/${FilterName} | [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_) | 
|  [ipset](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_managing_access.html#guardduty-resources)  | arn:${Partition}:guardduty:${Region}:${Account}:detector/${DetectorId}/ipset/${IPSetId} | [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_) | 
|  [malwareprotectionplan](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_managing_access.html#guardduty-resources)  | arn:${Partition}:guardduty:${Region}:${Account}:malware-protection-plan/${MalwareProtectionPlanId} | [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_) | 
|  [publishingDestination](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_managing_access.html#guardduty-resources)  | arn:${Partition}:guardduty:${Region}:${Account}:detector/${DetectorId}/publishingdestination/${PublishingDestinationId} | [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_) | 
|  [threatentityset](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_managing_access.html#guardduty-resources)  | arn:${Partition}:guardduty:${Region}:${Account}:detector/${DetectorId}/threatentityset/${ThreatEntitySetId} | [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_) | 
|  [threatintelset](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_managing_access.html#guardduty-resources)  | arn:${Partition}:guardduty:${Region}:${Account}:detector/${DetectorId}/threatintelset/${ThreatIntelSetId} | [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_) | 
|  [trustedentityset](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_managing_access.html#guardduty-resources)  | arn:${Partition}:guardduty:${Region}:${Account}:detector/${DetectorId}/trustedentityset/${TrustedEntitySetId} | [aws:ResourceTag/${TagKey}](#list_guardduty-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon GuardDuty
<a name="list_guardduty-policy-keys"></a>

Amazon GuardDuty defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by tag keys in the request | ArrayOfString | 