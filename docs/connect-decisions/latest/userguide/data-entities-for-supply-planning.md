# Data Entities for Supply Planning

The following table lists the data entities and columns used by Supply Planning.

## How to read the table:

- **Required** – The entity or columns in the data entity are mandatory for the supply planning engine to function correctly.
- **Conditionally required** – The entity or columns in the data entity are required depending on the specific major functional requirements, policy type, order type, or sourcing rule type selected.
- **Optional** – The entity or columns in the data entity is optional. For enhanced planning accuracy and feature output, it is recommended to add the column with values.

## site (required)

How is this data entity used? Supply Planning uses the site data to define the physical locations (plants, warehouses, and distribution centers) within the supply chain network. Sites serve as the origin and destination nodes for transportation lanes, sourcing rules, and inventory policies.

| Column         | Requirement | Supply Planning usage                                                                                                                                                                                               |
| -------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id             | Required    | Unique identifier for the physical site (plant, warehouse, or distribution center) within the supply chain network. Make sure the column values do not have invalid characters such as asterisk and double-quotes.  |
| description    | Optional    | Human-readable name or label for the site.                                                                                                                                                                          |
| geo\_id        | Optional    | Foreign key linking this site to its geographic location in the Geography table.                                                                                                                                    |
| is\_active     | Optional    | Boolean flag indicating whether the site is currently operational and available for planning. By default, the site is considered as Active.                                                                         |
| open\_date     | Optional    | Calendar date on which the site became or will become operationally active. Used by the planning engine to exclude future sites from current plans while incorporating them into forward-looking network scenarios. |
| end\_date      | Optional    | Calendar date on which the site was or will be decommissioned and removed from active planning. After this date, the planning engine will no longer route demand to or hold inventory at this site.                 |
| site\_level\_1 | Optional    | The highest level in the site hierarchy, typically representing the broadest geographic or organizational grouping. This denormalized field enables efficient filtering and sorting across the site hierarchy.      |
| site\_level\_2 | Optional    | The second level in the site hierarchy, representing a regional subdivision within the top-level site grouping. Leave blank if your site hierarchy has fewer than 2 levels.                                         |
| site\_level\_3 | Optional    | The third level in the site hierarchy, representing a more granular geographic or organizational classification within level 2. Leave blank if your site hierarchy has fewer than 3 levels.                         |
| site\_level\_4 | Optional    | The fourth level in the site hierarchy, representing a specific site cluster or sub-region within level 3. Leave blank if your site hierarchy has fewer than 4 levels.                                              |
| site\_level\_5 | Optional    | The fifth and most granular level in the site hierarchy. Leave blank if your site hierarchy has fewer than 5 levels.                                                                                                |

## product (required)

How is this data entity used? Supply Planning uses the product data to identify and classify all items being planned. Product attributes are used to establish hierarchy filters for supply plan review, link products to inventory policies and sourcing rules, and support multi-level product segmentation.

| Column             | Requirement | Supply Planning usage                                                                                                                                                                                       |
| ------------------ | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id                 | Required    | Unique identifier for the product/material (SKU-level). Make sure the column values do not have duplicate IDs and special characters such as asterisk and double-quotes.                                    |
| description        | Required    | Human-readable name or description of the product.                                                                                                                                                          |
| product\_group\_id | Optional    | Foreign key linking the product to its category in the Product Hierarchy table.                                                                                                                             |
| unit\_cost         | Optional    | Standard cost per unit used for inventory valuation and cost planning.                                                                                                                                      |
| unit\_price        | Optional    | Unit Price or standard price or MSRP of product.                                                                                                                                                            |
| base\_uom          | Optional    | Unit of measure for product. Default to Eaches. Currently supply planning only supports Eaches.                                                                                                             |
| volume\_uom        | Optional    | Product volume. Currently volume\_uom has be the same across all products.                                                                                                                                  |
| unit\_volume       | Optional    | Volume of product per volum\_uom defined at the warehouse level.                                                                                                                                            |
| is\_deleted        | Optional    | Boolean flag indicating whether the product has been discontinued or marked inactive. By default, the product is considered as Active or Not deleted.                                                       |
| product\_level\_1  | Optional    | The highest level in the product hierarchy, typically representing the broadest product category or division. This denormalized field enables efficient filtering and sorting across the product hierarchy. |
| product\_level\_2  | Optional    | The second level in the product hierarchy, representing a subcategory within the top-level product category. Leave blank if your product hierarchy has fewer than 2 levels.                                 |
| product\_level\_3  | Optional    | The third level in the product hierarchy, representing a more granular product classification within level 2. Leave blank if your product hierarchy has fewer than 3 levels.                                |
| product\_level\_4  | Optional    | The fourth level in the product hierarchy, representing a specific product family or sub-classification within level 3. Leave blank if your product hierarchy has fewer than 4 levels.                      |
| product\_level\_5  | Optional    | The fifth and most granular level in the product hierarchy. Leave blank if your product hierarchy has fewer than 5 levels.                                                                                  |

## product\_hierarchy (optional)

How is this data entity used? Supply Planning uses product hierarchy data to organize products into structured category trees. This enables multi-level filtering and aggregated analysis of supply plans, and allows sourcing rules and inventory policies to be applied at a group level rather than individual SKU level.

| Column                     | Requirement | Supply Planning usage                                                                                   |
| -------------------------- | ----------- | ------------------------------------------------------------------------------------------------------- |
| id                         | Required    | Unique identifier for the product group/category level.                                                 |
| description                | Optional    | Name or label of the product group/category.                                                            |
| parent\_product\_group\_id | Optional    | Foreign key to the parent category, forming the hierarchical tree structure for product classification. |

## geography (optional)

How is this data entity used? Supply Planning uses geography data to establish hierarchical location classifications for sites. Geographic entities enable regional rollup analysis and allow lead times and inventory policies to be defined at geographic region granularity.

| Column          | Requirement | Supply Planning usage                                                                                |
| --------------- | ----------- | ---------------------------------------------------------------------------------------------------- |
| id              | Required    | Unique identifier for the geographic entity (city, state, country, region).                          |
| description     | Optional    | Name of the geographic location (e.g., city name, region name).                                      |
| parent\_geo\_id | Optional    | Foreign key to the parent geography, enabling hierarchical rollups (e.g., city to state to country). |

## transportation\_lane (conditional required)

How is this data entity used? Supply Planning uses transportation lane data to model the physical routes between origin and destination sites in the network. This data defines transit times and validity windows that the planning engine uses to schedule inbound and outbound shipments accurately.

| Column             | Requirement | Supply Planning usage                                                                                                   |
| ------------------ | ----------- | ----------------------------------------------------------------------------------------------------------------------- |
| id                 | Required    | Unique identifier for the transportation lane, typically a composite of origin, destination, product group, and vendor. |
| from\_site\_id     | Required    | Origin site (supplier warehouse or manufacturing plant) from which goods are shipped.                                   |
| to\_site\_id       | Required    | Destination site (receiving warehouse or plant) where goods are delivered.                                              |
| product\_group\_id | Optional    | Product category this lane applies to, enabling lane-level filtering by product group.                                  |
| product\_id        | Optional    | Specific product this lane applies to, for product-level lane definitions.                                              |
| transit\_time      | Required    | Number of days required to transport goods from origin to destination. Default is 0.                                    |
| eff\_start\_date   | Required    | Date from which this transportation lane becomes active/valid.                                                          |
| eff\_end\_date     | Required    | Date after which this transportation lane is no longer valid.                                                           |

## trading\_partner (conditional required)

How is this data entity used? Supply Planning uses trading partner data to identify vendors, suppliers, customers, and carriers in the supply chain. Trading partners are referenced by sourcing rules, inbound order lines, and vendor lead times to associate supply activities with external business entities.

| Column           | Requirement | Supply Planning usage                                                                            |
| ---------------- | ----------- | ------------------------------------------------------------------------------------------------ |
| id               | Required    | Unique identifier for the trading partner (vendor, customer, carrier, or other external entity). |
| description      | Optional    | Name of the trading partner organization.                                                        |
| eff\_start\_date | Optional    | Date from which the trading partner relationship is valid. Default 1900-01-01 00:00:00.          |
| eff\_end\_date   | Optional    | Date after which the trading partner relationship expires. Default 9999-12-31 23:59:59.          |

## vendor\_product (conditional required)

How is this data entity used? Supply Planning uses vendor product data to define which vendors are authorized to supply specific products. This data enables the planning engine to validate sourcing rules and generate purchase orders only to approved vendor-product combinations within their effective date ranges.

| Column               | Requirement | Supply Planning usage                                                 |
| -------------------- | ----------- | --------------------------------------------------------------------- |
| vendor\_tpartner\_id | Required    | Vendor/supplier who can provide this product.                         |
| product\_id          | Required    | Product that the vendor is authorized/capable of supplying.           |
| eff\_start\_date     | Required    | Date from which the vendor is authorized to supply this product.      |
| eff\_end\_date       | Required    | Date after which the vendor is no longer authorized for this product. |

## vendor\_lead\_time (conditional required)

How is this data entity used? Supply Planning uses vendor lead time data to determine the expected duration between placing a purchase order and receiving the goods at the destination site. Accurate lead times are critical for the planning engine to recommend orders with the correct timing to meet demand without creating unnecessary stockouts or excess inventory.

| Column               | Requirement | Supply Planning usage                                                               |
| -------------------- | ----------- | ----------------------------------------------------------------------------------- |
| vendor\_tpartner\_id | Required    | Vendor/supplier whose lead time is being defined.                                   |
| product\_id          | Optional    | Specific product the lead time applies to (if product-level granularity).           |
| product\_group\_id   | Optional    | Product group the lead time applies to (if group-level granularity).                |
| site\_id             | Required    | Destination site for delivery, since lead times may vary by receiving location.     |
| planned\_lead\_time  | Required    | Expected number of days from order placement to delivery receipt.                   |
| eff\_start\_date     | Optional    | Date from which this lead time definition is valid. Default is 1900-01-01 00:00:00. |
| eff\_end\_date       | Optional    | Date after which this lead time definition expires. Default is 9999-12-31 23:59:59. |
| region\_id           | Optional    | Geographic region for region-specific lead time definitions.                        |

## company (optional)

How is this data entity used? Supply Planning uses company data to support multi-entity planning environments where different legal entities or business units operate within a shared supply chain instance.

| Column           | Requirement | Supply Planning usage                                 |
| ---------------- | ----------- | ----------------------------------------------------- |
| id               | Required    | Unique identifier for the company/legal entity.       |
| description      | Optional    | Name or label of the company.                         |
| address\_line\_1 | Optional    | Primary street address line for the company.          |
| address\_line\_2 | Optional    | Secondary address line (suite, building, floor).      |
| city             | Optional    | City where the company is located.                    |
| state\_prov      | Optional    | State or province where the company is located.       |
| postal\_code     | Optional    | Postal or ZIP code for the company address.           |
| country          | Optional    | Country where the company is registered or operating. |
| phone            | Optional    | Primary contact phone number for the company.         |
| email            | Optional    | Primary contact email address for the company.        |

## sourcing\_rules (required)

How is this data entity used? Supply Planning uses sourcing rules to determine how each product at each destination site is replenished. Rules specify whether supply comes from an external buy (purchase order), internal transfer (transfer order), or manufacturing (production order), and define the sourcing priority and allocation ratios when multiple supply options exist.

| Column                   | Requirement            | Supply Planning usage                                                                                                                                                                      |
| ------------------------ | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| sourcing\_rule\_id       | Required               | Unique identifier for the sourcing rule.                                                                                                                                                   |
| product\_id              | Optional               | Specific product governed by this sourcing rule.                                                                                                                                           |
| product\_group\_id       | Optional               | Product group governed by this sourcing rule.                                                                                                                                              |
| to\_site\_id             | Required               | Destination site that will receive supply under this rule.                                                                                                                                 |
| sourcing\_rule\_type     | Required               | Nature of the sourcing: buy (external procurement), manufacture (internal production), or transfer (inter-plant).                                                                          |
| from\_site\_id           | Conditionally required | Source/origin site for the supply (internal plant or warehouse). Required when sourcing\_rule\_type is "transfer".                                                                         |
| tpartner\_id             | Conditionally required | Vendor/supplier ID; required when sourcing\_rule\_type is "buy".                                                                                                                           |
| transportation\_lane\_id | Optional               | Link to the transportation lane used for this sourcing path.                                                                                                                               |
| sourcing\_priority       | Optional               | Priority ranking used when multiple sourcing options exist for the same product/site.                                                                                                      |
| sourcing\_ratio          | Optional               | Percentage allocation (0-100) defining what proportion of total demand this sourcing rule fulfills when multiple active sourcing rules exist for the same product-site-period combination. |
| min\_qty                 | Optional               | Minimum order quantity constraint for this sourcing rule.                                                                                                                                  |
| qty\_multiple            | Optional               | Order quantity must be a multiple of this value (lot sizing).                                                                                                                              |
| production\_process\_id  | Optional               | Manufacturing process/route used when sourcing\_rule\_type is "manufacture".                                                                                                               |
| eff\_start\_date         | Optional               | Date from which this sourcing rule is active. Default is 1900-01-01 00:00:00.                                                                                                              |
| eff\_end\_date           | Optional               | Date after which this sourcing rule expires. Default is 9999-12-31 23:59:59.                                                                                                               |

## inventory\_policy (required)

How is this data entity used? Supply Planning uses inventory policy data to determine the safety stock calculation method and replenishment thresholds for each product-site combination. The policy type (absolute level, days-of-cover demand, or days-of-cover forecast) governs how the planning engine computes minimum inventory buffers and generates replenishment recommendations.

| Column                 | Requirement            | Supply Planning usage                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------------- | ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id                     | Required               | Unique identifier for the inventory policy record.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| site\_id               | Optional               | The site/warehouse to which this inventory policy applies.                                                                                                                                                                                                                                                                                                                                                                                                             |
| dest\_geo\_id          | Optional               | Geographic region this policy targets, enabling region-specific stocking strategies.                                                                                                                                                                                                                                                                                                                                                                                   |
| product\_id            | Optional               | Specific product this policy applies to (if product-level policy).                                                                                                                                                                                                                                                                                                                                                                                                     |
| product\_group\_id     | Optional               | Product group this policy applies to (if group-level policy).                                                                                                                                                                                                                                                                                                                                                                                                          |
| ss\_policy             | Required               | Safety stock policy type governing how safety stock is calculated: Abs\_level, DOC\_dem, or DOC\_fcst. Currently sl (service level) is not supported. 1. Abs\_level: Uses units specified in min/max inventory qty. Ordering will be suggested whenever inventory falls below min. 2. DOC\_dem: Uses days of cover computed from historical demand as target level of inventory. 3. DOC\_fcst: Uses days of cover computed from forecast as target level of inventory. |
| min\_safety\_stock     | Optional               | Absolute minimum safety stock quantity floor that overrides any policy-calculated value. Expressed in the product's base unit of measure.                                                                                                                                                                                                                                                                                                                              |
| min\_inventory\_qty    | Conditionally required | Either min\_inventory\_qty/max\_inventory\_qty or target\_inventory\_qty is required when ss\_policy is abs\_level. Minimum inventory level (reorder point) that triggers a replenishment signal when on-hand quantity drops below this threshold.                                                                                                                                                                                                                     |
| max\_inventory\_qty    | Conditionally required | Either min\_inventory\_qty/max\_inventory\_qty or target\_inventory\_qty is required when ss\_policy is abs\_level. Maximum allowable inventory quantity (order-up-to level) defining the upper cap for replenishment orders. Prevents overstocking by limiting the total inventory a site should hold for this product.                                                                                                                                               |
| target\_inventory\_qty | Conditionally required | Either min\_inventory\_qty/max\_inventory\_qty or target\_inventory\_qty is required when ss\_policy is abs\_level. This is the target inventory quantity that the system will maintain.                                                                                                                                                                                                                                                                               |
| min\_doc\_limit        | Conditionally required | Either (min\_doc\_limit and max\_doc\_limit pair) or target\_doc\_limit is required when ss\_policy is doc\_dem or doc\_fcst. Minimum days of cover floor ensuring that inventory always covers at least this many days of forward demand.                                                                                                                                                                                                                             |
| max\_doc\_limit        | Conditionally required | Either (min\_doc\_limit and max\_doc\_limit pair) or target\_doc\_limit is required when ss\_policy is doc\_dem or doc\_fcst. Maximum days of cover limit representing the upper boundary on inventory coverage.                                                                                                                                                                                                                                                       |
| target\_doc\_limit     | Conditionally required | Either (min\_doc\_limit and max\_doc\_limit pair) or target\_doc\_limit is required when ss\_policy is doc\_dem or doc\_fcst. Target days of cover (historical demand or forecast based).                                                                                                                                                                                                                                                                              |
| eff\_start\_date       | Optional               | Date from which the inventory policy is effective. Default is 1900-01-01 00:00:00.                                                                                                                                                                                                                                                                                                                                                                                     |
| eff\_end\_date         | Optional               | Date after which the inventory policy expires. Default is 9999-12-31 23:59:59.                                                                                                                                                                                                                                                                                                                                                                                         |

## inventory\_level (required)

How is this data entity used? Supply Planning uses inventory level snapshots to establish the current on-hand stock position at each site for each product. This data is the starting point for replenishment calculations, enabling the planning engine to determine the gap between current inventory and the target level defined by the inventory policy.

| Column              | Requirement | Supply Planning usage                                                                             |
| ------------------- | ----------- | ------------------------------------------------------------------------------------------------- |
| snapshot\_date      | Required    | Date/time when the inventory snapshot was taken.                                                  |
| site\_id            | Required    | Site/warehouse where this inventory is physically located.                                        |
| product\_id         | Required    | Product/material whose inventory is being reported.                                               |
| on\_hand\_inventory | Required    | Quantity of unrestricted, available-for-use stock on hand.                                        |
| inv\_condition      | Optional    | Condition or quality classification of the inventory (e.g., available, blocked, in-quality-hold). |

## forecast (conditionally required)

How is this data entity used? Supply Planning uses forecast data as the primary demand signal for replenishment calculations. The planning engine uses the forecasted demand quantities by product and site to determine how much inventory needs to be replenished and when, driving purchase, transfer, and production order recommendations across the planning horizon. This data is not required if forecast is generated by Amazon Connect Decisions Demand Intelligence.

| Column                      | Requirement            | Supply Planning usage                                                                                                                                                       |
| --------------------------- | ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| snapshot\_date              | Required               | Date when this forecast was generated or last updated.                                                                                                                      |
| site\_id                    | Required               | Site for which demand is being forecasted.                                                                                                                                  |
| product\_id                 | Required               | Product for which demand is being forecasted.                                                                                                                               |
| mean                        | Conditionally required | Either mean or p50 needs to be provided. Arithmetic mean of the demand forecast distribution for this product-site-period combination. Serves as the primary demand signal. |
| p50                         | Conditionally required | Either mean or p50 needs to be provided. Median (50th percentile) forecast quantity representing the most likely demand scenario.                                           |
| p10/20/30/40/50/60/70/80/90 | Optional               | Probabilistic forecast values at 10th, 50th, and 90th percentiles for demand variability analysis.                                                                          |
| forecast\_start\_dttm       | Required               | Start date/time of the forecast bucket period.                                                                                                                              |
| forecast\_end\_dttm         | Required               | End date/time of the forecast bucket period.                                                                                                                                |

## outbound\_order\_line (conditionally required)

How is this data entity used? Supply Planning uses outbound order line data to track customer orders and demand commitments. This data provides visibility into confirmed demand, allowing the planning engine to reserve inventory for committed customer orders and factor fulfillment obligations into replenishment recommendations.

| Column                     | Requirement | Supply Planning usage                                                                               |
| -------------------------- | ----------- | --------------------------------------------------------------------------------------------------- |
| id                         | Required    | Unique identifier for the outbound order line (delivery line item).                                 |
| product\_id                | Required    | Product being shipped to the customer.                                                              |
| cust\_order\_id            | Required    | Customer's sales order number this line belongs to.                                                 |
| status                     | Optional    | Current fulfillment status of the line (e.g., Open, Cancelled, Closed).                             |
| order\_date                | Optional    | Date the order was placed.                                                                          |
| init\_quantity\_requested  | Optional    | Original quantity the customer initially ordered.                                                   |
| final\_quantity\_requested | Required    | Current/adjusted quantity still to be fulfilled (accounts for partial shipments and order changes). |
| requested\_delivery\_date  | Required    | Date the customer originally requested delivery.                                                    |
| promised\_delivery\_date   | Optional    | Date committed to the customer after availability check.                                            |
| actual\_delivery\_date     | Optional    | Date the goods were actually received by the customer.                                              |
| ship\_from\_site\_id       | Required    | Warehouse or plant from which the product will be shipped.                                          |
| quantity\_promised         | Optional    | Quantity confirmed/committed to the customer.                                                       |
| quantity\_delivered        | Optional    | Quantity that has been physically shipped/delivered.                                                |

## inbound\_order\_line (conditionally required)

How is this data entity used? Supply Planning uses inbound order line data to track open purchase orders, transfer orders, and manufacturing orders. This data provides visibility into planned supply receipts, enabling the planning engine to account for in-transit and confirmed inventory when generating replenishment recommendations.

| Column                   | Requirement            | Supply Planning usage                                                                                                                                                  |
| ------------------------ | ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id                       | Required               | Unique identifier for the order line item (typically a composite of order ID and line number).                                                                         |
| order\_id                | Required               | Inbound order header number.                                                                                                                                           |
| tpartner\_id             | Conditionally required | Mandatory for PO (Purchase Orders). Links the order line to the vendor/supplier. Default SCN\_RESERVED\_NO\_VALUE\_PROVIDED.                                           |
| product\_id              | Required               | The product/material being ordered on this line.                                                                                                                       |
| order\_type              | Required               | Type classification of this order line. Should be PO (Purchase Order), TO (Transfer Order) or MO (Manufacture Order).                                                  |
| status                   | Optional               | Current status of this specific line item (e.g., Open, InTransit, Closed, Cancelled).                                                                                  |
| from\_site\_id           | Conditionally required | Mandatory for TO (Transfer Orders). Origin site from which the product is being shipped.                                                                               |
| to\_site\_id             | Required               | Destination site for this line item's delivery.                                                                                                                        |
| quantity\_submitted      | Conditionally required | Original quantity requested/ordered. Either quantity\_submitted or quantity\_confirmed should be provided.                                                             |
| quantity\_confirmed      | Conditionally required | Quantity confirmed by the supplier for delivery. Either quantity\_submitted or quantity\_confirmed should be provided.                                                 |
| quantity\_received       | Optional               | Quantity physically received at the destination site.                                                                                                                  |
| submitted\_date          | Optional               | Date this line item was created in the system.                                                                                                                         |
| earliest\_delivery\_date | Conditionally required | At least one of earliest\_delivery\_date, latest\_delivery\_date or expected\_delivery\_date should be provided.                                                       |
| expected\_delivery\_date | Conditionally required | Planned or promised delivery date for this line item. At least one of earliest\_delivery\_date, latest\_delivery\_date or expected\_delivery\_date should be provided. |
| latest\_delivery\_date   | Conditionally required | At least one of earliest\_delivery\_date, latest\_delivery\_date or expected\_delivery\_date should be provided.                                                       |
| earliest\_ship\_date     | Optional               | Earliest date and time when vendor shipped products for this order-line. If populated, planning engine will use this date to determine order start date.               |
| latest\_ship\_date       | Optional               | Latest date and time when vendor shipped products for this order-line. If populated, planning engine will use this date to determine order start date.                 |
| product\_group\_id       | Optional               | Product group context for this alternate mapping.                                                                                                                      |
| to\_site\_id             | Optional               | Destination site for the alternate product delivery.                                                                                                                   |
| from\_site\_id           | Optional               | Origin site for the alternate product sourcing.                                                                                                                        |
| transportation\_lane\_id | Optional               | Transportation lane to use when sourcing this alternate product.                                                                                                       |
| min\_qty                 | Optional               | Minimum order quantity for the alternate product.                                                                                                                      |
| qty\_multiple            | Optional               | Order quantity must be a multiple of this value for the alternate product.                                                                                             |

## product\_bom (conditionally required)

How is this data entity used? Supply Planning uses Product Bill of Materials (BOM) data to explode finished goods demand into component-level requirements. When the planning engine generates production orders for manufactured products, it uses the BOM to calculate how much of each raw material or sub-assembly is needed, creating dependent demand signals for component procurement and production planning.

| Column                   | Requirement | Supply Planning usage                                                                                                                              |
| ------------------------ | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| id                       | Required    | Unique identifier for the BOM line record, typically a surrogate key or composite of parent product, component product, site, and effective dates. |
| product\_id              | Required    | Foreign key to the Product table identifying the finished good or parent assembly that is manufactured using this BOM.                             |
| site\_id                 | Required    | Foreign key to the Site table identifying the manufacturing location where this BOM is valid.                                                      |
| component\_product\_id   | Required    | Foreign key to the Product table identifying the raw material, sub-assembly, or intermediate component required to produce the parent product.     |
| component\_quantity\_per | Required    | Quantity of the component product required to produce one unit of the parent finished good, expressed in the component's base unit of measure.     |
| eff\_start\_date         | Required    | Calendar date from which this BOM relationship is effective and should be used by the planning engine for demand explosion.                        |
| eff\_end\_date           | Required    | Calendar date after which this BOM relationship is no longer valid and should not be used for planning.                                            |
| production\_process\_id  | Optional    | Foreign key to the Production Process table identifying which manufacturing route or recipe uses this specific BOM.                                |

## production\_process (not supported in Supply Planning right now, to be added soon)

How is this data entity used? This data entity is not supported in Supply Planning right now. But it will be added soon. When supported, the planning engine will use setup time and operation time to calculate the manufacturing lead times and evaluate production capacity feasibility.

| Column                  | Requirement | Supply Planning usage                                                                                                                                                                               |
| ----------------------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| production\_process\_id | Required    | Unique identifier for the manufacturing process or production route. Represents a specific sequence of operations that transforms raw materials/components into a finished product at a given site. |
| product\_id             | Required    | Foreign key to the Product table identifying the finished good or output product manufactured by this production process.                                                                           |
| site\_id                | Required    | Foreign key to the Site table identifying the manufacturing facility where this production process is physically executed.                                                                          |
| setup\_time             | Required    | Fixed one-time duration (in hours) required to changeover, calibrate, and prepare the production equipment before a batch run can begin.                                                            |
| operation\_time         | Required    | Variable processing time (in hours) consumed per unit of output produced on this manufacturing line. Total production duration = setup\_time + (operation\_time x planned quantity).                |

## segmentation\_rule (not supported in Supply Planning right now, to be added soon)

How is this data entity used? This data entity is not supported in Supply Planning right now. But it will be added soon. Segmentation Rule data will enable differentiated planning by classifying products and sites into segments (e.g., by demand variability, customer tier, or product lifecycle). When supported, the planning engine will apply segment-specific inventory policies, forecast models, and service-level targets.

| Column                          | Requirement | Supply Planning usage                                                                                                                               |
| ------------------------------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| segmentation\_rule\_id          | Required    | Unique identifier for a segmentation rule mapping a specific segment\_type + segment\_value combination to product/site/channel dimensions.         |
| segment\_type                   | Required    | Name of the segmentation dimension being defined (e.g., DemandVariability, CustomerTier, ProductLifecycle, ServiceLevel).                           |
| segment\_value                  | Required    | Specific value within the segment\_type classification (e.g., High, Medium, Low for DemandVariability; A, B, C for CustomerTier).                   |
| segmentation\_rule\_description | Optional    | Human-readable explanation of the business logic or criteria used to assign entities to this segment.                                               |
| product\_id                     | Optional    | Foreign key to the Product table. When populated, the rule applies to this specific product only.                                                   |
| product\_level\_1               | Optional    | Highest level in the product hierarchy. Enables broad segmentation across entire product families.                                                  |
| product\_level\_2               | Optional    | Second-level product hierarchy classification. Provides intermediate product grouping for segmentation.                                             |
| product\_level\_3               | Optional    | Third-level product hierarchy classification. Enables mid-granularity product segmentation.                                                         |
| product\_level\_4               | Optional    | Fourth-level product hierarchy classification. Enables fine-grained product segmentation.                                                           |
| product\_level\_5               | Optional    | Most granular product hierarchy level. Leave blank if the rule targets a coarser level or a specific product\_id.                                   |
| site\_id                        | Optional    | Foreign key to the Site table. When populated, the rule applies to this specific site only.                                                         |
| site\_level\_1                  | Optional    | Highest level in the site hierarchy. Enables broad geographic segmentation across the network.                                                      |
| site\_level\_2                  | Optional    | Second-level site hierarchy. Provides intermediate geographic grouping for segmentation.                                                            |
| site\_level\_3                  | Optional    | Third-level site hierarchy. Enables mid-granularity geographic segmentation.                                                                        |
| site\_level\_4                  | Optional    | Fourth-level site hierarchy. Enables fine-grained geographic segmentation.                                                                          |
| site\_level\_5                  | Optional    | Most granular site hierarchy level. Leave blank if the rule targets a coarser level or a specific site\_id.                                         |
| city                            | Optional    | City name of the ship-from site location. Provides geographic context for location-based segmentation.                                              |
| state\_prov                     | Optional    | State or province of the ship-from site. Enables regional segmentation and compliance with jurisdiction-specific business rules.                    |
| postal\_code                    | Optional    | Postal/ZIP code of the ship-from site. Enables precise geographic targeting for segmentation rules.                                                 |
| country                         | Optional    | Country of the ship-from site. Enables country-level segmentation for international operations.                                                     |
| trading\_partner\_id            | Optional    | Foreign key to the Trading Partner table. Enables segmentation rules based on supplier, customer, or carrier relationships.                         |
| company\_id                     | Optional    | Foreign key to the Company table. Enables multi-entity segmentation where different legal entities maintain separate classification rules.          |
| channel\_id                     | Optional    | Foreign key referencing the sales/distribution channel. Enables channel-specific segmentation for omnichannel operations.                           |
| creation\_date                  | Optional    | ISO 8601 timestamp when this segmentation rule was created. Supports audit trail and version tracking.                                              |
| connection\_id                  | Optional    | System-assigned identifier for the data source connection. Auto-populated by Prism upon ingestion — do not supply manually.                         |
| updated\_at                     | Optional    | System-managed timestamp of the last modification to this record. Auto-populated by Prism for data lineage — do not supply manually.                |
| updated\_by                     | Optional    | System-managed identifier of the user or process that last modified this record. Auto-populated by Prism for data lineage — do not supply manually. |

## Direct upload data entities

###### Note

capacity\_constraints, capacity\_product\_mapping, warehouse\_space\_limit, and planning\_time\_fence\_constraints don't require setting up the data ingestion flows. These data entities can be directly uploaded on the supply planning configuration page through Decision Teammates.

## capacity\_constraints (conditionally required)

How is this data entity used? Supply Planning uses capacity constraint data to define the minimum and maximum throughput limits for each capacity resource at each site within defined time buckets. The planning engine enforces these constraints when generating production and storage recommendations to ensure plans remain within physical or contractual feasibility boundaries.

| Column               | Requirement | Supply Planning usage                                                                                                                                                      |
| -------------------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id                   | Required    | Unique identifier for the capacity constraint record. References a combination of capacity resource, site, time bucket, and effective date range.                          |
| capacity\_id         | Required    | Foreign key to the Capacity table identifying the specific resource being constrained (e.g., a production line, storage zone, dock, or labor pool).                        |
| site\_id             | Required    | Foreign key to the Site table identifying the physical location where this capacity constraint applies.                                                                    |
| bucket\_type         | Required    | Defines the time bucket granularity for measuring and enforcing capacity utilization. Accepted values: Daily, Weekly, Monthly.                                             |
| eff\_start\_date     | Required    | Calendar date from which this capacity constraint becomes active and enforceable by the planning engine.                                                                   |
| eff\_end\_date       | Required    | Calendar date after which this capacity constraint expires and is no longer enforced.                                                                                      |
| min\_capacity\_usage | Optional    | Minimum throughput or utilization volume required within the defined time bucket. Represents a contractual or operational floor.                                           |
| max\_capacity\_usage | Required    | Maximum throughput or utilization volume allowed within the defined time bucket. The planning engine must not schedule production or allocate inventory beyond this limit. |

## capacity\_product\_mapping (conditionally required)

How is this data entity used? Supply Planning uses capacity product mapping data to link products to the capacity resources they consume at each site. This mapping enables the planning engine to aggregate total capacity demand across all products sharing a common resource, identify bottlenecks, and prioritize production sequencing when capacity is limited.

| Column       | Requirement | Supply Planning usage                                                                                                                              |
| ------------ | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| id           | Required    | Unique identifier for the capacity-to-product mapping record linking a specific product to the capacity resource it consumes at a given site.      |
| product\_id  | Required    | Foreign key to the Product table identifying the specific SKU or material whose production or handling consumes capacity from the mapped resource. |
| site\_id     | Required    | Foreign key to the Site table specifying the location where this product-to-capacity relationship is valid.                                        |
| capacity\_id | Required    | Foreign key to the Capacity table identifying which capacity resource this product consumes during production, storage, or handling.               |

## warehouse\_space\_limit (conditionally required)

How is this data entity used? Supply Planning uses warehouse space limit data to constrain replenishment recommendations so that planned inventory never exceeds the physical storage capacity of a warehouse. This prevents the planning engine from generating supply orders that would result in overcrowding or infeasible storage requirements at a site.

| Column        | Requirement | Supply Planning usage                                                                                                                                                           |
| ------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| site\_id      | Required    | Identifier of the warehouse whose capacity is being defined.                                                                                                                    |
| max\_capacity | Required    | Maximum storage capacity of the warehouse, expressed in the volume unit of measure defined in the Product entity. Used to constrain supply plans from exceeding physical space. |

## planning\_time\_fence\_constraints (conditionally required)

How is this data entity used? Supply Planning uses planning time fence constraint data to define time boundaries within which the planning engine is restricted from making changes to existing supply orders. These constraints enable planners to protect near-term supply plans from automatic rescheduling, preserving confirmed orders for specific products and sites within the defined time fence window.

| Column                      | Requirement | Supply Planning usage                                                                                                                                                                                                                                                |
| --------------------------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| rule\_id                    | Required    | Unique identifier for the planning time fence constraint rule.                                                                                                                                                                                                       |
| product\_id                 | Optional    | Foreign key to the Product table. When populated, the time fence applies to this specific product only. When left blank, the constraint applies to all products at the specified site.                                                                               |
| site\_id                    | Optional    | Foreign key to the Site table. When populated, the time fence applies to this specific site only. When left blank, the constraint applies to the specified product across all sites.                                                                                 |
| planning\_time\_fence\_days | Required    | Number of calendar days from the planning run date within which the planning engine will not automatically reschedule or cancel existing supply orders. Orders with order start dates within this window are treated as frozen and protected from automated changes. |
