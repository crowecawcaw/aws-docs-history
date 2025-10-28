# company

**Primary key (PK)**

The table below lists the column names that are uniquely identified in the data entity.

| Name               | Column    |
| ------------------ | --------- | -------------------------------------------------------------------- | -------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| company            | id        | The table below lists the column names supported by the data entity. |
| Column             | Data type | Required                                                             | Description                                              |
| ---                | ---       | ---                                                                  | ---                                                      |
| id                 | string    | Yes                                                                  | ID of the company.                                       |
| description        | string    | No                                                                   | Description of the company.                              |
| address_1          | string    | No                                                                   | Company address.                                         |
| address_2          | string    | No                                                                   | Company address.                                         |
| address_3          | string    | No                                                                   | Company address.                                         |
| city               | string    | No                                                                   | City where the company is located.                       |
| state_prov         | string    | No                                                                   | State where the company is located.                      |
| postal_code        | string    | No                                                                   | Postal code of the company address.                      |
| country            | string    | No                                                                   | Country where the company is located.                    |
| phone_number       | string    | No                                                                   | Company's contact number.                                |
| time_zone          | string    | No                                                                   | Company's local time zone.                               |
| calendar_id 1      | string    | No                                                                   | Default calendar that the company uses for planning.     |
| source             | string    | No                                                                   | Source of data.                                          |
| source_event_id    | string    | No                                                                   | ID of the event created in the source system.            |
| source_update_dttm | timestamp | No                                                                   | Date time stamp of the update made in the source system. | 1Foreign key **Foreign key (FK)** The table below lists the columns with the associated foreign key. |
| Column             | Category  | FK/Data entity                                                       | FK/Column                                                |
| ---                | ---       | ---                                                                  | ---                                                      |
| calendar_id        | Reference | calendar                                                             | calendar_id                                              |
