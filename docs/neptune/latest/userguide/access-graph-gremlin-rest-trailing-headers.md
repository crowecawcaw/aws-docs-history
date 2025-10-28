# Use optional HTTP

trailing headers to enable multi-part Gremlin responses

By default, the HTTP response to Gremlin queries is returned in a single
JSON result set. In the case of a very large result set, this can cause an
`OutOfMemoryError` exception on the DB instance.

However, you can enable _chunked_ responses (responses
that are returned in multiple separate parts). You do this by including
a transfer-encoding (TE) trailers header (`te: trailers`) in your
request. See [the
MDN page about TE request headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/TE "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/TE")) for more information about TE headers.

When a response is returned in multiple parts, it can be hard to diagnose a
problem that occurs after the first part is received, since the first part arrives
with an HTTP status code of `200` (OK). A subsequent failure usually
results in a message body containing a corrupt response, at the end of which Neptune
appends an error message.

To make detection and diagnosis of this kind of failure easier, Neptune also
includes two new header fields within the trailing headers of every response chunk:

- `X-Neptune-Status`  –   contains the
  response code followed by a short name. For instance, in case of success the
  trailing header would be: `X-Neptune-Status: 200 OK`.
  In the case of failure, the response code would be one of the [Neptune engine error code](errors-engine-codes.md "errors-engine-codes.md"), such as
  `X-Neptune-Status: 500 TimeLimitExceededException`.
- `X-Neptune-Detail`  –   is empty
  for successful requests. In the case of errors, it contains the JSON error
  message. Because only ASCII characters are allowed in HTTP header values,
  the JSON string is URL encoded.

###### Note

Neptune does not currently support `gzip` compression of
chunked responses. If the client requests both chunked encoding and compression
at the same time, Neptune skips the compression.
