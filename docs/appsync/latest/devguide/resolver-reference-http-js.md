# AWS AppSync JavaScript resolver function

reference for HTTP

The AWS AppSync HTTP resolver functions enable you to send requests from AWS AppSync to any HTTP endpoint,
and responses from your HTTP endpoint back to AWS AppSync. With your request handler, you can provide hints to
AWS AppSync about the nature of the operation to be invoked. This section describes the different
configurations for the supported HTTP resolver.

## Request

```
type HTTPRequest = {
  method: 'PUT' | 'POST' | 'GET' | 'DELETE' | 'PATCH';
  params?: {
    query?: { [key: string]: any };
    headers?: { [key: string]: string };
    body?: any;
  };
  resourcePath: string;
};
```

The following snippet is an example of an HTTP POST request, with a `text/plain` body:

```
export function request(ctx) {
  return {
    method: 'POST',
    params: {
      headers: { 'Content-Type': 'text/plain' },
      body: 'this is an example of text body',
    },
    resourcePath: '/',
  };
}
```

## Method

###### Note

This applies only to the Request handler.

HTTP method or verb (GET, POST, PUT, PATCH, or DELETE) that AWS AppSync sends to the HTTP
endpoint.

```
"method": "PUT"
```

## ResourcePath

###### Note

This applies only to the Request handler.

The resource path that you want to access. Along with the endpoint in the HTTP data source, the resource
path forms the URL that the AWS AppSync service makes a request to.

```
"resourcePath": "/v1/users"
```

When the request is evaluated, this path is sent as part of the HTTP request, including the HTTP endpoint.
For example, the previous example might translate to the following:

```
PUT <endpoint>/v1/users
```

## Params fields

###### Note

This applies only to the Request handler.

Used to specify what action your search performs, most commonly by setting the **query** value inside the **body**. However, there are several
other capabilities that can be configured, such as the formatting of responses.

\***\*headers\*\***

The header information, as key-value pairs. Both the key and the value must be strings.

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

You can’t set the following HTTP headers:

```
HOST
CONNECTION
USER-AGENT
EXPECTATION
TRANSFER_ENCODING
CONTENT_LENGTH
```

\***\*query\*\***

Key-value pairs that specify common options, such as code formatting for JSON responses. Both
the key and the value must be a string. The following example shows how you can send a query
string as `?type=json`:

```
"query" : {
    "type" : "json"
}
```

\***\*body\*\***

The body contains the HTTP request body that you choose to set. The request body is always a
UTF-8 encoded string unless the content type specifies the charset.

```
"body":"body string"
```

## Response

See an example [here](tutorial-http-resolvers-js.md "tutorial-http-resolvers-js.md").
