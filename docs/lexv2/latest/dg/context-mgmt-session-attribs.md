

# Setting session attributes for your Lex V2 bot
<a name="context-mgmt-session-attribs"></a>

*Session attributes* contain application-specific information that is passed between a bot and a client application during a session. Amazon Lex V2 passes session attributes to all Lambda functions configured for a bot. If a Lambda function adds or updates session attributes, Amazon Lex V2 passes the new information back to the client application. 

Use session attributes in your Lambda functions to initialize a bot and to customize prompts and response cards. For example:
+ Initialization — In a pizza ordering bot, the client application passes the user's location as a session attribute in the first call to the [RecognizeText](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_RecognizeText.html) or [RecognizeUtterance](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_RecognizeUtterance.html) operation. For example, `"Location": "111 Maple Street"`. The Lambda function uses this information to find the closest pizzeria to place the order.
+ Personalize prompts — Configure prompts and response cards to refer to session attributes. For example, "Hey [FirstName], what toppings would you like?" If you pass the user's first name as a session attribute (`{"FirstName": "Vivian"}`), Amazon Lex substitutes the name for the placeholder. It then sends a personalized prompt to the user, "Hey Vivian, which toppings would you like?"

Session attributes persist for the duration of the session. Amazon Lex V2 stores them in an encrypted data store until the session ends. The client can create session attributes in a request by calling either the [RecognizeText](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_RecognizeText.html) or [RecognizeUtterance](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_runtime_RecognizeUtterance.html) operation with the `sessionAttributes` field set to a value. A Lambda function can create a session attribute in a response. After the client or a Lambda function creates a session attribute, the stored attribute value is used any time that the client application doesn't include `sessionAttribute` field in a request to Amazon Lex V2.

For example, suppose you have two session attributes, `{"x": "1", "y": "2"}`. If the client calls the `RecognizeText` or `RecognizeUtterance` operation without specifying the `sessionAttributes` field, Amazon Lex V2 calls the Lambda function with the stored session attributes (`{"x": 1, "y": 2}`). If the Lambda function doesn't return session attributes, Amazon Lex V2 returns the stored session attributes to the client application.

If either the client application or a Lambda function passes session attributes, Amazon Lex V2 updates the stored session attributes. Passing an existing value, such as ` {"x": 2}`, updates the stored value. If you pass a new set of session attributes, such as `{"z": 3}`, the existing values are removed and only the new value is kept. When an empty map, `{}`, is passed, stored values are erased.

To send session attributes to Amazon Lex V2, you create a string-to-string map of the attributes. The following shows how to map session attributes: 

```
{
   "attributeName": "attributeValue",
   "attributeName": "attributeValue"
}
```

For the `RecognizeText` operation, you insert the map into the body of the request using the `sessionAttributes` field of the `sessionState` structure, as follows:

```
"sessionState": {
    "sessionAttributes": {
        "attributeName": "attributeValue",
        "attributeName": "attributeValue"
    }
}
```

For the `RecognizeUtterance` operation, you base64 encode the map, and then send it as part of the `x-amz-lex-session-state` header.

If you are sending binary or structured data in a session attribute, you must first transform the data to a simple string. For more information, see [Setting complex attributes in your Lex V2 bot](context-mgmt-complex-attributes.md).

## Predefined session attributes
<a name="predefined-session-attributes"></a>

Amazon Lex provides predefined session attributes. These attributes manage how Amazon Lex processes information sent to your bot. The attributes persist for the entire session. All predefined attributes are in the `x-amz-lex:` namespace. 

## Increasing code hook Lambda timeout
<a name="increasing-codehook-lambda-timeout-attributes"></a>

To increase the code hook Lambda timeout value in your bot, which is 30 seconds by default, use the `x-amz-lex:codehook-timeout-ms` session attribute. Set the session attribute value in milliseconds. The maximum timeout is 120 seconds. 

For example, if a user sets "x-amz-lex:codehook-timeout-ms": "90000", the code hook Lambda timeout will be 90 seconds.