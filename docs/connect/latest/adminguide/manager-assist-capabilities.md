

# Capabilities overview for manager assist
<a name="manager-assist-capabilities"></a>

More than 150 Connect Customer metrics are supported across all capability categories. You can ask about current performance, investigate historical trends, compare metrics across dimensions, and optimize self-service operations.

## How it works
<a name="manager-assist-how-it-works"></a>

When you submit a question, it is processed in the following steps:

1. **Ask** – you type a question in plain language.

1. **Interpret** – the metrics, entities (such as queues and agents), and time range in your question are identified.

1. **Retrieve** – the data that you have permission to view is retrieved and structured into a response.

1. **Act** – you review the response and, optionally, ask a follow-up question.

## Supported question types
<a name="manager-assist-query-types"></a>


| Question type | Description | Example | 
| --- | --- | --- | 
| Metric lookup | Retrieve a specific metric value. | What is the average handle time for the Sales queue today? | 
| Trend analysis | View metric changes over time. | Show me abandonment rate for the past 7 days. | 
| Comparison | Compare metrics across queues, agents, or time periods. | Compare service level between Sales and Support this week. | 
| Leaderboard | Rank agents or queues by a metric. | Who are the top 5 agents by contacts handled? | 
| Drill-down | Investigate a specific contact or time period. | What happened during the 2 PM hour today? | 
| Compound question | Ask a multi-part question in one message. | What is our busiest queue, and what is its current service level? | 
| Self-service analysis | Evaluate containment and deflection performance. | What percentage of contacts were resolved without reaching a live representative? | 
| Metric definition | Explain how a metric is calculated. | How is occupancy calculated? | 

## Capability categories
<a name="manager-assist-capability-categories"></a>


| Category | Description | 
| --- | --- | 
| Agent performance | Handle time, satisfaction, contacts handled, occupancy, after-contact work. | 
| Queue metrics | Service level, speed of answer, wait times, queue depth. | 
| Contact volume and trends | Total contacts, hourly breakdown, channel splits, historical patterns. | 
| Real-time insights | Current agent states, active queue depths, longest wait. | 
| Self-service optimization | Containment rate, deflection rate, bot performance, IVR completion, repeat contacts. | 
| Custom analysis | Questions that use the custom metrics defined in your instance. | 
| Leaderboards | Ranked views of agents or queues by selected metrics. | 
| Historical trends | Multi-day or multi-week metric patterns and comparisons. | 
| Per-contact drill-down | Investigation of an individual contact. | 
| Metric definitions | Explanations of metric calculations. | 
| Abandonment analysis | Abandonment patterns, rates by time, contributing factors. | 
| Service level analysis | Service level tracking and target comparisons. | 
| Channel analysis | Performance by voice, chat, email, and task. | 
| Transfer and escalation patterns | Transfer rates and escalation flows. | 
| Evaluations and quality | Evaluation scores, completion rates, quality trends. | 

## Supported metric categories
<a name="manager-assist-metric-categories"></a>


| Category | Examples | 
| --- | --- | 
| Contact handling | Average handle time, after-contact work time, hold time, interaction time | 
| Queue performance | Service level, speed of answer, queue wait time, contacts in queue | 
| Agent activity | Occupancy, availability, idle time, contacts handled | 
| Contact volume | Contacts queued, contacts handled, contacts abandoned, contacts transferred | 
| AI agents | Self-service resolution rate, containment rate, escalation rate, intent recognition confidence, average AI agent interaction duration | 
| Flow performance | Flow completion rate, flow abandonment rate, average time in flow, flow error rate, transfer-out rate | 
| Bots | Bot resolution rate, intent match rate, fallback intent rate, average bot conversation duration, slot fill rate | 
| Cases | Cases created, cases resolved, average resolution time, cases reopened, first-contact resolution rate | 
| Outbound campaigns | Contacts attempted, contacts reached, connection rate, right-party contact rate, campaign completion rate | 
| Customer experience | Abandonment rate, callback metrics | 
| Evaluations | Evaluation scores, evaluation completion rates | 
| Custom metrics | Any custom metrics defined in your instance | 

## Self-service optimization questions
<a name="manager-assist-self-service-questions"></a>

You can evaluate and optimize your self-service strategy. The following table provides example questions.


| Category | Example question | 
| --- | --- | 
| Self-service resolution | What is our self-service resolution rate this week compared to last week? | 
| Transfer out | What percentage of callers opted out of self-service and transferred to a queue? | 
| Flow performance | Which self-service flows have the highest abandonment rate? | 
| Bot effectiveness | Which intents have the lowest resolution rate in our chat bot? | 
| Channel shift | What percentage of our contacts are coming through chat compared to voice this month? | 
| Repeat contacts | What is the repeat contact rate for customers who used self-service first? | 
| Automation opportunity | Which 10 contact reasons could potentially be automated? | 

## Manage your chats
<a name="manager-assist-manage-chats"></a>

Each chat is saved, so you can return to a chat later, start a new chat for an unrelated question, or continue where you left off.

### Start a new chat
<a name="manager-assist-new-chat"></a>

Start a new chat when you want to ask about a different topic. Your previous chat is saved automatically and remains available in **History**.

**To start a new chat**

1. In the assistant panel, choose **New chat**.

1. Type your first question.

Starting a new chat clears the conversation from the panel but does not delete it. You can open it again from **History**.

![The assistant panel header, with the New chat icon.](http://docs.aws.amazon.com/connect/latest/adminguide/images/manager-assistant-new-chat.png)


### View your chat history
<a name="manager-assist-chat-history"></a>

Your chats from the last 60 days are kept, so you can revisit an earlier response or continue an unfinished chat.

**To view your chat history**

1. In the assistant panel, choose **History**.

1. Your past chats appear grouped by date, for example **Today** or **Yesterday**, with the newest chat first within each group. Each row shows the first question that you asked in that chat.

1. To see older chats, choose **View more** at the bottom of the panel.

**Note**  
**History** shows only the chats that you started, and only those that you still have permission to view.

![The History panel, listing chats from the last 60 days grouped by date, with the first question of each chat.](http://docs.aws.amazon.com/connect/latest/adminguide/images/manager-assistant-chat-history.png)


### Resume a chat
<a name="manager-assist-resume-chat"></a>

Resume a chat when you want to continue an earlier conversation. The full chat is reloaded, so responses to your follow-up questions reflect the earlier turns.

**To resume a chat**

1. Choose **History**.

1. Choose the chat that you want to resume. The chat reloads in the panel.

1. After the messages finish loading, type your next question.

**Tip**  
Resume a chat when your new question builds on an earlier one, for example when you drill into the same metric or time range. Start a new chat when your question is unrelated.

**Important**  
Because a resumed chat carries the full earlier conversation, responses might reference details from previous turns. To get a response that is based only on your new question, start a new chat.