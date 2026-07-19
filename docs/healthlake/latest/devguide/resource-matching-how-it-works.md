# How resource matching works

Whenever a resource is written to your data store – through a bulk import job or a
REST API `create`, `update` or `delete`, resource matching
evaluates its `identifier` values against the other resources of the same type in
the data store. Matching is deterministic: two resources are linked when they share a
high-confidence healthcare identifier, and each identifier is matched according to its
real-world scope.

- **Globally unique identifiers** – an
  identifier such as a National Provider Identifier (NPI) or Social Security Number
  (SSN) refers to the same entity regardless of which system issued the record. These
  are matched on value.
- **Scoped identifiers** – an identifier such as
  a medical record number (MRN), driver's license, or device serial number is only
  unique within a namespace (a hospital, a state, a manufacturer). These are matched on
  the combination of the identifying system and value, so that MRN `456` at
  one hospital is never linked to MRN `456` at another.
  Resource matching also recognizes when the same identifier is represented under different
  system URIs. For example, an SSN under `http://hl7.org/fhir/sid/us-ssn` and under
  `urn:oid:2.16.840.1.113883.4.1` are treated as the same identifier, so
  resources from sources that use different URI conventions still match.

Resource matching does not apply priority ordering or conflict resolution between
identifiers: any shared, non-placeholder identifier is enough to link two resources. Because
matching is non-destructive, you review the resulting links and decide how to act on
them.

###### Note

Resource matching evaluates resources of the same type against one another (for
example, `Patient` to `Patient`). It does not link resources of
different types.

###### Note

A resource sharing an identifier with more than 100 other resources may not be matched
against all of them.
