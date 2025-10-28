# Building a real-time

WebSocket client in AWS AppSync

###### Important

As of Mar 13, 2025, you can build a real-time PubSub API powered by WebSockets using
AWS AppSync Events. For more information, see [Publish events via WebSocket](../eventapi/publish-websocket.md "../eventapi/publish-websocket.md") in the _AWS AppSync Events
Developer Guide_..

AWS AppSync's real-time WebSocket client enables GraphQL subscriptions through a
multi-step process. The client first establishes a WebSocket connection with the
AWS AppSync real-time endpoint, sends a connection initialization message, and waits for
acknowledgment. After successful connection, the client registers subscriptions by
sending start messages with unique IDs and GraphQL queries. AWS AppSync confirms
successful subscriptions with acknowledgment messages. The client then listens for
subscription events, which are triggered by corresponding mutations. To maintain the
connection, AWS AppSync sends periodic keep-alive messages. When finished, the client
unregisters subscriptions by sending stop messages. This system supports multiple
subscriptions on a single WebSocket connection and accommodates various authorization
modes, including API keys, Amazon Cognito user pools, IAM, and Lambda.

## Real-time WebSocket client implementation for GraphQL subscriptions

The following sequence diagram and steps show the real-time subscriptions workflow
between the WebSocket client, HTTP client, and AWS AppSync.

![Sequence diagram showing WebSocket client, AppSync endpoints, and HTTP client interactions for real-time subscriptions.](images/realtime-client-flow.png)

1. The client establishes a WebSocket connection with the AWS AppSync real-time
   endpoint. If there is a network error, the client should do a jittered
   exponential backoff. For more information, see [Exponential
   backoff
   and
   jitter](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/ "https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/")
   on the AWS Architecture Blog.
2. (Optional) After successfully establishing the WebSocket connection, the
   client sends a `connection_init` message.
3. If `connection_init` is sent, the client waits for a
   `connection_ack` message from AWS AppSync. This message
   includes a `connectionTimeoutMs` parameter, which is the maximum
   wait time in milliseconds for a `"ka"` (keep-alive)
   message.
4. AWS AppSync sends `"ka"` messages periodically. The client keeps
   track of the time that it received each `"ka"` message. If the
   client doesn't receive a `"ka"` message within
   `connectionTimeoutMs` milliseconds, the client should close
   the connection.
5. The client registers the subscription by sending a `start`
   subscription message. A single WebSocket connection supports multiple
   subscriptions, even if they are in different authorization modes.
6. The client waits for AWS AppSync to send `start_ack` messages to
   confirm successful subscriptions. If there is an error, AWS AppSync returns a
   `"type": "error"` message.
7. The client listens for subscription events, which are sent after a
   corresponding mutation is called. Queries and mutations are usually sent
   through `https://` to the AWS AppSync GraphQL endpoint.
   Subscriptions flow through the AWS AppSync real-time endpoint using the secure
   WebSocket (`wss://`).
8. The client unregisters the subscription by sending a `stop`
   subscription message.
9. After unregistering all subscriptions and checking that there are no
   messages transferring through the WebSocket, the client can disconnect from
   the WebSocket connection.

## Handshake

details to establish the WebSocket connection

To connect and initiate a successful handshake with AWS AppSync, a WebSocket client
needs the following:

- The AWS AppSync real-time endpoint
- Headers – Contain information relevant to the AWS AppSync endpoint and
  authorization. AWS AppSync supports the following three methods for providing
  headers:
  - Headers via query string
    - The header information is encoded as a base64 string,
      derived from a stringified JSON object. This JSON object
      contains details relevant to the AWS AppSync endpoint and
      authorization. The content of the JSON object varies
      depending on the authorization mode.

  - Headers via `Sec-WebSocket-Protocol`
    - A base64Url-encoded string from the stringified JSON
      object that contains information relevant to the AWS AppSync
      endpoint and authorization is passed as the protocol in the
      `Sec-WebSocket-Protocol` header. The content
      of the JSON object varies depending on the authorization
      mode.

  - Headers via standard HTTP headers:
    - Headers can be passed as standard HTTP headers in the
      connection request, similar to how headers are passed for
      GraphQL queries and mutations to AWS AppSync. However, passing
      headers via standard HTTP headers is not supported for
      private API connection requests.

- `payload` – Base64-encoded string of `payload`.
  Payload is needed only if headers are provided using query string

With these requirements, a WebSocket client can connect to the URL, which contains
the real-time endpoint with the query string, using `graphql-ws` as the
WebSocket protocol.

### Discovering the real-time endpoint from the GraphQL endpoint

The AWS AppSync GraphQL endpoint and the AWS AppSync real-time endpoint are
slightly different in protocol and domain. You can retrieve the GraphQL endpoint
using the AWS Command Line Interface (AWS CLI) command `aws appsync
 get-graphql-api`.

\***\*AWS AppSync GraphQL endpoint:\*\***

`https://example1234567890000.appsync-api.us-east-1.amazonaws.com/graphql`

\***\*AWS AppSync real-time endpoint:\*\***

`wss://example1234567890000.appsync-realtime-api.us-east-1.amazonaws.com/graphql`

Applications can connect to the AWS AppSync GraphQL endpoint
(`https://`) using any HTTP client for queries and mutations.
Applications can connect to the AWS AppSync real-time endpoint
(`wss://`) using any WebSocket client for subscriptions.

With custom domain names, you can interact with both endpoints using a single
domain. For example, if you configure `api.example.com` as your
custom domain, you can interact with your GraphQL and real-time endpoints using
these URLs:

**AWS AppSync custom domain GraphQL
endpoint:**

`https://api.example.com/graphql`

**AWS AppSync custom domain real-time
endpoint:**

`wss://api.example.com/graphql/realtime`

## Header parameter format based on AWS AppSync API authorization mode

The format of the `header` object used in the connection query string
varies depending on the AWS AppSync API authorization mode. The `host`
field in the object refers to the AWS AppSync GraphQL endpoint, which is used to
validate the connection even if the `wss://` call is made against the
real-time endpoint. To initiate the handshake and establish the authorized
connection, the `payload` should be an empty JSON object. Payload is
needed only if headers are passed via query string.

The following sections demonstrate the header formats for each authorization
mode.

### API key

#### API key header

**Header contents**

- `"host": <string>`: The host for the AWS AppSync
  GraphQL endpoint or your custom domain name.
- `"x-api-key": <string>`: The API key configured for
  the AWS AppSync API.

**Example**

```
{
    "host":"example1234567890000.appsync-api.us-east-1.amazonaws.com",
    "x-api-key":"da2-12345678901234567890123456"
}
```

**Headers via query string**

First, a JSON object containing the `host` and the
`x-api-key` is converted into a string. Next, this string
is encoded using base64 encoding. The resulting base64-encoded string is
added as a query parameter named `header` to the WebSocket
URL for establishing the connection with the AWS AppSync real-time
endpoint. The resulting request URL takes the following form:

```
wss://example1234567890000.appsync-realtime-api.us-east-1.amazonaws.com/graphql?header=eyJob3N0IjoiZXhhbXBsZTEyMzQ1Njc4OTAwMDAuYXBwc3luYy1hcGkudXMtZWFzdC0xLmFtYXpvbmF3cy5jb20iLCJ4LWFtei1kYXRlIjoiMjAyMDA0MDFUMDAxMDEwWiIsIngtYXBpLWtleSI6ImRhMi16NHc0NHZoczV6Z2MzZHRqNXNranJsbGxqaSJ9&payload=e30=
```

It's important to note that in addition to the base64-encoded header
object, an empty JSON object {} is also base64-encoded and included as a
separate query parameter named `payload` in the WebSocket
URL.

**Headers via
`Sec-WebSocket-Protocol`**

A JSON object containing the `host` and the
`x-api-key` is converted to a string and then encoded using
base64Url encoding. The resulting base64Url-encoded string is prefixed with
`header-`. This prefixed string is then used as a new
sub-protocol in addition to `graphql-ws` in the
`Sec-WebSocket-Protocol` header when establishing the
WebSocket connection with the AWS AppSync real-time endpoint.

The resulting request URL takes the following form:

```
wss://example1234567890000.appsync-realtime-api.us-east-1.amazonaws.com/graphql
```

The `Sec-WebSocket-Protocol` header contains the following
value:

```
"sec-websocket-protocol" : ["graphql-ws", "header-ewogICAgImhvc3QiOiJleGFtcGxlMTIzNDU2Nzg5MDAwMC5hcHBzeW5jLWFwaS51cy1lYXN0LTEuYW1hem9uYXdzLmNvbSIsCiAgICAieC1hcGkta2V5IjoiZGEyLTEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Igp9"]
```

**Headers via standard HTTP
headers**

In this method, the host and API key information is transmitted using
standard HTTP headers when establishing the WebSocket connection with
the AWS AppSync real-time endpoint. The resulting request URL takes the
following form:

```
wss://example1234567890000.appsync-realtime-api.us-east-1.amazonaws.com/graphql
```

The request headers would include the following:

```
"sec-websocket-protocol" : ["graphql-ws"]
"host":"example1234567890000.appsync-api.us-east-1.amazonaws.com",
"x-api-key":"da2-12345678901234567890123456"
```

### Amazon Cognito user

pools and OpenID Connect (OIDC)

#### Amazon Cognito

and OIDCheader

Header contents:

- `"Authorization": <string>`: A JWT
  ID
  token.
  The header can use a [Bearer scheme](https://datatracker.ietf.org/doc/html/rfc6750#section-2.1 "https://datatracker.ietf.org/doc/html/rfc6750#section-2.1").
- `"host": <string>`: The host for the AWS AppSync
  GraphQL endpoint or your custom domain name.

Example:

```
{
    "Authorization":"eyEXAMPLEiJjbG5xb3A5eW5MK09QYXIrMTJHWEFLSXBieU5WNHhsQjEXAMPLEnM2WldvPSIsImFsZyI6IlEXAMPLEn0.eyEXAMPLEiJhNmNmMjcwNy0xNjgxLTQ1NDItOWYxOC1lNjY0MTg2NjlkMzYiLCJldmVudF9pZCI6ImVkMzM5MmNkLWNjYTMtNGM2OC1hNDYyLTJlZGI3ZTNmY2FjZiIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE1Njk0NTc3MTgsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC5hcC1zb3V0aGVhc3QtMi5hbWF6b25hd3MuY29tXC9hcC1zb3V0aGVhc3QtMl83OHY0SVZibVAiLCJleHAiOjE1Njk0NjEzMjAsImlhdCI6MTU2OTQ1NzcyMCwianRpIjoiNTgzZjhmYmMtMzk2MS00YzA4LWJhZTAtYzQyY2IxMTM5NDY5IiwiY2xpZW50X2lkIjoiM3FlajVlMXZmMzd1N3RoZWw0dG91dDJkMWwiLCJ1c2VybmFtZSI6ImVsb3EXAMPLEn0.B4EXAMPLEFNpJ6ikVp7e6DRee95V6Qi-zEE2DJH7sHOl2zxYi7f-SmEGoh2AD8emxQRYajByz-rE4Jh0QOymN2Ys-ZIkMpVBTPgu-TMWDyOHhDUmUj2OP82yeZ3wlZAtr_gM4LzjXUXmI_K2yGjuXfXTaa1mvQEBG0mQfVd7SfwXB-jcv4RYVi6j25qgow9Ew52ufurPqaK-3WAKG32KpV8J4-Wejq8t0c-yA7sb8EnB551b7TU93uKRiVVK3E55Nk5ADPoam_WYE45i3s5qVAP_-InW75NUoOCGTsS8YWMfb6ecHYJ-1j-bzA27zaT9VjctXn9byNFZmEXAMPLExw",
    "host":"example1234567890000.appsync-api.us-east-1.amazonaws.com"
}
```

**Headers via query string**

First, a JSON object containing the `host` and the
`Authorization` is converted into a string. Next, this
string is encoded using base64 encoding. The resulting base64-encoded
string is added as a query parameter named `header` to the
WebSocket URL for establishing the connection with the AWS AppSync
real-time endpoint. The resulting request URL takes the following
form:

```
wss://example1234567890000.appsync-realtime-api.us-east-1.amazonaws.com/graphql?header=eyJBdXRob3JpemF0aW9uIjoiZXlKcmFXUWlPaUpqYkc1eGIzQTVlVzVNSzA5UVlYSXJNVEpIV0VGTFNYQmllVTVXTkhoc1FqaFBWVzlZTW5NMldsZHZQU0lzSW1Gc1p5STZJbEpUTWpVMkluMC5leUp6ZFdJaU9pSmhObU5tTWpjd055MHhOamd4TFRRMU5ESXRPV1l4T0MxbE5qWTBNVGcyTmpsa016WWlMQ0psZG1WdWRGOXBaQ0k2SW1Wa016TTVNbU5rTFdOallUTXROR00yT0MxaE5EWXlMVEpsWkdJM1pUTm1ZMkZqWmlJc0luUnZhMlZ1WDNWelpTSTZJbUZqWTJWemN5SXNJbk5qYjNCbElqb2lZWGR6TG1OdloyNXBkRzh1YzJsbmJtbHVMblZ6WlhJdVlXUnRhVzRpTENKaGRYUm9YM1JwYldVaU9qRTFOamswTlRjM01UZ3NJbWx6Y3lJNkltaDBkSEJ6T2x3dlhDOWpiMmR1YVhSdkxXbGtjQzVoY0MxemIzVjBhR1ZoYzNRdE1pNWhiV0Y2YjI1aGQzTXVZMjl0WEM5aGNDMXpiM1YwYUdWaGMzUXRNbDgzT0hZMFNWWmliVkFpTENKbGVIQWlPakUxTmprME5qRXpNakFzSW1saGRDSTZNVFUyT1RRMU56Y3lNQ3dpYW5ScElqb2lOVGd6WmpobVltTXRNemsyTVMwMFl6QTRMV0poWlRBdFl6UXlZMkl4TVRNNU5EWTVJaXdpWTJ4cFpXNTBYMmxrSWpvaU0zRmxhalZsTVhabU16ZDFOM1JvWld3MGRHOTFkREprTVd3aUxDSjFjMlZ5Ym1GdFpTSTZJbVZzYjNKNllXWmxJbjAuQjRjZEp0aDNLRk5wSjZpa1ZwN2U2RFJlZTk1VjZRaS16RUUyREpIN3NIT2wyenhZaTdmLVNtRUdvaDJBRDhlbXhRUllhakJ5ei1yRTRKaDBRT3ltTjJZcy1aSWtNcFZCVFBndS1UTVdEeU9IaERVbVVqMk9QODJ5ZVozd2xaQXRyX2dNNEx6alhVWG1JX0syeUdqdVhmWFRhYTFtdlFFQkcwbVFmVmQ3U2Z3WEItamN2NFJZVmk2ajI1cWdvdzlFdzUydWZ1clBxYUstM1dBS0czMktwVjhKNC1XZWpxOHQwYy15QTdzYjhFbkI1NTFiN1RVOTN1S1JpVlZLM0U1NU5rNUFEUG9hbV9XWUU0NWkzczVxVkFQXy1Jblc3NU5Vb09DR1RzUzhZV01mYjZlY0hZSi0xai1iekEyN3phVDlWamN0WG45YnlORlptS0xwQTJMY3h3IiwiaG9zdCI6ImV4YW1wbGUxMjM0NTY3ODkwMDAwLmFwcHN5bmMtYXBpLnVzLWVhc3QtMS5hbWF6b25hd3MuY29tIn0=&payload=e30=
```

It's important to note that in addition to the base64-encoded header
object, an empty JSON object {} is also base64-encoded and included as a
separate query parameter named `payload` in the WebSocket
URL.

**Headers via
`Sec-WebSocket-Protocol`**

A JSON object containing the `host` and the
`Authorization` is converted to a string and then encoded
using base64Url encoding. The resulting base64Url-encoded string is
prefixed with `header-`. This prefixed string is then used as
a new sub-protocol in addition to `graphql-ws` in the
`Sec-WebSocket-Protocol` header when establishing the
WebSocket connection with the AWS AppSync real-time endpoint.

The resulting request URL takes the following form:

```
wss://example1234567890000.appsync-realtime-api.us-east-1.amazonaws.com/graphql
```

The `Sec-WebSocket-Protocol` header contains the following
value:

```
"sec-websocket-protocol" : ["graphql-ws", "header-ewogICAgImhvc3QiOiJleGFtcGxlMTIzNDU2Nzg5MDAwMC5hcHBzeW5jLWFwaS51cy1lYXN0LTEuYW1hem9uYXdzLmNvbSIsCiAgICAieC1hcGkta2V5IjoiZGEyLTEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Igp9"]
```

**Headers via standard HTTP
headers**

In this method, the host and Authorization information is transmitted
using standard HTTP headers when establishing the WebSocket connection
with the AWS AppSync real-time endpoint. The resulting request URL takes
the following form:

```
wss://example1234567890000.appsync-realtime-api.us-east-1.amazonaws.com/graphql
```

The request headers would include the following:

```
"sec-websocket-protocol" : ["graphql-ws"]
"Authorization":"eyEXAMPLEiJjbG5xb3A5eW5MK09QYXIrMTJHWEFLSXBieU5WNHhsQjEXAMPLEnM2WldvPSIsImFsZyI6IlEXAMPLEn0.eyEXAMPLEiJhNmNmMjcwNy0xNjgxLTQ1NDItOWYxOC1lNjY0MTg2NjlkMzYiLCJldmVudF9pZCI6ImVkMzM5MmNkLWNjYTMtNGM2OC1hNDYyLTJlZGI3ZTNmY2FjZiIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE1Njk0NTc3MTgsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC5hcC1zb3V0aGVhc3QtMi5hbWF6b25hd3MuY29tXC9hcC1zb3V0aGVhc3QtMl83OHY0SVZibVAiLCJleHAiOjE1Njk0NjEzMjAsImlhdCI6MTU2OTQ1NzcyMCwianRpIjoiNTgzZjhmYmMtMzk2MS00YzA4LWJhZTAtYzQyY2IxMTM5NDY5IiwiY2xpZW50X2lkIjoiM3FlajVlMXZmMzd1N3RoZWw0dG91dDJkMWwiLCJ1c2VybmFtZSI6ImVsb3EXAMPLEn0.B4EXAMPLEFNpJ6ikVp7e6DRee95V6Qi-zEE2DJH7sHOl2zxYi7f-SmEGoh2AD8emxQRYajByz-rE4Jh0QOymN2Ys-ZIkMpVBTPgu-TMWDyOHhDUmUj2OP82yeZ3wlZAtr_gM4LzjXUXmI_K2yGjuXfXTaa1mvQEBG0mQfVd7SfwXB-jcv4RYVi6j25qgow9Ew52ufurPqaK-3WAKG32KpV8J4-Wejq8t0c-yA7sb8EnB551b7TU93uKRiVVK3E55Nk5ADPoam_WYE45i3s5qVAP_-InW75NUoOCGTsS8YWMfb6ecHYJ-1j-bzA27zaT9VjctXn9byNFZmEXAMPLExw",
"host":"example1234567890000.appsync-api.us-east-1.amazonaws.com"
```

### IAM

#### IAM

header

**Header content**

- `"accept":
"application/json,
text/javascript"`: A constant `<string>`
  parameter.
- `"content-encoding":
"amz-1.0"`:
  A constant `<string>` parameter.
- `"content-type":
"application/json;
charset=UTF-8"`: A constant `<string>`
  parameter.
- `"host":
<string>`:
  This is the host for the AWS AppSync GraphQL endpoint.
  - `"x-amz-date":
<string>`:
    The timestamp must be in UTC and in the following ISO 8601
    format: YYYYMMDD'T'HHMMSS'Z'. For example, 20150830T123600Z
    is a valid timestamp. Do not include milliseconds in the
    timestamp. For more information, see [Handling dates in Signature Version 4](../../../general/latest/gr/sigv4-date-handling.md "../../../general/latest/gr/sigv4-date-handling.md") in the
    _AWS General Reference_.
  - `"X-Amz-Security-Token":
<string>`:
    The AWS session token, which is required when using
    temporary security credentials. For more information, see
    [Using temporary credentials with AWS
    resources](../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md "../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md") in the
    _IAM User Guide_.
  - `"Authorization":
<string>`:
    Signature Version 4 (SigV4) signing information for the
    AWS AppSync endpoint. For more information on the signing
    process, see [Task 4: Add the signature to the HTTP request](../../../general/latest/gr/sigv4-add-signature-to-request.md "../../../general/latest/gr/sigv4-add-signature-to-request.md")
    in the _AWS General Reference_.

The SigV4 signing HTTP request includes a canonical URL, which is the
AWS AppSync GraphQL endpoint with `/connect` appended. The service
endpoint AWS Region is same Region where you're using the AWS AppSync API,
and the service name is 'appsync'. The HTTP request to sign is the
following:

```
{
  url: "https://example1234567890000.appsync-api.us-east-1.amazonaws.com/graphql/connect",
  data: "{}",
  method: "POST",
  headers: {
    "accept": "application/json, text/javascript",
    "content-encoding": "amz-1.0",
    "content-type": "application/json; charset=UTF-8",
  }
}
```

**Example**

```
{
  "accept": "application/json, text/javascript",
  "content-encoding": "amz-1.0",
  "content-type": "application/json; charset=UTF-8",
  "host": "example1234567890000.appsync-api.us-east-1.amazonaws.com",
  "x-amz-date": "20200401T001010Z",
  "X-Amz-Security-Token": "AgEXAMPLEZ2luX2VjEAoaDmFwLXNvdXRoZWFEXAMPLEcwRQIgAh97Cljq7wOPL8KsxP3YtDuyc/9hAj8PhJ7Fvf38SgoCIQDhJEXAMPLEPspioOztj++pEagWCveZUjKEn0zyUhBEXAMPLEjj//////////8BEXAMPLExODk2NDgyNzg1NSIMo1mWnpESWUoYw4BkKqEFSrm3DXuL8w+ZbVc4JKjDP4vUCKNR6Le9C9pZp9PsW0NoFy3vLBUdAXEXAMPLEOVG8feXfiEEA+1khgFK/wEtwR+9zF7NaMMMse07wN2gG2tH0eKMEXAMPLEQX+sMbytQo8iepP9PZOzlZsSFb/dP5Q8hk6YEXAMPLEYcKZsTkDAq2uKFQ8mYUVA9EtQnNRiFLEY83aKvG/tqLWNnGlSNVx7SMcfovkFDqQamm+88y1OwwAEYK7qcoceX6Z7GGcaYuIfGpaX2MCCELeQvZ+8WxEgOnIfz7GYvsYNjLZSaRnV4G+ILY1F0QNW64S9Nvj+BwDg3ht2CrNvpwjVYlj9U3nmxE0UG5ne83LL5hhqMpm25kmL7enVgw2kQzmU2id4IKu0C/WaoDRuO2F5zE63vJbxN8AYs7338+4B4HBb6BZ6OUgg96Q15RA41/gIqxaVPxyTpDfTU5GfSLxocdYeniqqpFMtZG2n9d0u7GsQNcFkNcG3qDZm4tDo8tZbuym0a2VcF2E5hFEgXBa+XLJCfXi/77OqAEjP0x7Qdk3B43p8KG/BaioP5RsV8zBGvH1zAgyPha2rN70/tT13yrmPd5QYEfwzexjKrV4mWIuRg8NTHYSZJUaeyCwTom80VFUJXG+GYTUyv5W22aBcnoRGiCiKEYTLOkgXecdKFTHmcIAejQ9Welr0a196Kq87w5KNMCkcCGFnwBNFLmfnbpNqT6rUBxxs3X5ntX9d8HVtSYINTsGXXMZCJ7fnbWajhg/aox0FtHX21eF6qIGT8j1z+l2opU+ggwUgkhUUgCH2TfqBj+MLMVVvpgqJsPKt582caFKArIFIvO+9QupxLnEH2hz04TMTfnU6bQC6z1buVe7h+tOLnh1YPFsLQ88anib/7TTC8k9DsBTq0ASe8R2GbSEsmO9qbbMwgEaYUhOKtGeyQsSJdhSk6XxXThrWL9EnwBCXDkICMqdntAxyyM9nWsZ4bL9JHqExgWUmfWChzPFAqn3F4y896UqHTZxlq3WGypn5HHcem2Hqf3IVxKH1inhqdVtkryEiTWrI7ZdjbqnqRbl+WgtPtKOOweDlCaRs3R2qXcbNgVhleMk4IWnF8D1695AenU1LwHjOJLkCjxgNFiWAFEPH9aEXAMPLExA==",
  "Authorization": "AWS4-HMAC-SHA256 Credential=XXXXXXXXXXXXXXXXXXX/20200401/us-east-1/appsync/aws4_request, SignedHeaders=accept;content-encoding;content-type;host;x-amz-date;x-amz-security-token, Signature=83EXAMPLEbcc1fe3ee69f75cd5ebbf4cb4f150e4f99cec869f149c5EXAMPLEdc"
}
```

**Headers via query string**

First, a JSON object containing the `host` (AWS AppSync GraphQL
endpoint) and the other authorization
headers
is converted
to
a string. Next, this string is encoded using base64 encoding. The resulting
base64-encoded string is added to the WebSocket URL
as a
query parameter named `header`.
The
resulting request URL takes the following form:

```
wss://example1234567890000.appsync-realtime-api.us-east-1.amazonaws.com/graphql?header=eyJBdXRob3JpemF0aW9uIjoiZXlKcmFXUWlPaUpqYkc1eGIzQTVlVzVNSzA5UVlYSXJNVEpIV0VGTFNYQmllVTVXTkhoc1FqaFBWVzlZTW5NMldsZHZQU0lzSW1Gc1p5STZJbEpUTWpVMkluMC5leUp6ZFdJaU9pSmhObU5tTWpjd055MHhOamd4TFRRMU5ESXRPV1l4T0MxbE5qWTBNVGcyTmpsa016WWlMQ0psZG1WdWRGOXBaQ0k2SW1Wa016TTVNbU5rTFdOallUTXROR00yT0MxaE5EWXlMVEpsWkdJM1pUTm1ZMkZqWmlJc0luUnZhMlZ1WDNWelpTSTZJbUZqWTJWemN5SXNJbk5qYjNCbElqb2lZWGR6TG1OdloyNXBkRzh1YzJsbmJtbHVMblZ6WlhJdVlXUnRhVzRpTENKaGRYUm9YM1JwYldVaU9qRTFOamswTlRjM01UZ3NJbWx6Y3lJNkltaDBkSEJ6T2x3dlhDOWpiMmR1YVhSdkxXbGtjQzVoY0MxemIzVjBhR1ZoYzNRdE1pNWhiV0Y2YjI1aGQzTXVZMjl0WEM5aGNDMXpiM1YwYUdWaGMzUXRNbDgzT0hZMFNWWmliVkFpTENKbGVIQWlPakUxTmprME5qRXpNakFzSW1saGRDSTZNVFUyT1RRMU56Y3lNQ3dpYW5ScElqb2lOVGd6WmpobVltTXRNemsyTVMwMFl6QTRMV0poWlRBdFl6UXlZMkl4TVRNNU5EWTVJaXdpWTJ4cFpXNTBYMmxrSWpvaU0zRmxhalZsTVhabU16ZDFOM1JvWld3MGRHOTFkREprTVd3aUxDSjFjMlZ5Ym1GdFpTSTZJbVZzYjNKNllXWmxJbjAuQjRjZEp0aDNLRk5wSjZpa1ZwN2U2RFJlZTk1VjZRaS16RUUyREpIN3NIT2wyenhZaTdmLVNtRUdvaDJBRDhlbXhRUllhakJ5ei1yRTRKaDBRT3ltTjJZcy1aSWtNcFZCVFBndS1UTVdEeU9IaERVbVVqMk9QODJ5ZVozd2xaQXRyX2dNNEx6alhVWG1JX0syeUdqdVhmWFRhYTFtdlFFQkcwbVFmVmQ3U2Z3WEItamN2NFJZVmk2ajI1cWdvdzlFdzUydWZ1clBxYUstM1dBS0czMktwVjhKNC1XZWpxOHQwYy15QTdzYjhFbkI1NTFiN1RVOTN1S1JpVlZLM0U1NU5rNUFEUG9hbV9XWUU0NWkzczVxVkFQXy1Jblc3NU5Vb09DR1RzUzhZV01mYjZlY0hZSi0xai1iekEyN3phVDlWamN0WG45YnlORlptS0xwQTJMY3h3IiwiaG9zdCI6ImV4YW1wbGUxMjM0NTY3ODkwMDAwLmFwcHN5bmMtYXBpLnVzLWVhc3QtMS5hbWF6b25hd3MuY29tIn0=&payload=e30=
```

It's important to note that in addition to the base64-encoded header
object, an empty JSON object {} is also base64-encoded and included as a
separate query parameter named `payload` in the WebSocket
URL.

**Headers via
`Sec-WebSocket-Protocol`**

A JSON object containing the `host` and the other authorization
headers is converted to a string and then encoded using base64Url encoding.
The resulting base64Url-encoded string is prefixed with
`header-`. This prefixed string is then used as a new
sub-protocol in addition to `graphql-ws` in the
`Sec-WebSocket-Protocol` header when establishing the
WebSocket connection with the AWS AppSync real-time endpoint.

The resulting request URL takes the following form:

```
wss://example1234567890000.appsync-realtime-api.us-east-1.amazonaws.com/graphql
```

The `Sec-WebSocket-Protocol` header contains the following
value:

```
"sec-websocket-protocol" : ["graphql-ws", "header-ew0KICAiYWNjZXB0IjogImFwcGxpY2F0aW9uL2pzb24sIHRleHQvamF2YXNjcmlwdCIsDQogICJjb250ZW50LWVuY29kaW5nIjogImFtei0xLjAiLA0KICAiY29udGVudC10eXBlIjogImFwcGxpY2F0aW9uL2pzb247IGNoYXJzZXQ9VVRGLTgiLA0KICAiaG9zdCI6ICJleGFtcGxlMTIzNDU2Nzg5MDAwMC5hcHBzeW5jLWFwaS51cy1lYXN0LTEuYW1hem9uYXdzLmNvbSIsDQogICJ4LWFtei1kYXRlIjogIjIwMjAwNDAxVDAwMTAxMFoiLA0KICAiWC1BbXotU2VjdXJpdHktVG9rZW4iOiAiQWdFWEFNUExFWjJsdVgyVmpFQW9hRG1Gd0xYTnZkWFJvWldGRVhBTVBMRWN3UlFJZ0FoOTdDbGpxN3dPUEw4S3N4UDNZdER1eWMvOWhBajhQaEo3RnZmMzhTZ29DSVFEaEpFWEFNUExFUHNwaW9PenRqKytwRWFnV0N2ZVpVaktFbjB6eVVoQkVYQU1QTEVqai8vLy8vLy8vLy84QkVYQU1QTEV4T0RrMk5EZ3lOemcxTlNJTW8xbVducEVTV1VvWXc0QmtLcUVGU3JtM0RYdUw4dytaYlZjNEpLakRQNHZVQ0tOUjZMZTlDOXBacDlQc1cwTm9GeTN2TEJVZEFYRVhBTVBMRU9WRzhmZVhmaUVFQSsxa2hnRksvd0V0d1IrOXpGN05hTU1Nc2UwN3dOMmdHMnRIMGVLTUVYQU1QTEVRWCtzTWJ5dFFvOGllcFA5UFpPemxac1NGYi9kUDVROGhrNllFWEFNUExFWWNLWnNUa0RBcTJ1S0ZROG1ZVVZBOUV0UW5OUmlGTEVZODNhS3ZHL3RxTFdObkdsU05WeDdTTWNmb3ZrRkRxUWFtbSs4OHkxT3d3QUVZSzdxY29jZVg2WjdHR2NhWXVJZkdwYVgyTUNDRUxlUXZaKzhXeEVnT25JZno3R1l2c1lOakxaU2FSblY0RytJTFkxRjBRTlc2NFM5TnZqK0J3RGczaHQyQ3JOdnB3alZZbGo5VTNubXhFMFVHNW5lODNMTDVoaHFNcG0yNWttTDdlblZndzJrUXptVTJpZDRJS3UwQy9XYW9EUnVPMkY1ekU2M3ZKYnhOOEFZczczMzgrNEI0SEJiNkJaNk9VZ2c5NlExNVJBNDEvZ0lxeGFWUHh5VHBEZlRVNUdmU0x4b2NkWWVuaXFxcEZNdFpHMm45ZDB1N0dzUU5jRmtOY0czcURabTR0RG84dFpidXltMGEyVmNGMkU1aEZFZ1hCYStYTEpDZlhpLzc3T3FBRWpQMHg3UWRrM0I0M3A4S0cvQmFpb1A1UnNWOHpCR3ZIMXpBZ3lQaGEyck43MC90VDEzeXJtUGQ1UVlFZnd6ZXhqS3JWNG1XSXVSZzhOVEhZU1pKVWFleUN3VG9tODBWRlVKWEcrR1lUVXl2NVcyMmFCY25vUkdpQ2lLRVlUTE9rZ1hlY2RLRlRIbWNJQWVqUTlXZWxyMGExOTZLcTg3dzVLTk1Da2NDR0Zud0JORkxtZm5icE5xVDZyVUJ4eHMzWDVudFg5ZDhIVnRTWUlOVHNHWFhNWkNKN2ZuYldhamhnL2FveDBGdEhYMjFlRjZxSUdUOGoxeitsMm9wVStnZ3dVZ2toVVVnQ0gyVGZxQmorTUxNVlZ2cGdxSnNQS3Q1ODJjYUZLQXJJRkl2Tys5UXVweExuRUgyaHowNFRNVGZuVTZiUUM2ejFidVZlN2grdE9MbmgxWVBGc0xRODhhbmliLzdUVEM4azlEc0JUcTBBU2U4UjJHYlNFc21POXFiYk13Z0VhWVVoT0t0R2V5UXNTSmRoU2s2WHhYVGhyV0w5RW53QkNYRGtJQ01xZG50QXh5eU05bldzWjRiTDlKSHFFeGdXVW1mV0NoelBGQXFuM0Y0eTg5NlVxSFRaeGxxM1dHeXBuNUhIY2VtMkhxZjNJVnhLSDFpbmhxZFZ0a3J5RWlUV3JJN1pkamJxbnFSYmwrV2d0UHRLT093ZURsQ2FSczNSMnFYY2JOZ1ZobGVNazRJV25GOEQxNjk1QWVuVTFMd0hqT0pMa0NqeGdORmlXQUZFUEg5YUVYQU1QTEV4QT09IiwNCiAgIkF1dGhvcml6YXRpb24iOiAiQVdTNC1ITUFDLVNIQTI1NiBDcmVkZW50aWFsPVhYWFhYWFhYWFhYWFhYWFhYWFgvMjAyMDA0MDEvdXMtZWFzdC0xL2FwcHN5bmMvYXdzNF9yZXF1ZXN0LCBTaWduZWRIZWFkZXJzPWFjY2VwdDtjb250ZW50LWVuY29kaW5nO2NvbnRlbnQtdHlwZTtob3N0O3gtYW16LWRhdGU7eC1hbXotc2VjdXJpdHktdG9rZW4sIFNpZ25hdHVyZT04M0VYQU1QTEViY2MxZmUzZWU2OWY3NWNkNWViYmY0Y2I0ZjE1MGU0Zjk5Y2VjODY5ZjE0OWM1RVhBTVBMRWRjIg0KfQ"]
```

**Headers via standard HTTP headers**

In this method, the host and the other
authorization
information is transmitted using standard HTTP headers when establishing the
WebSocket connection with the AWS AppSync real-time endpoint. The resulting
request URL takes the following form:

```
wss://example1234567890000.appsync-realtime-api.us-east-1.amazonaws.com/graphql
```

The request headers would include the following:

```
"sec-websocket-protocol" : ["graphql-ws"]
"accept": "application/json, text/javascript",
"content-encoding": "amz-1.0",
"content-type": "application/json; charset=UTF-8",
"host": "example1234567890000.appsync-api.us-east-1.amazonaws.com",
"x-amz-date": "20200401T001010Z",
"X-Amz-Security-Token": "AgEXAMPLEZ2luX2VjEAoaDmFwLXNvdXRoZWFEXAMPLEcwRQIgAh97Cljq7wOPL8KsxP3YtDuyc/9hAj8PhJ7Fvf38SgoCIQDhJEXAMPLEPspioOztj++pEagWCveZUjKEn0zyUhBEXAMPLEjj//////////8BEXAMPLExODk2NDgyNzg1NSIMo1mWnpESWUoYw4BkKqEFSrm3DXuL8w+ZbVc4JKjDP4vUCKNR6Le9C9pZp9PsW0NoFy3vLBUdAXEXAMPLEOVG8feXfiEEA+1khgFK/wEtwR+9zF7NaMMMse07wN2gG2tH0eKMEXAMPLEQX+sMbytQo8iepP9PZOzlZsSFb/dP5Q8hk6YEXAMPLEYcKZsTkDAq2uKFQ8mYUVA9EtQnNRiFLEY83aKvG/tqLWNnGlSNVx7SMcfovkFDqQamm+88y1OwwAEYK7qcoceX6Z7GGcaYuIfGpaX2MCCELeQvZ+8WxEgOnIfz7GYvsYNjLZSaRnV4G+ILY1F0QNW64S9Nvj+BwDg3ht2CrNvpwjVYlj9U3nmxE0UG5ne83LL5hhqMpm25kmL7enVgw2kQzmU2id4IKu0C/WaoDRuO2F5zE63vJbxN8AYs7338+4B4HBb6BZ6OUgg96Q15RA41/gIqxaVPxyTpDfTU5GfSLxocdYeniqqpFMtZG2n9d0u7GsQNcFkNcG3qDZm4tDo8tZbuym0a2VcF2E5hFEgXBa+XLJCfXi/77OqAEjP0x7Qdk3B43p8KG/BaioP5RsV8zBGvH1zAgyPha2rN70/tT13yrmPd5QYEfwzexjKrV4mWIuRg8NTHYSZJUaeyCwTom80VFUJXG+GYTUyv5W22aBcnoRGiCiKEYTLOkgXecdKFTHmcIAejQ9Welr0a196Kq87w5KNMCkcCGFnwBNFLmfnbpNqT6rUBxxs3X5ntX9d8HVtSYINTsGXXMZCJ7fnbWajhg/aox0FtHX21eF6qIGT8j1z+l2opU+ggwUgkhUUgCH2TfqBj+MLMVVvpgqJsPKt582caFKArIFIvO+9QupxLnEH2hz04TMTfnU6bQC6z1buVe7h+tOLnh1YPFsLQ88anib/7TTC8k9DsBTq0ASe8R2GbSEsmO9qbbMwgEaYUhOKtGeyQsSJdhSk6XxXThrWL9EnwBCXDkICMqdntAxyyM9nWsZ4bL9JHqExgWUmfWChzPFAqn3F4y896UqHTZxlq3WGypn5HHcem2Hqf3IVxKH1inhqdVtkryEiTWrI7ZdjbqnqRbl+WgtPtKOOweDlCaRs3R2qXcbNgVhleMk4IWnF8D1695AenU1LwHjOJLkCjxgNFiWAFEPH9aEXAMPLExA==",
"Authorization": "AWS4-HMAC-SHA256 Credential=XXXXXXXXXXXXXXXXXXX/20200401/us-east-1/appsync/aws4_request, SignedHeaders=accept;content-encoding;content-type;host;x-amz-date;x-amz-security-token, Signature=83EXAMPLEbcc1fe3ee69f75cd5ebbf4cb4f150e4f99cec869f149c5EXAMPLEdc"
```

To sign the request using a custom domain:

```
{
  url: "https://api.example.com/graphql/connect",
  data: "{}",
  method: "POST",
  headers: {
    "accept": "application/json, text/javascript",
    "content-encoding": "amz-1.0",
    "content-type": "application/json; charset=UTF-8",
  }
}
```

**Example**

```
{
  "accept": "application/json, text/javascript",
  "content-encoding": "amz-1.0",
  "content-type": "application/json; charset=UTF-8",
  "host": "api.example.com",
  "x-amz-date": "20200401T001010Z",
  "X-Amz-Security-Token": "AgEXAMPLEZ2luX2VjEAoaDmFwLXNvdXRoZWFEXAMPLEcwRQIgAh97Cljq7wOPL8KsxP3YtDuyc/9hAj8PhJ7Fvf38SgoCIQDhJEXAMPLEPspioOztj++pEagWCveZUjKEn0zyUhBEXAMPLEjj//////////8BEXAMPLExODk2NDgyNzg1NSIMo1mWnpESWUoYw4BkKqEFSrm3DXuL8w+ZbVc4JKjDP4vUCKNR6Le9C9pZp9PsW0NoFy3vLBUdAXEXAMPLEOVG8feXfiEEA+1khgFK/wEtwR+9zF7NaMMMse07wN2gG2tH0eKMEXAMPLEQX+sMbytQo8iepP9PZOzlZsSFb/dP5Q8hk6YEXAMPLEYcKZsTkDAq2uKFQ8mYUVA9EtQnNRiFLEY83aKvG/tqLWNnGlSNVx7SMcfovkFDqQamm+88y1OwwAEYK7qcoceX6Z7GGcaYuIfGpaX2MCCELeQvZ+8WxEgOnIfz7GYvsYNjLZSaRnV4G+ILY1F0QNW64S9Nvj+BwDg3ht2CrNvpwjVYlj9U3nmxE0UG5ne83LL5hhqMpm25kmL7enVgw2kQzmU2id4IKu0C/WaoDRuO2F5zE63vJbxN8AYs7338+4B4HBb6BZ6OUgg96Q15RA41/gIqxaVPxyTpDfTU5GfSLxocdYeniqqpFMtZG2n9d0u7GsQNcFkNcG3qDZm4tDo8tZbuym0a2VcF2E5hFEgXBa+XLJCfXi/77OqAEjP0x7Qdk3B43p8KG/BaioP5RsV8zBGvH1zAgyPha2rN70/tT13yrmPd5QYEfwzexjKrV4mWIuRg8NTHYSZJUaeyCwTom80VFUJXG+GYTUyv5W22aBcnoRGiCiKEYTLOkgXecdKFTHmcIAejQ9Welr0a196Kq87w5KNMCkcCGFnwBNFLmfnbpNqT6rUBxxs3X5ntX9d8HVtSYINTsGXXMZCJ7fnbWajhg/aox0FtHX21eF6qIGT8j1z+l2opU+ggwUgkhUUgCH2TfqBj+MLMVVvpgqJsPKt582caFKArIFIvO+9QupxLnEH2hz04TMTfnU6bQC6z1buVe7h+tOLnh1YPFsLQ88anib/7TTC8k9DsBTq0ASe8R2GbSEsmO9qbbMwgEaYUhOKtGeyQsSJdhSk6XxXThrWL9EnwBCXDkICMqdntAxyyM9nWsZ4bL9JHqExgWUmfWChzPFAqn3F4y896UqHTZxlq3WGypn5HHcem2Hqf3IVxKH1inhqdVtkryEiTWrI7ZdjbqnqRbl+WgtPtKOOweDlCaRs3R2qXcbNgVhleMk4IWnF8D1695AenU1LwHjOJLkCjxgNFiWAFEPH9aEXAMPLExA==",
  "Authorization": "AWS4-HMAC-SHA256 Credential=XXXXXXXXXXXXXXXXXXX/20200401/us-east-1/appsync/aws4_request, SignedHeaders=accept;content-encoding;content-type;host;x-amz-date;x-amz-security-token, Signature=83EXAMPLEbcc1fe3ee69f75cd5ebbf4cb4f150e4f99cec869f149c5EXAMPLEdc"
}
```

**Request URL with query
string**

```
wss://api.example.com/graphql?header=eyEXAMPLEHQiOiJhcHBsaWNhdGlvbi9qc29uLCB0ZXh0L2phdmFEXAMPLEQiLCJjb250ZW50LWVuY29kaW5nIjoEXAMPLEEuMCIsImNvbnRlbnQtdHlwZSI6ImFwcGxpY2F0aW9EXAMPLE47IGNoYXJzZXQ9VVRGLTgiLCJob3N0IjoiZXhhbXBsZEXAMPLENjc4OTAwMDAuYXBwc3luYy1hcGkudXMtZWFzdC0xLmFtYEXAMPLEcy5jb20iLCJ4LWFtei1kYXRlIjoiMjAyMDA0MDFUMDAxMDEwWiIsIlgtEXAMPLElY3VyaXR5LVRva2VuIjoiQWdvSmIzSnBaMmx1WDJWakVBb2FEbUZ3TFhOdmRYUm9aV0Z6ZEMweUlrY3dSUUlnQWg5N0NsanE3d09QTDhLc3hQM1l0RHV5Yy85aEFqOFBoSjdGdmYzOFNnb0NJUURoSllKYkpsbmpQc3Bpb096dGorK3BFYWdXQ3ZlWlVqS0VuMHp5VWhCbXhpck5CUWpqLy8vLy8vLy8vLzhCRUFBYUREY3hPRGsyTkRneU56ZzFOU0lNbzFtV25wRVNXVW9ZdzRCa0txRUZTcm0zRFh1TDh3K1piVmM0SktqRFA0dlVDS05SNkxlOUM5cFpwOVBzVzBOb0Z5M3ZMQlVkQVh3dDZQSld1T1ZHOGZlWGZpRUVBKzFraGdGSy93RXR3Uis5ekY3TmFNTU1zZTA3d04yZ0cydEgwZUtNVFhuOEF3QVFYK3NNYnl0UW84aWVwUDlQWk96bFpzU0ZiL2RQNVE4aGs2WWpHVGFMMWVZY0tac1RrREFxMnVLRlE4bVlVVkE5RXRRbk5SaUZMRVk4M2FLdkcvdHFMV05uR2xTTlZ4N1NNY2ZvdmtGRHFRYW1tKzg4eTFPd3dBRVlLN3Fjb2NlWDZaN0dHY2FZdUlmR3BhWDJNQ0NFTGVRdlorOFd4RWdPbklmejdHWXZzWU5qTFpTYVJuVjRHK0lMWTFGMFFOVzY0UzlOdmorQndEZzNodDJDck52cHdqVllsajlVM25teEUwVUc1bmU4M0xMNWhocU1wbTI1a21MN2VuVmd3MmtRem1VMmlkNElLdTBDL1dhb0RSdU8yRjV6RTYzdkpieE44QVlzNzMzOCs0QjRIQmI2Qlo2T1VnZzk2UTE1UkE0MS9nSXF4YVZQeHlUcERmVFU1R2ZTTHhvY2RZZW5pcXFwRk10WkcybjlkMHU3R3NRTmNGa05jRzNxRFptNHREbzh0WmJ1eW0wYTJWY0YyRTVoRkVnWEJhK1hMSkNmWGkvNzdPcUFFalAweDdRZGszQjQzcDhLRy9CYWlvUDVSc1Y4ekJHdkgxekFneVBoYTJyTjcwL3RUMTN5cm1QZDVRWUVmd3pleGpLclY0bVdJdVJnOE5USFlTWkpVYWV5Q3dUb204MFZGVUpYRytHWVRVeXY1VzIyYUJjbm9SR2lDaUtFWVRMT2tnWGVjZEtGVEhtY0lBZWpROVdlbHIwYTE5NktxODd3NUtOTUNrY0NHRm53Qk5GTG1mbmJwTnFUNnJVQnh4czNYNW50WDlkOEhWdFNZSU5Uc0dYWE1aQ0o3Zm5iV2FqaGcvYW94MEZ0SFgyMWVGNnFJR1Q4ajF6K2wyb3BVK2dnd1Vna2hVVWdDSDJUZnFCaitNTE1WVnZwZ3FKc1BLdDU4MmNhRktBcklGSXZPKzlRdXB4TG5FSDJoejA0VE1UZm5VNmJRQzZ6MWJ1VmU3aCt0T0xuaDFZUEZzTFE4OGFuaWIvN1RUQzhrOURzQlRxMEFTZThSMkdiU0VzbU85cWJiTXdnRWFZVWhPS3RHZXlRc1NKZGhTazZYeFhUaHJXTDlFbndCQ1hEa0lDTXFkbnRBeHl5TTluV3NaNGJMOUpIcUV4Z1dVbWZXQ2h6UEZBcW4zRjR5ODk2VXFIVFp4bHEzV0d5cG41SEhjZW0ySHFmM0lWeEtIMWluaHFkVnRrcnlFaVRXckk3WmRqYnFucVJibCtXZ3RQdEtPT3dlRGxDYVJzM1IycVhjYk5nVmhsZU1rNElXbkY4RDE2OTVBZW5VMUx3SGpPSkxrQ2p4Z05GaVdBRkVQSDlhTklhcXMvWnhBPT0iLCJBdXRob3JpemF0aW9uIjoiQVdTNC1ITUFDLVNIQTI1NiBDcmVkZW50aWFsPVhYWFhYWFhYWFhYWFhYWFhYWFgvMjAxOTEwMDIvdXMtZWFzdC0xEXAMPLE5bmMvYXdzNF9yZXF1ZXN0LCBTaWduZWRIZWFkZXJzPWFjY2VwdDtjb250ZWEXAMPLE29kaW5nO2NvbnRlbnQtdHlwZTtob3EXAMPLEW16LWRhdGU7eC1hbXotc2VjdXJpdHktdG9rZW4sIFNpZ25hdHVyZT04MzE4EXAMPLEiY2MxZmUzZWU2OWY3NWNkEXAMPLE0Y2I0ZjE1MGU0Zjk5Y2VjODY5ZjE0OWM1ZDAzNDEXAMPLEn0=&payload=e30=
```

###### Note

One WebSocket connection can have multiple subscriptions (even with
different authentication modes). One way to implement this is to create
a WebSocket connection for the first subscription and then close it when
the last subscription is unregistered. You can optimize this by waiting
a few seconds before closing the WebSocket connection, in case the app
is subscribed immediately after the last subscription is unregistered.
For a mobile app example, when changing from one screen to another, on
_unmounting_ event it stops a subscription, and
on _mounting_ event it starts a different
subscription.

### Lambda authorization

#### Lambda

authorization header

**Header content**

- `"Authorization": <string>`: The value that is
  passed as `authorizationToken`.
- `"host": <string>`: The host for the AWS AppSync
  GraphQL
  endpoint
  or your custom domain name.

**Example**

```
{
    "Authorization":"M0UzQzM1MkQtMkI0Ni00OTZCLUI1NkQtMUM0MTQ0QjVBRTczCkI1REEzRTIxLTk5NzItNDJENi1BQjMwLTFCNjRFNzQ2NzlCNQo=",
    "host":"example1234567890000.appsync-api.us-east-1.amazonaws.com"
}
```

**Headers via query string**

First, a JSON object containing the `host` and the
`Authorization` is converted into a string. Next, this
string is encoded using base64 encoding. The resulting base64-encoded
string is added as a query parameter named `header` to the
WebSocket URL for establishing the connection with the AWS AppSync
real-time endpoint. The resulting request URL takes the following
form:

```
wss://example1234567890000.appsync-realtime-api.us-east-1.amazonaws.com/graphql?header=eyJBdXRob3JpemF0aW9uIjoiZXlKcmFXUWlPaUpqYkc1eGIzQTVlVzVNSzA5UVlYSXJNVEpIV0VGTFNYQmllVTVXTkhoc1FqaFBWVzlZTW5NMldsZHZQU0lzSW1Gc1p5STZJbEpUTWpVMkluMC5leUp6ZFdJaU9pSmhObU5tTWpjd055MHhOamd4TFRRMU5ESXRPV1l4T0MxbE5qWTBNVGcyTmpsa016WWlMQ0psZG1WdWRGOXBaQ0k2SW1Wa016TTVNbU5rTFdOallUTXROR00yT0MxaE5EWXlMVEpsWkdJM1pUTm1ZMkZqWmlJc0luUnZhMlZ1WDNWelpTSTZJbUZqWTJWemN5SXNJbk5qYjNCbElqb2lZWGR6TG1OdloyNXBkRzh1YzJsbmJtbHVMblZ6WlhJdVlXUnRhVzRpTENKaGRYUm9YM1JwYldVaU9qRTFOamswTlRjM01UZ3NJbWx6Y3lJNkltaDBkSEJ6T2x3dlhDOWpiMmR1YVhSdkxXbGtjQzVoY0MxemIzVjBhR1ZoYzNRdE1pNWhiV0Y2YjI1aGQzTXVZMjl0WEM5aGNDMXpiM1YwYUdWaGMzUXRNbDgzT0hZMFNWWmliVkFpTENKbGVIQWlPakUxTmprME5qRXpNakFzSW1saGRDSTZNVFUyT1RRMU56Y3lNQ3dpYW5ScElqb2lOVGd6WmpobVltTXRNemsyTVMwMFl6QTRMV0poWlRBdFl6UXlZMkl4TVRNNU5EWTVJaXdpWTJ4cFpXNTBYMmxrSWpvaU0zRmxhalZsTVhabU16ZDFOM1JvWld3MGRHOTFkREprTVd3aUxDSjFjMlZ5Ym1GdFpTSTZJbVZzYjNKNllXWmxJbjAuQjRjZEp0aDNLRk5wSjZpa1ZwN2U2RFJlZTk1VjZRaS16RUUyREpIN3NIT2wyenhZaTdmLVNtRUdvaDJBRDhlbXhRUllhakJ5ei1yRTRKaDBRT3ltTjJZcy1aSWtNcFZCVFBndS1UTVdEeU9IaERVbVVqMk9QODJ5ZVozd2xaQXRyX2dNNEx6alhVWG1JX0syeUdqdVhmWFRhYTFtdlFFQkcwbVFmVmQ3U2Z3WEItamN2NFJZVmk2ajI1cWdvdzlFdzUydWZ1clBxYUstM1dBS0czMktwVjhKNC1XZWpxOHQwYy15QTdzYjhFbkI1NTFiN1RVOTN1S1JpVlZLM0U1NU5rNUFEUG9hbV9XWUU0NWkzczVxVkFQXy1Jblc3NU5Vb09DR1RzUzhZV01mYjZlY0hZSi0xai1iekEyN3phVDlWamN0WG45YnlORlptS0xwQTJMY3h3IiwiaG9zdCI6ImV4YW1wbGUxMjM0NTY3ODkwMDAwLmFwcHN5bmMtYXBpLnVzLWVhc3QtMS5hbWF6b25hd3MuY29tIn0=&payload=e30=
```

It's important to note that in addition to the base64-encoded header
object, an empty JSON object {} is also base64-encoded and included as a
separate query parameter named `payload` in the WebSocket
URL.

**Headers via
`Sec-WebSocket-Protocol`**

A JSON object containing the `host` and the
`Authorization` is converted to a string and then encoded
using base64Url encoding. The resulting base64Url-encoded string is
prefixed with `header-`. This prefixed string is then used as
a new sub-protocol in addition to `graphql-ws` in the
`Sec-WebSocket-Protocol` header when establishing the
WebSocket connection with the AWS AppSync real-time endpoint.

The resulting request URL takes the following form:

```
wss://example1234567890000.appsync-realtime-api.us-east-1.amazonaws.com/graphql
```

The `Sec-WebSocket-Protocol` header contains the following
value:

```
"sec-websocket-protocol" : ["graphql-ws", "header-ewogICAgImhvc3QiOiJleGFtcGxlMTIzNDU2Nzg5MDAwMC5hcHBzeW5jLWFwaS51cy1lYXN0LTEuYW1hem9uYXdzLmNvbSIsCiAgICAieC1hcGkta2V5IjoiZGEyLTEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Igp9"]
```

**Headers via standard HTTP
headers**

In this method, the host and Authorization information is transmitted
using standard HTTP headers when establishing the WebSocket connection
with the AWS AppSync real-time endpoint. The resulting request URL takes
the following form:

```
wss://example1234567890000.appsync-realtime-api.us-east-1.amazonaws.com/graphql
```

The request headers would include the following:

```
"sec-websocket-protocol" : ["graphql-ws"]
"Authorization":"eyEXAMPLEiJjbG5xb3A5eW5MK09QYXIrMTJHWEFLSXBieU5WNHhsQjEXAMPLEnM2WldvPSIsImFsZyI6IlEXAMPLEn0.eyEXAMPLEiJhNmNmMjcwNy0xNjgxLTQ1NDItOWYxOC1lNjY0MTg2NjlkMzYiLCJldmVudF9pZCI6ImVkMzM5MmNkLWNjYTMtNGM2OC1hNDYyLTJlZGI3ZTNmY2FjZiIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE1Njk0NTc3MTgsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC5hcC1zb3V0aGVhc3QtMi5hbWF6b25hd3MuY29tXC9hcC1zb3V0aGVhc3QtMl83OHY0SVZibVAiLCJleHAiOjE1Njk0NjEzMjAsImlhdCI6MTU2OTQ1NzcyMCwianRpIjoiNTgzZjhmYmMtMzk2MS00YzA4LWJhZTAtYzQyY2IxMTM5NDY5IiwiY2xpZW50X2lkIjoiM3FlajVlMXZmMzd1N3RoZWw0dG91dDJkMWwiLCJ1c2VybmFtZSI6ImVsb3EXAMPLEn0.B4EXAMPLEFNpJ6ikVp7e6DRee95V6Qi-zEE2DJH7sHOl2zxYi7f-SmEGoh2AD8emxQRYajByz-rE4Jh0QOymN2Ys-ZIkMpVBTPgu-TMWDyOHhDUmUj2OP82yeZ3wlZAtr_gM4LzjXUXmI_K2yGjuXfXTaa1mvQEBG0mQfVd7SfwXB-jcv4RYVi6j25qgow9Ew52ufurPqaK-3WAKG32KpV8J4-Wejq8t0c-yA7sb8EnB551b7TU93uKRiVVK3E55Nk5ADPoam_WYE45i3s5qVAP_-InW75NUoOCGTsS8YWMfb6ecHYJ-1j-bzA27zaT9VjctXn9byNFZmEXAMPLExw",
"host":"example1234567890000.appsync-api.us-east-1.amazonaws.com"
```

## Real-time WebSocket

operation

After initiating a successful WebSocket handshake with AWS AppSync, the client must
send a subsequent message to connect to AWS AppSync for different operations. These
messages require the following data:

- `type`: The type of the operation.
- `id`: A unique identifier for the subscription. We recommend
  using a UUID for this purpose.
- `payload`: The associated payload, depending on the operation
  type.

The `type` field is the only required field; the `id` and
`payload` fields are optional.

### Sequence of events

To successfully initiate, establish, register, and process the subscription
request, the client must step through the following sequence:

1. Initialize connection (`connection_init`)
2. Connection acknowledgment (`connection_ack`)
3. Subscription registration (`start`)
4. Subscription acknowledgment (`start_ack`)
5. Processing subscription (`data`)
6. Subscription unregistration (`stop`)

## Connection init message

(Optional) After a successful handshake, the client can send the
`connection_init` message to start communicating with the AWS AppSync
real-time endpoint. The message is a string obtained by stringifying the JSON object
as follows:

```
{ "type": "connection_init" }
```

## Connection acknowledge

message

After sending the `connection_init` message, the client must wait for
the `connection_ack` message. All messages sent before receiving
`connection_ack` are ignored. The message should read as
follows:

```
{
  "type": "connection_ack",
  "payload": {
    // Time in milliseconds waiting for ka message before the client should terminate the WebSocket connection
    "connectionTimeoutMs": 300000
  }
}
```

## Keep-alive message

In addition to the connection acknowledgment message, the client periodically
receives keep-alive messages. If the client doesn't receive a keep-alive message
within the connection timeout period, the client should close the connection.
AWS AppSync keeps sending these messages and servicing the registered subscriptions
until it shuts down the connection automatically (after 24 hours). Keep-alive
messages are heartbeats and do not need the client to acknowledge them.

```
{ "type": "ka" }
```

## Subscription registration

message

After the client receives a `connection_ack` message, the client can
send subscription registration messages to AWS AppSync. This type of message is a
stringified JSON object that contains the following fields:

- `"id": <string>`: The ID of the subscription. This ID must
  be unique for each subscription, otherwise the server returns an error
  indicating that the subscription ID is duplicated.
- `"type": "start"`: A constant `<string>`
  parameter.
- `"payload": <Object>`: An object that contains the
  information relevant to the subscription.
  - `"data": <string>`: A stringified JSON object that
    contains a GraphQL query and variables.
    - `"query": <string>`: A GraphQL
      operation.
    - `"variables": <Object>`: An object that
      contains the variables for the query.

  - `"extensions": <Object>`: An object that contains
    an authorization object.

- `"authorization": <Object>`: An object that contains the
  fields required for authorization.

### Authorization object for subscription registration

The same rules in the [Header parameter format based on AWS AppSync API authorization mode](#header-parameter-format-based-on-appsync-api-authorization-mode "#header-parameter-format-based-on-appsync-api-authorization-mode") section apply for the authorization object. The only exception is for IAM,
where the SigV4 signature information is slightly different. For more details,
see the IAM example.

Example using Amazon Cognito user pools:

```
{
  "id": "ee849ef0-cf23-4cb8-9fcb-152ae4fd1e69",
  "payload": {
    "data": "{\"query\":\"subscription onCreateMessage {\\n onCreateMessage {\\n __typename\\n message\\n }\\n }\",\"variables\":{}}",
      "extensions": {
        "authorization": {
          "Authorization": "eyEXAMPLEiJjbG5xb3A5eW5MK09QYXIrMTJEXAMPLEBieU5WNHhsQjhPVW9YMnM2WldvPSIsImFsZyI6IlEXAMPLEn0.eyJzdWIiOiJhNmNmMjcwNy0xNjgxLTQ1NDItEXAMPLENjY0MTg2NjlkMzYiLCJldmVudF9pZCI6ImU3YWVmMzEyLWUEXAMPLEY0Zi04YjlhLTRjMWY5M2Q5ZTQ2OCIsInRva2VuX3VzZSI6ImFjY2VzcyIsIEXAMPLEIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE1Njk2MTgzMzgsImlzcyI6Imh0dEXAMPLEXC9jb2duaXRvLWlkcC5hcC1zb3V0aGVhc3QtMi5hbWF6b25hd3MuY29tXC9hcC1zbEXAMPLEc3QtMl83OHY0SVZibVAiLCJleHAiOjE1NzAyNTQ3NTUsImlhdCI6MTU3MDI1MTE1NSwianRpIjoiMmIEXAMPLEktZTVkMi00ZDhkLWJiYjItNjA0YWI4MDEwOTg3IiwiY2xpZW50X2lkIjoiM3FlajVlMXZmMzd1EXAMPLE0dG91dDJkMWwiLCJ1c2VybmFtZSI6ImVsb3J6YWZlIn0.CT-qTCtrYeboUJ4luRSTPXaNewNeEXAMPLE14C6sfg05tO0fOMpiUwj9k19gtNCCMqoSsjtQoUweFnH4JYa5EXAMPLEVxOyQEQ4G7jQrt5Ks6STn53vuseR3zRW9snWgwz7t3ZmQU-RWvW7yQU3sNQRLEXAMPLEcd0yufBiCYs3dfQxTTdvR1B6Wz6CD78lfNeKqfzzUn2beMoup2h6EXAMPLE4ow8cUPUPvG0DzRtHNMbWskjPanu7OuoZ8iFO_Eot9kTtAlVKYoNbWkZhkD8dxutyoU4RSH5JoLAnrGF5c8iKgv0B2dfEXAMPLEIihxaZVJ9w9w48S4EXAMPLEcA",
          "host": "example1234567890000.appsync-api.us-east-1.amazonaws.com"
         }
      }
  },
  "type": "start"
}
```

Example using IAM:

```
{
  "id": "eEXAMPLE-cf23-1234-5678-152EXAMPLE69",
  "payload": {
    "data": "{\"query\":\"subscription onCreateMessage {\\n onCreateMessage {\\n __typename\\n message\\n }\\n }\",\"variables\":{}}",
    "extensions": {
      "authorization": {
        "accept": "application/json, text/javascript",
        "content-type": "application/json; charset=UTF-8",
        "X-Amz-Security-Token": "AgEXAMPLEZ2luX2VjEAoaDmFwLXNvdXRoZWFEXAMPLEcwRQIgAh97Cljq7wOPL8KsxP3YtDuyc/9hAj8PhJ7Fvf38SgoCIQDhJEXAMPLEPspioOztj++pEagWCveZUjKEn0zyUhBEXAMPLEjj//////////8BEXAMPLExODk2NDgyNzg1NSIMo1mWnpESWUoYw4BkKqEFSrm3DXuL8w+ZbVc4JKjDP4vUCKNR6Le9C9pZp9PsW0NoFy3vLBUdAXEXAMPLEOVG8feXfiEEA+1khgFK/wEtwR+9zF7NaMMMse07wN2gG2tH0eKMEXAMPLEQX+sMbytQo8iepP9PZOzlZsSFb/dP5Q8hk6YEXAMPLEYcKZsTkDAq2uKFQ8mYUVA9EtQnNRiFLEY83aKvG/tqLWNnGlSNVx7SMcfovkFDqQamm+88y1OwwAEYK7qcoceX6Z7GGcaYuIfGpaX2MCCELeQvZ+8WxEgOnIfz7GYvsYNjLZSaRnV4G+ILY1F0QNW64S9Nvj+BwDg3ht2CrNvpwjVYlj9U3nmxE0UG5ne83LL5hhqMpm25kmL7enVgw2kQzmU2id4IKu0C/WaoDRuO2F5zE63vJbxN8AYs7338+4B4HBb6BZ6OUgg96Q15RA41/gIqxaVPxyTpDfTU5GfSLxocdYeniqqpFMtZG2n9d0u7GsQNcFkNcG3qDZm4tDo8tZbuym0a2VcF2E5hFEgXBa+XLJCfXi/77OqAEjP0x7Qdk3B43p8KG/BaioP5RsV8zBGvH1zAgyPha2rN70/tT13yrmPd5QYEfwzexjKrV4mWIuRg8NTHYSZJUaeyCwTom80VFUJXG+GYTUyv5W22aBcnoRGiCiKEYTLOkgXecdKFTHmcIAejQ9Welr0a196Kq87w5KNMCkcCGFnwBNFLmfnbpNqT6rUBxxs3X5ntX9d8HVtSYINTsGXXMZCJ7fnbWajhg/aox0FtHX21eF6qIGT8j1z+l2opU+ggwUgkhUUgCH2TfqBj+MLMVVvpgqJsPKt582caFKArIFIvO+9QupxLnEH2hz04TMTfnU6bQC6z1buVe7h+tOLnh1YPFsLQ88anib/7TTC8k9DsBTq0ASe8R2GbSEsmO9qbbMwgEaYUhOKtGeyQsSJdhSk6XxXThrWL9EnwBCXDkICMqdntAxyyM9nWsZ4bL9JHqExgWUmfWChzPFAqn3F4y896UqHTZxlq3WGypn5HHcem2Hqf3IVxKH1inhqdVtkryEiTWrI7ZdjbqnqRbl+WgtPtKOOweDlCaRs3R2qXcbNgVhleMk4IWnF8D1695AenU1LwHjOJLkCjxgNFiWAFEPH9aEXAMPLExA==",
        "Authorization": "AWS4-HMAC-SHA256 Credential=XXXXXXXXXXXXXXXXXXXX/20200401/us-east-1/appsync/aws4_request, SignedHeaders=accept;content-encoding;content-type;host;x-amz-date;x-amz-security-token, Signature=b90131a61a7c4318e1c35ead5dbfdeb46339a7585bbdbeceeaff51f4022eb1fd",
        "content-encoding": "amz-1.0",
        "host": "example1234567890000.appsync-api.us-east-1.amazonaws.com",
        "x-amz-date": "20200401T001010Z"
      }
    }
  },
  "type": "start"
}
```

Example using a custom domain name:

```
{
  "id": "key-cf23-4cb8-9fcb-152ae4fd1e69",
  "payload": {
    "data": "{\"query\":\"subscription onCreateMessage {\\n onCreateMessage {\\n __typename\\n message\\n }\\n }\",\"variables\":{}}",
      "extensions": {
        "authorization": {
          "x-api-key": "da2-12345678901234567890123456",
          "host": "api.example.com"
         }
      }
  },
  "type": "start"
}
```

The SigV4 signature does not need `/connect` to be appended to the
URL, and the JSON stringified GraphQL operation replaces `data`. The
following is an example of a SigV4 signature request:

```
{
  url: "https://example1234567890000.appsync-api.us-east-1.amazonaws.com/graphql",
  data: "{\"query\":\"subscription onCreateMessage {\\n onCreateMessage {\\n __typename\\n message\\n }\\n }\",\"variables\":{}}",
  method: "POST",
  headers: {
    "accept": "application/json, text/javascript",
    "content-encoding": "amz-1.0",
    "content-type": "application/json; charset=UTF-8",
  }
}
```

## Subscription acknowledgment

message

After sending the subscription start message, the client should wait for AWS AppSync
to send the `start_ack` message. The `start_ack` message
indicates that the subscription is successful.

Subscription acknowledgment example:

```
{
  "type": "start_ack",
  "id": "eEXAMPLE-cf23-1234-5678-152EXAMPLE69"
}
```

## Error message

If connection init or subscription registration fails, or if a subscription is
ended from the server, the server sends an error message to the client. If the error
happens during connection init time, the connection will be closed by the
server.

- `"type": "error"`: A constant `<string>`
  parameter.
- `"id": <string>`: The ID of the corresponding registered
  subscription, if relevant.
- `"payload" <Object>`: An object that contains the
  corresponding error information.

Example:

```
{
  "type": "error",
  "payload": {
    "errors": [
      {
        "errorType": "LimitExceededError",
        "message": "Rate limit exceeded"
      }
    ]
  }
}
```

## Processing data messages

When a client submits a mutation, AWS AppSync identifies all of the subscribers
interested in it and sends a `"type":"data"` message to each using the
corresponding subscription `id` from the `"start"`
subscription operation. The client is expected to keep track of the subscription
`id` that it sends so that when it receives a data message, the
client can match it with the corresponding subscription.

- `"type": "data"`: A constant `<string>`
  parameter.
- `"id": <string>`: The ID of the corresponding registered
  subscription.
- `"payload" <Object>`: An object that contains the
  subscription information.

Example:

```
{
  "type": "data",
  "id": "ee849ef0-cf23-4cb8-9fcb-152ae4fd1e69",
  "payload": {
    "data": {
      "onCreateMessage": {
        "__typename": "Message",
        "message": "test"
      }
    }
  }
}
```

## Subscription unregistration

message

When the app wants to stop listening to the subscription events, the client should
send a message with the following stringified JSON object:

- `"type": "stop"`: A constant `<string>`
  parameter.
- `"id": <string>`: The ID of the subscription to
  unregister.

Example:

```
{
  "type":"stop",
  "id":"ee849ef0-cf23-4cb8-9fcb-152ae4fd1e69"
}
```

AWS AppSync sends back a confirmation message with the following stringified JSON
object:

- `"type": "complete"`: A constant `<string>`
  parameter.
- `"id": <string>`: The ID of the unregistered
  subscription.

After the client receives the confirmation message, it receives no more messages
for this particular subscription.

Example:

```
{
  "type":"complete",
  "id":"eEXAMPLE-cf23-1234-5678-152EXAMPLE69"
}
```

## Disconnecting the WebSocket

Before disconnecting, to avoid data loss, the client should have the necessary
logic to check that no operation is currently in place through the WebSocket
connection. All subscriptions should be unregistered before disconnecting from the
WebSocket.
