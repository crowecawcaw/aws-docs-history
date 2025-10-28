# Removing a data subscriber from Security Lake

If you no longer want a subscriber to consume data from Security Lake, you can remove the
subscriber by following these steps.

Console

1. Open the Security Lake console at [https://console.aws.amazon.com/securitylake/](https://console.aws.amazon.com/securitylake/ "https://console.aws.amazon.com/securitylake/").
2. In the navigation pane, choose
   **Subscribers**.
3. Select the subscriber that you want to remove.
4. Choose **Delete** and confirm the action. This will delete the subscriber
   and all the associated notification settings.

APIBased on your scenario, do one of the following:

- To delete the subscriber and all associated notification settings,
  use the [DeleteSubscriber](../APIReference/API_DeleteSubscriber.md "../APIReference/API_DeleteSubscriber.md") operation of the Security Lake API. If you're using the
  AWS Command Line Interface (AWS CLI), run the [delete-subscriber](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/delete-subscriber.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/delete-subscriber.html") command.
- To retain the subscriber but stop future notifications to the
  subscriber, use the [DeleteSubscriberNotification](../APIReference/API_DeleteSubscriberNotification.md "../APIReference/API_DeleteSubscriberNotification.md") operation of the Security Lake
  API. If you're using the
  AWS Command Line Interface (AWS CLI), run the run the [delete-subscriber-notification](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/delete-subscriber-notification.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/delete-subscriber-notification.html") command.
