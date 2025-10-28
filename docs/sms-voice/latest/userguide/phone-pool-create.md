# Create a phone pool in AWS End User Messaging SMS

When you create a new phone pool it will inherit all of the settings from the first phone
number or sender ID that is added. For example, if you create a pool and the first phone number added has two-way messaging enabled, the other phone numbers that you add to the pool must also have
two-way messaging enabled.

Create a phone pool (Console)
To create a pool using the AWS End User Messaging SMS console, follow these steps:

###### To create a pool (Console)

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under **Configurations**, choose
   **Phone pools**.
3. On the **Phone pools** page, choose **Create phone
   pool**.
4. Under the **Pool setup** section, for **Pool name**
   enter a name for your pool.
5. Choose one of the following options:
   - **Phone number** – In the
     **Phone numbers available for association** section, choose a phone
     number to associate with the pool.
     - **Simulator number** (Optional)– If you don't have any phone numbers and
       want to request a simulator phone number then choose **Phone number** and
       in the **Phone numbers available for association** section, do the
       following:
       - Choose **Request simulator number**.
       - In **Request simulator number**, choose your country from the
         dropdown list.
       - Choose **Request number**.
       - In **Phone numbers available for association**, choose the new simulator phone number.

   - **Sender ID** – In the
     **Sender IDs available for association** section, choose a sender ID to
     associate with the pool.

6. (Optional) Expand the **Tags** and choose **Add new
   tag**.
   1. Enter a new blank key/value pair.
   2. (Optional) Choose **Add new tag** to add another tag.

7. Choose **Create phone pool**.

Create a phone pool (AWS CLI)
You can use the [create-pool](../../../cli/latest/reference/pinpoint-sms-voice-v2/create-pool.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/create-pool.md") command to
create new pools.

You can also add a phone number to a pool when you use the `RequestPhoneNumber`
API to purchase a phone number. For more information, see [Request a phone number in AWS End User Messaging SMS](phone-numbers-request.md "phone-numbers-request.md").

###### To create a pool using the AWS CLI

- At the command line, enter the following command:

```
`$` aws pinpoint-sms-voice-v2 create-pool \
`>` --origination-identity `originationIdentity` \
`>` --iso-country-code `XX` \
`>` --message-type `TRANSACTIONAL`
```

In the preceding command, make the following changes:

    + Replace `originationIdentity` with the unique ID or Amazon
     Resource Name (ARN) of the phone number or sender ID that you want to add to the
     pool.


    ###### Tip

    You can find both the ID and ARN of a phone number by using the [describe-phone-numbers](../../../cli/latest/reference/pinpoint-sms-voice-v2/describe-phone-numbers.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/describe-phone-numbers.md") operation. You can find the ID and ARN of a sender ID by
     using the [describe-sender-ids](../../../cli/latest/reference/pinpoint-sms-voice-v2/describe-sender-ids.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/describe-sender-ids.md") operation.
    + Replace `XX` with the ISO-3166 alpha-2 identifier of the
     country for the `originationIdentity`.
    + If you plan to use the pool to send marketing or promotional messages, replace
     `TRANSACTIONAL` with `PROMOTIONAL`. Otherwise, use
     `TRANSACTIONAL`.
