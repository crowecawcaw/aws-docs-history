# Common Errors

This section lists the errors common to the API actions of all AWS services. For errors specific to an API action for this service, see the topic for that API action.




**AccessDeniedException**


You do not have sufficient access to perform this action.


HTTP Status Code: 403




**ExpiredTokenException**


The security token included in the request is expired


HTTP Status Code: 403




**IncompleteSignature**


The request signature does not conform to AWS standards.


HTTP Status Code: 403




**InternalFailure**


The request processing has failed because of an unknown error, exception or failure.


HTTP Status Code: 500




**MalformedHttpRequestException**


Problems with the request at the HTTP level, e.g. we can't decompress the body according to the decompression algorithm specified by the content-encoding.


HTTP Status Code: 400




**NotAuthorized**


You do not have permission to perform this action.


HTTP Status Code: 401




**OptInRequired**


The AWS access key ID needs a subscription for the service.


HTTP Status Code: 403



**RequestAbortedException**

Convenient exception that can be used when a request is aborted before a reply is sent back (e.g. client closed connection).


HTTP Status Code: 400



**RequestEntityTooLargeException**

Problems with the request at the HTTP level. The request entity is too large.


HTTP Status Code: 413




**RequestExpired**


The request reached the service more than 15 minutes after the date stamp on the request or more than 15 minutes after the request expiration date (such as for pre-signed URLs), or the date stamp on the request is more than 15 minutes in the
 future.


HTTP Status Code: 400




**RequestTimeoutException**


Problems with the request at the HTTP level. Reading the Request timed out.


HTTP Status Code: 408




**ServiceUnavailable**


The request has failed due to a temporary failure of the server.


HTTP Status Code: 503




**ThrottlingException**


The request was denied due to request throttling.


HTTP Status Code: 400




**UnrecognizedClientException**


The X.509 certificate or AWS access key ID provided does not exist in our records.


HTTP Status Code: 403




**UnknownOperationException** 


The action or operation requested is invalid. Verify that the action is typed correctly.


HTTP Status Code: 404




**ValidationError**


The input fails to satisfy the constraints specified by an AWS service.


HTTP Status Code: 400
