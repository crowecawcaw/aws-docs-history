End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# Exercise 3: Add a Lambda Function (AWS CLI)

Add a Lambda function that validates user input and fulfills the user's intent to the
bot.

Adding a Lambda expression is a five-step process.

1. Use the Lambda [AddPermission](../../../lambda/latest/dg/API_AddPermission.md "../../../lambda/latest/dg/API_AddPermission.md") function to enable the `OrderFlowers`
   intent to call the Lambda [Invoke](../../../lambda/latest/dg/lambda-api-permissions-ref.md "../../../lambda/latest/dg/lambda-api-permissions-ref.md") operation.
2. Use the [GetIntent](API_GetIntent.md "API_GetIntent.md")
   operation to get the intent from Amazon Lex.
3. Update the intent to add the Lambda function.
4. Use the [PutIntent](API_PutIntent.md "API_PutIntent.md")
   operation to send the updated intent back to Amazon Lex.
5. Use the [GetBot](API_GetBot.md "API_GetBot.md") and [PutBot](API_PutBot.md "API_PutBot.md") operations to rebuild any
   bot that uses the intent.
   To run the commands in this exercise, you need to know the region where the commands
   will be run. For a list of regions, see [Model Building
   Quotas](gl-limits.md#gl-limits-model-building "gl-limits.md#gl-limits-model-building") .

If you add a Lambda function to an intent before you add the
`InvokeFunction` permission, you get the following error message:

```

            An error occurred (BadRequestException) when calling the
            PutIntent operation: Lex is unable to access the Lambda
            function Lambda function ARN in the context of intent
            intent ARN.  Please check the resource-based policy on
            the function.

```

The response from the `GetIntent` operation contains a field called
`checksum` that identifies a specific revision of the intent. When you
use the [PutIntent](API_PutIntent.md "API_PutIntent.md") operation to
update an intent, you must provide the checksum value. If you don't, you get the
following error message:

```

            An error occurred (PreconditionFailedException) when calling
            the PutIntent operation: Intent intent name already exists.
            If you are trying to update intent name you must specify the
            checksum.

```

This exercise uses the Lambda function from [Exercise 1: Create an Amazon Lex Bot Using a
Blueprint (Console)](gs-bp.md "gs-bp.md"). For instructions to create the Lambda function, see [Step 3: Create a
Lambda Function (Console)](gs-bp-create-lambda-function.md "gs-bp-create-lambda-function.md").

###### Note

The following AWS CLI example is formatted for Unix, Linux, and macOS. For Windows,
change `"\$LATEST"` to `$LATEST`.

###### To add a Lambda function to an intent

1. In the AWS CLI, add the `InvokeFunction` permission for the
   `OrderFlowers` intent:

```
aws lambda add-permission \
    --region `region` \
    --function-name OrderFlowersCodeHook \
    --statement-id LexGettingStarted-OrderFlowersBot \
    --action lambda:InvokeFunction \
    --principal lex.amazonaws.com \
    --source-arn "arn:aws:lex:`region`:`account ID`:intent:OrderFlowers:*"
    --source-account `account ID`
```

Lambda sends the following response:

```
{
    "Statement": "{\"Sid\":\"LexGettingStarted-OrderFlowersBot\",
      \"Resource\":\"arn:aws:lambda:region:account ID:function:OrderFlowersCodeHook\",
      \"Effect\":\"Allow\",
      \"Principal\":{\"Service\":\"lex.amazonaws.com\"},
      \"Action\":[\"lambda:InvokeFunction\"],
      \"Condition\":{\"StringEquals\":
        {\"AWS:SourceAccount\": \"account ID\"},
        {\"AWS:SourceArn\":
          \"arn:aws:lex:region:account ID:intent:OrderFlowers:*\"}}}"
}
```

2. Get the intent from Amazon Lex. Amazon Lex sends the output to a file called
   `OrderFlowers-V3.json`.

```
aws lex-models get-intent \
    --region `region` \
    --name OrderFlowers \
    --intent-version "\$LATEST" > OrderFlowers-V3.json
```

3. In a text editor, open the `OrderFlowers-V3.json`.
   1. Find and delete the `createdDate`,
      `lastUpdatedDate`, and `version`
      fields.
   2. Update the `fulfillmentActivity` field :

   ```
       "fulfillmentActivity": {
           "type": "CodeHook",
           "codeHook": {
               "uri": "arn:aws:lambda:`region`:`account ID`:function:OrderFlowersCodeHook",
               "messageVersion": "1.0"
           }
       }
   ```

   3. Save the file.

4. In the AWS CLI, send the updated intent to Amazon Lex:

```
aws lex-models put-intent \
    --region `region` \
    --name OrderFlowers \
    --cli-input-json file://OrderFlowers-V3.json
```

Now that you have updated the intent, rebuild the bot.

###### To rebuild the `OrderFlowersBot` bot

1. In the AWS CLI, get the definition of the `OrderFlowersBot` bot and
   save it to a file:

```
aws lex-models get-bot \
    --region `region` \
    --name OrderFlowersBot \
    --version-or-alias "\$LATEST" > OrderFlowersBot-V3.json
```

2. In a text editor,open `OrderFlowersBot-V3.json`. Remove
   the `createdDate`, `lastUpdatedDate`, `status`,
   and `version` fields.
3. In the text editor, add the following line to the definition of the
   bot:

```
"processBehavior": "BUILD",
```

4. In the AWS CLI, build a new revision of the bot:

```
aws lex-models put-bot \
    --region `region` \
    --name OrderFlowersBot \
    --cli-input-json file://OrderFlowersBot-V3.json
```

The response from the server is:

## Next Step

[Exercise 4: Publish a Version (AWS CLI)](gs-cli-publish.md "gs-cli-publish.md")
