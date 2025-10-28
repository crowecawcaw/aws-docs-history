# Sample request with session attributes

The following example shows how to invoke the AMAZON.BedrockAgentIntent and demonstrates the session and request attributes that are populated in the response. These attributes contain the Bedrock Agent's response data and can be used to access the agent's output, Amazon Bedrock Knowledge Base sources, and action group invocation details.

```
{
    "sessionId": "user-session-123",
    "messages": [{
        "content": "Your order #12345 is currently being processed and will ship within 2-3 business days. You will receive a tracking number via email once it ships.",
        "contentType": "PlainText"
    }],
    "sessionState": {
        "sessionAttributes": {
            "x-amz-lex:bedrock-agent-search-response": "Your order #12345 is currently being processed and will ship within 2-3 business days. You will receive a tracking number via email once it ships.",
            "x-amz-lex:bedrock-knowledge-base-search-response-source": "[{\"title\": \"Order Processing Guide\", \"uri\": \"s3://knowledge-base/orders/processing.pdf\", \"excerpt\": \"Standard orders typically ship within 2-3 business days...\"}]",
            "x-amz-lex:bedrock-agent-action-group-invocation-input": "{\"actionGroupName\": \"OrderLookup\", \"function\": \"getOrderStatus\", \"parameters\": {\"orderId\": \"12345\", \"customerId\": \"67890\"}}",
            "x-amz-lex:bedrock-agent-knowledge-base-lookup-input": "{\"knowledgeBaseId\": \"KB123456\", \"query\": \"order status processing time\", \"numberOfResults\": 3}"
        },
        "intent": {
            "name": "BedrockAgentIntent",
            "slots": {},
            "state": "Fulfilled",
            "confirmationState": "None"
        },
        "dialogAction": {
            "type": "ElicitIntent"
        }
    },
    "interpretations": [{
        "intent": {
            "name": "FallbackIntent",
            "slots": {}
        },
        "interpretationSource": "Lex"
    }],
    "requestAttributes": {
        "x-amz-lex:channels:platform": "Web",
        "x-amz-lex:accept-content-types": "PlainText",
        "x-amz-lex:bedrock-agent-search-response": "Your order #12345 is currently being processed and will ship within 2-3 business days. You will receive a tracking number via email once it ships.",
        "x-amz-lex:bedrock-knowledge-base-search-response-source": "[{\"title\": \"Order Processing Guide\", \"uri\": \"s3://knowledge-base/orders/processing.pdf\", \"excerpt\": \"Standard orders typically ship within 2-3 business days...\"}]",
        "x-amz-lex:bedrock-agent-action-group-invocation-input": "{\"actionGroupName\": \"OrderLookup\", \"function\": \"getOrderStatus\", \"parameters\": {\"orderId\": \"12345\", \"customerId\": \"67890\"}}",
        "x-amz-lex:bedrock-agent-knowledge-base-lookup-input": "{\"knowledgeBaseId\": \"KB123456\", \"query\": \"order status processing time\", \"numberOfResults\": 3}"
    }
}
```

In this example, the session attributes show how the BedrockAgentIntent populates response data including the agent's answer, Amazon Bedrock Knowledge Base sources used, action group invocations, and Amazon Bedrock Knowledge Base lookup details that were used to generate the response.
