# Preparing item metadata for training

Item metadata includes numerical and categorical data about the items your users interact with. Examples of item metadata
include creation timestamp, price, genre, description, and availability. You import metadata about your items into an Amazon Personalize
_Items dataset_.

Depending on your domain use case or custom recipe, item metadata can help Amazon Personalize recommend more relevant items to users,
more accurately predict similar items, or recommend more meaningful user segments. And it can help Amazon Personalize feature new items in recommendations. Item metadata is
required for some domain use cases and optional for all custom recipes. For more information, see the data requirements for your domain use case
or recipe in [Matching your use case to Amazon Personalize resources](use-cases-and-recipes.md "use-cases-and-recipes.md").

When training, Amazon Personalize doesn't use non-categorical string item data, such as item titles or author data.
However, importing this data can still enhance recommendations. For more information, see [Non-categorical string data](#item-string-data "#item-string-data").

The maximum number items Amazon Personalize considers during training depends on your use case or recipe. Only items considered during
training can appear in recommendations.

- For User-Personalization-v2 or Personalized-Ranking-v2, the maximum number of items that are considered by a model during
  training is 5 million. These items are from both the Items and Item interactions dataset.
- For all domain use cases and custom recipes other than User-Personalization-v2 and Personalized-Ranking-v2, the maximum number
  of items that are considered by a model during training and generating recommendations is 750,000.
  For all domain use cases and custom recipes, your bulk item data must be in a CSV file. Each row in the file should
  represent a unique item. After you finish preparing your data, you are ready to create a schema JSON file. This file tells Amazon Personalize about the
  structure of your data. For more information, see [Creating schema JSON files for Amazon Personalize schemas](how-it-works-dataset-schema.md "how-it-works-dataset-schema.md").

The following sections provide more information on how to prepare your item metadata for Amazon Personalize. For
bulk data format guidelines for all types of data, see [bulk data format guidelines](preparing-training-data.md#general-formatting-guidelines "preparing-training-data.md#general-formatting-guidelines")

###### Topics

- [Item data requirements](#item-data-requirements "#item-data-requirements")
- [Creation timestamp data](#creation-timestamp-data "#creation-timestamp-data")
- [Categorical metadata](#item-categorical-data "#item-categorical-data")
- [Unstructured text metadata](#text-data "#text-data")
- [Numerical data](#item-numerical-data "#item-numerical-data")
- [Non-categorical string data](#item-string-data "#item-string-data")
- [Items metadata example](#items-data-example "#items-data-example")

## Item data requirements

The following are item metadata requirements for Amazon Personalize.

If you aren't sure you have enough data or if you have questions about its quality, you can import your data into an
Amazon Personalize dataset and use Amazon Personalize to analyze it. For more information, see [Analyzing quality and quantity of data in Amazon Personalize datasets](analyzing-data.md "analyzing-data.md").

- For all domain use cases and custom recipes, you must have an ITEM_ID column that stores the unique identifier for each item. Every item must have an item ID. It
  must be a `string` with a max length of 256 characters.
- For custom recipes, your data must have at least one categorical string or numerical metadata column. Item metadata columns can include empty/null values.
  We recommend that these columns be at minimum 70 percent complete.
- For domain use cases, the required columns depend on your domain. For more information, see [VIDEO_ON_DEMAND domain requirements](#vod-item-data-req "#vod-item-data-req") or
  [ECOMMERCE domain requirements](#retail-item-data-req "#retail-item-data-req").
- The maximum number of metadata columns is 100.

### VIDEO_ON_DEMAND domain requirements

An item metadata is required for some use cases (see [VIDEO_ON_DEMAND use
cases](VIDEO_ON_DEMAND-use-cases.md "VIDEO_ON_DEMAND-use-cases.md")). When optional,
we still recommend importing item metadata to get the most relevant recommendations. If you import item metadata, your data must include the following columns:

- ITEM_ID
- GENRES (categorical `string`)
- CREATION_TIMESTAMP (in Unix epoch time format)

The following lists additional recommended columns and their required types. The `null` type indicates that the column can have missing values.
We recommend that these columns be at minimum 70 percent complete.
Including these columns can improve recommendations.

- PRICE (float)
- DURATION (float)
- GENRE_L2 (categorical `string`, `null`)
- GENRE_L3 (categorical `string`, `null`)
- AVERAGE_RATING (`float`, `null`)
- PRODUCT_DESCRIPTION (textual `string`, `null`)
- CONTENT_OWNER (categorical `string`, `null`) – The company that owns the video. For example, values might be HBO, Paramount, and NBC.
- CONTENT_CLASSIFICATION (categorical `string`, `null`) – The content's rating. For example, values might be G, PG, PG-13, R, NC-17, and unrated.

### ECOMMERCE domain requirements

Item metadata is optional for all ECOMMERCE use cases. If you have item data,
we recommend importing it to get the most relevant recommendations. If you import item metadata, your data must have the following columns:

- ITEM_ID
- PRICE (`float`)
- CATEGORY_L1 (categorical `string`) – For information about formatting categorical data, see [Categorical metadata](#item-categorical-data "#item-categorical-data").

The following lists additional recommended columns and their required types. The `null` type indicates that the column can have missing values.
We recommend that these columns be at minimum 70 percent complete.
Including these columns can improve recommendations.

- CATEGORY_L2 (categorical `string`, `null`)
- CATEGORY_L3 (categorical `string`, `null`)
- PRODUCT_DESCRIPTION (textual `string`, `null`)
- CREATION_TIMESTAMP (`float`)
- AGE_GROUP (categorical `string`, `null`) – The age group the item is for. Values might be newborns, infants, children, and adults.
- ADULT (categorical `string`, `null`) – Whether the item is restricted to only adults, such as alcohol. Values might be yes or no.
- GENDER (categorical `string`, `null`) – The gender the item is for. Values might be male, female, and unisex.

## Creation timestamp data

Creation timestamp data must be in Unix epoch time format in seconds. For example, the Epoch timestamp in seconds for date
July 31, 2020 is 1596238243. To convert dates to Unix epoch timestamps, use an [Epoch converter - Unix timestamp converter](https://www.epochconverter.com "https://www.epochconverter.com").

Amazon Personalize uses creation timestamp data (in Unix epoch time format, in seconds) to calculate
the age of an item and adjust recommendations accordingly.

If creation timestamp data is missing for one or more items, Amazon Personalize infers
this information from interaction data, if any, and uses the timestamp of the item’s
oldest interaction data as the item's creation timestamp. If an item has no interaction data,
its creation timestamp is set as the timestamp of the latest interaction in the training set
and Amazon Personalize considers it a new item.

## Categorical metadata

With certain recipes and all domain use cases, Amazon Personalize uses categorical metadata, such as an item's genre or color, when identifying
underlying patterns that reveal the most relevant items for your users. You define your own range of values based on your use case. Categorical metadata can be in any language.

For items with multiple categories, separate each value with the
vertical bar, '|'. For example, for a GENRES field, your data for an item
might be `Action|Crime|Biopic`. If you have a multiple levels
of categorical data and some items have multiple categories for each level
in the hierarchy, use a separate column for each level and append a level indicator
after each field name: GENRES, GENRE_L2, GENRE_L3. This allows you to filter
recommendations based on sub-categories, even if an item belongs to
multiple multi-level categories (for information on creating and using
filters see [Filtering recommendations and user segments](filter.md "filter.md")). For example,
a video might have the following data for each category level:

- GENRES: Action|Adventure
- GENRE_L2: Crime|Western
- GENRE_L3: Biopic

In this example, the video is in the action > crime > biopic hierarchy
_and_ the adventure > western > biopic hierarchy. We
recommend only using up to L3 but you can use more levels if
necessary.

Categorical values can have a maximum of 1000 characters. If you have an item with a categorical
value with more than 1000 characters, your dataset import job will fail. We recommend categorical columns have at most 1000 possible values. Importing categorical data with more values
can negatively impact recommendations. The following can help you reduce the number of possible values for a categorical column:

- Make sure values follow a consistent naming convention and check for typos. For example, use "Men's Shoes" rather than having a mix of
  "Men's Shoes", "Mens Shoes", and "Male Footwear".
- Consolidate similar categories that use slightly different terms referring to the same underlying category, like
  "Shoes" and "Sneakers".
- If your data has a hierarchical structure,
  where broader categories (like "Footwear") contain more specific subcategories (such as "Men's Shoes", "Women's Shoes", "Children's Shoes"),
  use a separate column for each level and append a level indicator after each field name. For example, CATEGORY_1, CATEGORY_2, and CATEGORY_3.
  This can reduce ambiguous or overlapping categories.

With all recipes and domains, you can import categorical data and use it to filter recommendations based on an item's attributes. For information
about filtering recommendations, see [Filtering recommendations and user segments](filter.md "filter.md").

## Unstructured text metadata

With certain recipes and domains, Amazon Personalize can extract meaningful information from unstructured text metadata, such as product descriptions, product reviews, or movie synopses.
Amazon Personalize uses unstructured text to identify relevant items for your users, particularly when items are new or have less interactions data. You can add at most
1 textual field.
Include unstructured text data in your Items dataset to increase click-through rates and conversation rates for new items in your catalog.

When you prepare your unstructured text metadata, wrap the text in double
quotes and remove any new line characters. Use the `\` character to escape any double quotes or \ characters in your data.
Amazon Personalize truncates text fields at the character limit. Make sure that the most relevant
information in the text is at the start of the field.

Unstructured text values can have at most 20,000 characters in all languages except Chinese
and Japanese. For Chinese and Japanese, you can have at most 7,000 characters.
Amazon Personalize truncates values that exceed the character limit to the character limit.

You can submit unstructured text items in multiple languages, but each
item's text should be in only one language. Text can be in the following languages:

- Chinese (Simplified)
- Chinese (Traditional)
- English
- French
- German
- Japanese
- Portuguese
- Spanish

## Numerical data

Amazon Personalize can use numerical item metadata, such as price or video duration, to generate more relevant recommendations for
users. This numerical data can be represented as whole numbers or decimal values.

If you use the [User-Personalization](native-recipe-new-item-USER_PERSONALIZATION.md "native-recipe-new-item-USER_PERSONALIZATION.md") or
[Personalized-Ranking](native-recipe-search.md "native-recipe-search.md") custom recipes, you can optimize an Amazon Personalize solution for an
Item metadata related objective in addition to maximum relevance, such as maximizing revenue. When you configure your
solution, you choose the numerical metadata column in your Items dataset that is related to your objective. For example, you
might choose a VIDEO_LENGTH column to maximize streaming minutes or a PRICE column to maximize revenue.

For more information, see [Optimizing a solution for an additional
objective](optimizing-solution-for-objective.md "optimizing-solution-for-objective.md").

## Non-categorical string data

Except for item IDs, Amazon Personalize doesn't use non-categorical non-textual string data when training, such as item titles or author data.
However, Amazon Personalize can use it with the following features. Non-categorical values can have a maximum of 1000 characters.

- Amazon Personalize can include item metadata in recommendations, including non-categorical string values. You might use metadata to enrich recommendations in your user
  interface, such as adding the director's name to a movie recommendations carousel. For more information, see [Item metadata in recommendations](campaigns.md#create-campaign-return-metadata "campaigns.md#create-campaign-return-metadata").
- If you use [Similar-Items](native-recipe-similar-items.md "native-recipe-similar-items.md"),
  you can generate batch recommendations with themes. When you generate batch recommendations with themes, you
  must specify an item name column in the batch inference job. For more information, see [Batch recommendations with themes from Content Generator](themed-batch-recommendations.md "themed-batch-recommendations.md").
- You can create filters to include or remove items from recommendations based on non-categorical string data. For more information
  about filters, see [Filtering recommendations and user segments](filter.md "filter.md").

## Items metadata example

The first few lines of movie metadata in a CSV file might look like the following.

```
ITEM_ID,GENRES,CREATION_TIMESTAMP,DESCRIPTION
1,Adventure|Animation|Children|Comedy|Fantasy,1570003267,"This is an animated movie that features action, comedy, and fantasy. Audience is children. This movie was released in 2004."
2,Adventure|Children|Fantasy,1571730101,"This is an adventure movie with elements of fantasy. Audience is children. This movie was release in 2010."
3,Comedy|Romance,1560515629,"This is a romantic comedy. The movie was released in 1999. Audience is young women."
4,Comedy|Drama|Romance,1581670067,"This movie includes elements of both comedy and drama as well as romance. This movie was released in 2020."
...
...
```

The `ITEM_ID` column is required and stores unique identifiers for each individual item. The `GENRE` column stores categorical metadata for each movie and the
`DESCRIPTION` column is unstructured textual metadata. The `CREATION_TIMESTAMP` column stores each items creation time in Unix epoch time format in seconds.

After you finish preparing your data, you are ready to create a schema JSON file. This file tells Amazon Personalize about the
structure of your data. For more information, see [Creating schema JSON files for Amazon Personalize schemas](how-it-works-dataset-schema.md "how-it-works-dataset-schema.md").
This is what the schema JSON file would look like for
the above sample data.

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
        "null",
        "string"
      ],
      "categorical": true
    },
    {
      "name": "CREATION_TIMESTAMP",
      "type": "long"
    },
    {
      "name": "DESCRIPTION",
      "type": [
        "null",
        "string"
      ],
      "textual": true
    }
  ],
  "version": "1.0"
}
```
