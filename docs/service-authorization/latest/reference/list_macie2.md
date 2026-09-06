

# Actions, resources, and condition keys for Amazon Macie
<a name="list_macie2"></a>

Amazon Macie (service prefix: `macie2`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/macie/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/macie/latest/APIReference/operations.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/macie2/macie2.json) for this service.

**Topics**
+ [API operations defined by Amazon Macie](#list_macie2-operations)
+ [Actions defined by Amazon Macie](#list_macie2-actions-as-permissions)
+ [Resource types defined by Amazon Macie](#list_macie2-resources-for-iam-policies)
+ [Condition keys for Amazon Macie](#list_macie2-policy-keys)

## API operations defined by Amazon Macie
<a name="list_macie2-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_macie2-actions-as-permissions).




- **   AcceptInvitation  **
  - **IAM action:**  [macie2:AcceptInvitation](#list_macie2-action-AcceptInvitation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchGetCustomDataIdentifiers  **
  - **IAM action:**  [macie2:BatchGetCustomDataIdentifiers](#list_macie2-action-BatchGetCustomDataIdentifiers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchUpdateAutomatedDiscoveryAccounts  **
  - **IAM action:**  [macie2:BatchUpdateAutomatedDiscoveryAccounts](#list_macie2-action-BatchUpdateAutomatedDiscoveryAccounts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAllowList  **
  - **IAM action:**  [macie2:CreateAllowList](#list_macie2-action-CreateAllowList)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [macie2:TagResource](#list_macie2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateClassificationJob  **
  - **IAM action:**  [macie2:CreateClassificationJob](#list_macie2-action-CreateClassificationJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [macie2:TagResource](#list_macie2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateCustomDataIdentifier  **
  - **IAM action:**  [macie2:CreateCustomDataIdentifier](#list_macie2-action-CreateCustomDataIdentifier)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [macie2:TagResource](#list_macie2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateFindingsFilter  **
  - **IAM action:**  [macie2:CreateFindingsFilter](#list_macie2-action-CreateFindingsFilter)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [macie2:TagResource](#list_macie2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateInvitations  **
  - **IAM action:**  [macie2:CreateInvitations](#list_macie2-action-CreateInvitations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateMember  **
  - **IAM action:**  [macie2:CreateMember](#list_macie2-action-CreateMember)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [macie2:TagResource](#list_macie2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateSampleFindings  **
  - **IAM action:**  [macie2:CreateSampleFindings](#list_macie2-action-CreateSampleFindings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeclineInvitations  **
  - **IAM action:**  [macie2:DeclineInvitations](#list_macie2-action-DeclineInvitations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAllowList  **
  - **IAM action:**  [macie2:DeleteAllowList](#list_macie2-action-DeleteAllowList) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCustomDataIdentifier  **
  - **IAM action:**  [macie2:DeleteCustomDataIdentifier](#list_macie2-action-DeleteCustomDataIdentifier) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFindingsFilter  **
  - **IAM action:**  [macie2:DeleteFindingsFilter](#list_macie2-action-DeleteFindingsFilter) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteInvitations  **
  - **IAM action:**  [macie2:DeleteInvitations](#list_macie2-action-DeleteInvitations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMember  **
  - **IAM action:**  [macie2:DeleteMember](#list_macie2-action-DeleteMember) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeBuckets  **
  - **IAM action:**  [macie2:DescribeBuckets](#list_macie2-action-DescribeBuckets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeClassificationJob  **
  - **IAM action:**  [macie2:DescribeClassificationJob](#list_macie2-action-DescribeClassificationJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeOrganizationConfiguration  **
  - **IAM action:**  [macie2:DescribeOrganizationConfiguration](#list_macie2-action-DescribeOrganizationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DisableMacie  **
  - **IAM action:**  [macie2:DisableMacie](#list_macie2-action-DisableMacie) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisableOrganizationAdminAccount  **
  - **IAM action:**  [macie2:DisableOrganizationAdminAccount](#list_macie2-action-DisableOrganizationAdminAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateFromAdministratorAccount  **
  - **IAM action:**  [macie2:DisassociateFromAdministratorAccount](#list_macie2-action-DisassociateFromAdministratorAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateFromMasterAccount  **
  - **IAM action:**  [macie2:DisassociateFromMasterAccount](#list_macie2-action-DisassociateFromMasterAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateMember  **
  - **IAM action:**  [macie2:DisassociateMember](#list_macie2-action-DisassociateMember) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableMacie  **
  - **IAM action:**  [macie2:EnableMacie](#list_macie2-action-EnableMacie) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableOrganizationAdminAccount  **
  - **IAM action:**  [macie2:EnableOrganizationAdminAccount](#list_macie2-action-EnableOrganizationAdminAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAdministratorAccount  **
  - **IAM action:**  [macie2:GetAdministratorAccount](#list_macie2-action-GetAdministratorAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAllowList  **
  - **IAM action:**  [macie2:GetAllowList](#list_macie2-action-GetAllowList) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAutomatedDiscoveryConfiguration  **
  - **IAM action:**  [macie2:GetAutomatedDiscoveryConfiguration](#list_macie2-action-GetAutomatedDiscoveryConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBucketStatistics  **
  - **IAM action:**  [macie2:GetBucketStatistics](#list_macie2-action-GetBucketStatistics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetClassificationExportConfiguration  **
  - **IAM action:**  [macie2:GetClassificationExportConfiguration](#list_macie2-action-GetClassificationExportConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetClassificationScope  **
  - **IAM action:**  [macie2:GetClassificationScope](#list_macie2-action-GetClassificationScope) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCustomDataIdentifier  **
  - **IAM action:**  [macie2:GetCustomDataIdentifier](#list_macie2-action-GetCustomDataIdentifier) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFindingStatistics  **
  - **IAM action:**  [macie2:GetFindingStatistics](#list_macie2-action-GetFindingStatistics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFindings  **
  - **IAM action:**  [macie2:GetFindings](#list_macie2-action-GetFindings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFindingsFilter  **
  - **IAM action:**  [macie2:GetFindingsFilter](#list_macie2-action-GetFindingsFilter) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFindingsPublicationConfiguration  **
  - **IAM action:**  [macie2:GetFindingsPublicationConfiguration](#list_macie2-action-GetFindingsPublicationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetInvitationsCount  **
  - **IAM action:**  [macie2:GetInvitationsCount](#list_macie2-action-GetInvitationsCount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMacieSession  **
  - **IAM action:**  [macie2:GetMacieSession](#list_macie2-action-GetMacieSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMasterAccount  **
  - **IAM action:**  [macie2:GetMasterAccount](#list_macie2-action-GetMasterAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMember  **
  - **IAM action:**  [macie2:GetMember](#list_macie2-action-GetMember) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourceProfile  **
  - **IAM action:**  [macie2:GetResourceProfile](#list_macie2-action-GetResourceProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRevealConfiguration  **
  - **IAM action:**  [macie2:GetRevealConfiguration](#list_macie2-action-GetRevealConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSensitiveDataOccurrences  **
  - **IAM action:**  [macie2:GetSensitiveDataOccurrences](#list_macie2-action-GetSensitiveDataOccurrences) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSensitiveDataOccurrencesAvailability  **
  - **IAM action:**  [macie2:GetSensitiveDataOccurrencesAvailability](#list_macie2-action-GetSensitiveDataOccurrencesAvailability) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSensitivityInspectionTemplate  **
  - **IAM action:**  [macie2:GetSensitivityInspectionTemplate](#list_macie2-action-GetSensitivityInspectionTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetUsageStatistics  **
  - **IAM action:**  [macie2:GetUsageStatistics](#list_macie2-action-GetUsageStatistics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetUsageTotals  **
  - **IAM action:**  [macie2:GetUsageTotals](#list_macie2-action-GetUsageTotals) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAllowLists  **
  - **IAM action:**  [macie2:ListAllowLists](#list_macie2-action-ListAllowLists) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAutomatedDiscoveryAccounts  **
  - **IAM action:**  [macie2:ListAutomatedDiscoveryAccounts](#list_macie2-action-ListAutomatedDiscoveryAccounts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListClassificationJobs  **
  - **IAM action:**  [macie2:ListClassificationJobs](#list_macie2-action-ListClassificationJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListClassificationScopes  **
  - **IAM action:**  [macie2:ListClassificationScopes](#list_macie2-action-ListClassificationScopes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCustomDataIdentifiers  **
  - **IAM action:**  [macie2:ListCustomDataIdentifiers](#list_macie2-action-ListCustomDataIdentifiers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFindings  **
  - **IAM action:**  [macie2:ListFindings](#list_macie2-action-ListFindings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFindingsFilters  **
  - **IAM action:**  [macie2:ListFindingsFilters](#list_macie2-action-ListFindingsFilters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListInvitations  **
  - **IAM action:**  [macie2:ListInvitations](#list_macie2-action-ListInvitations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListManagedDataIdentifiers  **
  - **IAM action:**  [macie2:ListManagedDataIdentifiers](#list_macie2-action-ListManagedDataIdentifiers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMembers  **
  - **IAM action:**  [macie2:ListMembers](#list_macie2-action-ListMembers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListOrganizationAdminAccounts  **
  - **IAM action:**  [macie2:ListOrganizationAdminAccounts](#list_macie2-action-ListOrganizationAdminAccounts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListResourceProfileArtifacts  **
  - **IAM action:**  [macie2:ListResourceProfileArtifacts](#list_macie2-action-ListResourceProfileArtifacts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListResourceProfileDetections  **
  - **IAM action:**  [macie2:ListResourceProfileDetections](#list_macie2-action-ListResourceProfileDetections) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSensitivityInspectionTemplates  **
  - **IAM action:**  [macie2:ListSensitivityInspectionTemplates](#list_macie2-action-ListSensitivityInspectionTemplates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [macie2:ListTagsForResource](#list_macie2-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutClassificationExportConfiguration  **
  - **IAM action:**  [macie2:PutClassificationExportConfiguration](#list_macie2-action-PutClassificationExportConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutFindingsPublicationConfiguration  **
  - **IAM action:**  [macie2:PutFindingsPublicationConfiguration](#list_macie2-action-PutFindingsPublicationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SearchResources  **
  - **IAM action:**  [macie2:SearchResources](#list_macie2-action-SearchResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   TagResource  **
  - **IAM action:**  [macie2:TagResource](#list_macie2-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   TestCustomDataIdentifier  **
  - **IAM action:**  [macie2:TestCustomDataIdentifier](#list_macie2-action-TestCustomDataIdentifier) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UntagResource  **
  - **IAM action:**  [macie2:UntagResource](#list_macie2-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAllowList  **
  - **IAM action:**  [macie2:UpdateAllowList](#list_macie2-action-UpdateAllowList) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAutomatedDiscoveryConfiguration  **
  - **IAM action:**  [macie2:UpdateAutomatedDiscoveryConfiguration](#list_macie2-action-UpdateAutomatedDiscoveryConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateClassificationJob  **
  - **IAM action:**  [macie2:UpdateClassificationJob](#list_macie2-action-UpdateClassificationJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateClassificationScope  **
  - **IAM action:**  [macie2:UpdateClassificationScope](#list_macie2-action-UpdateClassificationScope) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFindingsFilter  **
  - **IAM action:**  [macie2:UpdateFindingsFilter](#list_macie2-action-UpdateFindingsFilter) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateMacieSession  **
  - **IAM action:**  [macie2:UpdateMacieSession](#list_macie2-action-UpdateMacieSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateMemberSession  **
  - **IAM action:**  [macie2:UpdateMemberSession](#list_macie2-action-UpdateMemberSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateOrganizationConfiguration  **
  - **IAM action:**  [macie2:UpdateOrganizationConfiguration](#list_macie2-action-UpdateOrganizationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateResourceProfile  **
  - **IAM action:**  [macie2:UpdateResourceProfile](#list_macie2-action-UpdateResourceProfile) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateResourceProfileDetections  **
  - **IAM action:**  [macie2:UpdateResourceProfileDetections](#list_macie2-action-UpdateResourceProfileDetections) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRevealConfiguration  **
  - **IAM action:**  [macie2:UpdateRevealConfiguration](#list_macie2-action-UpdateRevealConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** reveal-samples.macie.amazonaws.com / **Access level:** Write

- **   UpdateSensitivityInspectionTemplate  **
  - **IAM action:**  [macie2:UpdateSensitivityInspectionTemplate](#list_macie2-action-UpdateSensitivityInspectionTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Macie
<a name="list_macie2-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AcceptInvitation](https://docs.aws.amazon.com/macie/latest/APIReference/invitations-accept.html)  **
  - **Description:** Grants permission to accept an Amazon Macie membership invitation
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [BatchGetCustomDataIdentifiers](https://docs.aws.amazon.com/macie/latest/APIReference/custom-data-identifiers-get.html)  **
  - **Description:** Grants permission to retrieve information about one or more custom data identifiers
  - **Resource types (\*required):** [CustomDataIdentifier\*](#list_macie2-resource-CustomDataIdentifier)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_macie2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchUpdateAutomatedDiscoveryAccounts](https://docs.aws.amazon.com/macie/latest/APIReference/automated-discovery-accounts.html)  **
  - **Description:** Grants permission to an Amazon Macie administrator to change the status of automated sensitive data discovery for one or more accounts in their organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateAllowList](https://docs.aws.amazon.com/macie/latest/APIReference/allow-lists.html)  **
  - **Description:** Grants permission to create and define the settings for an allow list
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_macie2-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_macie2-aws_TagKeys)
  - **Access level:** Write

- **   [CreateClassificationJob](https://docs.aws.amazon.com/macie/latest/APIReference/jobs.html)  **
  - **Description:** Grants permission to create and define the settings for a sensitive data discovery job
  - **Resource types (\*required):** [ClassificationJob\*](#list_macie2-resource-ClassificationJob)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_macie2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_macie2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_macie2-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCustomDataIdentifier](https://docs.aws.amazon.com/macie/latest/APIReference/custom-data-identifiers.html)  **
  - **Description:** Grants permission to create and define the settings for a custom data identifier
  - **Resource types (\*required):** [CustomDataIdentifier\*](#list_macie2-resource-CustomDataIdentifier)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_macie2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_macie2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_macie2-aws_TagKeys)
  - **Access level:** Write

- **   [CreateFindingsFilter](https://docs.aws.amazon.com/macie/latest/APIReference/findingsfilters.html)  **
  - **Description:** Grants permission to create and define the settings for a findings filter
  - **Resource types (\*required):** [FindingsFilter\*](#list_macie2-resource-FindingsFilter)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_macie2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_macie2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_macie2-aws_TagKeys)
  - **Access level:** Write

- **   [CreateInvitations](https://docs.aws.amazon.com/macie/latest/APIReference/invitations.html)  **
  - **Description:** Grants permission to send an Amazon Macie membership invitation
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateMember](https://docs.aws.amazon.com/macie/latest/APIReference/members.html)  **
  - **Description:** Grants permission to associate an account with an Amazon Macie administrator account
  - **Resource types (\*required):** [Member\*](#list_macie2-resource-Member)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_macie2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_macie2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_macie2-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSampleFindings](https://docs.aws.amazon.com/macie/latest/APIReference/findings-sample.html)  **
  - **Description:** Grants permission to create sample findings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeclineInvitations](https://docs.aws.amazon.com/macie/latest/APIReference/invitations-decline.html)  **
  - **Description:** Grants permission to decline Amazon Macie membership invitations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteAllowList](https://docs.aws.amazon.com/macie/latest/APIReference/allow-lists-id.html)  **
  - **Description:** Grants permission to delete an allow list
  - **Resource types (\*required):** [AllowList\*](#list_macie2-resource-AllowList)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_macie2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCustomDataIdentifier](https://docs.aws.amazon.com/macie/latest/APIReference/custom-data-identifiers-id.html)  **
  - **Description:** Grants permission to delete a custom data identifier
  - **Resource types (\*required):** [CustomDataIdentifier\*](#list_macie2-resource-CustomDataIdentifier)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_macie2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFindingsFilter](https://docs.aws.amazon.com/macie/latest/APIReference/findingsfilters-id.html)  **
  - **Description:** Grants permission to delete a findings filter
  - **Resource types (\*required):** [FindingsFilter\*](#list_macie2-resource-FindingsFilter)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_macie2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteInvitations](https://docs.aws.amazon.com/macie/latest/APIReference/invitations-delete.html)  **
  - **Description:** Grants permission to delete Amazon Macie membership invitations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteMember](https://docs.aws.amazon.com/macie/latest/APIReference/members-id.html)  **
  - **Description:** Grants permission to delete the association between an Amazon Macie administrator account and an account
  - **Resource types (\*required):** [Member\*](#list_macie2-resource-Member)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_macie2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeBuckets](https://docs.aws.amazon.com/macie/latest/APIReference/datasources-s3.html)  **
  - **Description:** Grants permission to retrieve statistical data and other information about S3 buckets that Amazon Macie monitors and analyzes
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeClassificationJob](https://docs.aws.amazon.com/macie/latest/APIReference/jobs-jobid.html)  **
  - **Description:** Grants permission to retrieve information about the status and settings for a sensitive data discovery job
  - **Resource types (\*required):** [ClassificationJob\*](#list_macie2-resource-ClassificationJob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_macie2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeOrganizationConfiguration](https://docs.aws.amazon.com/macie/latest/APIReference/admin-configuration.html)  **
  - **Description:** Grants permission to retrieve information about the Amazon Macie configuration settings for an AWS organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DisableMacie](https://docs.aws.amazon.com/macie/latest/APIReference/macie.html)  **
  - **Description:** Grants permission to disable an Amazon Macie account, which also deletes Macie resources for the account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DisableOrganizationAdminAccount](https://docs.aws.amazon.com/macie/latest/APIReference/admin.html)  **
  - **Description:** Grants permission to disable an account as the delegated Amazon Macie administrator account for an AWS organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DisassociateFromAdministratorAccount](https://docs.aws.amazon.com/macie/latest/APIReference/administrator-disassociate.html)  **
  - **Description:** Grants permission to an Amazon Macie member account to disassociate from its Macie administrator account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DisassociateFromMasterAccount](https://docs.aws.amazon.com/macie/latest/APIReference/master-disassociate.html)  **
  - **Description:** Grants permission to an Amazon Macie member account to disassociate from its Macie administrator account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DisassociateMember](https://docs.aws.amazon.com/macie/latest/APIReference/members-disassociate-id.html)  **
  - **Description:** Grants permission to an Amazon Macie administrator account to disassociate from a Macie member account
  - **Resource types (\*required):** [Member\*](#list_macie2-resource-Member)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_macie2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [EnableMacie](https://docs.aws.amazon.com/macie/latest/APIReference/macie.html)  **
  - **Description:** Grants permission to enable and specify the configuration settings for a new Amazon Macie account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [EnableOrganizationAdminAccount](https://docs.aws.amazon.com/macie/latest/APIReference/admin.html)  **
  - **Description:** Grants permission to enable an account as the delegated Amazon Macie administrator account for an AWS organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetAdministratorAccount](https://docs.aws.amazon.com/macie/latest/APIReference/administrator.html)  **
  - **Description:** Grants permission to retrieve information about the Amazon Macie administrator account for an account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetAllowList](https://docs.aws.amazon.com/macie/latest/APIReference/allow-lists-id.html)  **
  - **Description:** Grants permission to retrieve the settings and status of an allow list
  - **Resource types (\*required):** [AllowList\*](#list_macie2-resource-AllowList)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_macie2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAutomatedDiscoveryConfiguration](https://docs.aws.amazon.com/macie/latest/APIReference/automated-discovery-configuration.html)  **
  - **Description:** Grants permission to retrieve the configuration settings and status of automated sensitive data discovery for an Amazon Macie administrator account, organization, or standalone account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetBucketStatistics](https://docs.aws.amazon.com/macie/latest/APIReference/datasources-s3-statistics.html)  **
  - **Description:** Grants permission to retrieve aggregated statistical data for all the S3 buckets that Amazon Macie monitors and analyzes
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetClassificationExportConfiguration](https://docs.aws.amazon.com/macie/latest/APIReference/classification-export-configuration.html)  **
  - **Description:** Grants permission to retrieve the settings for exporting sensitive data discovery results
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetClassificationScope](https://docs.aws.amazon.com/macie/latest/APIReference/classification-scopes-id.html)  **
  - **Description:** Grants permission to retrieve the classification scope settings for an account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetCustomDataIdentifier](https://docs.aws.amazon.com/macie/latest/APIReference/custom-data-identifiers-id.html)  **
  - **Description:** Grants permission to retrieve information about the settings for a custom data identifier
  - **Resource types (\*required):** [CustomDataIdentifier\*](#list_macie2-resource-CustomDataIdentifier)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_macie2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetFindingStatistics](https://docs.aws.amazon.com/macie/latest/APIReference/findings-statistics.html)  **
  - **Description:** Grants permission to retrieve aggregated statistical data about findings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetFindings](https://docs.aws.amazon.com/macie/latest/APIReference/findings-describe.html)  **
  - **Description:** Grants permission to retrieve the details of one or more findings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetFindingsFilter](https://docs.aws.amazon.com/macie/latest/APIReference/findingsfilters-id.html)  **
  - **Description:** Grants permission to retrieve information about the settings for a findings filter
  - **Resource types (\*required):** [FindingsFilter\*](#list_macie2-resource-FindingsFilter)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_macie2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetFindingsPublicationConfiguration](https://docs.aws.amazon.com/macie/latest/APIReference/findings-publication-configuration.html)  **
  - **Description:** Grants permission to retrieve the configuration settings for publishing findings to AWS Security Hub
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetInvitationsCount](https://docs.aws.amazon.com/macie/latest/APIReference/invitations-count.html)  **
  - **Description:** Grants permission to retrieve the count of Amazon Macie membership invitations that were received by an account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetMacieSession](https://docs.aws.amazon.com/macie/latest/APIReference/macie.html)  **
  - **Description:** Grants permission to retrieve information about the status and configuration settings for an Amazon Macie account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetMasterAccount](https://docs.aws.amazon.com/macie/latest/APIReference/master.html)  **
  - **Description:** Grants permission to retrieve information about the Amazon Macie administrator account for an account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetMember](https://docs.aws.amazon.com/macie/latest/APIReference/members-id.html)  **
  - **Description:** Grants permission to retrieve information about an account that's associated with an Amazon Macie administrator account
  - **Resource types (\*required):** [Member\*](#list_macie2-resource-Member)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_macie2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetResourceProfile](https://docs.aws.amazon.com/macie/latest/APIReference/resource-profiles.html)  **
  - **Description:** Grants permission to retrieve sensitive data discovery statistics and the sensitivity score for an S3 bucket
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetRevealConfiguration](https://docs.aws.amazon.com/macie/latest/APIReference/reveal-configuration.html)  **
  - **Description:** Grants permission to retrieve the status and configuration settings for retrieving occurrences of sensitive data reported by findings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSensitiveDataOccurrences](https://docs.aws.amazon.com/macie/latest/APIReference/findings-findingid-reveal.html)  **
  - **Description:** Grants permission to retrieve occurrences of sensitive data reported by a finding
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSensitiveDataOccurrencesAvailability](https://docs.aws.amazon.com/macie/latest/APIReference/findings-findingid-reveal-availability.html)  **
  - **Description:** Grants permission to check whether occurrences of sensitive data can be retrieved for a finding
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSensitivityInspectionTemplate](https://docs.aws.amazon.com/macie/latest/APIReference/templates-sensitivity-inspections-id.html)  **
  - **Description:** Grants permission to retrieve the sensitivity inspection template settings for an account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetUsageStatistics](https://docs.aws.amazon.com/macie/latest/APIReference/usage-statistics.html)  **
  - **Description:** Grants permission to retrieve quotas and aggregated usage data for one or more accounts
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetUsageTotals](https://docs.aws.amazon.com/macie/latest/APIReference/usage.html)  **
  - **Description:** Grants permission to retrieve aggregated usage data for an account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListAllowLists](https://docs.aws.amazon.com/macie/latest/APIReference/allow-lists.html)  **
  - **Description:** Grants permission to retrieve a subset of information about all the allow lists for an account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAutomatedDiscoveryAccounts](https://docs.aws.amazon.com/macie/latest/APIReference/automated-discovery-accounts.html)  **
  - **Description:** Grants permission to retrieve the status of automated sensitive data discovery for an account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListClassificationJobs](https://docs.aws.amazon.com/macie/latest/APIReference/jobs-list.html)  **
  - **Description:** Grants permission to retrieve a subset of information about the status and settings for one or more sensitive data discovery jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListClassificationScopes](https://docs.aws.amazon.com/macie/latest/APIReference/classification-scopes.html)  **
  - **Description:** Grants permission to retrieve a subset of information about the classification scope for an account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCustomDataIdentifiers](https://docs.aws.amazon.com/macie/latest/APIReference/custom-data-identifiers-list.html)  **
  - **Description:** Grants permission to retrieve information about all custom data identifiers
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListFindings](https://docs.aws.amazon.com/macie/latest/APIReference/findings.html)  **
  - **Description:** Grants permission to retrieve a subset of information about one or more findings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListFindingsFilters](https://docs.aws.amazon.com/macie/latest/APIReference/findingsfilters.html)  **
  - **Description:** Grants permission to retrieve information about all findings filters
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListInvitations](https://docs.aws.amazon.com/macie/latest/APIReference/invitations.html)  **
  - **Description:** Grants permission to retrieve information about all the Amazon Macie membership invitations that were received by an account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListManagedDataIdentifiers](https://docs.aws.amazon.com/macie/latest/APIReference/managed-data-identifiers-list.html)  **
  - **Description:** Grants permission to retrieve information about managed data identifiers
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMembers](https://docs.aws.amazon.com/macie/latest/APIReference/members.html)  **
  - **Description:** Grants permission to retrieve information about the Amazon Macie member accounts that are associated with a Macie administrator account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListOrganizationAdminAccounts](https://docs.aws.amazon.com/macie/latest/APIReference/admin.html)  **
  - **Description:** Grants permission to retrieve information about the delegated Amazon Macie administrator account for an AWS organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListResourceProfileArtifacts](https://docs.aws.amazon.com/macie/latest/APIReference/resource-profiles-artifacts.html)  **
  - **Description:** Grants permission to retrieve information about objects that Amazon Macie selected from an S3 bucket for automated sensitive data discovery
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListResourceProfileDetections](https://docs.aws.amazon.com/macie/latest/APIReference/resource-profiles-detections.html)  **
  - **Description:** Grants permission to retrieve information about the types and amount of sensitive data that Amazon Macie found in an S3 bucket
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSensitivityInspectionTemplates](https://docs.aws.amazon.com/macie/latest/APIReference/templates-sensitivity-inspections.html)  **
  - **Description:** Grants permission to retrieve a subset of information about the sensitivity inspection template for an account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/macie/latest/APIReference/tags-resourcearn.html)  **
  - **Description:** Grants permission to retrieve the tags for an Amazon Macie resource
  - **Resource types (\*required):** [AllowList](#list_macie2-resource-AllowList) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_macie2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ClassificationJob](#list_macie2-resource-ClassificationJob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_macie2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [CustomDataIdentifier](#list_macie2-resource-CustomDataIdentifier) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_macie2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [FindingsFilter](#list_macie2-resource-FindingsFilter) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_macie2-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Member](#list_macie2-resource-Member) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_macie2-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PutClassificationExportConfiguration](https://docs.aws.amazon.com/macie/latest/APIReference/classification-export-configuration.html)  **
  - **Description:** Grants permission to create or update the settings for storing sensitive data discovery results
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutFindingsPublicationConfiguration](https://docs.aws.amazon.com/macie/latest/APIReference/findings-publication-configuration.html)  **
  - **Description:** Grants permission to update the configuration settings for publishing findings to AWS Security Hub
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SearchResources](https://docs.aws.amazon.com/macie/latest/APIReference/datasources-search-resources.html)  **
  - **Description:** Grants permission to retrieve statistical data and other information about AWS resources that Amazon Macie monitors and analyzes
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [TagResource](https://docs.aws.amazon.com/macie/latest/APIReference/tags-resourcearn.html)  **
  - **Description:** Grants permission to add or update the tags for an Amazon Macie resource
  - **Resource types (\*required):** [AllowList](#list_macie2-resource-AllowList) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_macie2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_macie2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_macie2-aws_TagKeys)
  - **Resource types (\*required):** [ClassificationJob](#list_macie2-resource-ClassificationJob) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_macie2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_macie2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_macie2-aws_TagKeys)
  - **Resource types (\*required):** [CustomDataIdentifier](#list_macie2-resource-CustomDataIdentifier) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_macie2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_macie2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_macie2-aws_TagKeys)
  - **Resource types (\*required):** [FindingsFilter](#list_macie2-resource-FindingsFilter) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_macie2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_macie2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_macie2-aws_TagKeys)
  - **Resource types (\*required):** [Member](#list_macie2-resource-Member) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_macie2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_macie2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_macie2-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [TestCustomDataIdentifier](https://docs.aws.amazon.com/macie/latest/APIReference/custom-data-identifiers-test.html)  **
  - **Description:** Grants permission to test a custom data identifier
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UntagResource](https://docs.aws.amazon.com/macie/latest/APIReference/tags-resourcearn.html)  **
  - **Description:** Grants permission to remove tags from an Amazon Macie resource
  - **Resource types (\*required):** [AllowList](#list_macie2-resource-AllowList) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_macie2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_macie2-aws_TagKeys)
  - **Resource types (\*required):** [ClassificationJob](#list_macie2-resource-ClassificationJob) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_macie2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_macie2-aws_TagKeys)
  - **Resource types (\*required):** [CustomDataIdentifier](#list_macie2-resource-CustomDataIdentifier) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_macie2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_macie2-aws_TagKeys)
  - **Resource types (\*required):** [FindingsFilter](#list_macie2-resource-FindingsFilter) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_macie2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_macie2-aws_TagKeys)
  - **Resource types (\*required):** [Member](#list_macie2-resource-Member) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_macie2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_macie2-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAllowList](https://docs.aws.amazon.com/macie/latest/APIReference/allow-lists-id.html)  **
  - **Description:** Grants permission to update the settings for an allow list
  - **Resource types (\*required):** [AllowList\*](#list_macie2-resource-AllowList)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_macie2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAutomatedDiscoveryConfiguration](https://docs.aws.amazon.com/macie/latest/APIReference/automated-discovery-configuration.html)  **
  - **Description:** Grants permission to change the status of automated sensitive data discovery for an Amazon Macie administrator account, organization, or standalone account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateClassificationJob](https://docs.aws.amazon.com/macie/latest/APIReference/jobs-jobid.html)  **
  - **Description:** Grants permission to change the status of a sensitive data discovery job
  - **Resource types (\*required):** [ClassificationJob\*](#list_macie2-resource-ClassificationJob)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_macie2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_macie2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_macie2-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateClassificationScope](https://docs.aws.amazon.com/macie/latest/APIReference/classification-scopes-id.html)  **
  - **Description:** Grants permission to update the classification scope settings for an account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateFindingsFilter](https://docs.aws.amazon.com/macie/latest/APIReference/findingsfilters-id.html)  **
  - **Description:** Grants permission to update the settings for a findings filter
  - **Resource types (\*required):** [FindingsFilter\*](#list_macie2-resource-FindingsFilter)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_macie2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_macie2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_macie2-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateMacieSession](https://docs.aws.amazon.com/macie/latest/APIReference/macie.html)  **
  - **Description:** Grants permission to an Amazon Macie administrator account to suspend or re-enable Macie for a member account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateMemberSession](https://docs.aws.amazon.com/macie/latest/APIReference/macie-members-id.html)  **
  - **Description:** Grants permission to an Amazon Macie administrator account to suspend or re-enable a Macie member account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateOrganizationConfiguration](https://docs.aws.amazon.com/macie/latest/APIReference/admin-configuration.html)  **
  - **Description:** Grants permission to update Amazon Macie configuration settings for an AWS organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateResourceProfile](https://docs.aws.amazon.com/macie/latest/APIReference/resource-profiles.html)  **
  - **Description:** Grants permission to update the sensitivity score for an S3 bucket
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateResourceProfileDetections](https://docs.aws.amazon.com/macie/latest/APIReference/resource-profiles-detections.html)  **
  - **Description:** Grants permission to update the sensitivity scoring settings for an S3 bucket
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateRevealConfiguration](https://docs.aws.amazon.com/macie/latest/APIReference/reveal-configuration.html)  **
  - **Description:** Grants permission to update the status and configuration settings for retrieving occurrences of sensitive data reported by findings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateSensitivityInspectionTemplate](https://docs.aws.amazon.com/macie/latest/APIReference/templates-sensitivity-inspections-id.html)  **
  - **Description:** Grants permission to update the sensitivity inspection template settings for an account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by Amazon Macie
<a name="list_macie2-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [AllowList](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html)  | arn:${Partition}:macie2:${Region}:${Account}:allow-list/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_macie2-aws_ResourceTag___TagKey_) | 
|  [ClassificationJob](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html)  | arn:${Partition}:macie2:${Region}:${Account}:classification-job/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_macie2-aws_ResourceTag___TagKey_) | 
|  [CustomDataIdentifier](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html.html)  | arn:${Partition}:macie2:${Region}:${Account}:custom-data-identifier/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_macie2-aws_ResourceTag___TagKey_) | 
|  [FindingsFilter](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html)  | arn:${Partition}:macie2:${Region}:${Account}:findings-filter/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_macie2-aws_ResourceTag___TagKey_) | 
|  [Member](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html)  | arn:${Partition}:macie2:${Region}:${Account}:member/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_macie2-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Macie
<a name="list_macie2-policy-keys"></a>

Amazon Macie defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by a tag key and value pair that is allowed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by a tag key and value pair of a resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of tag keys in the request | ArrayOfString | 