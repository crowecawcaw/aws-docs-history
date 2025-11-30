# Determine function purpose

Before you write your function code, determine the purpose of your function. Most
functions in CloudFront Functions have one of the following purposes.

###### Topics

- [Modify the HTTP request in a viewer
  request event type](#function-code-modify-request "#function-code-modify-request")
- [Generate an HTTP response in a
  viewer request event type](#function-code-generate-response "#function-code-generate-response")
- [Modify the HTTP response in a viewer
  response event type](#function-code-modify-response "#function-code-modify-response")
- [Validate mTLS connections in a
  connection request event type](#function-code-connection-request "#function-code-connection-request")
- [Related
  information](#related-information-cloudfront-functions-purpose "#related-information-cloudfront-functions-purpose")
  Regardless of your function’s purpose, the `handler` is the entry point for
  any function. It takes a single argument called `event`, which is passed to
  the function by CloudFront. The `event` is a JSON object that contains a
  representation of the HTTP request (and the response, if your function modifies the HTTP
  response).

## Modify the HTTP request in a viewer

request event type

Your function can modify the HTTP request that CloudFront receives from the viewer
(client), and return the modified request to CloudFront for continued processing. For
example, your function code might normalize the [cache key](understanding-the-cache-key.md "understanding-the-cache-key.md") or modify request
headers.

After you create and publish a function that modifies the HTTP request, make sure
to add an association for the _viewer request_
event type. For more information, see [Create the function](functions-tutorial.md#functions-tutorial-create "functions-tutorial.md#functions-tutorial-create"). This makes the function run each
time that CloudFront receives a request from a viewer, before checking to see whether the
requested object is in the CloudFront cache.

###### Example

The following pseudocode shows the structure of a function that modifies the
HTTP request.

```
function handler(event) {
    var request = event.request;

    // Modify the request object here.

    return request;
}
```

The function returns the modified `request` object to CloudFront. CloudFront
continues processing the returned request by checking the CloudFront cache for a cache
hit, and sending the request to the origin if necessary.

## Generate an HTTP response in a

viewer request event type

Your function can generate an HTTP response at the edge and return it directly to
the viewer (client) without checking for a cached response or any further processing
by CloudFront. For example, your function code might redirect the request to a new URL, or
check for authorization and return a `401` or `403` response
to unauthorized requests.

When you create a function that generates an HTTP response, make sure to choose
the _viewer request_ event type. This means that
the function runs each time CloudFront receives a request from a viewer, before CloudFront does
any further processing of the request.

###### Example

The following pseudocode shows the structure of a function that generates an
HTTP response.

```
function handler(event) {
    var request = event.request;

    var response = ...; // Create the response object here,
                        // using the request properties if needed.

    return response;
}
```

The function returns a `response` object to CloudFront, which CloudFront
immediately returns to the viewer without checking the CloudFront cache or sending a
request to the origin.

## Modify the HTTP response in a viewer

response event type

Your function can modify the HTTP response before CloudFront sends it to the viewer
(client), regardless of whether the response comes from the CloudFront cache or the
origin. For example, your function code might add or modify response headers, status
codes, and body content.

When you create a function that modifies the HTTP response, make sure to choose
the _viewer response_ event type. This means that
the function runs before CloudFront returns a response to the viewer, regardless of
whether the response comes from the CloudFront cache or the origin.

###### Example

The following pseudocode shows the structure of a function that modifies the
HTTP response.

```
function handler(event) {
    var request = event.request;
    var response = event.response;

    // Modify the response object here,
    // using the request properties if needed.

    return response;
}
```

The function returns the modified `response` object to CloudFront, which
CloudFront immediately returns to the viewer.

## Validate mTLS connections in a

connection request event type

Connection functions are a type of CloudFront Functions that run during TLS connections
to provide custom validation and authentication logic. Connection functions are currently
available for mutual TLS (mTLS) connections, where you can validate client certificates
and implement custom authentication logic beyond standard certificate validation. Connection
functions run during the TLS handshake process and can allow or deny connections based on
certificate properties, client IP addresses, or other criteria.

After you create and publish a connection function, make sure to add an
association for the _connection request_ event type
with an mTLS-enabled distribution. This makes the function run each time a client
attempts to establish an mTLS connection with CloudFront.

###### Example

The following pseudocode shows the structure of a connection function:

```
function connectionHandler(connection) {
    // Validate certificate and connection properties here.

    if (/* validation passes */) {
        connection.allow();
    } else {
        connection.deny();
    }
}
```

The function uses helper methods to determine whether to allow or deny the
connection. Unlike viewer request and viewer response functions, connection
functions cannot modify HTTP requests or responses.

## Related

information

For more information about working with CloudFront Functions, see the following
topics:

- [Event structure](functions-event-structure.md "functions-event-structure.md")
- [JavaScript runtime
  features](functions-javascript-runtime-features.md "functions-javascript-runtime-features.md")
- [CloudFront Functions examples](service_code_examples_cloudfront_functions_examples.md "service_code_examples_cloudfront_functions_examples.md")
- [Restrictions on edge functions](edge-functions-restrictions.md "edge-functions-restrictions.md")
