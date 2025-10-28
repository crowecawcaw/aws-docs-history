# Items dataset requirements (VIDEO_ON_DEMAND domain)

An _Items dataset_ stores metadata about your items in your catalogue. This might include information such as price, genre, and availability for each item.
For information about the types of item data you can import into Amazon Personalize, see
[Item metadata](items-datasets.md "items-datasets.md"). For information about general Amazon Personalize schema requirements, such as formatting requirements and available field data types, see [Creating schema JSON files for Amazon Personalize schemas](how-it-works-dataset-schema.md "how-it-works-dataset-schema.md"). These requirements
apply to all schemas, regardless of domain.

An Items dataset is required for some use cases (see [VIDEO_ON_DEMAND use
cases](VIDEO_ON_DEMAND-use-cases.md "VIDEO_ON_DEMAND-use-cases.md")). When optional,
we still recommend creating one to get the most relevant recommendations. If you create an Items dataset, your schema must include the following fields:

- ITEM_ID
- GENRES (categorical `string`)
- CREATION_TIMESTAMP (in Unix epoch time format)

Your schema can also include the following reserved keywords. Each keyword lists its required data type and whether it supports null data. Adding the null type is optional.

- PRICE (float)
- DURATION (float)
- GENRE_L2 (categorical `string`, `null`)
- GENRE_L3 (categorical `string`, `null`)
- AVERAGE_RATING (`float`, `null`)
- PRODUCT_DESCRIPTION (textual `string`, `null`)
- CONTENT_OWNER (categorical `string`, `null`): The company that owns the video. For example, values might be HBO, Paramount, and NBC.
- CONTENT_CLASSIFICATION (categorical `string`, `null`): The content's rating. For example, values might be G, PG, PG-13, R, NC-17, and unrated.

To get the best recommendations, we recommend that you keep these as many of these fields in your schema as you have data. The data you import must match your schema. The maximum number of metadata columns is 100.
You are free to add additional fields depending on your use case and your data. As long as the fields aren't listed as required or reserved, and the data types are listed in [Schema data types](how-it-works-dataset-schema.md#personalize-datatypes "how-it-works-dataset-schema.md#personalize-datatypes"), the field names and data types are up to you.

Use reserved keywords GENRE_L2 and GENRE_L3 for items with multiple multi-level categories. For more information, see [Using categorical data](#VIDEO-ON-DEMAND-items-categorical-data "#VIDEO-ON-DEMAND-items-categorical-data").
For information on textual and categorical metadata see [Preparing item metadata for training](items-datasets.md "items-datasets.md").
For an example of
the default schema for Items datasets for ECOMMERCE domains, see [Default Items schema (VIDEO_ON_DEMAND domain)](#VIDEO-ON-DEMAND-items-dataset-schema "#VIDEO-ON-DEMAND-items-dataset-schema").

## Using categorical data

To use categorical data, add a field of type `string` and set the field's categorical attribute to `true` in your schema.
Then include the categorical data in your bulk CSV file and individual item imports. Categorical values can have at most 1000 characters. If you have an item with a categorical
value with more than 1000 characters, your dataset import job will fail.

For items with multiple categories, separate each value with the vertical bar, '|'. For example, for a GENRES field your data for an item might be
`Action|Crime|Biopic`. If you have a multiple levels of categorical data and some items have multiple categories for each level in the hierarchy, add a field for each level and append a level indicator after each field name:
GENRES, GENRE_L2, GENRE_L3. This allows you filter recommendations based on sub-categories, even if an item belongs to multiple multi-level categories.
For example, a video might have the following data for each category level:

- GENRES: Action|Adventure
- GENRE_L2: Crime|Western
- GENRE_L3: biopic

In this example, the video is in the action > crime > biopic hierarchy _and_ the adventure > western > biopic hierarchy.
We recommend only using up to L3 but you can use more levels if necessary. For information on creating and using filters, see
[Filtering recommendations and user segments](filter.md "filter.md").

## Default Items schema (VIDEO_ON_DEMAND domain)

The following is the default schema for Items datasets for the VIDEO_ON_DEMAND domain.

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
      "name": "GENRES",
      "type": [
        "string"
      ],
      "categorical": true
    },
    {
      "name": "CREATION_TIMESTAMP",
      "type": "long"
    }
  ],
  "version": "1.0"
}
```
