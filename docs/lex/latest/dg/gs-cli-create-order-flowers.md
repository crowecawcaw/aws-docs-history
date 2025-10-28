End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# Step 3: Create an Intent

(AWS CLI)

Create an intent for the `OrderFlowersBot` bot and provide three slots,
or parameters. The slots allow the bot to fulfill the intent:

- `FlowerType` is a custom slot type that specifies which types
  of flowers can be ordered.
- `AMAZON.DATE` and `AMAZON.TIME` are built-in slot
  types used for getting the date and time to deliver the flowers from the
  user.
  To run the commands in this exercise, you need to know the region where the
  commands will be run. For a list of regions, see [Model Building
  Quotas](gl-limits.md#gl-limits-model-building "gl-limits.md#gl-limits-model-building") .

###### To create the `OrderFlowers` intent (AWS CLI)

1. Create a text file named `OrderFlowers.json`. Copy
   the JSON code from [OrderFlowers.json](gs-cli-create-order-flowers-json.md "gs-cli-create-order-flowers-json.md") into the text
   file.
2. In the AWS CLI, call the [PutIntent](API_PutIntent.md "API_PutIntent.md") operation to create the intent. The
   example is formatted for Unix, Linux, and macOS. For Windows, replace the
   backslash (\) Unix continuation character at the end of each line with a
   caret (^).

```
aws lex-models put-intent \
   --region `region` \
   --name OrderFlowers \
   --cli-input-json file://OrderFlowers.json
```

The server responds with the following:

## Next Step

[Step 4: Create a Bot
(AWS CLI)](gs-cli-create-order-flowers-bot.md "gs-cli-create-order-flowers-bot.md")
