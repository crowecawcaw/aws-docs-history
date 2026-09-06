

# Modifying Resources with PATCH Operation
<a name="managing-fhir-resources-patch"></a>

AWS HealthLake supports the PATCH operation for FHIR resources, enabling you to modify resources by targeting specific elements to add, replace, or delete without updating the entire resource. This operation is particularly useful when you need to:
+ Make targeted updates to large resources
+ Reduce network bandwidth usage
+ Perform atomic modifications on specific resource elements
+ Minimize the risk of overwriting concurrent changes
+ Update resources as part of batch and transaction workflows

## Supported PATCH Formats
<a name="patch-supported-formats"></a>

AWS HealthLake supports two standard PATCH formats:

### JSON Patch (RFC 6902)
<a name="patch-format-json"></a>

Uses JSON Pointer syntax to target elements by their position in the resource structure.

**Content-Type:** `application/json-patch+json`

### FHIRPath Patch (FHIR R4 Specification)
<a name="patch-format-fhirpath"></a>

Uses FHIRPath expressions to target elements by their content and relationships, providing a FHIR-native approach to patching.

**Content-Type:** `application/fhir+json`

## Usage
<a name="patch-usage"></a>

### Direct PATCH Operations
<a name="patch-usage-direct"></a>

The PATCH operation can be invoked directly on FHIR resources using the PATCH HTTP method:

```
PATCH [base]/[resource-type]/[id]{?_format=[mime-type]}
```

### PATCH in Bundles
<a name="patch-usage-bundles"></a>

PATCH operations can be included as entries within FHIR Bundles of type `batch` or `transaction`, enabling you to combine patch operations with other FHIR interactions (create, read, update, delete) in a single request.
+ **Transaction bundles**: All entries succeed or fail atomically
+ **Batch bundles**: Each entry is processed independently

## JSON Patch Format
<a name="patch-json-format"></a>

### Supported Operations
<a name="patch-json-supported-operations"></a>


| Operation | Description | 
| --- | --- | 
| add | Add a new value to the resource | 
| remove | Remove a value from the resource | 
| replace | Replace an existing value in the resource | 
| move | Remove a value from one location and add it to another | 
| copy | Copy a value from one location to another | 
| test | Test that a value at the target location equals a specified value | 

### Path Syntax
<a name="patch-json-path-syntax"></a>

JSON Patch uses JSON Pointer syntax (RFC 6901):


| Path Example | Description | 
| --- | --- | 
| /name/0/family | First name's family element | 
| /telecom/- | Append to telecom array | 
| /active | Root-level active element | 
| /address/0/line/1 | Second line of first address | 

### Examples
<a name="patch-json-examples"></a>

**Direct JSON Patch Request with Multiple Operations**  


```
PATCH [base]/Patient/example
Content-Type: application/json-patch+json
If-Match: W/"1"

[
  {
    "op": "replace",
    "path": "/name/0/family",
    "value": "Smith"
  },
  {
    "op": "add",
    "path": "/telecom/-",
    "value": {
      "system": "phone",
      "value": "555-555-5555",
      "use": "home"
    }
  },
  {
    "op": "remove",
    "path": "/address/0"
  },
  {
    "op": "move",
    "from": "/name/0/family",
    "path": "/name/1/family"
  },
  {
    "op": "test",
    "path": "/gender",
    "value": "male"
  },
  {
    "op": "copy",
    "from": "/name/0",
    "path": "/name/1"
  }
]
```

**Direct JSON Patch Request with Single Operation**  


```
PATCH [base]/Patient/example
Content-Type: application/json-patch+json

[
  {
    "op": "replace",
    "path": "/active",
    "value": false
  }
]
```

**JSON Patch in Bundle**  
Use a Binary resource containing the base64-encoded JSON Patch payload:

```
{
  "resourceType": "Bundle",
  "type": "transaction",
  "entry": [{
    "resource": {
      "resourceType": "Binary",
      "contentType": "application/json-patch+json",
      "data": "W3sib3AiOiJhZGQiLCJwYXRoIjoiL2JpcnRoRGF0ZSIsInZhbHVlIjoiMTk5MC0wMS0wMSJ9XQ=="
    },
    "request": {
      "method": "PATCH",
      "url": "Patient/123"
    }
  }]
}
```

## FHIRPath Patch Format
<a name="patch-fhirpath-format"></a>

### Supported Operations
<a name="patch-fhirpath-supported-operations"></a>


| Operation | Description | 
| --- | --- | 
| add | Add a new element to a resource | 
| insert | Insert an element at a specific position in a list | 
| delete | Remove an element from a resource | 
| replace | Replace the value of an existing element | 
| move | Reorder elements within a list | 

### Path Syntax
<a name="patch-fhirpath-path-syntax"></a>

FHIRPath Patch uses FHIRPath expressions, supporting:
+ **Index-based access**: `Patient.name[0]`
+ **Filtering with `where()`**: `Patient.name.where(use = 'official')`
+ **Boolean logic**: `Patient.telecom.where(system = 'phone' and use = 'work')`
+ **Subsetting functions**: `first()`, `last()`
+ **Existence checks**: `exists()`, `count()`
+ **Polymorphic navigation**: `Observation.value`

### Examples
<a name="patch-fhirpath-examples"></a>

**Direct FHIRPath Patch Request**  


```
PATCH [base]/Patient/123
Content-Type: application/fhir+json
Authorization: ...

{
  "resourceType": "Parameters",
  "parameter": [{
    "name": "operation",
    "part": [
      { "name": "type", "valueCode": "add" },
      { "name": "path", "valueString": "Patient" },
      { "name": "name", "valueString": "birthDate" },
      { "name": "value", "valueDate": "1990-01-01" }
    ]
  }]
}
```

**FHIRPath Patch in Bundle**  
Use a Parameters resource as the entry resource with `method: PATCH`:

```
{
  "resourceType": "Bundle",
  "type": "transaction",
  "entry": [{
    "resource": {
      "resourceType": "Parameters",
      "parameter": [{
        "name": "operation",
        "part": [
          { "name": "type", "valueCode": "add" },
          { "name": "path", "valueString": "Patient" },
          { "name": "name", "valueString": "birthDate" },
          { "name": "value", "valueDate": "1990-01-01" }
        ]
      }]
    },
    "request": {
      "method": "PATCH",
      "url": "Patient/123"
    }
  }]
}
```

## Request Headers
<a name="patch-request-headers"></a>


| Header | Required | Description | 
| --- | --- | --- | 
| Content-Type | Yes | application/json-patch\+json for JSON Patch or application/fhir\+json for FHIRPath Patch | 
| If-Match | No | Version-specific conditional update using ETag | 

## Sample Response
<a name="patch-sample-response"></a>

The operation returns the updated resource with new version information:

```
HTTP/1.1 200 OK
Content-Type: application/fhir+json
ETag: W/"2"
Last-Modified: Mon, 05 May 2025 10:10:10 GMT

{
  "resourceType": "Patient",
  "id": "example",
  "active": true,
  "name": [
    {
      "family": "Smith",
      "given": ["John"]
    }
  ],
  "telecom": [
    {
      "system": "phone",
      "value": "555-555-5555",
      "use": "home"
    }
  ],
  "meta": {
    "versionId": "2",
    "lastUpdated": "2025-05-05T10:10:10Z"
  }
}
```

## Behavior
<a name="patch-behavior"></a>

The PATCH operation:
+ Validates the patch syntax according to the appropriate specification (RFC 6902 for JSON Patch, FHIR R4 for FHIRPath Patch)
+ Applies operations atomically - all operations succeed or all fail
+ Updates the resource version ID and creates a new history entry
+ Preserves the original resource in history before applying changes
+ Validates FHIR resource constraints after applying patches
+ Supports conditional updates using If-Match header with ETag

## Error Handling
<a name="patch-error-handling"></a>

The operation handles the following error conditions:
+ **400 Bad Request**: Invalid patch syntax (non-conformant request or malformed patch document)
+ **404 Not Found**: Resource not found (specified ID does not exist)
+ **409 Conflict**: Version conflict (concurrent updates or non-current version ID provided)
+ **422 Unprocessable Entity**: Patch operations cannot be applied to the specified resource elements

## Summary of Capabilities
<a name="patch-summary-of-capabilities"></a>


| Capability | JSON Patch | FHIRPath Patch | 
| --- | --- | --- | 
| Content Type | application/json-patch\+json | application/fhir\+json | 
| Path Format | JSON Pointer (RFC 6901) | FHIRPath expressions | 
| Direct PATCH API | Supported | Supported | 
| Bundle Batch | Supported (via Binary) | Supported (via Parameters) | 
| Bundle Transaction | Supported (via Binary) | Supported (via Parameters) | 
| Operations | add, remove, replace, move, copy, test | add, insert, delete, replace, move | 

## Limitations
<a name="patch-limitations"></a>
+ Conditional PATCH operations using search conditions are not supported
+ JSON Patch in bundles must use Binary resources with base64-encoded content
+ FHIRPath Patch in bundles must use Parameters resources

## Additional Resources
<a name="patch-additional-resources"></a>

For more information about PATCH operations, see:
+ [FHIR R4 PATCH Documentation](https://hl7.org/fhir/http.html#patch)
+ [FHIR R4 FHIRPath Patch Specification](https://hl7.org/fhir/fhirpatch.html)
+ [RFC 6902 - JSON Patch](https://datatracker.ietf.org/doc/html/rfc6902#section-4)
+ [RFC 6901 - JSON Pointer](https://datatracker.ietf.org/doc/html/rfc6901)