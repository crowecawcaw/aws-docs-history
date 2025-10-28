AWS HealthOmics variant stores and annotation stores will no longer be open to new customers starting
November 7th, 2025. If you would like to use variant stores or annotation stores,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[AWS HealthOmics variant store and annotation store availability change](variant-store-availability-change.md "variant-store-availability-change.md").

# HealthOmics API quotas

HealthOmics has the following quotas related to API operations.
Where indicated, the quota is adjustable. To request an increase,
use the [quota increase form](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase "https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase").

For each API operation listed, the quota is the maximum
transactions per second (TPS) for that API operation
in each Region.

###### Topics

- [General API quotas](#api-quotas-general "#api-quotas-general")
- [Storage API quotas](#api-quotas-storage "#api-quotas-storage")
- [Workflow API quotas](#api-quotas-workflows "#api-quotas-workflows")
- [Analytics API quotas](#api-quotas-analytics "#api-quotas-analytics")

## General API quotas

The following table lists general API operations that apply to more than one
category (storage, workflows, and analytics).

| API operation                                                                                                 | Default maximum TPS | Adjustable (Yes/No) |
| ------------------------------------------------------------------------------------------------------------- | ------------------- | ------------------- | ------------------------------------------------------------------------------- |
| AcceptShare, CreateShare, DeleteShare, GetShare, ListShares                                                   | 1 TPS               | Yes                 | ## Storage API quotas The following table lists the storage API operations.     |
| Storage API operation                                                                                         | Default maximum TPS | Adjustable (Yes/No) |
| ---                                                                                                           | ---                 | ---                 |
| CreateSequenceStore, UpdateSequenceStore, DeleteSequenceStore, CreateReferenceStore, DeleteReferenceStore     | 1 TPS               | Yes                 |
| BatchDeleteReadSet, DeleteReference                                                                           | 1 TPS               | Yes                 |
| CreateMultipartReadSetUpload, CompleteMultipartReadSetUpload, AbortMultipartReadSetUpload                     | 1 TPS               | No                  |
| GetS3AccessPolicy, PutS3AccessPolicy, DeleteS3AccessPolicy                                                    | 1 TPS               | Yes                 |
| GetReference                                                                                                  | 10 TPS              | Yes                 |
| UploadReadSetPart                                                                                             | 10 TPS              | Yes                 |
| GetReadSet                                                                                                    | 30 TPS              | Yes                 |
| GetSequenceStore, ListSequenceStores                                                                          | 5 TPS               | Yes                 |
| GetReadSetMetadata, ListReadSets                                                                              | 5 TPS               | Yes                 |
| StartReadSetImportJob, GetReadSetImportJob, ListReadSetImportJobs                                             | 5 TPS               | Yes                 |
| StartReadSetExportJob, GetReadSetExportJob, ListReadSetExportJobs                                             | 5 TPS               | Yes                 |
| ListReferenceStores                                                                                           | 5 TPS               | Yes                 |
| StartReferencetImportJob, GetReferenceImportJob, ListReferenceImportJobs                                      | 5 TPS               | Yes                 |
| ListReferences, GetReferenceMetadata                                                                          | 5 TPS               | Yes                 |
| StartReadsetActivationJob                                                                                     | 5 TPS               | Yes                 |
| ListReadsetActivationJobs, GetReadSetActivationJob                                                            | 5 TPS               | Yes                 |
| ListMultipartReadSetUploads, ListReadSetUploadParts                                                           | 5 TPS               | Yes                 |
| TagResource, UntagResource, ListTagsForResource                                                               | 5 TPS               | Yes                 | ## Workflow API quotas The following table lists the workflow API operations.   |
| Workflow API operation                                                                                        | Default maximum TPS | Adjustable (Yes/No) |
| ---                                                                                                           | ---                 | ---                 |
| StartRun                                                                                                      | 0.1 TPS             | Yes                 |
| CreateWorkflow                                                                                                | 5 TPS               | Yes                 |
| CancelRun, DeleteRun, GetRun, GetRunTask, ListRunTasks, ListRuns                                              | 10 TPS              | Yes                 |
| CreateRunGroup, DeleteRunGroup, GetRunGroup, ListRunGroups, UpdateRunGroup                                    | 10 TPS              | Yes                 |
| CreateRunCache, UpdateRunCache, DeleteRunCache, GetRunCache, ListRunCaches                                    | 10 TPS              | Yes                 |
| DeleteWorkflow, GetWorkflow, ListWorkflows, UpdateWorkflow                                                    | 10 TPS              | Yes                 | ## Analytics API quotas The following table lists the analytics API operations. |
| Analytics API operation                                                                                       | Default maximum TPS | Adjustable (Yes/No) |
| ---                                                                                                           | ---                 | ---                 |
| CreateVariantStore, DeleteVariantStore, GetVariantStore, ListVariantStores, UpdateVariantStore                | 1 TPS               | No                  |
| StartVariantImportJob, CancelVariantImportJob, GetVariantImportJob, ListVariantImportJobs                     | 1 TPS               | No                  |
| CreateAnnotationStore, DeleteAnnotationStore, GetAnnotationStore, ListAnnotationStores, UpdateAnnotationStore | 1 TPS               | No                  |
| StartAnnotationImportJob, ListAnnotationImportJobs, GetAnnotationImportJob, CancelAnnotationImportJob         | 1 TPS               | No                  |
