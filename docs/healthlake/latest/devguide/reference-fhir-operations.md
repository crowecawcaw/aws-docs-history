# FHIR R4 `$operations` for HealthLake

FHIR $ operations (also called "dollar operations") are special server-side functions that extend beyond
standard CRUD (`Create`, `Read`, `Update`, `Delete`) operations in the FHIR specification. These operations are identified by
the "$" prefix and enable complex processing, data transformation, and bulk operations that would be difficult or 
 inefficient to perform using standard REST API calls. $ Operations can be invoked at the system level, resource type 
 level, or on specific resource instances, providing flexible ways to interact with FHIR data.
 AWS HealthLake supports multiple FHIR `$operations`. Please refer to each individual pages below for additional details.

###### Topics

- [Deleting Resource Types with $bulk-delete](reference-fhir-operations-bulk-delete.md "reference-fhir-operations-bulk-delete.md")
- [Generating Clinical Documents with $document](reference-fhir-operations-document.md "reference-fhir-operations-document.md")
- [Permanently Removing Resources with $erase](reference-fhir-operations-erase.md "reference-fhir-operations-erase.md")
- [Getting patient data with
  Patient/$everything](reference-fhir-operations-everything.md "reference-fhir-operations-everything.md")
- [Retrieving ValueSet Codes with $expand](reference-fhir-operations-expand.md "reference-fhir-operations-expand.md")
- [Exporting HealthLake data with FHIR
  $export](reference-fhir-operations-export.md "reference-fhir-operations-export.md")
- [Retrieving Concept Details with $lookup](reference-fhir-operations-lookup.md "reference-fhir-operations-lookup.md")
- [Removing Patient Compartment Resources with $purge](reference-fhir-operations-purge.md "reference-fhir-operations-purge.md")
- [Validating FHIR Resources with $validate](reference-fhir-operations-validate.md "reference-fhir-operations-validate.md")
