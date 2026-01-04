# Ingest network service descriptor (NSD) into AWS TNB network catalog

CSPs ingest the NSD, which describes the required compute and network resources, as
well as the NFs to be deployed, into the AWS TNB network catalog.

**Recommendation:** Design the NSD to be modular and
reusable, allowing for the creation of multiple network instances from a single template.
Leverage AWS TNB's support for ETSI SOL003/SOL005 APIs to integrate with existing ETSI-based
service orchestrators.

**Practical advice:** Thoroughly test the NSD in a
non-production environment to verify the correct mapping of resources and NFs. Maintain
version control of the NSD to enable updates and rollbacks.
