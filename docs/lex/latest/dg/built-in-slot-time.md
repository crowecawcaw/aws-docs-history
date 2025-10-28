End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# AMAZON.TIME

Converts words that represent times into time values. Includes
resolutions for ambiguous times. When a user enters an ambiguous
time, Amazon Lex uses the `slotDetails` attribute of a
Lambda event to pass resolutions for the ambiguous times to your
Lambda function. For example, if your bot prompts the user for a
delivery time, the user can respond by saying "10 o'clock." This
time is ambiguous. It means either 10:00 AM or 10:00 PM. In this
case, the value in the `slots` map is
`null`, and the `slotDetails` entity
contains the two possible resolutions of the time. Amazon Lex inputs
the following into the Lambda function:

```
"slots": {
   "deliveryTime": null
},
"slotDetails": {
   "deliveryTime": {
      "resolutions": [
         {
            "value": "10:00"
         },
         {
            "value": "22:00"
         }
      ]
   }
}
```

When the user responds with an unambiguous time, Amazon Lex sends
the time to your Lambda function in the `slots`
attribute of the Lambda event and the `slotDetails`
attribute is empty. For example, if your user responds to the
prompt for a delivery time with "10:00 PM," Amazon Lex inputs the
following into the Lambda function:

```
"slots": {
   "deliveryTime": "22:00"
}
```

For more information about the data sent from Amazon Lex to a Lambda
function, see [Input Event
Format](lambda-input-response-format.md#using-lambda-input-event-format "lambda-input-response-format.md#using-lambda-input-event-format").
