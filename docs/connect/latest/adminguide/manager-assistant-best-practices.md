# Best practices for manager assistant

Follow these best practices to get the most accurate and useful responses from
manager assistant.

## Prompting guidance

### Be specific about time ranges

Include the period that you want data from. Manager assistant returns better
results when your question includes an explicit time reference.

| Instead of this              | Try this                                                               |
| ---------------------------- | ---------------------------------------------------------------------- |
| How are we doing?            | What is our service level across all queues<br>today?                  |
| Tell me about the queue.     | What is the abandonment rate for the Sales queue this<br>week?         |
| How is this area performing? | What is the average handle time today compared to the team<br>average? |

### Use exact resource names

Refer to queues, routing profiles, and other resources by the exact names that they
have in Connect Customer. If you are not sure of an exact name, ask manager assistant:
`What queues are available?`

### Use standard metric terminology

| Recommended term        | Instead of              |
| ----------------------- | ----------------------- |
| Average handle time     | Call length, talk time  |
| Service level           | SLA                     |
| Abandonment rate        | Drop rate, hang-up rate |
| Occupancy               | Utilization             |
| After-contact work time | Wrap-up time            |
| Contacts handled        | Calls taken             |
| Containment rate        | Bot success rate        |

### Ask one primary question at a time

Start with a focused question, and then use follow-up questions to explore in more
detail. This approach produces more accurate results than a single complex
question.

### Start broad, then narrow

Begin with an overview question, and then drill into specifics. For example:

1. Are any queues below our service level target right now?
2. What is causing the Billing queue to be below target?
3. How many contacts are currently waiting in that queue?

## Common mistakes

| Mistake                          | Impact                                                      | Correction                                                                          |
| -------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| No time range specified          | May return an unexpected default range.                     | Include a time reference such as today or this week, or explicit<br>dates.          |
| Informal metric names            | May not be recognized.                                      | Use standard Connect Customer metric terminology.                                   |
| Overly complex compound question | May return partial or inaccurate results.                   | Break the question into multiple sequential<br>questions.                           |
| Not using follow-up questions    | Repeats full context and loses the investigation<br>thread. | Use follow-up questions such as `Break that down by<br>hour.`                       |
| Vague resource references        | An incorrect resource might be selected.                    | Use exact names, such as the Premium Support queue instead of<br>the support queue. |

## Recommended daily workflow

| Time of day         | Goal                      | Example question                                               |
| ------------------- | ------------------------- | -------------------------------------------------------------- |
| Start of shift      | Assess the current state. | What is the current queue status and agent<br>availability?    |
| Mid-morning         | Track targets.            | How are we tracking on service level so far<br>today?          |
| After a spike       | Investigate issues.       | Why did wait times increase in the last hour?                  |
| Midday              | Check performance.        | Who are my top and bottom performers today by handle<br>time?  |
| End of day          | Summarize and compare.    | Compare today's performance to yesterday across all<br>queues. |
| Self-service review | Optimize automation.      | What is our containment rate trend over the past 7<br>days?    |

## How manager assistant interprets time ranges

Manager assistant interprets time references and calculation boundaries as
follows.

| Expression  | Interpretation                                                                                 |
| ----------- | ---------------------------------------------------------------------------------------------- |
| Today       | The current calendar day in the time zone of your instance, from<br>00:00 to the current time. |
| Yesterday   | The previous calendar day, from 00:00 to 23:59 in the time zone<br>of your instance.           |
| This week   | The current week, starting from the most recent Sunday in the<br>time zone of your instance.   |
| Last 7 days | The 7 complete calendar days before today.                                                     |
| Last hour   | The rolling 60 minutes before the current time.                                                |
| This month  | The current month, from the first day of the month to the<br>current date.                     |

## Validate before you act

- Cross-reference critical findings with your Connect Customer dashboards before you
  act.
- Use manager assistant for rapid triage, and then confirm with formal reports
  for decisions that have significant operational impact.
- Document decisions separately. Manager assistant provides insights, and is
  not a system of record.

###### Important

Responses from manager assistant might contain inaccuracies. Always validate
information before you make business decisions.
