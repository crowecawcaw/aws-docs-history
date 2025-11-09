# trading_partner

**Primary key (PK)**

The table below lists the column names that are uniquely identified in the data entity.

| Name            | Column                                                  |
| --------------- | ------------------------------------------------------- |
| trading_partner | id, tpartner_type, geo_id, eff_start_date, eff_end_date |

The table below lists the column names supported by the data entity:

| Column             | Data type | Required | Description                                                                                     |
| ------------------ | --------- | -------- | ----------------------------------------------------------------------------------------------- |
| id                 | string    | Yes      | Partner ID. Referred to by other entities as<br>tpartner_id unless explicitly stated otherwise. |
| description        | string    | No       | Description of the trading partner.                                                             |
| company_id 2       | string    | No       | Company ID.                                                                                     |
| tpartner_type      | string    | Yes1     | Type of partner, for example, vendor, channel<br>partner, or 3PL.                               |
| geo_id 2           | string    | Yes1     | Region of the company associated with the trading<br>partner.                                   |
| eff_start_date     | timestamp | Yes1     | The start timestamp of the relationship between the<br>trading partner and the company.         |
| eff_end_date       | timestamp | Yes1     | The end timestamp of the relationship between the<br>trading partner and the company.           |
| is_active          | string    | No       | Indicates whether trading partner is active or<br>inactive.                                     |
| address_1          | string    | No       | The address corresponding to the trading<br>partner.                                            |
| address_2          | string    | No       | The address corresponding to the trading<br>partner.                                            |
| address_3          | string    | No       | The address corresponding to the trading<br>partner.                                            |
| city               | string    | No       | The city corresponding to the trading partner.                                                  |
| state_prov         | string    | No       | The state corresponding to the trading<br>partner.                                              |
| postal_code        | string    | No       | The postal code of the trading partner.                                                         |
| country            | string    | No       | The country corresponding to the trading<br>partner.                                            |
| phone_number       | string    | No       | The trading partner's contact phone number.                                                     |
| time_zone          | string    | No       | The trading partner's local time zone.                                                          |
| latitude           | double    | No       | Latitude of trading partner location.                                                           |
| longitude          | double    | No       | Longitude of trading partner location.                                                          |
| os_id              | string    | No       | Organizational identifier issued by Open Supplier Hub.                                          |
| duns_number        | string    | No       | Unique nine-digit identification number provided by Dun and Bradstreet (D and B).               |
| source             | string    | No       | Source of data.                                                                                 |
| source_event_id    | string    | No       | ID of the event created in the source system.                                                   |
| source_update_dttm | timestamp | No       | Date time stamp of the update made in the source<br>system.                                     |

1You must enter a value. When you ingest data from SAP
or EDI, the default value for _string_ is SCN_RESERVED_NO_VALUE_PROVIDED; and the default value for _timestamp_ is
1900-01-01 00:00:00 for start date, and 9999-12-31 23:59:59 for end date.

2Foreign key

**Foreign key (FK)**

The table below lists the columns with the associated foreign key.

| Column     | Category     | FK/Data entity | FK/Column |
| ---------- | ------------ | -------------- | --------- |
| company_id | Organization | company        | id        |
| geo_id     | Organization | geography      | id        |
