# Items dataset requirements (ECOMMERCE domain)

An _Items dataset_ stores metadata about your ECOMMERCE items. This might include information such as price, category, and product description for each item.
For more information on the types of item data you can import
into Amazon Personalize, see [Item metadata](items-datasets.md "items-datasets.md"). For information about general Amazon Personalize schema requirements, such as formatting requirements and available field data types, see [Creating schema JSON files for Amazon Personalize schemas](how-it-works-dataset-schema.md "how-it-works-dataset-schema.md"). These requirements
apply to all schemas, regardless of domain.

An Items dataset is optional for all ECOMMERCE use cases. If you have items data,
we recommend creating one to get the most relevant recommendations. If you create an items dataset, your schema must include the following fields:

- ITEM_ID
- PRICE (`float`)
- CATEGORY_L1 (categorical `string`)

Your schema can also include the following reserved keywords. For categorical fields, you can define your own range of values based on your use case.

- CATEGORY_L2 (categorical `string`, `null`)
- CATEGORY_L3 (categorical `string`, `null`)
- PRODUCT_DESCRIPTION (textual `string`, `null`)
- CREATION_TIMESTAMP (`float`)
- AGE_GROUP (categorical `string`, `null`): The age group the item is for. Values might be newborns, infants, children, and adults.
- ADULT (categorical `string`, `null`): Whether the item is restricted to only adults, such as alcohol. Values might be yes or no.
- GENDER (categorical `string`, `null`): The gender the item is for. Values might be male, female, and unisex.

To get the best recommendations, we recommend that you keep these as many of these fields in your schema as you have data. The data you import must match your schema. The data you import must match your schema.
The maximum number of metadata columns is 100. You are free to add additional fields depending on your use case and your data. As long as the fields aren't listed as required or reserved, and the data types are listed in [Schema data types](how-it-works-dataset-schema.md#personalize-datatypes "how-it-works-dataset-schema.md#personalize-datatypes"), the field names and data types are up to you.

Use reserved keywords CATEGORY_L2 and CATEGORY_L3 for items with multiple multi-level categories.
For more information, see [Using categorical data](#ECOMMERCE-items-categorical-data "#ECOMMERCE-items-categorical-data"). For information on textual and categorical metadata see [Unstructured text metadata](items-datasets.md#text-data "items-datasets.md#text-data").
For an example of
the default schema for Items datasets for ECOMMERCE domains, see [Default Items schema (ECOMMERCE domain)](#ECOMMERCE-items-dataset-schema "#ECOMMERCE-items-dataset-schema").

## Using categorical data

To use categorical data, add a field of type `string` and set the field's categorical attribute to `true` in your schema.
Then include the categorical data in your bulk CSV file and individual item imports. You can define your own range of values based on your use case. Categorical values can have at most 1000 characters. If you have an item with a categorical
value with more than 1000 characters, your dataset import job will fail.

For items with multiple categories, separate each value with the vertical bar, '|'. For example, for a CATEGORY_L1 field your data for an item might be
`Electronics|Productivity|Mouse`. If you have a multiple levels of categorical data and some items have multiple categories for each level in the hierarchy, add a field for each level and append a level indicator after each field name:
CATEGORY_L1, CATEGORY_L2, CATEGORY_L3. This allows you filter recommendations based on sub-categories, even if an item belongs to multiple multi-level categories.
For example, an item might have the following data for each category level:

- CATEGORY_L1: Electronics|Productivity
- CATEGORY_L2: Productivity|Computers
- CATEGORY_L3: Mouse

In this example, the item is in the electronics > productivity > mouse hierarchy _and_ the productivity > computers > mouse hierarchy.
We recommend only using up to L3 but you can use more levels if necessary. For information on creating and using filters see
[Filtering recommendations and user segments](filter.md "filter.md").

## Default Items schema (ECOMMERCE domain)

The following is the default schema for Items datasets for the ECOMMERCE domain with only the required fields.

```
{
  "type": "record",
  "name": "Items",
  "namespace": "com.amazonaws.personalize.schema",
  "fields": [
    {
      "name": "ITEM_ID",
      "type": "string"
    },
    {
      "name": "PRICE",
      "type": "float"
    },
    {
      "name": "CATEGORY_L1",
      "type": [
        "string"
      ],
      "categorical": true
    }
  ],
  "version": "1.0"
}
```
