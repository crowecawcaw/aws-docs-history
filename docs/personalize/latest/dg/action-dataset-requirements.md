# Actions dataset schema requirements (custom)

An _action_ is an engagement activity that you might want to recommend to your customers. Actions might
include installing your mobile app, completing a membership profile, joining your loyalty program, or signing up for
promotional emails. An _Actions dataset_ stores data about your actions. For information
about the types of action data you can import into Amazon Personalize, see [Action metadata](actions-datasets.md "actions-datasets.md").

The data you provide for each action must match your Actions dataset schema. Depending on your schema, action metadata
can include empty/null values.

At minimum, you must provide an Action ID for each item (max length 256 characters). Your schema must
have an minimum one metadata field, but if you add a `null` type, this value can be null for the action. You can
add additional fields depending on your use case and your data. You can choose the field names and data types unless the
fields are listed as required or reserved, and the data types are listed in [Schema data types](how-it-works-dataset-schema.md#personalize-datatypes "how-it-works-dataset-schema.md#personalize-datatypes").

To add a categorical field, add a field of type `string` and set the field's categorical attribute to
`true` in your schema. Then include the categorical data in your bulk CSV file and individual action imports.
Categorical values can have at most 1000 characters. If you have an action with a categorical value with more than
1000 characters, your dataset import job will fail.

For more information on minimum requirements and maximum data limits for an Actions dataset, see [Service quotas](limits.md#limits-table "limits.md#limits-table").

## Actions dataset schema example (custom)

The following example shows how to structure an Actions schema. The `ACTION_ID` field is required. The
`MEMBERSHIP_LEVEL` field is a categorical string field. The `VALUE`,
`CREATION_TIMESTAMP`, and `REPEAT_FREQUENCY` fields are reserved keywords with the required types. You
can add a maximum of 10 columns. For information about schema requirements, see [Custom dataset and schema
requirements](custom-datasets-and-schemas.md#dataset-requirements "custom-datasets-and-schemas.md#dataset-requirements").

```
{
  "type": "record",
  "name": "Actions",
  "namespace": "com.amazonaws.personalize.schema",
  "fields": [
    {
      "name": "ACTION_ID",
      "type": "string"
    },
    {
      "name": "VALUE",
      "type": [
        "null",
        "long"
      ]
    },

    {
      "name": "MEMBERSHIP_LEVEL",
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
      "name": "REPEAT_FREQUENCY",
      "type": [
        "long",
        "null"
      ]
    }
  ],
  "version": "1.0"
}
```

For this schema, the first few lines of historical data in a CSV file might look like the following.

```
ACTION_ID,VALUE,MEMBERSHIP_LEVEL,CREATION_TIMESTAMP,REPEAT_FREQUENCY
1,10,Deluxe|Premium,1510003267,7
2,5,Basic,1580003267,7
3,5,Preview,1590003267,3
4,10,Deluxe|Platinum,1560003267,4
...
...
```
