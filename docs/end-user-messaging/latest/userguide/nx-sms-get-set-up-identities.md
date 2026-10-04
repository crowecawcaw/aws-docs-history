

# Step 1: Get a phone number
<a name="nx-sms-get-set-up-identities"></a>

To send SMS messages, you need an origination identity. For SMS, an origination identity is either a phone number or a sender ID. The types available to you depend on the destination country and the regulations that apply there:


**SMS origination identity types**  

| Type | Description | 
| --- | --- | 
| Long codes (10DLC) | Standard local phone numbers. In the United States, 10DLC is the standard local number type and requires registration before you can send. | 
| Toll-free numbers | Toll-free numbers available in the United States and Canada. Requires registration before you can send. | 
| Short codes | High-throughput numbers for high-volume sending. Requires registration and carrier approval. | 
| Sender IDs | An alphanumeric name that identifies you as the sender, supported in many countries. Some countries require sender ID registration, and others allow unregistered sender IDs. | 
| Simulator numbers | Test numbers that generate realistic events without sending over the carrier network, with no registration required. Simulator numbers can only send to other simulator destination numbers in the same country. | 

The types available to you, and which ones require registration, depend on the destination country. To confirm what each country supports, see [Launch in a country](nx-sms-country-support.md).

**Tip**  
How you start testing depends on your destination country. If the country has simulator support, request a simulator number and begin sending test messages right away, without waiting for registration. If you are sending to a country that allows unregistered sender IDs, you can use a sender ID to start sending without the registration and carrier approval that number types require. For more information about requesting and managing phone numbers, see [Phone numbers](nx-features-phone-numbers.md); for sender IDs, see [Sender IDs](nx-features-senders.md).

To request a number from the console or the AWS CLI, choose the tab that matches how you want to work.

------
#### [ Console ]

**To request a phone number (console)**

1. Open the AWS End User Messaging console at [https://console.aws.amazon.com/end-user-messaging/](https://console.aws.amazon.com/end-user-messaging/).

1. In the navigation pane, under **Configurations**, choose **Phone numbers**, and then choose **Request originator**.

1. For **Country**, choose the destination country, and for **Number settings** select the capabilities you need (such as **SMS**). Choose a number type that supports your destination, then follow the prompts to request the number. Some number types require registration before you can send.

1. To finish without waiting for registration, request a **Simulator number** instead. Simulator numbers send realistic events without using the carrier network.

------
#### [ AWS CLI ]

Use the [request-phone-number](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/request-phone-number.html) command. Replace {{XX}} with the two-letter ISO country code and {{NUMBER\_TYPE}} with a type that supports your destination (such as `LONG_CODE`, `TOLL_FREE`, or `SHORT_CODE`).

```
$ aws pinpoint-sms-voice-v2 request-phone-number \
> --iso-country-code {{XX}} \
> --message-type {{TRANSACTIONAL}} \
> --number-capabilities {{SMS}} \
> --number-type {{NUMBER_TYPE}}
```

------