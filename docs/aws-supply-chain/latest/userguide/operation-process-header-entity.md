# process_header

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name                    | Column       |
| ----------------------- | ------------ | -------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| process_header          | process_id   | The table below lists the column names supported by the data entity: |
| Column                  | Data type    | Required                                                             | Description                                                                                  |
| ---                     | ---          | ---                                                                  | ---                                                                                          |
| process_id              | string       | Yes                                                                  | Process ID. For example, order, work order, maintenance order, or process inquiry.           |
| type                    | string       | No                                                                   | Type of process. For example, customer order, maintenance, or repair, etc.                   |
| company_id1             | string       | No                                                                   | Company ID.                                                                                  |
| site_id1                | string       | No                                                                   | Site or plant ID.                                                                            |
| site_location           | string       | No                                                                   | Name of the location or section in site or plant.                                            |
| planning_group          | string       | No                                                                   | Group planning the work. This field will be an organization entity in the source system.     |
| execution_group         | string       | No                                                                   | Group executing the work. This field will be an organization entity in the source system.    |
| program_group           | string       | No                                                                   | Long running program or project name used for group work. For example, maintenance campaign. |
| status                  | string       | No                                                                   | Status of the process.                                                                       |
| revision                | string       | No                                                                   | Revision number associated with planning or program group.                                   |
| latest_start_date       | timestamp    | No                                                                   | Latest start date for the process.                                                           |
| description             | string       | No                                                                   | Process description.                                                                         |
| priority                | string       | No                                                                   | Priority of the process.                                                                     |
| planned_cost            | double       | No                                                                   | Total planned costs for the process.                                                         |
| currency_uom            | string       | No                                                                   | Currency in which value is specified.                                                        |
| planned_completion_date | timestamp    | No                                                                   | Planned completion date of the process.                                                      |
| planned_closing_date    | timestamp    | No                                                                   | Planned closing date of the process.                                                         |
| planned_release_date    | timestamp    | No                                                                   | Date when the process is planned to be released.                                             |
| planned_start_date      | timestamp    | No                                                                   | Planned start date for the process.                                                          |
| actual_completion_date  | timestamp    | No                                                                   | Actual completion date of the process.                                                       |
| actual_closing_date     | timestamp    | No                                                                   | Actual close date of the process.                                                            |
| actual_release_date     | timestamp    | No                                                                   | Actual release date for process.                                                             |
| actual_start_date       | timestamp    | No                                                                   | Actual start date for process.                                                               |
| process_url             | string       | No                                                                   | URL to access process record in source system.                                               |
| source_update_dttm      | timestamp    | No                                                                   | Date time stamp of the update made in the source system.                                     |
| source_event_id         | string       | No                                                                   | ID of the event created in the source system.                                                |
| source                  | string       | No                                                                   | Source of data.                                                                              |
| flex_1                  | string       | No                                                                   | Process flexible field 1                                                                     |
| flex_2                  | string       | No                                                                   | Process flexible field 2                                                                     |
| flex_3                  | string       | No                                                                   | Process flexible field 3                                                                     |
| flex_4                  | string       | No                                                                   | Process flexible field 4                                                                     |
| flex_5                  | string       | No                                                                   | Process flexible field 5                                                                     | 1Foreign key **Foreign key (FK)** The table below lists the column names with the associated data entity and category: |
| Column                  | Category     | FK/Data entity                                                       | FK/Column                                                                                    |
| ---                     | ---          | ---                                                                  | ---                                                                                          |
| site_id                 | Network      | site                                                                 | id                                                                                           |
| company_id              | Organization | company                                                              | id                                                                                           |
