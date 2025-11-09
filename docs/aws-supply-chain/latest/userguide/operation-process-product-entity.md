# process_product

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name            | Column                         |
| --------------- | ------------------------------ |
| process_product | process_product_id, process_id |

The table below lists the column names supported by the data entity:

| Column                      | Data type | Required | Description                                                                        |
| --------------------------- | --------- | -------- | ---------------------------------------------------------------------------------- |
| process_product_id1         | string    | Yes      | ID associated with the process and product.                                        |
| process_id1                 | string    | Yes      | Process ID. For example, order, work order, maintenance order, or process inquiry. |
| process_operation_id1       | string    | No       | Process operational ID. This is an optional field.                                 |
| company_id1                 | string    | No       | Company ID.                                                                        |
| product_id1                 | string    | No       | Product ID of the requested product.                                               |
| type                        | string    | No       | Type associated within the process. For example, consumption or production.        |
| product_value               | double    | No       | Monetary value of product being requested.                                         |
| currency_uom                | string    | No       | Currency UOM of the product.                                                       |
| status                      | string    | No       | Status of the product process.                                                     |
| requested_availability_date | timestamp | No       | Date when the material was requested to be available.                              |
| quantity_submitted          | double    | No       | Quantity submitted as part of the process for product.                             |
| quantity_confirmed          | double    | No       | Quantity confirmed against the request.                                            |
| quantity_consumed           | double    | No       | Quantity consumed against the quantity on this process/work order.                 |
| reservation_id1             | string    | No       | Link to reservation ID associated with this record.                                |
| reservation_detail_id1      | string    | No       | Link to reservation detail ID associated with this record.                         |
| quantity_uom                | string    | No       | Unit of measure for quantity.                                                      |
| process_product_url         | string    | No       | URL to access process product record in source system.                             |
| source_update_dttm          | timestamp | No       | Date time stamp of the update made in the source system.                           |
| source_event_id             | string    | No       | ID of the event created in the source system.                                      |
| allocation_status           | string    | No       | Status of the allocation for the product.                                          |
| allocation_type             | string    | No       | Type of allocation for the product.                                                |
| flex_1                      | string    | No       | Process flexible field 1.                                                          |
| flex_2                      | string    | No       | Process flexible field 2.                                                          |
| flex_3                      | string    | No       | Process flexible field 3.                                                          |
| flex_4                      | string    | No       | Process flexible field 4.                                                          |
| flex_5                      | string    | No       | Process flexible field 5.                                                          |
| reservation_type            | string    | No       | Type of reservation of the product.                                                |

1Foreign key

**Foreign key (FK)**

The table below lists the columns with the associated foreign key.

| Column                | Category     | FK/Data entity    | FK/Column name        |
| --------------------- | ------------ | ----------------- | --------------------- |
| product_id            | Product      | product           | id                    |
| company_id            | Organization | company           | id                    |
| process_id            | Operation    | process_header    | process_id            |
| process_operation_id  | Operation    | process_operation | process_operation_id  |
| reservation_id        | Planning     | reservation       | reservation_id        |
| reservation_detail_id | Planning     | reservation       | reservation_detail_id |
