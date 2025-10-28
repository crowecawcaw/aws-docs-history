# SetSubscriptionAttributes

delivery policy JSON format

If you send a request to the `SetSubscriptionAttributes` action and set the
`AttributeName` parameter to a value of `DeliveryPolicy`, the
value of the `AttributeValue` parameter must be a valid JSON object. For
example, the following example sets the delivery policy to 5 total retries.

```
http://sns.us-east-2.amazonaws.com/
?Action=SetSubscriptionAttributes
&SubscriptionArn=arn%3Aaws%3Asns%3Aus-east-2%3A123456789012%3AMy-Topic%3A80289ba6-0fd4-4079-afb4-ce8c8260f0ca
&AttributeName=DeliveryPolicy
&AttributeValue={"healthyRetryPolicy":{"numRetries":5}}
...
```

Use the following JSON format for the value of the `AttributeValue`
parameter.

```
{
    "healthyRetryPolicy" : {
        "minDelayTarget" :  int,
        "maxDelayTarget" : int,
        "numRetries" : int,
        "numMaxDelayRetries" : int,
        "backoffFunction" : "linear|arithmetic|geometric|exponential"
    },
    "throttlePolicy" : {
        "maxReceivesPerSecond" : int
    },
    "requestPolicy" : {
        "headerContentType" : "text/plain | application/json | application/xml"
    }
}
```

For more information about the `SetSubscriptionAttribute` action, go to
[SetSubscriptionAttributes](../api/API_SetSubscriptionAttributes.md "../api/API_SetSubscriptionAttributes.md") in the _Amazon Simple Notification Service API Reference_. For
more information on the supported HTTP content-type headers, see [Creating an HTTP/S delivery policy](sns-message-delivery-retries.md#creating-delivery-policy "sns-message-delivery-retries.md#creating-delivery-policy").
