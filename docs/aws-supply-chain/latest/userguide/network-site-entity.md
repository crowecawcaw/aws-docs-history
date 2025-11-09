# site

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name | Column |
| ---- | ------ |
| site | id     |

The table below lists the column names supported by the data entity:

| Column             | Data type | Required | Description                                                                                                                     |
| ------------------ | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------------- |
| id                 | string    | Yes      | Site ID.                                                                                                                        |
| description        | string    | No       | Description of the site.                                                                                                        |
| company_id1        | string    | No       | Company ID.                                                                                                                     |
| geo_id1            | string    | No       | If the site belongs to a geography,<br>displays<br>the ID of the geographical hierarchy.                                        |
| address_1          | string    | No       | Site address.                                                                                                                   |
| address_2          | string    | No       | Site address.                                                                                                                   |
| address_3          | string    | No       | Site address.                                                                                                                   |
| city               | string    | No       | City in which the site is located.                                                                                              |
| state_prov         | string    | No       | State where the site is located.                                                                                                |
| postal_code        | string    | No       | Postal code of the site.                                                                                                        |
| country            | string    | No       | Country where the site is located.                                                                                              |
| phone_number       | string    | No       | Contact number of the site.                                                                                                     |
| email              | string    | No       | Point of contacts email information.                                                                                            |
| time_zone          | string    | No       | Local time zone of the site.                                                                                                    |
| site_type          | string    | No       | Type of site, for example, warehouse, delivery<br>station, factory, store, and so on.                                           |
| unlocode           | string    | No       | Standardized UN/LOCODE for the site.                                                                                            |
| latitude           | double    | No       | Latitude of the site location.                                                                                                  |
| longitude          | double    | No       | Longitude of the site location.                                                                                                 |
| is_active          | string    | No       | Indicates whether site is active ("true") or deleted ("false")                                                                  |
| site_calendar_id1  | string    | No       | Site's operating and holiday calendar.                                                                                          |
| site_classifier    | string    | No       | Information about site classification. For example, if a store is "high foot fall store" or if DC is Central DC vs Regional DC. |
| open_date          | timestamp | No       | Date when the site started operations.                                                                                          |
| end_date           | timestamp | No       | Date when the site discontinued operational<br>perspective.                                                                     |
| source             | string    | No       | Source of data.                                                                                                                 |
| source_event_id    | string    | No       | ID of the event created in the source system.                                                                                   |
| source_update_dttm | timestamp | No       | Date time stamp of the update made in the source<br>system.                                                                     |

1Foreign key

**Foreign key (FK)**

The table below lists the columns with the associated foreign key.

| Column           | Category     | FK/Data entity | FK/Column   |
| ---------------- | ------------ | -------------- | ----------- |
| company_id       | Organization | company        | id          |
| geo_id           | Organization | geography      | id          |
| site_calendar_id | Reference    | calendar       | calendar_id |
