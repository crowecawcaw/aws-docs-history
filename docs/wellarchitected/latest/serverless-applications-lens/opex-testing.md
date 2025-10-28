# Testing

Testing is commonly done through unit, integration, and acceptance tests. Developing robust
testing strategies allows you to emulate your serverless application under different loads
and conditions. Unit tests shouldn’t be different from non-serverless applications and,
therefore, can be designed to run locally without any changes. Integration tests shouldn’t
mock services you can’t control, since they might change and provide unexpected results.
These tests are better performed when using real services because they can provide the same
environment a serverless application would use when processing requests in production.
Acceptance or end-to-end tests should be performed without any changes because the primary
goal is to simulate the end users’ actions through the available external interface.
Therefore, there is no unique recommendation to be aware of here. In general, Lambda and
third-party tools that are available in the AWS Marketplace can be used as a test harness in the
context of performance testing. Here are some considerations during performance testing to
be aware of:

Metrics such as invoked maximum memory used and `init` duration are
available in CloudWatch Metrics. For more information, see the [performance pillar](performance-efficiency.md "performance-efficiency.md") section.

If your Lambda function is attached to Amazon Virtual Private Cloud (Amazon VPC), pay attention to the available IP
address space inside your subnet.

Creating modularized code as separate functions outside of the handler enables more
unit-testable functions.

Establishing externalized connection code (such as a connection pool to a relational
database) referenced in the Lambda function’s static constructor or initialization code
(global scope, outside the handler) will ensure that external connection thresholds are
not reached if the Lambda execution environment is reused.

Use a DynamoDB on-demand table unless your performance tests exceed current quotas in your
account.

Take into account any other service quotas that might be used within your serverless
application under performance testing.
