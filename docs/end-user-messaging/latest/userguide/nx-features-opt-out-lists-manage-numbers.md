

# Managing opt-out list phone numbers
<a name="nx-features-opt-out-lists-manage-numbers"></a>

Use the AWS End User Messaging console or AWS CLI to add or remove destination phone numbers from your opt-out list or to view the origination identities associated with the opt-out list.

------
#### [ Add a destination number (Console) ]

When you add a phone number to an opt-out list that phone number will no longer receive messages sent from an origination identity that is linked to the opt-out list.

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/end-user-messaging/](https://console.aws.amazon.com/end-user-messaging/).

1. In the navigation pane, under **Configurations**, choose **Opt-out lists**.

1. On the **Opt-out lists** page, choose an opt-out list.

1. On the **Opted-out numbers** tab, choose **Add number**.

1. On the **Add opt-out number** page, for **Destination number** enter in the phone number to add to the opt-out list. The phone number must be in E.164 format, for example \+12065550150.

1. Choose **Add number**

------
#### [ Search for an opted-out destination number (Console) ]

You can search an opt-out list to see if the opt-out list contains a destination number.

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/end-user-messaging/](https://console.aws.amazon.com/end-user-messaging/).

1. In the navigation pane, under **Configurations**, choose **Opt-out lists**.

1. On the **Opt-out lists** page, choose an opt-out list.

1. On the **Opted-out numbers** tab enter a phone number into the search field. The phone number must be in E.164 format for example **\+12065550149**.

1. Choose **Search**.

------
#### [ View originators (Console) ]

Multiple origination identities can use the same opt-out list. You can view a list of origination identities associated with an opt-out list in the **Linked origination numbers** tab.

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/end-user-messaging/](https://console.aws.amazon.com/end-user-messaging/).

1. In the navigation pane, under **Configurations**, choose **Opt-out lists**.

1. On the **Opt-out lists** page, choose an opt-out list.

1. On the **Linked origination numbers** tab you can view all origination identities associated with the opt-out list.

------
#### [ Add a destination number (AWS CLI) ]

When you add a phone number to an opt-out list that phone number will no longer receive messages sent from an origination identity that is linked to the opt-out list.

You can use the [put-opted-out-number](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/put-opted-out-number.html) command add a phone number to an opt-out list.

At the command line, enter the following command:

```
$ aws pinpoint-sms-voice-v2 put-opted-out-number \
> --opt-out-list-name {{optOutListName}} \
> --opted-out-number {{+12065550123}}
```

In the preceding example, make the following changes:
+ Replace {{optOutListName}} with the name or Amazon Resource Name (ARN) of the opt-out list that you want to add the destination identity to.
+ Replace {{\+12065550123}} with phone number that you want to add to the opt-out list. The phone number must be formatted in E.164 format.

------
#### [ Remove a destination number (Console) ]

When you remove a phone number to an opt-out list that phone number will receive messages sent from an origination identity that is linked to the opt-out list.

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/end-user-messaging/](https://console.aws.amazon.com/end-user-messaging/).

1. In the navigation pane, under **Configurations**, choose **Opt-out lists**.

1. On the **Opt-out lists** page, choose an opt-out list.

1. On the **Opted-out numbers** tab enter the phone number to remove and then **Search**.

1. If the phone number is found use it can be removed from the opt-out list by using **Remove number**.

1. In the **Remove opted-out number** window enter **release** and then **Remove number**.

------
#### [ Remove a destination number (AWS CLI) ]

When you remove a phone number to an opt-out list that phone number will receive messages sent from an origination identity that is linked to the opt-out list.

You can use the [delete-opted-out-number](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/delete-opted-out-number.html) command remove a phone number to an opt-out list.

At the command line, enter the following command:

```
$ aws pinpoint-sms-voice-v2 delete-opted-out-number \
> --opt-out-list-name {{optOutListName}} \
> --opted-out-number {{+12065550123}}
```

In the preceding example, make the following changes:
+ Replace {{optOutListName}} with the name or Amazon Resource Name (ARN) of the opt-out list that you want to add the destination identity to.
+ Replace {{\+12065550123}} with phone number that you want to add to the opt-out list. The phone number must be formatted in E.164 format.

------