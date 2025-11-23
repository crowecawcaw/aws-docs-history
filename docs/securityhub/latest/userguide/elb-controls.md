# Security Hub controls for ELB

These AWS Security Hub controls evaluate the Elastic Load Balancing service and resources. The controls might
not be available in all AWS Regions. For more information, see [Availability of controls by
Region](securityhub-regions.md#securityhub-regions-control-support "securityhub-regions.md#securityhub-regions-control-support").

## [ELB.1] Application Load Balancer should be configured to redirect all HTTP requests

to HTTPS

**Related requirements:** PCI DSS v3.2.1/2.3,PCI DSS
v3.2.1/4.1, NIST.800-53.r5 AC-17(2), NIST.800-53.r5 AC-4, NIST.800-53.r5 IA-5(1),
NIST.800-53.r5 SC-12(3), NIST.800-53.r5 SC-13, NIST.800-53.r5 SC-23, NIST.800-53.r5
SC-23(3), NIST.800-53.r5 SC-7(4), NIST.800-53.r5 SC-8, NIST.800-53.r5 SC-8(1),
NIST.800-53.r5 SC-8(2), NIST.800-53.r5 SI-7(6)

**Category:** Detect > Detection services

**Severity:** Medium

**Resource type:**
`AWS::ElasticLoadBalancingV2::LoadBalancer`

**AWS Config rule:**
[alb-http-to-https-redirection-check](../../../config/latest/developerguide/alb-http-to-https-redirection-check.md "../../../config/latest/developerguide/alb-http-to-https-redirection-check.md")

**Schedule type:** Periodic

**Parameters:** None

This control checks whether HTTP to HTTPS redirection is configured on all HTTP
listeners of Application Load Balancers. The control fails if any of the HTTP listeners
of Application Load Balancers do not have HTTP to HTTPS redirection configured.

Before you start to use your Application Load Balancer, you must add one or more
listeners. A listener is a process that uses the configured protocol and port to check
for connection requests. Listeners support both the HTTP and HTTPS protocols. You can
use an HTTPS listener to offload the work of encryption and decryption to your load
balancer. To enforce encryption in transit, you should use redirect actions with
Application Load Balancers to redirect client HTTP requests to an HTTPS request on port 443.

To learn more, see [Listeners for your Application Load Balancers](../../../elasticloadbalancing/latest/application/load-balancer-listeners.md "../../../elasticloadbalancing/latest/application/load-balancer-listeners.md") in
_User Guide for Application Load Balancers_.

### Remediation

To redirect HTTP requests to HTTPS, you must add an Application Load Balancer listener rule or edit an
existing rule.

For instructions on adding a new rule, see [Add a rule](../../../elasticloadbalancing/latest/application/listener-update-rules.md#add-rule "../../../elasticloadbalancing/latest/application/listener-update-rules.md#add-rule") in the _User Guide for Application Load Balancers_. For
**Protocol : Port**, choose **HTTP**, and then
enter `80`. For **Add action, Redirect to**,
choose **HTTPS**, and then enter `443`.

For instructions on editing an existing rule, see [Edit a rule](../../../elasticloadbalancing/latest/application/listener-update-rules.md#edit-rule "../../../elasticloadbalancing/latest/application/listener-update-rules.md#edit-rule") in the _User Guide for Application Load Balancers_. For
**Protocol : Port**, choose **HTTP**, and then
enter `80`. For **Add action, Redirect to**,
choose **HTTPS**, and then enter `443`.

## [ELB.2] Classic Load Balancers with SSL/HTTPS listeners should use a certificate

provided by AWS Certificate Manager

**Related requirements:** NIST.800-53.r5 AC-17(2),
NIST.800-53.r5 AC-4, NIST.800-53.r5 IA-5(1), NIST.800-53.r5 SC-12(3), NIST.800-53.r5
SC-13, NIST.800-53.r5 SC-23, NIST.800-53.r5 SC-23(5), NIST.800-53.r5 SC-7(4),
NIST.800-53.r5 SC-8, NIST.800-53.r5 SC-8(1), NIST.800-53.r5 SC-8(2), NIST.800-53.r5
SI-7(6), NIST.800-171.r2 3.13.8

**Category:** Protect > Data Protection > Encryption of data-in-transit

**Severity:** Medium

**Resource type:**
`AWS::ElasticLoadBalancing::LoadBalancer`

**AWS Config rule:**
[elb-acm-certificate-required](../../../config/latest/developerguide/elb-acm-certificate-required.md "../../../config/latest/developerguide/elb-acm-certificate-required.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether the Classic Load Balancer uses HTTPS/SSL certificates provided by
AWS Certificate Manager (ACM). The control fails if the Classic Load Balancer configured with HTTPS/SSL listener
does not use a certificate provided by ACM.

To create a certificate, you can use either ACM or a tool that supports the SSL and
TLS protocols, such as OpenSSL. Security Hub recommends that you use ACM to create or import
certificates for your load balancer.

ACM integrates with Classic Load Balancers so that you can deploy the certificate on your load
balancer. You also should automatically renew these certificates.

### Remediation

For information about how to associate an ACM SSL/TLS certificate with a Classic Load Balancer,
see the AWS Knowledge Center article [How can I associate an ACM SSL/TLS certificate with a
Classic, Application, or Network Load Balancer?](https://aws.amazon.com/premiumsupport/knowledge-center/associate-acm-certificate-alb-nlb/ "https://aws.amazon.com/premiumsupport/knowledge-center/associate-acm-certificate-alb-nlb/")

## [ELB.3] Classic Load Balancer listeners should be configured with HTTPS or TLS

termination

**Related requirements:** NIST.800-53.r5 AC-17(2),
NIST.800-53.r5 AC-4, NIST.800-53.r5 IA-5(1), NIST.800-53.r5 SC-12(3), NIST.800-53.r5
SC-13, NIST.800-53.r5 SC-23, NIST.800-53.r5 SC-23(3), NIST.800-53.r5 SC-7(4),
NIST.800-53.r5 SC-8, NIST.800-53.r5 SC-8(1), NIST.800-53.r5 SC-8(2), NIST.800-53.r5
SI-7(6), NIST.800-171.r2 3.13.8, NIST.800-171.r2 3.13.15, PCI DSS v4.0.1/4.2.1

**Category:** Protect > Data Protection > Encryption of data-in-transit

**Severity:** Medium

**Resource type:**
`AWS::ElasticLoadBalancing::LoadBalancer`

**AWS Config rule:**
[elb-tls-https-listeners-only](../../../config/latest/developerguide/elb-tls-https-listeners-only.md "../../../config/latest/developerguide/elb-tls-https-listeners-only.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether your Classic Load Balancer listeners are configured with HTTPS or TLS
protocol for front-end (client to load balancer) connections. The control is applicable
if a Classic Load Balancer has listeners. If your Classic Load Balancer does not have a listener configured, then the
control does not report any findings.

The control passes if the Classic Load Balancer listeners are configured with TLS or HTTPS for
front-end connections.

The control fails if the listener is not configured with TLS or HTTPS for front-end
connections.

Before you start to use a load balancer, you must add one or more listeners. A
listener is a process that uses the configured protocol and port to check for connection
requests. Listeners can support both HTTP and HTTPS/TLS protocols. You should always use
an HTTPS or TLS listener, so that the load balancer does the work of encryption and
decryption in transit.

### Remediation

To remediate this issue, update your listeners to use the TLS or HTTPS
protocol.

###### To change all noncompliant listeners to TLS/HTTPS listeners

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, under **Load Balancing**, choose
   **Load Balancers**.
3. Select your Classic Load Balancer.
4. On the **Listeners** tab, choose
   **Edit**.
5. For all listeners where **Load Balancer Protocol** is not
   set to HTTPS or SSL, change the setting to HTTPS or SSL.
6. For all modified listeners, on the **Certificates** tab,
   choose **Change default**.
7. For **ACM and IAM certificates**, select a
   certificate.
8. Choose **Save as default**.
9. After you update all of the listeners, choose
   **Save**.

## [ELB.4] Application Load Balancer should be configured to drop invalid http

headers

**Related requirements:** NIST.800-53.r5 SC-7(4),
NIST.800-53.r5 SC-8(2), PCI DSS v4.0.1/6.2.4

**Category:** Protect > Network Security

**Severity:** Medium

**Resource type:**
`AWS::ElasticLoadBalancingV2::LoadBalancer`

**AWS Config rule:**
[alb-http-drop-invalid-header-enabled](../../../config/latest/developerguide/alb-http-drop-invalid-header-enabled.md "../../../config/latest/developerguide/alb-http-drop-invalid-header-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control evaluates whether an Application Load Balancer is configured to drop invalid HTTP headers.
The control fails if the value of
`routing.http.drop_invalid_header_fields.enabled` is set to
`false`.

By default, Application Load Balancers are not configured to drop invalid HTTP header values. Removing
these header values prevents HTTP desync attacks.

###### Note

We recommend disabling this control if ELB.12 is enabled in your account. For more
information, see [[ELB.12] Application Load Balancer should be configured with defensive or strictest
desync mitigation mode](#elb-12 "#elb-12").

### Remediation

To remediate this issue, configure your load balancer to drop invalid header
fields.

###### To configure the load balancer to drop invalid header fields

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Load balancers**.
3. Choose an Application Load Balancer.
4. From **Actions**, choose **Edit
   attributes**.
5. Under **Drop Invalid Header Fields**, choose
   **Enable**.
6. Choose **Save**.

## [ELB.5] Application and Classic Load Balancers logging should be enabled

**Related requirements:** NIST.800-53.r5 AC-4(26),
NIST.800-53.r5 AU-10, NIST.800-53.r5 AU-12, NIST.800-53.r5 AU-2, NIST.800-53.r5 AU-3,
NIST.800-53.r5 AU-6(3), NIST.800-53.r5 AU-6(4), NIST.800-53.r5 CA-7, NIST.800-53.r5
SC-7(9), NIST.800-53.r5 SI-7(8)

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:**
`AWS::ElasticLoadBalancing::LoadBalancer`,
`AWS::ElasticLoadBalancingV2::LoadBalancer`

**AWS Config rule:**
[elb-logging-enabled](../../../config/latest/developerguide/elb-logging-enabled.md "../../../config/latest/developerguide/elb-logging-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether the Application Load Balancer and the Classic Load Balancerhave logging enabled. The control
fails if `access_logs.s3.enabled` is `false`.

ELB provides access logs that capture detailed information about requests sent to
your load balancer. Each log contains information such as the time the request was
received, the client's IP address, latencies, request paths, and server responses. You
can use these access logs to analyze traffic patterns and to troubleshoot issues.

To learn more, see [Access logs for
your Classic Load Balancer](../../../elasticloadbalancing/latest/classic/access-log-collection.md "../../../elasticloadbalancing/latest/classic/access-log-collection.md") in _User Guide for Classic Load Balancers_.

### Remediation

To enable access logs, see [Step 3: Configure access logs](../../../elasticloadbalancing/latest/application/enable-access-logging.md#enable-access-logs "../../../elasticloadbalancing/latest/application/enable-access-logging.md#enable-access-logs") in the
_User Guide for Application Load Balancers_.

## [ELB.6] Application, Gateway, and Network Load Balancers should have deletion

protection enabled

**Related requirements:** NIST.800-53.r5 CA-9(1),
NIST.800-53.r5 CM-2, NIST.800-53.r5 CM-2(2), NIST.800-53.r5 CM-3, NIST.800-53.r5
SC-5(2)

**Category:** Recover > Resilience > High
availability

**Severity:** Medium

**Resource type:**
`AWS::ElasticLoadBalancingV2::LoadBalancer`

**AWS Config rule:**
[elb-deletion-protection-enabled](../../../config/latest/developerguide/elb-deletion-protection-enabled.md "../../../config/latest/developerguide/elb-deletion-protection-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Application, Gateway, or Network Load Balancer has deletion protection
enabled. The control fails if deletion protection is disabled.

Enable deletion protection to protect your Application, Gateway, or Network Load Balancer from
deletion.

### Remediation

To prevent your load balancer from being deleted accidentally, you can enable
deletion protection. By default, deletion protection is disabled for your load
balancer.

If you enable deletion protection for your load balancer, you must disable delete
protection before you can delete the load balancer.

To enable deletion protection for an Application Load Balancer, see [Deletion protection](../../../elasticloadbalancing/latest/application/application-load-balancers.md#deletion-protection "../../../elasticloadbalancing/latest/application/application-load-balancers.md#deletion-protection") in the
_User Guide for Application Load Balancers_. To enable deletion protection for a Gateway Load Balancer,
see [Deletion protection](../../../elasticloadbalancing/latest/gateway/gateway-load-balancers.md#deletion-protection "../../../elasticloadbalancing/latest/gateway/gateway-load-balancers.md#deletion-protection") in the
_User Guide for Gateway Load Balancers_. To enable deletion protection for a Network Load Balancer,
see [Deletion protection](../../../elasticloadbalancing/latest/network/network-load-balancers.md#deletion-protection "../../../elasticloadbalancing/latest/network/network-load-balancers.md#deletion-protection") in the
_User Guide for Network Load Balancers_.

## [ELB.7] Classic Load Balancers should have connection draining enabled

**Related requirements:** NIST.800-53.r5 CA-9(1),
NIST.800-53.r5 CM-2

**Category:** Recover > Resilience

**Severity:** Low

**Resource type:**
`AWS::ElasticLoadBalancing::LoadBalancer`

**AWS Config rule:**
`elb-connection-draining-enabled` (custom Security Hub rule)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether Classic Load Balancers have connection draining enabled.

Enabling connection draining on Classic Load Balancers ensures that the load balancer stops sending
requests to instances that are de-registering or unhealthy. It keeps the existing
connections open. This is particularly useful for instances in Amazon EC2 Auto Scaling groups, to ensure
that connections aren't severed abruptly.

### Remediation

To enable connection draining on Classic Load Balancers, see [Configure
connection draining for your Classic Load Balancer](../../../elasticloadbalancing/latest/classic/config-conn-drain.md "../../../elasticloadbalancing/latest/classic/config-conn-drain.md") in _User Guide for Classic Load Balancers_.

## [ELB.8] Classic Load Balancers with SSL listeners should use a predefined

security policy that has strong AWS Configuration

**Related requirements:** NIST.800-53.r5 AC-17(2),
NIST.800-53.r5 AC-4, NIST.800-53.r5 IA-5(1), NIST.800-53.r5 SC-12(3), NIST.800-53.r5
SC-13, NIST.800-53.r5 SC-23, NIST.800-53.r5 SC-23(3), NIST.800-53.r5 SC-7(4),
NIST.800-53.r5 SC-8, NIST.800-53.r5 SC-8(1), NIST.800-53.r5 SC-8(2), NIST.800-53.r5
SI-7(6), NIST.800-171.r2 3.13.8, NIST.800-171.r2 3.13.15, PCI DSS v4.0.1/4.2.1

**Category:** Protect > Data Protection > Encryption of data-in-transit

**Severity:** Medium

**Resource type:**
`AWS::ElasticLoadBalancing::LoadBalancer`

**AWS Config rule:**
[elb-predefined-security-policy-ssl-check](../../../config/latest/developerguide/elb-predefined-security-policy-ssl-check.md "../../../config/latest/developerguide/elb-predefined-security-policy-ssl-check.md")

**Schedule type:** Change triggered

**Parameters:**

- `predefinedPolicyName`:
  `ELBSecurityPolicy-TLS-1-2-2017-01` (not customizable)

This control checks whether your Classic Load Balancer HTTPS/SSL listeners use the predefined policy
`ELBSecurityPolicy-TLS-1-2-2017-01`. The control fails if the Classic Load Balancer
HTTPS/SSL listeners do not use `ELBSecurityPolicy-TLS-1-2-2017-01`.

A security policy is a combination of SSL protocols, ciphers, and the Server Order
Preference option. Predefined policies control the ciphers, protocols, and preference
orders to support during SSL negotiations between a client and load balancer.

Using `ELBSecurityPolicy-TLS-1-2-2017-01` can help you to meet compliance
and security standards that require you to disable specific versions of SSL and TLS. For
more information, see [Predefined
SSL security policies for Classic Load Balancers](../../../elasticloadbalancing/latest/classic/elb-security-policy-table.md "../../../elasticloadbalancing/latest/classic/elb-security-policy-table.md") in _User Guide for Classic Load Balancers_.

### Remediation

For information on how to use the predefined security policy
`ELBSecurityPolicy-TLS-1-2-2017-01` with a Classic Load Balancer, see [Configure security settings](../../../elasticloadbalancing/latest/classic/elb-create-https-ssl-load-balancer.md#config-backend-auth "../../../elasticloadbalancing/latest/classic/elb-create-https-ssl-load-balancer.md#config-backend-auth") in _User Guide for Classic Load Balancers_.

## [ELB.9] Classic Load Balancers should have cross-zone load balancing

enabled

**Related requirements:** NIST.800-53.r5 CP-10,
NIST.800-53.r5 CP-6(2), NIST.800-53.r5 SC-36, NIST.800-53.r5 SC-5(2), NIST.800-53.r5
SI-13(5)

**Category:** Recover > Resilience > High availability

**Severity:** Medium

**Resource type:**
`AWS::ElasticLoadBalancing::LoadBalancer`

**AWS Config rule:**
[elb-cross-zone-load-balancing-enabled](../../../config/latest/developerguide/elb-cross-zone-load-balancing-enabled.md "../../../config/latest/developerguide/elb-cross-zone-load-balancing-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks if cross-zone load balancing is enabled for the Classic Load Balancers (CLBs). The
control fails if cross-zone load balancing is not enabled for a CLB.

A load balancer node distributes traffic only across the registered targets in its
Availability Zone. When cross-zone load balancing is disabled, each load balancer node
distributes traffic only across the registered targets in its Availability Zone. If the
number of registered targets is not same across the Availability Zones, traffic wont be
distributed evenly and the instances in one zone may end up over utilized compared to
the instances in another zone. With cross-zone load balancing enabled, each load
balancer node for your Classic Load Balancer distributes requests evenly across the registered instances
in all enabled Availability Zones. For details see [Cross-zone load balancing](../../../elasticloadbalancing/latest/userguide/how-elastic-load-balancing-works.md#cross-zone-load-balancing "../../../elasticloadbalancing/latest/userguide/how-elastic-load-balancing-works.md#cross-zone-load-balancing") in the ELB User Guide.

### Remediation

To enable cross-zone load balancing in a Classic Load Balancer, see [Enable cross-zone load balancing](../../../elasticloadbalancing/latest/classic/enable-disable-crosszone-lb.md#enable-cross-zone "../../../elasticloadbalancing/latest/classic/enable-disable-crosszone-lb.md#enable-cross-zone") in the _User Guide for
Classic Load Balancers_.

## [ELB.10] Classic Load Balancer should span multiple Availability Zones

**Related requirements:** NIST.800-53.r5 CP-10,
NIST.800-53.r5 CP-6(2), NIST.800-53.r5 SC-36, NIST.800-53.r5 SC-5(2), NIST.800-53.r5
SI-13(5)

**Category:** Recover > Resilience > High availability

**Severity:** Medium

**Resource type:**
`AWS::ElasticLoadBalancing::LoadBalancer`

**AWS Config rule:**
[clb-multiple-az](../../../config/latest/developerguide/clb-multiple-az.md "../../../config/latest/developerguide/clb-multiple-az.md")

**Schedule type:** Change triggered

**Parameters:**

| Parameter              | Description                          | Type | Allowed custom values | Security Hub default value |
| ---------------------- | ------------------------------------ | ---- | --------------------- | -------------------------- |
| `minAvailabilityZones` | Minimum number of Availability Zones | Enum | `2, 3, 4, 5, 6`       | `2`                        |

This control checks whether a Classic Load Balancer has been configured to span at least the specified
number of Availability Zones (AZs). The control fails if the Classic Load Balancer does not span at
least the specified number of AZs. Unless you provide a custom parameter value for the
minimum number of AZs, Security Hub uses a default value of two AZs.

A Classic Load Balancer can be set up to distribute incoming requests across Amazon EC2 instances in a
single Availability Zone or multiple Availability Zones. A Classic Load Balancer that does not span
multiple Availability Zones is unable to redirect traffic to targets in another
Availability Zone if the sole configured Availability Zone becomes unavailable.

### Remediation

To add Availability Zones to a Classic Load Balancer, see [Add or remove
subnets for your Classic Load Balancer](../../../elasticloadbalancing/latest/classic/elb-manage-subnets.md "../../../elasticloadbalancing/latest/classic/elb-manage-subnets.md") in the _User Guide for Classic Load Balancers_.

## [ELB.12] Application Load Balancer should be configured with defensive or strictest

desync mitigation mode

**Related requirements:** NIST.800-53.r5 AC-4(21),
NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-2, PCI DSS v4.0.1/6.2.4

**Category:** Protect > Data Protection > Data integrity

**Severity:** Medium

**Resource type:**
`AWS::ElasticLoadBalancingV2::LoadBalancer`

**AWS Config rule:**
[alb-desync-mode-check](../../../config/latest/developerguide/alb-desync-mode-check.md "../../../config/latest/developerguide/alb-desync-mode-check.md")

**Schedule type:** Change triggered

**Parameters:**

- `desyncMode`: `defensive, strictest` (not
  customizable)

This control checks whether an Application Load Balancer is configured with defensive or strictest desync
mitigation mode. The control fails if an Application Load Balancer is not configured with defensive or
strictest desync mitigation mode.

HTTP Desync issues can lead to request smuggling and make applications vulnerable to
request queue or cache poisoning. In turn, these vulnerabilities can lead to credential
stuffing or execution of unauthorized commands. Application Load Balancers configured with defensive or
strictest desync mitigation mode protect your application from security issues that may
be caused by HTTP Desync.

### Remediation

To update desync mitigation mode of an Application Load Balancer, see [Desync mitigation mode](../../../elasticloadbalancing/latest/application/application-load-balancers.md#desync-mitigation-mode "../../../elasticloadbalancing/latest/application/application-load-balancers.md#desync-mitigation-mode") in the _User Guide for Application Load Balancers_.

## [ELB.13] Application, Network and Gateway Load Balancers should span multiple

Availability Zones

**Related requirements:** NIST.800-53.r5 CP-10,
NIST.800-53.r5 CP-6(2), NIST.800-53.r5 SC-36, NIST.800-53.r5 SC-5(2), NIST.800-53.r5
SI-13(5)

**Category:** Recover > Resilience > High availability

**Severity:** Medium

**Resource type:**
`AWS::ElasticLoadBalancingV2::LoadBalancer`

**AWS Config rule:**
[elbv2-multiple-az](../../../config/latest/developerguide/elbv2-multiple-az.md "../../../config/latest/developerguide/elbv2-multiple-az.md")

**Schedule type:** Change triggered

**Parameters:**

| Parameter              | Description                          | Type | Allowed custom values | Security Hub default value |
| ---------------------- | ------------------------------------ | ---- | --------------------- | -------------------------- |
| `minAvailabilityZones` | Minimum number of Availability Zones | Enum | `2, 3, 4, 5, 6`       | `2`                        |

This control checks whether an Elastic Load Balancer V2 (Application, Network, or
Gateway Load Balancer) has registered instances from at least the specified number of Availability Zones
(AZs). The control fails if an Elastic Load Balancer V2 doesn't have instances
registered in at least the specified number of AZs. Unless you provide a custom
parameter value for the minimum number of AZs, Security Hub uses a default value of two
AZs.

ELB automatically distributes your incoming traffic across multiple targets, such as
EC2 instances, containers, and IP addresses, in one or more Availability Zones. ELB
scales your load balancer as your incoming traffic changes over time. It is recommended
to configure at least two availability zones to ensure availability of services, as the
Elastic Load Balancer will be able to direct traffic to another availability zone if one
becomes unavailable. Having multiple availability zones configured will help eliminate
having a single point of failure for the application.

### Remediation

To add an Availability Zone to an Application Load Balancer, see [Availability Zones for your Application Load Balancer](../../../elasticloadbalancing/latest/application/load-balancer-subnets.md "../../../elasticloadbalancing/latest/application/load-balancer-subnets.md") in the
_User Guide for Application Load Balancers_. To add an Availability Zone to an Network Load Balancer,
see [Network Load Balancers](../../../elasticloadbalancing/latest/network/network-load-balancers.md#availability-zones "../../../elasticloadbalancing/latest/network/network-load-balancers.md#availability-zones") in the _User Guide for Network Load Balancers_. To add an
Availability Zone to a Gateway Load Balancer, see [Create a
Gateway Load Balancer](../../../elasticloadbalancing/latest/gateway/create-load-balancer.md "../../../elasticloadbalancing/latest/gateway/create-load-balancer.md") in the _User Guide for Gateway Load Balancers_.

## [ELB.14] Classic Load Balancer should be configured with defensive or strictest

desync mitigation mode

**Related requirements:** NIST.800-53.r5 AC-4(21),
NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-2, PCI DSS v4.0.1/6.2.4

**Category:** Protect > Data Protection > Data integrity

**Severity:** Medium

**Resource type:**
`AWS::ElasticLoadBalancing::LoadBalancer`

**AWS Config rule:**
[clb-desync-mode-check](../../../config/latest/developerguide/clb-desync-mode-check.md "../../../config/latest/developerguide/clb-desync-mode-check.md")

**Schedule type:** Change triggered

**Parameters:**

- `desyncMode`: `defensive, strictest` (not
  customizable)

This control checks whether a Classic Load Balancer is configured with defensive or strictest desync
mitigation mode. The control fails if the Classic Load Balancer isn't configured with defensive or
strictest desync mitigation mode.

HTTP Desync issues can lead to request smuggling and make applications vulnerable to
request queue or cache poisoning. In turn, these vulnerabilities can lead to credential
hijacking or execution of unauthorized commands. Classic Load Balancers configured with defensive or
strictest desync mitigation mode protect your application from security issues that may
be caused by HTTP Desync.

### Remediation

To update desync mitigation mode on a Classic Load Balancer, see [Modify desync mitigation mode](../../../elasticloadbalancing/latest/classic/config-desync-mitigation-mode.md#update-desync-mitigation-mode "../../../elasticloadbalancing/latest/classic/config-desync-mitigation-mode.md#update-desync-mitigation-mode") in the
_User Guide for Classic Load Balancers_.

## [ELB.16] Application Load Balancers should be associated with an AWS WAF web

ACL

**Related requirements:** NIST.800-53.r5 AC-4(21)

**Category:** Protect > Protective services

**Severity:** Medium

**Resource type:**
`AWS::ElasticLoadBalancingV2::LoadBalancer`

**AWS Config rule:**
[alb-waf-enabled](../../../config/latest/developerguide/alb-waf-enabled.md "../../../config/latest/developerguide/alb-waf-enabled.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Application Load Balancer is associated with an AWS WAF Classic or AWS WAF web
access control list (web ACL). The control fails if the `Enabled` field for
the AWS WAF configuration is set to `false`.

AWS WAF is a web application firewall that helps protect web applications and APIs from
attacks. With AWS WAF, you can configure a web ACL, which is a set of rules that allow,
block, or count web requests based on customizable web security rules and conditions
that you define. We recommend associating your Application Load Balancer with an AWS WAF web ACL to help
protect it from malicious attacks.

### Remediation

To associate an Application Load Balancer with a web ACL, see [Associating or disassociating a web ACL with an AWS resource](../../../waf/latest/developerguide/web-acl-associating-aws-resource.md "../../../waf/latest/developerguide/web-acl-associating-aws-resource.md") in the
_AWS WAF Developer Guide_.

## [ELB.17] Application and Network Load Balancers with listeners

should use recommended security policies

**Related requirements:** NIST.800-53.r5 AC-17(2),
NIST.800-53.r5 AC-4, NIST.800-53.r5 IA-5(1), NIST.800-53.r5 SC-12(3), NIST.800-53.r5
SC-13, NIST.800-53.r5 SC-23, NIST.800-53.r5 SC-23(3), NIST.800-53.r5 SC-7(4),
NIST.800-53.r5 SC-8, NIST.800-53.r5 SC-8(1), NIST.800-53.r5 SC-8(2), NIST.800-53.r5
SI-7(6)

**Category:** Protect > Data Protection > Encryption of data-in-transit

**Severity:** Medium

**Resource type:**
`AWS::ElasticLoadBalancingV2::Listener`

**AWS Config rule:**
[elbv2-predefined-security-policy-ssl-check](../../../config/latest/developerguide/elbv2-predefined-security-policy-ssl-check.md "../../../config/latest/developerguide/elbv2-predefined-security-policy-ssl-check.md")

**Schedule type:** Change triggered

**Parameters:**
`sslPolicies`: `ELBSecurityPolicy-TLS13-1-2-2021-06,
 ELBSecurityPolicy-TLS13-1-2-FIPS-2023-04, ELBSecurityPolicy-TLS13-1-3-2021-06,
 ELBSecurityPolicy-TLS13-1-3-FIPS-2023-04, ELBSecurityPolicy-TLS13-1-2-Res-2021-06,
 ELBSecurityPolicy-TLS13-1-2-Res-FIPS-2023-04` (not customizable)

This control checks whether the HTTPS listener for an Application Load Balancer or the TLS listener for a
Network Load Balancer is configured to encrypt data in transit by using a recommended security policy.
The control fails if the HTTPS or TLS listener for a load balancer isn't configured to
use a recommended security policy.

Elastic Load Balancing uses an SSL negotiation configuration, known as a _security policy_, to negotiate connections between a client and a load
balancer. The security policy specifies a combination of protocols and ciphers. The
protocol establishes a secure connection between a client and a server. A cipher is an
encryption algorithm that uses encryption keys to create a coded message. During the
connection negotiation process, the client and the load balancer present a list of
ciphers and protocols that they each support, in order of preference. Using a
recommended security policy for a load balancer can help you meet compliance and
security standards.

### Remediation

For information about recommended security policies and how to update listeners,
see the following sections of the _Elastic Load Balancing User
Guides_: [Security policies for Application Load Balancers](../../../elasticloadbalancing/latest/application/describe-ssl-policies.md "../../../elasticloadbalancing/latest/application/describe-ssl-policies.md"), [Security
policies for Network Load Balancers](../../../elasticloadbalancing/latest/network/describe-ssl-policies.md "../../../elasticloadbalancing/latest/network/describe-ssl-policies.md"), [Update an HTTPS listener for your Application Load Balancer](../../../elasticloadbalancing/latest/application/listener-update-certificates.md "../../../elasticloadbalancing/latest/application/listener-update-certificates.md"), and [Update a
listener for your Network Load Balancer](../../../elasticloadbalancing/latest/network/listener-update-rules.md "../../../elasticloadbalancing/latest/network/listener-update-rules.md").

## [ELB.18] Application and Network Load Balancer listeners should

use secure protocols to encrypt data in transit

**Category:** Protect > Data Protection > Encryption of data-in-transit

**Severity:** Medium

**Resource type:**
`AWS::ElasticLoadBalancingV2::Listener`

**AWS Config rule:**
[elbv2-listener-encryption-in-transit](../../../config/latest/developerguide/elbv2-listener-encryption-in-transit.md "../../../config/latest/developerguide/elbv2-listener-encryption-in-transit.md")

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether the listener for an Application Load Balancer or Network Load Balancer is configured to use a
secure protocol for encryption of data in transit. The control fails if an Application Load Balancer
listener isn't configured to use the HTTPS protocol, or a Network Load Balancer listener isn't
configured to use the TLS protocol.

To encrypt data that's transmitted between a client and a load balancer, Elastic Load
Balancer listeners should be configured to use industry-standard security protocols:
HTTPS for Application Load Balancers, or TLS for Network Load Balancers. Otherwise, data that's transmitted between a client
and a load balancer is vulnerable to interception, tampering, and unauthorized access.
Use of HTTPS or TLS by a listener aligns with security best practices and helps ensure
the confidentiality and integrity of data during transmission. This is particularly
important for applications that handle sensitive information, or must comply with
security standards that require encryption of data in transit.

### Remediation

For information about configuring security protocols for listeners, see the
following sections of the _Elastic Load Balancing User Guides_:
[Create
an HTTPS listener for your Application Load Balancer](../../../elasticloadbalancing/latest/application/create-https-listener.md "../../../elasticloadbalancing/latest/application/create-https-listener.md") and [Create a listener
for your Network Load Balancer](../../../elasticloadbalancing/latest/network/create-listener.md "../../../elasticloadbalancing/latest/network/create-listener.md").
