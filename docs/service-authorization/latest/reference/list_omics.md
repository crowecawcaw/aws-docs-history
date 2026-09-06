

# Actions, resources, and condition keys for AWS HealthOmics
<a name="list_omics"></a>

AWS HealthOmics (service prefix: `omics`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/omics/latest/dev/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/omics/latest/api/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/omics/latest/dev/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/omics/omics.json) for this service.

**Topics**
+ [API operations defined by AWS HealthOmics](#list_omics-operations)
+ [Actions defined by AWS HealthOmics](#list_omics-actions-as-permissions)
+ [Resource types defined by AWS HealthOmics](#list_omics-resources-for-iam-policies)
+ [Condition keys for AWS HealthOmics](#list_omics-policy-keys)

## API operations defined by AWS HealthOmics
<a name="list_omics-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_omics-actions-as-permissions).




- **   AbortMultipartReadSetUpload  **
  - **IAM action:**  [omics:AbortMultipartReadSetUpload](#list_omics-action-AbortMultipartReadSetUpload) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AcceptShare  **
  - **IAM action:**  [omics:AcceptShare](#list_omics-action-AcceptShare) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchDeleteReadSet  **
  - **IAM action:**  [omics:BatchDeleteReadSet](#list_omics-action-BatchDeleteReadSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelAnnotationImportJob  **
  - **IAM action:**  [omics:CancelAnnotationImportJob](#list_omics-action-CancelAnnotationImportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelRun  **
  - **IAM action:**  [omics:CancelRun](#list_omics-action-CancelRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelRunBatch  **
  - **IAM action:**  [omics:CancelRunBatch](#list_omics-action-CancelRunBatch) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelVariantImportJob  **
  - **IAM action:**  [omics:CancelVariantImportJob](#list_omics-action-CancelVariantImportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CompleteMultipartReadSetUpload  **
  - **IAM action:**  [omics:CompleteMultipartReadSetUpload](#list_omics-action-CompleteMultipartReadSetUpload) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateAnnotationStore  **
  - **IAM action:**  [omics:CreateAnnotationStore](#list_omics-action-CreateAnnotationStore)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [omics:TagResource](#list_omics-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateAnnotationStoreVersion  **
  - **IAM action:**  [omics:CreateAnnotationStoreVersion](#list_omics-action-CreateAnnotationStoreVersion)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [omics:TagResource](#list_omics-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateConfiguration  **
  - **IAM action:**  [omics:CreateConfiguration](#list_omics-action-CreateConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [omics:TagResource](#list_omics-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [codeconnections:PassConnection](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-passconnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [ec2:DescribeSecurityGroups](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSecurityGroups.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [ec2:DescribeSubnets](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSubnets.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** omics.amazonaws.com / **Access level:** Write

- **   CreateMultipartReadSetUpload  **
  - **IAM action:**  [omics:CreateMultipartReadSetUpload](#list_omics-action-CreateMultipartReadSetUpload)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [omics:TagResource](#list_omics-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateReferenceStore  **
  - **IAM action:**  [omics:CreateReferenceStore](#list_omics-action-CreateReferenceStore)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [omics:TagResource](#list_omics-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateRunCache  **
  - **IAM action:**  [omics:CreateRunCache](#list_omics-action-CreateRunCache)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [omics:TagResource](#list_omics-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateRunGroup  **
  - **IAM action:**  [omics:CreateRunGroup](#list_omics-action-CreateRunGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [omics:TagResource](#list_omics-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateSequenceStore  **
  - **IAM action:**  [omics:CreateSequenceStore](#list_omics-action-CreateSequenceStore)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [omics:TagResource](#list_omics-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateShare  **
  - **IAM action:**  [omics:CreateShare](#list_omics-action-CreateShare) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateVariantStore  **
  - **IAM action:**  [omics:CreateVariantStore](#list_omics-action-CreateVariantStore)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [omics:TagResource](#list_omics-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateWorkflow  **
  - **IAM action:**  [omics:CreateWorkflow](#list_omics-action-CreateWorkflow)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [omics:TagResource](#list_omics-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [codeconnections:PassConnection](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-passconnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   CreateWorkflowVersion  **
  - **IAM action:**  [omics:CreateWorkflowVersion](#list_omics-action-CreateWorkflowVersion)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [omics:TagResource](#list_omics-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [codeconnections:PassConnection](https://docs.aws.amazon.com/dtconsole/latest/userguide/security-iam.html#permissions-reference-connections-passconnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   DeleteAnnotationStore  **
  - **IAM action:**  [omics:DeleteAnnotationStore](#list_omics-action-DeleteAnnotationStore) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAnnotationStoreVersions  **
  - **IAM action:**  [omics:DeleteAnnotationStoreVersions](#list_omics-action-DeleteAnnotationStoreVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteBatch  **
  - **IAM action:**  [omics:DeleteBatch](#list_omics-action-DeleteBatch) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConfiguration  **
  - **IAM action:**  [omics:DeleteConfiguration](#list_omics-action-DeleteConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteReference  **
  - **IAM action:**  [omics:DeleteReference](#list_omics-action-DeleteReference) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteReferenceStore  **
  - **IAM action:**  [omics:DeleteReferenceStore](#list_omics-action-DeleteReferenceStore) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRun  **
  - **IAM action:**  [omics:DeleteRun](#list_omics-action-DeleteRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRunBatch  **
  - **IAM action:**  [omics:DeleteRunBatch](#list_omics-action-DeleteRunBatch) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRunCache  **
  - **IAM action:**  [omics:DeleteRunCache](#list_omics-action-DeleteRunCache) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRunGroup  **
  - **IAM action:**  [omics:DeleteRunGroup](#list_omics-action-DeleteRunGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteS3AccessPolicy  **
  - **IAM action:**  [omics:DeleteS3AccessPolicy](#list_omics-action-DeleteS3AccessPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSequenceStore  **
  - **IAM action:**  [omics:DeleteSequenceStore](#list_omics-action-DeleteSequenceStore) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteShare  **
  - **IAM action:**  [omics:DeleteShare](#list_omics-action-DeleteShare) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteVariantStore  **
  - **IAM action:**  [omics:DeleteVariantStore](#list_omics-action-DeleteVariantStore) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWorkflow  **
  - **IAM action:**  [omics:DeleteWorkflow](#list_omics-action-DeleteWorkflow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWorkflowVersion  **
  - **IAM action:**  [omics:DeleteWorkflowVersion](#list_omics-action-DeleteWorkflowVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAnnotationImportJob  **
  - **IAM action:**  [omics:GetAnnotationImportJob](#list_omics-action-GetAnnotationImportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAnnotationStore  **
  - **IAM action:**  [omics:GetAnnotationStore](#list_omics-action-GetAnnotationStore) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAnnotationStoreVersion  **
  - **IAM action:**  [omics:GetAnnotationStoreVersion](#list_omics-action-GetAnnotationStoreVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBatch  **
  - **IAM action:**  [omics:GetBatch](#list_omics-action-GetBatch) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConfiguration  **
  - **IAM action:**  [omics:GetConfiguration](#list_omics-action-GetConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetReadSet  **
  - **IAM action:**  [omics:GetReadSet](#list_omics-action-GetReadSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetReadSetActivationJob  **
  - **IAM action:**  [omics:GetReadSetActivationJob](#list_omics-action-GetReadSetActivationJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetReadSetExportJob  **
  - **IAM action:**  [omics:GetReadSetExportJob](#list_omics-action-GetReadSetExportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetReadSetImportJob  **
  - **IAM action:**  [omics:GetReadSetImportJob](#list_omics-action-GetReadSetImportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetReadSetMetadata  **
  - **IAM action:**  [omics:GetReadSetMetadata](#list_omics-action-GetReadSetMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetReference  **
  - **IAM action:**  [omics:GetReference](#list_omics-action-GetReference) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetReferenceImportJob  **
  - **IAM action:**  [omics:GetReferenceImportJob](#list_omics-action-GetReferenceImportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetReferenceMetadata  **
  - **IAM action:**  [omics:GetReferenceMetadata](#list_omics-action-GetReferenceMetadata) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetReferenceStore  **
  - **IAM action:**  [omics:GetReferenceStore](#list_omics-action-GetReferenceStore) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRun  **
  - **IAM action:**  [omics:GetRun](#list_omics-action-GetRun) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRunCache  **
  - **IAM action:**  [omics:GetRunCache](#list_omics-action-GetRunCache) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRunGroup  **
  - **IAM action:**  [omics:GetRunGroup](#list_omics-action-GetRunGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRunTask  **
  - **IAM action:**  [omics:GetRunTask](#list_omics-action-GetRunTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetS3AccessPolicy  **
  - **IAM action:**  [omics:GetS3AccessPolicy](#list_omics-action-GetS3AccessPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSequenceStore  **
  - **IAM action:**  [omics:GetSequenceStore](#list_omics-action-GetSequenceStore) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetShare  **
  - **IAM action:**  [omics:GetShare](#list_omics-action-GetShare) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetVariantImportJob  **
  - **IAM action:**  [omics:GetVariantImportJob](#list_omics-action-GetVariantImportJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetVariantStore  **
  - **IAM action:**  [omics:GetVariantStore](#list_omics-action-GetVariantStore) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWorkflow  **
  - **IAM action:**  [omics:GetWorkflow](#list_omics-action-GetWorkflow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWorkflowVersion  **
  - **IAM action:**  [omics:GetWorkflowVersion](#list_omics-action-GetWorkflowVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAnnotationImportJobs  **
  - **IAM action:**  [omics:ListAnnotationImportJobs](#list_omics-action-ListAnnotationImportJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAnnotationStoreVersions  **
  - **IAM action:**  [omics:ListAnnotationStoreVersions](#list_omics-action-ListAnnotationStoreVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAnnotationStores  **
  - **IAM action:**  [omics:ListAnnotationStores](#list_omics-action-ListAnnotationStores) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListBatch  **
  - **IAM action:**  [omics:ListBatch](#list_omics-action-ListBatch) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListConfigurations  **
  - **IAM action:**  [omics:ListConfigurations](#list_omics-action-ListConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMultipartReadSetUploads  **
  - **IAM action:**  [omics:ListMultipartReadSetUploads](#list_omics-action-ListMultipartReadSetUploads) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListReadSetActivationJobs  **
  - **IAM action:**  [omics:ListReadSetActivationJobs](#list_omics-action-ListReadSetActivationJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListReadSetExportJobs  **
  - **IAM action:**  [omics:ListReadSetExportJobs](#list_omics-action-ListReadSetExportJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListReadSetImportJobs  **
  - **IAM action:**  [omics:ListReadSetImportJobs](#list_omics-action-ListReadSetImportJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListReadSetUploadParts  **
  - **IAM action:**  [omics:ListReadSetUploadParts](#list_omics-action-ListReadSetUploadParts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListReadSets  **
  - **IAM action:**  [omics:ListReadSets](#list_omics-action-ListReadSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListReferenceImportJobs  **
  - **IAM action:**  [omics:ListReferenceImportJobs](#list_omics-action-ListReferenceImportJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListReferenceStores  **
  - **IAM action:**  [omics:ListReferenceStores](#list_omics-action-ListReferenceStores) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListReferences  **
  - **IAM action:**  [omics:ListReferences](#list_omics-action-ListReferences) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRunCaches  **
  - **IAM action:**  [omics:ListRunCaches](#list_omics-action-ListRunCaches) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRunGroups  **
  - **IAM action:**  [omics:ListRunGroups](#list_omics-action-ListRunGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRunTasks  **
  - **IAM action:**  [omics:ListRunTasks](#list_omics-action-ListRunTasks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRuns  **
  - **IAM action:**  [omics:ListRuns](#list_omics-action-ListRuns) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRunsInBatch  **
  - **IAM action:**  [omics:ListRunsInBatch](#list_omics-action-ListRunsInBatch) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSequenceStores  **
  - **IAM action:**  [omics:ListSequenceStores](#list_omics-action-ListSequenceStores) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListShares  **
  - **IAM action:**  [omics:ListShares](#list_omics-action-ListShares) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [omics:ListTagsForResource](#list_omics-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListVariantImportJobs  **
  - **IAM action:**  [omics:ListVariantImportJobs](#list_omics-action-ListVariantImportJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListVariantStores  **
  - **IAM action:**  [omics:ListVariantStores](#list_omics-action-ListVariantStores) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListWorkflowVersions  **
  - **IAM action:**  [omics:ListWorkflowVersions](#list_omics-action-ListWorkflowVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListWorkflows  **
  - **IAM action:**  [omics:ListWorkflows](#list_omics-action-ListWorkflows) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutS3AccessPolicy  **
  - **IAM action:**  [omics:PutS3AccessPolicy](#list_omics-action-PutS3AccessPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartAnnotationImportJob  **
  - **IAM action:**  [omics:StartAnnotationImportJob](#list_omics-action-StartAnnotationImportJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** omics.amazonaws.com / **Access level:** Write

- **   StartReadSetActivationJob  **
  - **IAM action:**  [omics:StartReadSetActivationJob](#list_omics-action-StartReadSetActivationJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartReadSetExportJob  **
  - **IAM action:**  [omics:StartReadSetExportJob](#list_omics-action-StartReadSetExportJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** omics.amazonaws.com / **Access level:** Write

- **   StartReadSetImportJob  **
  - **IAM action:**  [omics:StartReadSetImportJob](#list_omics-action-StartReadSetImportJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [omics:TagResource](#list_omics-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** omics.amazonaws.com / **Access level:** Write

- **   StartReferenceImportJob  **
  - **IAM action:**  [omics:StartReferenceImportJob](#list_omics-action-StartReferenceImportJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [omics:TagResource](#list_omics-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** omics.amazonaws.com / **Access level:** Write

- **   StartRun  **
  - **IAM action:**  [omics:StartRun](#list_omics-action-StartRun)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [omics:TagResource](#list_omics-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** omics.amazonaws.com / **Access level:** Write

- **   StartRunBatch  **
  - **IAM action:**  [omics:StartRun](#list_omics-action-StartRun)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [omics:StartRunBatch](#list_omics-action-StartRunBatch)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [omics:TagResource](#list_omics-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** omics.amazonaws.com / **Access level:** Write

- **   StartVariantImportJob  **
  - **IAM action:**  [omics:StartVariantImportJob](#list_omics-action-StartVariantImportJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** omics.amazonaws.com / **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [omics:TagResource](#list_omics-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [omics:UntagResource](#list_omics-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAnnotationStore  **
  - **IAM action:**  [omics:UpdateAnnotationStore](#list_omics-action-UpdateAnnotationStore) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAnnotationStoreVersion  **
  - **IAM action:**  [omics:UpdateAnnotationStoreVersion](#list_omics-action-UpdateAnnotationStoreVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRunCache  **
  - **IAM action:**  [omics:UpdateRunCache](#list_omics-action-UpdateRunCache) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRunGroup  **
  - **IAM action:**  [omics:UpdateRunGroup](#list_omics-action-UpdateRunGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSequenceStore  **
  - **IAM action:**  [omics:UpdateSequenceStore](#list_omics-action-UpdateSequenceStore) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateVariantStore  **
  - **IAM action:**  [omics:UpdateVariantStore](#list_omics-action-UpdateVariantStore) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateWorkflow  **
  - **IAM action:**  [omics:UpdateWorkflow](#list_omics-action-UpdateWorkflow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateWorkflowVersion  **
  - **IAM action:**  [omics:UpdateWorkflowVersion](#list_omics-action-UpdateWorkflowVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UploadReadSetPart  **
  - **IAM action:**  [omics:UploadReadSetPart](#list_omics-action-UploadReadSetPart) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS HealthOmics
<a name="list_omics-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AbortMultipartReadSetUpload](https://docs.aws.amazon.com/omics/latest/api/API_AbortMultipartReadSetUpload.html)  **
  - **Description:** Grants permission to abort multipart read set uploads
  - **Resource types (\*required):** [sequenceStore\*](#list_omics-resource-sequenceStore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AcceptShare](https://docs.aws.amazon.com/omics/latest/api/API_AcceptShare.html)  **
  - **Description:** Grants permission to accept a share
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [BatchDeleteReadSet](https://docs.aws.amazon.com/omics/latest/api/API_BatchDeleteReadSet.html)  **
  - **Description:** Grants permission to batch delete Read Sets in the given Sequence Store
  - **Resource types (\*required):** [sequenceStore\*](#list_omics-resource-sequenceStore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CancelAnnotationImportJob](https://docs.aws.amazon.com/omics/latest/api/API_CancelAnnotationImportJob.html)  **
  - **Description:** Grants permission to cancel an Annotation Import Job 
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CancelRun](https://docs.aws.amazon.com/omics/latest/api/API_CancelRun.html)  **
  - **Description:** Grants permission to cancel a workflow run and stop all workflow tasks
  - **Resource types (\*required):** [run\*](#list_omics-resource-run)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CancelRunBatch](https://docs.aws.amazon.com/omics/latest/api/API_CancelRunBatch.html)  **
  - **Description:** Grants permission to cancel a batch of workflow runs
  - **Resource types (\*required):** [runBatch\*](#list_omics-resource-runBatch)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CancelVariantImportJob](https://docs.aws.amazon.com/omics/latest/api/API_CancelVariantImportJob.html)  **
  - **Description:** Grants permission to cancel a Variant Import Job 
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CompleteMultipartReadSetUpload](https://docs.aws.amazon.com/omics/latest/api/API_CompleteMultipartReadSetUpload.html)  **
  - **Description:** Grants permission to complete a multipart read set upload
  - **Resource types (\*required):** [sequenceStore\*](#list_omics-resource-sequenceStore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateAnnotationStore](https://docs.aws.amazon.com/omics/latest/api/API_CreateAnnotationStore.html)  **
  - **Description:** Grants permission to create an Annotation Store
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_omics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Access level:** Write

- **   [CreateAnnotationStoreVersion](https://docs.aws.amazon.com/omics/latest/api/API_CreateAnnotationStoreVersion.html)  **
  - **Description:** Grants permission to create a Version in an Annotation Store
  - **Resource types (\*required):** [AnnotationStore\*](#list_omics-resource-AnnotationStore)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_omics-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Access level:** Write

- **   [CreateConfiguration](https://docs.aws.amazon.com/omics/latest/api/API_CreateConfiguration.html)  **
  - **Description:** Grants permission to create a new configuration
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_omics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Access level:** Write

- **   [CreateMultipartReadSetUpload](https://docs.aws.amazon.com/omics/latest/api/API_CreateMultipartReadSetUpload.html)  **
  - **Description:** Grants permission to create a multipart read set upload
  - **Resource types (\*required):** [sequenceStore\*](#list_omics-resource-sequenceStore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateReferenceStore](https://docs.aws.amazon.com/omics/latest/api/API_CreateReferenceStore.html)  **
  - **Description:** Grants permission to create a Reference Store
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_omics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRunCache](https://docs.aws.amazon.com/omics/latest/api/API_CreateRunCache.html)  **
  - **Description:** Grants permission to create a new workflow run cache
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_omics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRunGroup](https://docs.aws.amazon.com/omics/latest/api/API_CreateRunGroup.html)  **
  - **Description:** Grants permission to create a new workflow run group
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_omics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSequenceStore](https://docs.aws.amazon.com/omics/latest/api/API_CreateSequenceStore.html)  **
  - **Description:** Grants permission to create a Sequence Store
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_omics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Access level:** Write

- **   [CreateShare](https://docs.aws.amazon.com/omics/latest/api/API_CreateShare.html)  **
  - **Description:** Grants permission to create a share
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateVariantStore](https://docs.aws.amazon.com/omics/latest/api/API_CreateVariantStore.html)  **
  - **Description:** Grants permission to create a Variant Store
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_omics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Access level:** Write

- **   [CreateWorkflow](https://docs.aws.amazon.com/omics/latest/api/API_CreateWorkflow.html)  **
  - **Description:** Grants permission to create a new workflow with a workflow definition and template of workflow parameters
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_omics-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Access level:** Write

- **   [CreateWorkflowVersion](https://docs.aws.amazon.com/omics/latest/api/API_CreateWorkflowVersion.html)  **
  - **Description:** Grants permission to create a new workflow version with a workflow definition and template of workflow parameters
  - **Resource types (\*required):** [workflow\*](#list_omics-resource-workflow)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_omics-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteAnnotationStore](https://docs.aws.amazon.com/omics/latest/api/API_DeleteAnnotationStore.html)  **
  - **Description:** Grants permission to delete an Annotation Store
  - **Resource types (\*required):** [AnnotationStore\*](#list_omics-resource-AnnotationStore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAnnotationStoreVersions](https://docs.aws.amazon.com/omics/latest/api/API_DeleteAnnotationStoreVersions.html)  **
  - **Description:** Grants permission to delete Versions in an Annotation Store
  - **Resource types (\*required):** [AnnotationStore\*](#list_omics-resource-AnnotationStore) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [AnnotationStoreVersion\*](#list_omics-resource-AnnotationStoreVersion) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteBatch](https://docs.aws.amazon.com/omics/latest/api/API_DeleteBatch.html)  **
  - **Description:** Grants permission to delete a batch
  - **Resource types (\*required):** [runBatch\*](#list_omics-resource-runBatch)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteConfiguration](https://docs.aws.amazon.com/omics/latest/api/API_DeleteConfiguration.html)  **
  - **Description:** Grants permission to delete a configuration
  - **Resource types (\*required):** [configuration\*](#list_omics-resource-configuration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteReference](https://docs.aws.amazon.com/omics/latest/api/API_DeleteReference.html)  **
  - **Description:** Grants permission to delete a Reference in the given Reference Store
  - **Resource types (\*required):** [reference\*](#list_omics-resource-reference) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [referenceStore\*](#list_omics-resource-referenceStore) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteReferenceStore](https://docs.aws.amazon.com/omics/latest/api/API_DeleteReferenceStore.html)  **
  - **Description:** Grants permission to delete a Reference Store
  - **Resource types (\*required):** [referenceStore\*](#list_omics-resource-referenceStore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRun](https://docs.aws.amazon.com/omics/latest/api/API_DeleteRun.html)  **
  - **Description:** Grants permission to delete a workflow run
  - **Resource types (\*required):** [run\*](#list_omics-resource-run)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRunBatch](https://docs.aws.amazon.com/omics/latest/api/API_DeleteRunBatch.html)  **
  - **Description:** Grants permission to delete a batch of workflow runs
  - **Resource types (\*required):** [run\*](#list_omics-resource-run) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [runBatch\*](#list_omics-resource-runBatch) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRunCache](https://docs.aws.amazon.com/omics/latest/api/API_DeleteRunCache.html)  **
  - **Description:** Grants permission to delete a workflow run cache
  - **Resource types (\*required):** [runCache\*](#list_omics-resource-runCache)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRunGroup](https://docs.aws.amazon.com/omics/latest/api/API_DeleteRunGroup.html)  **
  - **Description:** Grants permission to delete a workflow run group
  - **Resource types (\*required):** [runGroup\*](#list_omics-resource-runGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteS3AccessPolicy](https://docs.aws.amazon.com/omics/latest/api/API_DeleteS3AccessPolicy.html)  **
  - **Description:** Grants permission to delete an access policy on a given store
  - **Resource types (\*required):** [sequenceStore\*](#list_omics-resource-sequenceStore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSequenceStore](https://docs.aws.amazon.com/omics/latest/api/API_DeleteSequenceStore.html)  **
  - **Description:** Grants permission to delete a Sequence Store
  - **Resource types (\*required):** [sequenceStore\*](#list_omics-resource-sequenceStore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteShare](https://docs.aws.amazon.com/omics/latest/api/API_DeleteShare.html)  **
  - **Description:** Grants permission to delete a share
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteVariantStore](https://docs.aws.amazon.com/omics/latest/api/API_DeleteVariantStore.html)  **
  - **Description:** Grants permission to delete a Variant Store
  - **Resource types (\*required):** [VariantStore\*](#list_omics-resource-VariantStore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteWorkflow](https://docs.aws.amazon.com/omics/latest/api/API_DeleteWorkflow.html)  **
  - **Description:** Grants permission to delete a workflow
  - **Resource types (\*required):** [workflow\*](#list_omics-resource-workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteWorkflowVersion](https://docs.aws.amazon.com/omics/latest/api/API_DeleteWorkflowVersion.html)  **
  - **Description:** Grants permission to delete a workflow version
  - **Resource types (\*required):** [WorkflowVersion\*](#list_omics-resource-WorkflowVersion) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workflow\*](#list_omics-resource-workflow) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetAnnotationImportJob](https://docs.aws.amazon.com/omics/latest/api/API_GetAnnotationImportJob.html)  **
  - **Description:** Grants permission to get the status of an Annotation Import Job
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetAnnotationStore](https://docs.aws.amazon.com/omics/latest/api/API_GetAnnotationStore.html)  **
  - **Description:** Grants permission to get detailed information about an Annotation Store
  - **Resource types (\*required):** [AnnotationStore\*](#list_omics-resource-AnnotationStore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAnnotationStoreVersion](https://docs.aws.amazon.com/omics/latest/api/API_GetAnnotationStoreVersion.html)  **
  - **Description:** Grants permission to get detailed information about a version in an Annotation Store
  - **Resource types (\*required):** [AnnotationStoreVersion\*](#list_omics-resource-AnnotationStoreVersion)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetBatch](https://docs.aws.amazon.com/omics/latest/api/API_GetBatch.html)  **
  - **Description:** Grants permission to retrieve batch details and status
  - **Resource types (\*required):** [runBatch\*](#list_omics-resource-runBatch)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetConfiguration](https://docs.aws.amazon.com/omics/latest/api/API_GetConfiguration.html)  **
  - **Description:** Grants permission to retrieve configuration details
  - **Resource types (\*required):** [configuration\*](#list_omics-resource-configuration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetReadSet](https://docs.aws.amazon.com/omics/latest/api/API_GetReadSet.html)  **
  - **Description:** Grants permission to get a Read Set in the given Sequence Store
  - **Resource types (\*required):** [readSet\*](#list_omics-resource-readSet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [sequenceStore\*](#list_omics-resource-sequenceStore) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetReadSetActivationJob](https://docs.aws.amazon.com/omics/latest/api/API_GetReadSetActivationJob.html)  **
  - **Description:** Grants permission to get details about a Read Set activation job for the given Sequence Store
  - **Resource types (\*required):** [sequenceStore\*](#list_omics-resource-sequenceStore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetReadSetExportJob](https://docs.aws.amazon.com/omics/latest/api/API_GetReadSetExportJob.html)  **
  - **Description:** Grants permission to get details about a Read Set export job for the given Sequence Store
  - **Resource types (\*required):** [sequenceStore\*](#list_omics-resource-sequenceStore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetReadSetImportJob](https://docs.aws.amazon.com/omics/latest/api/API_GetReadSetImportJob.html)  **
  - **Description:** Grants permission to get details about a Read Set import job for the given Sequence Store
  - **Resource types (\*required):** [sequenceStore\*](#list_omics-resource-sequenceStore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetReadSetMetadata](https://docs.aws.amazon.com/omics/latest/api/API_GetReadSetMetadata.html)  **
  - **Description:** Grants permission to get details about a Read Set in the given Sequence Store
  - **Resource types (\*required):** [readSet\*](#list_omics-resource-readSet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [sequenceStore\*](#list_omics-resource-sequenceStore) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetReference](https://docs.aws.amazon.com/omics/latest/api/API_GetReference.html)  **
  - **Description:** Grants permission to get a Reference in the given Reference Store
  - **Resource types (\*required):** [reference\*](#list_omics-resource-reference) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [referenceStore\*](#list_omics-resource-referenceStore) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetReferenceImportJob](https://docs.aws.amazon.com/omics/latest/api/API_GetReferenceImportJob.html)  **
  - **Description:** Grants permission to get details about a Reference import job for the given Reference Store
  - **Resource types (\*required):** [referenceStore\*](#list_omics-resource-referenceStore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetReferenceMetadata](https://docs.aws.amazon.com/omics/latest/api/API_GetReferenceMetadata.html)  **
  - **Description:** Grants permission to get details about a Reference in the given Reference Store
  - **Resource types (\*required):** [reference\*](#list_omics-resource-reference) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [referenceStore\*](#list_omics-resource-referenceStore) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetReferenceStore](https://docs.aws.amazon.com/omics/latest/api/API_GetReferenceStore.html)  **
  - **Description:** Grants permission to get details about a Reference Store
  - **Resource types (\*required):** [referenceStore\*](#list_omics-resource-referenceStore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRun](https://docs.aws.amazon.com/omics/latest/api/API_GetRun.html)  **
  - **Description:** Grants permission to retrieve workflow run details
  - **Resource types (\*required):** [run\*](#list_omics-resource-run)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRunCache](https://docs.aws.amazon.com/omics/latest/api/API_GetRunCache.html)  **
  - **Description:** Grants permission to retrieve workflow run cache details
  - **Resource types (\*required):** [runCache\*](#list_omics-resource-runCache)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRunGroup](https://docs.aws.amazon.com/omics/latest/api/API_GetRunGroup.html)  **
  - **Description:** Grants permission to retrieve workflow run group details
  - **Resource types (\*required):** [runGroup\*](#list_omics-resource-runGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRunTask](https://docs.aws.amazon.com/omics/latest/api/API_GetRunTask.html)  **
  - **Description:** Grants permission to retrieve workflow task details
  - **Resource types (\*required):** [TaskResource\*](#list_omics-resource-TaskResource) / **Condition keys:**  
  - **Resource types (\*required):** [run\*](#list_omics-resource-run) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetS3AccessPolicy](https://docs.aws.amazon.com/omics/latest/api/API_GetS3AccessPolicy.html)  **
  - **Description:** Grants permission to get details about an access policy on a given store
  - **Resource types (\*required):** [sequenceStore\*](#list_omics-resource-sequenceStore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSequenceStore](https://docs.aws.amazon.com/omics/latest/api/API_GetSequenceStore.html)  **
  - **Description:** Grants permission to get details about a Sequence Store
  - **Resource types (\*required):** [sequenceStore\*](#list_omics-resource-sequenceStore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetShare](https://docs.aws.amazon.com/omics/latest/api/API_GetShare.html)  **
  - **Description:** Grants permission to get detailed information about a Share
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetVariantImportJob](https://docs.aws.amazon.com/omics/latest/api/API_GetVariantImportJob.html)  **
  - **Description:** Grants permission to get the status of a Variant Import Job
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetVariantStore](https://docs.aws.amazon.com/omics/latest/api/API_GetVariantStore.html)  **
  - **Description:** Grants permission to get detailed information about a Variant Store
  - **Resource types (\*required):** [VariantStore\*](#list_omics-resource-VariantStore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetWorkflow](https://docs.aws.amazon.com/omics/latest/api/API_GetWorkflow.html)  **
  - **Description:** Grants permission to retrieve workflow details
  - **Resource types (\*required):** [workflow\*](#list_omics-resource-workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetWorkflowVersion](https://docs.aws.amazon.com/omics/latest/api/API_GetWorkflowVersion.html)  **
  - **Description:** Grants permission to retrieve workflow version details
  - **Resource types (\*required):** [WorkflowVersion\*](#list_omics-resource-WorkflowVersion) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workflow\*](#list_omics-resource-workflow) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAnnotationImportJobs](https://docs.aws.amazon.com/omics/latest/api/API_ListAnnotationImportJobs.html)  **
  - **Description:** Grants permission to get a list of Annotation Import Jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAnnotationStoreVersions](https://docs.aws.amazon.com/omics/latest/api/API_ListAnnotationStoreVersions.html)  **
  - **Description:** Grants permission to retrieve a list of information about Versions in an Annotation Store
  - **Resource types (\*required):** [AnnotationStore\*](#list_omics-resource-AnnotationStore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAnnotationStores](https://docs.aws.amazon.com/omics/latest/api/API_ListAnnotationStores.html)  **
  - **Description:** Grants permission to retrieve a list of information about Annotation Stores
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListBatch](https://docs.aws.amazon.com/omics/latest/api/API_ListBatch.html)  **
  - **Description:** Grants permission to retrieve list of batches
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListConfigurations](https://docs.aws.amazon.com/omics/latest/api/API_ListConfigurations.html)  **
  - **Description:** Grants permission to retrieve a list of configurations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMultipartReadSetUploads](https://docs.aws.amazon.com/omics/latest/api/API_ListMultipartReadSetUploads.html)  **
  - **Description:** Grants permission to list multipart read set uploads
  - **Resource types (\*required):** [sequenceStore\*](#list_omics-resource-sequenceStore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListReadSetActivationJobs](https://docs.aws.amazon.com/omics/latest/api/API_ListReadSetActivationJobs.html)  **
  - **Description:** Grants permission to list Read Set activation jobs for the given Sequence Store
  - **Resource types (\*required):** [sequenceStore\*](#list_omics-resource-sequenceStore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListReadSetExportJobs](https://docs.aws.amazon.com/omics/latest/api/API_ListReadSetExportJobs.html)  **
  - **Description:** Grants permission to list Read Set export jobs for the given Sequence Store
  - **Resource types (\*required):** [sequenceStore\*](#list_omics-resource-sequenceStore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListReadSetImportJobs](https://docs.aws.amazon.com/omics/latest/api/API_ListReadSetImportJobs.html)  **
  - **Description:** Grants permission to list Read Set import jobs for the given Sequence Store
  - **Resource types (\*required):** [sequenceStore\*](#list_omics-resource-sequenceStore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListReadSetUploadParts](https://docs.aws.amazon.com/omics/latest/api/API_ListReadSetUploadParts.html)  **
  - **Description:** Grants permission to list read set upload parts
  - **Resource types (\*required):** [sequenceStore\*](#list_omics-resource-sequenceStore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListReadSets](https://docs.aws.amazon.com/omics/latest/api/API_ListReadSets.html)  **
  - **Description:** Grants permission to list Read Sets in the given Sequence Store
  - **Resource types (\*required):** [sequenceStore\*](#list_omics-resource-sequenceStore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListReferenceImportJobs](https://docs.aws.amazon.com/omics/latest/api/API_ListReferenceImportJobs.html)  **
  - **Description:** Grants permission to list Reference import jobs for the given Reference Store
  - **Resource types (\*required):** [referenceStore\*](#list_omics-resource-referenceStore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListReferenceStores](https://docs.aws.amazon.com/omics/latest/api/API_ListReferenceStores.html)  **
  - **Description:** Grants permission to list Reference Stores
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListReferences](https://docs.aws.amazon.com/omics/latest/api/API_ListReferences.html)  **
  - **Description:** Grants permission to list References in the given Reference Store
  - **Resource types (\*required):** [referenceStore\*](#list_omics-resource-referenceStore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListRunCaches](https://docs.aws.amazon.com/omics/latest/api/API_ListRunCaches.html)  **
  - **Description:** Grants permission to retrieve a list of workflow run caches
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRunGroups](https://docs.aws.amazon.com/omics/latest/api/API_ListRunGroups.html)  **
  - **Description:** Grants permission to retrieve a list of workflow run groups
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRunTasks](https://docs.aws.amazon.com/omics/latest/api/API_ListRunTasks.html)  **
  - **Description:** Grants permission to retrieve a list of tasks for a workflow run
  - **Resource types (\*required):** [run\*](#list_omics-resource-run)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListRuns](https://docs.aws.amazon.com/omics/latest/api/API_ListRuns.html)  **
  - **Description:** Grants permission to retrieve a list of workflow runs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRunsInBatch](https://docs.aws.amazon.com/omics/latest/api/API_ListRunsInBatch.html)  **
  - **Description:** Grants permission to retrieve list of workflow runs in batch
  - **Resource types (\*required):** [runBatch\*](#list_omics-resource-runBatch)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListSequenceStores](https://docs.aws.amazon.com/omics/latest/api/API_ListSequenceStores.html)  **
  - **Description:** Grants permission to list Sequence Stores
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListShares](https://docs.aws.amazon.com/omics/latest/api/API_ListShares.html)  **
  - **Description:** Grants permission to retrieve a list of information about shares
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/omics/latest/api/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to retrieve a list of resource AWS tags
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListVariantImportJobs](https://docs.aws.amazon.com/omics/latest/api/API_ListVariantImportJobs.html)  **
  - **Description:** Grants permission to get a list of Variant Import Jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListVariantStores](https://docs.aws.amazon.com/omics/latest/api/API_ListVariantStores.html)  **
  - **Description:** Grants permission to retrieve a list of metadata for Variant Stores
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListWorkflowVersions](https://docs.aws.amazon.com/omics/latest/api/API_ListWorkflowVersions.html)  **
  - **Description:** Grants permission to retrieve a list of available versions for a workflow
  - **Resource types (\*required):** [workflow\*](#list_omics-resource-workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListWorkflows](https://docs.aws.amazon.com/omics/latest/api/API_ListWorkflows.html)  **
  - **Description:** Grants permission to retrieve a list of available workflows
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [PutS3AccessPolicy](https://docs.aws.amazon.com/omics/latest/api/API_PutS3AccessPolicy.html)  **
  - **Description:** Grants permission to put an access policy on a given store
  - **Resource types (\*required):** [sequenceStore\*](#list_omics-resource-sequenceStore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartAnnotationImportJob](https://docs.aws.amazon.com/omics/latest/api/API_StartAnnotationImportJob.html)  **
  - **Description:** Grants permission to import a list of Annotation files to an Annotation Store
  - **Resource types (\*required):** [AnnotationStore\*](#list_omics-resource-AnnotationStore) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [AnnotationStoreVersion\*](#list_omics-resource-AnnotationStoreVersion) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartReadSetActivationJob](https://docs.aws.amazon.com/omics/latest/api/API_StartReadSetActivationJob.html)  **
  - **Description:** Grants permission to start a Read Set activation job from the given Sequence Store
  - **Resource types (\*required):** [sequenceStore\*](#list_omics-resource-sequenceStore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartReadSetExportJob](https://docs.aws.amazon.com/omics/latest/api/API_StartReadSetExportJob.html)  **
  - **Description:** Grants permission to start a Read Set export job from the given Sequence Store
  - **Resource types (\*required):** [sequenceStore\*](#list_omics-resource-sequenceStore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartReadSetImportJob](https://docs.aws.amazon.com/omics/latest/api/API_StartReadSetImportJob.html)  **
  - **Description:** Grants permission to start a Read Set import job into the given Sequence Store
  - **Resource types (\*required):** [sequenceStore\*](#list_omics-resource-sequenceStore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartReferenceImportJob](https://docs.aws.amazon.com/omics/latest/api/API_StartReferenceImportJob.html)  **
  - **Description:** Grants permission to start a Reference import job into the given Reference Store
  - **Resource types (\*required):** [referenceStore\*](#list_omics-resource-referenceStore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartRun](https://docs.aws.amazon.com/omics/latest/api/API_StartRun.html)  **
  - **Description:** Grants permission to start a workflow run
  - **Resource types (\*required):** [configuration](#list_omics-resource-configuration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_omics-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Resource types (\*required):** [run\*](#list_omics-resource-run) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_omics-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Resource types (\*required):** [runBatch](#list_omics-resource-runBatch) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_omics-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Resource types (\*required):** [runCache](#list_omics-resource-runCache) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_omics-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Resource types (\*required):** [runGroup](#list_omics-resource-runGroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_omics-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Resource types (\*required):** [workflow](#list_omics-resource-workflow) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_omics-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Access level:** Write

- **   [StartRunBatch](https://docs.aws.amazon.com/omics/latest/api/API_StartRunBatch.html)  **
  - **Description:** Grants permission to start batch of workflow runs
  - **Resource types (\*required):** [run\*](#list_omics-resource-run) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_omics-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Resource types (\*required):** [runBatch\*](#list_omics-resource-runBatch) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_omics-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Resource types (\*required):** [runCache](#list_omics-resource-runCache) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_omics-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Resource types (\*required):** [runGroup](#list_omics-resource-runGroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_omics-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Resource types (\*required):** [workflow](#list_omics-resource-workflow) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_omics-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Access level:** Write

- **   [StartVariantImportJob](https://docs.aws.amazon.com/omics/latest/api/API_StartVariantImportJob.html)  **
  - **Description:** Grants permission to import a list of variant files to an Variant Store
  - **Resource types (\*required):** [VariantStore\*](#list_omics-resource-VariantStore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/omics/latest/api/API_TagResource.html)  **
  - **Description:** Grants permission to add AWS tags to a resource
  - **Resource types (\*required):** [AnnotationStore](#list_omics-resource-AnnotationStore) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_omics-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Resource types (\*required):** [AnnotationStoreVersion](#list_omics-resource-AnnotationStoreVersion) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_omics-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Resource types (\*required):** [VariantStore](#list_omics-resource-VariantStore) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_omics-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Resource types (\*required):** [WorkflowVersion](#list_omics-resource-WorkflowVersion) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_omics-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Resource types (\*required):** [configuration](#list_omics-resource-configuration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_omics-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Resource types (\*required):** [readSet](#list_omics-resource-readSet) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_omics-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Resource types (\*required):** [reference](#list_omics-resource-reference) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_omics-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Resource types (\*required):** [referenceStore](#list_omics-resource-referenceStore) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_omics-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Resource types (\*required):** [run](#list_omics-resource-run) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_omics-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Resource types (\*required):** [runBatch](#list_omics-resource-runBatch) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_omics-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Resource types (\*required):** [runCache](#list_omics-resource-runCache) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_omics-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Resource types (\*required):** [runGroup](#list_omics-resource-runGroup) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_omics-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Resource types (\*required):** [sequenceStore](#list_omics-resource-sequenceStore) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_omics-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Resource types (\*required):** [workflow](#list_omics-resource-workflow) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_omics-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/omics/latest/api/API_UntagResource.html)  **
  - **Description:** Grants permission to remove resource AWS tags
  - **Resource types (\*required):** [AnnotationStore](#list_omics-resource-AnnotationStore) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Resource types (\*required):** [AnnotationStoreVersion](#list_omics-resource-AnnotationStoreVersion) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Resource types (\*required):** [VariantStore](#list_omics-resource-VariantStore) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Resource types (\*required):** [WorkflowVersion](#list_omics-resource-WorkflowVersion) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Resource types (\*required):** [configuration](#list_omics-resource-configuration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Resource types (\*required):** [readSet](#list_omics-resource-readSet) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Resource types (\*required):** [reference](#list_omics-resource-reference) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Resource types (\*required):** [referenceStore](#list_omics-resource-referenceStore) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Resource types (\*required):** [run](#list_omics-resource-run) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Resource types (\*required):** [runBatch](#list_omics-resource-runBatch) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Resource types (\*required):** [runCache](#list_omics-resource-runCache) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Resource types (\*required):** [runGroup](#list_omics-resource-runGroup) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Resource types (\*required):** [sequenceStore](#list_omics-resource-sequenceStore) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Resource types (\*required):** [workflow](#list_omics-resource-workflow) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_omics-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAnnotationStore](https://docs.aws.amazon.com/omics/latest/api/API_UpdateAnnotationStore.html)  **
  - **Description:** Grants permission to update information about the Annotation Store
  - **Resource types (\*required):** [AnnotationStore\*](#list_omics-resource-AnnotationStore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAnnotationStoreVersion](https://docs.aws.amazon.com/omics/latest/api/API_UpdateAnnotationStoreVersion.html)  **
  - **Description:** Grants permission to update information about the Version in an Annotation Store
  - **Resource types (\*required):** [AnnotationStoreVersion\*](#list_omics-resource-AnnotationStoreVersion)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRunCache](https://docs.aws.amazon.com/omics/latest/api/API_UpdateRunCache.html)  **
  - **Description:** Grants permission to update a workflow run cache
  - **Resource types (\*required):** [runCache\*](#list_omics-resource-runCache)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRunGroup](https://docs.aws.amazon.com/omics/latest/api/API_UpdateRunGroup.html)  **
  - **Description:** Grants permission to update a workflow run group
  - **Resource types (\*required):** [runGroup\*](#list_omics-resource-runGroup)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSequenceStore](https://docs.aws.amazon.com/omics/latest/api/API_UpdateSequenceStore.html)  **
  - **Description:** Grants permission to update details about a Sequence Store
  - **Resource types (\*required):** [sequenceStore\*](#list_omics-resource-sequenceStore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateVariantStore](https://docs.aws.amazon.com/omics/latest/api/API_UpdateVariantStore.html)  **
  - **Description:** Grants permission to update metadata about the Variant Store
  - **Resource types (\*required):** [VariantStore\*](#list_omics-resource-VariantStore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateWorkflow](https://docs.aws.amazon.com/omics/latest/api/API_UpdateWorkflow.html)  **
  - **Description:** Grants permission to update workflow details
  - **Resource types (\*required):** [workflow\*](#list_omics-resource-workflow)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateWorkflowVersion](https://docs.aws.amazon.com/omics/latest/api/API_UpdateWorkflowVersion.html)  **
  - **Description:** Grants permission to update workflow version details
  - **Resource types (\*required):** [WorkflowVersion\*](#list_omics-resource-WorkflowVersion) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [workflow\*](#list_omics-resource-workflow) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UploadReadSetPart](https://docs.aws.amazon.com/omics/latest/api/API_UploadReadSetPart.html)  **
  - **Description:** Grants permission to upload read set parts
  - **Resource types (\*required):** [sequenceStore\*](#list_omics-resource-sequenceStore)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS HealthOmics
<a name="list_omics-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [AnnotationStore](https://docs.aws.amazon.com/omics/latest/api/API_AnnotationStoreItem.html)  | arn:${Partition}:omics:${Region}:${Account}:annotationStore/${AnnotationStoreName} | [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_) | 
|  [AnnotationStoreVersion](https://docs.aws.amazon.com/omics/latest/api/API_AnnotationStoreVersionItem.html)  | arn:${Partition}:omics:${Region}:${Account}:annotationStore/${AnnotationStoreName}/version/${AnnotationStoreVersionName} | [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_) | 
|  [TaskResource](https://docs.aws.amazon.com/omics/latest/api/API_TaskListItem.html)  | arn:${Partition}:omics:${Region}:${Account}:task/${Id} |   | 
|  [VariantStore](https://docs.aws.amazon.com/omics/latest/api/API_VariantStoreItem.html)  | arn:${Partition}:omics:${Region}:${Account}:variantStore/${VariantStoreName} | [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_) | 
|  [WorkflowVersion](https://docs.aws.amazon.com/omics/latest/api/API_WorkflowVersionListItem.html)  | arn:${Partition}:omics:${Region}:${Account}:workflow/${Id}/version/${VersionName} | [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_) | 
|  [configuration](https://docs.aws.amazon.com/omics/latest/api/API_ConfigurationListItem.html)  | arn:${Partition}:omics:${Region}:${Account}:configuration/${Name} | [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_) | 
|  [readSet](https://docs.aws.amazon.com/omics/latest/api/API_ReadSetFiles.html)  | arn:${Partition}:omics:${Region}:${Account}:sequenceStore/${SequenceStoreId}/readSet/${ReadSetId} | [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_) | 
|  [reference](https://docs.aws.amazon.com/omics/latest/api/API_ReferenceFiles.html)  | arn:${Partition}:omics:${Region}:${Account}:referenceStore/${ReferenceStoreId}/reference/${ReferenceId} | [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_) | 
|  [referenceStore](https://docs.aws.amazon.com/omics/latest/api/API_ReferenceStoreDetail.html)  | arn:${Partition}:omics:${Region}:${Account}:referenceStore/${ReferenceStoreId} | [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_) | 
|  [run](https://docs.aws.amazon.com/omics/latest/api/API_RunListItem.html)  | arn:${Partition}:omics:${Region}:${Account}:run/${Id} | [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_) | 
|  [runBatch](https://docs.aws.amazon.com/omics/latest/api/API_BatchListItem.html)  | arn:${Partition}:omics:${Region}:${Account}:runBatch/${BatchId} | [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_) | 
|  [runCache](https://docs.aws.amazon.com/omics/latest/api/API_RunCacheListItem.html)  | arn:${Partition}:omics:${Region}:${Account}:runCache/${Id} | [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_) | 
|  [runGroup](https://docs.aws.amazon.com/omics/latest/api/API_RunGroupListItem.html)  | arn:${Partition}:omics:${Region}:${Account}:runGroup/${Id} | [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_) | 
|  [sequenceStore](https://docs.aws.amazon.com/omics/latest/api/API_SequenceStoreDetail.html)  | arn:${Partition}:omics:${Region}:${Account}:sequenceStore/${SequenceStoreId} | [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_) | 
|  [workflow](https://docs.aws.amazon.com/omics/latest/api/API_WorkflowListItem.html)  | arn:${Partition}:omics:${Region}:${Account}:workflow/${Id} | [aws:ResourceTag/${TagKey}](#list_omics-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS HealthOmics
<a name="list_omics-policy-keys"></a>

AWS HealthOmics defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the presence of tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the presence of tag keys in the request | ArrayOfString | 