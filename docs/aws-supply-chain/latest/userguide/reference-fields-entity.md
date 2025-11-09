# reference_field

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name            | Column                                                           |
| --------------- | ---------------------------------------------------------------- |
| reference_field | object_name, object_field, object_field_value, object_field_desc |

The table below lists the column names supported by the data entity:

| Column             | Data type | Required | Description                                             |
| ------------------ | --------- | -------- | ------------------------------------------------------- |
| company_id2        | string    | No       | Company ID.                                             |
| object_name        | string    | Yes1     | For example, sites, or transportation lanes.            |
| object_field       | string    | Yes1     | For example, site_type, or trans_mode.                  |
| object_field_value | string    | Yes1     | For example, site_type:01, or trans_mode:01.            |
| object_field_desc  | string    | Yes1     | For example, site_type:01:DC, or trans_mode:01:Surface. |

1You must enter a value. When you ingest data from SAP
or EDI, the default value for _string_ is SCN_RESERVED_NO_VALUE_PROVIDED.

2Foreign key

**Foreign key (FK)**

The table below lists the column names with the associated data entity and category:

| Column     | Category     | FK/Data entity | FK/Column |
| ---------- | ------------ | -------------- | --------- |
| company_id | Organization | company        | id        |
