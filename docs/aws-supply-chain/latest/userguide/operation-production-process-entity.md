# production_process

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name                    | Column                |
| ----------------------- | --------------------- | -------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| production_process      | production_process_id | The table below lists the column names supported by the data entity: |
| Column                  | Data type             | Required                                                             | Description                                                                       |
| ---                     | ---                   | ---                                                                  | ---                                                                               |
| production_process_id   | string                | Yes                                                                  | ID associated with the process and product.                                       |
| production_process_type | string                | No                                                                   | Type of the specific production process. For example, assembly, machining.        |
| production_process_name | string                | No                                                                   | Name of the specific production process. For example, milling, drilling, welding. |
| product_id1             | string                | No                                                                   | Product associated with the production process.                                   |
| company_id1             | string                | No                                                                   | Company ID associated with the production process.                                |
| site_id1                | string                | No                                                                   | Site ID where the production process is taking place.                             |
| start_location          | string                | No                                                                   | Location where the process starts.                                                |
| end_location            | string                | No                                                                   | Location where the process ends.                                                  |
| setup_time              | double                | No                                                                   | Time to setup the process.                                                        |
| setup_time_uom          | string                | No                                                                   | Unit of measure of the setup time.                                                |
| operation_time          | double                | No                                                                   | Total time to complete the process.                                               |
| operation_time_uom      | string                | No                                                                   | Unit of measure of the operation time.                                            |
| frozen_horizon          | double                | No                                                                   | Time period when there are no changes to the production process.                  |
| frozen_horizon_uom      | string                | No                                                                   | Unit of measure for the frozen horizon.                                           |
| unit_cost               | double                | No                                                                   | Cost of the production process.                                                   |
| cost_uom                | string                | No                                                                   | Unit of measure of the production process cost.                                   |
| source                  | string                | No                                                                   | Source of data.                                                                   |
| source_update_dttm      | timestamp             | No                                                                   | Date time stamp of the update made in the source system.                          |
| source_event_id         | string                | No                                                                   | ID of the event created in the source system.                                     | 1Foreign key **Foreign key (FK)** The table below lists the columns with the associated foreign key. |
| Column                  | Category              | FK/Data entity                                                       | FK/Column name                                                                    |
| ---                     | ---                   | ---                                                                  | ---                                                                               |
| product_id              | Product               | product                                                              | id                                                                                |
| company_id              | Organization          | company                                                              | id                                                                                |
| site_id                 | Network               | site                                                                 | id                                                                                |
