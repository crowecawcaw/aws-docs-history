# Security Hub and the Open Cybersecurity Findings Format (OCSF)

## OCSF overview

Security Hub findings are formatted using OCSF which is an open-source project, delivering an extensible framework for developing schemas, along with a vendor-agnostic core security schema.
Vendors and other data producers can adopt and extend the schema for their specific domains.
Data producers can map differing schemas to help security teams simplify data ingestion and normalization, so that data scientists and analysts can work with a common language for threat detection and investigation.
The goal is to provide an open standard, adopted in any environment, application, or solution, while complementing existing security standards and processes.

The framework is made up of a set of data types, an attribute dictionary, and the taxonomy.
It is not restricted to the cybersecurity domain nor to events, however the initial focus of the framework has been a schema for cybersecurity events.
OCSF is agnostic to storage format, data collection and Extract-Transform-Load (ETL) processes.
The core schema for cybersecurity events is intended to be agnostic to implementations.
The schema framework definition files and the resulting normative schema are written as JSON.

Security Hub currently supports findings in OCSF schema version 1.6.

## Related Resources

For more information about OCSF and its implementation, see the following resources:

- [Public OCSF Documentation](https://schema.ocsf.io/ "https://schema.ocsf.io/")
- [OCSF Extension Usage Documentation](https://schema.ocsf.io/1.0.0/extensions/ "https://schema.ocsf.io/1.0.0/extensions/")
- [OCSF Core Schema Reference](https://schema.ocsf.io/1.0.0/ "https://schema.ocsf.io/1.0.0/")
- [OCSF Extensions Registry](https://github.com/ocsf/ocsf-schema/tree/main/extensions "https://github.com/ocsf/ocsf-schema/tree/main/extensions")
