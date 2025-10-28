# Troubleshoot your Application Load Balancers

The following information can help you troubleshoot issues with your Application Load Balancer.

###### Issues

- [A registered target is not in service](#target-not-inservice "#target-not-inservice")
- [Clients cannot connect to an internet-facing
  load balancer](#client-cannot-connect "#client-cannot-connect")
- [Requests sent to a custom domain aren't received by the load balancer](#custom-domain-request "#custom-domain-request")
- [HTTPS requests sent to the load balancer return "NET::ERR_CERT_COMMON_NAME_INVALID"](#https-cert-invalid "#https-cert-invalid")
- [Load balancer shows elevated processing
  times](#elevated-processing-time "#elevated-processing-time")
- [The load balancer sends a response code of
  000](#response-code-000 "#response-code-000")
- [The load balancer generates an HTTP
  error](#load-balancer-http-error-codes "#load-balancer-http-error-codes")
- [A target generates an HTTP error](#target-http-errors "#target-http-errors")
- [An AWS Certificate Manager certificate is not available for use](#acm-cert-unavailable "#acm-cert-unavailable")
- [Multi-Line headers are not supported](#multi-line-headers-issue "#multi-line-headers-issue")
- [Troubleshoot unhealthy targets using the resource map](#troubleshoot-with-resourcemap "#troubleshoot-with-resourcemap")

## A registered target is not in service

If a target is taking longer than expected to enter the `InService` state,
it might be failing health checks. Your target is not in service until it passes one
health check. For more information, see [Health checks for Application Load Balancer target groups](target-group-health-checks.md "target-group-health-checks.md").

Verify that your instance is failing health checks and then check for the following
issues:

**A security group does not allow traffic**

The security group associated with an instance must allow traffic from the
load balancer using the health check port and health check protocol. You can
add a rule to the instance security group to allow all traffic from the load
balancer security group. Also, the security group for your load balancer
must allow traffic to the instances.

**A network access control list (ACL) does not allow traffic**

The network ACL associated with the subnets for your instances must allow
inbound traffic on the health check port and outbound traffic on the
ephemeral ports (1024-65535). The network ACL associated with the subnets
for your load balancer nodes must allow inbound traffic on the ephemeral
ports and outbound traffic on the health check and ephemeral ports.

**The ping path does not exist**

Create a target page for the health check and specify its path as the ping
path.

**The connection times out**

First, verify that you can connect to the target directly from within the
network using the private IP address of the target and the health check
protocol. If you can't connect, check whether the instance is over-utilized,
and add more targets to your target group if it is too busy to respond. If
you can connect, it is possible that the target page is not responding
before the health check timeout period. Choose a simpler target page for the
health check or adjust the health check settings.

**The target did not return a successful response code**

By default, the success code is 200, but you can optionally specify
additional success codes when you configure health checks. Confirm the
success codes that the load balancer is expecting and that your application
is configured to return these codes on success.

**The target response code was malformed or there was an error connecting to the
target**

Verify that your application responds to the load balancer's health check requests.
Some applications require additional configuration to respond to health checks, such
as a virtual host configuration to respond to the HTTP host header sent by the load
balancer. The host header value contains the private IP address of the target, followed
by the health check port when not using a default port. If the target uses a default
health check port, the host header value contains only the private IP address of the
target. For example, if your target’s private IP address is `10.0.0.10` and it's health
check port is `8080`, the HTTP Host header sent by the load balancer in health checks is
`Host: 10.0.0.10:8080`. If your target’s private IP address is `10.0.0.10` and it's health
check port is `80` then the HTTP Host header sent by the load balancer in health checks is
`Host: 10.0.0.10`. A virtual host configuration to respond to that host, or a default configuration,
may be required to successfully health check your application. Health check requests have the
following attributes: the `User-Agent` is set to `ELB-HealthChecker/2.0`, the line terminator for
message-header fields is the sequence CRLF, and the header terminates at the first empty line
followed by a CRLF.

## Clients cannot connect to an internet-facing

load balancer

If the load balancer is not responding to requests, check for the following
issues:

**Your internet-facing load balancer is attached to a private subnet**

You must specify public subnets for your load balancer. A public subnet
has a route to the Internet Gateway for your virtual private cloud
(VPC).

**A security group or network ACL does not allow traffic**

The security group for the load balancer and any network ACLs for the load
balancer subnets must allow inbound traffic from the clients and outbound
traffic to the clients on the listener ports.

## Requests sent to a custom domain aren't received by the load balancer

If the load balancer is not receiving requests sent to a custom domain, check for the following issues:

**The custom domain name does not resolve to the load balancer IP address**

- Confirm what IP address the custom domain name resolves to using a command line interface.
  - Linux, macOS, or Unix – You can use the `dig` command within Terminal. Ex.`dig example.com`
  - Windows – You can use the `nslookup` command within Command Prompt. Ex.`nslookup example.com`

- Confirm what IP address the load balancers DNS name resolves to using a command line interface.
- Compare the results of the two outputs. The IP addresses must match.

If using Route 53 to host your custom domain, see [My domain
is unavailable on the internet](../../../Route53/latest/DeveloperGuide/troubleshooting-domain-unavailable.md "../../../Route53/latest/DeveloperGuide/troubleshooting-domain-unavailable.md") in the _Amazon Route 53 Developer Guide_.

## HTTPS requests sent to the load balancer return "NET::ERR_CERT_COMMON_NAME_INVALID"

If HTTPS requests are receiving `NET::ERR_CERT_COMMON_NAME_INVALID` from the load balancer, check the following possible causes:

- The domain name used in the HTTPS request does not match the alternate name specified in the listeners associated ACM certificate.
- The load balancers default DNS name is being used. The default DNS name cannot be used to
  make HTTPS requests as a public certificate cannot be requested for the `*.amazonaws.com` domain.

## Load balancer shows elevated processing

times

The load balancer counts processing times differently based on configuration.

- If AWS WAF is associated with your Application Load Balancer and a client sends an HTTP POST
  request, the time to send the data for POST requests is reflected in the
  `request_processing_time` field in the load balancer access logs.
  This behavior is expected for HTTP POST requests.
- If AWS WAF is not associated with your Application Load Balancer and a client sends an HTTP POST
  request, the time to send the data for POST requests is reflected in the
  `target_processing_time` field in the load balancer access logs.
  This behavior is expected for HTTP POST requests.

## The load balancer sends a response code of

000

With HTTP/2 connections, if the number of requests served through one connection exceeds 10,000, the
load balancer sends a GOAWAY frame and closes the connection with a TCP FIN.

## The load balancer generates an HTTP

error

The following HTTP errors are generated by the load balancer. The load balancer sends
the HTTP code to the client, saves the request to the access log, and increments the
`HTTPCode_ELB_4XX_Count` or `HTTPCode_ELB_5XX_Count`
metric.

###### Errors

- [HTTP 400: Bad request](#http-400-issues "#http-400-issues")
- [HTTP 401: Unauthorized](#http-401-issues "#http-401-issues")
- [HTTP 403: Forbidden](#http-403-issues "#http-403-issues")
- [HTTP 405: Method not allowed](#http-405-issues "#http-405-issues")
- [HTTP 408: Request timeout](#http-408-issues "#http-408-issues")
- [HTTP 413: Payload too large](#http-413-issues "#http-413-issues")
- [HTTP 414: URI too long](#http-414-issues "#http-414-issues")
- [HTTP 460](#http-460-issues "#http-460-issues")
- [HTTP 463](#http-463-issues "#http-463-issues")
- [HTTP 464](#http-464-issues "#http-464-issues")
- [HTTP 500: Internal server error](#http-500-issues "#http-500-issues")
- [HTTP 501: Not implemented](#http-501-issues "#http-501-issues")
- [HTTP 502: Bad gateway](#http-502-issues "#http-502-issues")
- [HTTP 503: Service unavailable](#http-503-issues "#http-503-issues")
- [HTTP 504: Gateway timeout](#http-504-issues "#http-504-issues")
- [HTTP 505: Version not supported](#http-505-issues "#http-505-issues")
- [HTTP 507: Insufficient Storage](#http-507-issues "#http-507-issues")
- [HTTP 561: Unauthorized](#http-561-issues "#http-561-issues")

### HTTP 400: Bad request

Possible causes:

- The client sent a malformed request that does not meet the HTTP
  specification.
- The request header exceeded 16 K per request line, 16 K per single header,
  or 64 K for the entire request header.
- The client closed the connection before sending the full request
  body.

### HTTP 401: Unauthorized

You configured a listener rule to authenticate users, but one of the following is
true:

- You configured `OnUnauthenticatedRequest` to deny
  unauthenticated users or the IdP denied access.
- The size of the claims returned by the IdP exceeded the maximum size
  supported by the load balancer.
- A client submitted an HTTP/1.0 request without a host header, and the load
  balancer was unable to generate a redirect URL.
- The requested scope doesn't return an ID token.
- You don't complete the login process before the client login timeout
  expires. For more information see, [Client login timeout](listener-authenticate-users.md#client-login-timeout "listener-authenticate-users.md#client-login-timeout").

### HTTP 403: Forbidden

You configured an AWS WAF web access control list (web ACL) to monitor requests
to your Application Load Balancer and it blocked a request.

### HTTP 405: Method not allowed

The client used the TRACE method, which is not supported by Application Load Balancers.

### HTTP 408: Request timeout

The client did not send data before the idle timeout period expired. Sending a TCP
keep-alive does not prevent this timeout. Send at least 1 byte of data before each
idle timeout period elapses. Increase the length of the idle timeout period as
needed.

### HTTP 413: Payload too large

Possible causes:

- The target is a Lambda function and the request body exceeds 1 MB.
- The request header exceeded 16 K per request line, 16 K per single header,
  or 64 K for the entire request header.

### HTTP 414: URI too long

The request URL or query string parameters are too large.

### HTTP 460

The load balancer received a request from a client, but the client closed the
connection with the load balancer before the idle timeout period elapsed.

Check whether the client timeout period is greater than the idle timeout period
for the load balancer. Ensure that your target provides a response to the client
before the client timeout period elapses, or increase the client timeout period to
match the load balancer idle timeout, if the client supports this.

### HTTP 463

The load balancer received an **X-Forwarded-For** request header
with too many IP addresses. The upper limit for IP addresses is 30.

### HTTP 464

The load balancer received an incoming request protocol that is incompatible with
the version config of the target group protocol.

Possible causes:

- The request protocol is an HTTP/1.1, while the target group protocol
  version is a gRPC or HTTP/2.
- The request protocol is a gRPC, while the target group protocol version
  is an HTTP/1.1.
- The request protocol is an HTTP/2 and the request is not POST, while
  target group protocol version is a gRPC.

### HTTP 500: Internal server error

Possible causes:

- You configured an AWS WAF web access control list (web ACL) and there
  was an error executing the web ACL rules.
- The load balancer is unable to communicate with the IdP token endpoint or
  the IdP user info endpoint.
  - Verify that the IdP's DNS is publicly resolvable.
  - Verify that the security groups for your load balancer and the network
    ACLs for your VPC allow outbound access to these endpoints.
  - Verify that your VPC has internet access. If you have an internal-facing
    load balancer, use a NAT gateway to enable internet access.

- The user claim received from the IdP is greater than 11KB in size.
- The IdP token endpoint or the IdP user info endpoint is taking longer
  than 5 seconds to respond.

### HTTP 501: Not implemented

The load balancer received a **Transfer-Encoding** header with an
unsupported value. The supported values for **Transfer-Encoding**
are `chunked` and `identity`. As an alternative, you can use
the **Content-Encoding** header.

### HTTP 502: Bad gateway

Possible causes:

- The load balancer received a TCP RST from the target when attempting to
  establish a connection.
- The load balancer received an unexpected response from the target, such as
  "ICMP Destination unreachable (Host unreachable)", when attempting to
  establish a connection. Check whether traffic is allowed from the load
  balancer subnets to the targets on the target port.
- The target closed the connection with a TCP RST or a TCP FIN while the
  load balancer had an outstanding request to the target. Check whether the
  keep-alive duration of the target is shorter than the idle timeout value of
  the load balancer.
- The target response is malformed or contains HTTP headers that are not
  valid.
- The target response header exceeded 32 K for the entire response header.
- The deregistration delay period elapsed for a request being handled by a
  target that was deregistered. Increase the delay period so that lengthy
  operations can complete.
- The target is a Lambda function and the response body exceeds 1 MB.
- The target is a Lambda function that did not respond before its configured
  timeout was reached.
- The target is a Lambda function that returned an error or the function was
  throttled by the Lambda service.
- The load balancer encountered an SSL handshake error when connecting to a target.

For more information see [How do I troubleshoot Application Load Balancer HTTP 502 errors](https://repost.aws/knowledge-center/elb-alb-troubleshoot-502-errors "https://repost.aws/knowledge-center/elb-alb-troubleshoot-502-errors") in the AWS Support Knowledge Center.

### HTTP 503: Service unavailable

The target groups for the load balancer have no registered targets,
or all of the registered targets are in an `unused` state.

### HTTP 504: Gateway timeout

Possible causes:

- The load balancer failed to establish a connection to the target before
  the connection timeout expired (10 seconds).
- The load balancer established a connection to the target but the target
  did not respond before the idle timeout period elapsed.
- The networks ACL or SecurityGroup Policies did not allow traffic from
  the targets to the load balancer nodes on the ephemeral ports (1024-65535).
- The target returns a content-length header that is larger than the entity
  body. The load balancer timed out waiting for the missing bytes.
- The target is a Lambda function and the Lambda service did not respond
  before the connection timeout expired.
- The load balancer encountered an SSL handshake
  timeout (10 seconds) when connecting to a target.

### HTTP 505: Version not supported

The load balancer received an unexpected HTTP version request. For example, the
load balancer established an HTTP/1 connection but received an HTTP/2
request.

### HTTP 507: Insufficient Storage

The redirect URL is too long.

### HTTP 561: Unauthorized

You configured a listener rule to authenticate users, but the IdP returned an
error code when authenticating the user. Check your access logs for the related
[error reason code](load-balancer-access-logs.md#error-reason-codes "load-balancer-access-logs.md#error-reason-codes").

## A target generates an HTTP error

The load balancer forwards valid HTTP responses from targets to the client, including
HTTP errors. The HTTP errors generated by a target are recorded in the
`HTTPCode_Target_4XX_Count` and `HTTPCode_Target_5XX_Count`
metrics.

## An AWS Certificate Manager certificate is not available for use

When deciding to use an HTTPS listener with your Application Load Balancer, AWS Certificate Manager requires you to validate domain
ownership before issuing a certificate. If this step is missed during setup, the certificate
remains in the `Pending Validation` state, and not available for use until validated.

- If using email validation, see [Email validation](../../../acm/latest/userguide/email-validation.md "../../../acm/latest/userguide/email-validation.md") in the _AWS Certificate Manager User Guide_.
- If using DNS validation, see [DNS validation](../../../acm/latest/userguide/dns-validation.md "../../../acm/latest/userguide/dns-validation.md") in the _AWS Certificate Manager User Guide_.

## Multi-Line headers are not supported

Application Load Balancers do not support multi-line headers, including the `message/http` media
type header. When a multi-line header is provided the Application Load Balancer appends a colon character,
"`:`", before passing it to the target.

## Troubleshoot unhealthy targets using the resource map

If your Application Load Balancer targets are failing health checks, you can use the
resource map to find unhealthy targets and take actions based
on the failure reason code. For more information, see
[View the Application Load Balancer resource map](view-resource-map.md "view-resource-map.md").

Resource map provides two views: **Overview**, and **Unhealthy
Target Map**. **Overview** is selected by default and displays
all of your load balancer's resources. Selecting the **Unhealthy Target Map**
view will display only the unhealthy targets in each target group associated to the Application Load Balancer.

###### Note

You must enable **Show resource details** to view the health
check summary and error messages for all applicable resources within the resource map.
When not enabled, you must select each resource to view its details.

The **Target groups** column displays a summary of the healthy and
unhealthy targets for each target group. This can help determine if all the targets
are failing health checks, or only specific targets are failing. If all targets in a
target group are failing health checks, check the configuration of the target group.
Select a target groups name to open its detail page in a new tab.

The **Targets** column displays the TargetID and the current health
check status for each target. When a target is unhealthy, the health check failure
reason code is displayed. When a single target is failing a health check, verify the
target has sufficient resources and confirm that applications running on the target
are available. Select a targets ID to open its detail page in a new tab.

Selecting **Export** gives you the option of exporting the current
view of your Application Load Balancer's resource map as a PDF.

Verify that your instance is failing health checks and then based on the failure
reason code check for the following issues:

- **Unhealthy: HTTP Response Mismatch**
  - Verify the application running on the target is sending the correct HTTP response to
    the Application Load Balancer's health check requests.
  - Alternatively, you can update the Application Load Balancer's health check request to match the response
    from the application running on the target.

- **Unhealthy: Request timed out**
  - Verify the security groups and network access control lists (ACL) associated
    with your targets and Application Load Balancer are not blocking connectivity.
  - Verify the target has sufficient resources available to accept connections
    from the Application Load Balancer.
  - Verify the status of any applications running on the target.
  - The Application Load Balancer's health check responses can be viewed in each target's
    application logs. For more information, see
    [Health check reason codes](target-group-health-checks.md#target-health-reason-codes "target-group-health-checks.md#target-health-reason-codes").

- **Unhealthy: FailedHealthChecks**
  - Verify the status of any applications running on the target.
  - Verify the target is listening for traffic on the health check port.

  ###### When using an HTTPS listener

  You choose which security policy is used for front-end connections.
  The security policy used for back-end connections is automatically selected
  based on the front-end security policy in use.

      - If your HTTPS listener is using a TLS 1.3 security policy for
       front-end connections, the `ELBSecurityPolicy-TLS13-1-0-2021-06`
       security policy is used for back-end connections.
      - If your HTTPS listener is not using a TLS 1.3 security policy for
       front-end connections, the `ELBSecurityPolicy-2016-08`
       security policy is used for back-end connections.For more information, see

  [Security policies](describe-ssl-policies.md "describe-ssl-policies.md").
  - Verify the target is providing a server certificate and key in the correct format
    specified by the security policy.
  - Verify the target supports one or more matching ciphers, and a protocol provided
    by the Application Load Balancer to establish TLS handshakes.
