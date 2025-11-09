# reservation

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name        | Column                                |
| ----------- | ------------------------------------- |
| reservation | reservation_id, reservation_detail_id |

The table below lists the column names supported by the _reservation_ data entity:

| Column                         | Data type | Required | Description                                                                |
| ------------------------------ | --------- | -------- | -------------------------------------------------------------------------- |
| reservation_id                 | string    | Yes      | Reservation ID.                                                            |
| reservation_detail_id          | string    | Yes      | Reservation detail ID.                                                     |
| reservation_type               | string    | No       | Type of reservation. For example, procurement or build-to-stock.           |
| company_id1                    | string    | No       | Company ID.                                                                |
| status                         | string    | No       | Status of the reservation.                                                 |
| product_id1                    | string    | No       | Product ID.                                                                |
| site_id1                       | string    | No       | Site ID.                                                                   |
| quantity                       | double    | No       | Reservation quantity.                                                      |
| quantity_uom                   | string    | No       | Quantity UOM associated with reservation.                                  |
| reservation_date               | timestamp | No       | Date when the reservation is generated.                                    |
| is_deleted                     | string    | No       | Yes or No indicator to indicate whether the reservation is deleted or not. |
| requisition_id1                | string    | No       | Source object identifier reference to inbound order type.                  |
| requisition_line_id1           | string    | No       | Source object identifier reference to inbound order line.                  |
| rfq_id1                        | string    | No       | Source object identifier reference to inbound order type RFQ.              |
| rfq_line_id1                   | string    | No       | Source object identifier reference to inbound order line of type RFQ.      |
| order_id1                      | string    | No       | Source object identifier reference to inbound order.                       |
| order_line_id1                 | string    | No       | Source object identifier reference to inbound order line.                  |
| order_line_schedule_id1        | string    | No       | Source object identifier reference to inbound order line schedule.         |
| stock_transfer_1_order_id      | string    | No       | Stock transfer order ID.                                                   |
| stock_transfer_1_order_line_id | string    | No       | Stock transfer order line ID.                                              |
| stock_transfer_2_order_id      | string    | No       | Stock transfer order ID.                                                   |
| stock_transfer_2_order_line_id | string    | No       | Stock transfer order line ID.                                              |
| source_update_dttm             | timestamp | No       | Date time stamp of the update made in the source system.                   |
| source_event_id                | string    | No       | ID of the event created in the source system.                              |
| source                         | string    | No       | Source of data.                                                            |
| flex_1                         | string    | No       | Reservation flexible field 1                                               |
| flex_2                         | string    | No       | Reservation flexible field 2                                               |
| flex_3                         | string    | No       | Reservation flexible field 3                                               |
| flex_4                         | string    | No       | Reservation flexible field 4                                               |
| flex_5                         | string    | No       | Reservation flexible field 5                                               |

1Foreign key

**Foreign key (FK)**

The table below lists the column names with the associated data entity and category:

| Column                           | Category     | FK/Data entity              | FK/Column |
| -------------------------------- | ------------ | --------------------------- | --------- |
| site_id                          | Network      | site                        | id        |
| company_id                       | Organization | company                     | id        |
| product_id                       | Product      | product                     | id        |
| requisition_id, rfq_id           | Inbound      | inbound_order_line          | order_id  |
| requisition_line_id, rfq_line_id | Inbound      | inbound_order_line          | id        |
| order_line_schedule_id           | Inbound      | inbound_order_line_schedule | id        |
