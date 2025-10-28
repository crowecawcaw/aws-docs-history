# shipment_stop_order

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name                            | Column                                                |
| ------------------------------- | ----------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| shipment_stop_order             | shipment_stop_order_id, shipment_stop_id, shipment_id | The table below lists the column names supported by the data entity: |
| Column                          | Data type                                             | Required                                                             | Description                                              |
| ---                             | ---                                                   | ---                                                                  | ---                                                      |
| shipment_stop_order_id          | string                                                | Yes                                                                  | Shipment stop order ID.                                  |
| shipment_stop_id1               | string                                                | Yes                                                                  | Shipment stop ID.                                        |
| shipment_id1                    | string                                                | Yes                                                                  | Shipment ID.                                             |
| company_id1                     | string                                                | No                                                                   | Company ID.                                              |
| site_id1                        | string                                                | No                                                                   | Site ID.                                                 |
| inbound_order_id1               | string                                                | No                                                                   | Inbound order ID.                                        |
| inbound_order_line_id1          | string                                                | No                                                                   | Inbound order line ID.                                   |
| inbound_order_line_schedule_id1 | string                                                | No                                                                   | Inbound order line schedule ID.                          |
| action                          | string                                                | No                                                                   | Pickup or drop off shipment.                             |
| quantity                        | double                                                | No                                                                   | Quantity associated with action and order.               |
| quantity_uom                    | string                                                | No                                                                   | Quantity UOM of the shipment.                            |
| source_event_id                 | string                                                | No                                                                   | ID of the event created in the source system.            |
| source_update_dttm              | timestamp                                             | No                                                                   | Date time stamp of the update made in the source system. | 1Foreign key **Foreign key (FK)** The table below lists the columns with the associated foreign key. |
| Column                          | Category                                              | FK/Data entity                                                       | FK/Column                                                |
| ---                             | ---                                                   | ---                                                                  | ---                                                      |
| company_id                      | Organization                                          | company                                                              | id                                                       |
| site_id                         | Network                                               | site                                                                 | id                                                       |
| shipment_id                     | Inbound                                               | shipment                                                             | id                                                       |
| shipment_stop_id                | Inbound                                               | shipment_stop                                                        | shipment_stop_id                                         |
| inbound_order_id                | Inbound                                               | inbound_order_line                                                   | order_id                                                 |
| inbound_order_line_id           | Inbound                                               | inbound_order_line                                                   | id                                                       |
| inbound_order_line_schedule_id  | Inbound                                               | inbound_order_line_schedule                                          | id                                                       |
