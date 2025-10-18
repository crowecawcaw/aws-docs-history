# Restrictions on
 Lambda@Edge

The following restrictions apply only to Lambda@Edge.

###### Contents

* [DNS resolution](lambda-at-edge-function-restrictions.md#lambda-at-edge-restrictions-dns "lambda-at-edge-function-restrictions.md#lambda-at-edge-restrictions-dns")
* [HTTP status codes](lambda-at-edge-function-restrictions.md#lambda-at-edge-restrictions-status-codes "lambda-at-edge-function-restrictions.md#lambda-at-edge-restrictions-status-codes")
* [Lambda function version](lambda-at-edge-function-restrictions.md#lambda-at-edge-restrictions-version "lambda-at-edge-function-restrictions.md#lambda-at-edge-restrictions-version")
* [Lambda Region](lambda-at-edge-function-restrictions.md#lambda-at-edge-restrictions-region "lambda-at-edge-function-restrictions.md#lambda-at-edge-restrictions-region")
* [Lambda role
 permissions](lambda-at-edge-function-restrictions.md#lambda-at-edge-restrictions-role-permissions "lambda-at-edge-function-restrictions.md#lambda-at-edge-restrictions-role-permissions")
* [Lambda features](lambda-at-edge-function-restrictions.md#lambda-at-edge-restrictions-features "lambda-at-edge-function-restrictions.md#lambda-at-edge-restrictions-features")
* [Supported runtimes](lambda-at-edge-function-restrictions.md#lambda-at-edge-restrictions-runtime "lambda-at-edge-function-restrictions.md#lambda-at-edge-restrictions-runtime")
* [CloudFront
 headers](lambda-at-edge-function-restrictions.md#lambda-at-edge-restrictions-cloudfront-headers "lambda-at-edge-function-restrictions.md#lambda-at-edge-restrictions-cloudfront-headers")
* [Restrictions on the
 request body with the include body option](lambda-at-edge-function-restrictions.md#lambda-at-edge-restrictions-request-body "lambda-at-edge-function-restrictions.md#lambda-at-edge-restrictions-request-body")
* [Response timeout and keep-alive
 timeout (custom origins only)](lambda-at-edge-function-restrictions.md#timeout-for-lambda-edge-functions "lambda-at-edge-function-restrictions.md#timeout-for-lambda-edge-functions")
For information about quotas, see [Quotas on Lambda@Edge](cloudfront-limits.md#limits-lambda-at-edge "cloudfront-limits.md#limits-lambda-at-edge").


## DNS resolution


CloudFront performs a DNS resolution on the origin domain name
 *before* it executes your origin request Lambda@Edge function.
 If the DNS service for your domain is experiencing issues and CloudFront can't resolve the
 domain name to get the IP address, your Lambda@Edge function will not invoke. CloudFront
 will return an [HTTP 502 status code (Bad
 Gateway)](http-502-bad-gateway.md "http-502-bad-gateway.md") to the client. For more information, see [DNS error
 (NonS3OriginDnsError)](http-502-bad-gateway.md#http-502-dns-error "http-502-bad-gateway.md#http-502-dns-error").


If your function logic modifies the origin domain name, CloudFront will perform another
 DNS resolution on the updated domain name after the function has finished
 executing.


For more information about managing DNS failover, see [Configuring
 DNS failover](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring.html "https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring.html") in the *Amazon Route 53 Developer
 Guide*.


## HTTP status codes


Lambda@Edge functions for viewer response events cannot modify the HTTP status code
 of the response, regardless of whether the response came from the origin or the CloudFront
 cache.


## Lambda function version


You must use a numbered version of the Lambda function, not `$LATEST` or
 aliases.


## Lambda Region


The Lambda function must be in the US East (N. Virginia) Region.


## Lambda role
 permissions


The IAM execution role associated with the Lambda function must allow the service
 principals `lambda.amazonaws.com` and
 `edgelambda.amazonaws.com` to assume the role. For more information,
 see [Set up IAM permissions and roles for
 Lambda@Edge](lambda-edge-permissions.md "lambda-edge-permissions.md").


## Lambda features


The following Lambda features are not supported by Lambda@Edge:



* [Lambda runtime management configurations](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-update.html#runtime-management-controls "https://docs.aws.amazon.com/lambda/latest/dg/runtimes-update.html#runtime-management-controls") other than
 **Auto** (default)
* Configuration of your Lambda function to access resources inside your
 VPC
* [Lambda function dead
 letter queues](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#dlq "https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#dlq")
* [Lambda environment
 variables](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html "https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html") (except for reserved environment variables, which are
 automatically supported)
* Lambda functions with [Managing AWS Lambda
 dependencies with layers](https://docs.aws.amazon.com/lambda/latest/dg/chapter-layers.html "https://docs.aws.amazon.com/lambda/latest/dg/chapter-layers.html")
* [Using
 AWS X-Ray](https://docs.aws.amazon.com/lambda/latest/dg/lambda-x-ray.html "https://docs.aws.amazon.com/lambda/latest/dg/lambda-x-ray.html")
* Lambda provisioned concurrency


###### Note

Lambda@Edge functions share the same [Regional
 concurrency](https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html "https://docs.aws.amazon.com/lambda/latest/dg/configuration-concurrency.html") capabilities as all Lambda functions. For more
 information, see [Quotas on Lambda@Edge](cloudfront-limits.md#limits-lambda-at-edge "cloudfront-limits.md#limits-lambda-at-edge").
* [Create a Lambda function using a container image](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html "https://docs.aws.amazon.com/lambda/latest/dg/images-create.html")
* [Lambda functions that use the arm64 architecture](https://docs.aws.amazon.com/lambda/latest/dg/foundation-arch.html "https://docs.aws.amazon.com/lambda/latest/dg/foundation-arch.html")
* Lambda functions with more than 512 MB of ephemeral storage
* Using a [customer managed key to encrypt
 your .zip deployment packages](https://docs.aws.amazon.com/lambda/latest/dg/encrypt-zip-package.html "https://docs.aws.amazon.com/lambda/latest/dg/encrypt-zip-package.html")

## Supported runtimes


Lambda@Edge supports the latest versions of Node.js and Python runtimes. For a list
 of supported versions and their future deprecation dates, see [Supported
 runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtimes-supported "https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtimes-supported") in the *AWS Lambda Developer Guide*.


###### Tip


* As a best practice, use the latest versions of the provided runtimes
 for performance improvements and new features.
* You can’t create or update functions with deprecated versions of
 Node.js. You can only associate existing functions with these versions
 with CloudFront distributions. Functions with these versions that are
 associated with distributions will continue to run. However, we
 recommend that you move your function to newer versions of Node.js. For
 more information, see [Runtime deprecation policy](https://docs.aws.amazon.com/lambda/latest/dg/runtime-support-policy.html "https://docs.aws.amazon.com/lambda/latest/dg/runtime-support-policy.html") in the
 *AWS Lambda Developer Guide* and the [Node.js
 release schedule](https://github.com/nodejs/Release#release-schedule "https://github.com/nodejs/Release#release-schedule") on GitHub.

## CloudFront
 headers


Lambda@Edge functions can read, edit, remove, or add any of the CloudFront headers listed
 in [Add CloudFront request headers](adding-cloudfront-headers.md "adding-cloudfront-headers.md").


###### Notes


* If you want CloudFront to add these headers, you must configure CloudFront to add
 them by using a [cache
 policy](controlling-the-cache-key.md "controlling-the-cache-key.md") or [origin
 request policy](controlling-origin-requests.md "controlling-origin-requests.md").
* CloudFront adds the headers *after* the viewer request
 event, which means the headers aren't available to Lambda@Edge functions
 in a viewer request. The headers are only available to Lambda@Edge
 functions in an origin request and origin response.
* If the viewer request includes headers that have these names, and you
 configured CloudFront to add these headers using a [cache policy](controlling-the-cache-key.md "controlling-the-cache-key.md") or [origin request policy](controlling-origin-requests.md "controlling-origin-requests.md"),
 then CloudFront overwrites the header values that were in the viewer request.
 Viewer-facing functions see the header value from the viewer request,
 while origin-facing functions see the header value that CloudFront
 added.
* If a viewer request function adds the
 `CloudFront-Viewer-Country` header, it fails validation
 and CloudFront returns HTTP status code 502 (Bad Gateway) to the
 viewer.

## Restrictions on the
 request body with the include body option


When you choose the **Include Body** option to expose the request
 body to your Lambda@Edge function, the following information and size limits apply to
 the portions of the body that are exposed or replaced.



* CloudFront always base64 encodes the request body before exposing it to
 Lambda@Edge.
* If the request body is large, CloudFront truncates it before exposing it to
 Lambda@Edge, as follows:




	+ For viewer request events, the body is truncated at 40 KB.
	+ For origin request events, the body is truncated at 1 MB.
* If you access the request body as read-only, CloudFront sends the full original
 request body to the origin.
* If your Lambda@Edge function replaces the request body, the following size
 limits apply to the body that the function returns:




	+ If the Lambda@Edge function returns the body as plain text:
	
	
	
	
		- For viewer request events, the body limit is 40 KB.
		- For origin request events, the body limit is 1 MB.
	+ If the Lambda@Edge function returns the body as base64 encoded
	 text:
	
	
	
	
		- For viewer request events, the body limit is 53.2
		 KB.
		- For origin request events, the body limit is 1.33
		 MB.

###### Note

If your Lambda@Edge function returns a body that exceeds these limits, your
 request will fail with an HTTP 502 status code ([Lambda validation
 error](http-502-bad-gateway.md#http-502-lambda-validation-error "http-502-bad-gateway.md#http-502-lambda-validation-error")). We recommend that you
 update your Lambda@Edge function so that the body doesn't exceed these
 limits.


## Response timeout and keep-alive
 timeout (custom origins only)


If you're using Lambda@Edge functions to set the response timeout or keep-alive
 timeout for your distribution origins, verify that you're specifying a value that
 your origin can support. For more information, see [Response and keep-alive timeout
 quotas](DownloadDistValuesOrigin.md#response-keep-alive-timeout-quota "DownloadDistValuesOrigin.md#response-keep-alive-timeout-quota").
