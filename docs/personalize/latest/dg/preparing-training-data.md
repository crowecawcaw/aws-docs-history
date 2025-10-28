# Preparing training data for Amazon Personalize

After you [choose a domain use case or recipe](use-cases-and-recipes.md "use-cases-and-recipes.md") and note its data requirements,
you are ready to start preparing your data. Amazon Personalize can use the following types of data:

- [Item interactions](interactions-datasets.md "interactions-datasets.md") – In Amazon Personalize,
  an _item interaction_ is a positive interaction event between a user and an item in your catalogue.
  For example, a user watching a movie, viewing a listing, or purchasing a pair of shoes.
- [Items](items-datasets.md "items-datasets.md") – Item metadata might include
  information such as price, SKU type, description, or availability for each item in your catalog.
- [Users](users-datasets.md "users-datasets.md") – User metadata might include
  information such as age, gender, loyalty membership, and interest for each of your users.
- [Actions](actions-datasets.md "actions-datasets.md") – An _action_ is an engagement activity that you might want to recommend to your customers. Actions might
  include installing your mobile app, completing a membership profile, joining your loyalty program, or signing up for promotional emails. For the
  Next-Best-Action recipe, the Actions dataset is required. No other custom recipe or domain use case uses Actions data.
- [Action interactions](action-interactions-datasets.md "action-interactions-datasets.md") – An action interaction is an
  interaction event between a user and an action. The Next-Best-Action recipe uses this data and the data in your Actions
  dataset to recommend actions to your users. No other custom recipe or domain use case uses Action-interactions data.
  Amazon Personalize stores data in _datasets_, one for each type of data. Each dataset has different requirements.
  When you import data into an Amazon Personalize dataset, you can choose to import records in bulk, individually, or both. Bulk imports
  involve importing a large number of historical records stored in one or more CSV files in an Amazon S3 bucket.

- If you don't have bulk data, you can use individual import operations to collect data and stream events until you meet
  Amazon Personalize training requirements and the data requirements of your domain use case or recipe. For information about recording events,
  see [Recording real-time events to influence recommendations](recording-events.md "recording-events.md"). For information about importing individual
  records, see [Importing individual records into an Amazon Personalize dataset](incremental-data-updates.md "incremental-data-updates.md").
- If you aren't sure you have enough data or if you have questions about its quality, you can import your data into an
  Amazon Personalize dataset and use Amazon Personalize to analyze it. For more information, see [Analyzing quality and quantity of data in Amazon Personalize datasets](analyzing-data.md "analyzing-data.md").
  The following sections provide data requirements for each Amazon Personalize dataset type and guidelines for preparing bulk data. If
  you don't have bulk data, review the sections to understand the required and optional data you can
  import with individual import operations. If you need additional help formatting your data, you can use Amazon SageMaker AI Data Wrangler (Data Wrangler) to prepare your data.
  For more information, see [Preparing and importing bulk data using Amazon SageMaker AI Data Wrangler](preparing-importing-with-data-wrangler.md "preparing-importing-with-data-wrangler.md").

After you finish preparing your data, you are ready to create a schema JSON file. This file tells Amazon Personalize about the
structure of your data. For more information, see [Creating schema JSON files for Amazon Personalize schemas](how-it-works-dataset-schema.md "how-it-works-dataset-schema.md").

###### Topics

- [Bulk data format guidelines for all types of data](#general-formatting-guidelines "#general-formatting-guidelines")
- [Preparing item interaction data for training](interactions-datasets.md "interactions-datasets.md")
- [Preparing item metadata for training](items-datasets.md "items-datasets.md")
- [Preparing user metadata for training](users-datasets.md "users-datasets.md")
- [Preparing action metadata for training](actions-datasets.md "actions-datasets.md")
- [Preparing action interaction data for training](action-interactions-datasets.md "action-interactions-datasets.md")

## Bulk data format guidelines for all types of data

The following guidelines and requirements can help you make sure your bulk data is formatted correctly.

- Your input data must be in a CSV (comma-separated values) file.
- The first row of your CSV file must contain your column headers. Don't enclose headers in quotation marks (").
- Columns must have unique alphanumeric names. For example,
  you can't add both a `GENRES_FIELD_1` field and a `GENRESFIELD1` field.
- If you are imporitng multiple CSV files, all column headers must match across all files.
- Make sure you have the required fields for your dataset type and make sure that their names align with Amazon Personalize
  requirements. For example, your Items data might have a column called `ITEM_IDENTIFICATION_NUMBER` with IDs for
  each of your items. To use this column as an ITEM_ID field, rename the column to `ITEM_ID`. If you use Data Wrangler to
  format your data, you can use the **Map columns for Amazon Personalize** Data Wrangler transform to make sure your columns are
  named correctly.

For information about using Data Wrangler to prepare your data, see [Preparing and importing bulk data using Amazon SageMaker AI Data Wrangler](preparing-importing-with-data-wrangler.md "preparing-importing-with-data-wrangler.md").

- Each record in your CSV file must be on a single line.
- Amazon Personalize doesn't support complex data types such as arrays and maps.
- To have Amazon Personalize use boolean data when training or filtering,
  use string values `"True"` and `"False"` or numeric values `1` for true and `0` for false.
- If you use Data Wrangler to
  format your data, you can use the Data Wrangler transform [Parse Value as
  Type](../../../sagemaker/latest/dg/data-wrangler-transform.md#data-wrangler-transform-cast-type "../../../sagemaker/latest/dg/data-wrangler-transform.md#data-wrangler-transform-cast-type") to convert the data types.
- `TIMESTAMP` and `CREATION_TIMESTAMP` data must be in _UNIX epoch_ time
  format. For more information, see [Timestamp data](interactions-datasets.md#timestamp-data "interactions-datasets.md#timestamp-data").
- Avoid including any `"` characters or special characters in item ID, user ID, and action ID data.
- If your data includes any non-ASCII encoded characters, your CSV file must be encoded in UTF-8 format.
- Makes sure you format any textual data as described in [Unstructured text metadata](items-datasets.md#text-data "items-datasets.md#text-data").
