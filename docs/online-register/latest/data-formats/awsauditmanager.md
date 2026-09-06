

# Data retrieval APIs for AWS Audit Manager
<a name="awsauditmanager"></a>

AWS Audit Manager provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="auditmanager-GetAccountStatus"></a>[GetAccountStatus](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetAccountStatus.html) | Get the status of an account in AWS Audit Manager | Read | 
| <a name="auditmanager-GetAssessment"></a>[GetAssessment](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetAssessment.html) | Get an assessment created in AWS Audit Manager | Read | 
| <a name="auditmanager-GetAssessmentFramework"></a>[GetAssessmentFramework](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetAssessmentFramework.html) | Get an assessment framework in AWS Audit Manager | Read | 
| <a name="auditmanager-GetAssessmentReportUrl"></a>[GetAssessmentReportUrl](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetAssessmentReportUrl.html) | Get the URL for an assessment report in AWS Audit Manager | Read | 
| <a name="auditmanager-GetChangeLogs"></a>[GetChangeLogs](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetChangeLogs.html) | Get changelogs for an assessment in AWS Audit Manager | Read | 
| <a name="auditmanager-GetControl"></a>[GetControl](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetControl.html) | Get a control in AWS Audit Manager | Read | 
| <a name="auditmanager-GetDelegations"></a>[GetDelegations](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetDelegations.html) | Get all delegations in AWS Audit Manager | List | 
| <a name="auditmanager-GetEvidence"></a>[GetEvidence](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetEvidence.html) | Get evidence from AWS Audit Manager | Read | 
| <a name="auditmanager-GetEvidenceByEvidenceFolder"></a>[GetEvidenceByEvidenceFolder](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetEvidenceByEvidenceFolder.html) | Get all the evidence from an evidence folder in AWS Audit Manager | Read | 
| <a name="auditmanager-GetEvidenceFileUploadUrl"></a>[GetEvidenceFileUploadUrl](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetEvidenceFileUploadUrl.html) | Get a presigned Amazon S3 URL that can be used to upload a file as manual evidence | Read | 
| <a name="auditmanager-GetEvidenceFolder"></a>[GetEvidenceFolder](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetEvidenceFolder.html) | Get the evidence folder from AWS Audit Manager | Read | 
| <a name="auditmanager-GetEvidenceFoldersByAssessment"></a>[GetEvidenceFoldersByAssessment](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetEvidenceFoldersByAssessment.html) | Get the evidence folders from an assessment in AWS Audit Manager | Read | 
| <a name="auditmanager-GetEvidenceFoldersByAssessmentControl"></a>[GetEvidenceFoldersByAssessmentControl](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetEvidenceFoldersByAssessmentControl.html) | Get the evidence folders from an assessment control in AWS Audit Manager | Read | 
| <a name="auditmanager-GetInsights"></a>[GetInsights](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetInsights.html) | Get analytics data for all active assessments | Read | 
| <a name="auditmanager-GetInsightsByAssessment"></a>[GetInsightsByAssessment](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetInsightsByAssessment.html) | Get analytics data for a specific active assessment | Read | 
| <a name="auditmanager-GetOrganizationAdminAccount"></a>[GetOrganizationAdminAccount](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetOrganizationAdminAccount.html) | Get the delegated administrator account in AWS Audit Manager | Read | 
| <a name="auditmanager-GetServicesInScope"></a>[GetServicesInScope](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetServicesInScope.html) | Get the services in scope for an assessment in AWS Audit Manager | Read | 
| <a name="auditmanager-GetSettings"></a>[GetSettings](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetSettings.html) | Get all settings configured in AWS Audit Manager | Read | 
| <a name="auditmanager-ListAssessmentControlInsightsByControlDomain"></a>[ListAssessmentControlInsightsByControlDomain](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListAssessmentControlInsightsByControlDomain.html) | List analytics data for controls in a specific control domain and active assessment | List | 
| <a name="auditmanager-ListAssessmentFrameworkShareRequests"></a>[ListAssessmentFrameworkShareRequests](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListAssessmentFrameworkShareRequests.html) | List all sent or received share requests for custom frameworks in AWS Audit Manager | List | 
| <a name="auditmanager-ListAssessmentFrameworks"></a>[ListAssessmentFrameworks](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListAssessmentFrameworks.html) | List all assessment frameworks in AWS Audit Manager | List | 
| <a name="auditmanager-ListAssessmentReports"></a>[ListAssessmentReports](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListAssessmentReports.html) | List all assessment reports in AWS Audit Manager | List | 
| <a name="auditmanager-ListAssessments"></a>[ListAssessments](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListAssessments.html) | List all assessments in AWS Audit Manager | List | 
| <a name="auditmanager-ListControlDomainInsights"></a>[ListControlDomainInsights](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListControlDomainInsights.html) | List analytics data for control domains across all active assessments | List | 
| <a name="auditmanager-ListControlDomainInsightsByAssessment"></a>[ListControlDomainInsightsByAssessment](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListControlDomainInsightsByAssessment.html) | List analytics data for control domains in a specific active assessment | List | 
| <a name="auditmanager-ListControlInsightsByControlDomain"></a>[ListControlInsightsByControlDomain](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListControlInsightsByControlDomain.html) | List analytics data for controls in a specific control domain across all active assessments | List | 
| <a name="auditmanager-ListControls"></a>[ListControls](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListControls.html) | List all controls in AWS Audit Manager | List | 
| <a name="auditmanager-ListKeywordsForDataSource"></a>[ListKeywordsForDataSource](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListKeywordsForDataSource.html) | List all the data source keywords in AWS Audit Manager | List | 
| <a name="auditmanager-ListNotifications"></a>[ListNotifications](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListNotifications.html) | List all notifications in AWS Audit Manager | List | 
| <a name="auditmanager-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListTagsForResource.html) | List tags for an AWS Audit Manager resource | Read | 
| <a name="auditmanager-ValidateAssessmentReportIntegrity"></a>[ValidateAssessmentReportIntegrity](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ValidateAssessmentReportIntegrity.html) | Validate the integrity of an assessment report in AWS Audit Manager | Read | 