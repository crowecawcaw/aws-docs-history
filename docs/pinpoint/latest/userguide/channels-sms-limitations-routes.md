**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Message routes

The route your message uses is dependent on the type set for the message, either
**promotional** or **transactional**. When purchasing
a new number using the Amazon Pinpoint console you will be prompted to choose the route type.

Promotional routes are typically marketing or sales-related messages. Some countries or
regions have quiet time hours when you're not permitted to send promotional messages. A
transactional route is for more time-sensitive messages, such as password resets or one-time
passwords. This can be applied to the number when you're purchasing a new number or can be
passed as an optional parameter in the SendMessages operation of the Amazon Pinpoint API. When sending
a message using that number as the originator, Amazon Pinpoint chooses the applicable promotional or
transactional route.

You pass the route type as an optional parameter using the [SendMessages](../apireference/apps-application-id-messages.md#SendMessages "../apireference/apps-application-id-messages.md#SendMessages")
operation of the Amazon Pinpoint API. In some cases you might use a SenderID as the originator, or you
might have a shared pool of numbers. If you have both transactional and promotional numbers
associated with your account for the destination country, Amazon Pinpoint chooses a transactional
number by default. Delivery receipts and the Delivery dashboard show the route as either
promotional or transactional, based on the chosen number.
