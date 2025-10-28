End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# JSON Format for Importing and Exporting

The following examples show the JSON structure for exporting and importing slot
types, intents, and bots in Amazon Lex format.

## Slot Type structure

The following is the JSON structure for custom slot types. Use this structure
when you import or export slot types, and when you export intents that depend on
custom slot types.

```
{
  "metadata": {
    "schemaVersion": "1.0",
    "importType": "LEX",
    "importFormat": "JSON"
  },
  "resource": {
    "name": "`slot type name`",
    "version": "`version number`",
    "enumerationValues": [
      {
        "value": "`enumeration value`",
        "synonyms": []
      },
      {
        "value": "`enumeration value`",
        "synonyms": []
      }
    ],
    "valueSelectionStrategy": "`ORIGINAL_VALUE or TOP_RESOLUTION`"
  }
}
```

## Intent structure

The following is the JSON structure for intents. Use this structure when you
import or export intents and bots that depend on an intent.

## Bot structure

The following is the JSON structure for bots. Use this structure when you
import or export bots.
