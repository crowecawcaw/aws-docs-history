# Edit attributes for your Application Load Balancer

After you create an Application Load Balancer, you can edit its attributes.

###### Load balancer attributes

- [Connection idle timeout](#connection-idle-timeout "#connection-idle-timeout")
- [HTTP client keepalive duration](#http-client-keep-alive-duration "#http-client-keep-alive-duration")
- [Deletion protection](#deletion-protection "#deletion-protection")
- [Desync mitigation mode](#desync-mitigation-mode "#desync-mitigation-mode")
- [Host header preservation](#host-header-preservation "#host-header-preservation")

## Connection idle timeout

The connection idle timeout is the period of time an existing client or target
connection can remain inactive, with no data being sent or received, before the
load balancer closes the connection.

To ensure that lengthy operations such as file uploads have time to complete, send
at least 1 byte of data before each idle timeout period elapses and increase the
length of the idle timeout period as needed. We also recommend that you configure the
idle timeout of your application to be larger than the idle timeout configured for
the load balancer. Otherwise, if the application closes the TCP connection to the
load balancer ungracefully, the load balancer might send a request to the application
before it receives the packet indicating that the connection is closed. If this is
the case, then the load balancer sends an HTTP 502 Bad Gateway error to the client.

Application Load Balancers do not support HTTP/2 PING frames. These do not reset the connection idle timeout.

By default, ELB sets the idle timeout value for your load balancer to 60 seconds.

Console

###### To update the connection idle timeout value

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, choose **Load Balancers**.
3. Select the load balancer.
4. On the **Attributes** tab, choose **Edit**.
5. Under **Traffic configuration**, enter a value for
   **Connection idle timeout**. The valid range is 1
   through 4000 seconds.
6. Choose **Save changes**.

AWS CLI

###### To update the connection idle timeout value

Use the [modify-load-balancer-attributes](../../../cli/latest/reference/elbv2/modify-load-balancer-attributes.md "../../../cli/latest/reference/elbv2/modify-load-balancer-attributes.md") command with the
`idle_timeout.timeout_seconds` attribute. The valid range is
1 to 4000 seconds.

```
aws elbv2 modify-load-balancer-attributes \
    --load-balancer-arn `load-balancer-arn` \
    --attributes "Key=idle_timeout.timeout_seconds,Value=`120`"
```

CloudFormation

###### To update the connection idle timeout value

Update the [AWS::ElasticLoadBalancingV2::LoadBalancer](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.md") resource
to include the `idle_timeout.timeout_seconds` attribute.
The valid range is 1 to 4000 seconds.

```
Resources:
  myLoadBalancer:
    Type: 'AWS::ElasticLoadBalancingV2::LoadBalancer'
    Properties:
      Name: my-alb
      Type: application
      Scheme: internal
      Subnets:
        - !Ref subnet-AZ1
        - !Ref subnet-AZ2
      SecurityGroups:
        - !Ref mySecurityGroup
      LoadBalancerAttributes:
        - Key: "idle_timeout.timeout_seconds"
          Value: "`120`"
```

## HTTP client keepalive duration

The HTTP client keepalive duration is the maximum length of time that an Application Load Balancer maintains
a persistent HTTP connection to a client. After the configured HTTP client keepalive duration
elapses, the Application Load Balancer accepts one more request and then returns a response that gracefully closes
the connection.

The type of response sent by the load balancer depends on the HTTP version used by
the client connection.

- For clients connected using HTTP 1.x, the load balancer sends
  an HTTP header containing the field `Connection: close`.
- For clients connected using HTTP/2, the load balancer sends a `GOAWAY`
  frame.

By default, Application Load Balancer sets the HTTP client keepalive duration value for load balancers to 3600
seconds, or 1 hour. The HTTP client keepalive duration cannot be turned off or set below the
minimum of 60 seconds, but you can increase the HTTP client keepalive duration, up to
a maximum of 604800 seconds, or 7 days. An Application Load Balancer begins the HTTP client
keepalive duration period when an HTTP connection to a client is initially established.
The duration period continues when there's no traffic, and does not reset until
a new connection is established.

When load balancer traffic is shifted away from an impaired Availability
Zone using zonal shift or zonal autoshift, clients with existing open connections might continue to
make requests against the impaired location until the clients reconnect.
To support faster recovery, consider setting
a lower keepalive duration value, to limit the amount of time that clients stay connected
to a load balancer. For more information, see [Limit the time that clients stay connected to your endpoints](../../../r53recovery/latest/dg/route53-arc-best-practices.md#arc-zonal-shift.existing-connections "../../../r53recovery/latest/dg/route53-arc-best-practices.md#arc-zonal-shift.existing-connections") in the
_Amazon Application Recovery Controller (ARC) Developer Guide_.

###### Note

When the load balancer switches the IP address type of your Application Load Balancer to `dualstack-without-public-ipv4`,
the load balancer waits for all active connections to complete. To decrease the amount of time it
takes to switch the IP address type for your Application Load Balancer, consider lowering the HTTP client keepalive duration.

The Application Load Balancer assigns the HTTP client keepalive duration value during the initial connection.
When you update the HTTP client keepalive duration, this can result in simultaneous connections
with different HTTP client keepalive duration values. Existing connections retain the
HTTP client keepalive duration value applied during its initial connection. New connections receive
the updated HTTP client keepalive duration value.

Console

###### To update the client keepalive duration

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, choose **Load Balancers**.
3. Select the load balancer.
4. On the **Attributes** tab, choose **Edit**.
5. Under **Traffic configuration**, enter a value for
   **HTTP client keepalive duration**. The valid range is
   60 to 604800 seconds.
6. Choose **Save changes**.

AWS CLI

###### To update the client keepalive duration

Use the [modify-load-balancer-attributes](../../../cli/latest/reference/elbv2/modify-load-balancer-attributes.md "../../../cli/latest/reference/elbv2/modify-load-balancer-attributes.md") command with the
`client_keep_alive.seconds` attribute. The valid range is
60 to 604800 seconds.

```
aws elbv2 modify-load-balancer-attributes \
    --load-balancer-arn `load-balancer-arn` \
    --attributes "Key=client_keep_alive.seconds,Value=`7200`"
```

CloudFormation

###### To update the client keepalive duration

Update the [AWS::ElasticLoadBalancingV2::LoadBalancer](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.md") resource
to include the `client_keep_alive.seconds` attribute.
The valid range is 60 to 604800 seconds.

```
Resources:
  myLoadBalancer:
    Type: 'AWS::ElasticLoadBalancingV2::LoadBalancer'
    Properties:
      Name: my-alb
      Type: application
      Scheme: internal
      Subnets:
        - !Ref subnet-AZ1
        - !Ref subnet-AZ2
      SecurityGroups:
        - !Ref mySecurityGroup
      LoadBalancerAttributes:
        - Key: "client_keep_alive.seconds"
          Value: "`7200`"
```

## Deletion protection

To prevent your load balancer from being deleted accidentally, you can enable deletion
protection. By default, deletion protection is disabled for your load balancer.

If you enable deletion protection for your load balancer, you must disable it before
you can delete the load balancer.

Console

###### To enable or disable deletion protection

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, choose **Load Balancers**.
3. Select the load balancer.
4. On the **Attributes** tab, choose **Edit**.
5. Under **Protection**, enable or disable **Deletion
   protection**.
6. Choose **Save changes**.

AWS CLI

###### To enable or disable deletion protection

Use the [modify-load-balancer-attributes](../../../cli/latest/reference/elbv2/modify-load-balancer-attributes.md "../../../cli/latest/reference/elbv2/modify-load-balancer-attributes.md") command with the
`deletion_protection.enabled` attribute.

```
aws elbv2 modify-load-balancer-attributes \
    --load-balancer-arn `load-balancer-arn` \
    --attributes "Key=deletion_protection.enabled,Value=`true`"
```

CloudFormation

###### To enable or disable deletion protection

Update the [AWS::ElasticLoadBalancingV2::LoadBalancer](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.md") resource
to include the `deletion_protection.enabled` attribute.

```
Resources:
  myLoadBalancer:
    Type: 'AWS::ElasticLoadBalancingV2::LoadBalancer'
    Properties:
      Name: my-alb
      Type: application
      Scheme: internal
      Subnets:
        - !Ref subnet-AZ1
        - !Ref subnet-AZ2
      SecurityGroups:
        - !Ref mySecurityGroup
      LoadBalancerAttributes:
        - Key: "deletion_protection.enabled"
          Value: "`true`"
```

## Desync mitigation mode

Desync mitigation mode protects your application from issues due to HTTP desync. The
load balancer classifies each request based on its threat level, allows safe requests,
and then mitigates risk as specified by the mitigation mode that you specify. The desync
mitigation modes are monitor, defensive, and strictest. The default is the defensive
mode, which provides durable mitigation against HTTP desync while maintaining the
availability of your application. You can switch to strictest mode to ensure that your
application receives only requests that comply with [RFC 7230](https://tools.ietf.org/html/rfc7230 "https://tools.ietf.org/html/rfc7230").

The http_desync_guardian library analyzes HTTP requests to prevent HTTP desync
attacks. For more information, see [HTTP Desync Guardian](https://github.com/aws/http-desync-guardian "https://github.com/aws/http-desync-guardian") on
GitHub.

###### Classifications

The classifications are as follows:

- Compliant — Request complies with RFC 7230 and poses no known security
  threats.
- Acceptable — Request does not comply with RFC 7230 but poses no known
  security threats.
- Ambiguous — Request does not comply with RFC 7230 but poses a risk, as
  various web servers and proxies could handle it differently.
- Severe — Request poses a high security risk. The load balancer blocks
  the request, serves a 400 response to the client, and closes the client
  connection.

If a request does not comply with RFC 7230, the load balancer increments the
`DesyncMitigationMode_NonCompliant_Request_Count` metric. For more
information, see [Application Load Balancer metrics](load-balancer-cloudwatch-metrics.md#load-balancer-metrics-alb "load-balancer-cloudwatch-metrics.md#load-balancer-metrics-alb").

The classification for each request is included in the load balancer access logs. If
the request does not comply, the access logs include a classification reason code. For
more information, see [Classification reasons](load-balancer-access-logs.md#classification-reasons "load-balancer-access-logs.md#classification-reasons").

###### Modes

The following table describes how Application Load Balancers treat requests based on mode and
classification.

| Classification | Monitor mode | Defensive mode | Strictest mode |
| -------------- | ------------ | -------------- | -------------- |
| Compliant      | Allowed      | Allowed        | Allowed        |
| Acceptable     | Allowed      | Allowed        | Blocked        |
| Ambiguous      | Allowed      | Allowed¹       | Blocked        |
| Severe         | Allowed      | Blocked        | Blocked        |

¹ Routes the requests but closes the client and target connections. You might
incur additional charges if your load balancer receives a large number of Ambiguous
requests in Defensive mode. This is because the increased number of new connections per
second contributes to the Load Balancer Capacity Units (LCU) used per hour. You can use
the `NewConnectionCount` metric to compare how your load balancer establishes
new connections in Monitor mode and Defensive mode.

Console

###### To update desync mitigation mode

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, choose **Load Balancers**.
3. Select the load balancer.
4. On the **Attributes** tab, choose **Edit**.
5. Under **Traffic configuration**, **Packet handling**,
   for **Desync mitigation mode**, choose **Defensive**,
   **Strictest**, or **Monitor**.
6. Choose **Save changes**.

AWS CLI

###### To update desync mitigation mode

Use the [modify-load-balancer-attributes](../../../cli/latest/reference/elbv2/modify-load-balancer-attributes.md "../../../cli/latest/reference/elbv2/modify-load-balancer-attributes.md") command with the
`routing.http.desync_mitigation_mode` attribute. The possible values
are `monitor`, `defensive`, or `strictest`.
The default is `defensive`.

```
aws elbv2 modify-load-balancer-attributes \
    --load-balancer-arn `load-balancer-arn` \
    --attributes "Key=routing.http.desync_mitigation_mode,Value=`monitor`"
```

CloudFormation

###### To update desync mitigation mode

Update the [AWS::ElasticLoadBalancingV2::LoadBalancer](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.md") resource
to include the `routing.http.desync_mitigation_mode` attribute.
The possible values are `monitor`, `defensive`, or `strictest`.
The default is `defensive`.

```
Resources:
  myLoadBalancer:
    Type: 'AWS::ElasticLoadBalancingV2::LoadBalancer'
    Properties:
      Name: my-alb
      Type: application
      Scheme: internal
      Subnets:
        - !Ref subnet-AZ1
        - !Ref subnet-AZ2
      SecurityGroups:
        - !Ref mySecurityGroup
      LoadBalancerAttributes:
        - Key: "routing.http.desync_mitigation_mode"
          Value: "`monitor`"
```

## Host header preservation

When you enable the **Preserve host header** attribute,
the Application Load Balancer preserves the `Host` header in the HTTP request, and sends the
header to targets without any modification. If the Application Load Balancer receives multiple
`Host` headers, it preserves all of them. Listener rules are applied only
to the first `Host` header received.

By default, when the **Preserve host header** attribute
is not enabled, the Application Load Balancer modifies the `Host` header in the following manner:

**When host header preservation is not enabled, and listener port
is a non-default port**: When not using the default ports (ports 80 or 443)
we append the port number to the host header if it isn’t already appended by the client.
For example, the `Host` header in the HTTP request with `Host:
 www.example.com` would be modified to `Host: www.example.com:8080`,
if the listener port is a non-default port such as `8080`.

**When host header preservation is not enabled, and the listener
port is a default port (port 80 or 443)**: For default listener ports
(either port 80 or 443), we do not append the port number to the outgoing host header.
Any port number that was already in the incoming host header, is removed.

The following table shows more examples of how Application Load Balancers treat host headers in the HTTP
request based on listener port.

| Listener port                                                                                    | Example request                                                 | Host header in the request | Host header preservation is disabled (default behavior) | Host header preservation is enabled |
| ------------------------------------------------------------------------------------------------ | --------------------------------------------------------------- | -------------------------- | ------------------------------------------------------- | ----------------------------------- |
| Request is sent on default HTTP/HTTPS listener.                                                  | `GET /index.html HTTP/1.1 Host: example.com`                    | example.com                | example.com                                             | example.com                         |
| Request is sent on default HTTP listener and host header has a port<br>(for example, 80 or 443). | `GET /index.html HTTP/1.1 Host: example.com:80`                 | example.com:80             | example.com                                             | example.com:80                      |
| Request has an absolute path.                                                                    | `GET https://dns_name/index.html HTTP/1.1 Host:<br>example.com` | example.com                | dns_name                                                | example.com                         |
| Request is sent on a non-default listener port (for example, 8080)                               | `GET /index.html HTTP/1.1 Host: example.com`                    | example.com                | example.com:8080                                        | example.com                         |
| Request is sent on a non-default listener port and host header has<br>port (for example, 8080).  | `GET /index.html HTTP/1.1 Host: example.com:8080`               | example.com:8080           | example.com:8080                                        | example.com:8080                    |

Console

###### To enable host header preservation

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Load Balancers**.
3. Select the load balancer.
4. On the **Attributes** tab, choose **Edit**.
5. Under **Packet handling**, turn on **Preserve host header**.
6. Choose **Save changes**.

AWS CLI

###### To enable host header preservation

Use the [modify-load-balancer-attributes](../../../cli/latest/reference/elbv2/modify-load-balancer-attributes.md "../../../cli/latest/reference/elbv2/modify-load-balancer-attributes.md") command with the
`routing.http.preserve_host_header.enabled` attribute set to
`true`.

```
aws elbv2 modify-load-balancer-attributes \
    --load-balancer-arn `load-balancer-arn` \
    --attributes "Key=routing.http.preserve_host_header.enabled,Value=`true`"
```

CloudFormation

###### To enable host header preservation

Update the [AWS::ElasticLoadBalancingV2::LoadBalancer](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-elasticloadbalancingv2-loadbalancer.md") resource
to include the `routing.http.preserve_host_header.enabled` attribute.

```
Resources:
  myLoadBalancer:
    Type: 'AWS::ElasticLoadBalancingV2::LoadBalancer'
    Properties:
      Name: my-alb
      Type: application
      Scheme: internal
      Subnets:
        - !Ref subnet-AZ1
        - !Ref subnet-AZ2
      SecurityGroups:
        - !Ref mySecurityGroup
      LoadBalancerAttributes:
        - Key: "routing.http.preserve_host_header.enabled"
          Value: "`true`"
```
