

# Request timeout
<a name="web-functions-revisions-timeout"></a>

The `timeoutSeconds` setting controls the maximum time that a single HTTP request can run before Lambda terminates it. Valid values are 3–900 seconds (15 minutes). The default is 30 seconds.

Choose a timeout value based on your application's longest expected request. Setting the timeout too low causes long-running requests to fail. Setting it too high lets stuck requests run longer before Lambda terminates them.

When a non-streaming request exceeds the timeout, Lambda returns HTTP 504 with a `lambda-web-error-type` header of `Runtime.RequestTimeout`. For a streaming response, the timeout bounds the whole stream. When the timeout elapses, Lambda ends the stream, and the client receives the status code already sent, typically 200, with a truncated body and no `lambda-web-error-type` header.