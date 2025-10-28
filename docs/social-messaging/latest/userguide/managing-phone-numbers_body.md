# Phone number considerations for use with a WABA

When you link a phone number with your WhatsApp Business Account (WABA), you should consider the
following:

- Phone numbers can only be linked to one WABA at a time.
- The phone number can still be used for SMS, MMS, and voice calls.
- Each phone number has a quality rating from Meta.
  You can obtain an SMS-capable phone number through AWS End User Messaging SMS by
  doing the following:

1. Make sure that the [country or region](../../../sms-voice/latest/userguide/phone-numbers-sms-by-country.md "../../../sms-voice/latest/userguide/phone-numbers-sms-by-country.md") for the phone number supports
   two-way SMS.
2. Request the [phone number](../../../sms-voice/latest/userguide/phone-numbers-request.md "../../../sms-voice/latest/userguide/phone-numbers-request.md"). Depending on the country or
   region, you may be required to register the phone number.
3. [Enable two-way SMS messaging](../../../sms-voice/latest/userguide/phone-numbers-two-way-sms.md "../../../sms-voice/latest/userguide/phone-numbers-two-way-sms.md") for the phone number. Once setup is
   complete, your incoming SMS messages are sent to an event destination.
