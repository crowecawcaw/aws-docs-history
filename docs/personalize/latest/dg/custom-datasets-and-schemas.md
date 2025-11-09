# Custom datasets and

schemas

When you create a Custom dataset group, you create your own schemas
from scratch. Custom dataset group datasets and schemas have fewer
required fields and more flexibility. The following topics explain the
schema and data requirements for datasets
a Custom dataset group. Each dataset section lists the required data for
the dataset type and provides a JSON example of a schema.

For information on the types of data you can import into Amazon Personalize see
[Types of data Amazon Personalize can use](datasets.md "datasets.md"). For information about general
Amazon Personalize schema requirements, such as formatting requirements and available
field data types, see [Creating schema JSON files for Amazon Personalize schemas](how-it-works-dataset-schema.md "how-it-works-dataset-schema.md"). These requirements apply to
all Amazon Personalize schemas.

###### Topics

- [Custom dataset and schema
  requirements](#dataset-requirements "#dataset-requirements")
- [Item interactions dataset schema
  requirements (custom)](interactions-dataset-requirements.md "interactions-dataset-requirements.md")
- [Users dataset schema requirements
  (custom)](user-dataset-requirements.md "user-dataset-requirements.md")
- [Items dataset schema requirements
  (custom)](item-dataset-requirements.md "item-dataset-requirements.md")
- [Actions dataset schema requirements (custom)](action-dataset-requirements.md "action-dataset-requirements.md")
- [Action interactions dataset schema requirements (custom)](action-interactions-dataset-requirements.md "action-interactions-dataset-requirements.md")

## Custom dataset and schema

requirements

When you create a dataset for a Custom dataset group, each dataset
type has the following required fields and reserved keywords with required
data types.

| Dataset type                                                                                                                                                                                              | Required fields                                                                                      | Reserved keywords                                                                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Item interactions ([schema example](interactions-dataset-requirements.md#schema-examples-interactions "interactions-dataset-requirements.md#schema-examples-interactions"))                               | USER_ID (`string`)<br>ITEM_ID (`string`)<br>TIMESTAMP (`long`)                                       | EVENT_TYPE (`string`)<br>EVENT_VALUE (`float`, `null`)<br>IMPRESSION (`string`, `null`)<br>RECOMMENDATION_ID (`string`,<br>`null`)<br>EVENT_ATTRIBUTION_SOURCE (`string`, `null`) |
| Users ([schema<br>example](user-dataset-requirements.md#schema-examples-users "user-dataset-requirements.md#schema-examples-users"))                                                                      | USER_ID (`string`)<br>1 metadata field (categorical `string` or<br>numerical)                        |                                                                                                                                                                                   |
| Items ([schema<br>example](item-dataset-requirements.md#schema-examples-items "item-dataset-requirements.md#schema-examples-items"))                                                                      | ITEM_ID (`string`)<br>1 metadata field (categorical or textual `string`<br>field or numerical field) | CREATION_TIMESTAMP (`long`)                                                                                                                                                       |
| Actions ([schema example](action-dataset-requirements.md#schema-examples-actions "action-dataset-requirements.md#schema-examples-actions"))                                                               | ACTION_ID (`string`)<br>1 metadata field (categorical `string` or numerical)                         | CREATION_TIMESTAMP (`long`)<br>VALUE (`long`, `null`)<br>TYPE (`string`, `null`)<br>EXPIRATION_TIMESTAMP (`long`, `null`)<br>REPEAT_FREQUENCY (`long`, `null`)                    |
| Action interactions ([schema example](action-interactions-dataset-requirements.md#schema-examples-action-interactions "action-interactions-dataset-requirements.md#schema-examples-action-interactions")) | USER_ID (`string`)<br>ACTION_ID (`string`)<br>EVENT_TYPE (`string`)<br>TIMESTAMP (`long`)            | IMPRESSION (`string`, `null`)<br>RECOMMENDATION_ID (`string`, `null`)                                                                                                             |

### Metadata fields

Metadata includes string or non-string fields that aren't required
or don't use a reserved keyword. Metadata schemas have the following
restrictions:

- Users, Items, and Actions schemas require at least one metadata
  field.
- You can add at most 25 metadata fields for a
  Users schema, 100 metadata fields for an Items
  schema, and 10 metadata fields for an Actions schema.
- If you add your own metadata field of type `string`,
  it must include the `categorical` attribute or the
  `textual` attribute (only Items schemas support fields
  with the textual attribute). Otherwise, Amazon Personalize won't use the field
  when training a model.

### Reserved keywords

Reserved keywords are optional, non-metadata fields. These fields
are considered reserved because you must define the fields as their
required data type when you use them, and the keywords can't be used as
values in your data. Reserved categorical string fields must have
`categorical` set to `true`, while reserved
string fields can't be categorical. The following are reserved
keywords:

- EVENT_TYPE: For Item interactions datasets with one or more event
  types, such as both _click_ and
  _download_, use an `EVENT_TYPE`
  field. You must define an EVENT_TYPE field as a `string`
  and can't be set as categorical.
- EVENT_VALUE: For Item interactions datasets that include value data
  for events, such as the percentage of a video a user watched, use an
  `EVENT_VALUE` field with type `float` and
  optionally `null`.
- CREATION_TIMESTAMP: For Items or Actions datasets with a timestamp for
  each item’s creation date, use a `CREATION_TIMESTAMP`
  field with a type `long`. Amazon Personalize uses
  `CREATION_TIMESTAMP` data to calculate the age of an
  item and adjust recommendations accordingly. See [Creation timestamp data](items-datasets.md#creation-timestamp-data "items-datasets.md#creation-timestamp-data").
- IMPRESSION: For Item interactions datasets with explicit impressions
  data, use an `IMPRESSION` field with type
  `String` and optionally type `null`.
  Impressions are lists of items that were visible to a user when they
  interacted with (for example, clicked or watched) a particular item.
  For more information, see [Impressions data](interactions-datasets.md#interactions-impressions-data "interactions-datasets.md#interactions-impressions-data").
- RECOMMENDATION_ID: For Item interactions datasets that use previous
  recommendations as implicit impressions data, optionally use a
  `RECOMMENDATION_ID` field with type `String`
  and optionally type `null`.

You don't need to add a `RECOMMENDATION_ID` field for
Amazon Personalize to use implicit impressions when generating recommendations.
You can pass a `recommendationId` in a [PutEvents](API_UBS_PutEvents.md "API_UBS_PutEvents.md")
operation without it. For more information, see [Impressions data](interactions-datasets.md#interactions-impressions-data "interactions-datasets.md#interactions-impressions-data").

- VALUE: For Actions datasets, if you have value you data for some or all of your actions, add a `VALUE` field to your
  schema. For its type, use `long` and optionally type `null`. For more information about actions and their
  value, see [Value data](actions-datasets.md#action-value-data "actions-datasets.md#action-value-data").
- ACTION_EXPIRATION_TIMESTAMP: For Actions datasets, if you have an expiration timestamp for some or all of your actions,
  add a `ACTION_EXPIRATION_TIMESTAMP` field to your schema. For its type, use `long` and
  optionally type `null`. For more information about expiration timestamps, see [Action expiration timestamp data](actions-datasets.md#action-expiration-timestamp-data "actions-datasets.md#action-expiration-timestamp-data").
- REPEAT_FREQUENCY: For Actions datasets, if you have repeat frequency data for some or all of your actions, add a
  `REPEAT_FREQUENCY` field to your schema. For its type, use `long` and optionally type
  `null`. For more information about repeat frequency data, see [Repeat frequency data](actions-datasets.md#action-repeat-frequency "actions-datasets.md#action-repeat-frequency").
