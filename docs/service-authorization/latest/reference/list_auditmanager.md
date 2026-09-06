

# Actions, resources, and condition keys for AWS Audit Manager
<a name="list_auditmanager"></a>

AWS Audit Manager (service prefix: `auditmanager`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/audit-manager/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/audit-manager/latest/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/audit-manager/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/auditmanager/auditmanager.json) for this service.

**Topics**
+ [API operations defined by AWS Audit Manager](#list_auditmanager-operations)
+ [Actions defined by AWS Audit Manager](#list_auditmanager-actions-as-permissions)
+ [Resource types defined by AWS Audit Manager](#list_auditmanager-resources-for-iam-policies)
+ [Condition keys for AWS Audit Manager](#list_auditmanager-policy-keys)

## API operations defined by AWS Audit Manager
<a name="list_auditmanager-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_auditmanager-actions-as-permissions).




- **   AssociateAssessmentReportEvidenceFolder  **
  - **IAM action:**  [auditmanager:AssociateAssessmentReportEvidenceFolder](#list_auditmanager-action-AssociateAssessmentReportEvidenceFolder) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchAssociateAssessmentReportEvidence  **
  - **IAM action:**  [auditmanager:BatchAssociateAssessmentReportEvidence](#list_auditmanager-action-BatchAssociateAssessmentReportEvidence) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchCreateDelegationByAssessment  **
  - **IAM action:**  [auditmanager:BatchCreateDelegationByAssessment](#list_auditmanager-action-BatchCreateDelegationByAssessment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchDeleteDelegationByAssessment  **
  - **IAM action:**  [auditmanager:BatchDeleteDelegationByAssessment](#list_auditmanager-action-BatchDeleteDelegationByAssessment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchDisassociateAssessmentReportEvidence  **
  - **IAM action:**  [auditmanager:BatchDisassociateAssessmentReportEvidence](#list_auditmanager-action-BatchDisassociateAssessmentReportEvidence) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchImportEvidenceToAssessmentControl  **
  - **IAM action:**  [auditmanager:BatchImportEvidenceToAssessmentControl](#list_auditmanager-action-BatchImportEvidenceToAssessmentControl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAssessment  **
  - **IAM action:**  [auditmanager:CreateAssessment](#list_auditmanager-action-CreateAssessment)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [auditmanager:TagResource](#list_auditmanager-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateAssessmentFramework  **
  - **IAM action:**  [auditmanager:CreateAssessmentFramework](#list_auditmanager-action-CreateAssessmentFramework)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [auditmanager:TagResource](#list_auditmanager-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateAssessmentReport  **
  - **IAM action:**  [auditmanager:CreateAssessmentReport](#list_auditmanager-action-CreateAssessmentReport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateControl  **
  - **IAM action:**  [auditmanager:CreateControl](#list_auditmanager-action-CreateControl)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [auditmanager:TagResource](#list_auditmanager-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteAssessment  **
  - **IAM action:**  [auditmanager:DeleteAssessment](#list_auditmanager-action-DeleteAssessment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAssessmentFramework  **
  - **IAM action:**  [auditmanager:DeleteAssessmentFramework](#list_auditmanager-action-DeleteAssessmentFramework) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAssessmentFrameworkShare  **
  - **IAM action:**  [auditmanager:DeleteAssessmentFrameworkShare](#list_auditmanager-action-DeleteAssessmentFrameworkShare) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAssessmentReport  **
  - **IAM action:**  [auditmanager:DeleteAssessmentReport](#list_auditmanager-action-DeleteAssessmentReport) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteControl  **
  - **IAM action:**  [auditmanager:DeleteControl](#list_auditmanager-action-DeleteControl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeregisterAccount  **
  - **IAM action:**  [auditmanager:DeregisterAccount](#list_auditmanager-action-DeregisterAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeregisterOrganizationAdminAccount  **
  - **IAM action:**  [auditmanager:DeregisterOrganizationAdminAccount](#list_auditmanager-action-DeregisterOrganizationAdminAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateAssessmentReportEvidenceFolder  **
  - **IAM action:**  [auditmanager:DisassociateAssessmentReportEvidenceFolder](#list_auditmanager-action-DisassociateAssessmentReportEvidenceFolder) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAccountStatus  **
  - **IAM action:**  [auditmanager:GetAccountStatus](#list_auditmanager-action-GetAccountStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAssessment  **
  - **IAM action:**  [auditmanager:GetAssessment](#list_auditmanager-action-GetAssessment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAssessmentFramework  **
  - **IAM action:**  [auditmanager:GetAssessmentFramework](#list_auditmanager-action-GetAssessmentFramework) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAssessmentReportUrl  **
  - **IAM action:**  [auditmanager:GetAssessmentReportUrl](#list_auditmanager-action-GetAssessmentReportUrl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetChangeLogs  **
  - **IAM action:**  [auditmanager:GetChangeLogs](#list_auditmanager-action-GetChangeLogs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetControl  **
  - **IAM action:**  [auditmanager:GetControl](#list_auditmanager-action-GetControl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDelegations  **
  - **IAM action:**  [auditmanager:GetDelegations](#list_auditmanager-action-GetDelegations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetEvidence  **
  - **IAM action:**  [auditmanager:GetEvidence](#list_auditmanager-action-GetEvidence) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEvidenceByEvidenceFolder  **
  - **IAM action:**  [auditmanager:GetEvidenceByEvidenceFolder](#list_auditmanager-action-GetEvidenceByEvidenceFolder) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEvidenceFileUploadUrl  **
  - **IAM action:**  [auditmanager:GetEvidenceFileUploadUrl](#list_auditmanager-action-GetEvidenceFileUploadUrl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEvidenceFolder  **
  - **IAM action:**  [auditmanager:GetEvidenceFolder](#list_auditmanager-action-GetEvidenceFolder) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEvidenceFoldersByAssessment  **
  - **IAM action:**  [auditmanager:GetEvidenceFoldersByAssessment](#list_auditmanager-action-GetEvidenceFoldersByAssessment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEvidenceFoldersByAssessmentControl  **
  - **IAM action:**  [auditmanager:GetEvidenceFoldersByAssessmentControl](#list_auditmanager-action-GetEvidenceFoldersByAssessmentControl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetInsights  **
  - **IAM action:**  [auditmanager:GetInsights](#list_auditmanager-action-GetInsights) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetInsightsByAssessment  **
  - **IAM action:**  [auditmanager:GetInsightsByAssessment](#list_auditmanager-action-GetInsightsByAssessment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOrganizationAdminAccount  **
  - **IAM action:**  [auditmanager:GetOrganizationAdminAccount](#list_auditmanager-action-GetOrganizationAdminAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetServicesInScope  **
  - **IAM action:**  [auditmanager:GetServicesInScope](#list_auditmanager-action-GetServicesInScope) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSettings  **
  - **IAM action:**  [auditmanager:GetSettings](#list_auditmanager-action-GetSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAssessmentControlInsightsByControlDomain  **
  - **IAM action:**  [auditmanager:ListAssessmentControlInsightsByControlDomain](#list_auditmanager-action-ListAssessmentControlInsightsByControlDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAssessmentFrameworkShareRequests  **
  - **IAM action:**  [auditmanager:ListAssessmentFrameworkShareRequests](#list_auditmanager-action-ListAssessmentFrameworkShareRequests) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAssessmentFrameworks  **
  - **IAM action:**  [auditmanager:ListAssessmentFrameworks](#list_auditmanager-action-ListAssessmentFrameworks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAssessmentReports  **
  - **IAM action:**  [auditmanager:ListAssessmentReports](#list_auditmanager-action-ListAssessmentReports) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAssessments  **
  - **IAM action:**  [auditmanager:ListAssessments](#list_auditmanager-action-ListAssessments) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListControlDomainInsights  **
  - **IAM action:**  [auditmanager:ListControlDomainInsights](#list_auditmanager-action-ListControlDomainInsights) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListControlDomainInsightsByAssessment  **
  - **IAM action:**  [auditmanager:ListControlDomainInsightsByAssessment](#list_auditmanager-action-ListControlDomainInsightsByAssessment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListControlInsightsByControlDomain  **
  - **IAM action:**  [auditmanager:ListControlInsightsByControlDomain](#list_auditmanager-action-ListControlInsightsByControlDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListControls  **
  - **IAM action:**  [auditmanager:ListControls](#list_auditmanager-action-ListControls) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListKeywordsForDataSource  **
  - **IAM action:**  [auditmanager:ListKeywordsForDataSource](#list_auditmanager-action-ListKeywordsForDataSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListNotifications  **
  - **IAM action:**  [auditmanager:ListNotifications](#list_auditmanager-action-ListNotifications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [auditmanager:ListTagsForResource](#list_auditmanager-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   RegisterAccount  **
  - **IAM action:**  [auditmanager:RegisterAccount](#list_auditmanager-action-RegisterAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RegisterOrganizationAdminAccount  **
  - **IAM action:**  [auditmanager:RegisterOrganizationAdminAccount](#list_auditmanager-action-RegisterOrganizationAdminAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartAssessmentFrameworkShare  **
  - **IAM action:**  [auditmanager:StartAssessmentFrameworkShare](#list_auditmanager-action-StartAssessmentFrameworkShare) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [auditmanager:TagResource](#list_auditmanager-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [auditmanager:UntagResource](#list_auditmanager-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAssessment  **
  - **IAM action:**  [auditmanager:UpdateAssessment](#list_auditmanager-action-UpdateAssessment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAssessmentControl  **
  - **IAM action:**  [auditmanager:UpdateAssessmentControl](#list_auditmanager-action-UpdateAssessmentControl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAssessmentControlSetStatus  **
  - **IAM action:**  [auditmanager:UpdateAssessmentControlSetStatus](#list_auditmanager-action-UpdateAssessmentControlSetStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAssessmentFramework  **
  - **IAM action:**  [auditmanager:UpdateAssessmentFramework](#list_auditmanager-action-UpdateAssessmentFramework) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAssessmentFrameworkShare  **
  - **IAM action:**  [auditmanager:UpdateAssessmentFrameworkShare](#list_auditmanager-action-UpdateAssessmentFrameworkShare) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAssessmentStatus  **
  - **IAM action:**  [auditmanager:UpdateAssessmentStatus](#list_auditmanager-action-UpdateAssessmentStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateControl  **
  - **IAM action:**  [auditmanager:UpdateControl](#list_auditmanager-action-UpdateControl) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSettings  **
  - **IAM action:**  [auditmanager:UpdateSettings](#list_auditmanager-action-UpdateSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ValidateAssessmentReportIntegrity  **
  - **IAM action:**  [auditmanager:ValidateAssessmentReportIntegrity](#list_auditmanager-action-ValidateAssessmentReportIntegrity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read



## Actions defined by AWS Audit Manager
<a name="list_auditmanager-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateAssessmentReportEvidenceFolder](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_AssociateAssessmentReportEvidenceFolder.html)  **
  - **Description:** Grants permission to associate an evidence folder with an assessment report in AWS Audit Manager
  - **Resource types (\*required):** [assessment\*](#list_auditmanager-resource-assessment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_auditmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchAssociateAssessmentReportEvidence](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_BatchAssociateAssessmentReportEvidence.html)  **
  - **Description:** Grants permission to associate a list of evidence to an assessment report in AWS Audit Manager
  - **Resource types (\*required):** [assessment\*](#list_auditmanager-resource-assessment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_auditmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchCreateDelegationByAssessment](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_BatchCreateDelegationByAssessment.html)  **
  - **Description:** Grants permission to create delegations for an assessment in AWS Audit Manager
  - **Resource types (\*required):** [assessment\*](#list_auditmanager-resource-assessment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_auditmanager-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [assessmentControlSet\*](#list_auditmanager-resource-assessmentControlSet) / **Condition keys:**  
  - **Access level:** Write

- **   [BatchDeleteDelegationByAssessment](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_BatchDeleteDelegationByAssessment.html)  **
  - **Description:** Grants permission to delete delegations for an assessment in AWS Audit Manager
  - **Resource types (\*required):** [assessment\*](#list_auditmanager-resource-assessment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_auditmanager-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [assessmentControlSet\*](#list_auditmanager-resource-assessmentControlSet) / **Condition keys:**  
  - **Access level:** Write

- **   [BatchDisassociateAssessmentReportEvidence](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_BatchDisassociateAssessmentReportEvidence.html)  **
  - **Description:** Grants permission to disassociate a list of evidence from an assessment report in AWS Audit Manager
  - **Resource types (\*required):** [assessment\*](#list_auditmanager-resource-assessment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_auditmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchImportEvidenceToAssessmentControl](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_BatchImportEvidenceToAssessmentControl.html)  **
  - **Description:** Grants permission to import a list of evidence to an assessment control in AWS Audit Manager
  - **Resource types (\*required):** [assessmentControlSet\*](#list_auditmanager-resource-assessmentControlSet)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateAssessment](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_CreateAssessment.html)  **
  - **Description:** Grants permission to create an assessment to be used with AWS Audit Manager
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_auditmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_auditmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_auditmanager-aws_TagKeys)
  - **Access level:** Write

- **   [CreateAssessmentFramework](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_CreateAssessmentFramework.html)  **
  - **Description:** Grants permission to create a framework for use in AWS Audit Manager
  - **Resource types (\*required):** [assessmentFramework\*](#list_auditmanager-resource-assessmentFramework) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_auditmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_auditmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_auditmanager-aws_TagKeys)
  - **Resource types (\*required):** [control\*](#list_auditmanager-resource-control) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_auditmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_auditmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_auditmanager-aws_TagKeys)
  - **Access level:** Write

- **   [CreateAssessmentReport](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_CreateAssessmentReport.html)  **
  - **Description:** Grants permission to create an assessment report in AWS Audit Manager
  - **Resource types (\*required):** [assessment\*](#list_auditmanager-resource-assessment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_auditmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateControl](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_CreateControl.html)  **
  - **Description:** Grants permission to create a control to be used in AWS Audit Manager
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_auditmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_auditmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_auditmanager-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteAssessment](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_DeleteAssessment.html)  **
  - **Description:** Grants permission to delete an assessment in AWS Audit Manager
  - **Resource types (\*required):** [assessment\*](#list_auditmanager-resource-assessment)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_auditmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_auditmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_auditmanager-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteAssessmentFramework](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_DeleteAssessmentFramework.html)  **
  - **Description:** Grants permission to delete an assessment framework in AWS Audit Manager
  - **Resource types (\*required):** [assessmentFramework\*](#list_auditmanager-resource-assessmentFramework)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_auditmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_auditmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_auditmanager-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteAssessmentFrameworkShare](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_DeleteAssessmentFrameworkShare.html)  **
  - **Description:** Grants permission to delete a share request for a custom framework in AWS Audit Manager
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteAssessmentReport](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_DeleteAssessmentReport.html)  **
  - **Description:** Grants permission to delete an assessment report in AWS Audit Manager
  - **Resource types (\*required):** [assessment\*](#list_auditmanager-resource-assessment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_auditmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteControl](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_DeleteControl.html)  **
  - **Description:** Grants permission to delete a control in AWS Audit Manager
  - **Resource types (\*required):** [control\*](#list_auditmanager-resource-control)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_auditmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_auditmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_auditmanager-aws_TagKeys)
  - **Access level:** Write

- **   [DeregisterAccount](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_DeregisterAccount.html)  **
  - **Description:** Grants permission to deregister an account in AWS Audit Manager
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeregisterOrganizationAdminAccount](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_DeregisterOrganizationAdminAccount.html)  **
  - **Description:** Grants permission to deregister the delegated administrator account for AWS Audit Manager
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DisassociateAssessmentReportEvidenceFolder](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_DisassociateAssessmentReportEvidenceFolder.html)  **
  - **Description:** Grants permission to disassociate an evidence folder from an assessment report in AWS Audit Manager
  - **Resource types (\*required):** [assessment\*](#list_auditmanager-resource-assessment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_auditmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetAccountStatus](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetAccountStatus.html)  **
  - **Description:** Grants permission to get the status of an account in AWS Audit Manager
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetAssessment](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetAssessment.html)  **
  - **Description:** Grants permission to get an assessment created in AWS Audit Manager
  - **Resource types (\*required):** [assessment\*](#list_auditmanager-resource-assessment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_auditmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAssessmentFramework](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetAssessmentFramework.html)  **
  - **Description:** Grants permission to get an assessment framework in AWS Audit Manager
  - **Resource types (\*required):** [assessmentFramework\*](#list_auditmanager-resource-assessmentFramework)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_auditmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAssessmentReportUrl](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetAssessmentReportUrl.html)  **
  - **Description:** Grants permission to get the URL for an assessment report in AWS Audit Manager
  - **Resource types (\*required):** [assessment\*](#list_auditmanager-resource-assessment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_auditmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetChangeLogs](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetChangeLogs.html)  **
  - **Description:** Grants permission to get changelogs for an assessment in AWS Audit Manager
  - **Resource types (\*required):** [assessment\*](#list_auditmanager-resource-assessment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_auditmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetControl](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetControl.html)  **
  - **Description:** Grants permission to get a control in AWS Audit Manager
  - **Resource types (\*required):** [control\*](#list_auditmanager-resource-control)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_auditmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDelegations](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetDelegations.html)  **
  - **Description:** Grants permission to get all delegations in AWS Audit Manager
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [GetEvidence](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetEvidence.html)  **
  - **Description:** Grants permission to get evidence from AWS Audit Manager
  - **Resource types (\*required):** [assessmentControlSet\*](#list_auditmanager-resource-assessmentControlSet)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetEvidenceByEvidenceFolder](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetEvidenceByEvidenceFolder.html)  **
  - **Description:** Grants permission to get all the evidence from an evidence folder in AWS Audit Manager
  - **Resource types (\*required):** [assessmentControlSet\*](#list_auditmanager-resource-assessmentControlSet)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetEvidenceFileUploadUrl](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetEvidenceFileUploadUrl.html)  **
  - **Description:** Grants permission to get a presigned Amazon S3 URL that can be used to upload a file as manual evidence
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetEvidenceFolder](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetEvidenceFolder.html)  **
  - **Description:** Grants permission to get the evidence folder from AWS Audit Manager
  - **Resource types (\*required):** [assessmentControlSet\*](#list_auditmanager-resource-assessmentControlSet)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetEvidenceFoldersByAssessment](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetEvidenceFoldersByAssessment.html)  **
  - **Description:** Grants permission to get the evidence folders from an assessment in AWS Audit Manager
  - **Resource types (\*required):** [assessment\*](#list_auditmanager-resource-assessment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_auditmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEvidenceFoldersByAssessmentControl](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetEvidenceFoldersByAssessmentControl.html)  **
  - **Description:** Grants permission to get the evidence folders from an assessment control in AWS Audit Manager
  - **Resource types (\*required):** [assessmentControlSet\*](#list_auditmanager-resource-assessmentControlSet)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetInsights](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetInsights.html)  **
  - **Description:** Grants permission to get analytics data for all active assessments
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetInsightsByAssessment](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetInsightsByAssessment.html)  **
  - **Description:** Grants permission to get analytics data for a specific active assessment
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetOrganizationAdminAccount](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetOrganizationAdminAccount.html)  **
  - **Description:** Grants permission to get the delegated administrator account in AWS Audit Manager
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetServicesInScope](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetServicesInScope.html)  **
  - **Description:** Grants permission to get the services in scope for an assessment in AWS Audit Manager
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSettings](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetSettings.html)  **
  - **Description:** Grants permission to get all settings configured in AWS Audit Manager
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListAssessmentControlInsightsByControlDomain](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListAssessmentControlInsightsByControlDomain.html)  **
  - **Description:** Grants permission to list analytics data for controls in a specific control domain and active assessment
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAssessmentFrameworkShareRequests](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListAssessmentFrameworkShareRequests.html)  **
  - **Description:** Grants permission to list all sent or received share requests for custom frameworks in AWS Audit Manager
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAssessmentFrameworks](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListAssessmentFrameworks.html)  **
  - **Description:** Grants permission to list all assessment frameworks in AWS Audit Manager
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAssessmentReports](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListAssessmentReports.html)  **
  - **Description:** Grants permission to list all assessment reports in AWS Audit Manager
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAssessments](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListAssessments.html)  **
  - **Description:** Grants permission to list all assessments in AWS Audit Manager
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListControlDomainInsights](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListControlDomainInsights.html)  **
  - **Description:** Grants permission to list analytics data for control domains across all active assessments
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListControlDomainInsightsByAssessment](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListControlDomainInsightsByAssessment.html)  **
  - **Description:** Grants permission to list analytics data for control domains in a specific active assessment
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListControlInsightsByControlDomain](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListControlInsightsByControlDomain.html)  **
  - **Description:** Grants permission to list analytics data for controls in a specific control domain across all active assessments
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListControls](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListControls.html)  **
  - **Description:** Grants permission to list all controls in AWS Audit Manager
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListKeywordsForDataSource](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListKeywordsForDataSource.html)  **
  - **Description:** Grants permission to list all the data source keywords in AWS Audit Manager
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListNotifications](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListNotifications.html)  **
  - **Description:** Grants permission to list all notifications in AWS Audit Manager
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for an AWS Audit Manager resource
  - **Resource types (\*required):** [assessment](#list_auditmanager-resource-assessment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_auditmanager-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [control](#list_auditmanager-resource-control) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_auditmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [RegisterAccount](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_RegisterAccount.html)  **
  - **Description:** Grants permission to register an account in AWS Audit Manager
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [RegisterOrganizationAdminAccount](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_RegisterOrganizationAdminAccount.html)  **
  - **Description:** Grants permission to register an account within the organization as the delegated administrator for AWS Audit Manager
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartAssessmentFrameworkShare](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_StartAssessmentFrameworkShare.html)  **
  - **Description:** Grants permission to create a share request for a custom framework in AWS Audit Manager
  - **Resource types (\*required):** [assessmentFramework\*](#list_auditmanager-resource-assessmentFramework)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_auditmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag an AWS Audit Manager resource
  - **Resource types (\*required):** [assessment](#list_auditmanager-resource-assessment) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_auditmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_auditmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_auditmanager-aws_TagKeys)
  - **Resource types (\*required):** [assessmentFramework](#list_auditmanager-resource-assessmentFramework) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_auditmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_auditmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_auditmanager-aws_TagKeys)
  - **Resource types (\*required):** [control](#list_auditmanager-resource-control) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_auditmanager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_auditmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_auditmanager-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag an AWS Audit Manager resource
  - **Resource types (\*required):** [assessment](#list_auditmanager-resource-assessment) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_auditmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_auditmanager-aws_TagKeys)
  - **Resource types (\*required):** [assessmentFramework](#list_auditmanager-resource-assessmentFramework) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_auditmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_auditmanager-aws_TagKeys)
  - **Resource types (\*required):** [control](#list_auditmanager-resource-control) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_auditmanager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_auditmanager-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAssessment](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_UpdateAssessment.html)  **
  - **Description:** Grants permission to update an assessment in AWS Audit Manager
  - **Resource types (\*required):** [assessment\*](#list_auditmanager-resource-assessment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_auditmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAssessmentControl](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_UpdateAssessmentControl.html)  **
  - **Description:** Grants permission to update an assessment control in AWS Audit Manager
  - **Resource types (\*required):** [assessmentControlSet\*](#list_auditmanager-resource-assessmentControlSet)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateAssessmentControlSetStatus](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_UpdateAssessmentControlSetStatus.html)  **
  - **Description:** Grants permission to update the status of an assessment control set in AWS Audit Manager
  - **Resource types (\*required):** [assessmentControlSet\*](#list_auditmanager-resource-assessmentControlSet)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateAssessmentFramework](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_UpdateAssessmentFramework.html)  **
  - **Description:** Grants permission to update an assessment framework in AWS Audit Manager
  - **Resource types (\*required):** [assessmentFramework\*](#list_auditmanager-resource-assessmentFramework) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_auditmanager-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [control\*](#list_auditmanager-resource-control) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_auditmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAssessmentFrameworkShare](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_UpdateAssessmentFrameworkShare.html)  **
  - **Description:** Grants permission to update a share request for a custom framework in AWS Audit Manager
  - **Resource types (\*required):** [assessmentFramework\*](#list_auditmanager-resource-assessmentFramework)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_auditmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAssessmentStatus](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_UpdateAssessmentStatus.html)  **
  - **Description:** Grants permission to update the status of an assessment in AWS Audit Manager
  - **Resource types (\*required):** [assessment\*](#list_auditmanager-resource-assessment)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_auditmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateControl](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_UpdateControl.html)  **
  - **Description:** Grants permission to update a control in AWS Audit Manager
  - **Resource types (\*required):** [control\*](#list_auditmanager-resource-control)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_auditmanager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSettings](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_UpdateSettings.html)  **
  - **Description:** Grants permission to update settings in AWS Audit Manager
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ValidateAssessmentReportIntegrity](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ValidateAssessmentReportIntegrity.html)  **
  - **Description:** Grants permission to validate the integrity of an assessment report in AWS Audit Manager
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read



## Resource types defined by AWS Audit Manager
<a name="list_auditmanager-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [assessment](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_Assessment.html)  | arn:${Partition}:auditmanager:${Region}:${Account}:assessment/${AssessmentId} | [aws:ResourceTag/${TagKey}](#list_auditmanager-aws_ResourceTag___TagKey_) | 
|  [assessmentControlSet](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_AssessmentControlSet.html)  | arn:${Partition}:auditmanager:${Region}:${Account}:assessment/${AssessmentId}/controlSet/${ControlSetId} |   | 
|  [assessmentFramework](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_AssessmentFramework.html)  | arn:${Partition}:auditmanager:${Region}:${Account}:assessmentFramework/${AssessmentFrameworkId} | [aws:ResourceTag/${TagKey}](#list_auditmanager-aws_ResourceTag___TagKey_) | 
|  [control](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_Control.html)  | arn:${Partition}:auditmanager:${Region}:${Account}:control/${ControlId} | [aws:ResourceTag/${TagKey}](#list_auditmanager-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Audit Manager
<a name="list_auditmanager-policy-keys"></a>

AWS Audit Manager defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 