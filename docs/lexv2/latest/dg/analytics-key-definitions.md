# Key definitions

This topic provides key definitions that will help you interpret your bot analytics.
These definitions are related to the performance of your bot in four contexts:
**Intents**, **Slots**,
**Conversations**, and **Utterances**. The
following fields are relevant to many of the performance metrics:

- The [`state` field of the `Intent`](../APIReference/API_runtime_Intent.md#lexv2-Type-runtime_Intent-state "../APIReference/API_runtime_Intent.md#lexv2-Type-runtime_Intent-state") object.
- The [`type` field of the `dialogAction` object](../APIReference/API_runtime_DialogAction.md#lexv2-Type-runtime_DialogAction-type "../APIReference/API_runtime_DialogAction.md#lexv2-Type-runtime_DialogAction-type") within the [SessionState](../APIReference/API_runtime_SessionState.md "../APIReference/API_runtime_SessionState.md") object.

## Intents

Amazon Lex V2 categorizes intents in the following ways:

- **Success** – The bot successfully fulfilled the intent. One of the following situations is true:
  - The intent `state` is `ReadyForFulfillment` and the
    `type` of `dialogAction` is
    `Close`.
  - The intent `state` is `Fulfilled` and the
    `type` of `dialogAction` is
    `Close`.

- **Failed** – The bot failed to fulfill the intent. The intent state. One of the following situations is true:
  - The intent `state` is `Failed` and the `type` of `dialogAction` is `Close` (for example, the user declined the confirmation prompt).
  - The bot switches to the `AMAZON.FallbackIntent` before the intent is completed.

- **Switched** – The bot recognizes a different intent and switches to that intent instead, before the original intent is categorized as a _success_ or _failed_.
- **Dropped** – The customer doesn't
  respond before the intent is categorized as a _success_ or _failed_.

## Slots

Amazon Lex V2 categorizes slots in the following ways:

- **Success** – The bot filled the slot
  and successfully transitioned to another slot or the confirmation step.
- **Failed** – The bot wasn't able to fill the slot, even after reaching the maximum number of retries.
- **Dropped** – The customer doesn't
  respond or switches to another intent before the slot is categorized as a _success_ or _failed_.

## Conversations

When a customer makes a runtime call to Amazon Lex V2, they provide a [`sessionId`](../APIReference/API_runtime_PutSession.md#lexv2-runtime_PutSession-request-sessionId "../APIReference/API_runtime_PutSession.md#lexv2-runtime_PutSession-request-sessionId") and Amazon Lex V2 generates an [`originatingRequestId`](../APIReference/API_runtime_SessionState.md#lexv2-Type-runtime_SessionState-originatingRequestId "../APIReference/API_runtime_SessionState.md#lexv2-Type-runtime_SessionState-originatingRequestId"). If the customer doesn't respond
within the Session timeout ([`idleSessionTTLInSeconds`](../APIReference/API_CreateBot.md#lexv2-CreateBot-request-idleSessionTTLInSeconds "../APIReference/API_CreateBot.md#lexv2-CreateBot-request-idleSessionTTLInSeconds")) that you set for the bot, the
session expires. If a customer returns to the session by using the same
`sessionId`, Amazon Lex V2 generates a new
`originatingRequestId`.

For analytics, a _conversation_ is a unique combination of a `sessionId` and an `originatingRequestId`. Amazon Lex V2 categorizes conversations in the following ways:

- **Success** – The final intent in the
  conversation is categorized as a _success_.
- **Failed** – The final intent in the
  conversation is _failed_.
  The conversation is also _failed_ if Amazon Lex V2 defaults to the [AMAZON.FallbackIntent](built-in-intent-fallback.md "built-in-intent-fallback.md").
- **Dropped** – The customer doesn't
  respond before the conversation is categorized as a _success_ or _failed_.

## Utterances

Amazon Lex V2 categorizes utterances in the following ways:

- **Detected** – Amazon Lex V2 recognizes the utterance as an attempt to invoke an intent configured for a bot.
- **Missed** – Amazon Lex V2 doesn't recognize the utterance.
