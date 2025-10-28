End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# Exercise 4: Publish a Version (AWS CLI)

Now, create a version of the bot that you created in Exercise 1. A
_version_ is a snapshot of the bot. After you create a version,
you can’t change it. The only version of a bot that you can update is the
`$LATEST` version. For more information about versions, see [Versioning and Aliases](versioning-aliases.md "versioning-aliases.md").

Before you can publish a version of a bot, you must publish the intents that is uses.
Likewise, you must publish the slot types that those intents refer to. In general, to
publish a version of a bot, you do the following:

1. Publish a version of a slot type with the [CreateSlotTypeVersion](API_CreateSlotTypeVersion.md "API_CreateSlotTypeVersion.md") operation.
2. Publish a version of an intent with the [CreateIntentVersion](API_CreateIntentVersion.md "API_CreateIntentVersion.md")
   operation.
3. Publish a version of a bot with the [CreateBotVersion](API_CreateBotVersion.md "API_CreateBotVersion.md") operation .
   To run the commands in this exercise, you need to know the region where the commands
   will be run. For a list of regions, see [Model Building
   Quotas](gl-limits.md#gl-limits-model-building "gl-limits.md#gl-limits-model-building") .

###### Topics

- [Step 1: Publish the Slot Type
  (AWS CLI)](gs-cli-publish-slot-type.md "gs-cli-publish-slot-type.md")
- [Step 2: Publish the Intent (AWS CLI)](gs-cli-publish-intent.md "gs-cli-publish-intent.md")
- [Step 3: Publish the Bot (AWS CLI)](gs-cli-publish-bot.md "gs-cli-publish-bot.md")
