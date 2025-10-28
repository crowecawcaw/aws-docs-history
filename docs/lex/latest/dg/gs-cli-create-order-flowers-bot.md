End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# Step 4: Create a Bot

(AWS CLI)

The `OrderFlowersBot` bot has one intent, the `OrderFlowers`
intent that you created in the previous step. To run the commands in this exercise,
you need to know the region where the commands will be run. For a list of regions,
see [Model Building
Quotas](gl-limits.md#gl-limits-model-building "gl-limits.md#gl-limits-model-building") .

###### Note

The following AWS CLI example is formatted for Unix, Linux, and macOS. For
Windows, change `"\$LATEST"` to `$LATEST`.

###### To create the `OrderFlowersBot` bot (AWS CLI)

1. Create a text file named `OrderFlowersBot.json`. Copy
   the JSON code from [OrderFlowersBot.json](gs-cli-create-order-flowers-bot-json.md "gs-cli-create-order-flowers-bot-json.md") into the text
   file.
2. In the AWS CLI, call the [PutBot](API_PutBot.md "API_PutBot.md") operation to create the bot. The example is
   formatted for Unix, Linux, and macOS. For Windows, replace the backslash (\)
   Unix continuation character at the end of each line with a caret (^).

```
aws lex-models put-bot \
    --region `region` \
    --name OrderFlowersBot \
    --cli-input-json file://OrderFlowersBot.json
```

The response from the server follows. When you create or update bot, the
`status` field is set to `BUILDING`. This
indicates that the bot isn't ready to use. To determine when the bot is
ready for use, use the [GetBot](API_GetBot.md "API_GetBot.md") operation in the next step . 3. To determine if your new bot is ready for use, run the following command.
Repeat this command until the `status` field returns
`READY`. The example is formatted for Unix, Linux, and macOS.
For Windows, replace the backslash (\) Unix continuation character at the
end of each line with a caret (^).

```
aws lex-models get-bot \
    --region `region` \
    --name OrderFlowersBot \
    --version-or-alias "\$LATEST"
```

Look for the `status` field in the response:

```
{
    "status": "READY",

    ...

}

```

## Next Step

[Step 5: Test a Bot (AWS CLI)](gs-create-test.md "gs-create-test.md")
