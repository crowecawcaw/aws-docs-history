# un_details

**Primary key (PK)**

The table below lists the colum names that are uniquely identified in the data entity.

| Name               | Column    |
| ------------------ | --------- | -------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| product_un_details | un_id     | The table below lists the column names supported by the data entity: |
| Column name        | Data type | Required                                                             | Description                                                                                                                                                                                                       |
| ---                | ---       | ---                                                                  | ---                                                                                                                                                                                                               |
| un_class           | string    | No                                                                   | Hazardous material categories and subcategories.                                                                                                                                                                  |
| hazmat_class       | string    | No                                                                   | One of nine classes of hazardous materials (as of 2024).                                                                                                                                                          |
| image_url          | string    | No                                                                   | Image of the symbol for the hazmat class.                                                                                                                                                                         |
| un_description     | string    | No                                                                   | Description of the UN Proper Shipping Name.                                                                                                                                                                       |
| un_id              | string    | Yes                                                                  | UN IDs are four-digit numbers that identify dangerous goods, hazardous substances and articles (such as explosives, flammable liquids, toxic substances, and so on.) in the framework of international transport. |
