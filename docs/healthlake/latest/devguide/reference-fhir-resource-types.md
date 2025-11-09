# FHIR R4 supported resource types for HealthLake

The following table lists the FHIR R4 resource types supported by AWS HealthLake. For more information,
see [Resource Index](https://hl7.org/fhir/R4/resourcelist.html "https://hl7.org/fhir/R4/resourcelist.html") in the
**FHIR R4 documentation**.

FHIR R4 resource types supported by HealthLake| Account | DetectedIssue | Invoice | Practitioner |
| ActivityDefinition | Device | Library | PractitionerRole |
| AdverseEvent | DeviceDefinition | Linkage | Procedure |
| AllergyIntolerance | DeviceMetric | List | Provenance |
| Appointment | DeviceUseStatement | Location | Questionnaire |
| AppointmentResponse | DeviceRequest | Measure | QuestionnaireResponse |
| AuditEvent<br>• _See Note_ | DiagnosticReport | MeasureReport | RelatedPerson |
| Binary | DocumentManifest | Media | RequestGroup |
| BodyStructure | DocumentReference | Medication | ResearchStudy |
| Bundle<br>• _See Note_ | EffectEvidenceSynthesis | MedicationAdministration | ResearchSubject |
| CapabilityStatement | Encounter | MedicationDispense | RiskAssessment |
| CarePlan | Endpoint | MedicationKnowledge | RiskEvidenceSynthesis |
| CareTeam | EpisodeOfCare | MedicationRequest | Schedule |
| ChargeItem | EnrollmentRequest | MedicationStatement | ServiceRequest |
| ChargeItemDefinition | EnrollmentResponse | MessageHeader | Slot |
| Claim | ExplanationOfBenefit | MolecularSequence | Specimen |
| ClaimResponse | FamilyMemberHistory | NutritionOrder | StructureDefinition |
| Communication | Flag | Observation | StructureMap |
| CommunicationRequest | Goal | OperationOutcome<br>• _See Note_ | Substance |
| Composition | Group | Organization | SupplyDelivery |
| ConceptMap | GuidanceResponse | OrganizationAffiliation | SupplyRequest |
| Condition | HealthcareService | Parameters<br>• _See Note_ | Task |
| Consent | ImagingStudy | Patient | ValueSet |
| Contract | Immunization | PaymentNotice | VisionPrescription |
| Coverage | ImmunizationEvaluation | PaymentReconciliation | VerificationResult<br>• _See Note_ |
| CoverageEligibilityRequest | ImmunizationRecommendation | Person | |
| CoverageEligibilityResponse | InsurancePlan | PlanDefinition | |

###### FHIR specifications and HealthLake

- You cannot make `GET` or `POST` requests with FHIR `OperationOutcome` and `Parameters` resource types.
- **AuditEvent** — An AuditEvent resource can be created or read, but it cannot be updated or deleted.
- **Bundle** — There are multiple ways HealthLake manages Bundle requests. For more details, see [Bundling FHIR resources](managing-fhir-resources-bundle.md "managing-fhir-resources-bundle.md").
- **VerificationResult** — This resource type is only supported for data stores created after December 09, 2023.
