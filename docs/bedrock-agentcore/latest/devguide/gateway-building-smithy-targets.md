# Smithy model targets

Smithy is a language for defining services and software development kits (SDKs). Smithy models provide a more structured approach to defining APIs compared to OpenAPI, and are particularly useful for connecting to AWS services, such as AgentCore Gateway.

Smithy model targets connect your AgentCore gateway to services that are defined using Smithy API models. When you invoke a Smithy model gateway target, the gateway translates incoming MCP requests into API calls that are sent to these services. The gateway also handles the response formatting.

Review the key considerations and limitations, including feature support, to help you decide whether a Smithy target is applicable to your use case. If it is, you can create a schema that follows the specifications and then set up permissions for the gateway to be able to access the target. Select a topic to learn more:

###### Topics

- [Key considerations and limitations](#gateway-building-smithy-considerations "#gateway-building-smithy-considerations")
- [Smithy model specification](#gateway-smithy-models "#gateway-smithy-models")

## Key considerations and limitations

When using Smithy models with AgentCore Gateway, be aware of the following limitations:

- Maximum model size: 10MB
- Only JSON protocol bindings are fully supported
- Only RestJson protocol is supported
- Complex endpoint creation rule sets are not supported
- Only simple URL parameters like {region} are supported

In considering using Smithy models with AgentCore Gateway, review the following feature support table.

### Smithy feature support for AgentCore Gateway

The following table outlines the Smithy features that are supported and unsupported by Gateway:

| Smithy feature support                                                                                                                                                                    | Supported Features                                                                                                                                                          | Unsupported Features |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| **Service Definitions**<br>• Service structure definitions based on Smithy specifications<br>• Operation definitions with input/output shapes<br>• Resource definitions<br>• Trait shapes | **Endpoint Rules**<br>• Endpoint creation rule sets<br>• Runtime endpoint determination based on conditions<br>• Complex URL parameters beyond simple {region} substitution |
| **Protocol Support**<br>• RestJson protocol<br>• Standard HTTP request/response patterns                                                                                                  | **Protocol Support**<br>• RestXml protocol<br>• JsonRpc protocol<br>• AwsQuery protocol<br>• Ec2Query protocol<br>• Custom protocols                                        |
| **Data Types**<br>• Primitive types (string, integer, boolean, float, double)<br>• Complex types (structures, lists, maps)<br>• Timestamp handling<br>• Blob data types                   | **Authentication**<br>• Multiple egress authentication types for specific APIs<br>• Complex authentication schemes requiring runtime decisions                              |
| **HTTP Bindings**<br>• Basic HTTP method bindings<br>• Simple path parameter bindings<br>• Query parameter bindings<br>• Header bindings for simple cases                                 | **Operations**<br>• Streaming operations<br>• Operations requiring custom protocol implementations                                                                          |

## Smithy model specification

AgentCore Gateway provides built-in Smithy models for common AWS services. To see Smithy models for AWS services, see the [AWS API Models repository](https://github.com/aws/api-models-aws "https://github.com/aws/api-models-aws").

###### Note

AgentCore Gateway doesn't support custom Smithy models for non-AWS services.

After you define your Smithy model, you can do one of the following:

- Upload it to an Amazon S3 bucket and refer to the S3 location when you add the target to your gateway.
- Paste the definition inline when you add the target to your gateway.

Expand a section to see examples of supported and unsupported Smithy model specifications:

The following example shows a valid Smithy model specification for a weather service:

```
namespace example.weather

use aws.protocols#restJson1
use smithy.framework#ValidationException

/// Weather service for retrieving weather information
@restJson1
service WeatherService {
    version: "1.0.0",
    operations: [GetCurrentWeather]
}

/// Get current weather for a location
@http(method: "GET", uri: "/weather")
operation GetCurrentWeather {
    input: GetCurrentWeatherInput,
    output: GetCurrentWeatherOutput,
    errors: [ValidationException]
}

structure GetCurrentWeatherInput {
    /// City name or coordinates
    @required
    @httpQuery("location")
    location: String,

    /// Units of measurement (metric or imperial)
    @httpQuery("units")
    units: Units = metric
}

structure GetCurrentWeatherOutput {
    /// Location name
    location: String,

    /// Current temperature
    temperature: Float,

    /// Weather conditions description
    conditions: String,

    /// Humidity percentage
    humidity: Float
}

enum Units {
    metric
    imperial
}
```

The following example shows an invalid endpoint rules configuration using Smithy:

```
@endpointRuleSet({
  "rules": [
    {
      "conditions": [{"fn": "booleanEquals", "argv": [{"ref": "UseFIPS"}, true]}],
      "endpoint": {"url": "https://weather-fips.{Region}.example.com"}
    },
    {
      "endpoint": {"url": "https://weather.{Region}.example.com"}
    }
  ]
})
```
