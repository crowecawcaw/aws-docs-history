# work_order_plan

**Primary key (PK)**

The table below lists the column names that are uniquely identified in the data
entity.

| Name            | Column                                                                    |
| --------------- | ------------------------------------------------------------------------- |
| work_order_plan | process_id, product_id, business_process_id,<br>business_process_sequence |

The table below lists the column names supported by the data entity:

| Column                    | Data type | Required | Description                                                                                                                                                                                         |
| ------------------------- | --------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| process_id1               | string    | Yes      | Process ID. For example, order, work order, maintenance order, or process inquiry.                                                                                                                  |
| process_product_id        | string    | No       | ID associated with the process and product.                                                                                                                                                         |
| preferred_source          | string    | No       | Describes if the product is sourced from inventory (that is,<br>stocked to forecasted) or from direct purchase (for non-stocked<br>products).                                                       |
| product_id                | string    | Yes      | Product ID (material) in the work order.                                                                                                                                                            |
| business_process_id       | string    | Yes      | Business process identifier. For example, PO, PR, RFQ and so<br>on. Product ID (material) in the work order. The plan should<br>include both the purchasing and distribution business<br>processes. |
| site_id                   | string    | No       | The site linked to the business process. This field is<br>optional for purchasing process and mandatory for distribution<br>related processes.                                                      |
| business_process_sequence | int       | Yes      | Business process sequence.                                                                                                                                                                          |
| duration                  | int       | Yes      | Unit in days.                                                                                                                                                                                       |
| notes                     | string    | No       | Additional notes on work order plan.                                                                                                                                                                |
| flex_1                    | string    | No       | Plan flexible field 1.                                                                                                                                                                              |
| flex_2                    | string    | No       | Plan flexible field 2.                                                                                                                                                                              |
| flex_3                    | string    | No       | Plan flexible field 3.                                                                                                                                                                              |
| flex_4                    | string    | No       | Plan flexible field 4.                                                                                                                                                                              |
| flex_5                    | string    | No       | Plan flexible field 5.                                                                                                                                                                              |
| source_event_id           | string    | No       | ID of the event created in the source system.                                                                                                                                                       |
| source_update_dttm        | timestamp | No       | Date time stamp of the update made in the source<br>system.                                                                                                                                         |

1Foreign key

**Foreign key (FK)**

The table below lists the columns with the associated foreign key.

| Column     | Category | FK/Data entity | FK/Column |
| ---------- | -------- | -------------- | --------- |
| process_id | Insights | process_header | id        |
