# Amazon Q Business conversation log query examples

You can use [CloudWatch Logs insights](../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md "../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md") to interact
with conversation and feedback logs from Amazon Q Business. The following are examples of common
queries.

- Query for all the feedback type logs.

```
filter log_type = "Feedback"
```

- Query for all the chat type logs.

```
filter log_type = "VendedAnalyticsChat"
```

- Query for chat logs related to particular conversation.

```
filter conversation_id = <conversation_id>
```

- Query for chat logs where customer message with certain pattern.

```
filter customer_message like /pattern/
```

- Query for chat logs where system response message with certain pattern.

```
filter system_message like /pattern/
```

- Query for chat logs where system not able to provide answer.

```
filter system_message like /Sorry, I could not find relevant information to complete your request./
```

- Query for chat logs where system not able to provide answer.

```
filter output_metrics_is_message_with_no_answer = 1
```

- Query for chat logs where customer message was blocked.

```
filter output_metrics_is_message_blocked = 1
```

- Query for all the feedback logs where system answer was marked useful.

```
filter usefulness = "USEFUL"
```

- Query for all the feedback logs where system answer was marked not useful.

```
filter usefulness = "NOT_USEFUL"
```

- Query for all the feedback logs where system answer was marked not useful with reason
  “Other”.

```
filter usefulness = "NOT_USEFUL" and usefulness_reason = "OTHER"
```

- Query all feedback logs where system message was hallucinated

```
filter hallucinated_message != "NOT TRIGGERED" and hallucinated_message != NO HALLUCINATION DETECTED
```
