# Monitor HTTP APIs in API Gateway

You can use CloudWatch metrics and CloudWatch Logs to monitor HTTP APIs. By combining logs and
metrics, you can log errors and monitor your API's performance.

###### Note

API Gateway might not generate logs and metrics in the following cases:

- 413 Request Entity Too Large errors
- Excessive 429 Too Many Requests errors
- 400 series errors from requests sent to a custom domain that has no API mapping
- 500 series errors caused by internal failures

###### Topics

- [Monitor CloudWatch metrics for HTTP APIs in API Gateway](http-api-metrics.md "http-api-metrics.md")
- [Configure logging for HTTP APIs in API Gateway](http-api-logging.md "http-api-logging.md")
