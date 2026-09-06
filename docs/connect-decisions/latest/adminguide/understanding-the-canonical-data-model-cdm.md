

# Understanding the Canonical Data Model (CDM)
<a name="understanding-the-canonical-data-model-cdm"></a>

The Canonical Data Model (CDM) is the standardized data structure used by . When you onboard your supply chain data, it must be transformed into CDM format so that can process it for planning, forecasting, and operational insights.

This topic explains what the CDM is, why it matters, and which data entities are available.

## What is the CDM?
<a name="cdm-what-is"></a>

The CDM defines a common set of data entities and fields that represent supply chain concepts such as products, sites, orders, shipments, and inventory. Regardless of the format or structure of your source data, the CDM provides a single, consistent schema that uses across all of its features.

During data onboarding, your source data is mapped to CDM destination tables. The Data Agent can automatically suggest mappings between your source fields and CDM fields, and generate SQL transformation queries to convert your data.

## Why the CDM matters
<a name="cdm-why-it-matters"></a>
+ **Consistency** — All features in operate on the same data structure, ensuring uniform behavior across demand planning, inventory optimization, and lead time insights.
+ **Interoperability** — Data from different source systems (ERP, WMS, TMS) is normalized into a single model, enabling cross-system analysis.
+ **Simplified onboarding** — The Data Agent uses the CDM as the target schema when generating automated mappings, reducing manual effort.
+ **Data quality** — Validation checks run against CDM definitions to catch issues before data is used in production.

## Data entity categories
<a name="cdm-data-entity-categories"></a>

CDM data entities fall into two categories:
+ **Non-transactional data** — Reference or master data that changes infrequently, such as products, sites, trading partners, and geographies.
+ **Transactional data** — Operational data that changes frequently, such as forecasts, inventory levels, orders, and shipments.

## Supported data entities
<a name="cdm-supported-data-entities"></a>

The following table lists all data entities supported in the CDM.


**Supported CDM data entities**  

| Data entity | Type of data | Required | 
| --- | --- | --- | 
| Company | Non-transactional data | Yes | 
| Product | Non-transactional data | Yes | 
| Trading partner | Non-transactional data | Yes | 
| Vendor product | Non-transactional data | Yes | 
| Geography | Non-transactional data | Yes | 
| Product hierarchy | Non-transactional data | Yes | 
| Transportation lane | Non-transactional data | Yes | 
| Vendor lead time | Non-transactional data | Yes | 
| Site | Non-transactional data | Yes | 
| Vendor holiday | Non-transactional data | Yes | 
| Forecast | Transactional data | Yes | 
| Inventory | Transactional data | Yes | 
| Inbound order (PO/STO) | Transactional data | Yes | 
| Outbound order line | Transactional data | Yes | 
| Shipment | Transactional data | Yes | 
| Inventory policy | Transactional data | Yes | 
| Inbound order line (PO/STO) | Transactional data | Yes | 
| Outbound shipment | Transactional data | Yes | 
| Inbound order line schedule | Transactional data | Yes | 

## Entities required by feature
<a name="cdm-entities-required-by-feature"></a>

Not every feature in requires all CDM entities. The following sections describe which entities are required, optional, or not applicable for each feature.

### Inventory visibility
<a name="cdm-feature-inventory-visibility"></a>


**CDM entities for inventory visibility**  

| Data entity | Type of data | Required | 
| --- | --- | --- | 
| Company | Non-transactional | Optional | 
| Product | Non-transactional | Yes | 
| Trading partner | Non-transactional | Optional | 
| Vendor product | Non-transactional | Not applicable | 
| Geography | Non-transactional | Optional | 
| Product hierarchy | Non-transactional | Optional | 
| Transportation lane | Non-transactional | Optional | 
| Vendor lead time | Non-transactional | Not applicable | 
| Site | Non-transactional | Yes | 
| Vendor holiday | Non-transactional | Not applicable | 
| Forecast | Transactional | Optional | 
| Inventory | Transactional | Yes | 
| Inbound order (PO/STO) | Transactional | Optional | 
| Outbound order line | Transactional | Optional | 
| Shipment | Transactional | Optional | 
| Inventory policy | Transactional | Yes | 
| Inbound order line | Transactional | Optional | 
| Outbound shipment | Transactional | Optional | 
| Inbound order line schedule | Transactional | Optional | 

### Lead time insights
<a name="cdm-feature-lead-time-insights"></a>


**CDM entities for lead time insights**  

| Data entity | Type of data | Required | 
| --- | --- | --- | 
| Company | Non-transactional | Optional | 
| Product | Non-transactional | Yes | 
| Trading partner | Non-transactional | Yes | 
| Vendor product | Non-transactional | Yes | 
| Geography | Non-transactional | Optional | 
| Product hierarchy | Non-transactional | Optional | 
| Transportation lane | Non-transactional | Yes | 
| Vendor lead time | Non-transactional | Yes | 
| Site | Non-transactional | Yes | 
| Vendor holiday | Non-transactional | Optional | 
| Forecast | Transactional | Not applicable | 
| Inventory | Transactional | Not applicable | 
| Inbound order (PO/STO) | Transactional | Yes | 
| Outbound order line | Transactional | Not applicable | 
| Shipment | Transactional | Yes | 
| Inventory policy | Transactional | Not applicable | 
| Inbound order line | Transactional | Yes | 
| Outbound shipment | Transactional | Not applicable | 
| Inbound order line schedule | Transactional | Yes | 

### Demand planning
<a name="cdm-feature-demand-planning"></a>


**CDM entities for demand planning**  

| Data entity | Type of data | Required | 
| --- | --- | --- | 
| Company | Non-transactional | Optional | 
| Product | Non-transactional | Yes | 
| Trading partner | Non-transactional | Not applicable | 
| Vendor product | Non-transactional | Not applicable | 
| Geography | Non-transactional | Optional | 
| Product hierarchy | Non-transactional | Optional | 
| Transportation lane | Non-transactional | Not applicable | 
| Vendor lead time | Non-transactional | Not applicable | 
| Site | Non-transactional | Yes | 
| Vendor holiday | Non-transactional | Not applicable | 
| Forecast | Transactional | Not applicable | 
| Inventory | Transactional | Not applicable | 
| Inbound order (PO/STO) | Transactional | Not applicable | 
| Outbound order line | Transactional | Yes | 
| Shipment | Transactional | Not applicable | 
| Inventory policy | Transactional | Not applicable | 
| Inbound order line | Transactional | Not applicable | 
| Outbound shipment | Transactional | Not applicable | 
| Inbound order line schedule | Transactional | Not applicable | 

## How the CDM relates to data onboarding
<a name="cdm-relates-to-data-onboarding"></a>

When you onboard data into , the process follows these steps:

1. **Upload** — You upload your source data as CSV files to Amazon S3.

1. **Map** — The Data Agent analyzes your source datasets and suggests which CDM destination tables best match your data.

1. **Transform** — SQL transformation queries convert your source data format into CDM format.

1. **Validate** — Quality checks run against the transformed data to verify it conforms to CDM requirements.

1. **Activate** — Once validated, the data flows into and becomes available for features.

For step-by-step instructions on onboarding your data, see the Data Onboarding topic.