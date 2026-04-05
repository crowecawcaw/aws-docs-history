# Managing Library Entities

This section describes how to manage entities within your Data Automation Libraries. Entities are domain-specific resources that enhance extraction accuracy for your content processing workloads. Currently, [Custom Vocabulary](bda-library-custom-vocabulary.md "bda-library-custom-vocabulary.md") is the only supported entity type, which improves speech recognition and transcription for audio and video content.

You can perform entity-level operations using the AWS Management Console or AWS CLI. These operations include adding new entities via ingestion jobs with the vocabulary input provided either through S3 manifest files or inline payloads, monitoring status of such ingestion jobs, updating existing entities using UPSERT operations, deleting specific entities, and viewing entity details. Unlike library-level operations that manage the container itself, entity operations focus on the content within your libraries.

Managing library entities can be done using these APIs:

- [InvokeDataAutomationLibraryIngestionJob](../APIReference/API_data-automation_InvokeDataAutomationLibraryIngestionJob.md "../APIReference/API_data-automation_InvokeDataAutomationLibraryIngestionJob.md") adds, updates, or deletes entities through asynchronous ingestion jobs using UPSERT or DELETE operations;
- [GetDataAutomationLibraryIngestionJob](../APIReference/API_data-automation_GetDataAutomationLibraryIngestionJob.md "../APIReference/API_data-automation_GetDataAutomationLibraryIngestionJob.md") checks the status and progress of ingestion jobs;
- [ListDataAutomationLibraryIngestionJobs](../APIReference/API_data-automation_ListDataAutomationLibraryIngestionJobs.md "../APIReference/API_data-automation_ListDataAutomationLibraryIngestionJobs.md") retrieves a paginated list of all the ingestion jobs in account;
- [ListDataAutomationLibraryEntities](../APIReference/API_data-automation_ListDataAutomationLibraryEntities.md "../APIReference/API_data-automation_ListDataAutomationLibraryEntities.md") retrieves a paginated list of all entities within a library; and
- [GetDataAutomationLibraryEntity](../APIReference/API_data-automation_GetDataAutomationLibraryEntity.md "../APIReference/API_data-automation_GetDataAutomationLibraryEntity.md") retrieves detailed information about a specific entity including all vocabulary phrases.
  **Note**: Entity management is distinct from library management. For information about creating, updating, or deleting libraries, see [Managing Data Automation Library](bda-library-managing.md "bda-library-managing.md").
