# geography

**Primary key (PK)**

The table below lists the column names that are uniquely identified in the data entity.

| Name               | Column       |
| ------------------ | ------------ | -------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| geography          | id           | The table below lists the column names supported by the data entity: |
| Column             | Data type    | Required                                                             | Description                                                                                         |
| ---                | ---          | ---                                                                  | ---                                                                                                 |
| id                 | string       | Yes                                                                  | Geographical ID. Referred to by other entities as geo_id or region_id.                              |
| description        | string       | No                                                                   | Geographical location.                                                                              |
| company_id 1       | string       | No                                                                   | Company ID.                                                                                         |
| parent_geo_id 1    | string       | No                                                                   | Stores parent geographical ID for this record. If blank, this is a top level region in the company. |
| address_1          | string       | No                                                                   | City corresponding to this geo-region.                                                              |
| address_2          | string       | No                                                                   | City corresponding to this geo-region.                                                              |
| address_3          | string       | No                                                                   | City corresponding to this geo-region.                                                              |
| city               | string       | No                                                                   | Displays the city corresponding to this geo-region.                                                 |
| state_prov         | string       | No                                                                   | State corresponding to this geo-region.                                                             |
| postal_code        | string       | No                                                                   | Postal code corresponding to this geo-region.                                                       |
| country            | string       | No                                                                   | Country corresponding to this geo-region.                                                           |
| phone_number       | string       | No                                                                   | Company's contact number.                                                                           |
| time_zone          | string       | No                                                                   | Company local time zone.                                                                            |
| source             | string       | No                                                                   | Source of data.                                                                                     |
| source_event_id    | string       | No                                                                   | ID of the event created in the source system.                                                       |
| source_update_dttm | timestamp    | No                                                                   | Date time stamp of the update made in the source system.                                            | 1 Foreign key **Foreign key (FK)** The table below lists the columns with the associated foreign key. |
| Column             | Category     | FK/Data entity                                                       | FK/Column                                                                                           |
| ---                | ---          | ---                                                                  | ---                                                                                                 |
| company_id         | Organization | company                                                              | id                                                                                                  |
| parent_geo_id      | Organization | geography                                                            | id                                                                                                  |
