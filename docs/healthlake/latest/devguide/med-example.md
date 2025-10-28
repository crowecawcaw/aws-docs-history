# HealthLake Integrated NLP libraries

HealthLake infers data found in the `DocumentReference` resource type using Amazon Comprehend Medical
libraries. The Amazon Comprehend Medical API operations `DetectEntities-V2`,
`InferICD10-CM`, and `InferRxNorm` detect medical conditions as
_traits_. Each operation provides different insights.

###### Language support

Amazon Comprehend Medical API operations only detect medical entities in English language texts.

- **DetectEntities-V2**: Inspects the clinical text for a
  variety of medical entities and returns specific information about them, such as entity
  category, location, and confidence score.
- **InferICD10-CM**: Detects medical conditions in a
  patient record as entities, and it links those entities to normalized concept identifiers
  in the ICD-10-CM knowledge base from the CDC's National Center for Health Statistics under
  authorization by the World Health Organization (WHO).
- **InferRxNorm**: Detects medications as entities listed
  in a patient record, and it links them to the normalized concept identifiers in the RxNorm
  database from the National Library of Medicine.
  The supported traits for each API operation are `SIGN`, `SYMPTOM`,
  and `DIAGNOSIS`. If traits are detected, they are added as FHIR-compliant
  extensions to different locations in your HealthLake data store.

###### Locations where extensions are added.

- `DocumentReference`: The results from the Amazon Comprehend Medical API operations are added
  as an `extension` to each document found within the
  `DocumentReference` resource type. Results in the extension are divided into
  two groups. You can find them in the results based on their `URL`.
  - `http://healthlake.amazonaws.com/system-generated-resources/`
    - These are resource types that have been created or added to by HealthLake.

  - `http://healthlake.amazonaws.com/aws-cm/`
    - Where the raw output of the Amazon Comprehend Medical API operations is added to your HealthLake data
      store.

- `Linkage`: This resource type is either added or created as a result of the
  integrated NLP. A `GET` request on a specific `Linkage` returns a
  list of linked resources. To identify if a `Linkage` was added by HealthLake, look
  for the added `"tag": [{"display": "SYSTEM_GENERATED"}]` key-value pair. To
  learn more about the FHIR specifications for Linkage, see [`Linkage`](https://hl7.org/fhir/R4/linkage.html "https://hl7.org/fhir/R4/linkage.html") in the
  **FHIR R4 documentation**.
- FHIR resource types generated as a result of the Amazon Comprehend Medical operations.
  - `Observation`: includes results from the Amazon Comprehend Medical API actions
    `DetectEntities-V2` and `InferICD10-CM` when the traits are
    `SIGN` or `SYMPTOM`.
  - `Condition`: includes results from the Amazon Comprehend Medical API actions
    `DetectEntities-V2` and `InferICD10-CM` when the trait is
    `DIAGNOSIS`.
  - `MedicationStatement`: includes results from the Amazon Comprehend Medical API actions
    `InferRxNorm`.
