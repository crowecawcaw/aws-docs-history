End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# Step 2: Create a Custom Slot Type

(AWS CLI)

Create a custom slot type with enumeration values for the flowers that can be
ordered. You use this type in the next step when you create the
`OrderFlowers` intent. A _slot type_ defines the
possible values for a slot, or parameter, of the intent.

To run the commands in this exercise, you need to know the region where the
commands will be run. For a list of regions, see [Model Building
Quotas](gl-limits.md#gl-limits-model-building "gl-limits.md#gl-limits-model-building") .

###### To create a custom slot type (AWS CLI)

1. Create a text file named `FlowerTypes.json`. Copy the
   JSON code from [FlowerTypes.json](gs-cli-create-flower-types-json.md "gs-cli-create-flower-types-json.md") into the text
   file.
2. Call the [PutSlotType](API_PutSlotType.md "API_PutSlotType.md")
   operation using the AWS CLI to create the slot type. The example is formatted
   for Unix, Linux, and macOS. For Windows, replace the backslash (\) Unix
   continuation character at the end of each line with a caret (^).

```
aws lex-models put-slot-type \
    --region `region` \
    --name FlowerTypes \
    --cli-input-json file://FlowerTypes.json
```

The response from the server is:

```
{
    "enumerationValues": [
        {
            "value": "tulips"
        },
        {
            "value": "lilies"
        },
        {
            "value": "roses"
        }
    ],
    "name": "FlowerTypes",
    "checksum": "checksum",
    "version": "$LATEST",
    "lastUpdatedDate": timestamp,
    "createdDate": timestamp,
    "description": "Types of flowers to pick up"
}
```

## Next Step

[Step 3: Create an Intent
(AWS CLI)](gs-cli-create-order-flowers.md "gs-cli-create-order-flowers.md")
