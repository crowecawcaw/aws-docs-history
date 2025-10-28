# Optional HTTP trailing headers for multi-part SPARQL responses

###### Note

This feature is available starting in [Neptune engine release 1.0.3.0](engine-releases-1.0.3.md "engine-releases-1.0.3.md").

The HTTP response to SPARQL queries and updates is often returned in more than
one part or chunk. It can be hard to diagnose a failure that occurs after a
query or update begins sending these chunks, especially since the first one arrives
with an HTTP status code of `200`.

Unless you explicitly request trailing headers, Neptune only reports such
a failure by appending an error message to the message body, which is usually
corrupted.

To make detection and diagnosis of this kind of problem easier, you can include
a transfer-encoding (TE) trailers header (`te: trailers`) in your request
(see, for example, [the
MDN page about TE request headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/TE "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/TE")). Doing this will cause Neptune to include
two new header fields within the trailing headers of the response chunks:

- `X-Neptune-Status`  –   contains the
  response code followed by a short name. For instance, in case of success the
  trailing header would be: `X-Neptune-Status: 200 OK`.
  In the case of failure, the response code would be an [Neptune engine error code](errors-engine-codes.md "errors-engine-codes.md") such as
  `X-Neptune-Status: 500 TimeLimitExceededException`.
- `X-Neptune-Detail`  –   is empty
  for successful requests. In the case of errors, it contains the JSON error
  message. Because only ASCII characters are allowed in HTTP header values,
  the JSON string is URL encoded. The error message is also still appended
  to the response message body.
