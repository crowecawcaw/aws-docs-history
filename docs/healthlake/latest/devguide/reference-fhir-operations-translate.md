# Mapping Codes Between Terminologies with `$translate`

AWS HealthLake supports the `$translate` operation for ConceptMap resources, enabling you to map a code from one code system to an equivalent code in another using ConceptMaps you have ingested into your datastore. This operation is particularly useful when you need to:

- Map codes between terminologies (for example, ICD-10-CM to SNOMED CT)
- Normalize incoming data to a canonical code system
- Support interoperability across systems that use different terminologies
- Run clinical data analytics by standardizing heterogeneous source terminologies

## Usage

The `$translate` operation can be invoked on ConceptMap resources using both GET and POST methods:

###### Supported Operations

```
GET  [base]/ConceptMap/$translate?url={...}&system={...}&code={...}
GET  [base]/ConceptMap/[id]/$translate?system={...}&code={...}
POST [base]/ConceptMap/$translate
POST [base]/ConceptMap/[id]/$translate
```

## Supported Parameters

HealthLake supports a subset of FHIR R4 `$translate` parameters:

| Parameter      | Type | Required | Description                                                 |
| -------------- | ---- | -------- | ----------------------------------------------------------- |
| `code`         | code | Yes      | The source code to translate                                |
| `system`       | uri  | Yes      | The code system the code belongs to                         |
| `url`          | uri  | No       | Canonical URL of a specific ConceptMap to translate against |
| `source`       | uri  | No       | Restricts to maps whose source value set equals this URI    |
| `target`       | uri  | No       | Restricts to maps whose target value set equals this URI    |
| `targetsystem` | uri  | No       | Restricts matches to target codes in this code system       |

###### Note

The `url`, `source`, and `target` parameters are scope filters that apply only to the type-level invocation (`[base]/ConceptMap/$translate`). On the instance invocation (`ConceptMap/[id]/$translate`) they are ignored, as only `code`, `system`, and `targetsystem` take effect.

## Examples

###### GET Request (by ConceptMap ID)

```
GET [base]/ConceptMap/example-conceptmap/$translate?system=`http://snomed.info/sct`&code=`44054006`
```

###### GET Request (by canonical URL)

```
GET [base]/ConceptMap/$translate?url=`http://example.com/ConceptMap/sct-to-icd10`&system=`http://snomed.info/sct`&code=`44054006`
```

###### POST Request

```
POST [base]/ConceptMap/$translate
Content-Type: application/fhir+json

{
  "resourceType": "Parameters",
  "parameter": [
    {
      "name": "url",
      "valueUri": "`http://example.com/ConceptMap/sct-to-icd10`"
    },
    {
      "name": "system",
      "valueUri": "`http://snomed.info/sct`"
    },
    {
      "name": "code",
      "valueCode": "44054006"
    },
    {
      "name": "targetsystem",
      "valueUri": "`http://hl7.org/fhir/sid/icd-10-cm`"
    }
  ]
}
```

###### Sample Response

The operation returns a `Parameters` resource. The `result` parameter indicates whether a match was found. Each `match` contains the target `concept` and an `equivalence`:

```
{
  "resourceType": "Parameters",
  "parameter": [
    {
      "name": "result",
      "valueBoolean": true
    },
    {
      "name": "match",
      "part": [
        {
          "name": "equivalence",
          "valueCode": "equivalent"
        },
        {
          "name": "concept",
          "valueCoding": {
            "system": "http://hl7.org/fhir/sid/icd-10-cm",
            "code": "E11.9",
            "display": "Type 2 diabetes mellitus without complications"
          }
        }
      ]
    }
  ]
}
```

## Response Parameters

The response includes the following parameters:

| Parameter           | Type            | Description                                                      |
| ------------------- | --------------- | ---------------------------------------------------------------- |
| `result`            | boolean         | Whether a match was found                                        |
| `match`             | BackboneElement | A match found in the ConceptMap                                  |
| `match.equivalence` | code            | The degree of equivalence between the source and target concepts |
| `match.concept`     | Coding          | The target concept (includes system, code, and display)          |

## Behavior

The `$translate` operation:

1. Validates the required parameters (`code` and `system`).
2. Resolves the ConceptMap by instance `[id]` or by canonical `url`.
3. Translates the source code, optionally filtering matches to `targetsystem` when provided.
4. Returns `result: true` with one `match` per equivalent target code, or `result: false` when no mapping exists.

## Error Handling

The operation handles the following error conditions:

- 400 Bad Request: Invalid `$translate` request (non-conformant request or missing required parameters)
- 404 Not Found: ConceptMap not found in the datastore

## Caveats

For this release, the following are not supported:

- `reverse` parameter (reverse translation from target to source)
- Chained translations across multiple ConceptMaps
- Since more than 10 ConceptMap resources can match the `$translate` query, only matches from the first 10 ConceptMaps are returned, ordered by the ConceptMap's `date` field (most recent first).

For more information about the `$translate` operation specification, see the [FHIR R4 ConceptMap `$translate`](https://www.hl7.org/fhir/R4/conceptmap-operation-translate.html "https://www.hl7.org/fhir/R4/conceptmap-operation-translate.html") documentation.
