# Performance optimization

To optimize the performance of your Gateway implementations, consider the following
best practices:

**Minimize tool latency**

The overall latency of your gateway is largely determined by the latency of the
underlying tools. To minimize latency:

- Use Lambda functions in the same region as your gateway
- Optimize your Lambda functions for fast cold starts
- Use provisioned concurrency for Lambda functions that require low latency
- Ensure that REST APIs have low latency and high availability

**Use efficient tool schemas**

Well-designed tool schemas can improve the performance of your gateway:

- Keep schemas as simple as possible
- Use appropriate data types for parameters
- Include clear descriptions for parameters to help agents use the tools
  correctly
- Use required fields to ensure that agents provide necessary parameters

**Enable semantic search**

Semantic search helps agents find the right tools for their tasks, improving the
overall performance of your agent-gateway interactions. Enable semantic search when
creating your gateway:

```
from bedrock_agentcore_starter_toolkit.operations.gateway.client import GatewayClient

# Initialize the Gateway client
gateway_client = GatewayClient(region_name="us-west-2")

# Create a gateway with semantic search enabled
gateway = gateway_client.create_gateway(
    name="semantic-search-gateway",
    description="A gateway with semantic search enabled",
    protocol_configuration={
        "mcp": {
            "search_type": "SEMANTIC"
        }
    }
)
```

**Monitor and optimize**

Use the observability features described in the previous section to monitor the
performance of your gateway and identify opportunities for optimization:

- Set up CloudWatch alarms for key metrics
- Analyze logs to identify patterns and issues
- Regularly review performance metrics and make adjustments as needed
