# trading_partner_poc

**Primary key (PK)**

The table below lists the column names that are uniquely identified in the data entity.

| Name                     | Column             |
| ------------------------ | ------------------ | -------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| trading_partner_poc      | tpartner_id, email | The table below lists the column names supported by the data entity: |
| Column                   | Data type          | Required                                                             | Description                                                                                                             |
| ---                      | ---                | ---                                                                  | ---                                                                                                                     |
| tpartner_id 1            | string             | Yes                                                                  | Partner ID. Referred to by other entities as tpartner_id unless explicitly stated otherwise.                            |
| email                    | string             | Yes                                                                  | Partner's email ID.                                                                                                     |
| poc_first_name           | string             | No                                                                   | Partner's first name.                                                                                                   |
| poc_last_name            | string             | No                                                                   | Partner's last name.                                                                                                    |
| poc_org_unit_name        | string             | No                                                                   | Name of the team or internal organizational unit.                                                                       |
| poc_org_unit_description | string             | No                                                                   | AWS profile or description of the team's role in an organization to be shared with the customer to describe their team. |
| source                   | string             | No                                                                   | Source of data.                                                                                                         |
| source_event_id          | string             | No                                                                   | ID of the event created in the source system.                                                                           |
| source_update_dttm       | timestamp          | No                                                                   | Date time stamp of the update made in the source system.                                                                | 1Foreign key **Foreign key (FK)** The table below lists the columns with the associated foreign key. |
| Column                   | Category           | FK/Data entity                                                       | FK/Column                                                                                                               |
| ---                      | ---                | ---                                                                  | ---                                                                                                                     |
| tpartner_id              | Organization       | trading_partner                                                      | id                                                                                                                      |
