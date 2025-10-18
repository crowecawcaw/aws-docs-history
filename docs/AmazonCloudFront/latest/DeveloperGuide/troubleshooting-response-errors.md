# Troubleshooting error response status
 codes in CloudFront

If CloudFront requests an object from your origin, and the origin returns an HTTP 4xx or 5xx
 status code, there's a problem with communication between CloudFront and your origin. 

This topic also includes troubleshooting steps for these status codes when using
 Lambda@Edge or CloudFront Functions.

The following topics provide detailed explanations of the potential causes behind
 these error responses and offers step-by-step guidance on how to diagnose and resolve
 the underlying issues.

###### Topics

* [HTTP 400 status code (Bad Request)](http-400-bad-request.md "http-400-bad-request.md")
* [HTTP 401 status code (Unauthorized)](http-401-unauthorized.md "http-401-unauthorized.md")
* [HTTP 403 status code (Invalid method)](http-403-invalid-method.md "http-403-invalid-method.md")
* [HTTP 403 status code (Permission
 Denied)](http-403-permission-denied.md "http-403-permission-denied.md")
* [HTTP 404 status code (Not Found)](http-404-not-found.md "http-404-not-found.md")
* [HTTP 412 status code (Precondition
 Failed)](http-412-precondition-failed.md "http-412-precondition-failed.md")
* [HTTP 500 status code (Internal
 Server Error)](http-500-internal-server-error.md "http-500-internal-server-error.md")
* [HTTP 502 status code (Bad Gateway)](http-502-bad-gateway.md "http-502-bad-gateway.md")
* [HTTP 503 status code (Service
 Unavailable)](http-503-service-unavailable.md "http-503-service-unavailable.md")
* [HTTP 504 status code (Gateway
 Timeout)](http-504-gateway-timeout.md "http-504-gateway-timeout.md")
