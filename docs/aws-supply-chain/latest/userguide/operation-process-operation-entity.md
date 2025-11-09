# process_operation

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name              | Column                           |
| ----------------- | -------------------------------- |
| process_operation | process_operation_id, process_id |

The table below lists the column names supported by the _process_operation_ data entity:

| Column               | Data type | Required | Description                                                         |
| -------------------- | --------- | -------- | ------------------------------------------------------------------- |
| process_operation_id | string    | Yes      | Type of process operation.                                          |
| process_id1          | string    | Yes      | Process ID. For example, process, work order, or maintenance order. |
| company_id1          | string    | No       | Company ID.                                                         |
| type                 | string    | No       | Type of operation within the process. For example, open machine.    |
| site_location        | string    | No       | Name of the location or section in site or plant.                   |
| status               | string    | No       | Status of the process.                                              |
| operation_name       | string    | No       | Name of the operation.                                              |
| operation_sequence   | string    | No       | Sequence of the operation within the process.                       |
| planned_start_dttm   | timestamp | No       | Planned start date-time of operation.                               |
| planned_end_dttm     | timestamp | No       | Planned end date-time of operation.                                 |

1Foreign key

**Foreign key (FK)**

The table below lists the columns with the associated foreign key.

| Column     | Category     | FK/Data entity | FK/Column  |
| ---------- | ------------ | -------------- | ---------- |
| process_id | Operation    | process_header | process_id |
| company_id | Organization | company        | id         |
