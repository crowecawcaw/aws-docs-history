

# Updating a data subscriber in Security Lake
<a name="subscriber-update"></a>

You can update a subscriber by changing the sources from which the subscriber consumes. You can also assign or edit the tags for a subscriber. A *tag* is a label that you can define and assign to certain types of AWS resources, including subscribers. To learn more, see [Tagging Security Lake resources](tagging-resources.md).

Choose one of the access methods, and follow these steps to define new sources for an existing subscription.

------
#### [ Console ]

1. Open the Security Lake console at [https://console.aws.amazon.com/securitylake/](https://console.aws.amazon.com/securitylake/).

1. In the navigation pane, choose **Subscribers**.

1. Select the subscriber.

1. Choose **Edit**, and then do any of the following:
   + To update the sources for the subscriber, enter the new settings in the **Log and event sources** section.
   + To assign or edit tags for the subscriber, change the tags as necessary in the **Tags** section.

1. When you finish, choose **Save**.

------
#### [ API ]

To update data access sources for a subscriber programmatically, use the [UpdateSubscriber](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_UpdateSubscriber.html) operation of the Security Lake API. If you're using the AWS Command Line Interface (AWS CLI), run the [update-subscriber](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/update-subscriber.html) command. In your request, use the `sources` parameters to specify each source that you want the subscriber to access.

```
$ aws securitylake update-subscriber --subscriber-id {{subscriber ID}}
```

For a list of subscribers associated with a specific AWS account or organization, use the [ListSubscribers](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_ListSubscribers.html) operation. If you're using the AWS Command Line Interface (AWS CLI), run the [list-subscribers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/list-subscribers.html) command.

```
$ aws securitylake list-subscribers
```

To review the current settings for a particular subscriber, use the [GetSubscriber](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_GetSubscriber.html) operation. run the [get-subscriber](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/get-subscriber.html) command. Security Lake then returns the subscriber's name and description, external ID, and additional information. If you're using the AWS Command Line Interface (AWS CLI), run the [get-subscriber](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/get-subscriber.html) command.

 To update the notification method for a subscriber, use the [UpdateSubscriberNotification](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_UpdateSubscriberNotification.html) operation. If you're using the AWS Command Line Interface (AWS CLI), run the [update-subscriber-notification](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/update-subscriber-notification.html) command. For example, you can specify a new HTTPS endpoint for the subscriber or switch from an HTTPS endpoint to an Amazon SQS queue.

------