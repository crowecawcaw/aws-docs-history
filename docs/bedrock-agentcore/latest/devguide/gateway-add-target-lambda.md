

# AWS Lambda function targets

Lambda targets allow you to connect your gateway to AWS Lambda functions that implement your tools. This is useful when you want to execute custom code in response to tool invocations.

You create a Lambda function using the AWS Lambda service. In order to create the function, you should do the following:
+ Create a tool schema that defines the tools that your Lambda function can call.
+ Understand the Lambda input format. You can then follow the steps in the [AWS Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/) for **Building with** the language of your choice.

After you create the function, you configure permissions for the gateway to be able to access it.

Review the key considerations and limitations to help you decide whether a Lambda target is applicable to your use case. If it is, you can create the tool schema and the Lambda function and then set up permissions for the gateway to be able to access the target. Select a topic to learn more:

**Topics**
+ [Key considerations and limitations](#gateway-building-lambda-limitations)
+ [Lambda function tool schema](#gateway-lambda-tool-schema)
+ [Lambda function input format](#gateway-building-lambda-input)

## Key considerations and limitations
<a name="gateway-building-lambda-limitations"></a>

When working with Lambda targets, be aware of the following limitations and considerations:
+ Tool name prefixes will need to be manually stripped off from the toolname in your AWS Lambda function. For more information, see [Understand how AgentCore Gateway tools are named](gateway-tool-naming.md).
+ If you are using an existing AWS Lambda function and import it as a tool into the gateway, you will need to change the function code to account for a schema change for event and context objects
+ The Lambda function must return a valid JSON response that can be parsed by the gateway
+ Lambda function timeouts should be configured appropriately to handle the expected processing time of your tools
+ Consider implementing error handling in your Lambda function to provide meaningful error messages to the client

**Important**  
If your target propagates headers or query parameters and your Lambda function uses a strongly typed runtime (such as Java), set `propagatedHeadersEncoding` to `JSON_STRING`. Otherwise, your function fails before your handler runs. For more information, see [Propagated headers and query parameters encoding](#gateway-lambda-propagated-headers-encoding).

## Lambda function tool schema
<a name="gateway-lambda-tool-schema"></a>

This section explains the structure of the tool schema that defines a tool that your Lambda function can return. After you define your tool schema, you can do one of the following:
+ Upload it to an Amazon S3 bucket and refer to the S3 location when you add the target to your gateway.
+ Paste the definition inline when you add the target to your gateway.

Select a topic to learn more about the details of the tool schema or to see examples:

**Topics**
+ [Tool definition](#gateway-lambda-tool-definition)
+ [Top level schema definition for input and output schemas](#gateway-lambda-top-level-schema-definition)
+ [Property schema definition](#gateway-lambda-property-schema-definition)
+ [Example Lambda tool definitions](#gateway-lambda-example)

### Tool definition
<a name="gateway-lambda-tool-definition"></a>

When you add a Lambda function as a gateway target, you provide a [ToolDefinition](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ToolDefinition.html) when providing the target configuration. The structure of the tool definition is as follows:

```json
{
    "name": "string",
    "description": "string",
    "inputSchema": {
        "type": "object",
        "description": "string",
        "properties": {
            "string": SchemaDefinition
        },
        "required": ["string"]
    },
    "outputSchema": {
        "type": "object",
        "description": "string",
        "properties": {
            "string": SchemaDefinition
        },
        "required": ["string"]
    }
}
```

The tool definition contains the following fields:
+  **name** (required) – The name of the tool.
+  **description** (required) – A description of the tool and its purpose and usage.
+  **inputSchema** (required) – A JSON object that defines the structure of the input that the tool accepts.
+  **outputSchema** (optional) – A JSON object that defines the structure of the output that the tool produces.

The `inputSchema` and `outputSchema` fields both map to an object-type [SchemaDefinition](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_SchemaDefinition.html) , described in the following section.

### Top level schema definition for input and output schemas
<a name="gateway-lambda-top-level-schema-definition"></a>

The `inputSchema` and `outputSchema` fields at the top level of the tool definition both map to an object-type [SchemaDefinition](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_SchemaDefinition.html) that contains the following fields:

```json
{
    "type": "object",
    "description": "string",
    "properties": {
        "string": SchemaDefinition
    },
    "required": ["string"]
}
```
+  **type** (required) – Must be `object`.
+  **description** (optional) – A description of the schema and its purpose and usage.
+  **properties** (optional) – A JSON object that defines the properties or arguments of the tool. Each key is a name of a property and maps to a [SchemaDefinition](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_SchemaDefinition.html) object that defines the property.
+  **required** (optional) – An array that enumerates the properties that are required in the `properties` object.

If you include a `properties` field to define arguments for the tool, you provide a schema definition for each argument. The different types of schema definitions are outlined in the next section.

### Property schema definition
<a name="gateway-lambda-property-schema-definition"></a>

Each property in the top level `SchemaDefinition` maps to a [SchemaDefinition](https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_SchemaDefinition.html) object that has slightly different requirements from the top level schema definition. The available fields depend on the `type` for the property. To see the shape of the `SchemaDefinition` for a type, select from the following tabs:

**Example**  

1. The `SchemaDefinition` for a string property has the following structure:

   ```json
   {
       "type": "string",
       "description": "string"
   }
   ```

1. The `SchemaDefinition` for a number property has the following structure:

   ```json
   {
       "type": "number",
       "description": "string"
   }
   ```

1. The `SchemaDefinition` for a integer property has the following structure:

   ```json
   {
       "type": "integer",
       "description": "string"
   }
   ```

1. The `SchemaDefinition` for a boolean property has the following structure:

   ```json
   {
       "type": "boolean",
       "description": "string"
   }
   ```

1. The `SchemaDefinition` for an array property has the following structure:

   ```json
   {
       "type": "array",
       "description": "string",
       "items": SchemaDefinition
   }
   ```

   The value of the `items` field is a `SchemaDefinition` that defines the structure of each item in the array.

1. The `SchemaDefinition` for an object property has the following structure and matches the top level property schema definition.

   ```json
   {
       "type": "object",
       "description": "string",
       "properties": {
           "string": SchemaDefinition
       },
       "required": ["string"]
   }
   ```

If you include another object-type property, you will recursively add another `SchemaDefinition`.

### Example Lambda tool definitions
<a name="gateway-lambda-example"></a>

Select a tab to see example tool definitions that you can include in your Lambda function.

**Example**  

1. The following `get_weather` tool requires a `location` string argument and can be used to return the weather for that location:

   ```json
   {
       "name": "get_weather",
       "description": "Get weather for a location",
       "inputSchema": {
           "type": "object",
           "properties": {
               "location": {
                   "type": "string",
                   "description": "the location e.g. seattle, wa"
               }
           },
           "required": [
               "location"
           ]
       }
   }
   ```

1. The following `get_time` tool requires a `timezone` string argument and can be used to return the time for that timezone:

   ```json
   {
       "name": "get_time",
       "description": "Get time for a timezone",
       "inputSchema": {
           "type": "object",
           "properties": {
               "timezone": {
                   "type": "string"
               }
           },
           "required": [
               "timezone"
           ]
       }
   }
   ```

## Lambda function input format
<a name="gateway-building-lambda-input"></a>

When an Amazon Bedrock AgentCore gateway invokes a Lambda function, it passes an `event` object and a `context` object to the function. The Lambda event handler that you write can access values in these objects.

 **Event object** 

A map of `properties` from the `inputSchema` to their values, as returned by the tool. For example, if your input schema contains the properties `keywords` and `category` , the event object could be the following:

```json
{
  "keywords": "wireless headphones",
  "category": "electronics"
}
```

 **Context object** 

Contains the following metadata:
+ bedrockAgentCoreMessageVersion – The version of the message.
+ bedrockAgentCoreAwsRequestId – The ID of the request made to the Amazon Bedrock AgentCore service.
+ bedrockAgentCoreMcpMessageId – The ID of the message sent to the MCP server.
+ bedrockAgentCoreGatewayId – The ID of the gateway that was invoked.
+ bedrockAgentCoreTargetId – The ID of the gateway target that was invoked.
+ bedrockAgentCoreToolName– The name of the tool that was called. The tool name is in the format `${target_name}` *\_* `${tool_name}`.
+ bedrockAgentCorePropagatedHeaders – The request headers propagated to the target. Present only when the target’s `metadataConfiguration` allowlists request headers and at least one allowlisted header is present on the request. For more information, see [Header propagation with Gateway](gateway-headers.md).
+ bedrockAgentCorePropagatedQueryParameters – The query parameters propagated to the target. Present only when the target’s `metadataConfiguration` allowlists query parameters and at least one allowlisted query parameter is present on the request.

The `propagatedHeadersEncoding` setting of the target determines the format of the propagated fields. For more information, see [Propagated headers and query parameters encoding](#gateway-lambda-propagated-headers-encoding).

The format of the context object is as follows:

```json
{
  "bedrockAgentCoreMessageVersion": "1.0",
  "bedrockAgentCoreAwsRequestId": "string",
  "bedrockAgentCoreMcpMessageId": "string",
  "bedrockAgentCoreGatewayId": "string",
  "bedrockAgentCoreTargetId": "string",
  "bedrockAgentCoreToolName": "string"
}
```

The Lambda function that you write can access the properties of the event and context object. You can use the following boilerplate code to get started:

```python
# Access context properties in your Lambda function
def lambda_handler(event, context):
    # Since the visible tool name includes the target name as a prefix, we can use this delimiter to strip the prefix
    delimiter = "___"

    # Get the tool name from the context
    originalToolName = context.client_context.custom['bedrockAgentCoreToolName']
    toolName = originalToolName[originalToolName.index(delimiter) + len(delimiter):]

    # Get other context properties
    message_version = context.client_context.custom['bedrockAgentCoreMessageVersion']
    aws_request_id = context.client_context.custom['bedrockAgentCoreAwsRequestId']
    mcp_message_id = context.client_context.custom['bedrockAgentCoreMcpMessageId']
    gateway_id = context.client_context.custom['bedrockAgentCoreGatewayId']
    target_id = context.client_context.custom['bedrockAgentCoreTargetId']

    # Process the request based on the tool name
    if tool_name == 'searchProducts':
        # Handle searchProducts tool
        pass
    elif tool_name == 'getProductDetails':
        # Handle getProductDetails tool
        pass
    else:
        # Handle unknown tool
        pass
```

### Propagated headers and query parameters encoding
<a name="gateway-lambda-propagated-headers-encoding"></a>

When a Lambda target propagates request headers or query parameters, the gateway adds them to the context object as `bedrockAgentCorePropagatedHeaders` and `bedrockAgentCorePropagatedQueryParameters`. Use the optional `propagatedHeadersEncoding` field in the Lambda target configuration to control how the gateway encodes these fields:
+  `JSON_NESTED` (default) – Each propagated field is a nested JSON object. This is the behavior when you omit `propagatedHeadersEncoding`.
+  `JSON_STRING` – Each propagated field is a string that contains the serialized JSON object. Every value in the context object is then a string.

For example, with a propagated `x-tenant-id` header, the `bedrockAgentCorePropagatedHeaders` field has the following format with `JSON_NESTED` (default):

```json
{
  "bedrockAgentCorePropagatedHeaders": {"x-tenant-id": "tenant-123"}
}
```

With `JSON_STRING`, the same field has the following format:

```json
{
  "bedrockAgentCorePropagatedHeaders": "{\"x-tenant-id\":\"tenant-123\"}"
}
```

**Important**  
Strongly typed Lambda runtimes, such as the AWS Lambda Java managed runtime, deserialize the client context custom map as `Map<String, String>`. If a propagated field is a nested JSON object, the runtime fails before your handler runs. For example, the Java managed runtime fails with `IllegalStateException: Expected a string but was BEGIN_OBJECT`. If your Lambda function uses a strongly typed runtime and your target propagates headers or query parameters, set `propagatedHeadersEncoding` to `JSON_STRING`. Dynamically typed runtimes, such as Python, can use either encoding.

Set `propagatedHeadersEncoding` in the `lambda` object of the target configuration when you create or update the target. The following example shows a Lambda target configuration that uses `JSON_STRING` encoding:

```json
{
    "name": "my-java-lambda-target",
    "targetConfiguration": {
        "mcp": {
            "lambda": {
                "lambdaArn": "arn:aws:lambda:us-west-2:123456789012:function:my-java-function",
                "toolSchema": {
                    "s3": {
                        "uri": "s3://amzn-s3-demo-bucket/tool-schema.json"
                    }
                },
                "propagatedHeadersEncoding": "JSON_STRING"
            }
        }
    },
    "credentialProviderConfigurations": [{
        "credentialProviderType": "GATEWAY_IAM_ROLE"
    }],
    "metadataConfiguration": {
        "allowedRequestHeaders": ["x-tenant-id"],
        "allowedQueryParameters": ["version"]
    }
}
```

**Note**  
When you update a Lambda target and include the `lambda` configuration, the gateway applies the `propagatedHeadersEncoding` value from the request. If you omit the field, the encoding resets to the default (`JSON_NESTED`). To keep `JSON_STRING`, include it in every update that contains the `lambda` configuration.

With `JSON_STRING`, parse the propagated fields in your function. The following Java example reads the propagated headers:

```java
import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.util.Collections;
import java.util.Map;

public class Handler implements RequestHandler<Map<String, Object>, Map<String, Object>> {
    private static final ObjectMapper MAPPER = new ObjectMapper();

    @Override
    public Map<String, Object> handleRequest(Map<String, Object> event, Context context) {
        Map<String, String> custom = context.getClientContext().getCustom();

        // Propagated fields are JSON strings when propagatedHeadersEncoding is JSON_STRING
        Map<String, String> headers = parseJsonMap(custom.get("bedrockAgentCorePropagatedHeaders"));
        Map<String, String> queryParameters = parseJsonMap(custom.get("bedrockAgentCorePropagatedQueryParameters"));

        String tenantId = headers.get("x-tenant-id");
        // Process the request
        return Map.of("tenantId", tenantId == null ? "" : tenantId);
    }

    private static Map<String, String> parseJsonMap(String json) {
        if (json == null) {
            return Collections.emptyMap();
        }
        try {
            return MAPPER.readValue(json, new TypeReference<Map<String, String>>() {});
        } catch (JsonProcessingException e) {
            // The value is not a JSON object string. Confirm that the target sets propagatedHeadersEncoding to JSON_STRING.
            throw new IllegalArgumentException(
                "Propagated field is not a valid JSON object string. Set propagatedHeadersEncoding to JSON_STRING on the target.", e);
        }
    }
}
```

In Python, the propagated fields are dictionaries with `JSON_NESTED` and strings with `JSON_STRING`. The following Python example uses `json.loads()` to parse the propagated fields when the target uses `JSON_STRING` encoding:

```python
import json


def lambda_handler(event, context):
    custom = context.client_context.custom

    # Propagated fields are JSON strings when propagatedHeadersEncoding is JSON_STRING
    headers = json.loads(custom.get('bedrockAgentCorePropagatedHeaders', '{}'))
    query_parameters = json.loads(custom.get('bedrockAgentCorePropagatedQueryParameters', '{}'))

    tenant_id = headers.get('x-tenant-id', '')
    # Process the request
    return {'tenantId': tenant_id}
```