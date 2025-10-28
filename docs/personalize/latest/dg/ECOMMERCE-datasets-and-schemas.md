# ECOMMERCE datasets and schemas

When you create a Domain dataset group for the ECOMMERCE domain, each dataset type has a
default schema with a set of ECOMMERCE-specific required and recommended fields. You can use the
default schema or create a new one based on the default schema. The data you import must match
your schema in format and type. Use the default domain schemas listed in the sections below as a
guide to determine what data to import to create your ECOMMERCE-based recommender.

You are free to add additional fields. As long as the fields aren't listed as required or reserved,
and the data types are listed in [Schema data types](how-it-works-dataset-schema.md#personalize-datatypes "how-it-works-dataset-schema.md#personalize-datatypes"), the field names and data types
are up to you.

For information about general Amazon Personalize schema requirements, such as formatting requirements and available field data types, see [Creating schema JSON files for Amazon Personalize schemas](how-it-works-dataset-schema.md "how-it-works-dataset-schema.md"). These requirements
apply to all schemas, regardless of domain.

The following topics provide information about each dataset's required and recommended fields for the ECOMMERCE domain. Each dataset section includes the default ECOMMERCE schema in JSON format.

###### Topics

- [ECOMMERCE domain dataset and schema requirements](#ECOMMERCE-dataset-requirements "#ECOMMERCE-dataset-requirements")
- [Item interactions dataset requirements (ECOMMERCE
  domain)](ECOMMERCE-interactions-dataset.md "ECOMMERCE-interactions-dataset.md")
- [Users dataset requirements (ECOMMERCE domain)](ECOMMERCE-users-dataset.md "ECOMMERCE-users-dataset.md")
- [Items dataset requirements (ECOMMERCE domain)](ECOMMERCE-items-dataset.md "ECOMMERCE-items-dataset.md")

## ECOMMERCE domain dataset and schema requirements

Each dataset type has the following required fields and reserved keywords.
Reserved keywords are optional, non-metadata fields. These fields are considered reserved because you must define the fields
as their required data type when you use them. Reserved categorical string fields must have `categorical` set to `true`, while reserved string fields can't be
categorical. The keywords can't be in your data.

| Dataset type                                                                                                                                                            | Required fields                                                                                                                                                                          | Reserved keywords                                                                                                                                                                                                                                                                    |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Item interactions ([default schema](ECOMMERCE-interactions-dataset.md#ECOMMERCE-interactions-schema "ECOMMERCE-interactions-dataset.md#ECOMMERCE-interactions-schema")) | USER_ID (`string`) ITEM_ID (`string`) TIMESTAMP (`long`) EVENT_TYPE (`string` and depending on [use case](domain-use-cases.md "domain-use-cases.md"), `Purchase` and `View` event types) | EVENT_VALUE (`float`, `null`) IMPRESSION (`string`, `null`) RECOMMENDATION_ID (`string`, `null`) EVENT_ATTRIBUTION_SOURCE (`string`, `null`)                                                                                                                                         |
| Users ([default schema](ECOMMERCE-users-dataset.md#ECOMMERCE-users-dataset-schema "ECOMMERCE-users-dataset.md#ECOMMERCE-users-dataset-schema"))                         | USER_ID (`string`) 1 metadata field (categorical `string` or numerical)                                                                                                                  |                                                                                                                                                                                                                                                                                      |
| Items ([default schema](ECOMMERCE-items-dataset.md#ECOMMERCE-items-dataset-schema "ECOMMERCE-items-dataset.md#ECOMMERCE-items-dataset-schema"))                         | ITEM_ID (`string`) PRICE (`float`) CATEGORY_L1 (categorical `string`)                                                                                                                    | CATEGORY_L2 (categorical `string`, `null`) CATEGORY_L3 (categorical `string`, `null`) PRODUCT_DESCRIPTION (textual `string`, `null`) CREATION_TIMESTAMP (`long`) AGE_GROUP (categorical `string`, `null`) ADULT (categorical `string`, `null`) GENDER (categorical `string`, `null`) |
