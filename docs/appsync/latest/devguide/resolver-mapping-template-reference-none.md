

# AWS AppSync resolver mapping template reference for `None` data source
<a name="resolver-mapping-template-reference-none"></a>

**Note**  
We now primarily support the APPSYNC\_JS runtime and its documentation. Please consider using the APPSYNC\_JS runtime and its guides [here](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-reference-js-version.html).

The AWS AppSync resolver mapping template used with the data source of type *None*, enables you to shape requests for AWS AppSync local operations.

## Request mapping template
<a name="request-mapping-template"></a>

The mapping template is simple and enables you to pass as much context information as possible via the `payload` field.

```
{
   "version": string,
   "payload": any type
}
```

Here is the JSON schema representation of the request mapping template, once resolved:

```
{
    "definitions": {},
    "$schema": "https://json-schema.org/draft-06/schema#",
    "$id": "https://aws.amazon.com/appsync/request-mapping-template.json",
    "type": "object",
    "properties": {
        "version": {
            "$id": "/properties/version",
            "type": "string",
            "enum": [
                "2018-05-29"
            ],
            "title": "The Mapping template version.",
            "default": "2018-05-29"
        },
        "payload": {}
    },
    "required": [
        "version"
    ],
    "additionalProperties": false
}
```

Here is an example where the field arguments are passed via the VTL context property `$context.arguments`:

```
{
    "version": "2018-05-29",
    "payload": $util.toJson($context.arguments)
}
```

The value of the `payload` field will be forwarded to the response mapping template and available on the VTL context property (`$context.result`).

This is an example representing the interpolated value of the `payload` field:

```
{
    "id": "postId1"
}
```

## Version
<a name="version"></a>

Common to all request mapping templates, the `version` field defines the version used by the template.

 The `version` field is required.

Example:

```
"version": "2018-05-29"
```

## Payload
<a name="payload"></a>

The `payload` field is a container that can be used to pass any well-formed JSON to the response mapping template.

 The `payload` field is optional.

## Response mapping template
<a name="response-mapping-template"></a>

Because there is no data source, the value of the `payload` field will be forwarded to the response mapping template and set on the `context` object that is available via the VTL `$context.result` property.

If the shape of the `payload` field value exactly matches the shape of the GraphQL type, you can forward the response using the following response mapping template:

```
$util.toJson($context.result)
```

There are no required fields or shape restrictions that apply to the response mapping template. However, because GraphQL is strongly typed, the resolved mapping template must match the expected GraphQL type.