# segmentation

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name         | Column                                                                       |
| ------------ | ---------------------------------------------------------------------------- |
| segmentation | segment_id, creation_date, site_id, product_id, eff_start_date, eff_end_date |

The table below lists the column names supported by the data entity:

| Column              | Data type | Required | Description                                                                                                    |
| ------------------- | --------- | -------- | -------------------------------------------------------------------------------------------------------------- |
| segment_id          | string    | Yes      | Segment ID.                                                                                                    |
| creation_date       | timestamp | Yes      | Date and time that the segment was created.                                                                    |
| company_id2         | string    | No       | Displays the company ID.                                                                                       |
| site_id2            | string    | Yes      | Overrides policies specified for the region for this node in<br>the product hierarchy.                         |
| product_id2         | string    | Yes1     | Overrides policies specified for the product-group for this<br>node in the geo hierarchy.                      |
| segment_description | string    | No       | Segment description.                                                                                           |
| segment_type        | string    | No       | Type of segmentation, for example, value based, demand<br>variability based, or demand speed based.            |
| segment_value       | double    | No       | Metric associated with the segment calculated when the segment<br>is generated. Value depends on segment_type. |
| source              | string    | No       | Information about the segment creator.                                                                         |
| eff_start_date      | timestamp | Yes1     | Effective start date of the calendar.                                                                          |
| eff_end_date        | timestamp | Yes1     | Effective end date of the calendar.                                                                            |
| source_event_id     | string    | No       | ID of the event created in the source system.                                                                  |
| source_update_dttm  | timestamp | No       | Date time stamp of the update made in the source<br>system.                                                    |

1You must enter a value. When you ingest data from SAP
or EDI, the default values for string and timestamp date type values are
SCN_RESERVED_NO_VALUE_PROVIDED for _string_; and for
_timestamp_ , 1900-01-01 00:00:00 for start date, and
9999-12-31 23:59:59 for end date.

2Foreign key

**Foreign key (FK)**

The table below lists the column names with the associated data entity and category:

| Column     | Category     | FK/Data entity | FK/Column |
| ---------- | ------------ | -------------- | --------- |
| site_id    | Network      | site           | id        |
| company_id | Organization | company        | id        |
| product_id | Product      | product        | id        |
