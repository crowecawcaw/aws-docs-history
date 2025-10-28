# Terminology used in data lake

The following terms are used in data lake:

- **Entity** – Information about a data object for each category.
  For example, company, geography, and trading_partner are entities for an organization. For more information, see [Data entities and columns used in AWS Supply Chain](data-model.md "data-model.md").
- **Dataset** – Information related to the entity. You can
  have only one dataset per entity.
- **Connector** – A way to import data into AWS Supply Chain.
- **Recipe** – A set of steps that describes how to map source data into one dataset.
- **Source Flows1** – Displays
  the datasets and fields that you uploaded.
- **Destination Flows1** – Associates the data from your dataset to the AWS Supply Chain data entities in data lake.
- **Source system1** – Your
  existing enterprise resource planning (ERP) system, Warehouse Management System
  (WMS), or any supply chain data management system.
  1 – These terms are only displayed when you ingest
  data through Amazon S3 (or the **Upload any CSV** option in the
  web application).
