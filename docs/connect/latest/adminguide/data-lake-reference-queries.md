

# Reference queries for the Connect Customer data lake
<a name="data-lake-reference-queries"></a>

This topic provides Athena SQL queries (Trino engine v3) for calculating common Connect Customer metrics from data lake tables. All queries use double-quoted identifiers and assume a `connect_datalake` database name. Adjust the database name to match your Glue catalog configuration.

Replace `<YOUR_INSTANCE_ID>` in each query with your Connect Customer instance ID.

**Topics**
+ [Contact and queue metrics](#data-lake-rq-contact-queue)
+ [Agent performance metrics](#data-lake-rq-agent-performance)
+ [Chat metrics](#data-lake-rq-chat)
+ [Conversational analytics metrics](#data-lake-rq-contact-lens)
+ [AI agent metrics](#data-lake-rq-ai-agent)
+ [Flow metrics](#data-lake-rq-flow)
+ [Evaluation metrics](#data-lake-rq-evaluations)
+ [Outbound campaign metrics](#data-lake-rq-campaigns)
+ [Cases metrics](#data-lake-rq-cases)
+ [Bot metrics](#data-lake-rq-bot)
+ [Common query patterns](#data-lake-rq-patterns)
+ [Agent schedule adherence (activity-level)](#data-lake-rq-schedule-adherence)
+ [Best practices](#data-lake-rq-best-practices)

## Contact and queue metrics
<a name="data-lake-rq-contact-queue"></a>

### Abandonment rate
<a name="data-lake-rq-abandonment-rate"></a>

**Definition:** Percentage of contacts disconnected by the customer while in queue. Callbacks excluded.

**Source table:** `contact_statistic_record`

```
SELECT
    "queue_id",
    CAST(SUM("is_abandoned") AS DOUBLE) 
        / NULLIF(SUM("is_queued"), 0) * 100.0 AS "abandonment_rate_pct"
FROM "connect_datalake"."contact_statistic_record"
WHERE "disconnect_timestamp" >= TIMESTAMP '2026-06-09 00:00:00'
  AND "disconnect_timestamp" <  TIMESTAMP '2026-06-10 00:00:00'
  AND "instance_id" = '<YOUR_INSTANCE_ID>'
GROUP BY "queue_id"
ORDER BY "abandonment_rate_pct" DESC;
```

### Contacts abandoned
<a name="data-lake-rq-contacts-abandoned"></a>

**Definition:** Count of contacts disconnected by the customer while waiting in queue.

**Source table:** `contact_statistic_record`

```
SELECT
    "queue_id",
    SUM("is_abandoned") AS "contacts_abandoned"
FROM "connect_datalake"."contact_statistic_record"
WHERE "disconnect_timestamp" >= TIMESTAMP '2026-06-09 00:00:00'
  AND "disconnect_timestamp" <  TIMESTAMP '2026-06-10 00:00:00'
  AND "instance_id" = '<YOUR_INSTANCE_ID>'
GROUP BY "queue_id";
```

### Contacts abandoned in X seconds
<a name="data-lake-rq-contacts-abandoned-x-seconds"></a>

**Definition:** Count of contacts abandoned within X seconds of being enqueued.

**Source table:** `contact_statistic_record`

```
SELECT
    "queue_id",
    SUM(
        CASE WHEN "is_abandoned" = 1 
             AND "queue_time_ms" <= 30000 
             THEN 1 ELSE 0 END
    ) AS "contacts_abandoned_in_30s"
FROM "connect_datalake"."contact_statistic_record"
WHERE "disconnect_timestamp" >= TIMESTAMP '2026-06-09 00:00:00'
  AND "disconnect_timestamp" <  TIMESTAMP '2026-06-10 00:00:00'
  AND "instance_id" = '<YOUR_INSTANCE_ID>'
GROUP BY "queue_id";
```

### Average queue abandon time
<a name="data-lake-rq-avg-queue-abandon-time"></a>

**Definition:** Average time contacts waited in queue before abandoning.

**Source table:** `contact_statistic_record`

```
SELECT
    "queue_id",
    AVG("abandon_time_ms") / 1000.0 AS "avg_queue_abandon_time_sec"
FROM "connect_datalake"."contact_statistic_record"
WHERE "disconnect_timestamp" >= TIMESTAMP '2026-06-09 00:00:00'
  AND "disconnect_timestamp" <  TIMESTAMP '2026-06-10 00:00:00'
  AND "is_abandoned" = 1
  AND "abandon_time_ms" IS NOT NULL
  AND "instance_id" = '<YOUR_INSTANCE_ID>'
GROUP BY "queue_id";
```

### Average queue answer time
<a name="data-lake-rq-avg-queue-answer-time"></a>

**Definition:** Average time contacts waited in queue before being answered by an agent.

**Source table:** `contact_statistic_record`

```
SELECT
    "queue_id",
    AVG("queue_answer_time_ms") / 1000.0 AS "avg_queue_answer_time_sec"
FROM "connect_datalake"."contact_statistic_record"
WHERE "disconnect_timestamp" >= TIMESTAMP '2026-06-09 00:00:00'
  AND "disconnect_timestamp" <  TIMESTAMP '2026-06-10 00:00:00'
  AND "is_handled" = 1
  AND "queue_answer_time_ms" IS NOT NULL
  AND "instance_id" = '<YOUR_INSTANCE_ID>'
GROUP BY "queue_id";
```

### Service level
<a name="data-lake-rq-service-level"></a>

**Definition:** Count and percentage of contacts answered within X seconds.

**Source table:** `contact_statistic_record`

```
SELECT
    "queue_id",
    SUM(CASE WHEN "is_handled" = 1 AND "queue_answer_time_ms" <= 20000 
             THEN 1 ELSE 0 END) AS "contacts_answered_in_20s",
    SUM("is_queued") AS "contacts_queued",
    CAST(SUM(CASE WHEN "is_handled" = 1 AND "queue_answer_time_ms" <= 20000 
                  THEN 1 ELSE 0 END) AS DOUBLE)
        / NULLIF(SUM("is_queued"), 0) * 100.0 AS "service_level_20s_pct"
FROM "connect_datalake"."contact_statistic_record"
WHERE "disconnect_timestamp" >= TIMESTAMP '2026-06-09 00:00:00'
  AND "disconnect_timestamp" <  TIMESTAMP '2026-06-10 00:00:00'
  AND "instance_id" = '<YOUR_INSTANCE_ID>'
GROUP BY "queue_id";
```

### Contacts queued
<a name="data-lake-rq-contacts-queued"></a>

**Definition:** Count of contacts placed into a queue.

**Source table:** `contact_statistic_record`

```
SELECT
    "queue_id",
    SUM("is_queued") AS "contacts_queued"
FROM "connect_datalake"."contact_statistic_record"
WHERE "disconnect_timestamp" >= TIMESTAMP '2026-06-09 00:00:00'
  AND "disconnect_timestamp" <  TIMESTAMP '2026-06-10 00:00:00'
  AND "instance_id" = '<YOUR_INSTANCE_ID>'
GROUP BY "queue_id";
```

### Contacts handled
<a name="data-lake-rq-contacts-handled"></a>

**Definition:** Count of contacts connected to an agent.

**Source table:** `contact_statistic_record`

```
SELECT
    "queue_id",
    SUM("is_handled") AS "contacts_handled"
FROM "connect_datalake"."contact_statistic_record"
WHERE "disconnect_timestamp" >= TIMESTAMP '2026-06-09 00:00:00'
  AND "disconnect_timestamp" <  TIMESTAMP '2026-06-10 00:00:00'
  AND "instance_id" = '<YOUR_INSTANCE_ID>'
GROUP BY "queue_id";
```

### Contacts transferred in
<a name="data-lake-rq-contacts-transferred-in"></a>

**Definition:** Contacts transferred into a queue.

**Source table:** `contact_statistic_record`

```
SELECT
    "queue_id",
    SUM("is_transferred_in") AS "contacts_transferred_in"
FROM "connect_datalake"."contact_statistic_record"
WHERE "disconnect_timestamp" >= TIMESTAMP '2026-06-09 00:00:00'
  AND "disconnect_timestamp" <  TIMESTAMP '2026-06-10 00:00:00'
  AND "instance_id" = '<YOUR_INSTANCE_ID>'
GROUP BY "queue_id";
```

### Contacts transferred out
<a name="data-lake-rq-contacts-transferred-out"></a>

**Definition:** Contacts transferred out of a queue.

**Source table:** `contact_statistic_record`

```
SELECT
    "queue_id",
    SUM("is_transferred_out") AS "contacts_transferred_out",
    SUM("is_transferred_out_internal") AS "transferred_out_internal",
    SUM("is_transferred_out_external") AS "transferred_out_external"
FROM "connect_datalake"."contact_statistic_record"
WHERE "disconnect_timestamp" >= TIMESTAMP '2026-06-09 00:00:00'
  AND "disconnect_timestamp" <  TIMESTAMP '2026-06-10 00:00:00'
  AND "instance_id" = '<YOUR_INSTANCE_ID>'
GROUP BY "queue_id";
```

### Maximum queued time
<a name="data-lake-rq-max-queued-time"></a>

**Definition:** Longest time any contact spent waiting in queue.

**Source table:** `contact_record`

```
SELECT
    "queue_id",
    MAX("queue_duration_ms") / 1000.0 AS "max_queued_time_sec"
FROM "connect_datalake"."contact_record"
WHERE "disconnect_timestamp" >= TIMESTAMP '2026-06-09 00:00:00'
  AND "disconnect_timestamp" <  TIMESTAMP '2026-06-10 00:00:00'
  AND "queue_duration_ms" IS NOT NULL
  AND "instance_id" = '<YOUR_INSTANCE_ID>'
GROUP BY "queue_id";
```

### Average contact duration
<a name="data-lake-rq-avg-contact-duration"></a>

**Definition:** Average time from contact initiation to disconnect.

**Source table:** `contact_record`

```
SELECT
    "queue_id",
    AVG(
        date_diff('millisecond', "initiation_timestamp", "disconnect_timestamp")
    ) / 1000.0 AS "avg_contact_duration_sec"
FROM "connect_datalake"."contact_record"
WHERE "disconnect_timestamp" >= TIMESTAMP '2026-06-09 00:00:00'
  AND "disconnect_timestamp" <  TIMESTAMP '2026-06-10 00:00:00'
  AND "initiation_timestamp" IS NOT NULL
  AND "instance_id" = '<YOUR_INSTANCE_ID>'
GROUP BY "queue_id";
```

## Agent performance metrics
<a name="data-lake-rq-agent-performance"></a>

### Average handle time
<a name="data-lake-rq-avg-handle-time"></a>

**Definition:** Average time from contact connection to ACW completion.

**Source table:** `contact_statistic_record`

```
SELECT
    "agent_id",
    AVG("handle_time_ms") / 1000.0 AS "avg_handle_time_sec"
FROM "connect_datalake"."contact_statistic_record"
WHERE "disconnect_timestamp" >= TIMESTAMP '2026-06-09 00:00:00'
  AND "disconnect_timestamp" <  TIMESTAMP '2026-06-10 00:00:00'
  AND "is_handled" = 1
  AND "handle_time_ms" IS NOT NULL
  AND "instance_id" = '<YOUR_INSTANCE_ID>'
GROUP BY "agent_id";
```

### After contact work time
<a name="data-lake-rq-acw-time"></a>

**Definition:** Total time agents spent in ACW state.

**Source table:** `contact_statistic_record`

```
SELECT
    "agent_id",
    SUM("after_contact_work_time_ms") / 1000.0 AS "total_acw_time_sec"
FROM "connect_datalake"."contact_statistic_record"
WHERE "disconnect_timestamp" >= TIMESTAMP '2026-06-09 00:00:00'
  AND "disconnect_timestamp" <  TIMESTAMP '2026-06-10 00:00:00'
  AND "after_contact_work_time_ms" IS NOT NULL
  AND "instance_id" = '<YOUR_INSTANCE_ID>'
GROUP BY "agent_id";
```

### Customer hold time
<a name="data-lake-rq-customer-hold-time"></a>

**Definition:** Total time customers spent on hold after connecting to agent.

**Source table:** `contact_statistic_record`

```
SELECT
    "agent_id",
    SUM("customer_hold_time_ms") / 1000.0 AS "total_hold_time_sec"
FROM "connect_datalake"."contact_statistic_record"
WHERE "disconnect_timestamp" >= TIMESTAMP '2026-06-09 00:00:00'
  AND "disconnect_timestamp" <  TIMESTAMP '2026-06-10 00:00:00'
  AND "customer_hold_time_ms" IS NOT NULL
  AND "instance_id" = '<YOUR_INSTANCE_ID>'
GROUP BY "agent_id";
```

### Agent idle time
<a name="data-lake-rq-agent-idle-time"></a>

**Definition:** Time agent spent in Available status without handling contacts.

**Source table:** `agent_statistic_record`

```
SELECT
    "user_id" AS "agent_id",
    SUM("agent_idle_time") / 1000.0 AS "total_idle_time_sec"
FROM "connect_datalake"."agent_statistic_record"
WHERE "published_date" >= TIMESTAMP '2026-06-09 00:00:00'
  AND "published_date" <  TIMESTAMP '2026-06-10 00:00:00'
  AND "instance_id" = '<YOUR_INSTANCE_ID>'
GROUP BY "user_id";
```

### Occupancy
<a name="data-lake-rq-occupancy"></a>

**Definition:** Percentage of time agents were active on contacts versus available plus active.

**Source table:** `agent_statistic_record`

```
SELECT
    "user_id" AS "agent_id",
    CAST(SUM("agent_on_contact_time") AS DOUBLE)
        / NULLIF(SUM("agent_on_contact_time") + SUM("agent_idle_time"), 0) 
        * 100.0 AS "occupancy_pct"
FROM "connect_datalake"."agent_statistic_record"
WHERE "published_date" >= TIMESTAMP '2026-06-09 00:00:00'
  AND "published_date" <  TIMESTAMP '2026-06-10 00:00:00'
  AND "instance_id" = '<YOUR_INSTANCE_ID>'
GROUP BY "user_id";
```

### Agent non-response
<a name="data-lake-rq-agent-non-response"></a>

**Definition:** Count of contacts routed to agent but not answered.

**Source table:** `agent_queue_statistic_record`

```
SELECT
    "user_id" AS "agent_id",
    "queue_id",
    SUM("agent_non_response") AS "agent_non_response_count"
FROM "connect_datalake"."agent_queue_statistic_record"
WHERE "published_date" >= TIMESTAMP '2026-06-09 00:00:00'
  AND "published_date" <  TIMESTAMP '2026-06-10 00:00:00'
  AND "instance_id" = '<YOUR_INSTANCE_ID>'
GROUP BY "user_id", "queue_id";
```

### Agent answer rate
<a name="data-lake-rq-agent-answer-rate"></a>

**Definition:** Percentage of routed contacts answered by the agent.

**Source table:** `agent_queue_statistic_record`

```
SELECT
    "user_id" AS "agent_id",
    CAST(SUM("contacts_handled") AS DOUBLE) 
        / NULLIF(SUM("contacts_offered"), 0) * 100.0 AS "agent_answer_rate_pct"
FROM "connect_datalake"."agent_queue_statistic_record"
WHERE "published_date" >= TIMESTAMP '2026-06-09 00:00:00'
  AND "published_date" <  TIMESTAMP '2026-06-10 00:00:00'
  AND "instance_id" = '<YOUR_INSTANCE_ID>'
GROUP BY "user_id";
```

### Online time
<a name="data-lake-rq-online-time"></a>

**Definition:** Total time agent CCP was set to status other than Offline.

**Source table:** `agent_statistic_record`

```
SELECT
    "user_id" AS "agent_id",
    SUM("online_time") / 1000.0 AS "total_online_time_sec"
FROM "connect_datalake"."agent_statistic_record"
WHERE "published_date" >= TIMESTAMP '2026-06-09 00:00:00'
  AND "published_date" <  TIMESTAMP '2026-06-10 00:00:00'
  AND "instance_id" = '<YOUR_INSTANCE_ID>'
GROUP BY "user_id";
```

## Chat metrics
<a name="data-lake-rq-chat"></a>

### Average agent first response time
<a name="data-lake-rq-avg-agent-first-response-time"></a>

**Definition:** Average time for agent to send first message after obtaining a chat contact.

**Source table:** `contact_record`

```
SELECT
    "queue_id",
    AVG("chat_contact_metrics_agent_first_response_time_ms") / 1000.0 
        AS "avg_agent_first_response_sec"
FROM "connect_datalake"."contact_record"
WHERE "disconnect_timestamp" >= TIMESTAMP '2026-06-09 00:00:00'
  AND "disconnect_timestamp" <  TIMESTAMP '2026-06-10 00:00:00'
  AND "channel" = 'CHAT'
  AND "chat_contact_metrics_agent_first_response_time_ms" IS NOT NULL
  AND "instance_id" = '<YOUR_INSTANCE_ID>'
GROUP BY "queue_id";
```

### Average agent response time
<a name="data-lake-rq-avg-agent-response-time"></a>

**Definition:** Average time agents take to respond to customer messages.

**Source table:** `contact_record`

```
SELECT
    "queue_id",
    CAST(SUM("chat_agent_metrics_total_response_time_ms") AS DOUBLE)
        / NULLIF(SUM("chat_agent_metrics_num_responses"), 0) / 1000.0
        AS "avg_agent_response_time_sec"
FROM "connect_datalake"."contact_record"
WHERE "disconnect_timestamp" >= TIMESTAMP '2026-06-09 00:00:00'
  AND "disconnect_timestamp" <  TIMESTAMP '2026-06-10 00:00:00'
  AND "channel" = 'CHAT'
  AND "chat_agent_metrics_total_response_time_ms" IS NOT NULL
  AND "instance_id" = '<YOUR_INSTANCE_ID>'
GROUP BY "queue_id";
```

### Average total messages
<a name="data-lake-rq-avg-total-messages"></a>

**Definition:** Average total messages per chat contact.

**Source table:** `contact_record`

```
SELECT
    "queue_id",
    AVG(CAST("chat_contact_metrics_total_messages" AS DOUBLE)) AS "avg_total_messages"
FROM "connect_datalake"."contact_record"
WHERE "disconnect_timestamp" >= TIMESTAMP '2026-06-09 00:00:00'
  AND "disconnect_timestamp" <  TIMESTAMP '2026-06-10 00:00:00'
  AND "channel" = 'CHAT'
  AND "chat_contact_metrics_total_messages" IS NOT NULL
  AND "instance_id" = '<YOUR_INSTANCE_ID>'
GROUP BY "queue_id";
```

### Conversations abandoned
<a name="data-lake-rq-conversations-abandoned"></a>

**Definition:** Contacts where chat was abandoned by agent or customer.

**Source table:** `contact_record`

```
SELECT
    "queue_id",
    COUNT(*) AS "conversations_abandoned"
FROM "connect_datalake"."contact_record"
WHERE "disconnect_timestamp" >= TIMESTAMP '2026-06-09 00:00:00'
  AND "disconnect_timestamp" <  TIMESTAMP '2026-06-10 00:00:00'
  AND "channel" = 'CHAT'
  AND ("chat_agent_metrics_conversation_abandon" = true 
       OR "chat_customer_metrics_conversation_abandon" = true)
  AND "instance_id" = '<YOUR_INSTANCE_ID>'
GROUP BY "queue_id";
```

## Conversational analytics metrics
<a name="data-lake-rq-contact-lens"></a>

### Average talk time
<a name="data-lake-rq-avg-talk-time"></a>

**Definition:** Average combined agent and customer talk time per voice contact.

**Source table:** `contact_lens_conversational_analytics`

```
SELECT
    AVG("talk_time_total_ms") / 1000.0 AS "avg_talk_time_sec"
FROM "connect_datalake"."contact_lens_conversational_analytics"
WHERE "disconnect_timestamp" >= TIMESTAMP '2026-06-09 00:00:00'
  AND "disconnect_timestamp" <  TIMESTAMP '2026-06-10 00:00:00'
  AND "channel" = 'VOICE'
  AND "instance_id" = '<YOUR_INSTANCE_ID>';
```

### Average non-talk time
<a name="data-lake-rq-avg-non-talk-time"></a>

**Definition:** Average hold plus silence time per voice contact.

**Source table:** `contact_lens_conversational_analytics`

```
SELECT
    AVG("non_talk_time_total_ms") / 1000.0 AS "avg_non_talk_time_sec"
FROM "connect_datalake"."contact_lens_conversational_analytics"
WHERE "disconnect_timestamp" >= TIMESTAMP '2026-06-09 00:00:00'
  AND "disconnect_timestamp" <  TIMESTAMP '2026-06-10 00:00:00'
  AND "channel" = 'VOICE'
  AND "instance_id" = '<YOUR_INSTANCE_ID>';
```

### Sentiment scores
<a name="data-lake-rq-sentiment-scores"></a>

**Definition:** Overall sentiment scores for agent and customer.

**Source table:** `contact_lens_conversational_analytics`

```
SELECT
    AVG("sentiment_overall_score_agent") AS "avg_agent_sentiment",
    AVG("sentiment_overall_score_customer") AS "avg_customer_sentiment",
    AVG("sentiment_end_score_agent") AS "avg_agent_end_sentiment",
    AVG("sentiment_end_score_customer") AS "avg_customer_end_sentiment"
FROM "connect_datalake"."contact_lens_conversational_analytics"
WHERE "disconnect_timestamp" >= TIMESTAMP '2026-06-09 00:00:00'
  AND "disconnect_timestamp" <  TIMESTAMP '2026-06-10 00:00:00'
  AND "instance_id" = '<YOUR_INSTANCE_ID>';
```

### Average agent interruptions
<a name="data-lake-rq-avg-agent-interruptions"></a>

**Definition:** Average count of agent interruptions per contact.

**Source table:** `contact_lens_conversational_analytics`

```
SELECT
    AVG(CAST("interruptions_agent_count" AS DOUBLE)) AS "avg_agent_interruptions"
FROM "connect_datalake"."contact_lens_conversational_analytics"
WHERE "disconnect_timestamp" >= TIMESTAMP '2026-06-09 00:00:00'
  AND "disconnect_timestamp" <  TIMESTAMP '2026-06-10 00:00:00'
  AND "channel" = 'VOICE'
  AND "instance_id" = '<YOUR_INSTANCE_ID>';
```

## AI agent metrics
<a name="data-lake-rq-ai-agent"></a>

### AI agent invocation success rate
<a name="data-lake-rq-ai-invocation-success-rate"></a>

**Definition:** Rate of successful AI Agent invocations.

**Source table:** `ai_agent`

```
SELECT
    "ai_agent_name",
    SUM(CASE WHEN "invocation_success" = true THEN 1 ELSE 0 END) AS "success_count",
    COUNT(*) AS "total_invocations",
    CAST(SUM(CASE WHEN "invocation_success" = true THEN 1 ELSE 0 END) AS DOUBLE)
        / NULLIF(COUNT(*), 0) * 100.0 AS "success_rate_pct"
FROM "connect_datalake"."ai_agent"
WHERE "creation_timestamp" >= CAST('2026-06-09' AS TIMESTAMP) * 1000
  AND "instance_id" = '<YOUR_INSTANCE_ID>'
  AND "ai_agent_id" IS NOT NULL
GROUP BY "ai_agent_name";
```

### AI handoff rate
<a name="data-lake-rq-ai-handoff-rate"></a>

**Definition:** Rate of AI sessions that escalated to human agents.

**Source table:** `ai_session`

```
SELECT
    SUM(CASE WHEN "is_handed_off" = true THEN 1 ELSE 0 END) AS "ai_handoffs",
    COUNT(*) AS "ai_involved_contacts",
    CAST(SUM(CASE WHEN "is_handed_off" = true THEN 1 ELSE 0 END) AS DOUBLE)
        / NULLIF(COUNT(*), 0) * 100.0 AS "handoff_rate_pct"
FROM "connect_datalake"."ai_session"
WHERE "creation_timestamp" >= CAST('2026-06-09' AS TIMESTAMP) * 1000
  AND "instance_id" = '<YOUR_INSTANCE_ID>'
  AND "ai_session_id" IS NOT NULL;
```

### AI quality scores
<a name="data-lake-rq-ai-quality-scores"></a>

**Definition:** Average goal success, faithfulness, and completeness scores.

**Source table:** `ai_session`

```
SELECT
    AVG("goal_success_rate") AS "avg_goal_success_rate",
    AVG("faithfulness_score") AS "avg_faithfulness_score",
    AVG("completeness_score") AS "avg_completeness_score"
FROM "connect_datalake"."ai_session"
WHERE "creation_timestamp" >= CAST('2026-06-09' AS TIMESTAMP) * 1000
  AND "instance_id" = '<YOUR_INSTANCE_ID>'
  AND "goal_success_rate" IS NOT NULL;
```

### AI tool accuracy
<a name="data-lake-rq-ai-tool-accuracy"></a>

**Definition:** Accuracy scores for AI tool parameter usage, selection, and utilization.

**Source table:** `ai_tool`

```
SELECT
    "ai_tool_name",
    AVG("ai_tool_parameter_accuracy") AS "avg_parameter_accuracy",
    AVG("ai_tool_selection_accuracy") AS "avg_selection_accuracy",
    AVG("ai_tool_utilization_accuracy") AS "avg_use_accuracy"
FROM "connect_datalake"."ai_tool"
WHERE "creation_timestamp" >= CAST('2026-06-09' AS TIMESTAMP) * 1000
  AND "instance_id" = '<YOUR_INSTANCE_ID>'
  AND "ai_tool_id" IS NOT NULL
GROUP BY "ai_tool_name";
```

## Flow metrics
<a name="data-lake-rq-flow"></a>

### Flows started
<a name="data-lake-rq-flows-started"></a>

**Definition:** Count of flows that began execution.

**Source table:** `contact_flow_events`

```
SELECT
    "flow_resource_id",
    "flow_type",
    COUNT(*) AS "flows_started"
FROM "connect_datalake"."contact_flow_events"
WHERE "start_timestamp" >= TIMESTAMP '2026-06-09 00:00:00'
  AND "start_timestamp" <  TIMESTAMP '2026-06-10 00:00:00'
  AND "instance_id" = '<YOUR_INSTANCE_ID>'
GROUP BY "flow_resource_id", "flow_type";
```

### Flow outcome percentage
<a name="data-lake-rq-flow-outcome-pct"></a>

**Definition:** Percentage of each flow outcome type.

**Source table:** `contact_flow_events`

```
WITH flow_counts AS (
    SELECT
        "flow_resource_id",
        "flow_outcome",
        COUNT(*) AS "outcome_count",
        SUM(COUNT(*)) OVER (PARTITION BY "flow_resource_id") AS "total_completed"
    FROM "connect_datalake"."contact_flow_events"
    WHERE "start_timestamp" >= TIMESTAMP '2026-06-09 00:00:00'
      AND "start_timestamp" <  TIMESTAMP '2026-06-10 00:00:00'
      AND "end_timestamp" IS NOT NULL
      AND "instance_id" = '<YOUR_INSTANCE_ID>'
    GROUP BY "flow_resource_id", "flow_outcome"
)
SELECT
    "flow_resource_id",
    "flow_outcome",
    "outcome_count",
    CAST("outcome_count" AS DOUBLE) / "total_completed" * 100.0 AS "outcome_pct"
FROM flow_counts
ORDER BY "flow_resource_id", "outcome_pct" DESC;
```

### Average flow time
<a name="data-lake-rq-avg-flow-time"></a>

**Definition:** Average duration of flow executions.

**Source table:** `contact_flow_events`

```
SELECT
    "flow_resource_id",
    AVG(
        date_diff('millisecond', "start_timestamp", "end_timestamp")
    ) / 1000.0 AS "avg_flow_time_sec"
FROM "connect_datalake"."contact_flow_events"
WHERE "start_timestamp" >= TIMESTAMP '2026-06-09 00:00:00'
  AND "start_timestamp" <  TIMESTAMP '2026-06-10 00:00:00'
  AND "end_timestamp" IS NOT NULL
  AND "instance_id" = '<YOUR_INSTANCE_ID>'
GROUP BY "flow_resource_id";
```

## Evaluation metrics
<a name="data-lake-rq-evaluations"></a>

### Evaluations performed
<a name="data-lake-rq-evaluations-performed"></a>

**Definition:** Number of submitted evaluations.

**Source table:** `contact_evaluation_record`

```
SELECT
    COUNT(DISTINCT "evaluation_id") AS "evaluations_performed"
FROM "connect_datalake"."contact_evaluation_record"
WHERE "evaluation_submitted_timestamp" >= TIMESTAMP '2026-06-09 00:00:00'
  AND "evaluation_submitted_timestamp" <  TIMESTAMP '2026-06-10 00:00:00'
  AND "item_type" = 'Form'
  AND "to_delete" = false
  AND ("evaluation_type" IS NULL OR "evaluation_type" != 'calibration')
  AND "instance_id" = '<YOUR_INSTANCE_ID>';
```

### Average evaluation score
<a name="data-lake-rq-avg-evaluation-score"></a>

**Definition:** Average evaluation score across submitted evaluations.

**Source table:** `contact_evaluation_record`

```
SELECT
    AVG("score") AS "avg_evaluation_score_pct"
FROM "connect_datalake"."contact_evaluation_record"
WHERE "evaluation_submitted_timestamp" >= TIMESTAMP '2026-06-09 00:00:00'
  AND "evaluation_submitted_timestamp" <  TIMESTAMP '2026-06-10 00:00:00'
  AND "item_type" = 'Form'
  AND "to_delete" = false
  AND ("evaluation_type" IS NULL OR "evaluation_type" != 'calibration')
  AND "instance_id" = '<YOUR_INSTANCE_ID>';
```

### Automatic fails percent
<a name="data-lake-rq-automatic-fails"></a>

**Definition:** Percentage of evaluations that triggered automatic fail.

**Source table:** `contact_evaluation_record`

```
SELECT
    CAST(
        COUNT(DISTINCT CASE WHEN "automatic_fail" = true THEN "evaluation_id" END) AS DOUBLE
    ) / NULLIF(COUNT(DISTINCT "evaluation_id"), 0) * 100.0 
        AS "automatic_fail_pct"
FROM "connect_datalake"."contact_evaluation_record"
WHERE "evaluation_submitted_timestamp" >= TIMESTAMP '2026-06-09 00:00:00'
  AND "evaluation_submitted_timestamp" <  TIMESTAMP '2026-06-10 00:00:00'
  AND "item_type" = 'Form'
  AND "to_delete" = false
  AND ("evaluation_type" IS NULL OR "evaluation_type" != 'calibration')
  AND "instance_id" = '<YOUR_INSTANCE_ID>';
```

## Outbound campaign metrics
<a name="data-lake-rq-campaigns"></a>

### Campaign contacts
<a name="data-lake-rq-campaign-contacts"></a>

**Definition:** Count of outbound campaign contacts.

**Source table:** `contact_record`

```
SELECT
    "campaign_id",
    COUNT(*) AS "campaign_contacts"
FROM "connect_datalake"."contact_record"
WHERE "disconnect_timestamp" >= TIMESTAMP '2026-06-09 00:00:00'
  AND "disconnect_timestamp" <  TIMESTAMP '2026-06-10 00:00:00'
  AND "campaign_id" IS NOT NULL
  AND "instance_id" = '<YOUR_INSTANCE_ID>'
GROUP BY "campaign_id";
```

### Human answered
<a name="data-lake-rq-human-answered"></a>

**Definition:** Outbound campaign calls connected to a live customer.

**Source table:** `contact_record`

```
SELECT
    "campaign_id",
    COUNT(*) AS "human_answered"
FROM "connect_datalake"."contact_record"
WHERE "disconnect_timestamp" >= TIMESTAMP '2026-06-09 00:00:00'
  AND "disconnect_timestamp" <  TIMESTAMP '2026-06-10 00:00:00'
  AND "campaign_id" IS NOT NULL
  AND "answering_machine_detection_status" = 'HUMAN_ANSWERED'
  AND "instance_id" = '<YOUR_INSTANCE_ID>'
GROUP BY "campaign_id";
```

## Cases metrics
<a name="data-lake-rq-cases"></a>

### Cases created
<a name="data-lake-rq-cases-created"></a>

**Definition:** Total cases created in a time period.

**Source table:** `case_events`

```
SELECT
    COUNT(DISTINCT "case_id") AS "cases_created"
FROM "connect_datalake"."case_events"
WHERE "event_timestamp" >= TIMESTAMP '2026-06-09 00:00:00'
  AND "event_timestamp" <  TIMESTAMP '2026-06-10 00:00:00'
  AND "event_type" = 'CASE.CREATED'
  AND "instance_id" = '<YOUR_INSTANCE_ID>';
```

### Average case resolution time
<a name="data-lake-rq-avg-case-resolution"></a>

**Definition:** Average time from case creation to close.

**Source table:** `case_events`

```
SELECT
    AVG(
        date_diff('hour', "created_timestamp", "last_closed_timestamp")
    ) AS "avg_resolution_time_hours"
FROM "connect_datalake"."case_events"
WHERE "last_closed_timestamp" >= TIMESTAMP '2026-06-09 00:00:00'
  AND "last_closed_timestamp" <  TIMESTAMP '2026-06-10 00:00:00'
  AND "created_timestamp" IS NOT NULL
  AND "instance_id" = '<YOUR_INSTANCE_ID>';
```

## Bot metrics
<a name="data-lake-rq-bot"></a>

### Bot conversation outcomes
<a name="data-lake-rq-bot-outcomes"></a>

**Definition:** Percentage breakdown of bot conversation outcomes.

**Source table:** `bot_conversations`

```
WITH bot_outcomes AS (
    SELECT
        "bot_id",
        "bot_conversation_outcome",
        COUNT(*) AS "cnt",
        SUM(COUNT(*)) OVER (PARTITION BY "bot_id") AS "total"
    FROM "connect_datalake"."bot_conversations"
    WHERE "bot_conversation_start_timestamp" >= TIMESTAMP '2026-06-09 00:00:00'
      AND "bot_conversation_start_timestamp" <  TIMESTAMP '2026-06-10 00:00:00'
      AND "instance_id" = '<YOUR_INSTANCE_ID>'
    GROUP BY "bot_id", "bot_conversation_outcome"
)
SELECT
    "bot_id",
    "bot_conversation_outcome",
    "cnt",
    CAST("cnt" AS DOUBLE) / "total" * 100.0 AS "outcome_pct"
FROM bot_outcomes;
```

## Common query patterns
<a name="data-lake-rq-patterns"></a>

The following patterns show how to combine multiple data lake tables for comprehensive dashboards and reporting.

### Daily summary dashboard
<a name="data-lake-rq-daily-summary"></a>

**Definition:** Comprehensive daily queue metrics including service level.

**Source table:** `contact_statistic_record`

```
SELECT
    "queue_id",
    SUM("is_queued") AS "contacts_queued",
    SUM("is_handled") AS "contacts_handled",
    SUM("is_abandoned") AS "contacts_abandoned",
    AVG(CASE WHEN "is_handled" = 1 THEN "queue_answer_time_ms" END) / 1000.0 
        AS "avg_answer_time_sec",
    AVG(CASE WHEN "is_handled" = 1 THEN "handle_time_ms" END) / 1000.0 
        AS "avg_handle_time_sec",
    CAST(SUM(CASE WHEN "is_handled" = 1 AND "queue_answer_time_ms" <= 20000 
                  THEN 1 ELSE 0 END) AS DOUBLE)
        / NULLIF(SUM("is_queued"), 0) * 100.0 AS "sl_20s_pct"
FROM "connect_datalake"."contact_statistic_record"
WHERE "disconnect_timestamp" >= TIMESTAMP '2026-06-09 00:00:00'
  AND "disconnect_timestamp" <  TIMESTAMP '2026-06-10 00:00:00'
  AND "instance_id" = '<YOUR_INSTANCE_ID>'
GROUP BY "queue_id"
ORDER BY "contacts_queued" DESC;
```

### Hourly trend analysis
<a name="data-lake-rq-hourly-trend"></a>

**Definition:** Hourly contact volume and service level trends.

**Source table:** `contact_statistic_record`

```
SELECT
    date_trunc('hour', "disconnect_timestamp") AS "hour",
    "queue_id",
    SUM("is_queued") AS "contacts_queued",
    SUM("is_handled") AS "contacts_handled",
    SUM("is_abandoned") AS "contacts_abandoned",
    CAST(SUM("is_abandoned") AS DOUBLE) 
        / NULLIF(SUM("is_queued"), 0) * 100.0 AS "abandon_rate_pct",
    AVG(CASE WHEN "is_handled" = 1 THEN "handle_time_ms" END) / 1000.0 AS "aht_sec"
FROM "connect_datalake"."contact_statistic_record"
WHERE "disconnect_timestamp" >= TIMESTAMP '2026-06-09 00:00:00'
  AND "disconnect_timestamp" <  TIMESTAMP '2026-06-10 00:00:00'
  AND "instance_id" = '<YOUR_INSTANCE_ID>'
GROUP BY date_trunc('hour', "disconnect_timestamp"), "queue_id"
ORDER BY "hour";
```

### Conversational analytics enriched contacts
<a name="data-lake-rq-contact-lens-enriched"></a>

**Definition:** Enrich contact records with conversational analytics.

**Source table:** `contact_record` joined with `contact_lens_conversational_analytics`

```
SELECT
    cr."contact_id",
    cr."queue_id",
    cr."agent_id",
    cr."agent_interaction_duration_ms" / 1000.0 AS "interaction_sec",
    cl."talk_time_agent_ms" / 1000.0 AS "agent_talk_sec",
    cl."talk_time_customer_ms" / 1000.0 AS "customer_talk_sec",
    cl."sentiment_overall_score_agent",
    cl."sentiment_overall_score_customer"
FROM "connect_datalake"."contact_record" cr
JOIN "connect_datalake"."contact_lens_conversational_analytics" cl
    ON cr."contact_id" = cl."contact_id"
    AND cr."instance_id" = cl."instance_id"
WHERE cr."disconnect_timestamp" >= TIMESTAMP '2026-06-09 00:00:00'
  AND cr."disconnect_timestamp" <  TIMESTAMP '2026-06-10 00:00:00'
  AND cr."instance_id" = '<YOUR_INSTANCE_ID>'
  AND cr."channel" = 'VOICE';
```

## Agent schedule adherence (activity-level)
<a name="data-lake-rq-schedule-adherence"></a>

**Definition:** Compares an agent's actual activity state (from `agent_statistic_record`) against their scheduled shift activities (from scheduling tables) for each time interval in a day. Produces a per-interval adherence determination: IN (agent was doing what they were scheduled to do) or OUT (they weren't).

**Output columns:** Agent, Date, Begin, End, Scheduled Activity, Actual Activity, Adherence State, Duration

**Source tables:**
+ `staff_shifts` — Agent shifts for the day (latest non-deleted version)
+ `staff_shift_activities` — Scheduled activity blocks within each shift
+ `shift_activities` — Activity name lookup (maps ARN to human-readable name)
+ `agent_statistic_record` — Actual agent state per interval
+ `users` — Agent name and ARN resolution

**Adherence logic (simplified):**
+ Scheduled "Open" — agent is IN if status is Available, On Contact, or ACW
+ Scheduled "Break" — agent is IN if status is Break or Lunch
+ Scheduled "Meeting" — agent is IN if status is Training or Meeting
+ Otherwise — OUT

```
WITH latest_shift_versions AS (
    -- Get the latest (non-deleted) shift version per shift_id
    SELECT
        shift_id,
        MAX(shift_version) AS max_version
    FROM "connect_datalake"."staff_shifts"
    WHERE is_deleted = false
      AND CAST(shift_start_timestamp AS DATE) = DATE '2026-06-10'  -- SET REPORT DATE
    GROUP BY shift_id
),

latest_shifts AS (
    SELECT
        ss.shift_id,
        ss.agent_arn,
        ss.shift_start_timestamp,
        ss.shift_end_timestamp
    FROM "connect_datalake"."staff_shifts" ss
    INNER JOIN latest_shift_versions lsv
        ON ss.shift_id = lsv.shift_id
        AND ss.shift_version = lsv.max_version
    WHERE ss.is_deleted = false
),

-- Get scheduled activity blocks with human-readable activity names
scheduled_blocks AS (
    SELECT
        ls.agent_arn,
        ssa.activity_start_timestamp,
        ssa.activity_end_timestamp,
        sa.shift_activity_name,
        CASE
            WHEN sa.shift_activity_name IN ('Work', 'Overtime') THEN 'Open'
            WHEN sa.shift_activity_name IN ('Break', 'Lunch') THEN 'Break'
            WHEN sa.shift_activity_name = 'Training' THEN 'Meeting'
            WHEN sa.shift_activity_name = 'PTO' THEN 'PTO'
            ELSE sa.shift_activity_name
        END AS scheduled_activity_label
    FROM "connect_datalake"."staff_shift_activities" ssa
    INNER JOIN latest_shifts ls
        ON ssa.shift_id = ls.shift_id
    INNER JOIN latest_shift_versions lsv
        ON ssa.shift_id = lsv.shift_id
        AND ssa.shift_version = lsv.max_version
    INNER JOIN "connect_datalake"."shift_activities" sa
        ON ssa.shift_activity_arn = sa.shift_activity_arn
    WHERE ssa.is_deleted = false
),

-- Get actual agent state intervals for the day
actual_states AS (
    SELECT
        u.user_arn AS agent_arn,
        u.first_name,
        u.last_name,
        asr.interval_start_time,
        asr.interval_end_time,
        asr.agent_status_name,
        asr.online_time,
        asr.agent_idle_time,
        asr.agent_on_contact_time,
        asr.non_productive_time,
        CASE
            WHEN asr.agent_on_contact_time IS NOT NULL AND asr.agent_on_contact_time > 0
                THEN 'On Inbound Call'
            WHEN asr.agent_idle_time IS NOT NULL AND asr.agent_idle_time > 0
                THEN 'Available'
            WHEN asr.non_productive_time IS NOT NULL AND asr.non_productive_time > 0
                THEN COALESCE(asr.agent_status_name, 'Non-Productive')
            WHEN asr.online_time IS NOT NULL AND asr.online_time > 0
                THEN 'Available'
            ELSE COALESCE(asr.agent_status_name, 'Offline')
        END AS actual_activity_label
    FROM "connect_datalake"."agent_statistic_record" asr
    INNER JOIN "connect_datalake"."users" u
        ON asr.user_id = u.user_id
    WHERE asr.interval_start_time >= TIMESTAMP '2026-06-10 00:00:00' -- SET REPORT DATE (UTC)
      AND asr.interval_start_time < TIMESTAMP '2026-06-11 00:00:00'
),

-- Join actual states with scheduled blocks
activity_timeline AS (
    SELECT
        act.first_name || ' ' || act.last_name AS agent_name,
        act.interval_start_time,
        act.interval_end_time,
        act.actual_activity_label,
        act.agent_status_name,
        COALESCE(sb.scheduled_activity_label, 'Open') AS scheduled_activity
    FROM actual_states act
    LEFT JOIN scheduled_blocks sb
        ON act.agent_arn = sb.agent_arn
        AND act.interval_start_time < sb.activity_end_timestamp
        AND act.interval_end_time > sb.activity_start_timestamp
)

SELECT
    agent_name AS "AGENT",
    CAST(interval_start_time AS DATE) AS "DATE",
    DATE_FORMAT(interval_start_time, '%H:%i:%s') AS "BEGIN",
    DATE_FORMAT(interval_end_time, '%H:%i:%s') AS "END",
    scheduled_activity AS "SCHEDULED ACTIVITY",
    actual_activity_label AS "ACTUAL ACTIVITY",
    CASE
        WHEN scheduled_activity = 'Open'
            AND actual_activity_label IN ('Available', 'On Inbound Call', 'On Outbound Call',
                                          'Call Ringing', 'Aftercall (ACW)')
            THEN 'IN'
        WHEN scheduled_activity = 'Break'
            AND agent_status_name IN ('Break', 'Lunch')
            THEN 'IN'
        WHEN scheduled_activity = 'Meeting'
            AND agent_status_name IN ('Training', 'Meeting')
            THEN 'IN'
        ELSE 'OUT'
    END AS "ADHERENCE STATE",
    CAST(DATE_DIFF('second', interval_start_time, interval_end_time) / 3600 AS VARCHAR)
        || ':' ||
        LPAD(CAST((DATE_DIFF('second', interval_start_time, interval_end_time) % 3600) / 60 AS VARCHAR), 2, '0')
        || ':' ||
        LPAD(CAST(DATE_DIFF('second', interval_start_time, interval_end_time) % 60 AS VARCHAR), 2, '0')
    AS "DURATION"
FROM activity_timeline
ORDER BY interval_start_time ASC;
```

## Best practices
<a name="data-lake-rq-best-practices"></a>
+ **Partition pruning** — Always include partition filters (`disconnect_timestamp`, `published_date`, or `creation_timestamp`) to minimize scan costs.
+ **Deduplication** — Connect Customer delivers records at least once. Use `DISTINCT` on primary keys when exact counts are required.
+ **Time zones** — All timestamps are in UTC. Apply `AT TIME ZONE` for local reporting.
+ **Milliseconds** — Most duration fields are stored in milliseconds. Divide by 1000.0 for seconds.
+ **Instance ID filter** — Always filter by `instance_id` in multi-instance environments.
+ **Real-time metrics** — For true real-time metrics, use the `GetCurrentMetricData` API. The data lake provides historical data only.