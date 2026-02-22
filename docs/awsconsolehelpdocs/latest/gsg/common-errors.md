# Common Errors

The following errors are common to API actions of all AWS services. For errors specific to an API action, see that action's documentation.

**AccessDeniedException**

You don't have sufficient access to perform this action.

HTTP status code: 403

For more information, see [Troubleshooting access denied errors](troubleshooting.md#access-denied-error "troubleshooting.md#access-denied-error").

**ExpiredTokenException**

The security token included in the request is expired.

HTTP status code: 403

**IncompleteSignature**

The request signature doesn't conform to AWS standards.

HTTP status code: 403

**InternalFailure**

The request processing has failed because of an unknown error, exception, or failure.

HTTP status code: 500

**MalformedHttpRequestException**

There are problems with the request at the HTTP level. For example, we can't decompress the body according to the decompression algorithm specified by the content-encoding.

HTTP status code: 400

**NotAuthorized**

You don't have permission to perform this action.

HTTP status code: 401

**OptInRequired**

The AWS access key ID needs a subscription for the service.

HTTP status code: 403

**RequestAbortedException**

The request was aborted before a reply was sent back (for example, the client closed the connection).

HTTP status code: 400

**RequestEntityTooLargeException**

There are problems with the request at the HTTP level. The request entity is too large.

HTTP status code: 413

**RequestExpired**

The request reached the service more than 15 minutes after the date stamp on the request or more than 15 minutes after the request expiration date (such as for pre-signed URLs), or the date stamp on the request is more than 15 minutes in the future.

HTTP status code: 400

**RequestTimeoutException**

There are problems with the request at the HTTP level. Reading the request timed out.

HTTP status code: 408

**ServiceUnavailable**

The request has failed due to a temporary failure of the server.

HTTP status code: 503

**ThrottlingException**

The request was denied due to request throttling.

HTTP status code: 400

**UnrecognizedClientException**

The X.509 certificate or AWS access key ID provided doesn't exist in our records.

HTTP status code: 403

**UnknownOperationException**

The action or operation requested is invalid. Verify that the action is typed correctly.

HTTP status code: 404

**ValidationError**

The input fails to satisfy the constraints specified by an AWS service.

HTTP status code: 400
