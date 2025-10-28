# uom_conversion

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name               | Column                                               |
| ------------------ | ---------------------------------------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| uom_conversion     | uom, conversion_uom_id, eff_start_date, eff_end_date | The table below lists the column names supported by the data entity: |
| Column             | Data type                                            | Required                                                             | Description                                                   |
| ---                | ---                                                  | ---                                                                  | ---                                                           |
| uom                | string                                               | Yes                                                                  | Unit of measure (UOM). For example, weight_uom, currency_uom. |
| company_id2        | string                                               | No                                                                   | Company ID.                                                   |
| uom_code           | string                                               | No                                                                   | Alternate code for UOM.                                       |
| uom_description    | string                                               | No                                                                   | UOM description.                                              |
| uom_type           | string                                               | No                                                                   | UOM type, for example, currency, weight, volume, or unit.     |
| conversion_uom_id  | string                                               | Yes                                                                  | UOM ID for conversion.                                        |
| conversion_factor  | double                                               | Yes                                                                  | Conversion factor.                                            |
| eff_start_date     | timestamp                                            | Yes1                                                                 | Effective start date and time.                                |
| eff_end_date       | timestamp                                            | Yes1                                                                 | Effective end date and time.                                  |
| source             | string                                               | No                                                                   | Source of data.                                               |
| source_update_dttm | timestamp                                            | No                                                                   | Date time stamp of the update made in the source system.      | 1You must enter a value. When you ingest data from SAP or EDI, the default value for _timestamp_ date type value is 1900-01-01 00:00:00 for start date, and 9999-12-31 23:59:59 for end date. 2Foreign key **Foreign key (FK)** The table below lists the column names with the associated data entity and category: |
| Column             | Category                                             | FK/Data entity                                                       | FK/Column                                                     |
| ---                | ---                                                  | ---                                                                  | ---                                                           |
| company_id         | Organization                                         | company                                                              | id                                                            |
