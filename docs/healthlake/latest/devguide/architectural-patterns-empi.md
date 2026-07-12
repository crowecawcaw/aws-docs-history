# Integrating AWS HealthLake with an Enterprise Master Patient Index (EMPI)

If your organization already operates a third-party Enterprise Master Patient Index
(EMPI), you can integrate it with AWS HealthLake by resolving patient identities
upstream—before data is ingested.

In this pattern, your EMPI assigns a master patient identifier and tags each FHIR
resource (for example, Patient, Encounter, Observation) with that identifier in the
`Patient.identifier` field or through consistent resource references
(`subject.identifier`) prior to writing them into HealthLake. This ensures that
all clinical data arriving in your FHIR data store is pre-linked to a single,
authoritative patient identity. HealthLake stores and serves the already-reconciled
resources.

HealthLake is a standards-based FHIR R4 data store, so any EMPI that produces
FHIR-formatted identifiers and references is compatible with this approach.

## Cloud-native patient resolution with AWS Entity Resolution

For organizations that do not yet have an EMPI or want to build a cloud-native
solution, AWS provides a purpose-built path using [AWS
Entity Resolution](../../../entityresolution/latest/userguide/what-is-service.md "../../../entityresolution/latest/userguide/what-is-service.md") in conjunction with HealthLake.

The
[Guidance
for Patient Entity Resolution with AWS HealthLake](https://aws.amazon.com/solutions/guidance/patient-entity-resolution-with-aws-healthlake/ "https://aws.amazon.com/solutions/guidance/patient-entity-resolution-with-aws-healthlake/") demonstrates how to use machine
learning–based matching rules to identify, match, and link disparate patient
records across multiple data sources. This produces unified patient profiles with
confidence scores.

This architecture uses AWS Step Functions, Lambda, AWS Glue, Amazon Athena, and
Amazon S3 to orchestrate the resolution workflow, and writes the resulting linkages back
into HealthLake. You retain full control over how your FHIR data is
organized—you decide the matching thresholds, linking strategies, and whether
resolved identities are expressed as merged records or linked references.

## FHIR-native patient identity mechanisms

The FHIR specification offers native mechanisms for patient identity management
that HealthLake supports.

- **Patient.link** – Enables you to
  assert relationships between duplicate or distributed patient records using
  link types such as `replaced-by`, `replaces`,
  `refer`, or `seealso`.
- **$member-match operation** – Allows
 payer organizations to find a member's unique identifier across different
 healthcare systems using demographic and coverage information. This is a key
 capability for payer-to-payer data exchange under CMS interoperability
 rules. For more information, see
 [$member-match operation for HealthLake](reference-fhir-operations-member-match.md "reference-fhir-operations-member-match.md").
- **Person resource** – Serves as a
  cross-resource identity anchor, linking Patient, Practitioner, and
  RelatedPerson records that represent the same individual. This pattern is
  commonly used in regional or national patient index registries.

You can use these FHIR-native patterns independently or in combination with an
external EMPI or AWS Entity Resolution. This gives you flexibility to choose the
identity management strategy that best fits your organization's governance and
interoperability requirements.
