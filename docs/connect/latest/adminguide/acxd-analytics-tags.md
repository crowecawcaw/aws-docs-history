# Analytics tags

Analytics tags help you mark important moments in a conversation flow so you can
track how users move through your agentic CX designer application.

A tag can be applied to a specific node in a flow. When a user reaches that node
during a deployed conversation, the tag is recorded. You can then use tags to
review flow traversal, filter conversation history, or create analytics dashboard
charts around milestones that matter to your team.

Use analytics tags to track moments such as:

- Task started or completed
- User reached fallback or escalation
- Booking completed
- Offer accepted or declined
- Knowledge base answer shown
- Payment handoff started
- User reached a key decision point
  Analytics tags do not automatically determine whether a conversation was
  successful, helpful, or automated. They mark the points you choose so you can
  measure and review them later.

To access analytics tags, select **Analytics** from your workspace menu then
choose **Analytics tags**.

## Strategic tag placement

Users may not always complete a conversation in the way you expect. They may
abandon a flow, loop through a retry path, escalate to a human agent, or complete a
task successfully.

By placing analytics tags at strategic points in a flow, you can better understand
where users are going and what outcomes they are reaching.

For example:

| Tag placement                | What it tells you                                 |
| ---------------------------- | ------------------------------------------------- |
| First node in a booking flow | How many users begin the booking process.         |
| Confirmation node            | How many users complete the booking.              |
| Fallback or recovery path    | How often users hit an error or unsupported path. |
| Human handoff node           | How often users request or require escalation.    |
| Decline path after an offer  | How often users reject an offer.                  |

These tags can help you identify completion rates, drop-off points, repeated
issues, and opportunities to improve the experience.

## Default system tags

Agentic CX designer includes default system tags that can be used in flows:

- Automated
- Not helpful
- Escalated

These tags are available by default, but they do not automatically classify a
conversation. You decide where to place them based on what each point in your
flow represents.

For example, you might place Automated on a node reached after the application
completes a task without human handoff, or Not helpful on a path where the user
indicates the answer did not solve their issue.

## Custom analytics tags

You can create custom analytics tags for the milestones, outcomes, or events that
matter to your application.

###### To add a custom analytics tag

1. Open **Analytics**.
2. Select **Analytics tags**.
3. Choose **Create tag**.
4. Enter the tag details.
5. Save the tag.

Custom tag fields include:

|                 |                                                                                                                |
| --------------- | -------------------------------------------------------------------------------------------------------------- |
| **Name**        | The name of the tag that appears when tagging nodes in a flow. Use a clear, descriptive name.                  |
| **Category**    | Categorizes the tag for analytics reporting, if available.                                                     |
| **Description** | Explains what the tag is intended to track. This description is visible from the Analytics tags resource page. |

Tag labels should be easy to understand and consistent across the workspace. Use
names that describe the event clearly, such as booking\_completed, escalation\_requested, or payment\_started.

## Applying tags to nodes

After a tag is created, you can apply it to nodes in a flow.

###### To add an analytics tag to a node

1. Open the flow in the Canvas.
2. Select the node you want to track.
3. Open the node's **Add functionality** menu.
4. Choose **Analytics tags**.
5. Select one or more tags.
6. Save the flow.

Once the updated flow is included in a deployed build, future conversations that
reach the tagged node will record the tag.

You can review tag activity in several places:

|                          |                                                                                    |
| ------------------------ | ---------------------------------------------------------------------------------- |
| **In-Canvas analytics**  | Filter the flow view to conversations that reached tagged nodes.                   |
| **Conversation history** | Filter transcripts by selected tags to review sessions where a milestone occurred. |
| **Analytics dashboards** | Create dashboard charts that track tag activity over time.                         |

Use tags when you want to move beyond general conversation volume and monitor
specific outcomes or checkpoints inside the experience.

## Deleting a tag

###### To delete a custom tag

1. Open **Analytics**.
2. Select **Analytics tags**.
3. Expand the tag details.
4. Choose **Delete**.

Before deleting a tag, confirm that it is no longer needed for active reporting or flow analysis.

## Best practices

- Analytics tags only apply to conversations that occur after the tag is added to a node and deployed.
- Tags are not applied retroactively to previous conversations.
- A node can have more than one tag, but using one tag per node is often easier to interpret and helps avoid confusing counts.
- Tags mark that a node was reached; they do not automatically explain why the user reached that node.
- Use clear tag names and descriptions so teammates understand what each tag is intended to measure.
