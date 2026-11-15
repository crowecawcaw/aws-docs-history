

# Comparing Resources with `$diff`
<a name="reference-fhir-operations-diff"></a>

AWS HealthLake supports the `$diff` operation, which returns the changes between two FHIR resources as a FHIR `Parameters` resource. For example, after a patient's family name is corrected from `Roe` to `Major`, a `$diff` of version 1 and version 2 of that `Patient` returns one `replace` operation for `Patient.name[0].family`.

`$diff` is not defined in the FHIR R4 specification. It is a HealthLake operation that follows the same request and response shape as the `$diff` operation in HAPI FHIR. Each change in the response is written in FHIRPath Patch format. For more information, see [FHIRPath Patch](https://hl7.org/fhir/fhirpatch.html) on the HL7 website. This page documents only what HealthLake adds to that format.

You can call `$diff` at two levels. Both use `GET` and return the same [Response](#diff-response). The instance level selects versions of one resource, so its parameters, `source` and `target`, are version numbers. The type level selects two resources, so its parameters, `from` and `to`, are references. The response always names the two compared versions `from` and `to`.

## Instance level: compare two versions of one resource
<a name="diff-instance-level"></a>

```
GET [base]/[ResourceType]/[ID]/$diff?source=[VersionID]&target=[VersionID]
```

The following table lists the instance-level parameters.


| Parameter | Required | Default | Description | 
| --- | --- | --- | --- | 
| source | No | target - 1 | Version ID to compare from. Must be a positive integer. | 
| target | No | The latest version | Version ID to compare to. Must be a positive integer. | 
| includeMeta | No | false | When true, changes to meta elements are included in the result. See [What is compared](#diff-comparison). | 

With no parameters, HealthLake compares the version just before the latest to the latest version.
+ If the defaults resolve to version 0, the request fails with HTTP `400`. This happens when the resource has only one version and you pass no parameters, or when you pass `target=1` without `source`.
+ If `source` equals `target`, the response has only `from` and `to`, with no `operation` parameters.
+ If `source` is greater than `target`, the comparison runs from the later version to the earlier one. The operations describe how to get from `source` to `target`.

**Example Request**  


```
GET [base]/Patient/example-patient/$diff?source=1&target=2
```

**Example Response**  


```
{
  "resourceType": "Parameters",
  "parameter": [
    {
      "name": "from",
      "valueReference": { "reference": "Patient/example-patient/_history/1" }
    },
    {
      "name": "to",
      "valueReference": { "reference": "Patient/example-patient/_history/2" }
    },
    {
      "name": "operation",
      "part": [
        { "name": "type", "valueCode": "replace" },
        { "name": "path", "valueString": "Patient.name[0].family" },
        { "name": "previousValue", "valueString": "Roe" },
        { "name": "value", "valueString": "Major" }
      ]
    },
    {
      "name": "operation",
      "part": [
        { "name": "type", "valueCode": "insert" },
        { "name": "path", "valueString": "Patient.name" },
        { "name": "index", "valueInteger": 1 },
        { "name": "value", "valueHumanName": { "family": "Doe" } }
      ]
    },
    {
      "name": "operation",
      "part": [
        { "name": "type", "valueCode": "add" },
        { "name": "path", "valueString": "Patient" },
        { "name": "name", "valueString": "maritalStatus" },
        { "name": "value", "valueCodeableConcept": { "text": "M" } }
      ]
    }
  ]
}
```

## Type level: compare two resources of the same type
<a name="diff-type-level"></a>

```
GET [base]/[ResourceType]/$diff?from=[ID]&to=[ID]
```

The following table lists the type-level parameters.


| Parameter | Required | Default | Description | 
| --- | --- | --- | --- | 
| from | Yes | None | The first resource, in the form [ID], [ResourceType]/[ID], or [ResourceType]/[ID]/\_history/[VersionID]. The resource type comes from the request path, so a [ResourceType]/ prefix is optional. If you include one, it must match the path. Without a version, the current version is used. | 
| to | Yes | None | The second resource, in the same form as from. | 
| includeMeta | No | false | When true, changes to meta elements are included in the result. See [What is compared](#diff-comparison). | 

**Example Request**  


```
GET [base]/Patient/$diff?from=patient-a&to=Patient/patient-b/_history/3
```

**Example Response**  


```
{
  "resourceType": "Parameters",
  "parameter": [
    {
      "name": "from",
      "valueReference": { "reference": "Patient/patient-a/_history/2" }
    },
    {
      "name": "to",
      "valueReference": { "reference": "Patient/patient-b/_history/3" }
    },
    {
      "name": "operation",
      "part": [
        { "name": "type", "valueCode": "replace" },
        { "name": "path", "valueString": "Patient.birthDate" },
        { "name": "previousValue", "valueDate": "1985-04-12" },
        { "name": "value", "valueDate": "1990-01-01" }
      ]
    },
    {
      "name": "operation",
      "part": [
        { "name": "type", "valueCode": "delete" },
        { "name": "path", "valueString": "Patient.telecom[1]" }
      ]
    }
  ]
}
```

## Response
<a name="diff-response"></a>

A successful request returns HTTP `200` and a `Parameters` resource with:
+ A `from` parameter and a `to` parameter. Each holds a versioned reference (`[ResourceType]/[ID]/_history/[VersionID]`) to the version that was compared.
+ One `operation` parameter per change. If nothing changed, the response holds only `from` and `to`.

Each `operation` parameter follows FHIRPath Patch. Its `type` part is one of `replace`, `add`, `insert`, or `delete`, and its `path` part is a FHIRPath such as `Patient.name[0].family`. For the meaning of each type and its parts, see [FHIRPath Patch](https://hl7.org/fhir/fhirpatch.html) on the HL7 website. A `delete` has only `type` and `path`; it does not include the deleted value.

HealthLake adds one part that is not in FHIRPath Patch. The following table describes it.


| Part | Description | 
| --- | --- | 
| previousValue | On replace only. The value in the from version. | 

## What is compared
<a name="diff-comparison"></a>
+ The resource `id` is never compared.
+ When `includeMeta` is false, these elements are not compared: `meta.versionId`, `meta.lastUpdated`, `meta.source`, `meta.tag`, `meta.profile`, `meta.security`, and `meta.extension`.
+ All other elements are compared.

## Throttling and Size Limits
<a name="diff-throttling"></a>

These limits apply per AWS account, per Region. They are not per data store. The following table lists the limits.


| Limit | Value | 
| --- | --- | 
| Requests per second | 50 | 
| Resource data compared per second | 300 MiB | 
| Combined size of the two resources in one request | 60 MiB | 

## Errors
<a name="diff-errors"></a>


| HTTP status | Cause | 
| --- | --- | 
| 400 | A parameter is invalid: a version is not a positive integer, a default version resolves to 0, from or to is missing or malformed, or a reference type does not match the request path. | 
| 400 | The two resources together are larger than 60 MiB. | 
| 403 | On a SMART on FHIR data store, the caller's scope does not allow reading both compared versions. | 
| 404 | The resource or a requested version does not exist. | 
| 410 | The resource is currently deleted, or one of the compared versions is a delete. If a resource was deleted and then created again, compare the versions before and after the delete. | 
| 429 | A per-second limit was exceeded. Retry with exponential backoff. | 

## Limitations
<a name="diff-limitations"></a>
+ `$diff` uses best-effort parsing. Resources stored with minimal validation are compared as far as they can be parsed. Elements that are not valid FHIR may be left out of the result without any warning, or the request may fail to parse the resource.
+ Both resources must be in the same data store and have the same resource type.

## See also
<a name="diff-see-also"></a>
+ [Reading FHIR resource history](managing-fhir-resources-read-history.md)
+ [Modifying Resources with PATCH Operation](managing-fhir-resources-patch.md)
+ [FHIR R4 FHIRPath Patch Specification](https://hl7.org/fhir/fhirpatch.html)