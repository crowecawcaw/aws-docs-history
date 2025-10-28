# Creating replays of archived events in

Amazon EventBridge

When you start a new replay, you specify a time period for the event you want EventBridge to resend to the source event bus. You can also specify for EventBridge to send the events to specific rules.

###### To start an event replay (console)

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. Navigate to the replays directly, or from the archive you want to replay:
   - In the navigation pane, choose **Archives**.

   On the **Archives** page, choose the archive and then choose**Replay**.
   - In the navigation pane, choose **Replays**.

   Choose **Start new replay**.

3. Enter a **Name** for the replay and, optionally, a
   **Description**.
4. For **Source**, select the archive to replay events from.
5. For destination, you can replay events only to the same event bus that emitted the
   events.
6. For **Specify rules**, do one of the following:
   - Choose **All rules** to replay events to all
     rules.
   - Choose **Specify rules**, and then select the rule or
     rules to replay the events to.

7. Under **Replay time frame**, specify the
   **Date**, **Time**, and **Time
   zone** for the **Start time** and the **End
   time**.

Only events that occurred between the **Start time** and
**End time** are replayed. 8. Choose **Start replay**.

###### To start a replay (AWS CLI)

- Use [start-replay](../../../cli/latest/reference/events/start-replay.md "../../../cli/latest/reference/events/start-replay.md").
