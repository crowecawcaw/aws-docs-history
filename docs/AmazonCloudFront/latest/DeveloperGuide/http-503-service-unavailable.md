# HTTP 503 status code (Service Unavailable)

An HTTP 503 status code (Service Unavailable) typically indicates a performance
issue on the origin server. In rare cases, it indicates that CloudFront temporarily can't
satisfy a request because of resource constraints at an edge location.

If you are using Lambda@Edge or CloudFront Functions, the issue might be an execution
error or a Lambda@Edge limit exceeded error.

###### Topics

- [Origin server does not have enough capacity to support the request rate](#http-503-service-unavailable-not-enough-origin-capacity "#http-503-service-unavailable-not-enough-origin-capacity")
- [CloudFront caused the error due to resource constraints at the edge location](#http-503-service-unavailable-limited-resources-at-edge-location "#http-503-service-unavailable-limited-resources-at-edge-location")
- [Lambda@Edge or CloudFront Function execution error](#http-503-lambda-execution-error "#http-503-lambda-execution-error")
- [Lambda@Edge limit exceeded](#http-503-lambda-limit-exceeded-error "#http-503-lambda-limit-exceeded-error")

## Origin server does not have enough capacity to support the request rate

When an origin server is unavailable or unable to serve incoming requests, it
returns an HTTP 503 status code (Service Unavailable). CloudFront then relays the
error back to the user. To resolve this issue, try the following
solutions:

- **If you use Amazon S3 as your origin
  server**:
  - You can send 3,500 PUT/COPY/POST/DELETE or 5,500 GET/HEAD
    requests per second per partitioned Amazon S3 prefix. When Amazon S3
    returns a 503 Slow Down response, this typically indicates an
    excessive request rate against a specific Amazon S3 prefix.

  Because request rates apply per prefix in an S3 bucket,
  objects should be distributed across multiple prefixes. As the
  request rate on the prefixes gradually increases, Amazon S3 scales up
  to handle requests for each of the prefixes separately. As a
  result, the overall request rate that the bucket handles is a
  multiple of the number of prefixes.
  - For more information, see [Optimizing Amazon S3 performance](../../../AmazonS3/latest/userguide/optimizing-performance.md "../../../AmazonS3/latest/userguide/optimizing-performance.md") in
    the _Amazon Simple Storage Service User Guide_.

- **If you use Elastic Load Balancing as your origin
  server**:

      + Make sure that your backend instances can respond to health
       checks.
      + Make sure that your load balancer and backend instances can
       handle the load.

  For more information, see:

      + [How do I troubleshoot 503 errors returned while using
       Classic Load Balancer?](https://repost.aws/knowledge-center/503-error-classic "https://repost.aws/knowledge-center/503-error-classic")
      + [How do I troubleshoot 503 (service unavailable) errors from
       my Application Load Balancer?](https://repost.aws/knowledge-center/alb-troubleshoot-503-errors "https://repost.aws/knowledge-center/alb-troubleshoot-503-errors")

- **If you use a custom origin**:
  - Examine the application logs to ensure that your origin has
    sufficient resources, such as memory, CPU, and disk size.
  - If you use Amazon EC2 as the backend, make sure that the instance
    type has the appropriate resources to fulfill the incoming
    requests. For more information, see [Instance types](../../../AWSEC2/latest/UserGuide/instance-types.md "../../../AWSEC2/latest/UserGuide/instance-types.md") in the
    _Amazon EC2 User Guide_.

- **If you use API Gateway**:
  - This error is related to the backend integration when the
    API Gateway API is unable to receive a response. The backend server
    might be:
    - Overloaded beyond capacity and unable to process new
      client requests.
    - Under temporary maintenance.

  - To resolve this error, look at your API Gateway application logs to
    determine if there is an issue with backend capacity,
    integration, or something else.

## CloudFront caused the error due to resource constraints at the edge location

You will receive this error in the rare situation that CloudFront can't route
requests to the next best available edge location, and so can't satisfy a
request. This error is common when you perform load testing on your CloudFront
distribution. To help prevent this, follow the [Load testing CloudFront](load-testing.md "load-testing.md")
guidelines for avoiding 503 (capacity exceeded) errors.

If this happens in your production environment, contact [Support](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

## Lambda@Edge or CloudFront Function execution error

If you're using Lambda@Edge or CloudFront Functions, an HTTP 503 status code can
indicate that your function returned an execution error.

For more details about how to identify and resolve Lambda@Edge errors, see
[Test and debug Lambda@Edge functions](lambda-edge-testing-debugging.md "lambda-edge-testing-debugging.md").

For more information about testing CloudFront Functions, see [Test functions](test-function.md "test-function.md").

## Lambda@Edge limit exceeded

If you're using Lambda@Edge, an HTTP 503 status code can indicate that Lambda
returned an error. The error might be caused by one of the following:

- The number of function executions exceeded one of the quotas that
  Lambda sets to throttle executions in an AWS Region (concurrent
  executions or invocation frequency).
- The function exceeded the Lambda function timeout quota.

For more information about the Lambda@Edge quotas, see [Quotas on Lambda@Edge](cloudfront-limits.md#limits-lambda-at-edge "cloudfront-limits.md#limits-lambda-at-edge"). For
more details about how to identify and resolve Lambda@Edge errors, see [Test and debug Lambda@Edge functions](lambda-edge-testing-debugging.md "lambda-edge-testing-debugging.md"). You can also see the [Lambda
service quotas](../../../lambda/latest/dg/gettingstarted-limits.md "../../../lambda/latest/dg/gettingstarted-limits.md") in the _AWS Lambda Developer Guide_.
