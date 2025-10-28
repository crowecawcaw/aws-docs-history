# HTTP 500 status code (Internal

Server Error)

An HTTP 500 status code (Internal Server Error) indicates that the server
encountered an unexpected condition that prevented it from fulfilling the request.
The following are some common causes of 500 errors in Amazon CloudFront.

###### Topics

- [Origin server returns 500 error to
  CloudFront](#origin-server-500-error "#origin-server-500-error")

## Origin server returns 500 error to

CloudFront

Your origin server might be returning a 500 error to CloudFront. Refer to the
following troubleshooting topics for more information:

- **If Amazon S3 returns a 500 error**, see
  [How do I troubleshoot a HTTP 500 or 503 error from
  Amazon S3?](https://repost.aws/knowledge-center/http-5xx-errors-s3 "https://repost.aws/knowledge-center/http-5xx-errors-s3")
- **If API Gateway returns a 500 error**, see
  [How
  do I troubleshoot 5xx errors for API Gateway REST API?](https://repost.aws/knowledge-center/api-gateway-5xx-error "https://repost.aws/knowledge-center/api-gateway-5xx-error").
- **If Elastic Load Balancing returns a 500 error**, see
  [HTTP 500: Internal server error](../../../elasticloadbalancing/latest/application/load-balancer-troubleshooting.md#http-500-issues "../../../elasticloadbalancing/latest/application/load-balancer-troubleshooting.md#http-500-issues") in the
  _User Guide for Application Load Balancers_.

If the preceding list doesn't resolve the 500 error, the issue might be with a
CloudFront Point of Presence returning an internal server error. You can contact [Support](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/") for assistance.
