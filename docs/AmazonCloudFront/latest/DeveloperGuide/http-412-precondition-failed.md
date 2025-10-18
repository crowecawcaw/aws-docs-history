# HTTP 412 status code (Precondition
 Failed)

CloudFront returns a 412 (Precondition Failed) error code when access to the target
 resource has been denied. In some cases, a server is configured to accept requests
 only after certain conditions are fulfilled. If any of the specified conditions are
 not met, then the server doesn't allow the client to access the given resource.
 Instead, the server responds with a 412 error code.

Common causes of a 412 error in CloudFront include:


* Conditional requests on methods other than `GET` or
 `HEAD` when the condition defined by the
 `If-Unmodified-Since` or `If-None-Match` headers
 is not fulfilled. In that case, the request, usually an upload or a
 modification of a resource, can't be made.
* A condition in one or more of the request fields in the CloudFront [UpdateDistribution](../../../cloudfront/latest/APIReference/API_UpdateDistribution.md "../../../cloudfront/latest/APIReference/API_UpdateDistribution.md") API operation evaluates as false.
