# Amazon Q Business chat message and feedback log examples

The following are examples of Amazon Q Business chat message and feedback logs in CloudWatch Logs.

**Chat message**

```
{
    "application_id": "`<ApplicationId>`",
    "event_timestamp": "`2024-09-05T19:43:58Z`",
    "log_type": "Message",
    "account_id": "`<AccountId>`",
    "conversation_id": "`<conversationId>`",
    "system_message_id": "`<systemMessageId>`",
    "user_message_id": "`<userMessageId>`",
    "user_message": `string`,
    "system_message": `string`,
    "output_metrics_is_message_blocked": `boolean`,
    "output_metrics_is_message_with_no_answer": `boolean`,
    "user_email": "`<userEmail>`"
}
```

**Amazon Q Business generated chat message (hallucination
detected)**

```
{
    "hallucinated_message": "`string`",
    "application_id": "`<ApplicationId>`",
    "event_timestamp": "`2024-09-05T19:43:58Z`",
    "log_type": "Message",
    "account_id": "`<AccountId>`",
    "conversation_id": "`<conversationId>`",
    "system_message_id": "`<systemMessageId>`",
    "user_message_id": "`<userMessageId>`",
    "user_message": `string`,
    "system_message": `string`,
    "output_metrics_is_message_blocked": `boolean`,
    "output_metrics_is_message_with_no_answer": `boolean`,
    "user_email": "`<userEmail>`"
}
```

**Amazon Q Business generated chat message (no hallucination
detected)**

```
{
    "hallucinated_message": "NO HALLUCINATION DETECTED",
    "application_id": "`<ApplicationId>`",
    "event_timestamp": "`2024-09-05T19:43:58Z`",
    "log_type": "Message",
    "account_id": "`<AccountId>`",
    "conversation_id": "`<conversationId>`",
    "system_message_id": "`<systemMessageId>`",
    "user_message_id": "`<userMessageId>`",
    "user_message": `string`,
    "system_message": `string`,
    "output_metrics_is_message_blocked": `boolean`,
    "output_metrics_is_message_with_no_answer": `boolean`,
    "user_email": "`<userEmail>`"
}
```

For system generated messages that have hallucination, you'll see one of the following log
descriptions:

- Hallucination mitigation disabled – `hallucinated_message:
DISABLED`
- Hallucination mitigation enabled but not triggered –
  `hallucinated_message: NOT TRIGGERED`
- Hallucination mitigation enabled and triggered, but no hallucinations detected
  – `hallucinated_message: NO HALLUCINATION DETECTED`
- Hallucination mitigation feature enabled and triggered, and hallucinations detected
  – `hallucinated_message: `string``
  **Feedback**

```
{
    "application_id": "`<ApplicationId>`",
    "event_timestamp": "`2024-09-05T13:13:27Z`",
    "log_type": "Feedback",
    "account_id": "`<AccountId>`",
    "conversation_id": "`<conversationId>`",
    "system_message_id": "`<systemMessageId>`",
    "user_message_id": "`<userMessageId>`",
    "user_message": `string`,
    "system_message": `string`,
    "usefulness_reason": "NOT_FACTUALLY_CORRECT" | "HARMFUL_OR_UNSAFE" | "INCORRECT_OR_MISSING_SOURCES" | "NOT_HELPFUL" | "FACTUALLY_CORRECT" | "COMPLETE" | "RELEVANT_SOURCES" | "HELPFUL" | "NOT_BASED_ON_DOCUMENTS" | "NOT_COMPLETE" | "NOT_CONCISE" | "OTHER",
    "usefulness": "NOT_USEFUL" | "USEFUL",
    "comment": `string`,
    "user_email": "`<userEmail>`"
}
```
