# Item interactions dataset requirements (ECOMMERCE

domain)

An _Item interactions dataset_ stores historical and real-time data from interactions between users and items in your ECOMMERCE catalog.
For more information about the types of data you can store in an interactions dataset, see [Item interaction data](interactions-datasets.md "interactions-datasets.md").
For information about general Amazon Personalize schema requirements, such as formatting requirements and available field data types, see [Creating schema JSON files for Amazon Personalize schemas](how-it-works-dataset-schema.md "how-it-works-dataset-schema.md"). These requirements
apply to all schemas, regardless of domain.

You must at minimum create an Item interactions dataset and your schema must have the following fields:

- USER_ID (`string`)
- ITEM_ID (`string`)
- TIMESTAMP (`long`)
- EVENT_TYPE (`string` and depending on [use case](domain-use-cases.md "domain-use-cases.md"), `Purchase` and `View` event types)

Your schema can also include the following reserved keywords:

- EVENT_VALUE (`float`, `null`)
- IMPRESSION (`string`, `null`)
- RECOMMENDATION_ID (`string`, `null`)

The data you import must match your schema. You are free to add additional fields depending on your use case and your data. As long as the fields aren't listed as required or reserved, and the data types are listed in [Schema data types](how-it-works-dataset-schema.md#personalize-datatypes "how-it-works-dataset-schema.md#personalize-datatypes"), the field names and data types are up to you. For an example of
the default schema for Item interactions datasets for ECOMMERCE domains, see [Default Interactions schema (ECOMMERCE domain)](#ECOMMERCE-interactions-schema "#ECOMMERCE-interactions-schema").

Optionally add the
reserved keyword EVENT_VALUE if you have value data for events. Optionally add the reserved keyword IMPRESSION if you want to include explicit and implicit impressions data.
For more information about recording impressions data see [Impressions data](interactions-datasets.md#interactions-impressions-data "interactions-datasets.md#interactions-impressions-data").

The maximum total number of optional metadata fields you can add to an Item interactions dataset, combined with total number of _distinct_ event types in your
Item interaction data,
is 10. The metadata fields included in this count are
EVENT_TYPE, EVENT_VALUE fields along with any custom metadata fields you add to your schema. The maximum number of metadata fields excluding reserved fields, such as
IMPRESSION, is 5. Categorical values can have at most 1000 characters. If you have an interaction with a categorical
value with more than 1000, your dataset import job will fail.

For more information on minimum requirements and maximum data limits for an Item interactions dataset for the ECOMMERCE domain, see [Service quotas](limits.md#limits-table "limits.md#limits-table").

## Default Interactions schema (ECOMMERCE domain)

The following is the default ECOMMERCE domain schema for Item interactions datasets.

```
{

  "type": "record",
  "name": "Interactions",
  "namespace": "com.amazonaws.personalize.schema",
  "fields": [
      {
          "name": "USER_ID",
          "type": "string"
      },
      {
          "name": "ITEM_ID",
          "type": "string"
      },
      {
          "name": "EVENT_TYPE",
          "type": "string"
      },
      {
          "name": "TIMESTAMP",
          "type": "long"
      }
  ],
  "version": "1.0"
}
```
