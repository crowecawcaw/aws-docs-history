# Using FHIR REST API interactions

By default, traits detected by the Amazon Comprehend Medical API operations are not returned when making a
`GET` request. To see the results of the integrated NLP operations, you must
specify a known `ID` for the following FHIR resource types.

- `Linkage`
- `Observation`
- `Condition`
- `MedicationStatement`
  The results of HealthLake integrated NLP actions outside the `DocumentReference`
  resource type are available using a `GET` request where the specified
  `ID` is know to contain results from the Amazon Comprehend Medical API operations.
