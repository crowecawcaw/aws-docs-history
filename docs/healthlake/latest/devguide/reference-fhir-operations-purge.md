

# Removing Patient Compartment Resources with `$purge`
<a name="reference-fhir-operations-purge"></a>

AWS HealthLake supports the `$purge` operation, enabling permanent deletion of all resources within a patient's compartment. This operation is particularly useful when you need to:
+ Remove all data associated with a patient
+ Comply with patient data removal requests
+ Manage patient data lifecycle
+ Execute comprehensive patient record cleanup

## Usage
<a name="purge-usage"></a>

The `$purge` operation can be invoked on Patient resources:

```
POST [base]/Patient/[ID]/$purge?deleteAuditEvent=true
```

## Parameters
<a name="purge-parameters"></a>


| Parameter | Type | Required | Default | Description | 
| --- | --- | --- | --- | --- | 
| deleteAuditEvent | boolean | No | false | When true, deletes associated audit events | 
| \_since | string | No | Datastore creation time | When entered, selects the starting cutoff time to find resources based on their lastModified time. Cannot be used with start or end | 
| start | string | No | Datastore creation time | When entered, selects the cutoff time to find resources based on their lastModified time. Can be used with end | 
| end | string | No | Job submission time | When entered, selects the ending cutoff time to find resources based on their lastModified time | 

## Examples
<a name="purge-examples"></a>

**Example Request**  


```
POST [base]/Patient/example-patient/$purge?deleteAuditEvent=true
```

**Example Response**  


```
{
  "resourceType": "OperationOutcome",
  "id": "purge-job",
  "issue": [
    {
      "severity": "information",
      "code": "informational",
      "diagnostics": "Purge job started successfully. Job ID: 12345678-1234-1234-1234-123456789012"
    }
  ]
}
```

## Job Status
<a name="purge-job-status"></a>

To check the status of a purge job:

```
GET [base]/$purge/[jobId]
```

The operation returns job status information:

```
{
      "datastoreId": "36622996b1fcecb7e12ee2ee085308d3",
      "jobId": "3dd1c7a5b6c0ef8c110f566eb87e2ef9",
      "status": "COMPLETED",
      "submittedTime": "2025-10-31T18:43:21.822Z"
    }
```

## Behavior
<a name="purge-behavior"></a>

The `$purge` operation:

1. Processes asynchronously to handle multiple resources

1. Maintains ACID transactions for data integrity

1. Provides job status tracking with resource deletion counts

1. Permanently removes all resources in the patient compartment

1. Includes comprehensive audit logging of deletion activities

1. Supports selective deletion of audit events

## Audit Logging
<a name="purge-audit-logging"></a>

The `$purge` operation logs as StartFHIRBulkDeleteJob and DescribeFHIRBulkDeleteJob with detailed operation information.

## Limitations
<a name="purge-limitations"></a>
+ Purged resources will not appear in search responses
+ Resources being purged may be temporarily inaccessible during processing
+ All resources in the patient compartment are permanently removed