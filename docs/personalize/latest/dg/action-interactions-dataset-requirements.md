# Action interactions dataset schema requirements (custom)

An _Action interactions dataset_ stores historical and real-time data from
interactions between users and actions in your _Actions dataset_. For information on the types of data Amazon Personalize can use, see
[Action interaction data](action-interactions-datasets.md "action-interactions-datasets.md").

The data you provide for each interaction must match your schema. Depending on your schema, interaction metadata can
include empty/null values. At minimum, your schema must include the following:

- USER_ID
- ACTION_ID
- TIMESTAMP
- EVENT_TYPE
  You can add additional fields depending on your use case and your data. You can choose the field names and data types
  unless the fields are listed as required or reserved, and the data types are listed in [Schema data types](how-it-works-dataset-schema.md#personalize-datatypes "how-it-works-dataset-schema.md#personalize-datatypes").

For more information about minimum requirements and maximum data limits for an Action interactions dataset, see [Service quotas](limits.md#limits-table "limits.md#limits-table").

## Action interactions dataset schema example (custom)

The following example shows a schema for an Action interactions dataset with only the required fields. For information about
general schema formatting requirements, see [Schema formatting requirements](how-it-works-dataset-schema.md#general-schema-requirements "how-it-works-dataset-schema.md#general-schema-requirements").

```
{

  "type": "record",
  "name": "ActionInteractions",
  "namespace": "com.amazonaws.personalize.schema",
  "fields": [
      {
          "name": "USER_ID",
          "type": "string"
      },
      {
          "name": "ACTION_ID",
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

For this schema, the first few lines of historical data in a CSV file might look like the following.

```
USER_ID,ACTION_ID,EVENT_TYPE,TIMESTAMP
35,73,Viewed,1586731606
54,35,Not taken,1586731609
9,33,Viewed,1586735158
23,10,Taken,1586735697
27,11,Taken,1586735763
...
...
```
