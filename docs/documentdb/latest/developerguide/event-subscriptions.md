# Subscribing to Amazon DocumentDB events

You can use the Amazon DocumentDB console to subscribe to event subscriptions, as follows:

1. Sign in to the AWS Management Console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb "https://console.aws.amazon.com/docdb").
2. In the navigation pane, choose **Event subscriptions**.

![Amazon DocumentDB console navigation pane with Event Subscriptions option highlighted.](images/event-subs/subscribe-event-subs.png) 3. In the **Event subscriptions** pane, choose **Create event subscription**.

![Event Subscriptions pane highlighting the Create event subscription button in the upper-right corner.](images/event-subs/subscribe-create.png) 4. In the **Create event subscription** dialog box, do the following:

    * For **Name**, enter a name for the event notification subscription.



    ![The Create event subscription form showing the Details section and the Name input field.](images/event-subs/subscribe-name.png)
    * For **Target**, choose where you want to send notifications to. You can choose an existing **ARN** or choose **New Email Topic** to enter the name of a topic and a list of recipients.



    ![The Target section with options to specify where to send notifications to.](images/event-subs/subscribe-target.png)
    * For **Source**, choose a source type. Depending on the source type you selected, choose the event categories and the sources that you want to receive event notifications from.



    ![The Source section to select a source type to receive event notifications from.](images/event-subs/subscribe-source.png)
    * Choose **Create**.



    ![The Source section with the Create button in the lower-right corner.](images/event-subs/subscribe-create-2.png)
