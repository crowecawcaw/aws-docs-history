# Example of modeling relational data in DynamoDB

This example describes how to model relational data in Amazon DynamoDB. The DynamoDB table design
corresponds to the relational order entry schema that is shown in [Relational modeling](bp-relational-modeling.md "bp-relational-modeling.md"). This design
uses multiple specialized tables rather than a single adjacency list, providing clear operational
boundaries while leveraging strategic GSIs to serve all access patterns efficiently.

The design approach uses aggregate-oriented principles, grouping data based on access patterns
rather than rigid entity boundaries. Key design decisions include using separate tables for entities
with low access correlation, embedding related data when always accessed together, and using
item collections for identifying relationships.

The following tables and their accompanying indexes support the relational order entry schema:

## Employee Table Design

The Employee table stores employee information as a single entity per item, optimized for direct employee lookups and supporting multiple query patterns through strategic GSIs. This table demonstrates the principle of designing separate tables for entities with independent operational characteristics and low cross-entity access correlation.

The table uses a simple partition key (employee_id) without a sort key, as each employee is a distinct entity. Four GSIs enable efficient querying by different attributes:

- _EmployeeByName GSI_ - Uses INCLUDE projection with all employee attributes to support complete employee detail retrieval by name, handling potential duplicate names with employee_id as sort key
- _EmployeeByWarehouse GSI_ - Uses INCLUDE projection with only essential attributes (name, job_title, hire_date) to minimize storage costs while supporting warehouse-based queries
- _EmployeeByJobTitle GSI_ - Enables role-based queries with INCLUDE projection for reporting and organizational analysis
- _EmployeeByHireDate GSI_ - Uses a static partition key value "EMPLOYEE" with hire_date as sort key to enable efficient date range queries for recent hires. Since employee additions/updates are typically under 1,000 WCU, a single partition can handle the write load without hot partition issues

| Employee Table - Base Table Structure | employee_id (PK) | name                           | phone_numbers | warehouse_id | job_title  | hire_date | entity_type |
| ------------------------------------- | ---------------- | ------------------------------ | ------------- | ------------ | ---------- | --------- | ----------- |
| emp_001                               | John Smith       | ["+1-555-0101"]                | wh_sea        | Manager      | 2024-03-15 | EMPLOYEE  |
| emp_002                               | Jane Doe         | ["+1-555-0102", "+1-555-0103"] | wh_sea        | Associate    | 2025-01-10 | EMPLOYEE  |
| emp_003                               | Bob Wilson       | ["+1-555-0104"]                | wh_pdx        | Associate    | 2025-06-20 | EMPLOYEE  |
| emp_004                               | Alice Brown      | ["+1-555-0105"]                | wh_pdx        | Supervisor   | 2023-11-05 | EMPLOYEE  |
| emp_005                               | Charlie Davis    | ["+1-555-0106"]                | wh_sea        | Associate    | 2025-12-01 | EMPLOYEE  |

| EmployeeByName GSI - Supporting Employee Name Queries | name (GSI-PK) | employee_id (GSI-SK)           | phone_numbers | warehouse_id | job_title  | hire_date |
| ----------------------------------------------------- | ------------- | ------------------------------ | ------------- | ------------ | ---------- | --------- |
| Alice Brown                                           | emp_004       | ["+1-555-0105"]                | wh_pdx        | Supervisor   | 2023-11-05 |
| Bob Wilson                                            | emp_003       | ["+1-555-0104"]                | wh_pdx        | Associate    | 2025-06-20 |
| Charlie Davis                                         | emp_005       | ["+1-555-0106"]                | wh_sea        | Associate    | 2025-12-01 |
| Jane Doe                                              | emp_002       | ["+1-555-0102", "+1-555-0103"] | wh_sea        | Associate    | 2025-01-10 |
| John Smith                                            | emp_001       | ["+1-555-0101"]                | wh_sea        | Manager      | 2024-03-15 |

| EmployeeByWarehouse GSI - Supporting Warehouse Queries | warehouse_id (GSI-PK) | employee_id (GSI-SK) | name       | job_title  | hire_date |
| ------------------------------------------------------ | --------------------- | -------------------- | ---------- | ---------- | --------- |
| wh_pdx                                                 | emp_003               | Bob Wilson           | Associate  | 2025-06-20 |
| wh_pdx                                                 | emp_004               | Alice Brown          | Supervisor | 2023-11-05 |
| wh_sea                                                 | emp_001               | John Smith           | Manager    | 2024-03-15 |
| wh_sea                                                 | emp_002               | Jane Doe             | Associate  | 2025-01-10 |
| wh_sea                                                 | emp_005               | Charlie Davis        | Associate  | 2025-12-01 |

| EmployeeByJobTitle GSI - Supporting Job Title Queries | job_title (GSI-PK) | employee_id (GSI-SK) | name   | warehouse_id | hire_date |
| ----------------------------------------------------- | ------------------ | -------------------- | ------ | ------------ | --------- |
| Associate                                             | emp_002            | Jane Doe             | wh_sea | 2025-01-10   |
| Associate                                             | emp_003            | Bob Wilson           | wh_pdx | 2025-06-20   |
| Associate                                             | emp_005            | Charlie Davis        | wh_sea | 2025-12-01   |
| Manager                                               | emp_001            | John Smith           | wh_sea | 2024-03-15   |
| Supervisor                                            | emp_004            | Alice Brown          | wh_pdx | 2023-11-05   |

| EmployeeByHireDate GSI - Supporting Recent Hire Queries | entity_type (GSI-PK) | hire_date (GSI-SK) | employee_id   | name   | warehouse_id |
| ------------------------------------------------------- | -------------------- | ------------------ | ------------- | ------ | ------------ |
| EMPLOYEE                                                | 2023-11-05           | emp_004            | Alice Brown   | wh_pdx |
| EMPLOYEE                                                | 2024-03-15           | emp_001            | John Smith    | wh_sea |
| EMPLOYEE                                                | 2025-01-10           | emp_002            | Jane Doe      | wh_sea |
| EMPLOYEE                                                | 2025-06-20           | emp_003            | Bob Wilson    | wh_pdx |
| EMPLOYEE                                                | 2025-12-01           | emp_005            | Charlie Davis | wh_sea |

## Customer Table Design

The Customer table maintains customer information with strategic denormalization of account_rep_id to enable efficient account representative queries. This design choice trades slight storage overhead for query performance, eliminating the need for joins between customer and account representative data.

The table supports multiple phone numbers per customer using a list attribute, demonstrating DynamoDB's schema flexibility. The single GSI enables account representative workflows:

- _CustomerByAccountRep GSI_ - Uses INCLUDE projection with name and email attributes to support account rep customer management without requiring full customer record retrieval

| Customer Table - Base Table Structure | customer_id (PK) | name                           | phone_numbers           | email   | account_rep_id |
| ------------------------------------- | ---------------- | ------------------------------ | ----------------------- | ------- | -------------- |
| cust_001                              | Acme Corp        | ["+1-555-1001"]                | contact@acme.com        | rep_001 |
| cust_002                              | TechStart Inc    | ["+1-555-1002", "+1-555-1003"] | info@techstart.com      | rep_001 |
| cust_003                              | Global Traders   | ["+1-555-1004"]                | sales@globaltraders.com | rep_002 |
| cust_004                              | BuildRight LLC   | ["+1-555-1005"]                | orders@buildright.com   | rep_002 |
| cust_005                              | FastShip Co      | ["+1-555-1006"]                | support@fastship.com    | rep_003 |

| CustomerByAccountRep GSI - Supporting Account Rep Queries | account_rep_id (GSI-PK) | customer_id (GSI-SK) | name                    | email |
| --------------------------------------------------------- | ----------------------- | -------------------- | ----------------------- | ----- |
| rep_001                                                   | cust_001                | Acme Corp            | contact@acme.com        |
| rep_001                                                   | cust_002                | TechStart Inc        | info@techstart.com      |
| rep_002                                                   | cust_003                | Global Traders       | sales@globaltraders.com |
| rep_002                                                   | cust_004                | BuildRight LLC       | orders@buildright.com   |
| rep_003                                                   | cust_005                | FastShip Co          | support@fastship.com    |

## Order Table Design

The Order table uses vertical partitioning with separate items for order headers and order items. This design enables efficient product-based queries while maintaining all order components within the same partition for efficient access. Each order consists of multiple items:

- _Order Header_ - Contains order metadata with PK=order_id, SK=order_id
- _Order Items_ - Individual line items with PK=order_id, SK=product_id, enabling direct product queries

###### Note

This vertical partitioning approach trades the simplicity of embedded order items for enhanced query flexibility. Each order item becomes a separate DynamoDB item, enabling efficient product-based queries while maintaining all order data within the same partition for efficient retrieval in a single request.

The table includes strategic denormalization of account_rep_id (duplicated from Customer table) to enable direct account representative queries without requiring customer lookups. For high-throughput write scenarios, OPEN orders include status and shard attributes to enable write sharding across multiple partitions.

Four GSIs support different query patterns with optimized projections:

- _OrderByCustomerDate GSI_ - Uses INCLUDE projection with order summary and item details to support customer order history with date range filtering
- _OpenOrdersByDate GSI (Sparse, Sharded)_ - Uses multi-attribute partition key (status + shard) with 5 shards to distribute 5,000 WPS (writes per second) across partitions (1,000 WPS each, matching DynamoDB's 1,000 WCU per partition limit). Only indexes OPEN orders (20% of total), which can help reduce GSI storage costs. Requires parallel queries across all 5 shards with client-side result merging
- _OrderByAccountRep GSI_ - Uses INCLUDE projection with order summary attributes to support account representative workflows without full order details
- _ProductInOrders GSI_ - Created from OrderItem records (PK=order_id, SK=product_id), this GSI enables queries to find all orders containing a specific product. Uses INCLUDE projection with order context (customer_id, order_date, quantity) for product demand analysis

| Order Table - Base Table Structure (Vertical Partitioning) | PK       | SK       | customer_id | order_date | status  | account_rep_id | quantity | price | shard |
| ---------------------------------------------------------- | -------- | -------- | ----------- | ---------- | ------- | -------------- | -------- | ----- | ----- |
| ord_001                                                    | ord_001  | cust_001 | 2025-11-15  | CLOSED     | rep_001 |                |          |       |
| ord_001                                                    | prod_100 |          |             |            |         | 5              | 25.00    |       |
| ord_002                                                    | ord_002  | cust_001 | 2025-12-20  | OPEN       | rep_001 |                |          | 0     |
| ord_002                                                    | prod_101 |          |             |            |         | 10             | 15.00    |       |
| ord_003                                                    | ord_003  | cust_002 | 2026-01-05  | OPEN       | rep_001 |                |          | 2     |
| ord_003                                                    | prod_100 |          |             |            |         | 3              | 25.00    |       |

| OrderByCustomerDate GSI - Supporting Customer Order Queries | customer_id (GSI-PK) | order_date (GSI-SK) | order_id | status | total_amount                          | order_items | shard |
| ----------------------------------------------------------- | -------------------- | ------------------- | -------- | ------ | ------------------------------------- | ----------- | ----- |
| cust_001                                                    | 2025-11-15           | ord_001             | CLOSED   | 225.00 | [{product\_id: "prod\_100", qty: 5}]  |             |
| cust_001                                                    | 2025-12-20           | ord_002             | OPEN     | 150.00 | [{product\_id: "prod\_101", qty: 10}] | 0           |
| cust_002                                                    | 2026-01-05           | ord_003             | OPEN     | 175.00 | [{product\_id: "prod\_100", qty: 3}]  | 2           |
| cust_003                                                    | 2025-10-10           | ord_004             | CLOSED   | 250.00 | [{product\_id: "prod\_101", qty: 5}]  |             |
| cust_004                                                    | 2026-01-03           | ord_005             | OPEN     | 200.00 | [{product\_id: "prod\_100", qty: 20}] | 1           |

| OpenOrdersByDate GSI (Sparse, Sharded) - Supporting High-Throughput Open Order Queries | status (GSI-PK-1) | shard (GSI-PK-2) | order_date (SK) | order_id | customer_id | account_rep_id                        | order_items | total_amount |
| -------------------------------------------------------------------------------------- | ----------------- | ---------------- | --------------- | -------- | ----------- | ------------------------------------- | ----------- | ------------ |
| OPEN                                                                                   | 0                 | 2025-12-20       | ord_002         | cust_001 | rep_001     | [{product\_id: "prod\_101", qty: 10}] | 150.00      |
| OPEN                                                                                   | 1                 | 2026-01-03       | ord_005         | cust_004 | rep_002     | [{product\_id: "prod\_100", qty: 20}] | 200.00      |
| OPEN                                                                                   | 2                 | 2026-01-05       | ord_003         | cust_002 | rep_001     | [{product\_id: "prod\_100", qty: 3}]  | 175.00      |

| OrderByAccountRep GSI - Supporting Account Rep Order Queries | account_rep_id (GSI-PK) | order_date (GSI-SK) | order_id | customer_id | status | total_amount |
| ------------------------------------------------------------ | ----------------------- | ------------------- | -------- | ----------- | ------ | ------------ |
| rep_001                                                      | 2025-11-15              | ord_001             | cust_001 | CLOSED      | 225.00 |
| rep_001                                                      | 2025-12-20              | ord_002             | cust_001 | OPEN        | 150.00 |
| rep_001                                                      | 2026-01-05              | ord_003             | cust_002 | OPEN        | 175.00 |
| rep_002                                                      | 2025-10-10              | ord_004             | cust_003 | CLOSED      | 250.00 |
| rep_002                                                      | 2026-01-03              | ord_005             | cust_004 | OPEN        | 200.00 |

| ProductInOrders GSI - Supporting Product Order Queries | product_id (GSI-PK) | order_id (GSI-SK) | customer_id | order_date | quantity |
| ------------------------------------------------------ | ------------------- | ----------------- | ----------- | ---------- | -------- |
| prod_100                                               | ord_001             | cust_001          | 2025-11-15  | 5          |
| prod_100                                               | ord_003             | cust_002          | 2026-01-05  | 3          |
| prod_101                                               | ord_002             | cust_001          | 2025-12-20  | 10         |

## Product Table Design

The Product table uses the item collection pattern to store both product metadata and inventory data within the same partition. This design leverages the identifying relationship between products and inventory - inventory cannot exist without a parent product. Using PK=product_id with SK=product_id for product metadata and SK=warehouse_id for inventory items eliminates the need for a separate Inventory table and GSI, reducing costs by approximately 50%.

This pattern enables efficient queries for both individual warehouse inventory (GetItem with composite key) and all warehouse inventory for a product (Query on partition key). The total_inventory attribute in the product metadata item provides denormalized aggregation for quick total inventory lookups.

| Product Table - Base Table Structure (Item Collection Pattern) | product_id (PK) | warehouse_id (SK) | product_name | category | unit_price | inventory_quantity | total_inventory |
| -------------------------------------------------------------- | --------------- | ----------------- | ------------ | -------- | ---------- | ------------------ | --------------- |
| prod_100                                                       | prod_100        | Widget A          | Hardware     | 25.00    |            | 500                |
| prod_100                                                       | wh_sea          |                   |              |          | 200        |                    |
| prod_100                                                       | wh_pdx          |                   |              |          | 150        |                    |
| prod_100                                                       | wh_atl          |                   |              |          | 150        |                    |
| prod_101                                                       | prod_101        | Gadget B          | Electronics  | 50.00    |            | 300                |
| prod_101                                                       | wh_sea          |                   |              |          | 100        |                    |
| prod_101                                                       | wh_pdx          |                   |              |          | 200        |                    |

Each table is designed with specific Global Secondary Indexes (GSIs) to support the required
access patterns efficiently. The design uses aggregate-oriented principles with strategic denormalization
and sparse indexing to optimize both performance and cost.

Key design optimizations include:

- _Sparse GSI_ - OpenOrdersByDate only indexes OPEN orders (20% of total), which can help reduce GSI storage costs
- _Item Collection Pattern_ - Product table stores inventory using PK=product_id, SK=warehouse_id to eliminate separate inventory table
- _Order + OrderItems Aggregation_ - Embedded as single item due to 100% access correlation
- _Strategic Denormalization_ - account_rep_id duplicated in Order table for efficient queries
  Finally, you can revisit the access patterns that were defined earlier. The following table shows
  how each access pattern is efficiently supported using the multi-table design with strategic GSIs.
  Each pattern uses either direct key lookups or single GSI queries, avoiding expensive scans and
  providing consistent performance at any scale.

| S. No. | Access patterns                               | Query conditions                                                                                                                                                         |
| ------ | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1      | Look up Employee Details by Employee ID       | Employee Table: GetItem(employee_id="emp_001")                                                                                                                           |
| 2      | Query Employee Details by Employee Name       | EmployeeByName GSI: Query(name="John Smith")                                                                                                                             |
| 3      | Find an Employee's Phone Number(s)            | Employee Table: GetItem(employee_id="emp_001")                                                                                                                           |
| 4      | Find a Customer's Phone Number(s)             | Customer Table: GetItem(customer_id="cust_001")                                                                                                                          |
| 5      | Get Orders for Customer within Date Range     | OrderByCustomerDate GSI: Query(customer_id="cust_001", order_date BETWEEN "2025-01-01" AND "2025-12-31")                                                                 |
| 6      | Show all Open Orders within Date Range        | OpenOrdersByDate GSI: Query 5 shards in parallel with multi-attribute PK (status="OPEN" + shard=0-4), SK=order_date BETWEEN "2025-01-01" AND "2025-12-31", merge results |
| 7      | See all Employees hired recently              | EmployeeByHireDate GSI: Query(entity_type="EMPLOYEE", hire_date >= "2025-01-01")                                                                                         |
| 8      | Find all Employees in Warehouse               | EmployeeByWarehouse GSI: Query(warehouse_id="wh_sea")                                                                                                                    |
| 9      | Get all Items on Order for Product            | ProductInOrders GSI: Query(product_id="prod_100")                                                                                                                        |
| 10     | Get Inventories for Product at all Warehouses | Product Table: Query(product_id="prod_100")                                                                                                                              |
| 11     | Get Customers by Account Rep                  | CustomerByAccountRep GSI: Query(account_rep_id="rep_001")                                                                                                                |
| 12     | Get Orders by Account Rep                     | OrderByAccountRep GSI: Query(account_rep_id="rep_001")                                                                                                                   |
| 13     | Get Employees with Job Title                  | EmployeeByJobTitle GSI: Query(job_title="Manager")                                                                                                                       |
| 14     | Get Inventory by Product and Warehouse        | Product Table: GetItem(product_id="prod_100", warehouse_id="wh_sea")                                                                                                     |
| 15     | Get Total Product Inventory                   | Product Table: GetItem(product_id="prod_100", warehouse_id="prod_100")                                                                                                   |
