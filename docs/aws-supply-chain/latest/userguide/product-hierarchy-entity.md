# product_hierarchy

**Primary key (PK)**

The table below lists the column names that are uniquely identified in the data entity.

| Name              | Column |
| ----------------- | ------ |
| product_hierarchy | id     |

The table below lists the column names supported by the data entity:

| Column                   | Data type | Required | Description                                                                                      |
| ------------------------ | --------- | -------- | ------------------------------------------------------------------------------------------------ |
| id                       | string    | Yes      | Product group ID.                                                                                |
| description              | string    | No       | Description of the product group.                                                                |
| company_id1              | string    | No       | Company ID.                                                                                      |
| parent_product_group_id1 | string    | No       | Parent of this product group. If null, it indicates this<br>record is a top level product group. |
| creation_date            | timestamp | No       | Date when the product group was created.                                                         |
| update_date              | timestamp | No       | Date when the product group was updated.                                                         |
| source                   | string    | No       | Source of data.                                                                                  |

1Foreign key

**Foreign key (FK)**

The table below lists the columns with the associated foreign key.

| Column                  | Category     | FK/Data entity    | FK/Column |
| ----------------------- | ------------ | ----------------- | --------- |
| company_id              | Organization | company           | id        |
| parent_product_group_id | Product      | product_hierarchy | id        |
