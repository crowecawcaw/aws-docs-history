

# Managing Amazon DocumentDB event notification subscriptions
<a name="event-subscriptions.managing"></a>

If you choose **Event subscriptions** in the navigation pane of the Amazon DocumentDB console, you can view subscription categories and a list of your current subscriptions. You can also modify or delete a specific subscription.

## To modify your current Amazon DocumentDB event notification subscriptions
<a name="event-subscriptions.modify"></a>

1. Sign in to the AWS Management Console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb).

1. In the navigation pane, choose **Event subscriptions**. The **Event subscriptions** pane shows all your event notification subscriptions.   
![Amazon DocumentDB console navigation pane with Event Subscriptions option highlighted.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/event-subs/modify-event-subs.png)

1. In the **Event subscriptions** pane, choose the subscription that you want to modify and choose **Edit**.  
![The Event subscriptions pane showing a selected subscription and the Edit button.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/event-subs/modify-edit.png)

1. Make your changes to the subscription in either the **Target** or **Source** section. You can add or remove source identifiers by selecting or deselecting them in the Source section.   
![The Modify event subscription form highlighting the Target section.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/event-subs/modify-target.png)

1. Choose **Modify**. The Amazon DocumentDB console indicates that the subscription is being modified.   
![The end of the Modify event subscription form with the Modify button highlighted.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/event-subs/modify-button.png)

## Deleting an Amazon DocumentDB event notification subscription
<a name="event-subscriptions.delete"></a>

You can delete a subscription when you no longer need it. All subscribers to the topic will no longer receive event notifications specified by the subscription. 

1. Sign in to the AWS Management Console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb).

1. In the navigation pane, choose **Event subscriptions**.   
![Amazon DocumentDB console navigation pane with Event Subscriptions option highlighted.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/event-subs/delete-event-subs.png)

1. In the **Event subscriptions** pane, choose the subscription that you want to delete.   
![The Event subscriptions pane showing a selected subscription.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/event-subs/delete-select.png)

1. Choose **Delete**.  
![The Event subscriptions pane highlighting the Delete button.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/event-subs/delete-delete.png)

1. A pop-up window will appear asking you if you want to permanently delete this notification. Choose **Delete**.  
![A dialog box confirming deletion of the event subscription with the Delete button highlighted in the lower-right corner.](http://docs.aws.amazon.com/documentdb/latest/devguide/images/event-subs/delete-delete-2.png)