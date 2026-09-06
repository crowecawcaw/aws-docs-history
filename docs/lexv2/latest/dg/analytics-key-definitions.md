

# Key definitions
<a name="analytics-key-definitions"></a>

This topic provides key definitions that will help you interpret your bot analytics. These definitions are related to the performance of your bot in four contexts: **Intents**, **Slots**, **Conversations**, and **Utterances**. The following fields are relevant to many of the performance metrics:
+ The [`state` field of the `Intent`](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_Intent.html#lexv2-Type-runtime_Intent-state) object.
+ The [`type` field of the `dialogAction` object](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_DialogAction.html#lexv2-Type-runtime_DialogAction-type) within the [SessionState](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_SessionState.html) object.

## Intents
<a name="analytics-key-definitions-intents"></a>

Amazon Lex V2 categorizes intents in the following ways:
+ **Success** – The bot successfully fulfilled the intent. One of the following situations is true:
  + The intent `state` is `ReadyForFulfillment` and the `type` of `dialogAction` is `Close`.
  + The intent `state` is `Fulfilled` and the `type` of `dialogAction` is `Close`.
+ **Failed** – The bot failed to fulfill the intent. The intent state. One of the following situations is true:
  + The intent `state` is `Failed` and the `type` of `dialogAction` is `Close` (for example, the user declined the confirmation prompt).
  + The bot switches to the `AMAZON.FallbackIntent` before the intent is completed.
+ **Switched** – The bot recognizes a different intent and switches to that intent instead, before the original intent is categorized as a *success* or *failed*.
+ **Dropped** – The customer doesn't respond before the intent is categorized as a *success* or *failed*.

## Slots
<a name="analytics-key-definitions-slots"></a>

Amazon Lex V2 categorizes slots in the following ways:
+ **Success** – The bot filled the slot and successfully transitioned to another slot or the confirmation step.
+ **Failed** – The bot wasn't able to fill the slot, even after reaching the maximum number of retries.
+ **Dropped** – The customer doesn't respond or switches to another intent before the slot is categorized as a *success* or *failed*.

## Conversations
<a name="analytics-key-definitions-conversations"></a>

When a customer makes a runtime call to Amazon Lex V2, they provide a [`sessionId`](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_PutSession.html#lexv2-runtime_PutSession-request-sessionId) and Amazon Lex V2 generates an [`originatingRequestId`](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_SessionState.html#lexv2-Type-runtime_SessionState-originatingRequestId). If the customer doesn't respond within the Session timeout ([`idleSessionTTLInSeconds`](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateBot.html#lexv2-CreateBot-request-idleSessionTTLInSeconds)) that you set for the bot, the session expires. If a customer returns to the session by using the same `sessionId`, Amazon Lex V2 generates a new `originatingRequestId`.

For analytics, a *conversation* is a unique combination of a `sessionId` and an `originatingRequestId`. Amazon Lex V2 categorizes conversations in the following ways:
+ **Success** – The final intent in the conversation is categorized as a *success*.
+ **Failed** – The final intent in the conversation is *failed*. The conversation is also *failed* if Amazon Lex V2 defaults to the [AMAZON.FallbackIntent](built-in-intent-fallback.md).
+ **Dropped** – The customer doesn't respond before the conversation is categorized as a *success* or *failed*.

## Utterances
<a name="analytics-key-definitions-utterances"></a>

Amazon Lex V2 categorizes utterances in the following ways:
+ **Detected** – Amazon Lex V2 recognizes the utterance as an attempt to invoke an intent configured for a bot.
+ **Missed** – Amazon Lex V2 doesn't recognize the utterance.