# Filtering notifications with AWS HealthLake

Refine your notifications using standard FHIR search parameters in your `Subscription` criteria.

**Supported filters**

The following table shows a list of supported filter criteria that HealthLake supports for Subscriptions.

| Search parameter types | FHIR data type                                                                             | Modifiers                 | Supported prefixes                                   |
| ---------------------- | ------------------------------------------------------------------------------------------ | ------------------------- | ---------------------------------------------------- |
| String                 | string<br>HumanName<br>Address                                                             | exact, contains missing   |                                                      |
| Token                  | boolean<br>code<br>string<br>Coding<br>CodeableConcept<br>Identifier<br>ContactPoint<br>id | not, text, missing        |                                                      |
| Number                 | integer<br>decimal<br>positiveInt<br>unsignedInt                                           | missing                   | "eq", "ne", "gt", "lt", "ge", "le", "sa", "eb", "ap" |
| Date                   | date<br>dateTime<br>instant<br>Period<br>Timing                                            |                           | "eq", "ne", "gt", "lt", "ge", "le", "sa", "eb", "ap" |
| Quantity               | Quantity<br>Money<br>Range<br>SimpleQuantity                                               |                           | "eq", "ne", "gt", "lt", "ge", "le", "sa", "eb", "ap" |
| Reference              | Reference                                                                                  | missing, identifier, type |                                                      |
| URI                    | uri<br>url<br>canonical<br>uid<br>oid                                                      | missing                   |                                                      |

**Sample supported filters**

The following table shows samples of supported filter criteria that HealthLake supports for Subscriptions:

| Purpose                       | Filter criteria                                 | Description                                                               |
| ----------------------------- | ----------------------------------------------- | ------------------------------------------------------------------------- | ----------------------------------------------------------- |
| Patient-specific observations | `Observation?patient=Patient/[id]&status=final` | Get notifications when observations for a specific patient are finalized  |
| Patient-specific observations | `Patient?birthdate=gt2021`                      | Get notifications when patients born after 2021 are registered or updated |
| Patient-specific observations | `Condition?code=http://snomed.info/sct          | 39065001`                                                                 | Get notifications for conditions with specific SNOMED codes |
| Patient-specific observations | `Observation?code=http://loinc.org              | 8480-6&value-quantity=gt160`                                              | Get notifications for high systolic blood pressure readings |
