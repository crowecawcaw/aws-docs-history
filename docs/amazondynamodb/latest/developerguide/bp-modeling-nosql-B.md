

# Example of modeling relational data in DynamoDB
<a name="bp-modeling-nosql-B"></a>

This example describes how to model relational data in Amazon DynamoDB. The DynamoDB table design corresponds to the relational order entry schema that is shown in [Relational modeling](bp-relational-modeling.md). This design uses multiple specialized tables rather than a single adjacency list, providing clear operational boundaries while leveraging strategic GSIs to serve all access patterns efficiently.

The design approach uses aggregate-oriented principles, grouping data based on access patterns rather than rigid entity boundaries. Key design decisions include using separate tables for entities with low access correlation, embedding related data when always accessed together, and using item collections for identifying relationships.

The following tables and their accompanying indexes support the relational order entry schema:

## Employee Table Design
<a name="employee-table-design"></a>

The Employee table stores employee information as a single entity per item, optimized for direct employee lookups and supporting multiple query patterns through strategic GSIs. This table demonstrates the principle of designing separate tables for entities with independent operational characteristics and low cross-entity access correlation.

The table uses a simple partition key (employee\_id) without a sort key, as each employee is a distinct entity. Four GSIs enable efficient querying by different attributes:
+ *EmployeeByName GSI* - Uses INCLUDE projection with all employee attributes to support complete employee detail retrieval by name, handling potential duplicate names with employee\_id as sort key
+ *EmployeeByWarehouse GSI* - Uses INCLUDE projection with only essential attributes (name, job\_title, hire\_date) to minimize storage costs while supporting warehouse-based queries
+ *EmployeeByJobTitle GSI* - Enables role-based queries with INCLUDE projection for reporting and organizational analysis
+ *EmployeeByHireDate GSI* - Uses a static partition key value "EMPLOYEE" with hire\_date as sort key to enable efficient date range queries for recent hires. Since employee additions/updates are typically under 1,000 WCU, a single partition can handle the write load without hot partition issues


**Employee Table - Base Table Structure**  

| employee\_id (PK) | name | phone\_numbers | warehouse\_id | job\_title | hire\_date | entity\_type | 
| --- | --- | --- | --- | --- | --- | --- | 
| emp\_001 | John Smith | ["\+1-555-0101"] | wh\_sea | Manager | 2024-03-15 | EMPLOYEE | 
| emp\_002 | Jane Doe | ["\+1-555-0102", "\+1-555-0103"] | wh\_sea | Associate | 2025-01-10 | EMPLOYEE | 
| emp\_003 | Bob Wilson | ["\+1-555-0104"] | wh\_pdx | Associate | 2025-06-20 | EMPLOYEE | 
| emp\_004 | Alice Brown | ["\+1-555-0105"] | wh\_pdx | Supervisor | 2023-11-05 | EMPLOYEE | 
| emp\_005 | Charlie Davis | ["\+1-555-0106"] | wh\_sea | Associate | 2025-12-01 | EMPLOYEE | 


**EmployeeByName GSI - Supporting Employee Name Queries**  

| name (GSI-PK) | employee\_id (GSI-SK) | phone\_numbers | warehouse\_id | job\_title | hire\_date | 
| --- | --- | --- | --- | --- | --- | 
| Alice Brown | emp\_004 | ["\+1-555-0105"] | wh\_pdx | Supervisor | 2023-11-05 | 
| Bob Wilson | emp\_003 | ["\+1-555-0104"] | wh\_pdx | Associate | 2025-06-20 | 
| Charlie Davis | emp\_005 | ["\+1-555-0106"] | wh\_sea | Associate | 2025-12-01 | 
| Jane Doe | emp\_002 | ["\+1-555-0102", "\+1-555-0103"] | wh\_sea | Associate | 2025-01-10 | 
| John Smith | emp\_001 | ["\+1-555-0101"] | wh\_sea | Manager | 2024-03-15 | 


**EmployeeByWarehouse GSI - Supporting Warehouse Queries**  

| warehouse\_id (GSI-PK) | employee\_id (GSI-SK) | name | job\_title | hire\_date | 
| --- | --- | --- | --- | --- | 
| wh\_pdx | emp\_003 | Bob Wilson | Associate | 2025-06-20 | 
| wh\_pdx | emp\_004 | Alice Brown | Supervisor | 2023-11-05 | 
| wh\_sea | emp\_001 | John Smith | Manager | 2024-03-15 | 
| wh\_sea | emp\_002 | Jane Doe | Associate | 2025-01-10 | 
| wh\_sea | emp\_005 | Charlie Davis | Associate | 2025-12-01 | 


**EmployeeByJobTitle GSI - Supporting Job Title Queries**  

| job\_title (GSI-PK) | employee\_id (GSI-SK) | name | warehouse\_id | hire\_date | 
| --- | --- | --- | --- | --- | 
| Associate | emp\_002 | Jane Doe | wh\_sea | 2025-01-10 | 
| Associate | emp\_003 | Bob Wilson | wh\_pdx | 2025-06-20 | 
| Associate | emp\_005 | Charlie Davis | wh\_sea | 2025-12-01 | 
| Manager | emp\_001 | John Smith | wh\_sea | 2024-03-15 | 
| Supervisor | emp\_004 | Alice Brown | wh\_pdx | 2023-11-05 | 


**EmployeeByHireDate GSI - Supporting Recent Hire Queries**  

| entity\_type (GSI-PK) | hire\_date (GSI-SK) | employee\_id | name | warehouse\_id | 
| --- | --- | --- | --- | --- | 
| EMPLOYEE | 2023-11-05 | emp\_004 | Alice Brown | wh\_pdx | 
| EMPLOYEE | 2024-03-15 | emp\_001 | John Smith | wh\_sea | 
| EMPLOYEE | 2025-01-10 | emp\_002 | Jane Doe | wh\_sea | 
| EMPLOYEE | 2025-06-20 | emp\_003 | Bob Wilson | wh\_pdx | 
| EMPLOYEE | 2025-12-01 | emp\_005 | Charlie Davis | wh\_sea | 

## Customer Table Design
<a name="customer-table-design"></a>

The Customer table maintains customer information with strategic denormalization of account\_rep\_id to enable efficient account representative queries. This design choice trades slight storage overhead for query performance, eliminating the need for joins between customer and account representative data.

The table supports multiple phone numbers per customer using a list attribute, demonstrating DynamoDB's schema flexibility. The single GSI enables account representative workflows:
+ *CustomerByAccountRep GSI* - Uses INCLUDE projection with name and email attributes to support account rep customer management without requiring full customer record retrieval


**Customer Table - Base Table Structure**  

| customer\_id (PK) | name | phone\_numbers | email | account\_rep\_id | 
| --- | --- | --- | --- | --- | 
| cust\_001 | Acme Corp | ["\+1-555-1001"] | contact@acme.com | rep\_001 | 
| cust\_002 | TechStart Inc | ["\+1-555-1002", "\+1-555-1003"] | info@techstart.com | rep\_001 | 
| cust\_003 | Global Traders | ["\+1-555-1004"] | sales@globaltraders.com | rep\_002 | 
| cust\_004 | BuildRight LLC | ["\+1-555-1005"] | orders@buildright.com | rep\_002 | 
| cust\_005 | FastShip Co | ["\+1-555-1006"] | support@fastship.com | rep\_003 | 


**CustomerByAccountRep GSI - Supporting Account Rep Queries**  

| account\_rep\_id (GSI-PK) | customer\_id (GSI-SK) | name | email | 
| --- | --- | --- | --- | 
| rep\_001 | cust\_001 | Acme Corp | contact@acme.com | 
| rep\_001 | cust\_002 | TechStart Inc | info@techstart.com | 
| rep\_002 | cust\_003 | Global Traders | sales@globaltraders.com | 
| rep\_002 | cust\_004 | BuildRight LLC | orders@buildright.com | 
| rep\_003 | cust\_005 | FastShip Co | support@fastship.com | 

## Order Table Design
<a name="order-table-design"></a>

The Order table uses vertical partitioning with separate items for order headers and order items. This design enables efficient product-based queries while maintaining all order components within the same partition for efficient access. Each order consists of multiple items:
+ *Order Header* - Contains order metadata with PK=order\_id, SK=order\_id
+ *Order Items* - Individual line items with PK=order\_id, SK=product\_id, enabling direct product queries

**Note**  
This vertical partitioning approach trades the simplicity of embedded order items for enhanced query flexibility. Each order item becomes a separate DynamoDB item, enabling efficient product-based queries while maintaining all order data within the same partition for efficient retrieval in a single request.

The table includes strategic denormalization of account\_rep\_id (duplicated from Customer table) to enable direct account representative queries without requiring customer lookups. For high-throughput write scenarios, OPEN orders include status and shard attributes to enable write sharding across multiple partitions.

Four GSIs support different query patterns with optimized projections:
+ *OrderByCustomerDate GSI* - Uses INCLUDE projection with order summary and item details to support customer order history with date range filtering
+ *OpenOrdersByDate GSI (Sparse, Sharded)* - Uses multi-attribute partition key (status \+ shard) with 5 shards to distribute 5,000 WPS (writes per second) across partitions (1,000 WPS each, matching DynamoDB's 1,000 WCU per partition limit). Only indexes OPEN orders (20% of total), which can help reduce GSI storage costs. Requires parallel queries across all 5 shards with client-side result merging
+ *OrderByAccountRep GSI* - Uses INCLUDE projection with order summary attributes to support account representative workflows without full order details
+ *ProductInOrders GSI* - Created from OrderItem records (PK=order\_id, SK=product\_id), this GSI enables queries to find all orders containing a specific product. Uses INCLUDE projection with order context (customer\_id, order\_date, quantity) for product demand analysis


**Order Table - Base Table Structure (Vertical Partitioning)**  

| PK | SK | customer\_id | order\_date | status | account\_rep\_id | quantity | price | shard | 
| --- | --- | --- | --- | --- | --- | --- | --- | --- | 
| ord\_001 | ord\_001 | cust\_001 | 2025-11-15 | CLOSED | rep\_001 |  |  |  | 
| ord\_001 | prod\_100 |  |  |  |  | 5 | 25.00 |  | 
| ord\_002 | ord\_002 | cust\_001 | 2025-12-20 | OPEN | rep\_001 |  |  | 0 | 
| ord\_002 | prod\_101 |  |  |  |  | 10 | 15.00 |  | 
| ord\_003 | ord\_003 | cust\_002 | 2026-01-05 | OPEN | rep\_001 |  |  | 2 | 
| ord\_003 | prod\_100 |  |  |  |  | 3 | 25.00 |  | 


**OrderByCustomerDate GSI - Supporting Customer Order Queries**  

| customer\_id (GSI-PK) | order\_date (GSI-SK) | order\_id | status | total\_amount | order\_items | shard | 
| --- | --- | --- | --- | --- | --- | --- | 
| cust\_001 | 2025-11-15 | ord\_001 | CLOSED | 225.00 | [{product\_id: "prod\_100", qty: 5}] |  | 
| cust\_001 | 2025-12-20 | ord\_002 | OPEN | 150.00 | [{product\_id: "prod\_101", qty: 10}] | 0 | 
| cust\_002 | 2026-01-05 | ord\_003 | OPEN | 175.00 | [{product\_id: "prod\_100", qty: 3}] | 2 | 
| cust\_003 | 2025-10-10 | ord\_004 | CLOSED | 250.00 | [{product\_id: "prod\_101", qty: 5}] |  | 
| cust\_004 | 2026-01-03 | ord\_005 | OPEN | 200.00 | [{product\_id: "prod\_100", qty: 20}] | 1 | 


**OpenOrdersByDate GSI (Sparse, Sharded) - Supporting High-Throughput Open Order Queries**  

| status (GSI-PK-1) | shard (GSI-PK-2) | order\_date (SK) | order\_id | customer\_id | account\_rep\_id | order\_items | total\_amount | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
| OPEN | 0 | 2025-12-20 | ord\_002 | cust\_001 | rep\_001 | [{product\_id: "prod\_101", qty: 10}] | 150.00 | 
| OPEN | 1 | 2026-01-03 | ord\_005 | cust\_004 | rep\_002 | [{product\_id: "prod\_100", qty: 20}] | 200.00 | 
| OPEN | 2 | 2026-01-05 | ord\_003 | cust\_002 | rep\_001 | [{product\_id: "prod\_100", qty: 3}] | 175.00 | 


**OrderByAccountRep GSI - Supporting Account Rep Order Queries**  

| account\_rep\_id (GSI-PK) | order\_date (GSI-SK) | order\_id | customer\_id | status | total\_amount | 
| --- | --- | --- | --- | --- | --- | 
| rep\_001 | 2025-11-15 | ord\_001 | cust\_001 | CLOSED | 225.00 | 
| rep\_001 | 2025-12-20 | ord\_002 | cust\_001 | OPEN | 150.00 | 
| rep\_001 | 2026-01-05 | ord\_003 | cust\_002 | OPEN | 175.00 | 
| rep\_002 | 2025-10-10 | ord\_004 | cust\_003 | CLOSED | 250.00 | 
| rep\_002 | 2026-01-03 | ord\_005 | cust\_004 | OPEN | 200.00 | 


**ProductInOrders GSI - Supporting Product Order Queries**  

| product\_id (GSI-PK) | order\_id (GSI-SK) | customer\_id | order\_date | quantity | 
| --- | --- | --- | --- | --- | 
| prod\_100 | ord\_001 | cust\_001 | 2025-11-15 | 5 | 
| prod\_100 | ord\_003 | cust\_002 | 2026-01-05 | 3 | 
| prod\_101 | ord\_002 | cust\_001 | 2025-12-20 | 10 | 

## Product Table Design
<a name="product-table-design"></a>

The Product table uses the item collection pattern to store both product metadata and inventory data within the same partition. This design leverages the identifying relationship between products and inventory - inventory cannot exist without a parent product. Using PK=product\_id with SK=product\_id for product metadata and SK=warehouse\_id for inventory items eliminates the need for a separate Inventory table and GSI, reducing costs by approximately 50%.

This pattern enables efficient queries for both individual warehouse inventory (GetItem with composite key) and all warehouse inventory for a product (Query on partition key). The total\_inventory attribute in the product metadata item provides denormalized aggregation for quick total inventory lookups.


**Product Table - Base Table Structure (Item Collection Pattern)**  

| product\_id (PK) | warehouse\_id (SK) | product\_name | category | unit\_price | inventory\_quantity | total\_inventory | 
| --- | --- | --- | --- | --- | --- | --- | 
| prod\_100 | prod\_100 | Widget A | Hardware | 25.00 |  | 500 | 
| prod\_100 | wh\_sea |  |  |  | 200 |  | 
| prod\_100 | wh\_pdx |  |  |  | 150 |  | 
| prod\_100 | wh\_atl |  |  |  | 150 |  | 
| prod\_101 | prod\_101 | Gadget B | Electronics | 50.00 |  | 300 | 
| prod\_101 | wh\_sea |  |  |  | 100 |  | 
| prod\_101 | wh\_pdx |  |  |  | 200 |  | 

Each table is designed with specific Global Secondary Indexes (GSIs) to support the required access patterns efficiently. The design uses aggregate-oriented principles with strategic denormalization and sparse indexing to optimize both performance and cost.

Key design optimizations include:
+ *Sparse GSI* - OpenOrdersByDate only indexes OPEN orders (20% of total), which can help reduce GSI storage costs
+ *Item Collection Pattern* - Product table stores inventory using PK=product\_id, SK=warehouse\_id to eliminate separate inventory table
+ *Order \+ OrderItems Aggregation* - Embedded as single item due to 100% access correlation
+ *Strategic Denormalization* - account\_rep\_id duplicated in Order table for efficient queries

Finally, you can revisit the access patterns that were defined earlier. The following table shows how each access pattern is efficiently supported using the multi-table design with strategic GSIs. Each pattern uses either direct key lookups or single GSI queries, avoiding expensive scans and providing consistent performance at any scale.


| S. No. | Access patterns | Query conditions | 
| --- | --- | --- | 
| 1 | Look up Employee Details by Employee ID | Employee Table: GetItem(employee\_id="emp\_001") | 
| 2 | Query Employee Details by Employee Name | EmployeeByName GSI: Query(name="John Smith") | 
| 3 | Find an Employee's Phone Number(s) | Employee Table: GetItem(employee\_id="emp\_001") | 
| 4 | Find a Customer's Phone Number(s) | Customer Table: GetItem(customer\_id="cust\_001") | 
| 5 | Get Orders for Customer within Date Range | OrderByCustomerDate GSI: Query(customer\_id="cust\_001", order\_date BETWEEN "2025-01-01" AND "2025-12-31") | 
| 6 | Show all Open Orders within Date Range | OpenOrdersByDate GSI: Query 5 shards in parallel with multi-attribute PK (status="OPEN" \+ shard=0-4), SK=order\_date BETWEEN "2025-01-01" AND "2025-12-31", merge results | 
| 7 | See all Employees hired recently | EmployeeByHireDate GSI: Query(entity\_type="EMPLOYEE", hire\_date >= "2025-01-01") | 
| 8 | Find all Employees in Warehouse | EmployeeByWarehouse GSI: Query(warehouse\_id="wh\_sea") | 
| 9 | Get all Items on Order for Product | ProductInOrders GSI: Query(product\_id="prod\_100") | 
| 10 | Get Inventories for Product at all Warehouses | Product Table: Query(product\_id="prod\_100") | 
| 11 | Get Customers by Account Rep | CustomerByAccountRep GSI: Query(account\_rep\_id="rep\_001") | 
| 12 | Get Orders by Account Rep | OrderByAccountRep GSI: Query(account\_rep\_id="rep\_001") | 
| 13 | Get Employees with Job Title | EmployeeByJobTitle GSI: Query(job\_title="Manager") | 
| 14 | Get Inventory by Product and Warehouse | Product Table: GetItem(product\_id="prod\_100", warehouse\_id="wh\_sea") | 
| 15 | Get Total Product Inventory | Product Table: GetItem(product\_id="prod\_100", warehouse\_id="prod\_100") | 