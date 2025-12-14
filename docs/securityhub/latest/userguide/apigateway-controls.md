# Security Hub CSPM controls for Amazon API Gateway

These AWS Security Hub CSPM controls evaluate the Amazon API Gateway service and resources. The controls might not
be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [APIGateway.1] API Gateway REST and WebSocket API execution logging

should be enabled

**Related requirements:** NIST.800-53.r5 AC-4(26),
NIST.800-53.r5 AU-10, NIST.800-53.r5 AU-12, NIST.800-53.r5 AU-2, NIST.800-53.r5 AU-3,
NIST.800-53.r5 AU-6(3), NIST.800-53.r5 AU-6(4), NIST.800-53.r5 CA-7, NIST.800-53.r5 SC-7(9),
NIST.800-53.r5 SI-7(8)

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:**
`AWS::ApiGateway::Stage`, `AWS::ApiGatewayV2::Stage`

**AWS Config rule:**
[api-gw-execution-logging-enabled](../../../config/latest/developerguide/api-gw-execution-logging-enabled.md "../../../config/latest/developerguide/api-gw-execution-logging-enabled.md")

**Schedule type:** Change triggered

**Parameters:**

| Parameter      | Description   | Type | Allowed custom values | Security Hub CSPM default value |
| -------------- | ------------- | ---- | --------------------- | ------------------------------- |
| `loggingLevel` | Logging level | Enum | `ERROR`, `INFO`       | `No default value`              |

This control checks whether all stages of an Amazon API Gateway REST or WebSocket API have logging
enabled. The control fails if the `loggingLevel` isn't `ERROR` or `INFO` for all stages of the API.
Unless you provide custom parameter values to indicate that a specific log type should be enabled, Security Hub CSPM produces a passed finding if the
logging level is either `ERROR` or `INFO`.

API Gateway REST or WebSocket API stages should have relevant logs enabled. API Gateway REST and
WebSocket API execution logging provides detailed records of requests made to API Gateway REST and
WebSocket API stages. The stages include API integration backend responses, Lambda authorizer
responses, and the `requestId` for AWS integration endpoints.

### Remediation

To enable logging for REST and WebSocket API operations, see [Set up CloudWatch API logging using the API Gateway console](../../../apigateway/latest/developerguide/set-up-logging.md#set-up-access-logging-using-console "../../../apigateway/latest/developerguide/set-up-logging.md#set-up-access-logging-using-console") in the _API Gateway Developer Guide_.

## [APIGateway.2] API Gateway REST API stages should be configured to use

SSL certificates for backend authentication

**Related requirements:** NIST.800-53.r5 AC-17(2),
NIST.800-53.r5 AC-4, NIST.800-53.r5 IA-5(1), NIST.800-53.r5 SC-12(3), NIST.800-53.r5
SC-13, NIST.800-53.r5 SC-23, NIST.800-53.r5 SC-23(3), NIST.800-53.r5 SC-7(4),
NIST.800-53.r5 SC-8, NIST.800-53.r5 SC-8(1), NIST.800-53.r5 SC-8(2), NIST.800-53.r5
SI-7(6), NIST.800-171.r2 3.13.15

**Category:** Protect > Data Protection > Encryption of data-in-transit

**Severity:** Medium

**Resource type:**
`AWS::ApiGateway::Stage`

**AWS Config rule:**
[api-gw-ssl-enabled](../../../config/latest/developerguide/api-gw-ssl-enabled.md "../../../config/latest/developerguide/api-gw-ssl-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether Amazon API Gateway REST API stages have SSL certificates configured.
Backend systems use these certificates to authenticate that incoming requests are from
API Gateway.

API Gateway REST API stages should be configured with SSL certificates to allow backend systems to
authenticate that requests originate from API Gateway.

### Remediation

For detailed instructions on how to generate and configure API Gateway REST API SSL certificates,
see [Generate and configure an SSL certificate for backend authentication](../../../apigateway/latest/developerguide/getting-started-client-side-ssl-authentication.md "../../../apigateway/latest/developerguide/getting-started-client-side-ssl-authentication.md") in the _API Gateway Developer Guide_.

## [APIGateway.3] API Gateway REST API stages should have AWS X-Ray

tracing enabled

**Related requirements:** NIST.800-53.r5 CA-7

**Category:** Detect > Detection services

**Severity:** Low

**Resource type:**
`AWS::ApiGateway::Stage`

**AWS Config rule:**
[api-gw-xray-enabled](../../../config/latest/developerguide/api-gw-xray-enabled.md "../../../config/latest/developerguide/api-gw-xray-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether AWS X-Ray active tracing is enabled for your Amazon API Gateway REST API
stages.

X-Ray active tracing enables a more rapid response to performance changes in the underlying
infrastructure. Changes in performance could result in a lack of availability of the API. X-Ray
active tracing provides real-time metrics of user requests that flow through your API Gateway REST API
operations and connected services.

### Remediation

For detailed instructions on how to enable X-Ray active tracing for API Gateway REST API
operations, see [Amazon API Gateway active tracing support for
AWS X-Ray](../../../xray/latest/devguide/xray-services-apigateway.md "../../../xray/latest/devguide/xray-services-apigateway.md") in the _AWS X-Ray Developer Guide_.

## [APIGateway.4] API Gateway should be associated with a WAF Web

ACL

**Related requirements:** NIST.800-53.r5 AC-4(21)

**Category:** Protect > Protective services

**Severity:** Medium

**Resource type:**
`AWS::ApiGateway::Stage`

**AWS Config rule:**
[api-gw-associated-with-waf](../../../config/latest/developerguide/api-gw-associated-with-waf.md "../../../config/latest/developerguide/api-gw-associated-with-waf.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an API Gateway stage uses an AWS WAF web access control list (ACL). This
control fails if an AWS WAF web ACL is not attached to a REST API Gateway stage.

AWS WAF is a web application firewall that helps protect web applications and APIs from
attacks. It enables you to configure an ACL, which is a set of rules that allow, block, or count
web requests based on customizable web security rules and conditions that you define. Ensure that
your API Gateway stage is associated with an AWS WAF web ACL to help protect it from malicious
attacks.

### Remediation

For information on how to use the API Gateway console to associate an AWS WAF Regional web ACL with
an existing API Gateway API stage, see [Using AWS WAF
to protect your APIs](../../../apigateway/latest/developerguide/apigateway-control-access-aws-waf.md "../../../apigateway/latest/developerguide/apigateway-control-access-aws-waf.md") in the _API Gateway Developer Guide_.

## [APIGateway.5] API Gateway REST API cache data should be encrypted at

rest

**Related requirements:** NIST.800-53.r5 CA-9(1),
NIST.800-53.r5 CM-3(6), NIST.800-53.r5 SC-13, NIST.800-53.r5 SC-28, NIST.800-53.r5 SC-28(1),
NIST.800-53.r5 SC-7(10), NIST.800-53.r5 SI-7(6)

**Category:** Protect > Data protection > Encryption of data at
rest

**Severity:** Medium

**Resource type:**
`AWS::ApiGateway::Stage`

**AWS Config rule:** `api-gw-cache-encrypted` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether all methods in API Gateway REST API stages that have cache enabled are
encrypted. The control fails if any method in an API Gateway REST API stage is configured to cache and
the cache is not encrypted. Security Hub CSPM evaluates the encryption of a particular method only when caching
is enabled for that method.

Encrypting data at rest reduces the risk of data stored on disk being accessed by a user not
authenticated to AWS. It adds another set of access controls to limit unauthorized users
ability access the data. For example, API permissions are required to decrypt the data before it
can be read.

API Gateway REST API caches should be encrypted at rest for an added layer of security.

### Remediation

To configure API caching for a stage, see [Enable Amazon API Gateway caching](../../../apigateway/latest/developerguide/api-gateway-caching.md#enable-api-gateway-caching "../../../apigateway/latest/developerguide/api-gateway-caching.md#enable-api-gateway-caching") in the _API Gateway Developer Guide_.
In **Cache Settings**, choose **Encrypt cache data**.

## [APIGateway.8] API Gateway routes should specify an authorization

type

**Related requirements:** NIST.800-53.r5 AC-3, NIST.800-53.r5
CM-2, NIST.800-53.r5 CM-2(2)

**Category:** Protect > Secure Access Management

**Severity:** Medium

**Resource type:**
`AWS::ApiGatewayV2::Route`

**AWS Config rule:**
[api-gwv2-authorization-type-configured](../../../config/latest/developerguide/api-gwv2-authorization-type-configured.md "../../../config/latest/developerguide/api-gwv2-authorization-type-configured.md")

**Schedule type:** Periodic

**Parameters:**

| Parameter           | Description                          | Type | Allowed custom values      | Security Hub CSPM default value |
| ------------------- | ------------------------------------ | ---- | -------------------------- | ------------------------------- |
| `authorizationType` | Authorization type of the API routes | Enum | `AWS_IAM`, `CUSTOM`, `JWT` | No default value                |

This control checks if Amazon API Gateway routes have an authorization type. The control fails if the
API Gateway route doesn't have any authorization type. Optionally, you can provide a custom parameter value
if you want the control to pass only if the route uses the authorization type specified in the `authorizationType` parameter.

API Gateway supports multiple mechanisms for controlling and managing access to your API. By
specifying an authorization type, you can restrict access to your API to only authorized users or
processes.

### Remediation

To set an authorization type for HTTP APIs, see [Controlling and managing
access to an HTTP API in API Gateway](../../../apigateway/latest/developerguide/http-api-access-control.md "../../../apigateway/latest/developerguide/http-api-access-control.md") in the _API Gateway Developer Guide_. To
set an authorization type for WebSocket APIs, see [Controlling
and managing access to a WebSocket API in API Gateway](../../../apigateway/latest/developerguide/apigateway-websocket-api-control-access.md "../../../apigateway/latest/developerguide/apigateway-websocket-api-control-access.md") in the
_API Gateway Developer Guide_.

## [APIGateway.9] Access logging should be configured for API Gateway V2

Stages

**Related requirements:** NIST.800-53.r5 AC-4(26),
NIST.800-53.r5 AU-10, NIST.800-53.r5 AU-12, NIST.800-53.r5 AU-2, NIST.800-53.r5 AU-3,
NIST.800-53.r5 AU-6(3), NIST.800-53.r5 AU-6(4), NIST.800-53.r5 CA-7, NIST.800-53.r5 SC-7(9),
NIST.800-53.r5 SI-7(8), PCI DSS v4.0.1/10.4.2

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:**
`AWS::ApiGatewayV2::Stage`

**AWS Config rule:**
[api-gwv2-access-logs-enabled](../../../config/latest/developerguide/api-gwv2-access-logs-enabled.md "../../../config/latest/developerguide/api-gwv2-access-logs-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks if Amazon API Gateway V2 stages have access logging configured. This control
fails if access log settings aren't defined.

API Gateway access logs provide detailed information about who has accessed your API and how the
caller accessed the API. These logs are useful for applications such as security and access
audits and forensics investigation. Enable these access logs to analyze traffic patterns and to
troubleshoot issues.

For additional best practices, see [Monitoring REST APIs](../../../apigateway/latest/developerguide/rest-api-monitor.md "../../../apigateway/latest/developerguide/rest-api-monitor.md") in the
_API Gateway Developer Guide_.

### Remediation

To set up access logging, see [Set up CloudWatch API logging using the API Gateway console](../../../apigateway/latest/developerguide/set-up-logging.md#set-up-access-logging-using-console "../../../apigateway/latest/developerguide/set-up-logging.md#set-up-access-logging-using-console") in the
_API Gateway Developer Guide_.
