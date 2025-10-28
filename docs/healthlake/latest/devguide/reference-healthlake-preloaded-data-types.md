# Synthea preloaded data types for

HealthLake

HealthLake supports only SYNTHEA as a preloaded data type. [Synthea](https://synthetichealth.github.io/synthea/ "https://synthetichealth.github.io/synthea/") is a synthetic patient
generator that models `Patient` medical history. It’s hosted in an open-source Git
repository that allows HealthLake to generate a FHIR R4-compliant resource `Bundle` so
that users can test models without using actual patient data.

The following resource types are available in preloaded HealthLake data stores. For more information
about preloading HealthLake data stores with Synthea data, see [Creating a HealthLake data store](managing-data-stores-create.md "managing-data-stores-create.md").

###### Note

To view a full list of HealthLake-supported FHIR R4 resources, see [FHIR R4 supported resource types for HealthLake](reference-fhir-resource-types.md "reference-fhir-resource-types.md").

Synthea FHIR resource types supported by HealthLake| AllergyIntolerance | Location |
| CarePlan | MedicationAdministration |
| CareTeam | MedicationRequest |
| Claim | Observation |
| Condition | Organization |
| Device | Patient |
| DiagnosticReport | Practitioner |
| Encounter | PractitionerRole |
| ExplanationofBenefit | Procedure |
| ImagingStudy | Provenance |
| Immunization | |
