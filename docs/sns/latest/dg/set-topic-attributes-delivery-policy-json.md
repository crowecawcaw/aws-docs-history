# SetTopicAttributes delivery

policy JSON format

If you send a request to the `SetTopicAttributes` action and set the
`AttributeName` parameter to a value of `DeliveryPolicy`, the
value of the `AttributeValue` parameter must be a valid JSON object. For
example, the following example sets the delivery policy to 5 total retries.

```
http://sns.us-east-2.amazonaws.com/
?Action=SetTopicAttributes
&TopicArn=arn%3Aaws%3Asns%3Aus-east-2%3A123456789012%3AMy-Topic
&AttributeName=DeliveryPolicy
&AttributeValue={"http":{"defaultHealthyRetryPolicy":{"numRetries":5}}}
...
```

Use the following JSON format for the value of the `AttributeValue`
parameter.

```
{
    "http" : {
        "defaultHealthyRetryPolicy" : {
            "minDelayTarget":  int,
            "maxDelayTarget": int,
            "numRetries": int,
            "numMaxDelayRetries": int,
            "backoffFunction": "linear|arithmetic|geometric|exponential"
        },
        "disableSubscriptionOverrides" : Boolean,
        "defaultThrottlePolicy" : {
            "maxReceivesPerSecond" : int
        },
        "defaultRequestPolicy" : {
            "headerContentType" : "text/plain | application/json | application/xml"
        }
    }
}
```

For more information about the `SetTopicAttribute` action, go to [SetTopicAttributes](../api/API_SetTopicAttributes.md "../api/API_SetTopicAttributes.md") in the
_Amazon Simple Notification Service API Reference_. For more information on the supported HTTP
content-type headers, see [Creating an HTTP/S delivery policy](sns-message-delivery-retries.md#creating-delivery-policy "sns-message-delivery-retries.md#creating-delivery-policy").
