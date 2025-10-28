**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Message fallback

When sending a message using the Amazon Pinpoint API, three optional parameters can be passed in the
request: `originationNumber`, `registeredKeyword`, and
`senderID`. If Amazon Pinpoint encounters an `originationNumber` error
– for example, an invalid character – and the error is retriable, Amazon Pinpoint uses a
fallback process for choosing a valid number for the request. Fallback checks for a valid
number in the following order. At any point during this process Amazon Pinpoint will choose the first
valid number it finds as the originating number.

1. Origination number. Any other valid origination numbers are checked.
2. Keyword. Registered keywords are scanned and matched against any dedicated number.
3. Sender ID. Any other valid sender IDs are checked.

###### Note

If you send a message with an `originationNumber` that doesn't exist in your
account, there's no fallback process, and an exception message returned instead.

If none of the previous parameters are passed in the request, Amazon Pinpoint looks at your
account and checks for a valid number in this order:

1. Dedicated numbers. Any dedicated numbers associated with your account are
   checked in this order: short code, 10DLC, then long code/toll-free number. Domestic
   numbers are checked before international numbers. If you have both transactional and
   promotional long codes in your account, Amazon Pinpoint chooses a transactional number by
   default.
2. Default sender IDs.
3. Shared routes.

###### Note

Amazon Pinpoint does attempt to deliver messages in countries where an origination identity isn't
required.
