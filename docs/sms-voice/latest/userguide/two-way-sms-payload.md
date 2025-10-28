# Example of a two-way SMS message payload for Amazon SNS

topics

When your number receives an SMS message, AWS End User Messaging SMS sends a JSON payload to an Amazon SNS topic
that you designate. The JSON payload contains the message and related data, as in the
following example:

```
{
  "originationNumber":"+14255550182",
  "destinationNumber":"+12125550101",
  "messageKeyword":"JOIN",
  "messageBody":"EXAMPLE",
  "inboundMessageId":"cae173d2-66b9-564c-8309-21f858e9fb84",
  "previousPublishedMessageId":"wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
}
```

The incoming message payload contains the following information:

| Property                     | Description                                                                                            |
| ---------------------------- | ------------------------------------------------------------------------------------------------------ |
| `originationNumber`          | The phone number that sent the incoming message to you (in other words, your customer's phone number). |
| `destinationNumber`          | The phone number that the customer sent the message to (your dedicated phone number).                  |
| `messageKeyword`             | The registered keyword that's associated with your dedicated phone number.                             |
| `messageBody`                | The message that the customer sent to you.                                                             |
| `inboundMessageId`           | The unique identifier for the incoming message.                                                        |
| `previousPublishedMessageId` | The unique identifier of the message that the customer is responding to.                               |
