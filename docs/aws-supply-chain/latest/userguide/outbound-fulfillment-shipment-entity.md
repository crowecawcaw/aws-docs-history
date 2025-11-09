# outbound_shipment

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name              | Column                                            |
| ----------------- | ------------------------------------------------- |
| outbound_shipment | id, cust_order_id, cust_order_line_id, product_id |

The table below lists the column names supported by the data entity:

| Column                    | Data type | Required | Description                                                                                                       |
| ------------------------- | --------- | -------- | ----------------------------------------------------------------------------------------------------------------- |
| id                        | string    | Yes 1    | Outbound shipment ID.                                                                                             |
| company_id2               | string    | No       | Company ID.                                                                                                       |
| cust_order_id2            | string    | Yes 1    | Customer order ID.                                                                                                |
| cust_order_line_id2       | string    | Yes 1    | Customer<br>order line ID.                                                                                        |
| product_id2               | string    | Yes 1    | Product ID.                                                                                                       |
| shipped_qty               | double    | No       | Shipment quantity.                                                                                                |
| cust_shipment_status      | string    | No       | Status of the shipment, for example, canceled, open, closed,<br>or delivered.                                     |
| expected_ship_date        | timestamp | No       | Date product was expected to ship from the company<br>location.                                                   |
| actual_ship_date          | timestamp | No       | Date product was actually shipped from the company<br>location.                                                   |
| from_site_id2             | string    | No       | Site ID where the product is shipped from.                                                                        |
| to_site_id2               | string    | No       | Destination site ID for outbound shipments.                                                                       |
| expected_delivery_date    | timestamp | No       | Expected delivery date of the products to the customer.                                                           |
| actual_delivery_date      | timestamp | No       | Displays when the product was actually delivered to the<br>customer.                                              |
| shipping_cost             | double    | No       | Final shipping cost.                                                                                              |
| tracking_number           | string    | No       | Tracking number associated with the shipment.                                                                     |
| bill_weight               | double    | No       | Shipped weight of product used for billing.                                                                       |
| sap_2lis_08trtlp\_\_vbeln | string    | No       | Delivery number. Predicate key for SAP mapping. Upsert key for 2LIS_12_VCITM.                                     |
| sap_2lis_08trtlp\_\_posnr | string    | No       | Delivery item number. Predicate key for SAP mapping. Upsert key for 2LIS_12_VCITM.                                |
| sap_2lis_08trtlp\_\_tknum | string    | No       | Shipment item number. Predicate key for SAP mapping. Upsert key for 2LIS_08TRTK.                                  |
| source                    | string    | No       | Source of data.                                                                                                   |
| source_event_id           | string    | No       | ID of the event created in the source system.                                                                     |
| source_update_dttm        | timestamp | No       | Date time stamp of the update made in the source<br>system.                                                       |
| tpartner_id               | string    | No       | Unique identifier for a trading partner.                                                                          |
| service_level             | string    | No       | Focuses on the quality and speed of the shipment. For example, Standard, next day, two-day, expedited, and so on. |

1You must enter a value. When you ingest data from SAP
or EDI, the default value for _string_ is SCN_RESERVED_NO\_
VALUE_PROVIDED.

2Foreign key

**Foreign key (FK)**

The table below lists the column names with the associated data entity and category:

| Column                   | Category            | FK/Data entity      | FK/Column     |
| ------------------------ | ------------------- | ------------------- | ------------- |
| company_id               | Organization        | company             | id            |
| product_id               | Product             | product             | id            |
| cust_order_line_id       | OutboundFulfillment | outbound_order_line | id            |
| cust_order_id            | OutboundFulfillment | outbound_order_line | cust_order_id |
| from_site_id, to_site_id | Network             | site                | id            |
| tpartner_id              | Organization        | trading_partner     | id            |
