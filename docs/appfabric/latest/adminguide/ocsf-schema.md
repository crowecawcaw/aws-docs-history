# Open Cybersecurity Schema Framework for AWS AppFabric

The [Open Cybersecurity Schema Framework](https://schema.ocsf.io/ "https://schema.ocsf.io/")
(OCSF) is a collaborative, open-source effort by AWS and leading
partners
in the cybersecurity industry. OCSF provides a standard schema for common security events,
defines versioning criteria to facilitate schema evolution, and includes a self-governance
process for security log producers and consumers. The public source code for OCSF is hosted
on [GitHub](https://github.com/ocsf/ocsf-schema "https://github.com/ocsf/ocsf-schema").

## OCSF-based schema in AppFabric

The AWS AppFabric for security
[OCSF 1.1](https://schema.ocsf.io/1.1.0/ "https://schema.ocsf.io/1.1.0/") based schema is tailored
specifically to address your needs for normalized, consistent, low-effort observability
of their software as a service (SaaS) portfolio. AppFabric determines the right mapping for each field and events. AppFabric, in collaboration with the OCSF
open source community, introduced new OCSF event categories, event classes, activities,
and objects so that OCSF is applicable to SaaS application events. AppFabric automatically
normalizes audit events that it receives from SaaS applications and delivers this data
to the Amazon Simple Storage Service (Amazon S3) or Amazon Data Firehose services in your AWS account. For an Amazon S3
destination, you can choose between two normalization options (OCSF or Raw) and two data
format options (JSON or Parquet). When delivering to Firehose, you can also
choose between two normalization options (OCSF or Raw) but the data format is limited to
JSON.
