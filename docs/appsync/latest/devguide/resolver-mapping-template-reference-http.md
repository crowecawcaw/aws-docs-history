# AWS AppSync resolver

mapping template reference for HTTP

###### Note

We now primarily support the APPSYNC_JS runtime and its documentation. Please consider using the
APPSYNC_JS runtime and its guides [here](resolver-reference-js-version.md "resolver-reference-js-version.md").

The AWS AppSync HTTP resolver mapping templates enable you to send requests from
AWS AppSync to any HTTP endpoint, and responses from your HTTP endpoint back to
AWS AppSync. By using mapping templates, you can provide hints to AWS AppSync about the
nature of the operation to be invoked. This section describes the different mapping
templates for the supported HTTP resolver.

## Request mapping template

```
{
    "version": "2018-05-29",
    "method": "PUT|POST|GET|DELETE|PATCH",
    "params": {
        "query": Map,
        "headers": Map,
        "body": any
    },
    "resourcePath": string
}
```

After the HTTP request mapping template is resolved, the JSON schema representation of
the request mapping template looks like the following:

```
{
    "$id": "https://aws.amazon.com/appsync/request-mapping-template.json",
    "type": "object",
    "properties": {
        "version": {
        "$id": "/properties/version",
        "type": "string",
        "title": "The Version Schema ",
        "default": "",
        "examples": [
            "2018-05-29"
        ],
        "enum": [
            "2018-05-29"
        ]
        },
        "method": {
        "$id": "/properties/method",
        "type": "string",
        "title": "The Method Schema ",
        "default": "",
        "examples": [
            "PUT|POST|GET|DELETE|PATCH"
        ],
        "enum": [
            "PUT",
            "PATCH",
            "POST",
            "DELETE",
            "GET"
        ]
        },
        "params": {
        "$id": "/properties/params",
        "type": "object",
        "properties": {
            "query": {
            "$id": "/properties/params/properties/query",
            "type": "object"
            },
            "headers": {
            "$id": "/properties/params/properties/headers",
            "type": "object"
            },
            "body": {
            "$id": "/properties/params/properties/body",
            "type": "string",
            "title": "The Body Schema ",
            "default": "",
            "examples": [
                ""
            ]
            }
        }
        },
        "resourcePath": {
        "$id": "/properties/resourcePath",
        "type": "string",
        "title": "The Resourcepath Schema ",
        "default": "",
        "examples": [
            ""
        ]
        }
    },
    "required": [
        "version",
        "method",
        "resourcePath"
    ]
}
```

Following is an example of an HTTP POST request, with a `text/plain`
body:

```
{
    "version": "2018-05-29",
    "method": "POST",
    "params": {
        "headers":{
        "Content-Type":"text/plain"
        },
        "body":"this is an example of text body"
    },
    "resourcePath": "/"
}
```

## Version

###### Note

This applies only to the Request mapping template.

Defines the version that the template uses. `version` is common to all
request mapping templates and is required.

```
"version": "2018-05-29"
```

## Method

###### Note

This applies only to the Request mapping template.

HTTP method or verb (GET, POST, PUT, PATCH, or DELETE) that AWS AppSync sends to the
HTTP endpoint.

```
"method": "PUT"
```

## ResourcePath

###### Note

This applies only to the Request mapping template.

The resource path that you want to access. Along with the endpoint in the HTTP data
source, the resource path forms the URL that the AWS AppSync service makes a request
to.

```
"resourcePath": "/v1/users"
```

When the mapping template is evaluated, this path is sent as part of the HTTP request,
including the HTTP endpoint. For example, the previous example might translate to the
following:

```
PUT <endpoint>/v1/users
```

## Params fields

###### Note

This applies only to the Request mapping template.

Used to specify what action your search performs, most commonly by setting the
**query** value inside the **body**. However, there are several other capabilities that can be
configured, such as the formatting of responses.

\***\*headers\*\***

The header information, as key-value pairs. Both the key and the value
must be strings.

For example:

```
"headers" : {
    "Content-Type" : "application/json"
}
```

Currently supported `Content-Type` headers are:

```
text/*
application/xml
application/json
application/soap+xml
application/x-amz-json-1.0
application/x-amz-json-1.1
application/vnd.api+json
application/x-ndjson
```

**Note**: You can’t set the following HTTP
headers:

```
HOST
CONNECTION
USER-AGENT
EXPECTATION
TRANSFER_ENCODING
CONTENT_LENGTH
```

\***\*query\*\***

Key-value pairs that specify common options, such as code formatting for
JSON responses. Both the key and the value must be a string. The following
example shows how you can send a query string as
`?type=json`:

```
"query" : {
    "type" : "json"
}
```

\***\*body\*\***

The body contains the HTTP request body that you choose to set. The
request body is always a UTF-8 encoded string unless the content type
specifies the charset.

```
"body":"body string"
```

## Response

See an example [here](tutorial-http-resolvers.md "tutorial-http-resolvers.md").
