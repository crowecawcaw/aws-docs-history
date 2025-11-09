# shipment_lot

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name         | Column                                                                        |
| ------------ | ----------------------------------------------------------------------------- |
| shipment_lot | id, product_id, tpartner_id, order_id, shipment_id, order_line_id, package_id |

The table below lists the column names supported by the data entity:

| Column             | Data type | Required | Description                                                                                                                                                                     |
| ------------------ | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id                 | string    | Yes      | Shipment ID. Unique shipment identifier.                                                                                                                                        |
| product_id2        | string    | Yes      | Product ID. Unique product identifier.                                                                                                                                          |
| serial_number      | string    | No       | Unique serial number assigned to the lot. Serial numbers are often used for tracking and traceability purposes, particularly in industries where lot-level tracking is crucial. |
| lot_qty            | double    | Yes      | Quantity or number of units within the specific lot. It allows you to track the size or volume of each lot.                                                                     |
| mfg_date           | timestamp | No       | Manufacturing date.                                                                                                                                                             |
| expiry_date        | timestamp | No       | Expiry date.                                                                                                                                                                    |
| tpartner_id2       | string    | No1      | Partner that is sending the shipment. For example, shipments generated under POs, this will be vendors.                                                                         |
| order_id           | string    | No1      | Order ID.                                                                                                                                                                       |
| shipment_id2       | string    | Yes1     | Shipment ID. Unique shipment identifier.                                                                                                                                        |
| order_line_id2     | string    | No1      | Order line ID.                                                                                                                                                                  |
| package_id2        | string    | No1      | Package ID. One shipment can have multiple packages in EDI.                                                                                                                     |
| source_event_id    | string    | No       | ID of the event created in the source system.                                                                                                                                   |
| source_update_dttm | timestamp | No       | Date timestamp of the update made in the source system.                                                                                                                         |

1You must enter a value. When you ingest data from SAP
or EDI, the default value for _string_ is SCN_RESERVED_NO_VALUE_PROVIDED.

2Foreign key

1Foreign key

**Foreign key (FK)**

The table below lists the columns with the associated foreign key.

| Column        | Category | FK/Data entity | FK/Column            |
| ------------- | -------- | -------------- | -------------------- |
| product_id    | Inbound  | shipment       | product_id           |
| tpartner_id   | Inbound  | shipment       | supplier_tpartner_id |
| order_id      | Inbound  | shipment       | order_id             |
| shipment_id   | Inbound  | shipment       | id                   |
| order_line_id | Inbound  | shipment       | order_line_id        |
| package_id    | Inbound  | shipment       | package_id           |
