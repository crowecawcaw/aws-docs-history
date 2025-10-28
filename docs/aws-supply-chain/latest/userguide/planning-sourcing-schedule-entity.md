# sourcing_schedule

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name                     | Column                                             |
| ------------------------ | -------------------------------------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| sourcing_schedule        | sourcing_schedule_id, eff_start_date, eff_end_date | The table below lists the column names supported by the data entity: |
| Column                   | Data type                                          | Required                                                             | Description                                                         |
| ---                      | ---                                                | ---                                                                  | ---                                                                 |
| sourcing_schedule_id     | string                                             | Yes                                                                  | Sourcing schedule ID.                                               |
| company_id2              | string                                             | No                                                                   | Displays the company ID.                                            |
| tpartner_id2             | string                                             | No                                                                   | Trading partner ID.                                                 |
| status                   | string                                             | No                                                                   | Status of the supply schedule. For example, active, inactive.       |
| from_site_id2            | string                                             | No                                                                   | Origin site ID. For example, hub, vendor.                           |
| to_site_id2              | string                                             | No                                                                   | Destination site ID. For example, hub or a customer in the network. |
| schedule_type            | string                                             | No                                                                   | Type of schedule. For example, inbound ordering, outbound shipping. |
| eff_start_date           | timestamp                                          | Yes1                                                                 | Date-time when schedule becomes effective.                          |
| eff_end_date             | timestamp                                          | Yes1                                                                 | Date-time till when schedule is effective.                          |
| source                   | string                                             | No                                                                   | Source of data.                                                     |
| source_event_id          | string                                             | No                                                                   | ID of the event created in the source system.                       |
| source_update_dttm       | timestamp                                          | No                                                                   | Date time stamp of the update made in the source system.            | 1You must enter a value. When you ingest data from SAP or EDI, the default values for _timestamp_ is, 1900-01-01 00:00:00 for start date, and 9999-12-31 23:59:59 for end date. 2Foreign key **Foreign key (FK)** The table below lists the column names with the associated data entity and category: |
| Column                   | Category                                           | FK/Data entity                                                       | FK/Column                                                           |
| ---                      | ---                                                | ---                                                                  | ---                                                                 |
| from_site_id, to_site_id | Network                                            | site                                                                 | id                                                                  |
| company_id               | Organization                                       | company                                                              | id                                                                  |
| tpartner_id              | Organization                                       | trading_partner                                                      | id                                                                  |
