# Removing Patient Compartment Resources with `$purge`

AWS HealthLake supports the `$purge` operation, enabling permanent deletion of all resources within a patient's compartment. This operation is particularly useful when you need to:

- Remove all data associated with a patient
- Comply with patient data removal requests
- Manage patient data lifecycle
- Execute comprehensive patient record cleanup

## Usage

The `$purge` operation can be invoked on Patient resources:

```
POST [base]/Patient/[ID]/$purge?deleteAuditEvent=true
```

## Parameters

| Parameter          | Type    | Required | Default                 | Description                                                                                                                         |
| ------------------ | ------- | -------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `deleteAuditEvent` | boolean | No       | false                   | When true, deletes associated audit events                                                                                          |
| `_since`           | string  | No       | Datastore creation time | When entered, selects the starting cutoff time to find resources based on their lastModified time. Cannot be used with start or end |
| `start`            | string  | No       | Datastore creation time | When entered, selects the cutoff time to find resources based on their lastModified time. Can be used with end                      |
| `end`              | string  | No       | Job submission time     | When entered, selects the ending cutoff time to find resources based on their lastModified time                                     | ## Examples ###### Example Request `POST [base]/Patient/example-patient/$purge?deleteAuditEvent=true` ###### Example Response `{ "resourceType": "OperationOutcome", "id": "purge-job", "issue": [ { "severity": "information", "code": "informational", "diagnostics": "Purge job started successfully. Job ID: 12345678-1234-1234-1234-123456789012" } ] }` ## Job Status To check the status of a purge job: `GET [base]/$purge/[jobId]` The operation returns job status information: `{ "resourceType": "Parameters", "parameter": [ { "name": "jobId", "valueString": "12345678-1234-1234-1234-123456789012" }, { "name": "jobStatus", "valueString": "COMPLETED" }, { "name": "totalResourcesDeleted", "valueInteger": 1256 }, { "name": "startTime", "valueInstant": "2023-06-15T10:00:00Z" }, { "name": "endTime", "valueInstant": "2023-06-15T10:05:23Z" } ] }` ## Behavior The `$purge` operation: 1. Processes asynchronously to handle multiple resources 2. Maintains ACID transactions for data integrity 3. Provides job status tracking with resource deletion counts 4. Permanently removes all resources in the patient compartment 5. Includes comprehensive audit logging of deletion activities 6. Supports selective deletion of audit events ## Audit Logging The `$purge` operation logs as StartFHIRBulkDeleteJob and DescribeFHIRBulkDeleteJob with detailed operation information. ## Limitations <br>• Purged resources will not appear in search responses <br>• Resources being purged may be temporarily inaccessible during processing <br>• All resources in the patient compartment are permanently removed |
