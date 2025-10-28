# Request a phone number in AWS End User Messaging SMS

Using the AWS End User Messaging SMS console, we’ll recommend one of the below origination identities depending on
your use-case. Recommendations are based on your input criteria including if you require SMS, MMS,
and/or voice capabilities, a two-way number, and estimate monthly messages.

###### Note

Depending on the country, the following phone number types have to be requested in the
Support Center Console.

- **Short codes** – [Requesting dedicated short codes](phone-numbers-request-short-code.md "phone-numbers-request-short-code.md").
- **Long codes** – [Requesting dedicated long codes](phone-numbers-request-long-code.md "phone-numbers-request-long-code.md").

###### Note

You must use a **Resource policy** to share the phone number with Amazon Pinpoint or
Amazon SNS even if you are using the same AWS account.

You can use either the AWS End User Messaging SMS console or AWS CLI to request a new phone number.

Request a phone number (Console)

###### Important

To request a new phone number for the United States through the AWS End User Messaging SMS console
follow the directions in the [Request a phone number for the United
States (Console)](#request-us "#request-us") tab.

To request a phone number using the AWS End User Messaging SMS console, follow these steps:

###### Request a phone number (Console)

1.  Open the AWS End User Messaging SMS console at
    [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2.  In the navigation pane, under **Configurations**, choose
    **Phone numbers** and then **Request originator**.
3.  On the **Select country** page you must choose the **Message
    destination country** from the dropdown that messages will be sent to. Choose
    **Next**.
4.  On the **Messaging use case** section, enter the following:
    - Under **Number capabilities**, choose any combination of available
      capabilities:

    ###### Important

    Capabilities for SMS, MMS, and Voice can't be changed after the phone number has been
    purchased.

        + **Text messages (SMS)** Choose this if you need SMS
         capabilities.
        + **Text and media messages (SMS, MMS)** – Choose this if you
         need SMS and/or MMS capabilities.


        ###### Note

        MMS capabilities are only available in certain countries and are only supported on
         certain origination types. **Text and media messages (SMS, MMS)** is
         only present if MMS is supported in the **Message destination
         country**. For more information, see [Supported countries and regions for MMS messaging in AWS End User Messaging SMS](phone-numbers-mms-by-country.md "phone-numbers-mms-by-country.md")
         and [Choosing an origination identity](phone-number-types.md "phone-number-types.md").
        + **Text to audio messages (Voice)** – Choose this if you need
         voice capabilities.

    - Under **Estimated monthly message volume – optional**, choose
      the estimated number of SMS messages you will send each month.
    - For **Company headquarters - optional**, choose either of the
      following:
      - **Local** – Choose this if your company's headquarters is in
        the same country as your customers who will revive SMS messages. For example, you would
        choose this option if your headquarters is in the United States and your users who will
        receive messages are also in the United States.
      - **International** – Choose this if your company's
        headquarters is not in the same country as your customers who will revive SMS
        messages.

    - For **Two-way messaging**, choose **Yes** if you
      require two-way messaging.

5.  Choose **Next**.
6.  Under **Select originator type**, choose either the recommend phone
    number type or one of the available number types. The available options are based on the use
    case information you filled out in the previous steps.
    - If you choose 10DLC and already have a registered campaign you can choose the campaign
      from the **Associate to registered campaign** to add the 10DLC phone number
      to the 10DLC campaign.
    - If the number type you want isn't available you can choose **Previous**
      to go back and modify your use case. Also check the [Supported countries and regions for SMS
      messaging with AWS End User Messaging SMS](phone-numbers-sms-by-country.md "phone-numbers-sms-by-country.md") to
      make sure the originator type you want is supported in the destination country.
    - If you want to request a short code or long code you may need to open a case with Support. For
      more information, see [Requesting dedicated short codes](phone-numbers-request-short-code.md "phone-numbers-request-short-code.md") and [Requesting dedicated long codes](phone-numbers-request-long-code.md "phone-numbers-request-long-code.md").

7.  Use **Resource policy** to share your phone number other AWS accounts or AWS services. To share the phone number at a later time, see [Sharing a phone number, pool, opt-out list, or sender ID](shared-resources.md#sharing-share "shared-resources.md#sharing-share"). For more information on
    **Resource policy**, see [Working with shared resources in AWS End User Messaging SMS](shared-resources.md "shared-resources.md").

###### Note

You must use a **Resource policy** to share the phone number with Amazon Pinpoint or
Amazon SNS even if you are using the same AWS account.

    1. Choose **Pinpoint campaign orchestration(Amazon Pinpoint)** to share the pool
     with Amazon Pinpoint
    2. Choose **Simple notification Service (Amazon SNS)** to share the pool with
     Amazon SNS

8. Choose **Next**.
9. On **Review and request** you can verify and edit your request before submitting it. Choose **Request**.
10. A **Registration Required** window might appear depending on the type
    of phone number you requested. Your phone number or sender ID is associated with this
    registration and can't send messages until your registration has been approved. For more
    information about registrations requirements see [Origination identity registration in AWS End User Messaging SMS](registrations.md "registrations.md").
    1. For **Registration form name** enter a friendly name.
    2. Choose **Begin registration** to finish registering the phone
       number or **Register later**.

    ###### Important

    Your phone number or sender ID can't send messages until your registration has been
    approved.

    You are still billed the recurring monthly lease fee for the phone number regardless of
    registration status. For more information about registrations requirements see [Origination identity registration in AWS End User Messaging SMS](registrations.md "registrations.md").

Request a phone number for the United States (Console)

###### Important

Follow these directions to request a new phone number for the United States through the
AWS End User Messaging SMS console.

Before requesting a 10DLC phone number you must have an approved 10DLC registered brand
and 10DLC registered campaign to associate with the 10DLC phone number. For more information
on registering a 10DLC registered brand and 10DLC registered campaign, see [10DLC brand registration form](registrations-10dlc-company.md "registrations-10dlc-company.md") and
[10DLC campaign registration form](registrations-10dlc-register-campaign.md "registrations-10dlc-register-campaign.md").

The **Messaging capabilities** (SMS, MMS, or VOICE) are specified in the 10DLC registered campaign and applied to your 10DLC phone number request.

###### Request a phone number for the United States (Console)

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under **Configurations**, choose
   **Phone numbers** and then **Request originator**.
3. On the **Select country** page you must choose the **United States (US)** from the **Message
   destination country** dropdown. Choose
   **Next**.
4. On the **Messaging use case** section, enter the following:
   - Under **Estimated monthly message volume – optional**, choose
     the estimated number of SMS messages you will send each month.
   - For **Company headquarters - optional**, choose either of the
     following:
     - **Local** – Choose this if your company's headquarters is in
       the same country as your customers who will revive SMS messages. For example, you would
       choose this option if your headquarters is in the United States and your users who will
       receive messages are also in the United States.
     - **International** – Choose this if your company's
       headquarters is not in the same country as your customers who will revive SMS
       messages.

   - For **Two-way messaging**, choose **Yes** if you
     require two-way messaging.

5. Choose **Next**.
6. Under **Originator type**, choose either the recommend phone
   number type or one of the available number types. The available options are based on the use
   case information you filled out in the previous steps.
   - For a 10DLC phone number you have to choose the registered brand and registered
     campaign to associate with the 10DLC phone number request.
     - Use **Associate to registered brand** to choose a brand.
     - Use **Associate to registered campaign** to choose a campaign.

   - If you want to request a short code or long code you need to open a case with Support.
     For more information, see [Requesting dedicated short codes](phone-numbers-request-short-code.md "phone-numbers-request-short-code.md") and [Requesting dedicated long codes](phone-numbers-request-long-code.md "phone-numbers-request-long-code.md").

7. Use **Resource policy** to share your resources with other AWS accounts or AWS services. To share the phone number at a later time, see [Sharing a phone number, pool, opt-out list, or sender ID](shared-resources.md#sharing-share "shared-resources.md#sharing-share"). For more information on
   **Resource policy**, see [Working with shared resources in AWS End User Messaging SMS](shared-resources.md "shared-resources.md").

###### Note

You must use a **Resource policy** to share the phone number with Amazon Pinpoint or
Amazon SNS even if you are using the same AWS account.

    1. Choose **Pinpoint campaign orchestration(Amazon Pinpoint)** to share the pool
     with Amazon Pinpoint
    2. Choose **Simple notification Service (Amazon SNS)** to share the pool with
     Amazon SNS

8. Choose **Next**.
9. On **Review and request** you can verify and edit your request before
   submitting it. Choose **Request**.
10. A **Registration Required** window might appear depending on the type
    of phone number you requested. Your phone number or sender ID is associated with this
    registration and can't send messages until your registration has been approved. For more
    information about registrations requirements see [Origination identity registration in AWS End User Messaging SMS](registrations.md "registrations.md").
    1. For **Registration form name** enter a friendly name.
    2. Choose **Begin registration** to finish registering the phone number
       or **Register later**.

    ###### Important

    Your phone number or sender ID can't send messages until your registration has been
    approved.

    You are still billed the recurring monthly lease fee for the phone number regardless
    of registration status. For more information about registrations requirements see [Origination identity registration in AWS End User Messaging SMS](registrations.md "registrations.md").

Request a phone number (AWS CLI)You can use the [request-phone-number](../../../cli/latest/reference/pinpoint-sms-voice-v2/request-phone-number.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/request-phone-number.md") command to add new phone numbers to your account. Phone
number availability and supported features vary by country.

###### Important

You might need to register the phone number or sender ID after you complete the request.
You are still billed the recurring monthly lease fee for the phone number regardless of
registration status. For more information about registrations requirements see [Origination identity registration in AWS End User Messaging SMS](registrations.md "registrations.md").

MMS capabilities are only available in some countries. For more information on supported
countries for SMS and MMS, see [Supported countries and regions for SMS
messaging with AWS End User Messaging SMS](phone-numbers-sms-by-country.md "phone-numbers-sms-by-country.md") and [Supported countries and regions for MMS messaging in AWS End User Messaging SMS](phone-numbers-mms-by-country.md "phone-numbers-mms-by-country.md").

###### To request a phone number

- At the command line, enter the following command:

```
`$` aws pinpoint-sms-voice-v2 request-phone-number \
`>` --iso-country-code `XX` \
`>` --message-type `TRANSACTIONAL` \
`>` --number-capabilities `VOICE` \
`>` --number-type `LONG_CODE` \
`>` --pool-id `poolId` \
`>` --deletion-protection-enabled \
`>` --opt-out-list-name `optOutListName` \
`>` --registration-id `CO123EX`
```

In the preceding command, make the following changes:

    + Replace `XX` with the two-letter ISO-3166
     alpha-2 code for the country of the phone number (such as
     `CA` for Canada).
    + If you want to use the phone number to send promotional or
     marketing-related content, replace
     `TRANSACTIONAL` with
     `PROMOTIONAL`. Otherwise, use
     `TRANSACTIONAL`.
    + If you want to request a phone number for sending SMS messages, replace
     `VOICE` with `SMS`. You can request a phone number
     with SMS, MMS, and voice message capabilities by specifying `SMS MMS
     VOICE`.
    + Replace `LONG_CODE` with the type of phone number you want to
     request. Acceptable values are `LONG_CODE`, `TOLL_FREE`,
     `TEN_DLC`, or `SIMULATOR`.


    When you request a `SIMULATOR` phone number, you must set
     `message-type` as `TRANSACTIONAL`.
    + Replace `poolId` with the ID or Amazon
     Resource Name (ARN) of the pool that you want to add the phone number
     to. This parameter is optional. If you don't want to add the phone
     number to a pool, omit this parameter.
    + If you want to enable deletion protection for this phone number, add the
     `--deletion-protection-enabled` parameter. Deletion protection is disabled by
     default. If deletion protection is enabled, you can't delete the phone number using the
     [ReleasePhoneNumber](../../../pinpoint/latest/apireference_smsvoicev2/API_ReleasePhoneNumber.md "../../../pinpoint/latest/apireference_smsvoicev2/API_ReleasePhoneNumber.md") API, unless you update the configuration of the phone number
     to disable this feature.
    + Replace `optOutListName` with the name or ARN
     of the opt-out list that you want to associate with the phone number.
     This parameter is optional. If you don't want to associate the phone
     number with an opt-out list, omit this parameter.
    + If you're requesting a phone number to use with a 10DLC campaign,
     replace `CO123EX` with the ID of the 10DLC
     campaign that you want to use.


    ###### Note

    If you plan to use a 10DLC phone number, you must first register
     your company and campaign. Currently, the only way to complete these
     registration processes is to use the AWS End User Messaging SMS console. For more
     information about 10DLC registration, see [United States 10DLC registration](registrations-10dlc.md "registrations-10dlc.md").

If the number is successfully added to your account, you see output similar to the
following:

```
{
    "PhoneNumberArn": "arn:aws:sms-voice:us-east-1:111122223333:phone-number/phone-615790209ea34aea8da9b729fexample",
    "PhoneNumberId": "phone-615790209ea34aea8da9b729fexample",
    "PhoneNumber": "+12045550123",
    "Status": "PENDING",
    "IsoCountryCode": "CA",
    "MessageType": "TRANSACTIONAL",
    "NumberCapabilities": [
        "SMS"
    ],
    "NumberType": "LONG_CODE",
    "MonthlyLeasingPrice": "1.00",
    "TwoWayEnabled": false,
    "SelfManagedOptOutsEnabled": false,
    "OptOutListName": "Default",
    "DeletionProtectionEnabled": false,
    "CreatedTimestamp": 1645568542.0
}
```

###### Note

When you first purchase a phone number, the value of the `Status`
attribute is `PENDING`. When the phone number is ready to use, the value
of `Status` changes to `ACTIVE`.

If a phone number that meets the parameters you specified isn't available, the request
fails with an error.

###### Topics

- [Requesting short codes](phone-numbers-request-short-code.md "phone-numbers-request-short-code.md")
- [Requesting long codes](phone-numbers-request-long-code.md "phone-numbers-request-long-code.md")
