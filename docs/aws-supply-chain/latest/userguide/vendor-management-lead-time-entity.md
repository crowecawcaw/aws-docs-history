# vendor_lead_time

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name             | Column                                                                                             |
| ---------------- | -------------------------------------------------------------------------------------------------- |
| vendor_lead_time | vendor_tpartner_id, product_id, product_group_id, site_id, region_id, eff_start_date, eff_end_date |

The table below lists the column names supported by the data entity:

| Column                | Data type | Required | Description                                                                                           |
| --------------------- | --------- | -------- | ----------------------------------------------------------------------------------------------------- |
| company_id2           | string    | No       | Company ID.                                                                                           |
| vendor_tpartner_id2   | string    | Yes      | Trading partner ID of the vendor.                                                                     |
| product_id2           | string    | Yes1     | Product ID.                                                                                           |
| product_group_id2     | string    | Yes1     | Used if lead time is set at product-group level.                                                      |
| site_id2              | string    | Yes1     | Site where this product is being supplied.                                                            |
| region_id2            | string    | Yes1     | Used if lead time is set at geographical region level. Site<br>level values will override this value. |
| planned_lead_time     | double    | No       | Planned lead time from vendor into company's site.                                                    |
| planned_lead_time_dev | double    | No       | Standard deviation of lead time.                                                                      |
| actual_lead_time_mean | double    | No       | Field to store actual lead time computed from transactional<br>data.                                  |
| actual_lead_time_sd   | double    | No       | Standard deviation of actual lead time.                                                               |
| actual_p50            | double    | No       | 50th percentile of actual lead time.                                                                  |
| actual_p90            | double    | No       | 90th percentile of actual lead time.                                                                  |
| shipping_cost         | double    | No       | Inbound shipping cost from vendor to company.                                                         |
| cost_uom              | string    | No       | Unit of measure of shipping cost.                                                                     |
| we_pay                | string    | No       | Yes or No indicator. Yes if company pays for inbound shipping,<br>and No if vendor pays for shipping. |
| eff_start_date        | timestamp | Yes1     | Date and time from when this record is effective.                                                     |
| eff_end_date          | timestamp | Yes1     | Date and time till when this record is effective.                                                     |
| sap_eina\_\_infnr     | string    | No       | Record on number of purchases. Predicate key for SAP mapping. Upsert key for EINE.                    |
| source_site_id 2      | string    | No       | Site from where the inbound shipment is originated.                                                   |
| trans_mode            | string    | No       | Transportation mode. For example, ship, water, truck, or rail.                                        |
| source                | string    | No       | Source of data.                                                                                       |
| source_event_id       | string    | No       | ID of the event created in the source system.                                                         |
| source_update_dttm    | timestamp | No       | Date time stamp of the update made in the source<br>system.                                           |

1You must enter a value. When you ingest data from SAP
or EDI, the default values for string and timestamp date type values are
SCN_RESERVED_NO_VALUE_PROVIDED for _string_; and for
_timestamp_, 1900-01-01 00:00:00 for start date, and
9999-12-31 23:59:59 for end date.

2Foreign key

**Foreign key (FK)**

The table below lists the columns with the associated foreign key.

| Column             | Category     | FK/Data entity    | FK/Column |
| ------------------ | ------------ | ----------------- | --------- |
| site_id            | Network      | site              | id        |
| source_site_id     | Network      | site              | id        |
| company_id         | Organization | company           | id        |
| region_id          | Organization | geography         | id        |
| vendor_tpartner_id | Organization | trading_partner   | id        |
| product_group_id   | Product      | product_hierarchy | id        |
| product_id         | Product      | product_id        | id        |
