# Searching FHIR resources in AWS HealthLake

Use FHIR [`search`](https://hl7.org/fhir/R4/http.html#search "https://hl7.org/fhir/R4/http.html#search")
interaction to search a set of FHIR resources in a HealthLake data store based on some filter
criteria. The `search` interaction can be performed using either a `GET`
or `POST` request. For searches that involve personally identifiable information (PII) or protected health information (PHI), it's
recommended to use `POST` requests, as PII and PHI is added as part of the request
body and is encrypted in transit.

###### Note

The FHIR `search` interaction described in this chapter is built in conformance
to the HL7 FHIR R4 standard for health care data exchange. Because it is a representation of
a HL7 FHIR service, it is not offered through AWS CLI and AWS SDKs. For more information,
see [`search`](https://hl7.org/fhir/R4/http.html#search "https://hl7.org/fhir/R4/http.html#search") in the
**FHIR R4 RESTful API documentation**.

HealthLake supports a subset of FHIR R4 search parameters. For more information, see
[FHIR R4 search parameters for HealthLake](reference-fhir-search-parameters.md "reference-fhir-search-parameters.md").

###### Topics

- [Searching with GET](searching-fhir-resources-get.md "searching-fhir-resources-get.md")
- [Searching with
  POST](searching-fhir-resources-post.md "searching-fhir-resources-post.md")
- [Search Consistency Levels](searching-fhir-consistency-levels.md "searching-fhir-consistency-levels.md")
