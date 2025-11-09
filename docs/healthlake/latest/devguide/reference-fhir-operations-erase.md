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
| ------------------ | ------- | -------- | ------- | ------------------------------------------ |
| `deleteAuditEvent` | boolean | No       | false   | When true, deletes associated audit events |

## Examples

###### Example Request

```
POST [base]/Patient/example-patient/$erase
```

###### Example Response

```
{
      "jobId": "5df47e2f51ff3c731847678cb8cad48e",
      "jobStatus": "SUBMITTED"
    }
```

## Job Status

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

The `$erase` operation:

1. Processes asynchronously to ensure data integrity
2. Maintains ACID transactions
3. Provides job status tracking
4. Permanently removes the specified resource and its versions
5. Includes comprehensive audit logging of deletion activities
6. Supports selective deletion of audit events

## Audit Logging

The `$erase` operation logs as DeleteResource with user ID, timestamp, and resource details.

## Limitations

- `$erased` resource will not appear in search results or `_history` queries.
- Resources being erased may be temporarily inaccessible during processing
- Storage metering is adjusted immediately as resources are permanently removed
