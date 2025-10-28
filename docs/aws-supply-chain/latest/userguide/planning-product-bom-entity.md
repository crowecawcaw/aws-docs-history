# product_bom

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name                      | Column                               |
| ------------------------- | ------------------------------------ | -------------------------------------------------------------------- | --------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| product_bom               | id, product_id, component_product_id | The table below lists the column names supported by the data entity: |
| column                    | Data type                            | Required                                                             | Description                                                           |
| ---                       | ---                                  | ---                                                                  | ---                                                                   |
| id                        | string                               | Yes                                                                  | Displays the BOM ID.                                                  |
| product_id 2              | string                               | Yes                                                                  | Product for which the BOM is defined.                                 |
| site_id 2                 | string                               | No                                                                   | Site for which the BOM is defined.                                    |
| company_id2               | string                               | No                                                                   | Displays the company ID.                                              |
| level                     | int                                  | No                                                                   | Displays the level of the BOM in multi-level BOM.                     |
| component_product_id      | string                               | Yes 1                                                                | Displays the component's product ID.                                  |
| component_quantity_per    | double                               | Yes                                                                  | Quantity of component required to produce one unit of parent product. |
| component_quantity_uom    | string                               | No                                                                   | Unit of measurement of the component.                                 |
| component_line_number     | int                                  | No                                                                   | Line ID of the child record.                                          |
| lifecycle_phase           | string                               | No                                                                   | Information about the life cycle phase associated with the BOM.       |
| assembly_cost             | double                               | No                                                                   | UOM of the product.                                                   |
| assembly_cost_uom         | string                               | No                                                                   | Assembly cost of the product.                                         |
| eff_start_date            | timestamp                            | No                                                                   | Dates from when the record is effective.                              |
| eff_end_date              | timestamp                            | No                                                                   | Dates till when the record is effective.                              |
| description               | string                               | No                                                                   | BOM description.                                                      |
| production_process_id     | string                               | No                                                                   | ID associated with a specific production process.                     |
| alternative_product_id    | string                               | No1                                                                  | ID of the alternate product used in the BOM.                          |
| priority                  | string                               | No                                                                   | Priority of the product or components used in the BOM.                |
| alternate_group_id        | string                               | No                                                                   | ID of the alternate product group.                                    |
| alternate_product_qty     | double                               | No                                                                   | Quantity of the alternate product used in the BOM.                    |
| alternate_product_qty_uom | string                               | No                                                                   | UOM associated with the quantity of the alternate product.            |
| ratio                     | double                               | No                                                                   | Ratio of the products in the BOM.                                     |
| creation_date             | timestamp                            | No1                                                                  | Date when the BOM was created.                                        |
| change_date               | timestamp                            | No1                                                                  | Date when the BOM was updated.                                        |
| source                    | string                               | No                                                                   | Source of data.                                                       |
| source_event_id           | string                               | No                                                                   | ID of the event created in the source system.                         |
| source_update_dttm        | timestamp                            | No                                                                   | Date time stamp of the update made in the source system.              | 1You must enter a value. When you ingest data from SAP or EDI, the default values for string and timestamp date type values are: SCN_RESERVED_NO_VALUE_PROVIDED for _string_; and for _timestamp_ , 1900-01-01 00:00:00 for start date, and 9999-12-31 23:59:59 for end date. 2Foreign key **Foreign key (FK)** The table below lists the column names with the associated data entity and category: |
| Column                    | Category                             | FK/Data entity                                                       | FK/Column                                                             |
| ---                       | ---                                  | ---                                                                  | ---                                                                   |
| company_id                | Organization                         | company                                                              | id                                                                    |
| product_id                | Product                              | product                                                              | id                                                                    |
| site_id                   | Network                              | site                                                                 | id                                                                    |
| production_process_id     | Operation                            | production_process                                                   | production_process_id                                                 |
| alternative_product_id    | Product                              | product_alternate                                                    | product_alternate_id                                                  |
