

# Step 1: Get an MMS-capable phone number
<a name="nx-mms-get-set-up-identities"></a>

To send MMS messages, you need an origination identity that supports the MMS channel in the destination country. MMS is currently supported in the United States and Canada. The following origination identity types support MMS:
+ **Short codes** – Supported for MMS in the United States and Canada.
+ **Long codes (10DLC)** – Supported for MMS in the United States and Canada. In the United States, 10DLC numbers require registration before you can send.
+ **Toll-free numbers** – Supported for MMS in the United States only. Toll-free numbers require registration before you can send.

The following table shows which origination identity types support MMS in each supported country.


**MMS-capable number types by country**  

| Country | Short codes | Long codes (10DLC) | Toll-free | Sender ID | 
| --- | --- | --- | --- | --- | 
| United States | Yes | Yes | Yes | No | 
| Canada | Yes | Yes | No | No | 

Request a number of a type that supports MMS in your destination country. For the full list of supported countries and their MMS capabilities, see [Country support](nx-mms-scale-country-support.md). For the full phone number request and management operations, see [Phone numbers](nx-features-phone-numbers.md).

After you request the number, you add it to a phone pool in Step 3.

To request a number from the console or the AWS CLI, choose the tab that matches how you want to work.

------
#### [ Console ]

**To request a phone number (console)**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/end-user-messaging/](https://console.aws.amazon.com/end-user-messaging/).

1. In the navigation pane, under **Configurations**, choose **Phone numbers**, and then choose **Request originator**.

1. For **Country**, choose the destination country, and for **Number settings** select the capabilities you need (such as **MMS**). Choose a number type that supports your destination, then follow the prompts to request the number. Some number types require registration before you can send.

1. To finish without waiting for registration, request a **Simulator number** instead. Simulator numbers send realistic events without using the carrier network.

------
#### [ AWS CLI ]

Use the [request-phone-number](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/request-phone-number.html) command. Replace {{US}} with the two-letter ISO country code and {{NUMBER\_TYPE}} with a type that supports your destination (such as `LONG_CODE`, `TOLL_FREE`, or `SHORT_CODE`).

```
$ aws pinpoint-sms-voice-v2 request-phone-number \
> --iso-country-code {{US}} \
> --message-type {{TRANSACTIONAL}} \
> --number-capabilities {{MMS}} \
> --number-type {{NUMBER_TYPE}}
```

------