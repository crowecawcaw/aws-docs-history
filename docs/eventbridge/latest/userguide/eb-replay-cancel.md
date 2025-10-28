# Canceling replays of archived events in Amazon EventBridge

If you start a replay and then want to stop it, you can cancel it while its status is
`Starting` or `Running`.

###### To cancel a replay (console)

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the left navigation pane, choose **Replays**.
3. Choose the replay to cancel.
4. Choose **Cancel**.

###### To cancel a replay (AWS CLI)

- Use [cancel-replay](../../../cli/latest/reference/events/cancel-replay.md "../../../cli/latest/reference/events/cancel-replay.md").
