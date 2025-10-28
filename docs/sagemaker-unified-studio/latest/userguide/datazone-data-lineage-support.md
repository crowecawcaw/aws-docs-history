# Data lineage support

In Amazon SageMaker Unified Studio, domain administrators or data users can configure lineage in
projects while setting up connections for data lake and data warehouse sources to
ensure the data source runs created from those resources are enabled for automatic
lineage capture. Data lineage is automatically captured from data sources, such as
AWS Glue and Amazon Redshift, as well as from tools, such as Visual ETL and
notebooks, as executions create, update, or transform data. Additionally, Amazon SageMaker Unified Studio
captures the movement of data within the catalog as producers bring their asset into
inventory, and publish them, as well as when consumers subscribe and get access, to
indicate who the subscribing projects are for a given asset. With this automation,
different stages of an asset in the catalog are captured including when schema
changes are detected.

Using Amazon SageMaker Unified Studio's OpenLineage-compatible APIs, domain administrators and data
producers can capture and store lineage events beyond what is available in
Amazon SageMaker Unified Studio, including transformations in Amazon S3, AWS Glue, and other services. This
provides a comprehensive view for the data consumers and helps them gain confidence
of the asset's origin, while data producers can assess the impact of changes to an
asset by understanding its usage. Additionally, Amazon SageMaker Unified Studio versions lineage with each
event, enabling users to visualize lineage at any point in time or compare
transformations across an asset's or job's history. This historical lineage provides
a deeper understanding of how data has evolved, essential for troubleshooting,
auditing, and ensuring the integrity of data assets.

With data lineage, you can accomplish the following in Amazon SageMaker Unified Studio:

- Understand the provenance of data: knowing where the data originated
  fosters trust in data by providing you with a clear understanding of its
  origins, dependencies, and transformations. This transparency helps in
  making confident data-driven decisions.
- Understand the impact of changes to data pipelines: when changes are made
  to data pipelines, lineage can be used to identify all of the downstream
  consumers that are to be affected. This helps to ensure that changes are
  made without disrupting critical data flows.
- Identify the root cause of data quality issues: if a data quality issue is
  detected in a downstream report, lineage, especially column-level lineage,
  can be used to trace the data back (at a column level) to identify the issue
  back to its source. This can help data engineers to identify and fix the
  problem.
- Improve data governance and compliance: column-level lineage can be used
  to demonstrate compliance with data governance and privacy regulations. For
  example, column-level lineage can be used to show where sensitive data (such
  as PII) is stored and how it is processed in downstream activities.
  **OpenLineage custom transport to send lineage events to
  SageMaker**

OpenLineage events which contain metadata about data pipelines, jobs, and runs,
are typically sent to backend for storage and analysis. The transport mechanism
handles this transmission. As an extension of the OpenLineage project, a custom
transport is available to send lineage events directly Amazon SageMaker Unified Studio's endpoint. The
custom transport was merged into OpenLineage version 1.33.0 ([https://openlineage.io/docs/releases/1_33_0/](https://openlineage.io/docs/releases/1_33_0/ "https://openlineage.io/docs/releases/1_33_0/")). This allows the use of
OpenLineage plugins with the transport to send lineage events collected directly to
Amazon SageMaker Unified Studio.
