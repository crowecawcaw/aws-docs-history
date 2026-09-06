

# Delete a keyword from a phone pool in AWS End User Messaging SMS
<a name="keywords-pool-delete"></a>

Use the AWS End User Messaging SMS console or AWS CLI to delete a keyword from your phone pool.

------
#### [ Delete a keyword (Console) ]

Use the AWS End User Messaging SMS console to delete keywords in your pool. 

**Note**  
Required opt-out keywords can't be deleted.

**To delete a keyword**

1. Open the AWS End User Messaging SMS console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Configurations**, choose **Phone pools**.

1. On the **Phone Pools** page, choose the pool that contains the keyword.

1. On the **Keywords** tab, choose the keyword and then **Remove keyword**. 

------
#### [ Delete a keyword (AWS CLI) ]

You can use the [delete-keyword](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/delete-keyword.html) CLI to delete a keyword.

At the command line, enter the following command:

```
$ aws pinpoint-sms-voice-v2 delete-keyword \
> --origination-identity {{OriginationIdentity}} \
> --keyword {{Keyword}}
```

In the preceding command, make the following changes:
+ Replace {{OriginationIdentity}} with the unique ID or Amazon Resource Name (ARN) of the phone number or sender ID that you want to remove the keyword from.
+ Replace {{Keyword}} with the keyword to delete.

------