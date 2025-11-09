# customer_cost

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name          | Column                 |
| ------------- | ---------------------- |
| customer_cost | cost_id, incurred_date |

The table below lists the column names supported by the data entity:

| Column             | Data type | Required | Description                                                                                                                                                  |
| ------------------ | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| cost_id            | string    | Yes1     | A unique identifier for each cost record associated with an user.                                                                                            |
| customer_id2       | string    | Yes      | The unique identifier for the user incurring the cost.                                                                                                       |
| incurred_date      | timestamp | Yes1     | The date and time when the cost was incurred. Displays the timestamp of cost.                                                                                |
| order_id2          | string    | No       | The unique identifier of the user order associated with the cost.                                                                                            |
| shipment_id2       | string    | No       | Unique identifier of the outbound shipment.                                                                                                                  |
| cost_type          | string    | No       | Displays the cost type. For example, handling, packing, storage, and shipping.                                                                               |
| amount             | double    | No       | The amount of cost incurred by the user.                                                                                                                     |
| amount_uom         | string    | No       | Unit of measure for the amount of cost incurred by the user.                                                                                                 |
| tax 1              | string    | No       | Tax amount incurred by the user.                                                                                                                             |
| tax 2              | string    | No       | Tax amount incurred by the user.                                                                                                                             |
| tax 3              | string    | No       | Tax amount incurred by the user.                                                                                                                             |
| tax_uom            | string    | No       | Unit of measure for the tax amount.                                                                                                                          |
| currency_uom       | string    | No       | Unit of measure for the currency.                                                                                                                            |
| payment_status     | string    | No       | The status of the payment. For example, Pending Paid.                                                                                                        |
| incoterm           | string    | No       | A set of internationally recognized rules which define the responsibilities of sellers and buyers in the export transaction. For example, FOB, ExWorks, DDP. |
| source             | string    | No       | Source of data.                                                                                                                                              |
| source_event_id    | string    | No       | ID of the event created in the source system. For example, PO receipt, Shipment schedule, and so on.                                                         |
| source_update_dttm | timestamp | No       | Date time stamp of the update made in the source<br>system.                                                                                                  |
| discount_1         | double    | No       | The discount associated for a specific cost ID.                                                                                                              |
| discount_2         | double    | No       | The additional discount associated for a specific cost ID.                                                                                                   |
| discount_3         | double    | No       | The additional discount associated for a specific cost ID.                                                                                                   |
| online_order_id    | string    | No       | Unique identifier for the order line.                                                                                                                        |

1You must enter a value. When you ingest data from SAP or EDI, the default value for _string_ is SCN_RESERVED_NO\_ VALUE_PROVIDED and the default value for _timestamp_ date type value is 1900-01-01 00:00:00 for start date, and 9999-12-31 23:59:59 for end date.

2Foreign key

**Foreign key (FK)**

The table below lists the columns with the associated foreign key.

| Column        | Category             | FK/Data entity      | FK/Column |
| ------------- | -------------------- | ------------------- | --------- |
| customer_id   | Organization         | trading_partner     | id        |
| order_id      | Outbound fulfillment | outbound_order_line | id        |
| shipment_id   | Outbound fulfillment | outbound_shipment   | id        |
| order_line_id | Outbound fulfillment | outbound_order_line | id        |
