

# Canceling replays of archived events in Amazon EventBridge
<a name="eb-replay-cancel"></a>

If you start a replay and then want to stop it, you can cancel it while its status is `Starting` or `Running`.

**To cancel a replay (console)**

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/).

1. In the left navigation pane, choose **Replays**.

1. Choose the replay to cancel.

1. Choose **Cancel**.

**To cancel a replay (AWS CLI)**
+ Use [cancel-replay](https://docs.aws.amazon.com/cli/latest/reference/events/cancel-replay.html).