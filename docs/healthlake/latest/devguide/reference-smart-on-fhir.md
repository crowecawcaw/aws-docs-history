# SMART on FHIR support for AWS HealthLake

A Substitutable Medical Applications and Reusable Technologies (SMART) on FHIR enabled HealthLake
data store allows access to SMART on FHIR compliant applications. HealthLake data is accessed by
authenticating and authorizing requests using a third-party authorization server. So instead of
managing user credentials via AWS Identity and Access Management, you are doing so using a SMART on FHIR compliant
authorization server.

###### Note

HealthLake supports SMART on FHIR versions 1.0 and 2.0. To learn more about these frameworks, see [SMART App Launch](https://www.hl7.org/fhir/smart-app-launch/ "https://www.hl7.org/fhir/smart-app-launch/") in the _FHIR R4 documentation_.

HealthLake data stores support the following authentication and authorization frameworks for
SMART on FHIR requests:

- **OpenID (AuthN)**: for authenticating the person or
  client application is who (or what) they claim to be.
- **OAuth 2.0 (AuthZ)**: for authorizing which FHIR
  resources in your HealthLake data store an authenticated request can read or write to. This is
  defined by the scopes set up in your authorization server.
  You can create a SMART on FHIR enabled data store using the AWS CLI or AWS SDKs. For more
  information, see [Creating a HealthLake data store](managing-data-stores-create.md "managing-data-stores-create.md").

###### Topics

- [Getting started with
  SMART on FHIR](reference-smart-on-fhir-getting-started.md "reference-smart-on-fhir-getting-started.md")
- [HealthLake authentication requirements
  for SMART on FHIR](reference-smart-on-fhir-authentication.md "reference-smart-on-fhir-authentication.md")
- [SMART on FHIR OAuth 2.0 scopes
  supported by HealthLake](reference-smart-on-fhir-oauth-scopes.md "reference-smart-on-fhir-oauth-scopes.md")
- [Token validation using
  AWS Lambda](reference-smart-on-fhir-token-validation.md "reference-smart-on-fhir-token-validation.md")
- [Using fine-grained
  authorization with a SMART on FHIR enabled HealthLake data store](reference-smart-on-fhir-fine-grained-authorization.md "reference-smart-on-fhir-fine-grained-authorization.md")
- [Fetching the SMART on FHIR
  Discovery Document](reference-smart-on-fhir-discovery-document.md "reference-smart-on-fhir-discovery-document.md")
- [Making a FHIR REST API request on a
  SMART-enabled HealthLake data store](reference-smart-on-fhir-request-example.md "reference-smart-on-fhir-request-example.md")
