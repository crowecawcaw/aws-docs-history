

# Choosing a 10DLC phone number by area code
<a name="phone-numbers-10dlc-select"></a>

When you request a 10 digit long code (10DLC) phone number, you can search for and choose a specific number instead of receiving a random assignment. You can search by area code or by a pattern within the phone number. You can also request an exact phone number. This feature is available for United States 10DLC phone numbers only.

Phone number selection works in two steps:

1. **Search** – Use the `ListAvailablePhoneNumbers` API or the console to browse available 10DLC numbers filtered by area code or pattern.

1. **Request** – Use the `RequestPhoneNumber` API with the optional `NumberPreference` parameter, or select a number in the console, to request a specific phone number.

## Prerequisites
<a name="phone-numbers-10dlc-select-prereqs"></a>

Before you can search for and choose a 10DLC phone number, you must have the following:
+ An approved 10DLC registered brand. For more information, see [10DLC brand registration form](registrations-10dlc-company.md).
+ An approved 10DLC registered campaign associated with the brand. For more information, see [10DLC campaign registration form](registrations-10dlc-register-campaign.md).

The phone number search returns numbers that are available through the aggregator associated with your 10DLC campaign registration. You do not need to specify an aggregator.

## Search pattern types
<a name="phone-numbers-10dlc-select-search-types"></a>

You can search for available phone numbers using the following pattern types:


| Pattern type | Description | Example | 
| --- | --- | --- | 
| StartsWith | Returns numbers that begin with the specified digits. Use this to search by area code. | Filter \+1510 returns numbers in the 510 area code, such as \+15103921111. | 
| EndsWith | Returns numbers that end with the specified digits. | Filter 1234 returns numbers ending in 1234, such as \+12025551234. | 
| Contains | Returns numbers that contain the specified digits anywhere in the number. | Filter 555 returns numbers containing 555, such as \+15105559876. | 
| ExactMatch | Requests a specific phone number. This type is only valid with the RequestPhoneNumber API, not with ListAvailablePhoneNumbers. | Filter \+15103921234 requests that exact number. | 

## Important considerations
<a name="phone-numbers-10dlc-select-important"></a>
+ Phone number availability is not guaranteed. A number shown in search results can be purchased by another customer before you request it. If this happens, request a different number or search again.
+ Search results are not a reservation. Numbers are not held for you between the search step and the request step.
+ Search results return a maximum of 10 numbers per page. To retrieve additional pages of results, use the `NextToken` parameter.
+ If you do not specify a `NumberPreference` when calling `RequestPhoneNumber`, the existing behavior is unchanged and AWS End User Messaging SMS assigns a phone number automatically.
+ This feature is available for United States 10DLC (`TEN_DLC`) phone numbers only.

## Search for and request a 10DLC phone number
<a name="phone-numbers-10dlc-select-procedures"></a>

You can search for and request a specific 10DLC phone number using either the AWS End User Messaging SMS console or the AWS CLI.

------
#### [ Console ]

You can search for and choose a specific 10DLC phone number during the phone number request process in the AWS End User Messaging SMS console.

**Choose a 10DLC phone number by area code (Console)**

1. Open the AWS End User Messaging SMS console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/).

1. In the navigation pane, under **Configurations**, choose **Phone numbers** and then **Request originator**.

1. On the **Select country** page, choose **United States (US)** from the **Message destination country** dropdown. Choose **Next**.

1. Complete the **Messaging use case** section and choose **Next**.

1. Under **Originator type**, choose the 10DLC number type and associate your registered brand and campaign.

1. (Optional) On the **Number preference** step, search for a specific phone number:

   1. Select a search pattern type: **Starts with**, **Ends with**, or **Contains**.

   1. Enter a pattern. For example, enter **510** to search for numbers in the 510 area code. The console automatically formats your input with the country code prefix.

   1. Choose **Search**. A table displays up to 10 available phone numbers.

   1. Select the phone number you want, then choose **Next**.

   If you skip this step, AWS End User Messaging SMS assigns a phone number automatically.

1. Configure **Resource policy** sharing if needed, then choose **Next**.

1. On **Review and request**, verify your settings and choose **Request**.

------
#### [ AWS CLI ]

Use the AWS CLI to search for available 10DLC phone numbers and then request a specific number.

**Step 1: Search for available numbers**

Use the [list-available-phone-numbers](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/list-available-phone-numbers.html) command to search for available 10DLC phone numbers. The following example searches for numbers in the 510 area code:

```
$ aws pinpoint-sms-voice-v2 list-available-phone-numbers \
    --iso-country-code US \
    --number-type TEN_DLC \
    --registration-id registration-1234567890 \
    --number-preference '[{"PreferenceType": ["StartsWith"], "Filter": ["+1510"]}]'
```

If numbers matching your search criteria are available, the response includes a list of phone numbers in E.164 format:

```
{
    "AvailablePhoneNumbers": [
        "+15103921111",
        "+15103922222",
        "+15103923333",
        "+15103924444",
        "+15103925555"
    ],
    "NextToken": "AAMAJDUwNzE4ZTQwLWJkOTUtNDk4Ny..."
}
```

In the preceding command, make the following changes:
+ Replace `registration-1234567890` with the ID of your approved 10DLC campaign registration.
+ Replace `+1510` with the area code or pattern you want to search for.
+ Replace `StartsWith` with `EndsWith` or `Contains` to change the search pattern type.

If the response includes a `NextToken` value, pass it in a subsequent request to retrieve the next page of results. When `NextToken` is null, there are no more results.

**Step 2: Request a specific number**

After you find a phone number in the search results, use the [request-phone-number](https://docs.aws.amazon.com/cli/latest/reference/pinpoint-sms-voice-v2/request-phone-number.html) command with the `--number-preference` parameter to request that number.

The following example requests an exact phone number:

```
$ aws pinpoint-sms-voice-v2 request-phone-number \
    --iso-country-code US \
    --message-type TRANSACTIONAL \
    --number-type TEN_DLC \
    --number-capabilities SMS \
    --registration-id registration-1234567890 \
    --number-preference '{"PreferenceType": ["ExactMatch"], "Filter": ["+15103921111"]}'
```

You can also request a phone number using a pattern. The following example requests any available number in the 510 area code:

```
$ aws pinpoint-sms-voice-v2 request-phone-number \
    --iso-country-code US \
    --message-type TRANSACTIONAL \
    --number-type TEN_DLC \
    --number-capabilities SMS \
    --registration-id registration-1234567890 \
    --number-preference '{"PreferenceType": ["StartsWith"], "Filter": ["+1510"]}'
```

In the preceding commands, make the following changes:
+ Replace `registration-1234567890` with the ID of your approved 10DLC campaign registration.
+ Replace `TRANSACTIONAL` with `PROMOTIONAL` if you are sending promotional messages.
+ Replace `SMS` with the capabilities you need. You can specify `SMS`, `MMS`, and `VOICE`.
+ Replace the phone number or pattern in `Filter` with your preferred value.

If the requested number is available, the response is the same as a standard `RequestPhoneNumber` response, including the `PhoneNumberId`, `PhoneNumber`, and `Status` fields. If the exact number is no longer available, the request returns an error. Search again to find a different available number.

------