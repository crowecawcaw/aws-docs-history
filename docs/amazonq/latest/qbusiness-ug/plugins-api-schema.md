# Defining OpenAPI schemas for custom plugins

Amazon Q Business uses the configured third-party OpenAPI specifications to
dynamically determine which API operations to perform in order to fulfill an end user
requests. To configure a custom plugin you must define at least 1 API operation and a
maximum of 20 API operations that can be invoked. To define the API operations, create
an OpenAPI schema in JSON or YAML format. You can create OpenAPI schema files and upload
them to Amazon Simple Storage Service (Amazon S3). Alternatively, you can use the
OpenAPI text editor in the console, which will validate your schema.

This section will first cover the required definitions for the OpenAPI schema. The
next section will cover [best practices and examples for configuring OpenAPI schema
definitions](plugins-api-schema-best-practices.md "plugins-api-schema-best-practices.md") to maximize the accuracy of your Amazon Q Business custom
plugins. For more details about OpenAPI schemas, see [OpenAPI specification](https://swagger.io/specification/ "https://swagger.io/specification/") on the
Swagger website.

###### Topics

- [OpenAPI Schema definitions for custom plugins](#plugins-api-schema-definition "#plugins-api-schema-definition")

## OpenAPI Schema definitions for custom plugins

The following is the general format of an OpenAPI schema for a custom
plugin.

```
{
    "openapi": "3.0.0",
    "servers": [
    {
      "url": "https://api.example.com"
    }
  ],
    "paths": {
        "/`path`": {
            "`method`": {
                "description": "`string`",
                "operationId": "`string`",
                "parameters": [ ... ],
                "requestBody": { ... },
                "responses": { ... },
                "security": [ ... ]
           }
       }
    },
    "security": [
        {
            "OAuth2": ["read", "write"]
        }
    ],
    "components": {
    "securitySchemes": {}
 }
}
```

The following list describes fields in the OpenAPI schema

- `openapi` – (Required) The version of OpenAPI that's
  being used. This value must be `"3.0.0"` or higher for custom
  plugins.
- `servers` – (Required) The identifier for application
  connectivity from API clients. This is required for the custom plugin call
  to succeed.
- `paths` – (Required) Contains relative paths to
  individual endpoints. Each path must begin with a forward slash
  (`/`). Amazon Q Business supports only one configured
  endpoint per custom plugin.
- `method` – (Required) Defines the method to use.
- `securitySchemes` – (Optional) Defines the OAuth security
  parameters.
- `security` – (Required when using authentication) Defines
  which security schemes are applied to the whole API or specific operations.
  This is required when using OAuth authentication.

Minimally, each method requires the following fields:

- `description` – A description of the API operation. Use
  this field to let the custom plugin know when to call this API operation and
  what the operation does.
- `responses` – Contains properties that the custom plugin
  returns in the API response. The custom plugin uses the response properties
  to construct prompts, accurately process the results of an API call, and
  determine a correct set of steps for performing an action.

The fields within the following two objects provide more information for your
custom plugin to effectively select API operations that are needed to fulfill an end
user request. For each field, set the value of the `required` field to
`true` if required and to `false` if optional.

- `parameters` – Contains information about parameters that
  can be included in the request.
- `requestBody` – Contains the fields in the request body
  for the operation. Don't include this field for `GET` and
  `DELETE` methods.

For details on configuring the fields review the following sections:

###### Topics

- [OpenAPI Schema responses](#plugins-api-schema-responses "#plugins-api-schema-responses")
- [OpenAPI Schema parameters](#plugins-api-schema-parameters "#plugins-api-schema-parameters")
- [OpenAPI Schema request body](#plugins-api-schema-request-body "#plugins-api-schema-request-body")
- [OpenAPI Schema security schemes](#plugins-api-schema-security-scheme "#plugins-api-schema-security-scheme")

### OpenAPI Schema responses

The following is a sample response.

```
"responses": {
    "200": {
        "content": {
            "`<media type>`": {
                "schema": {
                    "properties": {
                        "`<property>`": {
                            "type": "`string`",
                            "description": "`string`"
                        },
                        ...
                    }
                }
            }
        },
    },
    ...
}
```

Each key in the `responses` object is a response code, which
describes the status of the response. The response code maps to an object that
contains the following information for the response:

- `content` – (Required for each response) The content
  of the response.
- `<media type>` – The format of
  the response body. At this time, only `application/json` is
  supported by custom plugins. For more information, see [Media
  types](https://swagger.io/docs/specification/media-types/ "https://swagger.io/docs/specification/media-types/") on the Swagger website.
- `schema` – (Required for each media type) Defines the
  data type of the response body and its fields.
- `properties` – (Required if there are
  `items` in the schema) Your custom plugins uses
  properties that you define in the schema to determine the information it
  needs to return to the end user in order to fulfill a task. Each
  property contains the following fields:
  - `type` – (Required for each property) The
    data type of the response field.
  - `description` – (Optional) Describes the
    property. The custom plugin can use this information to
    determine the information that it needs to return to the end
    user.

### OpenAPI Schema parameters

The following are examples of parameters.

```
"parameters": [
    {
        "name": "string", // e.g. "userName"
        "description": "string",
        "required": boolean,
        "x-amzn-form-display-name": "string" // e.g. "User Name"
        "schema": {
            ...
        }
    },
    {
        "name": "string", // e.g. "employeeId"
        "description": "string",
        "required": boolean,
        "x-amzn-form-hide": boolean //e.g. true
        "schema": {
            ...
        }
    }
    ...
]
```

Your custom plugin uses the following fields to determine the information it
must get from the end user to perform the plugin's requirements.

- `name` – (Required) The name of the parameter.
- `description` – (Required) A description of the
  parameter. Use this field to help the plugin to understand how to elicit
  this parameter from the user or determine that it already has that
  parameter value from prior actions or from the user’s request to the
  custom plugin.
- `required` – (Optional) Whether the parameter is
  required for the API request. Use this field to indicate to the custom
  plugin whether this parameter is needed for every invocation or if it's
  optional.
- `schema` – (Optional) The definition of input and
  output data types. For more information, see [Data Models
  (Schemas)](https://swagger.io/docs/specification/data-models/ "https://swagger.io/docs/specification/data-models/") on the Swagger website.
- Extension support – (Optional) For a write API operation, an
  Amazon Q Business custom plugin may dynamically create a confirmation form that
  is presented to end users. This form allows users to confirm and/or
  correct parameters Amazon Q populated based on the end user’s request
  or past actions. The following extensions can be used to modify how that
  form is created:
  - `x-amzn-form-display-name` – (Optional) This
    can be used at parameter level to override the default name
    visible in the form.
  - `x-amzn-form-hide` – (Optional) This can be
    used to hide a parameter from being displayed in the user facing
    form.

- Schemas containing composition keywords (`allOf`,
  `not`, `oneOf`, or `anyOf`) are not
  supported.
- Schemas containing array types are not supported. For example, schemas
  such as `{"type": "array", "items": {"string"}}` are not
  supported.

### OpenAPI Schema request body

The following is the general structure of a `requestBody`
field:

```
"requestBody": {
    "required": boolean,
    "content": {
        "`<media type>`": {
            "schema": {
                "properties": {
                    "`<property>`": {
                        "type": "`string`",
                        "description": "`string`"
                    },
                    ...
                }
            }
        }
    }
}
```

The following list describes each field:

- `required` – (Optional) Whether the request body is
  required for the API request.
- `content` – (Required) The content of the request
  body.
- `<media type>` – (Optional) The
  format of the request body. At this time, only
  `application/json` is supported by custom plugins. For
  more information, see [Media
  types](https://swagger.io/docs/specification/media-types/ "https://swagger.io/docs/specification/media-types/") on the Swagger website.
- `schema` – (Optional) Defines the data type of the
  request body and its fields.
- `properties` – (Optional) Your custom plugin uses
  properties that you define in the schema to determine the information it
  must get from the end user to make the API request. Each property
  contains the following fields:
  - `type` – (Optional) The data type of the
    request field.
  - `description` – (Optional) Describes the
    property. The custom plugin can use this information to
    determine the information it needs to return to the end
    user.

- Schemas containing composition keywords (`allOf`,
  `not`, `oneOf`, or `anyOf`) are not
  supported.
- Schemas containing array types are not supported. For example, schemas
  such as `{"type": "array", "items": {"string"}}` are not
  supported.

### OpenAPI Schema security schemes

Following is the general structure of a `securityScheme`
field:

```
"securitySchemes": {
      "OAuth2": {
        "type": "oauth2",
        "flows": {
          "authorizationCode": {
            "authorizationUrl": "https://example.com/oauth/authorize",
            "tokenUrl": "https://example.com/oauth/token",
            "scopes": {
              "read": "Read access to resources",
              "write": "Write access to resources"
            }
          }
        }
      }
    }
```

If your API requires OAuth authorization, the OpenAPI schema needs to include
security schemes. We support the following authorization code flow of
OAuth:

- `type` – Must be `oauth2`.
- `flows` – Must contain
  `authorizationCode`.
- `authorizationUrl` – The URL to which the user will
  be sent to begin the authorization process.
- `tokenUrl` – (Optional) The URL that the custom
  plugin will use to exchange the authorization code for an access
  token.
- `scopes` – Defines the permissions that the custom
  plugin will request.

Successful authorization using OAuth also requires an OAuth client ID, client
secret, and a redirect url. These will need to be provided as secrets when
creating the custom plugin.
