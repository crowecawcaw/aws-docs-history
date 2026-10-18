

# Data Requirements for Supply Planning
<a name="data-requirements-for-supply-planning"></a>

## Data Entities for Supply Planning
<a name="data-requirements-for-supply-planning-data-entities"></a>

The following table lists the data entities and columns used by Supply Planning.

How to read the table:
+ Required - The entity or columns in the data entity are mandatory for the supply planning engine to function correctly.
+ Conditionally required - The entity or columns in the data entity are required depending on the specific major functional requirements, policy type, order type, or sourcing rule type selected.
+ Optional - The entity or columns in the data entity is optional. For enhanced planning accuracy and feature output, it is recommended to add the column with values.

### site (required)
<a name="data-requirements-for-supply-planning-site"></a>

How is this data entity used? Supply Planning uses the site data to define the internal locations (plants, warehouses, and distribution centers) within the supply chain network. Sites serve as the origin and destination nodes for transportation lanes and sourcing rules.


| Column | Is the column required? | How is this column used in Supply Planning? | 
| --- | --- | --- | 
| id | Required | Unique identifier for the internal site (plant, warehouse, or distribution center) within the supply chain network. Make sure the column values do not have invalid characters such as asterisk and double-quotes. | 
| description | Optional | Human-readable name or label for the site. | 
| geo\_id | Optional | Group the sites into a geographical region. Inventory policies and vendor lead time can be defined at geo\_id level. | 
| is\_active | Optional | Boolean flag indicating whether the site is currently operational and available for planning. By default, the site is considered as Active. | 
| open\_date | Optional | Calendar date on which the site became or will become operationally active. Used by the planning engine to exclude future sites from current plans while incorporating them into forward-looking network scenarios. | 
| end\_date | Optional | Calendar date on which the site was or will be decommissioned and removed from active planning. After this date, the planning engine will no longer route demand to or hold inventory at this site. | 
| site\_level\_1 | Optional | The highest level in the site hierarchy, typically representing the broadest geographic or organizational grouping. This denormalized field enables efficient filtering and sorting across the site hierarchy. | 
| site\_level\_2 | Optional | The second level in the site hierarchy, representing a regional subdivision within the top-level site grouping. Leave blank if your site hierarchy has fewer than 2 levels. | 
| site\_level\_3 | Optional | The third level in the site hierarchy, representing a more granular geographic or organizational classification within level 2. Leave blank if your site hierarchy has fewer than 3 levels. | 
| site\_level\_4 | Optional | The fourth level in the site hierarchy, representing a specific site cluster or sub-region within level 3. Leave blank if your site hierarchy has fewer than 4 levels. | 
| site\_level\_5 | Optional | The fifth and most granular level in the site hierarchy. Leave blank if your site hierarchy has fewer than 5 levels. | 

### product (required)
<a name="data-requirements-for-supply-planning-product"></a>

How is this data entity used? Supply Planning uses the product data to identify and classify all items being planned. Product data are used to establish hierarchy filters for supply plan review, link products to inventory policies and sourcing rules, and support multi-level product segmentation.


| Column | Is the column required? | How is this column used in Supply Planning? | 
| --- | --- | --- | 
| id | Required | Unique identifier for the product/material (SKU-level). Make sure the column values do not have duplicate IDs and special characters such as asterisk and double-quotes. | 
| description | Required | Human-readable name or description of the product. | 
| product\_group\_id | Optional | Group the products into a product group. Sourcing rules and inventory policies can be defined at product\_group\_id level. | 
| unit\_cost | Optional | Standard cost per unit used for inventory valuation and cost planning. | 
| unit\_price | Optional | Unit Price or standard price or MSRP of product. | 
| base\_uom | Optional | Unit of measure for product. Default to Each. | 
| volume\_uom | Optional | Product volume UOM. Currently volume\_uom has to be the same across all products if populated. | 
| unit\_volume | Optional | Units of product per volume\_uom defined at the warehouse level. | 
| is\_deleted | Optional | Boolean flag indicating whether the product has been discontinued or marked inactive. By default, the product is considered as Active or Not deleted. | 
| product\_level\_1 | Optional | The highest level in the product hierarchy, typically representing the broadest product category or division. This denormalized field enables efficient filtering and sorting across the product hierarchy. | 
| product\_level\_2 | Optional | The second level in the product hierarchy, representing a subcategory within the top-level product category. Leave blank if your product hierarchy has fewer than 2 levels. | 
| product\_level\_3 | Optional | The third level in the product hierarchy, representing a more granular product classification within level 2. Leave blank if your product hierarchy has fewer than 3 levels. | 
| product\_level\_4 | Optional | The fourth level in the product hierarchy, representing a specific product family or sub-classification within level 3. Leave blank if your product hierarchy has fewer than 4 levels. | 
| product\_level\_5 | Optional | The fifth and most granular level in the product hierarchy. Leave blank if your product hierarchy has fewer than 5 levels. | 

### sourcing\_rules (required)
<a name="data-requirements-for-supply-planning-sourcing-rules"></a>

How is this data entity used? Supply Planning uses sourcing rules to determine how each product at each destination site is replenished. Rules specify whether supply comes from an external buy (purchase order), internal transfer (transfer order), or manufacturing (production order), and define the sourcing priority and allocation ratios when multiple supply options exist.


| Column | Is the column required? | How is this column used in Supply Planning? | 
| --- | --- | --- | 
| sourcing\_rule\_id | Required | Unique identifier for the sourcing rule. | 
| product\_id | Optional | Specific product governed by this sourcing rule. | 
| product\_group\_id | Optional | Product group governed by this sourcing rule. This field will ignored if product\_id is populated. | 
| to\_site\_id | Required | Destination site that will receive supply under this rule. | 
| sourcing\_rule\_type | Required | Nature of the sourcing: buy (external procurement), manufacture (internal production), or transfer (inter transfer). | 
| from\_site\_id | Conditionally required | Source/origin site for the supply (internal plant or warehouse). Required when sourcing\_rule\_type is "transfer". | 
| tpartner\_id | Conditionally required | Vendor/supplier ID; required when sourcing\_rule\_type is "buy". | 
| transportation\_lane\_id | Optional | transportation lane used for this sourcing path. | 
| production\_process\_id | Optional | Manufacturing process/route used when sourcing\_rule\_type is "manufacture". | 
| sourcing\_priority | Optional | Priority ranking used when multiple sourcing options exist for the same product/site. The planning engine will try to adhere to this priority when possible. | 
| sourcing\_ratio | Optional | Relative ratio which defines what proportion of total demand this sourcing rule fulfills when multiple active sourcing rules exist for the same product-site-period combination. For example, the ratio can be defined as 1:2:4 if there are 3 sources. The system will try to split demand according to this ratio when possible. | 
| min\_qty | Optional | Minimum order quantity constraint for this sourcing rule. | 
| qty\_multiple | Optional | Order quantity must be a multiple of this value (lot sizing). | 
| eff\_start\_date | Optional | Date from which this sourcing rule is active. Default is 1900-01-01 00:00:00. | 
| eff\_end\_date | Optional | Date after which this sourcing rule expires. Default is 2999-12-31 23:59:59. | 

### inventory\_policy (required)
<a name="data-requirements-for-supply-planning-inventory-policy"></a>

How is this data entity used? Supply Planning uses inventory policy data to determine the safety stock calculation method and replenishment thresholds for each product-site combination. The policy type (absolute level, days-of-cover average demand, or days-of-cover future forecast) governs how the planning engine computes inventory buffers and generates replenishment recommendations.


| Column | Is the column required? | How is this column used in Supply Planning? | 
| --- | --- | --- | 
| id | Required | Unique identifier for the inventory policy record. | 
| site\_id | Optional | The site/warehouse to which this inventory policy applies. | 
| dest\_geo\_id | Optional | Geographic region this policy targets, enabling region-specific stocking strategies. | 
| product\_id | Optional | Specific product this policy applies to. | 
| product\_group\_id | Optional | Product group this policy applies to. This field will be ignored if product\_id is populated. | 
| ss\_policy | Required | Safety stock policy type governing how safety stock is calculated: Abs\_level, DOC\_dem, or DOC\_fcst. Currently sl (service level) is not supported. 1. Abs\_level: Quantity based inventory policy. 2. DOC\_dem: Days of cover computed from average historical demand. 3. DOC\_fcst: Days of cover computed from future forecast and open sales orders. | 
| min\_safety\_stock | Optional | Absolute minimum safety stock quantity floor that overrides any calculated value based on days of cover policies. | 
| min\_inventory\_qty | Conditionally required | Either min\_inventory\_qty/max\_inventory\_qty or target\_inventory\_qty is required when ss\_policy is abs\_level. Minimum inventory level (reorder point) that triggers a replenishment signal when on-hand quantity drops below this threshold. | 
| max\_inventory\_qty | Conditionally required | Either min\_inventory\_qty/max\_inventory\_qty or target\_inventory\_qty is required when ss\_policy is abs\_level. Maximum allowable inventory quantity (order-up-to level) defining the upper cap for replenishment orders. Prevents overstocking by limiting the total inventory a site should hold for this product. | 
| target\_inventory\_qty | Conditionally required | Either min\_inventory\_qty/max\_inventory\_qty or target\_inventory\_qty is required when ss\_policy is abs\_level. This is the target inventory quantity that the system will maintain. | 
| min\_doc\_limit | Conditionally required | Either (min\_doc\_limit and max\_doc\_limit pair) or target\_doc\_limit is required when ss\_policy is doc\_dem or doc\_fcst. Minimum days of cover floor ensuring that inventory always covers at least this many days of forward demand. | 
| max\_doc\_limit | Conditionally required | Either (min\_doc\_limit and max\_doc\_limit pair) or target\_doc\_limit is required when ss\_policy is doc\_dem or doc\_fcst. Maximum days of cover limit representing the upper boundary on inventory coverage. | 
| target\_doc\_limit | Conditionally required | Either (min\_doc\_limit and max\_doc\_limit pair) or target\_doc\_limit is required when ss\_policy is doc\_dem or doc\_fcst. Target days of cover (historical demand or forecast based). | 
| eff\_start\_date | Optional | Date from which the inventory policy is effective. Default is 1900-01-01 00:00:00. | 
| eff\_end\_date | Optional | Date after which the inventory policy expires. Default is 9999-12-31 23:59:59. | 

### trading\_partner (conditional required)
<a name="data-requirements-for-supply-planning-trading-partner"></a>

How is this data entity used? Supply Planning uses trading partner data to identify suppliers in the supply chain. Trading partners are referenced by sourcing rules, inbound order lines, and vendor lead times to associate supply activities with external business entities. This data is required for sourcing rule lines which have sourcing rule type set to "buy".


| Column | Is the column required? | How is this column used in Supply Planning? | 
| --- | --- | --- | 
| id | Required | Unique identifier for the trading partner (vendor, customer, carrier, or other external entity). | 
| description | Optional | Name of the trading partner organization. | 
| eff\_start\_date | Optional | Date from which the trading partner relationship is valid. Default 1900-01-01 00:00:00. | 
| eff\_end\_date | Optional | Date after which the trading partner relationship expires. Default 2999-12-31 23:59:59. | 

### vendor\_product (conditional required)
<a name="data-requirements-for-supply-planning-vendor-product"></a>

How is this data entity used? Supply Planning uses vendor product data to define which vendors are authorized to supply specific products. This data enables the planning engine to validate sourcing rules and generate purchase orders only for approved vendor-product combinations within their effective date ranges. This data is required for sourcing rule lines which have sourcing rule type set to "buy".


| Column | Is the column required? | How is this column used in Supply Planning? | 
| --- | --- | --- | 
| vendor\_tpartner\_id | Required | Vendor/supplier who can provide this product. | 
| product\_id | Required | Product that the vendor can supply. | 
| eff\_start\_date | Required | Date from which the vendor is authorized to supply this product. | 
| eff\_end\_date | Required | Date after which the vendor is no longer authorized for this product. | 

### vendor\_lead\_time (optional)
<a name="data-requirements-for-supply-planning-vendor-lead-time"></a>

How is this data entity used? Supply Planning uses vendor lead time data to determine the expected duration between placing a purchase order and receiving the goods at the destination site. Accurate lead times are critical for the planning engine to recommend orders with the correct timing to meet demand without creating unnecessary stockouts or excess inventory. Supply planning will assume zero vendor lead time if this data is not available.


| Column | Is the column required? | How is this column used in Supply Planning? | 
| --- | --- | --- | 
| vendor\_tpartner\_id | Required | Vendor/supplier whose lead time is being defined. | 
| product\_id | Optional | Specific product the lead time applies to. | 
| product\_group\_id | Optional | Product group the lead time applies to. This field will be ignored if product\_id is populated. | 
| site\_id | Conditional Required | Destination site for delivery, since lead times may vary by receiving location. This field needs to be populated if region\_id is not populated. | 
| region\_id | Optional | Geographic region for region-specific lead time definitions. | 
| planned\_lead\_time | Required | Expected number of days from order placement to delivery receipt. | 
| eff\_start\_date | Optional | Date from which this lead time definition is valid. Default is 1900-01-01 00:00:00. | 
| eff\_end\_date | Optional | Date after which this lead time definition expires. Default is 2999-12-31 23:59:59. | 

### transportation\_lane (optional)
<a name="data-requirements-for-supply-planning-transportation-lane"></a>

How is this data entity used? Supply Planning uses transportation lane data to model the routes between origin and destination sites in the network. This data defines transit times and validity windows that the system uses to schedule the transfer orders. Supply planning will assume zero vendor lead time if this data is not available for sourcing rule lines which have sourcing rule type set to "transfer".


| Column | Is the column required? | How is this column used in Supply Planning? | 
| --- | --- | --- | 
| id | Required | Unique identifier for the transportation lane, typically a composite of origin, destination, product group, and vendor. | 
| from\_site\_id | Required | Origin site (supplier warehouse or manufacturing plant) from which goods are shipped. | 
| to\_site\_id | Required | Destination site (receiving warehouse or plant) where goods are delivered. | 
| product\_group\_id | Optional | Product category this lane applies to, enabling lane-level filtering by product group. | 
| product\_id | Optional | Specific product this lane applies to, for product-level lane definitions. | 
| transit\_time | Required | Number of days required to transport goods from origin to destination. Default is 0. | 
| eff\_start\_date | Required | Date from which this transportation lane becomes active/valid. | 
| eff\_end\_date | Required | Date after which this transportation lane is no longer valid. | 

### inventory\_level (required)
<a name="data-requirements-for-supply-planning-inventory-level"></a>

How is this data entity used? Supply Planning uses inventory level snapshots to establish the current on-hand stock position at each site for each product. This data is the starting point for replenishment calculations, enabling the planning engine to determine the gap between current inventory and the target level defined by the inventory policy.


| Column | Is the column required? | How is this column used in Supply Planning? | 
| --- | --- | --- | 
| snapshot\_date | Required | Date/time when the inventory snapshot was taken. | 
| site\_id | Required | Site where this inventory is located. | 
| product\_id | Required | Product whose inventory is being reported. | 
| on\_hand\_inventory | Required | Quantity on hand. | 
| inv\_condition | Optional | The inv\_condition indicates whether inventory is available for planning purposes. Unrestricted - Interpreted as Available. Blocked - Interpreted as Not Available. No value - Interpreted as Available. Any other status or condition - Interpreted as Available. | 

### forecast (conditionally required)
<a name="data-requirements-for-supply-planning-forecast"></a>

How is this data entity used? Supply Planning uses forecast data as the primary demand signal for replenishment calculations. The system uses the forecasted demand quantities by product and site to determine how much inventory needs to be replenished and when, driving purchase, transfer, and production order recommendations across the planning horizon. This data is not required if forecast is generated by Amazon Connect Decisions Demand Intelligence and the forecast source in supply plan configuration is set to Internal. This data is required when Forecast is selected for Demand Netting and Forecast Source is set to External on supply planning configuration page.


| Column | Is the column required? | How is this column used in Supply Planning? | 
| --- | --- | --- | 
| snapshot\_date | Required | Date when this forecast was generated or last updated. | 
| site\_id | Required | Site for which the demand is being forecasted. | 
| product\_id | Required | Product for which the demand is being forecasted. | 
| mean | Optional | Arithmetic mean of the demand forecast distribution for this product-site-period combination. Serves as the primary planning signal when probabilistic forecast values are not available. | 
| p50 | Conditionally required | Median (50th percentile) forecast quantity representing the most likely demand scenario. This field needs to be populated if mean is not populated. If both fields are populated, P50 takes precedence over mean. | 
| p10/20/30/40/50/60/70/80/90 | Optional | Probabilistic forecast values at 10th, 50th, and 90th percentiles for demand variability analysis. | 
| forecast\_start\_dttm | Required | Start date/time of the forecast bucket period. | 
| forecast\_end\_dttm | Required | End date/time of the forecast bucket period. | 

### outbound\_order\_line (conditionally required)
<a name="data-requirements-for-supply-planning-outbound-order-line"></a>

How is this data entity used? Supply Planning uses outbound order line data to track customer orders. This data provides visibility into confirmed demand, allowing the system to plan inventory for committed customer orders. This data is required if Sales order is enabled for demand netting in supply plan configuration.


| Column | Is the column required? | How is this column used in Supply Planning? | 
| --- | --- | --- | 
| id | Required | Unique identifier for the outbound order line (delivery line item). | 
| product\_id | Required | Product being shipped to the customer. | 
| cust\_order\_id | Required | Customer's sales order number this line belongs to. | 
| status | Optional | Current fulfillment status of the line. The supported status includes Open, Cancelled, and Closed. Open - Open sales order line. Cancelled - The system will ignore the cancelled lines. Closed - The system will ignore the closed lines. Any other status or condition - Interpreted as Open. | 
| order\_date | Optional | Date the order was placed. | 
| requested\_delivery\_date | Conditionally required | Date the customer originally requested delivery. This field is required if promised\_delivery\_date is not populated. If both fields are populated, promised\_delivery\_date takes precedence over requested\_delivery\_date. | 
| promised\_delivery\_date | Optional | Date committed to the customer after availability check. promised\_delivery\_date takes precedence over requested\_delivery\_date if both are populated. | 
| actual\_delivery\_date | Optional | Date the goods were actually received by the customer. This fields should be populated only for closed order lines. | 
| init\_quantity\_requested | Optional | Original quantity the customer initially ordered. | 
| final\_quantity\_requested | Conditionally required | Current/adjusted quantity still to be fulfilled. This field is required if both init\_quantity\_requested and quantity\_promised are not populated. final\_quantity\_requested takes precedence over init\_quantity\_requested. | 
| quantity\_promised | Optional | Quantity confirmed to the customer. quantity\_promised takes precedence over init\_quantity\_requested and final\_quantity\_requested. | 
| quantity\_delivered | Optional | Quantity that has been delivered. When calculating the orde line open quantity, quantity\_delivered is subtracted from quantity\_promised or quantity\_requested. | 

### inbound\_order\_line (optional)
<a name="data-requirements-for-supply-planning-inbound-order-line"></a>

How is this data entity used? Supply Planning uses inbound order line data to track open purchase orders, transfer orders, and manufacturing orders. This data provides visibility into existing supply orders, enabling the system to account for in-transit and confirmed inventory when generating replenishment recommendations.


| Column | Is the column required? | How is this column used in Supply Planning? | 
| --- | --- | --- | 
| id | Required | Unique identifier for the order line item (typically a composite of order ID and line number). | 
| order\_id | Required | inbound order header number | 
| product\_id | Required | The product/material being ordered on this line. | 
| order\_type | Required | Type classification of this order line. Should be PO (Purchase Order), TO (Transfer Order) or MO (Manufacture Order). | 
| tpartner\_id | Conditionally required | Mandatory for PO (Purchase Orders). Links the order line to the vendor/supplier. | 
| from\_site\_id | Conditionally required | Mandatory for TO(Transfer Orders). Origin site from which the product is being shipped. | 
| to\_site\_id | Required | Destination site for this line item's delivery. | 
| status | Optional | Current status of this specific line item. Supported status includes Open, InTransit, Closed, Cancelled. Open - Open TO lines will be considered as both demand at origin site and supply at destination site. Open PO and MO lines are only considered as supply. InTransit - In-transit lines will only be considered as supply. Cancelled - The system will ignore the cancelled lines. Closed - The system will ignore the closed lines. Any other status or condition - Interpreted as Open. | 
| quantity\_submitted | Conditionally required | Original quantity requested/ordered. This field needs to be populated if quantity\_confirmed is not provided. | 
| quantity\_confirmed | Optional | Quantity confirmed for delivery. Either quantity\_submitted or quantity\_confirmed should be provided. If both fields are popualted, quantity\_confirmed takes precedence over quantity\_submitted. | 
| quantity\_received | Optional | Quantity received at the destination site. If populated, quantity\_received will be subtracted from submitted quantity or confirmed quantity to calculate the order line open quantity. | 
| submitted\_date | Optional | Date this line item was created in the system. | 
| expected\_delivery\_date | required | Planned or promised delivery date for this line item. At least one of earliest\_delivery\_date, latest\_delivery\_date or expected\_delivery\_date should be provided. | 
| latest\_ship\_date | Optional | Latest date and time when this order line should be shipped. If populated, the system will use this date to determine order start date. If it is populated, the system will use lead time to calculate the order start date. | 

### product\_bom (Optional)
<a name="data-requirements-for-supply-planning-product-bom"></a>

How is this data entity used? Supply Planning uses Product Bill of Materials (BOM) data to explode finished goods demand into component-level requirements. When the planning engine generates production orders for manufactured products, it uses the BOM to calculate how much of each raw material or sub-assembly is needed, creating dependent demand signals for component procurement and production planning. If product\_bom is not defined, the production order will not consume any raw material.


| Column | Is the column required? | How is this column used in Supply Planning? | 
| --- | --- | --- | 
| id | Required | Unique identifier for the BOM line record, typically a surrogate key or composite of parent product, component product, site, and effective dates. | 
| product\_id | Required | product\_id which identifies the finished good or parent assembly that is manufactured using this BOM. | 
| site\_id | Required | site\_id which identifies the manufacturing location where this BOM is valid. | 
| component\_product\_id | Required | product\_id which identifies the raw material, sub-assembly, or intermediate component required to produce the parent product. | 
| component\_quantity\_per | Required | Quantity of the component product required to produce one unit of the parent finished good, expressed in the component's base unit of measure. | 
| eff\_start\_date | Required | Calendar date from which this BOM relationship is effective and should be used by the planning engine for demand explosion. | 
| eff\_end\_date | Required | Calendar date after which this BOM relationship is no longer valid and should not be used for planning. | 
| production\_process\_id | Optional | Foreign key to the Production Process table identifying which manufacturing route uses this specific BOM. | 

### production\_process (Optional)
<a name="data-requirements-for-supply-planning-production-process"></a>

How is this data entity used? The planning engine will use setup time plus operation time to calculate the manufacturing lead times and evaluate production capacity feasibility. Supply planning will assume zero vendor lead time if this data is not available for sourcing rule lines which have sourcing rule type set to "manufacture".


| Column | Is the column required? | How is this column used in Supply Planning? | 
| --- | --- | --- | 
| production\_process\_id | Required | Unique identifier for the manufacturing process or production route which transforms raw materials/components into a finished product at a given site. | 
| product\_id | Required | product\_id which identifies the finished good or output product manufactured by this production process. | 
| site\_id | Required | site\_id which identifies the manufacturing facility where this production process is physically executed. | 
| setup\_time | Optional | Fixed duration (in days) required to changeover, calibrate, and prepare the production equipment before a batch run can begin. | 
| operation\_time | Required | Fixed duration (in days) consumed in the actual manufacturing process. Total production duration = setup\_time \+ operation\_time | 

### segmentation\_rule (Optional)
<a name="data-requirements-for-supply-planning-segmentation-rule"></a>

How is this data entity used? Segmentation Rule data will enable differentiated classifications by grouping products and sites into segments (e.g. by planner code, ABC classifications, or product lifecycle). These segments can be used as filters in the planning hub.


| Column | Is the column required? | How is this column used in Supply Planning? | 
| --- | --- | --- | 
| segmentation\_rule\_id | Required | Unique identifier for a segmentation rule mapping a specific segment\_type \+ segment\_value combination to product/site dimensions. | 
| segment\_type | Required | Name of the segmentation dimension being defined (e.g., planner code, ABC classifications, product lifecycle). | 
| segment\_value | Required | Specific value within the segment\_type classification (e.g., A, B, C for ABC classification). | 
| segmentation\_rule\_description | Optional | Human-readable explanation of the business logic or criteria used to assign entities to this segment. | 
| product\_id | Optional | When populated, the rule applies to this specific product only. | 
| product\_level\_1 | Optional | Highest level in the product hierarchy. Enables broad segmentation across entire product families. | 
| product\_level\_2 | Optional | Second-level product hierarchy classification. Provides intermediate product grouping for segmentation. | 
| product\_level\_3 | Optional | Third-level product hierarchy classification. Enables mid-granularity product segmentation. | 
| product\_level\_4 | Optional | Fourth-level product hierarchy classification. Enables fine-grained product segmentation. | 
| product\_level\_5 | Optional | Most granular product hierarchy level. Leave blank if the rule targets a coarser level or a specific product\_id. | 
| site\_id | Optional | When populated, the rule applies to this specific site only. | 
| site\_level\_1 | Optional | Highest level in the site hierarchy. Enables broad geographic segmentation across the network. | 
| site\_level\_2 | Optional | Second-level site hierarchy. Provides intermediate geographic grouping for segmentation. | 
| site\_level\_3 | Optional | Third-level site hierarchy. Enables mid-granularity geographic segmentation. | 
| site\_level\_4 | Optional | Fourth-level site hierarchy. Enables fine-grained geographic segmentation. | 
| site\_level\_5 | Optional | Most granular site hierarchy level. Leave blank if the rule targets a coarser level or a specific site\_id. | 

### product\_alternate (Optional)
<a name="data-requirements-for-supply-planning-product-alternate"></a>

How is this data entity used? When an alternate product relationship is defined, supply planning considers available inventory and supply of the alternate product at the same site when fulfilling demand for the main product. The system consumes the available alternate product supply first. Once that supply is exhausted, the system will then create new planned orders for the main product.


| Column | Is the column required? | How is this column used in Forecasting? | 
| --- | --- | --- | 
| product\_alternate\_id | Required | unique record identifier. | 
| product\_id | Required | ID of the new product or newer version of the product. | 
| alternative\_product\_id | Required | product\_id of alternate product (older version of the product) | 
| alternate\_type | Optional | Alternate product type. For example, similar\_demand\_value. | 
| eff\_start\_date | Optional | The date and time the record becomes effective. | 
| eff\_end\_date | Optional | The date and time the record ends. Make sure this date is on or after the eff\_start\_date. | 
| status | Optional | Status of the alternate product record. For example, Active, Inactive. Inactive records will be ignored. | 

### product\_uom (Optional)
<a name="data-requirements-for-supply-planning-product-uom"></a>

How is this data entity used? The Product UOM data defines unit-of-measure (UOM) conversions for products. Each product has a base UOM specified in the Product Master table. The Product UOM table establishes conversion rates between the base UOM and supported alternate UOMs. These conversions enable users to view product quantities in alternate units of measure within the Supply Planning Hub, including the Horizontal Supply Plan Grid and other applicable planning views. This provides flexibility in how product quantities are displayed while maintaining consistency with the product's defined base UOM.


| Column | Is the column required? | How is this column used in Forecasting? | 
| --- | --- | --- | 
| product\_uom\_id | Required | unique record identifier. | 
| Product\_id | Required | product\_id for which alternate UOM is defined | 
| quantity | Required | This quantity represents the UOM conversion rate used to translate from product base UOM to the alternate UOM. | 
| quantity\_uom | Required | The alternate UOM of the product | 
| eff\_start\_date | Optional | The date and time the record becomes effective. | 
| eff\_end\_date | Optional | The date and time the record ends. Make sure this date is on or after the eff\_start\_date. | 
| status | Optional | Status of the alternate product record. For example, Active, Inactive. Inactive records will be ignored. | 

**Note**  
Planning constraints such as production\_capacity\_constraints, capacity\_product\_mapping, warehouse\_space\_limit, planning\_time\_fence\_constraints don't require setting up the data ingestion flows. These data should be directly uploaded on supply planning configuration page through Decision Teammates.

### production\_capacity\_constraints (optional)
<a name="data-requirements-for-supply-planning-production-capacity-constraints"></a>

How is this data entity used? Supply Planning uses production capacity constraint data to define the minimum and maximum throughput limits for each production capacity resource at each site within defined time buckets. The system enforces these constraints when generating production orders to ensure the supply plan remain within contractual production feasibility boundaries.


| Column | Is the column required? | How is this column used in Supply Planning? | 
| --- | --- | --- | 
| capacity\_id | Required | capacity\_id identifying the specific resource being constrained (e.g., a production line, storage zone, dock, or labor pool). | 
| site\_id | Required | site\_id identifying the physical location where this capacity constraint applies. | 
| bucket\_type | Required | Defines the time bucket granularity for measuring and enforcing capacity utilization. Accepted values: Daily, Weekly, Monthly. | 
| eff\_start\_date | Required | Calendar date from which this capacity constraint becomes active and enforceable by the planning engine. | 
| eff\_end\_date | Required | Calendar date after which this capacity constraint expires and is no longer enforced. | 
| min\_capacity\_usage | Optional | Minimum throughput or utilization volume required within the defined time bucket. Represents a contractual or operational floor. | 
| max\_capacity\_usage | Required | Maximum throughput or utilization volume allowed within the defined time bucket. The planning engine must not schedule production or allocate inventory beyond this limit. | 
| max\_changeover | Optional | Maximum number of allowed changeovers within the defined time bucket, effectively setting the limit on the SKU mix that can be produced in that period. | 

### capacity\_product\_mapping (optional)
<a name="data-requirements-for-supply-planning-capacity-product-mapping"></a>

How is this data entity used? Supply Planning uses capacity product mapping data to link products to the production capacity resources they consume at each site. This mapping enables the system to aggregate total capacity demand across all products sharing a common resource, identify bottlenecks, and prioritize production sequencing when capacity is limited.


| Column | Is the column required? | How is this column used in Supply Planning? | 
| --- | --- | --- | 
| product\_id | Required | product\_id identifying the specific SKU or material whose production or handling consumes capacity from the mapped resource. | 
| site\_id | Required | site\_id specifying the site where this product-to-capacity relationship is valid. | 
| capacity\_id | Required | capacity\_id identifying which capacity resource this product consumes during production, storage, or handling. | 
| capacity\_usage | Optional | Capacity usage defines how many units of capacity is consumed by producing one unit of a product. | 

### warehouse\_space\_limit (optional)
<a name="data-requirements-for-supply-planning-warehouse-space-limit"></a>

How is this data entity used? Supply Planning uses warehouse space limit data to constrain replenishment recommendations so that planned inventory never exceeds the physical storage capacity of a warehouse. This prevents the system from generating supply orders that would result in overcrowding or infeasible storage requirements at a site.


| Column | Is the column required? | How is this column used in Supply Planning? | 
| --- | --- | --- | 
| site\_id | Required | Identifier of the warehouse whose capacity is being defined. | 
| max\_capacity | Required | Maximum storage capacity of the warehouse, expressed in the volume unit of measure defined in the Product entity. Used to constrain supply plans from exceeding physical space. | 

### planning\_time\_fence\_constraints (optional)
<a name="data-requirements-for-supply-planning-planning-time-fence-constraints"></a>

How is this data entity used? Supply Planning uses planning time fence constraint data to define time boundaries within which the planning engine is restricted from making changes to existing supply orders. These constraints enable planners to protect near-term supply plans from automatic rescheduling, preserving confirmed orders for specific products and sites within the defined time fence window.


| Column | Is the column required? | How is this column used in Supply Planning? | 
| --- | --- | --- | 
| rule\_id | Required | Unique identifier for the planning time fence constraint rule. | 
| product\_id | Optional | When populated, the time fence applies to this specific product only. When left blank, site\_id must be popualted and the constraint applies to all products at the specified site. | 
| site\_id | Optional | When populated, the time fence applies to this specific site only. When left blank, product\_id must be populated and the constraint applies to the specified product across all sites. | 
| planning\_time\_fence\_days | Required | Number of calendar days from the planning run date within which the planning engine will not automatically reschedule or cancel existing supply orders. Orders with order start dates within this window are treated as frozen and protected from automated changes. | 