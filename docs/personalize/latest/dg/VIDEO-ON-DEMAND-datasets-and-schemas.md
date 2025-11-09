# VIDEO_ON_DEMAND datasets and

schemas

When you create a Domain dataset group for the VIDEO_ON_DEMAND domain, each dataset type has a default schema with a set of VIDEO_ON_DEMAND specific required and recommended fields.
You can either use the default schema or create a new one based on the default schema.
The data you import must match your schema in format and type. Use the default domain schemas listed in the sections below as a guide to determine what data to import to create your VIDEO_ON_DEMAND-based recommender.

You are free to add additional fields. As long as the fields aren't listed as required or reserved,
and the data types are listed in [Schema data types](how-it-works-dataset-schema.md#personalize-datatypes "how-it-works-dataset-schema.md#personalize-datatypes"), the field names and data types
are up to you.

For information about general Amazon Personalize schema requirements, such as formatting requirements and available field data types, see [Creating schema JSON files for Amazon Personalize schemas](how-it-works-dataset-schema.md "how-it-works-dataset-schema.md"). These requirements
apply to all schemas, regardless of domain.

The following topics provide information about each dataset's required and recommended fields for the VIDEO_ON_DEMAND domain. Each dataset section includes the default VIDEO_ON_DEMAND schema in JSON format.

###### Topics

- [VIDEO_ON_DEMAND domain dataset and schema requirements](#VIDEO-ON-DEMAND-dataset-requirements "#VIDEO-ON-DEMAND-dataset-requirements")
- [Item interactions dataset requirements
  (VIDEO_ON_DEMAND domain)](VIDEO-ON-DEMAND-interactions-dataset.md "VIDEO-ON-DEMAND-interactions-dataset.md")
- [Users dataset requirements (VIDEO_ON_DEMAND domain)](VIDEO-ON-DEMAND-users-dataset.md "VIDEO-ON-DEMAND-users-dataset.md")
- [Items dataset requirements (VIDEO_ON_DEMAND domain)](VIDEO-ON-DEMAND-items-dataset.md "VIDEO-ON-DEMAND-items-dataset.md")

## VIDEO_ON_DEMAND domain dataset and schema requirements

Each dataset type has the following required fields and reserved keywords. Reserved
keywords are optional, non-metadata fields. These fields are considered reserved because you
must define the fields as their required data type when you use them. Reserved categorical string fields must have `categorical` set to `true`, while reserved string fields can't be
categorical. The keywords can't be in your data.

| Dataset type                                                                                                                                                                                    | Required fields                                                                                                                                                                                 | Reserved keywords                                                                                                                                                                                                                                                                                                                          |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Item interactions ([default schema](VIDEO-ON-DEMAND-interactions-dataset.md#VIDEO-ON-DEMAND-interactions-schema "VIDEO-ON-DEMAND-interactions-dataset.md#VIDEO-ON-DEMAND-interactions-schema")) | USER_ID (`string`)<br>ITEM_ID (`string`)<br>TIMESTAMP (`long`)<br>EVENT_TYPE (`string` and depending on [use case](domain-use-cases.md "domain-use-cases.md"), `Watch` and `Click` event types) | EVENT_VALUE (`float`, `null`)<br>IMPRESSION (`string`, `null`)<br>RECOMMENDATION_ID (`string`, `null`)<br>EVENT_ATTRIBUTION_SOURCE (`string`, `null`)                                                                                                                                                                                      |
| Users ([default schema](VIDEO-ON-DEMAND-users-dataset.md#VIDEO-ON-DEMAND-users-dataset-schema "VIDEO-ON-DEMAND-users-dataset.md#VIDEO-ON-DEMAND-users-dataset-schema"))                         | USER_ID (`string`)<br>1 metadata field (categorical `string` or numerical)                                                                                                                      | SUBSCRIPTION_MODEL (categorical `string`, `null`)                                                                                                                                                                                                                                                                                          |
| Items ([default schema](VIDEO-ON-DEMAND-items-dataset.md#VIDEO-ON-DEMAND-items-dataset-schema "VIDEO-ON-DEMAND-items-dataset.md#VIDEO-ON-DEMAND-items-dataset-schema"))                         | ITEM_ID (`string`)<br>CREATION_TIMESTAMP (`long`)<br>GENRES (categorical `string`)                                                                                                              | PRICE (`float`, `null`)<br>DURATION (`float`, `null`)<br>GENRE_L2 (categorical `string`, `null`)<br>GENRE_L3 (categorical `string`, `null`)<br>AVERAGE_RATING (`float`, `null`)<br>PRODUCT_DESCRIPTION (textual `string`, `null`)<br>CONTENT_OWNER (categorical `string`, `null`)<br>CONTENT_CLASSIFICATION (categorical `string`, `null`) |
