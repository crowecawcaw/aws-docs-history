# Integrating an Amazon Lex V2

bot with a messaging platform

This section explains how to integrate Amazon Lex V2 bots with the
Facebook, Slack, and Twilio messaging platforms. If you don't
already have an Amazon Lex V2 bot, create one. In this
topic, we assume that you are using the bot that you created in
[Exercise 1: Create a chatbot from a
template](exercise-1.md "exercise-1.md").
However, you can use any bot.

###### Note

When storing your Facebook, Slack, or Twilio configurations,
Amazon Lex V2 uses an AWS KMS key to encrypt information. The first
time that you create a channel to one of these messaging
platforms, Amazon Lex V2 creates a default customer managed key
(`aws/lex`) in your AWS account or you can
select your own customer managed key. Amazon Lex V2 supports only symmetric keys.
For more information, see the [AWS Key Management Service Developer Guide](../../../kms/latest/developerguide.md "../../../kms/latest/developerguide.md").

When a messaging platform sends a request to Amazon Lex V2 it includes
platform-specific information as a request attribute to you Lambda
function. Use this attribute to customize the way that your bot
behaves. For more information, see [Setting request
attributes for your Lex V2 bot](context-mgmt-request-attribs.md "context-mgmt-request-attribs.md").

| Common request attributes for messaging platforms | Attribute                                                               | Description |
| ------------------------------------------------- | ----------------------------------------------------------------------- | ----------- |
| x-amz-lex:channels:platform                       | One of the following values:<br>• `Facebook`<br>• `Slack`<br>• `Twilio` |
