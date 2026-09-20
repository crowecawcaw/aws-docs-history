

# Patching resources at scale with `$bulk-patch`
<a name="reference-fhir-operations-bulk-patch"></a>

AWS HealthLake supports the `$bulk-patch` operation for applying patch operations to large numbers of FHIR resources asynchronously. You can target a specific list of resources by ID, or all resources of a given type within a datastore. With this operation, you can modify resources at scale without updating each resource individually.

The `$bulk-patch` operation is particularly useful when you need to do the following:
+ Apply metadata tags or labels to resources across an entire datastore
+ Update specific fields on thousands or millions of resources
+ Perform bulk data corrections or enrichments
+ Apply compliance-related changes across resource types
+ Migrate or standardize data elements at scale

**Note**  
The `$bulk-patch` operation applies the same patch to every targeted resource. To modify an individual resource, use the PATCH operation. For more information, see [Modifying Resources with PATCH Operation](managing-fhir-resources-patch.md).
Bulk patch applies each patch atomically to each resource. Each resource either succeeds or fails independently.
Resources that are deleted or modified after job submission are skipped rather than patched, to avoid overwriting concurrent changes.

## Usage
<a name="bulk-patch-usage"></a>

The `$bulk-patch` operation is asynchronous. To start a job, submit a POST request:

```
POST [base]/$bulk-patch
```

To poll the status of a job, use the describe endpoint:

```
GET [base]/$bulk-patch/{jobId}
```

To get started with the `$bulk-patch` operation, do the following:

1. Submit a bulk patch request that specifies the target resources and patch operations. The response includes a job ID.

1. Poll the job status using the describe endpoint until the status is `COMPLETED` or `COMPLETED_WITH_ERRORS`.

1. Review the job summary to see how many resources succeeded, failed, or were skipped.

## Parameters
<a name="bulk-patch-parameters"></a>

The `$bulk-patch` operation supports the following parameters.


| Parameter | Type | Required | Description | 
| --- | --- | --- | --- | 
| resourceType | string | Yes | The FHIR resource type to patch, for example Patient or Observation. | 
| resourceIds | string[] | No | The list of resource IDs to patch. When you omit this parameter, the operation patches all resources of the specified type. | 
| operations | object | Yes | The patch operations to apply. Accepts either a JSON Patch array or a FHIR Patch Parameters resource. | 
| clientToken | string | No | User-provided token used for ensuring idempotency. Resubmitting a job with the same client token returns the existing job instead of creating a new one. | 
| validationLevel | string | No | The FHIR validation level applied when updating each resource. Accepted values are strict (default), structure-only, and minimal. | 

## Targeting resources
<a name="bulk-patch-targeting"></a>

You can target resources in two modes.

**Resource type mode**  
In resource type mode, the operation patches all resources of a specific type in the datastore.

```
{
    "resourceType": "Patient",
    "operations": { ... }
}
```

**Resource IDs mode**  
In resource IDs mode, the operation patches a specific list of resources by ID. All resource IDs must be the same type and match the `resourceType` parameter. The format can be a full reference (`[resourceType]/[id]`) or only the ID (`[id]`). The list can contain up to 50,000 resource IDs.

```
{
    "resourceType": "Patient",
    "resourceIds": ["Patient/001", "Patient/002", "Patient/003"],
    "operations": { ... }
}
```

## Supported patch formats
<a name="bulk-patch-formats"></a>

The `$bulk-patch` operation supports both JSON Patch (RFC 6902) and FHIR Patch (FHIRPath-based) syntax. It uses the same set of supported operations and the same syntax as the synchronous PATCH operation. For more information, see [Modifying Resources with PATCH Operation](managing-fhir-resources-patch.md).

## Start bulk patch job example
<a name="bulk-patch-examples"></a>

The following example submits a bulk patch job that adds a compliance tag to specific `Patient` resources using FHIR Patch.

**Example Request**  


```
POST [base]/$bulk-patch
Content-Type: application/json

{
    "resourceType": "Patient",
    "resourceIds": ["patient-1", "patient-2", "patient-3"],
    "validationLevel": "strict",
    "clientToken": "unique-idempotency-token-123",
    "operations": {
        "resourceType": "Parameters",
        "parameter": [
            {
                "name": "operation",
                "part": [
                    {"name": "type", "valueCode": "add"},
                    {"name": "path", "valueString": "Patient.meta"},
                    {"name": "name", "valueString": "tag"},
                    {"name": "value", "valueCoding": {
                        "system": "http://example.org/compliance",
                        "code": "2026-audit-complete"
                    }}
                ]
            }
        ]
    }
}
```

**Example Response**  


```
{
    "datastoreId": "datastoreId",
    "jobId": "jobId",
    "jobStatus": "SUBMITTED"
}
```

## Bulk patch job status polling
<a name="bulk-patch-job-status"></a>

After you submit a job, poll the job status to track progress and retrieve results. The job transitions through `SUBMITTED` and `IN_PROGRESS`, and then to a terminal state of `COMPLETED` or `COMPLETED_WITH_ERRORS`.

```
GET [base]/$bulk-patch/{jobId}
```

The following example shows a response for a job that is in progress.

```
{
    "datastoreId": "datastoreId",
    "jobId": "jobId",
    "status": "IN_PROGRESS",
    "submittedTime": "2026-09-14T06:53:31.429Z",
    "summary": {
        "estimatedResourceCount": 1000
    }
}
```

**Note**  
The `estimatedResourceCount` is exact for resource IDs mode, and is equal to the size of the submitted list. For resource type mode, the actual number of resources processed might differ slightly because resources can be created or deleted while the job is running.

When the job reaches a terminal state, the describe response includes a count summary of succeeded, failed, and skipped resources. If any resources failed or were skipped, the response lists the reasons in `failedResources` and `skippedResources`. The job status is `COMPLETED_WITH_ERRORS` when there are any failures, whether a customer error or a server error. Response size limits the `failedResources` and `skippedResources` lists, so they might be truncated. Check `failedResourcesTruncated` and `skippedResourcesTruncated` to determine whether the full list is included.

```
{
    "datastoreId": "datastoreId",
    "jobId": "jobId",
    "status": "COMPLETED_WITH_ERRORS",
    "submittedTime": "2026-09-14T06:53:31.429Z",
    "endTime": "2026-09-14T07:08:34.930Z",
    "summary": {
        "estimatedResourceCount": 1000,
        "totalResourcesProcessed": 1000,
        "succeeded": 985,
        "failedWithCustomerError": 5,
        "failedWithServerError": 0,
        "skipped": 10
    },
    "failedResources": [
        {
            "resourceId": "Patient/patient-101",
            "message": "FHIR resource in payload failed FHIR validation rules."
        }
    ],
    "skippedResources": [
        {
            "resourceId": "Patient/patient-201",
            "message": "Resource was modified after job submission"
        },
        {
            "resourceId": "Patient/patient-202",
            "message": "Resource was deleted."
        },
        {
            "resourceId": "Patient/patient-203",
            "message": "Resource not found."
        }
    ],
    "failedResourcesTruncated": false,
    "skippedResourcesTruncated": false
}
```

## Common skipped reasons
<a name="bulk-patch-skipped-reasons"></a>

The operation skips a resource when it is in scope but cannot patch the resource because its state changed between job submission and processing. Skipped resources are not considered errors. The following are common reasons that a resource is skipped.
+ **Resource was modified after job submission** — The resource was updated by another operation after the bulk patch job captured its version at submission time. In rare cases, a resource that was successfully patched might be reported as skipped with the reason modified after job submission. This is expected and might occur at a very low rate (1 out of millions of resources).
+ **Resource was deleted after job submission** — The resource was deleted after the job was submitted (resource type mode). Not all deleted resources are guaranteed to appear in the skipped list. If a resource is deleted before the job begins processing, it is excluded from the job scope entirely and is not reflected in the job results.
+ **Resource was deleted** — The specified resource ID is in a deleted state (resource IDs mode).
+ **Resource not found** — The specified resource ID does not exist (resource IDs mode only).

## Common customer failures
<a name="bulk-patch-failures"></a>

A resource fails when the operation cannot apply the patch because of an issue with the resource or the patch operations. Failed resources include an error message with diagnostic details. The following are common customer failures.
+ **FHIR validation failure** — The patched resource fails FHIR validation. Bulk patch applies FHIR validation on the entire patched resource, not just the modified fields. This failure can occur when the patch produces an invalid field value, or when the resource already contains fields that are not FHIR compliant. Use the `validationLevel` parameter to control validation strictness.
+ **Patch application failure** — The patch operations are incompatible with the resource structure, for example, replacing a field that does not exist, or adding to a non-array path.

## Best practices
<a name="bulk-patch-best-practices"></a>

We recommend the following best practices when you use the `$bulk-patch` operation.
+ **Test with synchronous PATCH first.** AWS HealthLake validates patch operation syntax at job submission and rejects invalid payloads synchronously. However, syntactically valid patch operations can still fail at processing time if they do not match the underlying stored resource structure. Understand the characteristics of your target resources and test your patch operations with the synchronous PATCH operation before you run a bulk patch job. This helps you avoid large-scale failures.
+ **Use error and skipped reasons to debug.** Review the `failedResources` and `skippedResources` lists in the describe response to understand why specific resources were not patched.
+ **Verify resource state before retrying.** Patch operations are not idempotent by nature. Applying the same patch twice can produce different results, for example, adding a tag that already exists creates a duplicate. After you see skipped or failed resources, verify the current resource state before you submit a retry job.

## Authorization
<a name="bulk-patch-authorization"></a>

The `$bulk-patch` operation supports the following authorization methods:
+ AWS Identity and Access Management (IAM) Signature Version 4 (SigV4) for programmatic access.
+ SMART on FHIR with the following required scopes:
  + **Scope level** — Only system-level scopes are supported. The operation rejects patient-level and user-level scopes.
  + **Resource type** — Scopes must match the resource type targeted by the job.
  + **Operations** — The required scopes depend on the job mode and SMART version:
    + **Start a job (resource type mode)** — SMART v1 requires `read` and `write` scopes. SMART v2 datastores require `search` and `update` scopes.
    + **Start a job (resource IDs mode)** — SMART v1 requires `read` and `write` scopes. SMART v2 datastores require `read` and `update` scopes.
    + **Describe a job** — Requires the `read` scope.

## Performance characteristics
<a name="bulk-patch-performance"></a>

The `$bulk-patch` operation is designed for high-volume processing and runs asynchronously.
+ **Concurrency** — Each datastore supports a maximum of 1 concurrent bulk patch job. The operation queues additional jobs and starts them automatically when the current job completes.
+ **Scalability** — Each job supports up to 2 billion resources. The operation rejects jobs that exceed this limit. This limit prevents prolonged processing times, during which many resources can change state, and avoids holding datastore job concurrency for an extended period. Use resource IDs mode to partition the workload. Sample response when a job exceeds the supported scale:

  ```
  "status": "COMPLETED_WITH_ERRORS",
  "message": "The requested bulk patch operation exceeds the supported scale."
  ```
+ **Parallel operations** — Bulk patch is not compatible with concurrent bulk delete, import, or export operations on the same datastore.
+ **Cancellation** — Bulk patch jobs cannot be canceled after they are submitted.

## Related operations
<a name="bulk-patch-related"></a>
+ [Modifying Resources with PATCH Operation](managing-fhir-resources-patch.md) — Single-resource PATCH using JSON Patch or FHIR Patch.
+ [Deleting Resource Types with `$bulk-delete`](reference-fhir-operations-bulk-delete.md) — Delete all resources of a specific type.
+ [FHIR R4 `$operations` for HealthLake](reference-fhir-operations.md) — Complete list of supported operations.