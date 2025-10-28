# Permanently Removing Resources with `$erase`

AWS HealthLake supports the `$erase` operation, enabling permanent deletion of a specific resource and its historical versions. This operation is particularly useful when you need to:

- Permanently remove individual resources
- Delete specific version histories
- Manage individual resource lifecycles
- Comply with specific data removal requirements

## Usage

The `$erase` operation can be invoked at two levels:

###### Resource Instance Level

```
POST [base]/[ResourceType]/[ID]/$erase?deleteAuditEvent=true
```

###### Version-Specific Level

```
POST [base]/[ResourceType]/[ID]/_history/[VersionID]/$erase
```

## Parameters

| Parameter          | Type    | Required | Default | Description                                |
| ------------------ | ------- | -------- | ------- | ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `deleteAuditEvent` | boolean | No       | false   | When true, deletes associated audit events | ## Examples ###### Example Request `POST [base]/Patient/example-patient/$erase?deleteAuditEvent=true` ###### Example Response `{ "resourceType": "OperationOutcome", "id": "erase-job", "issue": [ { "severity": "information", "code": "informational", "diagnostics": "Erase job started successfully. Job ID: 12345678-1234-1234-1234-123456789012" } ] }` ## Job Status To check the status of an erase job: `GET [base]/$erase/[jobId]` The operation returns job status information: `{ "resourceType": "Parameters", "parameter": [ { "name": "jobId", "valueString": "12345678-1234-1234-1234-123456789012" }, { "name": "jobStatus", "valueString": "COMPLETED" }, { "name": "totalResourcesDeleted", "valueInteger": 1 }, { "name": "startTime", "valueInstant": "2023-06-15T10:00:00Z" }, { "name": "endTime", "valueInstant": "2023-06-15T10:05:23Z" } ] }` ## Behavior The `$erase` operation: 1. Processes asynchronously to ensure data integrity 2. Maintains ACID transactions 3. Provides job status tracking 4. Permanently removes the specified resource and its versions 5. Includes comprehensive audit logging of deletion activities 6. Supports selective deletion of audit events ## Audit Logging The `$erase` operation logs as DeleteResource with user ID, timestamp, and resource details. ## Limitations <br>• Erased resources will not appear in search responses <br>• Resources being erased may be temporarily inaccessible during processing <br>• Storage metering is adjusted immediately as resources are permanently removed |
