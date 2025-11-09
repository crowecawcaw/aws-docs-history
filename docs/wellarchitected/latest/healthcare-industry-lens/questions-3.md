# Questions

| HCL_OE1. Does your organization use master data management<br>processes to unambiguously identify patients or individuals and link clinical concepts and<br>measures to standard healthcare vocabularies (such as SNOMED, ICD, CPT, or<br>NDC)? |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                                                                                                                                                 |

Datasets should be cleansed, tracked, and versioned to maintain their quality. Use a
central Data Catalog to register and discover these datasets. Automate master data
management processes to reduce burden and improve adoption. Label sensitive datasets with
authorization enforced. Track licenses for applicable datasets. Standard healthcare
ontologies are preferred over proprietary to promote reuse and data sharing.

| HCL_OE2. Does your organization have a process for updating the<br>vocabularies used in master data management processes? |
| ------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                           |

Various public and private organizations maintain healthcare ontologies. The frequency
of publication and methods of distribution vary widely. New concepts are added to these
ontologies over time and others are deprecated. Automated processes for keeping the content
updated reduce manual error-prone efforts and improve data quality. The publication of new
content may be used to trigger this update process; otherwise, set up an automated schedule
aligned with the content owner.

| HCL_OE3. Are open data formats being used for health data? |
| ---------------------------------------------------------- |
|                                                            |

Health data lakes should store a copy of data in open standard formats (such as HL7,
DICOM, standard genomic files like Binary Alignment Map (BAM), Compressed Reference-oriented
Alignment Map (CRAM) and (g)VCF, XML, CSV, JSON, Parquet, or JPEG). Derivative copies of
data may use non-standard formats to support downstream analytics. Storing health data
in open formats expands the software that can be used to process the data, and may decrease
the data transformations needed for interoperability.

| HCL_SEC13. Does your organization employ role-based and<br>attribute-based access control, as well as fine-grained secure data access at the table,<br>column, or row level to ensure least privilege access? |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                                                                                                               |

Healthcare data access should follow least privilege. Access to the data should be
granted to only those individuals who need it. Maintaining this access is greatly simplified
using role-based and attribute-based mechanisms built on a common identity provider.
Likewise, revoke access when no longer needed. Control access to individual datasets, but
also verify that the user’s ability to combine datasets does not expose unintended risks.

| HCL_SEC14. Are comprehensive audit logs capturing all data access<br>(create, read, update, and delete) and show compliance with centrally defined<br>policies? |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                                                                 |

Audit logs for access to all protected information must be maintained in a central
immutable data store. Lock down permissions to audit logs. The logs must be maintained in
accordance with your regulatory compliance. The logs can be migrated to lower-cost storage
tiers automatically over time to reduce costs.

| HCL_SEC15. Is sensitive data (for example, PII or health data) being<br>deidentified or redacted when possible? |
| --------------------------------------------------------------------------------------------------------------- |
|                                                                                                                 |

Many healthcare analytics use cases don’t require personally identifiable information.
By deidentifying or redacting data, storing and accessing data becomes less risky. Use
irreversible de-identification mechanisms to scrub sensitive information if it’s not needed
by downstream consumers of the data.
