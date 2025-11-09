# supply_planning_parameters

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name                       | Column                                                                             |
| -------------------------- | ---------------------------------------------------------------------------------- |
| supply_planning_parameters | product_id, product_group_id, site_id, eff_start_date, eff_end_date, connection_id |

The table below lists the column names supported by the _supply_planning_parameters_ data entity:

| Column                             | Data type | Required | Description                                                                     |
| ---------------------------------- | --------- | -------- | ------------------------------------------------------------------------------- |
| product_id1                        | string    | Yes      | ID of product                                                                   |
| product_group_id1                  | string    | Yes      | For future Use. Please populate SCN_RESERVED_NO_VALUE_PROVIDED for now.         |
| site_id1                           | string    | Yes      | For future Use. Please populate SCN_RESERVED_NO_VALUE_PROVIDED for now.         |
| planner_name                       | string    | No       | name of the supply planner who manages a product or a product group             |
| demand_time_fence_days             | int       | No       | For future Use.                                                                 |
| forecast_consumption_backward_days | int       | No       | For future Use                                                                  |
| forecast_consumption_forward_days  | int       | No       | For future Use.                                                                 |
| eff_start_date                     | timestamp | Yes      | effective start date time                                                       |
| eff_end_date                       | timestamp | Yes      | effective end date time                                                         |
| connection_id                      | string    | Yes      | Unique identifier for the data source (i.e. connection). Auto populated by ASC. |

1Foreign key

**Foreign key (FK)**

The table below lists the column names with the associated data entity and category:

| Column           | Category | FK/Data entity    | FK/Column |
| ---------------- | -------- | ----------------- | --------- |
| product_id       | Product  | product           | id        |
| product_group_id | Product  | product_hierarchy | id        |
| site_id          | Network  | site              | id        |
