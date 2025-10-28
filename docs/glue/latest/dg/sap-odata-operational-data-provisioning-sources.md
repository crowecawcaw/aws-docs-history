# Operational Data Provisioning (ODP) Sources

Operational Data Provisioning (ODP) provides a technical infrastructure that you can use to support data extraction and replication for various target applications and supports delta mechanisms in these scenarios. In case of a delta procedure, the data from a source (ODP Provider) is automatically written to a delta queue (Operational Delta Queue – ODQ) using an update process or passed to the delta queue using an extractor interface. An ODP Provider can be a DataSource (extractors), ABAP Core Data Services Views (ABAP CDS Views), SAP BW or SAP BW/4HANA, SAP Landscape Transformation Replication Server (SLT), and SAP HANA Information Views (calculation views). The target applications (referred to as ODQ 'subscribers' or more generally “ODP Consumers”) retrieve the data from the delta queue and continue processing the data.

## Full Load

In the context of SAP OData and ODP entities, a **Full Load** refers to the process of extracting all available data from an ODP entity in a single operation. This operation retrieves the complete dataset from the source system, ensuring that the target system has a comprehensive and up-to-date copy of the entity's data.
Full loads are typically used for sources that do not support incremental loads or when a refresh of the target system is required.

**Example**

You can explicitly set the `ENABLE_CDC` flag to false, when creating the DynamicFrame. Note: `ENABLE_CDC` is false by default, if you don’t want to initialize the delta queue, you don’t have to send this flag or set it to true. Not setting this flag to true will result in a full load extraction.

```
sapodata_df = glueContext.create_dynamic_frame.from_options(
    connection_type="SAPOData",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "entityName",
        "ENABLE_CDC": "false"
    }, transformation_ctx=key)
```

## Incremental Load

An **incremental load** in the context of ODP (Operational Data Provisioning) entities involves extracting only the new or changed data (deltas) from the source system since the last data extraction, avoiding preprocessing the already processed records. This approach significantly improves efficiency, reduces data transfer volumes, enhances performance, ensures efficient synchronization between systems, and minimizes processing time, especially for large datasets that change frequently.
