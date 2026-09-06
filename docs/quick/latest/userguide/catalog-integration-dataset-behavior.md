

# Behavior of created datasets
<a name="catalog-integration-dataset-behavior"></a>

Datasets created through the agentic catalog experience have the following characteristics:
+ **Semantics inherited indicator** – Created datasets display a **Semantics inherited** badge to show that definitions come from the upstream catalog.
+ **DirectQuery** – All datasets use DirectQuery mode by default. Data is always queried at the source with no duplication.
+ **Sync semantics** – Choose **Sync semantics** on a dataset to refresh table and column definitions from the upstream catalog at any time. This ensures the catalog remains the single source of truth for metadata.
+ **Flexibility** – You can edit these datasets to switch to SPICE or add transformations in Quick. However, after you do so, semantic sync is no longer available and the dataset is treated as a standard Quick dataset.

**Note**  
In this preview, Quick inherits table and column descriptions, and primary and foreign key definitions. Support for additional semantic information such as metric views and semantic views is planned for the future.