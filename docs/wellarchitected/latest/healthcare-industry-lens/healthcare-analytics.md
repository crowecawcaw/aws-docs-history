# Healthcare analytics

Healthcare delivery systems, payors, and service providers use
analytics for a range of purposes, such as revenue cycle
management, quality management, and process improvement. These
entities generate, analyze, and exchange large volumes of data.
The health data processed spans a diverse set of domains,
including clinical, finance, supply chain, human resources,
research and more. The volume and variety of data processed by
analytics is steadily increasing, making extensible, elastic,
cloud-based architectures increasingly attractive.

Healthcare analytics architectures have the following
characteristics:

- Source data is ingested from upstream sources such as EHRs
  using bulk and streaming protocols. The raw data is oftentimes
  persisted for data lineage and reprocessing. For example, raw
  HL7 v2 messages, EDI transactions for claims, genomic variant
  data, medical images, faxed or scanned documents, and so on
  are ingested and stored for downstream processing, oftentimes
  for multiple, disparate use-cases (such as input data for
  AI/ML inferencing, dashboards, forecasting, and sharing).
- Data transformations create derived datasets by applying
  structural and semantic transforms and linking data from
  different tables, systems, or domains. During this process,
  the data can be mapped to standard clinical terminologies
  (such as SNOMED, ICD, CPT, and NDC) to provide consistency for
  downstream consumers of the data. Transformation jobs may
  include machine learning steps such as OCR of scanned or faxed
  documents, transcription of voice recording, or natural
  language processing of clinical text. Additionally, these
  transformations may include steps to reduce the fidelity of
  the data for specific use cases, such as generating
  de-identified or limited datasets for research use cases.
- Business logic runs on the derived data to generate actionable
  insights. Late binding approaches for the data schema enable a
  more agile approach and avoids large, upfront investments in
  heavy ETL. Results are sent to one or more purpose-built data
  stores.
- Various stakeholders consume the data to glean insights. Data
  consumers are often diverse, ranging from non-technical
  reviewers of business intelligence dashboards, to researchers
  running deep learning algorithms.
- Data remains encrypted at-rest and in-transit throughout the
  entire process. Identity and access controls are enforced so
  that access to sensitive health data is limited appropriately.
  All data assets can be recorded in a centralized Data Catalog
  to promote data discovery and reuse.
