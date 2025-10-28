End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# Exercise 2: Add a New Utterance

(AWS CLI)

To improve the machine learning model that Amazon Lex uses to recognize requests from your
users, add another sample utterance to the bot.

Adding a new utterance is a four-step process.

1. Use the [GetIntent](API_GetIntent.md "API_GetIntent.md")
   operation to get an intent from Amazon Lex.
2. Update the intent.
3. Use the [PutIntent](API_PutIntent.md "API_PutIntent.md")
   operation to send the updated intent back to Amazon Lex.
4. Use the [GetBot](API_GetBot.md "API_GetBot.md") and [PutBot](API_PutBot.md "API_PutBot.md") operations to rebuild any
   bot that uses the intent.
   To run the commands in this exercise, you need to know the region where the commands
   will be run. For a list of regions, see [Model Building
   Quotas](gl-limits.md#gl-limits-model-building "gl-limits.md#gl-limits-model-building") .

The response from the `GetIntent` operation contains a field called
`checksum` that identifies a specific revision of the intent. You must
provide the checksum value when you use the [PutIntent](API_PutIntent.md "API_PutIntent.md") operation to update an intent. If you don't, you'll
get the following error message:

```

            An error occurred (PreconditionFailedException) when calling
            the PutIntent operation: Intent intent name already exists.
            If you are trying to update intent name you must specify the
            checksum.

```

###### Note

The following AWS CLI example is formatted for Unix, Linux, and macOS. For Windows,
change `"\$LATEST"` to `$LATEST` and replace the backslash (\)
continuation character at the end of each line with a caret (^).

###### To update the `OrderFlowers` intent (AWS CLI)

1. In the AWS CLI, get the intent from Amazon Lex. Amazon Lex sends the output to a file
   called `OrderFlowers-V2.json.`

```
aws lex-models get-intent \
    --region `region` \
    --name OrderFlowers \
    --intent-version "\$LATEST" > OrderFlowers-V2.json
```

2. Open `OrderFlowers-V2.json` in a text editor.
   1. Find and delete the `createdDate`,
      `lastUpdatedDate`, and `version`
      fields.
   2. Add the following to the `sampleUtterances` field:

   ```
   I want to order flowers
   ```

   3. Save the file.

3. Send the updated intent to Amazon Lex with the following command:

```
aws lex-models put-intent  \
    --region `region` \
    --name OrderFlowers \
    --cli-input-json file://OrderFlowers-V2.json
```

Amazon Lex sends the following response:
Now that you have updated the intent, rebuild any bot that uses it.

###### To rebuild the `OrderFlowersBot` bot (AWS CLI)

1. In the AWS CLI, get the definition of the `OrderFlowersBot` bot and
   save it to a file with the following command:

```
aws lex-models get-bot \
    --region `region` \
    --name OrderFlowersBot \
    --version-or-alias "\$LATEST" > OrderFlowersBot-V2.json
```

2. In a text editor, open `OrderFlowersBot-V2.json`. Remove
   the `createdDate`, `lastUpdatedDate`, `status`
   and `version` fields.
3. In a text editor, add the following line to the bot definition:

```
"processBehavior": "BUILD",
```

4. In the AWS CLI, build a new revision of the bot by running the following command
   to :

```
aws lex-models put-bot \
    --region `region` \
    --name OrderFlowersBot \
    --cli-input-json file://OrderFlowersBot-V2.json
```

The response from the server is:

## Next Step

[Exercise 3: Add a Lambda Function (AWS CLI)](gs-cli-update-lambda.md "gs-cli-update-lambda.md")
