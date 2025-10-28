# Monitor REST APIs in API Gateway

In this section, you can learn how to monitor your API by using CloudWatch metrics, CloudWatch Logs,
Firehose, and AWS X-Ray. By combining CloudWatch execution logs and CloudWatch metrics, you can log errors
and execution traces, and monitor your API's performance. You might also want to log API
calls to Firehose. You can also use AWS X-Ray to trace calls through the downstream services
that make up your API.

###### Note

API Gateway might not generate logs and metrics in the following cases:

- 413 Request Entity Too Large errors
- 431 Request Header Fields Too Large errors
- Excessive 429 Too Many Requests errors
- 400 series errors from requests sent to a custom domain that has no API mapping
- 500 series errors caused by internal failures
  API Gateway will not generate logs and metrics when testing a REST API method. The CloudWatch entries are simulated. For
  more information, see [Use the API Gateway console to test a REST API method](how-to-test-method.md "how-to-test-method.md").

###### Topics

- [Monitor REST API execution with Amazon CloudWatch metrics](monitoring-cloudwatch.md "monitoring-cloudwatch.md")
- [Set up CloudWatch logging for REST APIs in API Gateway](set-up-logging.md "set-up-logging.md")
- [Log REST API calls to Amazon Data Firehose in API Gateway](apigateway-logging-to-kinesis.md "apigateway-logging-to-kinesis.md")
- [Variables for access logging for API Gateway](api-gateway-variables-for-access-logging.md "api-gateway-variables-for-access-logging.md")
- [Trace user requests to REST APIs using X-Ray in API Gateway](apigateway-xray.md "apigateway-xray.md")
