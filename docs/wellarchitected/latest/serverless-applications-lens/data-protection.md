# Data protection

Consider enabling [API Gateway Access Logs](../../../apigateway/latest/developerguide/set-up-logging.md "../../../apigateway/latest/developerguide/set-up-logging.md")
and selectively choose only what you need, since the logs might contain sensitive data,
depending on your serverless application design. For this reason, we recommend that you
encrypt any sensitive data traversing your serverless application.

API Gateway and AWS AppSync employ TLS across all communications, clients, and integrations.
Although HTTP payloads are encrypted in-transit, request path and query strings that are
part of a URL might not be. Therefore, sensitive data can be accidentally exposed via
CloudWatch Logs if sent to standard output.

Additionally, malformed or intercepted input can be used as an attack vector—either
to gain access to a system or cause a malfunction. Sensitive data should be protected at
all times in all layers possible, as discussed in detail in the [AWS Well-Architected Framework](../framework/welcome.md "../framework/welcome.md"). The recommendations in that whitepaper
still apply here.

With regard to API Gateway, sensitive data should be either encrypted at the client-side
before making its way as part of an HTTP request, or sent as a payload as part of an
HTTP POST request. That also includes encrypting any headers that might contain
sensitive data prior to making a given request.

Concerning Lambda functions or any integrations that API Gateway may be configured with,
sensitive data should be encrypted before any processing or data manipulation. This will
prevent data leakage if such data gets exposed in persistent storage or by standard
output that is streamed and persisted by CloudWatch Logs.

In the scenarios described earlier in this document, Lambda functions would persist
encrypted data in either DynamoDB, OpenSearch Service, or Amazon S3 along with encryption at rest. We strictly
advise against sending, logging, and storing unencrypted sensitive data, either as part
of HTTP request path or query strings, or in the standard output of a Lambda function.

Enabling logging in API Gateway where sensitive data is unencrypted is also discouraged. As
mentioned in the [Detective controls](detective-controls.md "detective-controls.md") subsection, you should consult your compliance team
before enabling API Gateway logging in such cases.

| SEC 3: How do you implement application security in your workload? |
| ------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                    | Review security awareness documents authored by AWS Security bulletins and industry threat intelligence as covered in the AWS Well-Architected Framework. OWASP guidelines for application security still apply. Validate and sanitize inbound events, and perform a security code review as you normally would for non-serverless applications. For API Gateway, set up basic request validation as a first step to ensure that the request adheres to the configured JSON-schema request model as well as any required parameters in the URI, query string, or headers. Application-specific deep validation should be implemented, whether that is as a separate Lambda function, library, framework, or service. To add protection for your code executing in Lambda runtime against any unintended and unauthorised changes while it is moving in your CI/CD pipelines, you can add code signature. Signing the code will confirm that it comes from a trusted source and is unaltered. [AWS Signer](../../../signer/latest/developerguide/Welcome.md "../../../signer/latest/developerguide/Welcome.md") integrates with AWS Lambda to sign the code and enforce that only trusted code is deployed into your runtime. Store your secrets, such as database passwords or API keys, in a secrets manager that allows for rotation, secure and audited access. Secrets Manager allows fine-grained policies for secrets including auditing. |
