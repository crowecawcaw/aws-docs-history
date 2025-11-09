# Deleting Resource Types with `$bulk-delete`

AWS HealthLake supports the `$bulk-delete` operation, enabling deletion of all resources of a specific type within a datastore. This operation is particularly useful when you need to:

- Perform seasonal auditing and clean-up
- Manage data lifecycle at scale
- Remove specific resource types
- Comply with data retention policies

## Usage

The `$bulk-delete` operation can be invoked using POST methods:

```
POST [base]/[ResourceType]/$bulk-delete?isHardDelete=false&deleteAuditEvent=true
```

## Parameters

| Parameter          | Type    | Required | Default                 | Description                                                                                                                         |
| ------------------ | ------- | -------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `isHardDelete`     | boolean | No       | false                   | When true, permanently removes resources from storage                                                                               |
| `deleteAuditEvent` | boolean | No       | true                    | When true, deletes associated audit events                                                                                          |
| `_since`           | string  | No       | Datastore creation time | When entered, selects the starting cutoff time to find resources based on their lastModified time. Cannot be used with start or end |
| `start`            | string  | No       | Datastore creation time | When entered, selects the cutoff time to find resources based on their lastModified time. Can be used with end                      |
| `end`              | string  | No       | Job submission time     | When entered, selects the ending cutoff time to find resources based on their lastModified time                                     |

## Examples

###### Example Request

```
POST [base]/Observation/$bulk-delete?isHardDelete=false
```

###### Example Response

```
{
      "jobId": "jobId",
      "jobStatus": "SUBMITTED"
    }
```

## Job Status

To check the status of a bulk delete job:

```
GET [base]/$bulk-delete/[jobId]
```

The operation returns job status information:

```
{
      "datastoreId": "datastoreId",
      "jobId": "jobId",
      "status": "COMPLETED",
      "submittedTime": "2025-10-09T15:09:51.336Z"
    }
```

## Behavior

The `$bulk-delete` operation:

1. Processes asynchronously to handle large volumes of resources
2. Maintains ACID transactions for data integrity
3. Provides job status tracking with resource deletion counts
4. Supports both soft and hard deletion modes
5. Includes comprehensive audit logging of deletion activities
6. Allows for selective deletion of historical versions and audit events

## Audit Logging

The `$bulk-delete` operation logs as StartFHIRBulkDeleteJob and DescribeFHIRBulkDeleteJob with detailed operation information.

## Limitations

- When `isHardDelete` is set to true, hard-deleted resources will not appear in search results or `_history` queries.
- Resources being deleted through this operation may be temporarily inaccessible during processing
- Storage metering is adjusted on historical versions only - deleteVersionHistory=false will not adjust datastore storage
