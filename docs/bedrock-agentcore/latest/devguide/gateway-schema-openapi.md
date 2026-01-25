# OpenAPI schema targets

OpenAPI (formerly known as Swagger) is a widely used standard for describing RESTful
APIs. Gateway supports OpenAPI 3.0 specifications for defining API targets.

OpenAPI targets connect your gateway to REST APIs defined using OpenAPI specifications. The Gateway translates incoming MCP requests into HTTP requests to these APIs and handles the response formatting.

Review the key considerations and limitations, including feature support, to help you decide whether an OpenAPI target is applicable to your use case. If it is, you can create a schema that follows the specifications and then set up permissions for the gateway to be able to access the target. Select a topic to learn more:

###### Topics

- [Key considerations and
  limitations](#gateway-schema-openapi-considerations "#gateway-schema-openapi-considerations")
- [OpenAPI schema specification](#gateway-openapi-schema "#gateway-openapi-schema")

## Key considerations and

limitations

###### Important

The OpenAPI specification must include `operationId` fields for all
operations that you want to expose as tools. The operationId is used as the tool name in
the MCP interface.

When using OpenAPI targets, keep in mind the following requirements and
limitations:

- OpenAPI versions 3.0 and 3.1 are supported (Swagger 2.0 is not supported)
- The OpenAPI file must be free of semantic errors
- The server attribute needs to have a valid URL of the actual endpoint
- Only application/json content type is fully supported
- Complex schema features like oneOf, anyOf, and allOf are not supported
- Path parameter serializers and parameter serializers for query, header, and cookie
  parameters are not supported
- Each LLM will have ToolSpec constraints. If OpenAPI has APIs/properties/object
  names not compliant to ToolSpec of the respective downstream LLMs, the data plane will
  fail. Common errors are property name exceeding the allowed length or the name
  containing unsupported character.

For best results with OpenAPI targets:

- Always include operationId in all operations
- Use simple parameter structures instead of complex serialization
- Implement authentication and authorization outside of the specification
- Only use supported media types for maximum compatibility

### Security best practices for URL parameters

###### Warning

When defining server URLs in your OpenAPI specifications, avoid using overly permissive URL parameter patterns that could expose your gateway to security risks.

URL parameters in OpenAPI server definitions allow dynamic endpoint configuration. However, certain patterns can introduce security vulnerabilities if not properly constrained. Specifically, avoid using fully dynamic domain patterns such as:

- `https://{yourDomain}/` - Allows arbitrary domain substitution
- `https://{subdomain}.{env}.{domain}.com` - Multiple unconstrained placeholders
- `https://{host}/api/` - Unrestricted host parameter

These patterns can potentially be exploited to:

- Redirect requests to unintended or malicious endpoints
- Access internal network resources (Server-Side Request Forgery)
- Exfiltrate credentials or sensitive data

**Recommended practices:**

- Use fully qualified, static URLs whenever possible: `https://api.example.com/v1`
- Limit parameters to subdomains within your controlled domain and implement validation in your application
- Avoid using parameters that allow arbitrary domain or host substitution
- Implement additional validation in your API to verify that runtime parameter values match expected patterns

AgentCore Gateway automatically validates region parameters and blocks requests to private IP ranges.

Example of a secure server URL configuration:

```
{
  "servers": [
    {
      "url": "https://api.example.com/v1"
    }
  ]
}
```

If dynamic parameters are necessary, use fully qualified domains with minimal placeholders and enum restrictions:

```
{
  "servers": [
    {
      "url": "https://{tenant}.api.example.com/v1",
      "variables": {
        "tenant": {
          "default": "default-tenant",
          "description": "Customer tenant identifier",
          "enum": ["tenant1", "tenant2", "tenant3"]
        }
      }
    }
  ]
}
```

This approach restricts URL parameters to specific subdomains within your controlled domain while maintaining flexibility for multi-tenant deployments. Using enum restrictions prevents arbitrary values and helps protect against SSRF attacks by limiting parameters to predefined, safe values. Additionally, always validate tenant values in your application logic.

In considering using OpenAPI schema targets with AgentCore Gateway, review the following feature support table.

### OpenAPI feature support

The following table outlines the OpenAPI features that are supported and unsupported
by Gateway:

| OpenAPI feature support                                                                                                                                                                                        | Supported Features                                                                                                                                                                                                                       | Unsupported Features |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| **Schema Definitions**<br>• Basic data types (string, number, integer, boolean, array,<br>object)<br>• Required field validation<br>• Nested object structures<br>• Array definitions with item specifications | **Schema Composition**<br>• oneOf specifications<br>• anyOf specifications<br>• allOf specifications                                                                                                                                     |
| **HTTP Methods**<br>• Standard HTTP methods (GET, POST, PUT, DELETE, PATCH, HEAD,<br>OPTIONS)                                                                                                                  | **Security Schemes**<br>• Security schemes at the OpenAPI specification level (authentication<br>must be configured using the Gateway's outbound authorization configuration)                                                            |
| **Media Types**<br>• application/json<br>• application/xml<br>• multipart/form-data<br>• application/x-www-form-urlencoded                                                                                     | **Media Types**<br>• Custom media types beyond the supported list<br>• Binary media types                                                                                                                                                |
| **Path Parameters**<br>• Simple path parameter definitions (Example: /users/{userId})                                                                                                                          | **Parameter Serialization**<br>• Complex path parameter serializers (Example:<br>`/users{;id\\*}{?metadata}`)<br>• Query parameter arrays with complex serialization<br>• Header parameter serializers<br>• Cookie parameter serializers |
| **Query Parameters**<br>• Basic query parameter definitions<br>• Simple string, number, and boolean types                                                                                                      | **Callbacks and Webhooks**<br>• Callback operations<br>• Webhook definitions                                                                                                                                                             |
| **Request/Response Bodies**<br>• JSON request and response bodies<br>• XML request and response bodies<br>• Standard HTTP status codes (200, 201, 400, 404, 500, etc.)                                         | **Links**<br>• Links between operations                                                                                                                                                                                                  |

## OpenAPI schema specification

The OpenAPI specification defines the REST API that your Gateway will expose. Refer to the following resources when setting up your OpenAPI specification:

- For information about the format of the OpenAPI specification, see [OpenAPI Specification](https://swagger.io/specification/ "https://swagger.io/specification/").
- For information about supported and unsupported features when using an OpenAPI specification with AgentCore Gateway, see the table in [OpenAPI feature support](#gateway-schema-openapi-features "#gateway-schema-openapi-features"). Adhere to these requirements to prevent errors during target creation and invocation.

After you define your OpenAPI schema, you can do one of the following:

- Upload it to an Amazon S3 bucket and refer to the S3 location when you add the target to your gateway.
- Paste the definition inline when you add the target to your gateway.

Expand a section to see examples of supported and unsupported OpenAPI specifications:

Following shows an example of a supported OpenAPI specification

Example of a supported OpenAPI specification:

```
{
  "openapi": "3.0.0",
  "info": {
    "title": "Weather API",
    "version": "1.0.0",
    "description": "API for retrieving weather information"
  },
  "servers": [
    {
      "url": "https://api.example.com/v1"
    }
  ],
  "paths": {
    "/weather": {
      "get": {
        "summary": "Get current weather",
        "description": "Returns current weather information for a location",
        "operationId": "getCurrentWeather",
        "parameters": [
          {
            "name": "location",
            "in": "query",
            "description": "City name or coordinates",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "units",
            "in": "query",
            "description": "Units of measurement (metric or imperial)",
            "required": false,
            "schema": {
              "type": "string",
              "enum": ["metric", "imperial"],
              "default": "metric"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful response",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "location": {
                      "type": "string"
                    },
                    "temperature": {
                      "type": "number"
                    },
                    "conditions": {
                      "type": "string"
                    },
                    "humidity": {
                      "type": "number"
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Invalid request"
          },
          "404": {
            "description": "Location not found"
          }
        }
      }
    }
  }
}
```

Following shows another example of a supported OpenAPI specification.

```
{
  "openapi": "3.0.0",
  "info": {
    "title": "Search API",
    "version": "1.0.0",
    "description": "API for searching content"
  },
  "servers": [
    {
      "url": "https://api.example.com/v1"
    }
  ],
  "paths": {
    "/search": {
      "get": {
        "summary": "Search for content",
        "operationId": "searchContent",
        "parameters": [
          {
            "name": "query",
            "in": "query",
            "description": "Search query",
            "required": true,
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "limit",
            "in": "query",
            "description": "Maximum number of results",
            "required": false,
            "schema": {
              "type": "integer",
              "default": 10
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successful response",
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "properties": {
                    "results": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "title": {
                            "type": "string"
                          },
                          "url": {
                            "type": "string"
                          },
                          "snippet": {
                            "type": "string"
                          }
                        }
                      }
                    },
                    "total": {
                      "type": "integer"
                    }
                  }
                }
              }
            }
          },
          "400": {
            "description": "Bad request"
          }
        }
      }
    }
  }
}
```

The following shows an example of an unsupported schema with oneOf:

```
{
  "oneOf": [
    {"$ref": "#/components/schemas/Pencil"},
    {"$ref": "#/components/schemas/Pen"}
  ]
}
```
