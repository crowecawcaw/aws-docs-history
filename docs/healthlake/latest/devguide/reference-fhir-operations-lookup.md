# Retrieving Concept Details with `$lookup`

AWS HealthLake now supports the `$lookup` operation for CodeSystem resources, enabling you to retrieve details about a specific concept in a code system by providing identifying information such as its code. This operation is particularly useful when you need to:

- Retrieve detailed information about specific medical codes
- Validate code meanings and properties
- Access concept definitions and relationships
- Support clinical decision-making with accurate terminology data

## Usage

The `$lookup` operation can be invoked on CodeSystem resources using both GET and POST methods:

###### Supported Operations

```
GET [base]/CodeSystem/$lookup?system=`http://snomed.info/sct&code=73211009&version=20230901`
POST [base]/CodeSystem/$lookup
```

## Supported Parameters

HealthLake supports a subset of FHIR R4 `$lookup` parameters:

| Parameter | Type   | Required | Description                                                                                                              |
| --------- | ------ | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| `code`    | code   | Yes      | The concept code you're looking up (e.g., "71620000" in SNOMED CT)                                                       |
| `system`  | uri    | Yes      | The canonical URL of the code system (e.g., "[http://snomed.info/sct](http://snomed.info/sct "http://snomed.info/sct")") |
| `version` | string | No       | Specific version of the code system                                                                                      |

## Examples

###### GET Request

```
GET [base]/CodeSystem/$lookup?system=`http://snomed.info/sct&code=71620000&version=2023-09`
```

###### POST Request

```
POST [base]/CodeSystem/$lookup
Content-Type: application/fhir+json

{
  "resourceType": "Parameters",
  "parameter": [
    {
      "name": "system",
      "valueUri": "`http://snomed.info/sct`"
    },
    {
      "name": "code",
      "valueCode": "71620000"
    },
    {
      "name": "version",
      "valueString": "2023-09"
    }
  ]
}
```

###### Sample Response

The operation returns a Parameters resource containing the concept details:

```
{
    "resourceType": "Parameters",
    "parameter": [{
            "name": "name",
            "valueString": "SNOMED CT Fractures"
        },
        {
            "name": "version",
            "valueString": "2023-09"
        },
        {
            "name": "display",
            "valueString": "Fracture of femur"
        },
        {
            "name": "property",
            "part": [{
                    "name": "code",
                    "valueCode": "child"
                },
                {
                    "name": "value",
                    "valueCode": "263225007"
                },
                {
                    "name": "description",
                    "valueString": "Fracture of neck of femur"
                }
            ]
        },
        {
            "name": "property",
            "part": [{
                    "name": "code",
                    "valueCode": "child"
                },
                {
                    "name": "value",
                    "valueCode": "263227004"
                },
                {
                    "name": "description",
                    "valueString": "Fracture of shaft of femur"
                }
            ]
        }
    ]
}
```

## Response Parameters

The response includes the following parameters when available:

| Parameter     | Type            | Description                                                            |
| ------------- | --------------- | ---------------------------------------------------------------------- |
| `name`        | string          | Name of the code system                                                |
| `version`     | string          | Version of the code system                                             |
| `display`     | string          | Display name of the concept                                            |
| `designation` | BackboneElement | Additional representations for this concept.                           |
| `property`    | BackboneElement | Additional properties of the concept (definition, relationships, etc.) |

## Behavior

The `$lookup` operation:

1. Validates the required parameters (`code` and `system`)
2. Searches for the concept within the specified code system stored in the datastore
3. Returns detailed concept information including display name, designations, and properties.
4. Supports version-specific lookups when the `version` parameter is provided
5. Operates only on code systems explicitly stored in the HealthLake datastore

## Error Handling

The operation handles the following error conditions:

- 400 Bad Request: Invalid `$lookup` operation (non-conformant request or missing required parameters)
- 404 Not Found: Code system not found or code not found in the specified code system

## Caveats

For this release, the following are not supported:

- `$lookup` operation by calling external terminology servers
- `$lookup` operation on CodeSystems managed by HealthLake but not explicitly stored in the datastore

For more information about the `$lookup` operation specification, see the [FHIR R4 CodeSystem `$lookup`](https://www.hl7.org/fhir/R4/codesystem-operation-lookup.html "https://www.hl7.org/fhir/R4/codesystem-operation-lookup.html") documentation.
