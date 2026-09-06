

# Actions, resources, and condition keys for Amazon Inspector2
<a name="list_inspector2"></a>

Amazon Inspector2 (service prefix: `inspector2`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/inspector/v2/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/inspector/latest/user/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/inspector2/inspector2.json) for this service.

**Topics**
+ [API operations defined by Amazon Inspector2](#list_inspector2-operations)
+ [Actions defined by Amazon Inspector2](#list_inspector2-actions-as-permissions)
+ [Resource types defined by Amazon Inspector2](#list_inspector2-resources-for-iam-policies)
+ [Condition keys for Amazon Inspector2](#list_inspector2-policy-keys)

## API operations defined by Amazon Inspector2
<a name="list_inspector2-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_inspector2-actions-as-permissions).




- **   AssociateMember  **
  - **IAM action:**  [inspector2:AssociateMember](#list_inspector2-action-AssociateMember) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchAssociateCodeSecurityScanConfiguration  **
  - **IAM action:**  [inspector2:BatchAssociateCodeSecurityScanConfiguration](#list_inspector2-action-BatchAssociateCodeSecurityScanConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchDisassociateCodeSecurityScanConfiguration  **
  - **IAM action:**  [inspector2:BatchDisassociateCodeSecurityScanConfiguration](#list_inspector2-action-BatchDisassociateCodeSecurityScanConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchGetAccountStatus  **
  - **IAM action:**  [inspector2:BatchGetAccountStatus](#list_inspector2-action-BatchGetAccountStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetCodeSnippet  **
  - **IAM action:**  [inspector2:BatchGetCodeSnippet](#list_inspector2-action-BatchGetCodeSnippet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetFindingDetails  **
  - **IAM action:**  [inspector2:BatchGetFindingDetails](#list_inspector2-action-BatchGetFindingDetails) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetFreeTrialInfo  **
  - **IAM action:**  [inspector2:BatchGetFreeTrialInfo](#list_inspector2-action-BatchGetFreeTrialInfo) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetMemberEc2DeepInspectionStatus  **
  - **IAM action:**  [inspector2:BatchGetMemberEc2DeepInspectionStatus](#list_inspector2-action-BatchGetMemberEc2DeepInspectionStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchUpdateMemberEc2DeepInspectionStatus  **
  - **IAM action:**  [inspector2:BatchUpdateMemberEc2DeepInspectionStatus](#list_inspector2-action-BatchUpdateMemberEc2DeepInspectionStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelFindingsReport  **
  - **IAM action:**  [inspector2:CancelFindingsReport](#list_inspector2-action-CancelFindingsReport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelSbomExport  **
  - **IAM action:**  [inspector2:CancelSbomExport](#list_inspector2-action-CancelSbomExport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateCisScanConfiguration  **
  - **IAM action:**  [inspector2:CreateCisScanConfiguration](#list_inspector2-action-CreateCisScanConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [inspector2:TagResource](#list_inspector2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateCodeSecurityIntegration  **
  - **IAM action:**  [inspector2:CreateCodeSecurityIntegration](#list_inspector2-action-CreateCodeSecurityIntegration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [inspector2:TagResource](#list_inspector2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateCodeSecurityScanConfiguration  **
  - **IAM action:**  [inspector2:CreateCodeSecurityScanConfiguration](#list_inspector2-action-CreateCodeSecurityScanConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [inspector2:TagResource](#list_inspector2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateConnector  **
  - **IAM action:**  [inspector2:CreateConnector](#list_inspector2-action-CreateConnector)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [inspector2:TagResource](#list_inspector2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateFilter  **
  - **IAM action:**  [inspector2:CreateFilter](#list_inspector2-action-CreateFilter)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [inspector2:TagResource](#list_inspector2-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateFindingsReport  **
  - **IAM action:**  [inspector2:CreateFindingsReport](#list_inspector2-action-CreateFindingsReport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateSbomExport  **
  - **IAM action:**  [inspector2:CreateSbomExport](#list_inspector2-action-CreateSbomExport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCisScanConfiguration  **
  - **IAM action:**  [inspector2:DeleteCisScanConfiguration](#list_inspector2-action-DeleteCisScanConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCodeSecurityIntegration  **
  - **IAM action:**  [inspector2:DeleteCodeSecurityIntegration](#list_inspector2-action-DeleteCodeSecurityIntegration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCodeSecurityScanConfiguration  **
  - **IAM action:**  [inspector2:DeleteCodeSecurityScanConfiguration](#list_inspector2-action-DeleteCodeSecurityScanConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConnector  **
  - **IAM action:**  [inspector2:DeleteConnector](#list_inspector2-action-DeleteConnector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFilter  **
  - **IAM action:**  [inspector2:DeleteFilter](#list_inspector2-action-DeleteFilter) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeOrganizationConfiguration  **
  - **IAM action:**  [inspector2:DescribeOrganizationConfiguration](#list_inspector2-action-DescribeOrganizationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   Disable  **
  - **IAM action:**  [inspector2:Disable](#list_inspector2-action-Disable) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisableDelegatedAdminAccount  **
  - **IAM action:**  [inspector2:DisableDelegatedAdminAccount](#list_inspector2-action-DisableDelegatedAdminAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateMember  **
  - **IAM action:**  [inspector2:DisassociateMember](#list_inspector2-action-DisassociateMember) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   Enable  **
  - **IAM action:**  [inspector2:Enable](#list_inspector2-action-Enable) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableDelegatedAdminAccount  **
  - **IAM action:**  [inspector2:EnableDelegatedAdminAccount](#list_inspector2-action-EnableDelegatedAdminAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetCisScanReport  **
  - **IAM action:**  [inspector2:GetCisScanReport](#list_inspector2-action-GetCisScanReport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCisScanResultDetails  **
  - **IAM action:**  [inspector2:GetCisScanResultDetails](#list_inspector2-action-GetCisScanResultDetails) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetClustersForImage  **
  - **IAM action:**  [inspector2:GetClustersForImage](#list_inspector2-action-GetClustersForImage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCodeSecurityIntegration  **
  - **IAM action:**  [inspector2:GetCodeSecurityIntegration](#list_inspector2-action-GetCodeSecurityIntegration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCodeSecurityScan  **
  - **IAM action:**  [inspector2:GetCodeSecurityScan](#list_inspector2-action-GetCodeSecurityScan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCodeSecurityScanConfiguration  **
  - **IAM action:**  [inspector2:GetCodeSecurityScanConfiguration](#list_inspector2-action-GetCodeSecurityScanConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConfiguration  **
  - **IAM action:**  [inspector2:GetConfiguration](#list_inspector2-action-GetConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDelegatedAdminAccount  **
  - **IAM action:**  [inspector2:GetDelegatedAdminAccount](#list_inspector2-action-GetDelegatedAdminAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEc2DeepInspectionConfiguration  **
  - **IAM action:**  [inspector2:GetEc2DeepInspectionConfiguration](#list_inspector2-action-GetEc2DeepInspectionConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEncryptionKey  **
  - **IAM action:**  [inspector2:GetEncryptionKey](#list_inspector2-action-GetEncryptionKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFindingsReportStatus  **
  - **IAM action:**  [inspector2:GetFindingsReportStatus](#list_inspector2-action-GetFindingsReportStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMember  **
  - **IAM action:**  [inspector2:GetMember](#list_inspector2-action-GetMember) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSbomExport  **
  - **IAM action:**  [inspector2:GetSbomExport](#list_inspector2-action-GetSbomExport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAccountPermissions  **
  - **IAM action:**  [inspector2:ListAccountPermissions](#list_inspector2-action-ListAccountPermissions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCisScanConfigurations  **
  - **IAM action:**  [inspector2:ListCisScanConfigurations](#list_inspector2-action-ListCisScanConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCisScanResultsAggregatedByChecks  **
  - **IAM action:**  [inspector2:ListCisScanResultsAggregatedByChecks](#list_inspector2-action-ListCisScanResultsAggregatedByChecks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCisScanResultsAggregatedByTargetResource  **
  - **IAM action:**  [inspector2:ListCisScanResultsAggregatedByTargetResource](#list_inspector2-action-ListCisScanResultsAggregatedByTargetResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCisScans  **
  - **IAM action:**  [inspector2:ListCisScans](#list_inspector2-action-ListCisScans) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCodeSecurityIntegrations  **
  - **IAM action:**  [inspector2:ListCodeSecurityIntegrations](#list_inspector2-action-ListCodeSecurityIntegrations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCodeSecurityScanConfigurationAssociations  **
  - **IAM action:**  [inspector2:ListCodeSecurityScanConfigurationAssociations](#list_inspector2-action-ListCodeSecurityScanConfigurationAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCodeSecurityScanConfigurations  **
  - **IAM action:**  [inspector2:ListCodeSecurityScanConfigurations](#list_inspector2-action-ListCodeSecurityScanConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListConnectorScanConfigurations  **
  - **IAM action:**  [inspector2:ListConnectorScanConfigurations](#list_inspector2-action-ListConnectorScanConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListConnectors  **
  - **IAM action:**  [inspector2:ListConnectors](#list_inspector2-action-ListConnectors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCoverage  **
  - **IAM action:**  [inspector2:ListCoverage](#list_inspector2-action-ListCoverage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCoverageStatistics  **
  - **IAM action:**  [inspector2:ListCoverageStatistics](#list_inspector2-action-ListCoverageStatistics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDelegatedAdminAccounts  **
  - **IAM action:**  [inspector2:ListDelegatedAdminAccounts](#list_inspector2-action-ListDelegatedAdminAccounts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFilters  **
  - **IAM action:**  [inspector2:ListFilters](#list_inspector2-action-ListFilters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFindingAggregations  **
  - **IAM action:**  [inspector2:ListFindingAggregations](#list_inspector2-action-ListFindingAggregations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFindings  **
  - **IAM action:**  [inspector2:ListFindings](#list_inspector2-action-ListFindings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMembers  **
  - **IAM action:**  [inspector2:ListMembers](#list_inspector2-action-ListMembers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [inspector2:ListTagsForResource](#list_inspector2-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListUsageTotals  **
  - **IAM action:**  [inspector2:ListUsageTotals](#list_inspector2-action-ListUsageTotals) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ResetEncryptionKey  **
  - **IAM action:**  [inspector2:ResetEncryptionKey](#list_inspector2-action-ResetEncryptionKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SearchVulnerabilities  **
  - **IAM action:**  [inspector2:SearchVulnerabilities](#list_inspector2-action-SearchVulnerabilities) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   SendCisSessionHealth  **
  - **IAM action:**  [inspector2:SendCisSessionHealth](#list_inspector2-action-SendCisSessionHealth) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SendCisSessionTelemetry  **
  - **IAM action:**  [inspector2:SendCisSessionTelemetry](#list_inspector2-action-SendCisSessionTelemetry) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartCisSession  **
  - **IAM action:**  [inspector2:StartCisSession](#list_inspector2-action-StartCisSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartCodeSecurityScan  **
  - **IAM action:**  [inspector2:StartCodeSecurityScan](#list_inspector2-action-StartCodeSecurityScan) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopCisSession  **
  - **IAM action:**  [inspector2:StopCisSession](#list_inspector2-action-StopCisSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [inspector2:TagResource](#list_inspector2-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [inspector2:UntagResource](#list_inspector2-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateCisScanConfiguration  **
  - **IAM action:**  [inspector2:UpdateCisScanConfiguration](#list_inspector2-action-UpdateCisScanConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCodeSecurityIntegration  **
  - **IAM action:**  [inspector2:UpdateCodeSecurityIntegration](#list_inspector2-action-UpdateCodeSecurityIntegration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCodeSecurityScanConfiguration  **
  - **IAM action:**  [inspector2:UpdateCodeSecurityScanConfiguration](#list_inspector2-action-UpdateCodeSecurityScanConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateConfiguration  **
  - **IAM action:**  [inspector2:UpdateConfiguration](#list_inspector2-action-UpdateConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateConnector  **
  - **IAM action:**  [inspector2:UpdateConnector](#list_inspector2-action-UpdateConnector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateConnectorScanConfiguration  **
  - **IAM action:**  [inspector2:UpdateConnectorScanConfiguration](#list_inspector2-action-UpdateConnectorScanConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateEc2DeepInspectionConfiguration  **
  - **IAM action:**  [inspector2:UpdateEc2DeepInspectionConfiguration](#list_inspector2-action-UpdateEc2DeepInspectionConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateEncryptionKey  **
  - **IAM action:**  [inspector2:UpdateEncryptionKey](#list_inspector2-action-UpdateEncryptionKey) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateFilter  **
  - **IAM action:**  [inspector2:UpdateFilter](#list_inspector2-action-UpdateFilter) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateOrgEc2DeepInspectionConfiguration  **
  - **IAM action:**  [inspector2:UpdateOrgEc2DeepInspectionConfiguration](#list_inspector2-action-UpdateOrgEc2DeepInspectionConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateOrganizationConfiguration  **
  - **IAM action:**  [inspector2:UpdateOrganizationConfiguration](#list_inspector2-action-UpdateOrganizationConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Inspector2
<a name="list_inspector2-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateMember](https://docs.aws.amazon.com/inspector/v2/APIReference/API_AssociateMember.html)  **
  - **Description:** Grants permission to associate an account with an Amazon Inspector administrator account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [BatchAssociateCodeSecurityScanConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_BatchAssociateCodeSecurityScanConfiguration.html)  **
  - **Description:** Grants permission to associate multiple code repositories with an Amazon Inspector code security scan configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [BatchDisassociateCodeSecurityScanConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_BatchDisassociateCodeSecurityScanConfiguration.html)  **
  - **Description:** Grants permission to disassociate multiple code repositories from an Amazon Inspector code security scan configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [BatchGetAccountStatus](https://docs.aws.amazon.com/inspector/v2/APIReference/API_BatchGetAccountStatus.html)  **
  - **Description:** Grants permission to retrieve information about Amazon Inspector accounts for an account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [BatchGetCodeSnippet](https://docs.aws.amazon.com/inspector/v2/APIReference/API_BatchGetCodeSnippet.html)  **
  - **Description:** Grants permission to retrieve code snippet information about one or more code vulnerability findings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [BatchGetFindingDetails](https://docs.aws.amazon.com/inspector/v2/APIReference/API_BatchGetFindingDetails.html)  **
  - **Description:** Grants permission to let a customer get enhanced vulnerability intelligence details for findings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [BatchGetFreeTrialInfo](https://docs.aws.amazon.com/inspector/v2/APIReference/API_BatchGetFreeTrialInfo.html)  **
  - **Description:** Grants permission to retrieve free trial period eligibility about Amazon Inspector accounts for an account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [BatchGetMemberEc2DeepInspectionStatus](https://docs.aws.amazon.com/inspector/v2/APIReference/API_BatchGetMemberEc2DeepInspectionStatus.html)  **
  - **Description:** Grants permission to delegated administrator to retrieve ec2 deep inspection status of member accounts
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [BatchUpdateMemberEc2DeepInspectionStatus](https://docs.aws.amazon.com/inspector/v2/APIReference/API_BatchUpdateMemberEc2DeepInspectionStatus.html)  **
  - **Description:** Grants permission to update ec2 deep inspection status by delegated administrator for its associated member accounts
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CancelFindingsReport](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CancelFindingsReport.html)  **
  - **Description:** Grants permission to cancel the generation of a findings report
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CancelSbomExport](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CancelSbomExport.html)  **
  - **Description:** Grants permission to cancel the generation of an SBOM report
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateCisScanConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CreateCisScanConfiguration.html)  **
  - **Description:** Grants permission to create and define the settings for a CIS scan configuration
  - **Resource types (\*required):** [CIS Scan Configuration\*](#list_inspector2-resource-CISScanConfiguration)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_inspector2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_inspector2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_inspector2-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCodeSecurityIntegration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CreateCodeSecurityIntegration.html)  **
  - **Description:** Grants permission to create a code security integration with a source code repository provider
  - **Resource types (\*required):** [Code Security Integration\*](#list_inspector2-resource-CodeSecurityIntegration)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_inspector2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_inspector2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_inspector2-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCodeSecurityScanConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CreateCodeSecurityScanConfiguration.html)  **
  - **Description:** Grants permission to create a scan configuration for code security scanning
  - **Resource types (\*required):** [Code Security Scan Configuration\*](#list_inspector2-resource-CodeSecurityScanConfiguration)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_inspector2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_inspector2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_inspector2-aws_TagKeys)
  - **Access level:** Write

- **   [CreateConnector](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CreateConnector.html)  **
  - **Description:** Grants permission to create a connector to scan resources from a third-party cloud provider
  - **Resource types (\*required):** [Connector\*](#list_inspector2-resource-Connector)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_inspector2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_inspector2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_inspector2-aws_TagKeys)
  - **Access level:** Write

- **   [CreateFilter](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CreateFilter.html)  **
  - **Description:** Grants permission to create and define the settings for a findings filter
  - **Resource types (\*required):** [Filter\*](#list_inspector2-resource-Filter)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_inspector2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_inspector2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_inspector2-aws_TagKeys)
  - **Access level:** Write

- **   [CreateFindingsReport](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CreateFindingsReport.html)  **
  - **Description:** Grants permission to request the generation of a findings report
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateSbomExport](https://docs.aws.amazon.com/inspector/v2/APIReference/API_CreateSbomExport.html)  **
  - **Description:** Grants permission to request the generation of an SBOM report
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteCisScanConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_DeleteCisScanConfiguration.html)  **
  - **Description:** Grants permission to delete a CIS scan configuration
  - **Resource types (\*required):** [CIS Scan Configuration\*](#list_inspector2-resource-CISScanConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_inspector2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCodeSecurityIntegration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_DeleteCodeSecurityIntegration.html)  **
  - **Description:** Grants permission to delete a code security integration
  - **Resource types (\*required):** [Code Security Integration\*](#list_inspector2-resource-CodeSecurityIntegration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_inspector2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCodeSecurityScanConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_DeleteCodeSecurityScanConfiguration.html)  **
  - **Description:** Grants permission to delete a code security scan configuration
  - **Resource types (\*required):** [Code Security Scan Configuration\*](#list_inspector2-resource-CodeSecurityScanConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_inspector2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteConnector](https://docs.aws.amazon.com/inspector/v2/APIReference/API_DeleteConnector.html)  **
  - **Description:** Grants permission to delete a connector configured for scanning resources from a third-party cloud provider
  - **Resource types (\*required):** [Connector\*](#list_inspector2-resource-Connector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_inspector2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFilter](https://docs.aws.amazon.com/inspector/v2/APIReference/API_DeleteFilter.html)  **
  - **Description:** Grants permission to delete a findings filter
  - **Resource types (\*required):** [Filter\*](#list_inspector2-resource-Filter)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_inspector2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeOrganizationConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_DescribeOrganizationConfiguration.html)  **
  - **Description:** Grants permission to retrieve information about the Amazon Inspector configuration settings for an AWS organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [Disable](https://docs.aws.amazon.com/inspector/v2/APIReference/API_Disable.html)  **
  - **Description:** Grants permission to disable an Amazon Inspector account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DisableDelegatedAdminAccount](https://docs.aws.amazon.com/inspector/v2/APIReference/API_DisableDelegatedAdminAccount.html)  **
  - **Description:** Grants permission to disable an account as the delegated Amazon Inspector administrator account for an AWS organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DisassociateMember](https://docs.aws.amazon.com/inspector/v2/APIReference/API_DisassociateMember.html)  **
  - **Description:** Grants permission to an Amazon Inspector administrator account to disassociate from an Inspector member account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [Enable](https://docs.aws.amazon.com/inspector/v2/APIReference/API_Enable.html)  **
  - **Description:** Grants permission to enable and specify the configuration settings for a new Amazon Inspector account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [EnableDelegatedAdminAccount](https://docs.aws.amazon.com/inspector/v2/APIReference/API_EnableDelegatedAdminAccount.html)  **
  - **Description:** Grants permission to enable an account as the delegated Amazon Inspector administrator account for an AWS organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetCisScanReport](https://docs.aws.amazon.com/inspector/v2/APIReference/API_GetCisScanReport.html)  **
  - **Description:** Grants permission to retrieve a report containing information about completed CIS scans
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetCisScanResultDetails](https://docs.aws.amazon.com/inspector/v2/APIReference/API_GetCisScanResultDetails.html)  **
  - **Description:** Grants permission to retrieve information about all details pertaining to one CIS scan and one targeted resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [GetClustersForImage](https://docs.aws.amazon.com/inspector/v2/APIReference/API_GetClustersForImage.html)  **
  - **Description:** Grants permission to get cluster information for a given a continuously scanned amazon Ecr image
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetCodeSecurityIntegration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_GetCodeSecurityIntegration.html)  **
  - **Description:** Grants permission to retrieve information about a code security integration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetCodeSecurityScan](https://docs.aws.amazon.com/inspector/v2/APIReference/API_GetCodeSecurityScan.html)  **
  - **Description:** Grants permission to retrieve information about a specific code security scan
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetCodeSecurityScanConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_GetCodeSecurityScanConfiguration.html)  **
  - **Description:** Grants permission to retrieve information about a code security scan configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_GetConfiguration.html)  **
  - **Description:** Grants permission to retrieve information about the Amazon Inspector configuration settings for an AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetDelegatedAdminAccount](https://docs.aws.amazon.com/inspector/v2/APIReference/API_GetDelegatedAdminAccount.html)  **
  - **Description:** Grants permission to retrieve information about the Amazon Inspector administrator account for an account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetEc2DeepInspectionConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_GetEc2DeepInspectionConfiguration.html)  **
  - **Description:** Grants permission to retrieve ec2 deep inspection configuration for standalone accounts, delegated administrator and member account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetEncryptionKey](https://docs.aws.amazon.com/inspector/v2/APIReference/API_GetEncryptionKey.html)  **
  - **Description:** Grants permission to retrieve information about the KMS key used to encrypt code snippets with
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetFindingsReportStatus](https://docs.aws.amazon.com/inspector/v2/APIReference/API_GetFindingsReportStatus.html)  **
  - **Description:** Grants permission to retrieve status for a requested findings report
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetMember](https://docs.aws.amazon.com/inspector/v2/APIReference/API_GetMember.html)  **
  - **Description:** Grants permission to retrieve information about an account that's associated with an Amazon Inspector administrator account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSbomExport](https://docs.aws.amazon.com/inspector/v2/APIReference/API_GetSbomExport.html)  **
  - **Description:** Grants permission to retrieve a requested SBOM report
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListAccountPermissions](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListAccountPermissions.html)  **
  - **Description:** Grants permission to retrieve feature configuration permissions associated with an Amazon Inspector account within an organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCisScanConfigurations](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListCisScanConfigurations.html)  **
  - **Description:** Grants permission to retrieve information about all CIS scan configurations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCisScanResultsAggregatedByChecks](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListCisScanResultsAggregatedByChecks.html)  **
  - **Description:** Grants permission to retrieve information about all checks pertaining to one CIS scan
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCisScanResultsAggregatedByTargetResource](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListCisScanResultsAggregatedByTargetResource.html)  **
  - **Description:** Grants permission to retrieve information about all resources pertaining to one CIS scan
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCisScans](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListCisScans.html)  **
  - **Description:** Grants permission to retrieve information about completed CIS scans
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCodeSecurityIntegrations](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListCodeSecurityIntegrations.html)  **
  - **Description:** Grants permission to list all code security integrations in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCodeSecurityScanConfigurationAssociations](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListCodeSecurityScanConfigurationAssociations.html)  **
  - **Description:** Grants permission to list the associations between code repositories and Amazon Inspector code security scan configurations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCodeSecurityScanConfigurations](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListCodeSecurityScanConfigurations.html)  **
  - **Description:** Grants permission to list all code security scan configurations in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListConnectorScanConfigurations](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListConnectorScanConfigurations.html)  **
  - **Description:** Grants permission to list scan configurations for connectors
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListConnectors](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListConnectors.html)  **
  - **Description:** Grants permission to list connectors configured for scanning resources from third-party cloud providers
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCoverage](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListCoverage.html)  **
  - **Description:** Grants permission to retrieve the types of statistics Amazon Inspector can generate for resources Inspector monitors
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCoverageStatistics](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListCoverageStatistics.html)  **
  - **Description:** Grants permission to retrieve statistical data and other information about the resources Amazon Inspector monitors
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDelegatedAdminAccounts](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListDelegatedAdminAccounts.html)  **
  - **Description:** Grants permission to retrieve information about the delegated Amazon Inspector administrator account for an AWS organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListFilters](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListFilters.html)  **
  - **Description:** Grants permission to retrieve information about all findings filters
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListFindingAggregations](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListFindingAggregations.html)  **
  - **Description:** Grants permission to retrieve statistical data and other information about Amazon Inspector findings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListFindings](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListFindings.html)  **
  - **Description:** Grants permission to retrieve a subset of information about one or more findings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMembers](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListMembers.html)  **
  - **Description:** Grants permission to retrieve information about the Amazon Inspector member accounts that are associated with an Inspector administrator account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to retrieve the tags for an Amazon Inspector resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListUsageTotals](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListUsageTotals.html)  **
  - **Description:** Grants permission to retrieve aggregated usage data for an account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ResetEncryptionKey](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ResetEncryptionKey.html)  **
  - **Description:** Grants permission to let a customer reset to use an Amazon-owned KMS key to encrypt code snippets with
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SearchVulnerabilities](https://docs.aws.amazon.com/inspector/v2/APIReference/API_SearchVulnerabilities.html)  **
  - **Description:** Grants permission to list Amazon Inspector coverage details for a specific vulnerability
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [SendCisSessionHealth](https://docs.aws.amazon.com/inspector/v2/APIReference/API_SendCisSessionHealth.html)  **
  - **Description:** Grants permission to send CIS health for a CIS scan
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SendCisSessionTelemetry](https://docs.aws.amazon.com/inspector/v2/APIReference/API_SendCisSessionTelemetry.html)  **
  - **Description:** Grants permission to send CIS telemetry for a CIS scan
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartCisSession](https://docs.aws.amazon.com/inspector/v2/APIReference/API_StartCisSession.html)  **
  - **Description:** Grants permission to start a CIS scan session
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartCodeSecurityScan](https://docs.aws.amazon.com/inspector/v2/APIReference/API_StartCodeSecurityScan.html)  **
  - **Description:** Grants permission to initiate a code security scan on a specified repository
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StopCisSession](https://docs.aws.amazon.com/inspector/v2/APIReference/API_StopCisSession.html)  **
  - **Description:** Grants permission to stop a CIS scan session
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/inspector/v2/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add or update the tags for an Amazon Inspector resource
  - **Resource types (\*required):** [CIS Scan Configuration](#list_inspector2-resource-CISScanConfiguration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_inspector2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_inspector2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_inspector2-aws_TagKeys)
  - **Resource types (\*required):** [Code Security Integration](#list_inspector2-resource-CodeSecurityIntegration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_inspector2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_inspector2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_inspector2-aws_TagKeys)
  - **Resource types (\*required):** [Code Security Scan Configuration](#list_inspector2-resource-CodeSecurityScanConfiguration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_inspector2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_inspector2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_inspector2-aws_TagKeys)
  - **Resource types (\*required):** [Connector](#list_inspector2-resource-Connector) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_inspector2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_inspector2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_inspector2-aws_TagKeys)
  - **Resource types (\*required):** [Filter](#list_inspector2-resource-Filter) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_inspector2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_inspector2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_inspector2-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/inspector/v2/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from an Amazon Inspector resource
  - **Resource types (\*required):** [CIS Scan Configuration](#list_inspector2-resource-CISScanConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_inspector2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_inspector2-aws_TagKeys)
  - **Resource types (\*required):** [Code Security Integration](#list_inspector2-resource-CodeSecurityIntegration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_inspector2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_inspector2-aws_TagKeys)
  - **Resource types (\*required):** [Code Security Scan Configuration](#list_inspector2-resource-CodeSecurityScanConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_inspector2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_inspector2-aws_TagKeys)
  - **Resource types (\*required):** [Connector](#list_inspector2-resource-Connector) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_inspector2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_inspector2-aws_TagKeys)
  - **Resource types (\*required):** [Filter](#list_inspector2-resource-Filter) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_inspector2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_inspector2-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateCisScanConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_UpdateCisScanConfiguration.html)  **
  - **Description:** Grants permission to update the settings for a CIS scan configuration
  - **Resource types (\*required):** [CIS Scan Configuration\*](#list_inspector2-resource-CISScanConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_inspector2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCodeSecurityIntegration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_UpdateCodeSecurityIntegration.html)  **
  - **Description:** Grants permission to update an existing code security integration
  - **Resource types (\*required):** [Code Security Integration\*](#list_inspector2-resource-CodeSecurityIntegration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_inspector2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCodeSecurityScanConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_UpdateCodeSecurityScanConfiguration.html)  **
  - **Description:** Grants permission to update an existing code security scan configuration
  - **Resource types (\*required):** [Code Security Scan Configuration\*](#list_inspector2-resource-CodeSecurityScanConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_inspector2-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_UpdateConfiguration.html)  **
  - **Description:** Grants permission to update information about the Amazon Inspector configuration settings for an AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateConnector](https://docs.aws.amazon.com/inspector/v2/APIReference/API_UpdateConnector.html)  **
  - **Description:** Grants permission to update a connector configured for scanning resources from a third-party cloud provider
  - **Resource types (\*required):** [Connector\*](#list_inspector2-resource-Connector)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_inspector2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_inspector2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_inspector2-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateConnectorScanConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_UpdateConnectorScanConfiguration.html)  **
  - **Description:** Grants permission to update scan configuration settings for resources associated with a connector
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateEc2DeepInspectionConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_UpdateEc2DeepInspectionConfiguration.html)  **
  - **Description:** Grants permission to update ec2 deep inspection configuration by delegated administrator, member and standalone account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateEncryptionKey](https://docs.aws.amazon.com/inspector/v2/APIReference/API_UpdateEncryptionKey.html)  **
  - **Description:** Grants permission to let a customer use a KMS key to encrypt code snippets with
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateFilter](https://docs.aws.amazon.com/inspector/v2/APIReference/API_UpdateFilter.html)  **
  - **Description:** Grants permission to update the settings for a findings filter
  - **Resource types (\*required):** [Filter\*](#list_inspector2-resource-Filter)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_inspector2-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_inspector2-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_inspector2-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateOrgEc2DeepInspectionConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_UpdateOrgEc2DeepInspectionConfiguration.html)  **
  - **Description:** Grants permission to update ec2 deep inspection configuration by delegated administrator for its associated member accounts
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateOrganizationConfiguration](https://docs.aws.amazon.com/inspector/v2/APIReference/API_UpdateOrganizationConfiguration.html)  **
  - **Description:** Grants permission to update Amazon Inspector configuration settings for an AWS organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by Amazon Inspector2
<a name="list_inspector2-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [CIS Scan Configuration](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html)  | arn:${Partition}:inspector2:${Region}:${Account}:owner/${OwnerId}/cis-configuration/${CISScanConfigurationId} | [aws:ResourceTag/${TagKey}](#list_inspector2-aws_ResourceTag___TagKey_) | 
|  [Code Security Integration](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html)  | arn:${Partition}:inspector2:${Region}:${Account}:codesecurity-integration/${CodeSecurityIntegrationId} | [aws:ResourceTag/${TagKey}](#list_inspector2-aws_ResourceTag___TagKey_) | 
|  [Code Security Scan Configuration](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html)  | arn:${Partition}:inspector2:${Region}:${Account}:owner/${OwnerId}/codesecurity-configuration/${CodeSecurityScanConfigurationId} | [aws:ResourceTag/${TagKey}](#list_inspector2-aws_ResourceTag___TagKey_) | 
|  [Connector](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html)  | arn:${Partition}:inspector2:${Region}:${Account}:connector/${ConnectorId} | [aws:ResourceTag/${TagKey}](#list_inspector2-aws_ResourceTag___TagKey_) | 
|  [Filter](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html)  | arn:${Partition}:inspector2:${Region}:${Account}:owner/${OwnerId}/filter/${FilterId} | [aws:ResourceTag/${TagKey}](#list_inspector2-aws_ResourceTag___TagKey_) | 
|  [Finding](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html)  | arn:${Partition}:inspector2:${Region}:${Account}:finding/${FindingId} |   | 

## Condition keys for Amazon Inspector2
<a name="list_inspector2-policy-keys"></a>

Amazon Inspector2 defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of tag keys in the request | ArrayOfString | 