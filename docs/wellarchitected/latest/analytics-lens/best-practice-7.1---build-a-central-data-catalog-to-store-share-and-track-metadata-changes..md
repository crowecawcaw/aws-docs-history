# Best practice 7.1 – Build a central Data Catalog to store, share, and track metadata changes

Building a central Data Catalog to store, share, and manage metadata across the organization is an integral part of data governance. This will promote standardization and reuse. Tracing metadata change history in the central Data Catalog helps you manage and control version changes in the metadata. A Data Catalog is often required for auditing and compliance but by incorporating business context to a Data Catalog, it allows users in the organization to discover data assets using business terms rather than technical naming conventions.

## Suggestion 7.1.1 – Changes on the metadata in the Data Catalog should be controlled and versioned

Use the Data Catalog change tracking features. For example, when the schema
changes, AWS Glue Data Catalog will track the version change. You can use AWS Glue to compare
schema versions, if needed. In addition, we recommend a change control process that only
allows those authorized to make schema changes in your Data Catalog. The AWS Glue Schema registry allows you to centrally discover and control data schemas. You can create a schema contract between producers and consumers to improve data consumer awareness to data format changes.

## Suggestion 7.1.2 – Capture and publish business metadata of your data assets

Capturing business metadata and publishing it with metadata assets is essential for data consumers and data stewards alike. Metadata such as regulatory compliance statuses, data classification, and other important data governance characteristics, guides consumers on how to best process the data and informs data governance processes conducted by data stewards. Establishing a business glossary across the organization creates a collection of business terms that can be associated with the data assets. This ensures that business definitions are common across the organization.

For more details, see AWS Data Zone: [Governed Analytics](https://aws.amazon.com/datazone/ "https://aws.amazon.com/datazone/").
