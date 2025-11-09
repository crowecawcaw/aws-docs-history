# product_uom

**Primary key (PK)**

The table below lists the column names that are uniquely identified in the data entity.

| Name        | Column                                       |
| ----------- | -------------------------------------------- |
| product_bom | product_uom_id, eff_start_date, eff_end_date |

The table below lists the column names supported by the data entity:

| Column         | Data type | Required | Description                                                                        |
| -------------- | --------- | -------- | ---------------------------------------------------------------------------------- |
| product_uom_id | string    | Yes      | ID for product unit of measurement (UOM) combination.                              |
| product_id     | string    | Yes      | Product associated with product-uom combination.                                   |
| uom            | string    | Yes      | UOM identifier.                                                                    |
| description    | string    | No       | Description of product-uom.                                                        |
| company_id 1   | string    | No       | Company ID.                                                                        |
| price          | double    | No       | Price of product-uom.                                                              |
| cost           | double    | No       | Cost of product-uom.                                                               |
| currency_uom   | string    | No       | Unit of measure (UOM) of currency.                                                 |
| status         | string    | No       | Status of record. For example, Active, Inactive and so on.                         |
| is_standard    | string    | No       | Describe if this is a standard product-uom.                                        |
| barcode_type   | string    | No       | Type of barcode.                                                                   |
| barcode_value  | string    | No       | Value of barcode.                                                                  |
| type           | string    | No       | Type of product-uom.                                                               |
| quantity       | double    | No       | Displays the quantity for one product uom ID in terms of base UOM for the product. |
| quantity_uom   | string    | No       | Unit of measure (UOM) of quantity in base UOM.                                     |
| length         | double    | No       | Length of the package.                                                             |
| width          | double    | No       | Width of the package.                                                              |
| height         | double    | No       | Height of the package.                                                             |
| dimension_uom  | string    | No       | Unit of measure (UOM) of dimension.                                                |
| volume         | double    | No       | Volume of the package.                                                             |
| volume_uom     | string    | No       | Unit of measure (UOM) of volume.                                                   |
| weight         | double    | No       | Package weight.                                                                    |
| weight_uom     | string    | No       | Unit of measure (UOM) of weight.                                                   |
| eff_start_date | timestamp | Yes      | Displays the date and time the record becomes effective.                           |
| eff_end_date   | timestamp | Yes      | Displays the date and time the record ends.                                        |
| source         | string    | No       | Source of data.                                                                    |

1Foreign key

**Foreign key (FK)**

The table below lists the columns with the associated foreign key.

| Column     | Category     | FK/Data entity | FK/Column |
| ---------- | ------------ | -------------- | --------- |
| company_id | Organization | company        | id        |
