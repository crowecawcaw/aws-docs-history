# sourcing_rules

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name           | Column                                         |
| -------------- | ---------------------------------------------- |
| sourcing_rules | sourcing_rule_id, eff_start_date, eff_end_date |

The table below lists the column names supported by the data entity:

| Column                 | Data type | Required | Description                                                                                                                                                                                                                                                    |
| ---------------------- | --------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| sourcing_rule_id       | string    | Yes      | Sourcing rule ID.                                                                                                                                                                                                                                              |
| company_id2            | string    | No       | Displays the company ID.                                                                                                                                                                                                                                       |
| product_id2            | string    | No       | Product ID to be sourced.                                                                                                                                                                                                                                      |
| to_site_id2            | string    | No       | Site ID into which product will be sourced.                                                                                                                                                                                                                    |
| from_site_id2          | string    | No       | Site ID from which product will be sourced.                                                                                                                                                                                                                    |
| product_group_id2      | string    | No       | Product group ID.                                                                                                                                                                                                                                              |
| sourcing_rule_type     | string    | No       | Type of sourcing rule. The supported sourcing rule types are<br>transfer, buy, and manufacture. Only lower case is<br>allowed.                                                                                                                                 |
| tpartner_id2           | string    | No       | Trading partner ID is used depending on sourcing rule type. For example, when sourcing rule type is Buy, Buy is the Vendor ID and you can use this vendor ID along with other attributes to find additional<br>details from vendor_product and other entities. |
| tpartner_location      | string    | No       | The location of the trading partner. For example, Seattle, China, New Mexico, and so on.                                                                                                                                                                       |
| transportation_lane_id | string    | No       | Transportation lane ID is used depending on sourcing rule type. For example, when sourcing type is Transfer, you can use this ID along with other attributes to choose the correct transportation_lane.                                                        |
| sourcing_priority2     | int       | No       | Priority of sourcing rule.                                                                                                                                                                                                                                     |
| sourcing_ratio         | double    | No       | Proportion of product to be sourced from this product/group, to_site, from_site/tpartner_id combination. All sources for a product, site should add to 1 for a specific time period<br>(or application normalizes the ratio to 1).                             |
| qty_uom                | string    | No       | Quantity UOM associated with sourcing rule.                                                                                                                                                                                                                    |
| min_qty                | double    | No       | Minimum quantity for the sourcing rule.                                                                                                                                                                                                                        |
| max_qty                | double    | No       | Maximum quantity for the sourcing rule.                                                                                                                                                                                                                        |
| qty_multiple           | double    | No       | Quantity is in multiples of this value.                                                                                                                                                                                                                        |
| eff_start_date         | timestamp | Yes1     | Effective start date of the calendar.                                                                                                                                                                                                                          |
| eff_end_date           | timestamp | Yes1     | Effective end date of the calendar.                                                                                                                                                                                                                            |
| source                 | string    | No       | Source of data.                                                                                                                                                                                                                                                |
| production_process_id  | string    | No       | Type of process operation. For example, stop machine.                                                                                                                                                                                                          |
| source_event_id        | string    | No       | ID of the event created in the source system.                                                                                                                                                                                                                  |
| source_update_dttm     | timestamp | No       | Date time stamp of the update made in the source<br>system.                                                                                                                                                                                                    |

1You must enter a value. When you ingest data from SAP
or EDI, the default values for _timestamp_ is, 1900-01-01 00:00:00 for start date, and
9999-12-31 23:59:59 for end date.

2Foreign key

**Foreign key (FK)**

The table below lists the column names with a foreign key:

|                          | Category     | FK/Data entity       | FK/Column             |
| ------------------------ | ------------ | -------------------- | --------------------- |
| to_site_id, from_site_id | Network      | site                 | id                    |
| company_id               | Organization | company              | id                    |
| product_id               | Product      | product              | id                    |
| product_group_id         | Product      | product_hierarchy    | id                    |
| tpartner_id              | Organization | trading_partner      | id                    |
| transportation_lane_id   | Network      | transporatation_lane | id                    |
| production_process_id    | Operation    | production_process   | production_process_id |
