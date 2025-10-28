# vendor_holiday

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name                | Column                                                 |
| ------------------- | ------------------------------------------------------ | -------------------------------------------------------------------- | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| vendor_holiday      | vendor_tpartner_id, outage_start_date, outage_end_date | The table below lists the column names supported by the data entity: |
| Column              | Data type                                              | Required                                                             | Description                       |
| ---                 | ---                                                    | ---                                                                  | ---                               |
| company_id2         | string                                                 | No                                                                   | Company ID.                       |
| vendor_tpartner_id2 | string                                                 | Yes                                                                  | Trading partner ID of the vendor. |
| outage_start_date   | timestamp                                              | Yes1                                                                 | Outage start date.                |
| outage_end_date     | timestamp                                              | Yes1                                                                 | Outage end date.                  |
| outage_type         | string                                                 | No                                                                   | Type of outage.                   |
| comment             | string                                                 | No                                                                   | Comment from the vendor.          | 1You must enter a value. When you ingest data from SAP or EDI, the default value for _timestamp_ date type value is 1900-01-01 00:00:00 for start date, and 9999-12-31 23:59:59 for end date. 2Foreign key **Foreign key (FK)** The table below lists the column names with the associated data entity and category: |
| Column              | Category                                               | FK/Data entity                                                       | FK/Column                         |
| ---                 | ---                                                    | ---                                                                  | ---                               |
| company_id          | Organization                                           | company                                                              | id                                |
| vendor_tpartner_id  | Organization                                           | trading_partner                                                      | id                                |
