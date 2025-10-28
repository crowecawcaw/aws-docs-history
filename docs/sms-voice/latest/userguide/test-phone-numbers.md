# Simulator phone numbers in AWS End User Messaging SMS

You can use the SMS simulator that is included with AWS End User Messaging SMS to send text messages and receive
realistic event records. The SMS simulator is also useful for:

- Viewing actual SMS event records.
- Testing applications that use AWS End User Messaging SMS to send SMS messages.
  When using the SMS simulator, messages originate from a origination simulator phone number, and
  messages are sent to destination simulator phone numbers that you request. The simulator phone numbers
  are designed to stay within AWS End User Messaging SMS, so that messages are not sent over the carrier network. Origination
  and destination simulator phone numbers work with SMS and MMS.

###### Topics

- [Origination simulator phone numbers](#test-phone-numbers-origination "#test-phone-numbers-origination")
- [Destination simulator phone numbers](#test-phone-numbers-destination "#test-phone-numbers-destination")

## Origination simulator phone numbers

You can request a simulator phone number to use as your origination identity to send
test SMS and MMS messages. The simulator phone number will have a country code from the
country that you choose. When you use a simulator phone number as the origination identity you
can only send messages to the destination simulator phone number from the same country.
If you try to send to a different country the message will fail. For example, if you use
a simulator phone number from the United States and try to send a message to United
Kingdoms success simulator phone number an error is returned.

###### Note

AWS End User Messaging SMS currently supports origination simulator phone numbers in
the United States.

You can request an origination simulator phone number through the SMS simulator in the
AWS End User Messaging SMS console or with the AWS CLI. To request an origination simulator phone number in the
AWS CLI follow the directions in [Request a phone number (AWS CLI)](phone-numbers-request.md#request-cli "phone-numbers-request.md#request-cli") tab and use `SIMULATOR` for the number
type.

###### Request an origination simulator phone number

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. Choose **Shortcuts** and then **Test SMS sending with SMS simulator**.
3. Under **Originator** choose **Phone number** and then choose the **request a simulator number** link.
4. In the **Request simulator number** window, for **Country** choose a country from the drop down list. Choose **Request number**.

## Destination simulator phone numbers

Destination simulator phone numbers are available in several countries and regions.
For each country and region, there are phone numbers that generate message success
events, and numbers that generate message failure events. The following table contains
SMS/MMS simulator phone numbers for all of the countries and regions in which the
simulator is available.

| Country        | Event type | Phone number    |
| -------------- | ---------- | --------------- |
| Australia      | Success    | +61455944038    |
| Australia      | Failure    | +61455944039    |
| Austria        | Success    | +43676800442031 |
| Austria        | Failure    | +43676800442032 |
| Belgium        | Success    | +32460213922    |
| Belgium        | Failure    | +32460213923    |
| Chile          | Success    | +56229140630    |
| Chile          | Failure    | +56229140631    |
| Czech Republic | Success    | +420790542286   |
| Czech Republic | Failure    | +420790542287   |
| Denmark        | Success    | +4525919410     |
| Denmark        | Failure    | +4525919215     |
| Estonia        | Success    | +37282720792    |
| Estonia        | Failure    | +37282720793    |
| Finland        | Success    | +3584573979110  |
| Finland        | Failure    | +3584573979111  |
| France         | Success    | +33755512501    |
| France         | Failure    | +33755512502    |
| Hong Kong      | Success    | +85257048426    |
| Hong Kong      | Failure    | +85257048854    |
| Hungary        | Success    | +36707178770    |
| Hungary        | Failure    | +36707178772    |
| Italy          | Success    | +394390009172   |
| Italy          | Failure    | +394390009174   |
| Jersey         | Success    | +447937404990   |
| Jersey         | Failure    | +447937404992   |
| Luxembourg     | Success    | +352691385880   |
| Luxembourg     | Failure    | +352691385882   |
| Netherlands    | Success    | +3197008100148  |
| Netherlands    | Failure    | +3197008100150  |
| Norway         | Success    | +4759449384     |
| Norway         | Failure    | +4759449387     |
| Poland         | Success    | +48732141440    |
| Poland         | Failure    | +48732141442    |
| Portugal       | Success    | +351927946948   |
| Portugal       | Failure    | +351927946950   |
| Romania        | Success    | +40783900330    |
| Romania        | Failure    | +40783900332    |
| Spain          | Success    | +34683783440    |
| Spain          | Failure    | +34683783442    |
| Sweden         | Success    | +46790645100    |
| Sweden         | Failure    | +46790645102    |
| Switzerland    | Success    | +41798075872    |
| Switzerland    | Failure    | +41798075874    |
| Taiwan         | Success    | +886903444630   |
| Taiwan         | Failure    | +886903444632   |
| United Kingdom | Success    | +447860019066   |
| United Kingdom | Failure    | +447860019067   |
| United States  | Success    | +14254147755    |
| United States  | Failure    | +14254147167    |
