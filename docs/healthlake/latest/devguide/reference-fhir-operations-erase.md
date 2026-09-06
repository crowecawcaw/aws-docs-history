

# Permanently Removing Resources with `$erase`
<a name="reference-fhir-operations-erase"></a>

AWS HealthLake supports the `$erase` operation, enabling permanent deletion of a specific resource and its historical versions. This operation is particularly useful when you need to:
+ Permanently remove individual resources
+ Delete specific version histories
+ Manage individual resource lifecycles
+ Comply with specific data removal requirements

## Usage
<a name="erase-usage"></a>

The `$erase` operation can be invoked at two levels:

**Resource Instance Level**  


```
POST [base]/[ResourceType]/[ID]/$erase?deleteAuditEvent=true
```

**Version-Specific Level**  


```
POST [base]/[ResourceType]/[ID]/_history/[VersionID]/$erase
```

## Parameters
<a name="erase-parameters"></a>


| Parameter | Type | Required | Default | Description | 
| --- | --- | --- | --- | --- | 
| deleteAuditEvent | boolean | No | false | When true, deletes associated audit events | 

## Examples
<a name="erase-examples"></a>

**Example Request**  


```
POST [base]/Patient/example-patient/$erase
```

**Example Response**  


```
{
      "jobId": "5df47e2f51ff3c731847678cb8cad48e",
      "jobStatus": "SUBMITTED"
    }
```

## Job Status
<a name="erase-job-status"></a>

To check the status of an erase job:

```
GET [base]/$erase/[jobId]
```

The operation returns job status information:

```
{
      "datastoreId": "36622996b1fcecb7e12ee2ee085308d3",
      "jobId": "5df47e2f51ff3c731847678cb8cad48e",
      "status": "COMPLETED",
      "submittedTime": "2025-10-30T16:39:24.160Z"
    }
```

## Behavior
<a name="erase-behavior"></a>

The `$erase` operation:

1. Processes asynchronously to ensure data integrity

1. Maintains ACID transactions

1. Provides job status tracking

1. Permanently removes the specified resource and its versions

1. Includes comprehensive audit logging of deletion activities

1. Supports selective deletion of audit events

## Audit Logging
<a name="erase-audit-logging"></a>

The `$erase` operation logs as DeleteResource with user ID, timestamp, and resource details.

## Limitations
<a name="erase-limitations"></a>
+ `$erased` resource will not appear in search results or `_history` queries.
+ Resources being erased may be temporarily inaccessible during processing
+ Storage metering is adjusted immediately as resources are permanently removed