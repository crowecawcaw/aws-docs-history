# Conversation history

Conversation history provides historical information about sessions that have taken
place with a deployed agentic CX designer application.

Use these historical transcripts to review what happened during real user
interactions, troubleshoot unexpected behavior, inspect transcripts, and identify
opportunities to improve flows, routing, prompts, integrations, or escalation paths.

Conversation history gives you a session-level view of user interactions with your
deployed application.

Each conversation record can help you understand:

- What the user asked
- How long the session lasted and latency of the system
- Whether the user engaged or abandoned the experience
- Whether analytics tags were reached
- What the full transcript looked like
  Use conversation history when you need to move from high-level performance data
  into the details of a specific user session.

## Accessing conversation history

###### To access conversation history for an application

1. Open **Applications**.
2. Select a deployed application.
3. Open the **Observe** tab.
4. Select **Conversation history**.
5. Review the Conversations table.

The **Observe** tab appears after an application has been deployed for the first time.

## Filters

Use filters to narrow conversation history to the sessions you want to inspect.

|                    |                                                                     |
| ------------------ | ------------------------------------------------------------------- |
| **Date range**     | Filter conversations within a specific date and time range.         |
| **Engagement**     | Filter for conversations where the user did or did not respond.     |
| **Analytics tags** | Review conversations where selected analytics tags were reached.    |
| **Search**         | Find conversations containing specific user utterances or keywords. |

Filters are useful when investigating a known issue, reviewing behavior from a
specific release window, or finding examples of repeated user friction.

Each row in the conversation history table represents a unique conversation session.

Select a conversation row to view more details.

## Conversation details

When you open a conversation, you can review the full transcript and supporting
session details.

Conversation details include:

- Conversation ID (select the Information icon)
- User ID (select the Information icon)
- Full message transcript

  - User messages
  - Application responses

- Debugger/event log (select a message in the transcript to review all events in the selected turn)

|                     |                                                                                                                    |
| ------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **First utterance** | The first user utterance in the conversation. If a user started a session and did not engage, this appears as N/A. |
| **Start time**      | When the conversation session started.                                                                             |
| **Duration**        | How long the conversation lasted.                                                                                  |
| **Confidence**      | Confidence or AI-related scoring details available for the session.                                                |
| **Latency**         | How long the application took to respond on average.                                                               |
| **Flows**           | Flows invoked during the conversation.                                                                             |
| **Tags**            | Analytics tags reached during the session, when available.                                                         |
| **Transcript**      | The full exchange between the user and the application.                                                            |

Copy options are available for conversation and user IDs. These IDs can be useful
when investigating a specific session or reviewing that same path in In-Canvas analytics.

## Troubleshooting workflow

Conversation history helps explain what happened in a transcript. In-Canvas
analytics helps you see where that conversation traveled inside a flow.

A common troubleshooting workflow is:

1. Find the relevant conversation in Conversation history.
2. Open the conversation and review the transcript.
3. Select the information icon > Copy the Conversation ID.
4. Open the flow involved in the conversation.
5. Use In-Canvas analytics to filter by that Conversation ID.
6. Review the path the user took through the flow.

This is useful when a conversation shows unexpected fallback behavior, missed
routing, repeated questions, drop-off, or escalation.

## Common use cases

|                                    |                                                                                                       |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Review a specific interaction**  | Review the transcript to see what the user asked and how the application responded.                   |
| **Investigate escalations**        | Filter by escalation-related flows or tags and inspect the conversations leading up to escalation.    |
| **Identify drop-off patterns**     | Review transcripts near drop-off points and compare with In-Canvas analytics.                         |
| **Validate routing**               | Search for user utterances and review whether routing matched the intended flow.                      |
| **Investigate integration issues** | Review affected conversations and compare timing or failure behavior.                                 |
| **Discover new content needs**     | Search repeated phrases and identify whether a new flow, prompt, or knowledge base content is needed. |
