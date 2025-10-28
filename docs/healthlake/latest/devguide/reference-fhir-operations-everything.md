# Getting patient data with

`Patient/$everything`

The `Patient/$everything` operation is used to query a FHIR
`Patient` resource, along with any other resources related to that
`Patient`. The operation can be used to provide a patient with access to their
entire record or for a provider to perform a bulk data download related to a patient. HealthLake
supports `Patient/$everything` for a specific patient `id`.

`Patient/$everything` is a FHIR REST API operation that can be invoked as
shown in the examples below.

GET request

```
GET https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/Patient/`id`/$everything
```

###### Note

Resources in response are sorted by resource type and resource `id`.

Response is always populated with `Bundle.total`.

## `Patient/$everything`

parameters

HealthLake supports the following query parameters

| Parameter                   | Details                                                                                                         |
| --------------------------- | --------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| start                       | Get all `Patient` data after a specified start date.                                                            |
| end                         | Get all `Patient` data before a specified end date.                                                             |
| since                       | Get all `Patient` data updated after a specified date.                                                          |
| \_type                      | Get `Patient` data for specific resource types.                                                                 |
| \_count                     | Get `Patient` data and specify page size.                                                                       | ###### Example - Get all patient data after a specified start date `Patient/$everything` can use the `start` filter to query only data after a specific date. ``GET https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/Patient/`id`/$everything?start=2024-03-15T00:00:00.000Z`` ###### Example - Get all `Patient` data before a specified end date Patient $everything can use the `end` filter to only query data before a specific date. ``` GET https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/Patient/`id`/$everything?end=2024-03-15T00:00:00.000Z ``###### Example - Get all `Patient` data updated after a specified date `Patient/$everything` can use the `since` filter to query only data updated after a specific date.`` GET https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/Patient/`id`/$everything?since=2024-03-15T00:00:00.000Z ``###### Example - Get `Patient` data for specific resource types Patient $everything can use the `_type` filter to specify specific resource types to be included in the response. Multiple resource types can be specified in a comma separated list.`` GET https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/Patient/`id`/$everything?_type=Observation,Condition ``###### Example - Get `Patient` data and specify page size Patient $everything can use the `_count` to set the page size.`` GET https://healthlake.`region`.amazonaws.com/datastore/`datastoreId`/r4/Patient/`id`/$everything?_count=15 ```##`Patient/$everything`  `start`and`end`attributes HealthLake supports the following resource attributes for the`Patient/ $everything` `start`and`end` query parameters. |
| Resource                    | Resource Element                                                                                                |
| ---                         | ---                                                                                                             |
| Account                     | Account.servicePeriod.start                                                                                     |
| AdverseEvent                | AdverseEvent.date                                                                                               |
| AllergyIntolerance          | AllergyIntolerance.recordedDate                                                                                 |
| Appointment                 | Appointment.start                                                                                               |
| AppointmentResponse         | AppointmentResponse.start                                                                                       |
| AuditEvent                  | AuditEvent.period.start                                                                                         |
| Basic                       | Basic.created                                                                                                   |
| BodyStructure               | NO_DATE                                                                                                         |
| CarePlan                    | CarePlan.period.start                                                                                           |
| CareTeam                    | CareTeam.period.start                                                                                           |
| ChargeItem                  | ChargeItem.occurrenceDateTime, ChargeItem.occurrencePeriod.start, ChargeItem.occurrenceTiming.event             |
| Claim                       | Claim.billablePeriod.start                                                                                      |
| ClaimResponse               | ClaimResponse.created                                                                                           |
| ClinicalImpression          | ClinicalImpression.date                                                                                         |
| Communication               | Communication.sent                                                                                              |
| CommunicationRequest        | CommunicationRequest.occurrenceDateTime, CommunicationRequest.occurrencePeriod.start                            |
| Composition                 | Composition.date                                                                                                |
| Condition                   | Condition.recordedDate                                                                                          |
| Consent                     | Consent.dateTime                                                                                                |
| Coverage                    | Coverage.period.start                                                                                           |
| CoverageEligibilityRequest  | CoverageEligibilityRequest.created                                                                              |
| CoverageEligibilityResponse | CoverageEligibilityResponse.created                                                                             |
| DetectedIssue               | DetectedIssue.identified                                                                                        |
| DeviceRequest               | DeviceRequest.authoredOn                                                                                        |
| DeviceUseStatement          | DeviceUseStatement.recordedOn                                                                                   |
| DiagnosticReport            | DiagnosticReport.effective                                                                                      |
| DocumentManifest            | DocumentManifest.created                                                                                        |
| DocumentReference           | DocumentReference.context.period.start                                                                          |
| Encounter                   | Encounter.period.start                                                                                          |
| EnrollmentRequest           | EnrollmentRequest.created                                                                                       |
| EpisodeOfCare               | EpisodeOfCare.period.start                                                                                      |
| ExplanationOfBenefit        | ExplanationOfBenefit.billablePeriod.start                                                                       |
| FamilyMemberHistory         | NO_DATE                                                                                                         |
| Flag                        | Flag.period.start                                                                                               |
| Goal                        | Goal.statusDate                                                                                                 |
| Group                       | NO_DATE                                                                                                         |
| ImagingStudy                | ImagingStudy.started                                                                                            |
| Immunization                | Immunization.recorded                                                                                           |
| ImmunizationEvaluation      | ImmunizationEvaluation.date                                                                                     |
| ImmunizationRecommendation  | ImmunizationRecommendation.date                                                                                 |
| Invoice                     | Invoice.date                                                                                                    |
| List                        | List.date                                                                                                       |
| MeasureReport               | MeasureReport.period.start                                                                                      |
| Media                       | Media.issued                                                                                                    |
| MedicationAdministration    | MedicationAdministration.effective                                                                              |
| MedicationDispense          | MedicationDispense.whenPrepared                                                                                 |
| MedicationRequest           | MedicationRequest.authoredOn                                                                                    |
| MedicationStatement         | MedicationStatement.dateAsserted                                                                                |
| MolecularSequence           | NO_DATE                                                                                                         |
| NutritionOrder              | NutritionOrder.dateTime                                                                                         |
| Observation                 | Observation.effective                                                                                           |
| Patient                     | NO_DATE                                                                                                         |
| Person                      | NO_DATE                                                                                                         |
| Procedure                   | Procedure.performed                                                                                             |
| Provenance                  | Provenance.occurredPeriod.start, Provenance.occurredDateTime                                                    |
| QuestionnaireResponse       | QuestionnaireResponse.authored                                                                                  |
| RelatedPerson               | NO_DATE                                                                                                         |
| RequestGroup                | RequestGroup.authoredOn                                                                                         |
| ResearchSubject             | ResearchSubject.period                                                                                          |
| RiskAssessment              | RiskAssessment.occurrenceDateTime, RiskAssessment.occurrencePeriod.start                                        |
| Schedule                    | Schedule.planningHorizon                                                                                        |
| ServiceRequest              | ServiceRequest.authoredOn                                                                                       |
| Specimen                    | Specimen.receivedTime                                                                                           |
| SupplyDelivery              | SupplyDelivery.occurrenceDateTime, SupplyDelivery.occurrencePeriod.start, SupplyDelivery.occurrenceTiming.event |
| SupplyRequest               | SupplyRequest.authoredOn                                                                                        |
| VisionPrescription          | VisionPrescription.dateWritten                                                                                  |
