# Call functions from your Amazon Bedrock chat agent app

Amazon Bedrock in SageMaker Unified Studio functions let a model include information that it has no previous knowledge of
in its response. For example, you can use a function to include dynamic information in a model's
response such as a weather forecast, sports results, or traffic conditions.

In Amazon Bedrock in SageMaker Unified Studio, a function calls an API hosted outside of Amazon Bedrock in SageMaker Unified Studio. You either
create the API yourself, or use an existing API. To create an API, you can use [Amazon API Gateway](../../../apigateway.md "../../../apigateway.md").

To use a function in Amazon Bedrock in SageMaker Unified Studio you add a
_function component_ to your app. As part of the
function, you define an OpenAPI schema for the API that you want the model to call. You also
specify how to authenticate the call to the API. When a model receives a prompt, it uses the schema
and the prompt to determine if an API should be called and the parameters that the API should
receive. If the API is called, the response from the model includes the output from the API.

APIs that you call in a function must have a response size that is less than 20K.

When add a function to an app, you need to specify the app's system instruction.
The system instruction needs to be at least 40 characters long and should mention the new skills that
the new function introduces.

You can use functions in a [chat agent app](create-chat-app.md "create-chat-app.md").

###### Topics

- [Function schema](#functions-schema "#functions-schema")
- [Authentication methods](#functions-authentication "#functions-authentication")
- [Create an Amazon Bedrock function component](creating-a-function-component.md "creating-a-function-component.md")
- [Add a function component to an Amazon Bedrock chat agent app](add-function-component-chat-app.md "add-function-component-chat-app.md")

## Function schema

Amazon Bedrock in SageMaker Unified Studio has the following requirements for the schema that you use to create a
function.

- The function schema must be [OpenAPI
  version 3.0.0](https://spec.openapis.org/oas/v3.0.0.html "https://spec.openapis.org/oas/v3.0.0.html").
- The function schema must be in JSON or YAML format.
- The function can have no authentication, API key authentication, Bearer token
  authentication, or basic authentication. For more information, see [Authentication methods](#functions-authentication "#functions-authentication").
- You can have 0 or 1 server URL.
- All [Operation
  Objects](https://swagger.io/specification/v3/#operation-object "https://swagger.io/specification/v3/#operation-object") must have a description.
- All [Parameter
  Objects](https://swagger.io/specification/v3/#parameter-object "https://swagger.io/specification/v3/#parameter-object") must have a description.
- [Security
  scheme object](https://swagger.io/specification/v3/#security-scheme-object "https://swagger.io/specification/v3/#security-scheme-object") must have a type that is either `apiKey` or
  `http`.

When the type is `http`, the scheme field must either be `basic` or
`bearer`.

When the type is `apiKey`, the `in` property must be
`query` or `header`. Also, the `name` property must be defined.

- Amazon Bedrock in SageMaker Unified Studio only honors [globally-scoped
  security requirement](https://swagger.io/specification/v3/#security-requirement-object "https://swagger.io/specification/v3/#security-requirement-object"). For more information, see [Valid components for globally-scoped security requirements](#example-components "#example-components").
- Parameters (**parameter.in**) must be pass passed through
  query or path. You can't use cookies or headers to pass parameters.
- Parameters (**parameter schema type**) must be primitive
  types, arrays, or objects (one-level JSON). You can't pass complex nested objects.
- Parameter content (**parameter.content**) is mutually
  exclusive with the schema. Schema is more commonly used. Use content only for more complex
  types, or for complex serialization scenarios that are not covered by style and explode.
- Parameter **style** and **explode** values. `form` and `true` for query,
  `simple` and `false` for paths). For more information, see [Parameter
  Serialization](https://swagger.io/docs/specification/serialization/ "https://swagger.io/docs/specification/serialization/").
- Request body content must be passed as `application/json`.
- The schema can have up to 5 APIs and an app can use up to 5 APIs across all functions. For
  the model to correctly choose function, it is important to provide detailed descriptions of the
  API, including parameters, properties, and responses.

### Valid components for globally-scoped security requirements

Amazon Bedrock in SageMaker Unified Studio only honors
[globally-scoped
security requirements](https://swagger.io/specification/v3/#security-requirement-object "https://swagger.io/specification/v3/#security-requirement-object"). That is, Amazon Bedrock in SageMaker Unified Studio ignores security requirements indicated in operation objects.

When the requirement array contains a security scheme object with type `http`
and scheme of `bearer` or `basic`, the array must contain a single entry.
Amazon Bedrock in SageMaker Unified Studio ignores further entries.

When the requirement array contains a security scheme object with type
`apiKey`, you can have a maximum of 2 entries.

For example, if you have the following [components](https://swagger.io/specification/v3/#components-object "https://swagger.io/specification/v3/#components-object"):

```
"components": {
  "securitySchemes": {
    "api_key_1": {
      "type": "apiKey",
      "name": "appid1",
      "in": "query"
    },
    "api_key_2": {
      "type": "apiKey",
      "name": "appid2",
      "in": "header"
    },
    "api_key_3": {
      "type": "apiKey",
      "name": "appid3",
      "in": "cookie"
    },
    "bearer_1": {
      "type": "http",
      "scheme": "bearer",
    },
    "bearer_2": {
      "type": "http",
      "scheme": "bearer",
    },
    "basic_1": {
      "type": "http",
      "scheme": "basic",
    },
    "basic_2": {
      "type": "http",
      "scheme": "basic",
    },
    "http_digest": {
      "type": "http",
      "scheme": "digest"
    },
    "oauth2_1": {
      "type": "oauth2"
    }
  }
}
```

The following are valid:

```
# 1 API key
"security": [
  {
    "api_key_1": []
  }
],

# 2 API keys
"security": {
  {
    "api_key_1": [],
    "api_key_2": []
  }
}

# Bearer
"security": {
   "bearer_1": []
}

# Basic
"security": {
   "basic_1": []
}
```

The following are invalid:

```
# Invalid: `type` must only be `apiKey` or `http`
"security": {
  "oauth2_1": []
}

# Invalid: `scheme` must only be `basic` or `bearer` if `type` is `http`
"security": {
  "http_digest": []
}

# Invalid: `security` must only contain 1 entry if `type` is `basic` or `bearer`
"security": {
  "basic_1": [],
  "basic_2": []
}

# Invalid: `security` must not contain varying security types
"security": {
  "api_key_1": [],
  "basic_1": []
}

# Invalid: API key must only have `in` property set to `header` or `query`
"security": {
  "api_key_1": [],
  "api_key_3": []
}

# Invalid: `security` must not have more than 2 API keys
"security": {
  {
    "api_key_1": [],
    "api_key_2": [],
    "api_key_3": []
  }
}
```

## Authentication methods

Amazon Bedrock in SageMaker Unified Studio supports the following methods for authenticating function calls to an API
server. If you authenticate a function call, make sure the credentials you provide are correct
as Amazon Bedrock in SageMaker Unified Studio doesn't verify the credentials before you use them in a function call.

- **No authentication** – No authentication means that
  the client doesn't need to provide any credentials to access a resource or service. This method
  is typically used for publicly available resources that don't require any form of
  authentication.
- **[API
  keys](https://swagger.io/docs/specification/authentication/api-keys/ "https://swagger.io/docs/specification/authentication/api-keys/")** – An API key is a unique identifier used
  to authenticate a client application and allow it to access an API or service. You can add a
  maximum of two keys.
- **[Bearer token](https://swagger.io/docs/specification/authentication/bearer-authentication/ "https://swagger.io/docs/specification/authentication/bearer-authentication/")** – A bearer token is an opaque string
  that represents an authentication credential. It is typically obtained after a successful
  authentication process, such as OAuth 2.0. This method allows the client to access protected
  resources without having to send the actual credentials (username and password) with each
  request.

###### Note

Amazon Bedrock in SageMaker Unified Studio is unable to assure whether the token is valid or has already expired. It
is your responsibility to make sure that you provide a valid token, and
to update the token to a new one before it expires. If the token expires, Amazon Bedrock
won't be able to successfully call APIs with the token.

- **[Basic
  authentication](https://swagger.io/docs/specification/authentication/basic-authentication/ "https://swagger.io/docs/specification/authentication/basic-authentication/")** – Basic authentication is a simple authentication
  scheme built into the HTTP protocol. The credentials are sent with every request, which can be
  a security concern if the connection is not secured using HTTPS. Basic authentication is
  generally considered less secure than other modern authentication methods and should be used
  with caution, especially in production environments.
