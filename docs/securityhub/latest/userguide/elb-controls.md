

# Security Hub CSPM controls for Elastic Load Balancing
<a name="elb-controls"></a>

These AWS Security Hub CSPM controls evaluate the Elastic Load Balancing service and resources. The controls might not be available in all AWS Regions. For more information, see [Availability of controls by Region](securityhub-regions.md#securityhub-regions-control-support).

## [ELB.1] Application Load Balancer should be configured to redirect all HTTP requests to HTTPS
<a name="elb-1"></a>

**Related requirements:** PCI DSS v3.2.1/2.3,PCI DSS v3.2.1/4.1, NIST.800-53.r5 AC-17(2), NIST.800-53.r5 AC-4, NIST.800-53.r5 IA-5(1), NIST.800-53.r5 SC-12(3), NIST.800-53.r5 SC-13, NIST.800-53.r5 SC-23, NIST.800-53.r5 SC-23(3), NIST.800-53.r5 SC-7(4), NIST.800-53.r5 SC-8, NIST.800-53.r5 SC-8(1), NIST.800-53.r5 SC-8(2), NIST.800-53.r5 SI-7(6)

**Category:** Detect > Detection services

**Severity:** Medium

**Resource type:** `AWS::ElasticLoadBalancingV2::LoadBalancer`

**AWS Config rule:** [alb-http-to-https-redirection-check](https://docs.aws.amazon.com/config/latest/developerguide/alb-http-to-https-redirection-check.html) 

**Schedule type:** Periodic

**Parameters:** None

This control checks whether HTTP to HTTPS redirection is configured on all HTTP listeners of Application Load Balancers. The control fails if any of the HTTP listeners of Application Load Balancers do not have HTTP to HTTPS redirection configured.

Before you start to use your Application Load Balancer, you must add one or more listeners. A listener is a process that uses the configured protocol and port to check for connection requests. Listeners support both the HTTP and HTTPS protocols. You can use an HTTPS listener to offload the work of encryption and decryption to your load balancer. To enforce encryption in transit, you should use redirect actions with Application Load Balancers to redirect client HTTP requests to an HTTPS request on port 443.

To learn more, see [Listeners for your Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html) in *User Guide for Application Load Balancers*.

### Remediation
<a name="elb-1-remediation"></a>

To redirect HTTP requests to HTTPS, you must add an Application Load Balancer listener rule or edit an existing rule.

For instructions on adding a new rule, see [Add a rule](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/listener-update-rules.html#add-rule) in the *User Guide for Application Load Balancers*. For **Protocol : Port**, choose **HTTP**, and then enter **80**. For **Add action, Redirect to**, choose **HTTPS**, and then enter **443**.

For instructions on editing an existing rule, see [Edit a rule](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/listener-update-rules.html#edit-rule) in the *User Guide for Application Load Balancers*. For **Protocol : Port**, choose **HTTP**, and then enter **80**. For **Add action, Redirect to**, choose **HTTPS**, and then enter **443**.

## [ELB.2] Classic Load Balancers with SSL/HTTPS listeners should use a certificate provided by AWS Certificate Manager
<a name="elb-2"></a>

**Related requirements:** NIST.800-53.r5 AC-17(2), NIST.800-53.r5 AC-4, NIST.800-53.r5 IA-5(1), NIST.800-53.r5 SC-12(3), NIST.800-53.r5 SC-13, NIST.800-53.r5 SC-23, NIST.800-53.r5 SC-23(5), NIST.800-53.r5 SC-7(4), NIST.800-53.r5 SC-8, NIST.800-53.r5 SC-8(1), NIST.800-53.r5 SC-8(2), NIST.800-53.r5 SI-7(6), NIST.800-171.r2 3.13.8

**Category:** Protect > Data Protection > Encryption of data-in-transit

**Severity:** Medium

**Resource type:** `AWS::ElasticLoadBalancing::LoadBalancer`

**AWS Config rule:** [elb-acm-certificate-required](https://docs.aws.amazon.com/config/latest/developerguide/elb-acm-certificate-required.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether the Classic Load Balancer uses HTTPS/SSL certificates provided by AWS Certificate Manager (ACM). The control fails if the Classic Load Balancer configured with HTTPS/SSL listener does not use a certificate provided by ACM.

To create a certificate, you can use either ACM or a tool that supports the SSL and TLS protocols, such as OpenSSL. Security Hub CSPM recommends that you use ACM to create or import certificates for your load balancer.

ACM integrates with Classic Load Balancers so that you can deploy the certificate on your load balancer. You also should automatically renew these certificates.

### Remediation
<a name="elb-2-remediation"></a>

For information about how to associate an ACM SSL/TLS certificate with a Classic Load Balancer, see the AWS Knowledge Center article [How can I associate an ACM SSL/TLS certificate with a Classic, Application, or Network Load Balancer?](https://aws.amazon.com/premiumsupport/knowledge-center/associate-acm-certificate-alb-nlb/)

## [ELB.3] Classic Load Balancer listeners should be configured with HTTPS or TLS termination
<a name="elb-3"></a>

**Related requirements:** NIST.800-53.r5 AC-17(2), NIST.800-53.r5 AC-4, NIST.800-53.r5 IA-5(1), NIST.800-53.r5 SC-12(3), NIST.800-53.r5 SC-13, NIST.800-53.r5 SC-23, NIST.800-53.r5 SC-23(3), NIST.800-53.r5 SC-7(4), NIST.800-53.r5 SC-8, NIST.800-53.r5 SC-8(1), NIST.800-53.r5 SC-8(2), NIST.800-53.r5 SI-7(6), NIST.800-171.r2 3.13.8, NIST.800-171.r2 3.13.15, PCI DSS v4.0.1/4.2.1

**Category:** Protect > Data Protection > Encryption of data-in-transit

**Severity:** Medium

**Resource type:** `AWS::ElasticLoadBalancing::LoadBalancer`

**AWS Config rule:** [elb-tls-https-listeners-only](https://docs.aws.amazon.com/config/latest/developerguide/elb-tls-https-listeners-only.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether your Classic Load Balancer listeners are configured with HTTPS or TLS protocol for front-end (client to load balancer) connections. The control is applicable if a Classic Load Balancer has listeners. If your Classic Load Balancer does not have a listener configured, then the control does not report any findings.

The control passes if the Classic Load Balancer listeners are configured with TLS or HTTPS for front-end connections.

The control fails if the listener is not configured with TLS or HTTPS for front-end connections.

Before you start to use a load balancer, you must add one or more listeners. A listener is a process that uses the configured protocol and port to check for connection requests. Listeners can support both HTTP and HTTPS/TLS protocols. You should always use an HTTPS or TLS listener, so that the load balancer does the work of encryption and decryption in transit.

### Remediation
<a name="elb-3-remediation"></a>

To remediate this issue, update your listeners to use the TLS or HTTPS protocol.

**To change all noncompliant listeners to TLS/HTTPS listeners**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, under **Load Balancing**, choose **Load Balancers**.

1. Select your Classic Load Balancer.

1. On the **Listeners** tab, choose **Edit**.

1. For all listeners where **Load Balancer Protocol** is not set to HTTPS or SSL, change the setting to HTTPS or SSL.

1. For all modified listeners, on the **Certificates** tab, choose **Change default**.

1. For **ACM and IAM certificates**, select a certificate.

1. Choose **Save as default**.

1. After you update all of the listeners, choose **Save**.

## [ELB.4] Application Load Balancer should be configured to drop invalid http headers
<a name="elb-4"></a>

**Related requirements:** NIST.800-53.r5 SC-7(4), NIST.800-53.r5 SC-8(2), PCI DSS v4.0.1/6.2.4

**Category:** Protect > Network Security

**Severity:** Medium

**Resource type:** `AWS::ElasticLoadBalancingV2::LoadBalancer`

**AWS Config rule:** [alb-http-drop-invalid-header-enabled](https://docs.aws.amazon.com/config/latest/developerguide/alb-http-drop-invalid-header-enabled.html)

**Schedule type:** Change triggered

**Parameters:** None

This control evaluates whether an Application Load Balancer is configured to drop invalid HTTP headers. The control fails if the value of `routing.http.drop_invalid_header_fields.enabled` is set to `false`.

By default, Application Load Balancers are not configured to drop invalid HTTP header values. Removing these header values prevents HTTP desync attacks.

**Note**  
We recommend disabling this control if ELB.12 is enabled in your account. For more information, see [[ELB.12] Application Load Balancer should be configured with defensive or strictest desync mitigation mode](#elb-12).

### Remediation
<a name="elb-4-remediation"></a>

To remediate this issue, configure your load balancer to drop invalid header fields.

**To configure the load balancer to drop invalid header fields**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Load balancers**.

1. Choose an Application Load Balancer.

1. From **Actions**, choose **Edit attributes**.

1. Under **Drop Invalid Header Fields**, choose **Enable**.

1. Choose **Save**.

## [ELB.5] Application and Classic Load Balancers logging should be enabled
<a name="elb-5"></a>

**Related requirements:** NIST.800-53.r5 AC-4(26), NIST.800-53.r5 AU-10, NIST.800-53.r5 AU-12, NIST.800-53.r5 AU-2, NIST.800-53.r5 AU-3, NIST.800-53.r5 AU-6(3), NIST.800-53.r5 AU-6(4), NIST.800-53.r5 CA-7, NIST.800-53.r5 SC-7(9), NIST.800-53.r5 SI-7(8)

**Category:** Identify > Logging

**Severity:** Medium

**Resource type:** `AWS::ElasticLoadBalancing::LoadBalancer`, `AWS::ElasticLoadBalancingV2::LoadBalancer`

**AWS Config rule:** [elb-logging-enabled](https://docs.aws.amazon.com/config/latest/developerguide/elb-logging-enabled.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether the Application Load Balancer and the Classic Load Balancerhave logging enabled. The control fails if `access_logs.s3.enabled` is `false`.

Elastic Load Balancing provides access logs that capture detailed information about requests sent to your load balancer. Each log contains information such as the time the request was received, the client's IP address, latencies, request paths, and server responses. You can use these access logs to analyze traffic patterns and to troubleshoot issues. 

To learn more, see [Access logs for your Classic Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/access-log-collection.html) in *User Guide for Classic Load Balancers*.

### Remediation
<a name="elb-5-remediation"></a>

To enable access logs, see [Step 3: Configure access logs](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/enable-access-logging.html#enable-access-logs) in the *User Guide for Application Load Balancers*.

## [ELB.6] Application, Gateway, and Network Load Balancers should have deletion protection enabled
<a name="elb-6"></a>

**Related requirements:** NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-2, NIST.800-53.r5 CM-2(2), NIST.800-53.r5 CM-3, NIST.800-53.r5 SC-5(2)

**Category:** Recover > Resilience > High availability

**Severity:** Medium

**Resource type:** `AWS::ElasticLoadBalancingV2::LoadBalancer`

**AWS Config rule:** [elb-deletion-protection-enabled](https://docs.aws.amazon.com/config/latest/developerguide/elb-deletion-protection-enabled.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Application, Gateway, or Network Load Balancer has deletion protection enabled. The control fails if deletion protection is disabled.

Enable deletion protection to protect your Application, Gateway, or Network Load Balancer from deletion.

### Remediation
<a name="elb-6-remediation"></a>

To prevent your load balancer from being deleted accidentally, you can enable deletion protection. By default, deletion protection is disabled for your load balancer.

If you enable deletion protection for your load balancer, you must disable delete protection before you can delete the load balancer.

To enable deletion protection for an Application Load Balancer, see [Deletion protection](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancers.html#deletion-protection) in the *User Guide for Application Load Balancers*. To enable deletion protection for a Gateway Load Balancer, see [Deletion protection](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/gateway-load-balancers.html#deletion-protection) in the *User Guide for Gateway Load Balancers*. To enable deletion protection for a Network Load Balancer, see [Deletion protection](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-load-balancers.html#deletion-protection) in the *User Guide for Network Load Balancers*.

## [ELB.7] Classic Load Balancers should have connection draining enabled
<a name="elb-7"></a>

**Related requirements:** NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-2

**Category:** Recover > Resilience

**Severity:** Low

**Resource type:** `AWS::ElasticLoadBalancing::LoadBalancer`

**AWS Config rule:** `elb-connection-draining-enabled` (custom Security Hub CSPM rule)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether Classic Load Balancers have connection draining enabled.

Enabling connection draining on Classic Load Balancers ensures that the load balancer stops sending requests to instances that are de-registering or unhealthy. It keeps the existing connections open. This is particularly useful for instances in Auto Scaling groups, to ensure that connections aren't severed abruptly.

### Remediation
<a name="elb-7-remediation"></a>

To enable connection draining on Classic Load Balancers, see [Configure connection draining for your Classic Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-conn-drain.html) in *User Guide for Classic Load Balancers*.

## [ELB.8] Classic Load Balancers with SSL listeners should use a predefined security policy that has strong AWS Configuration
<a name="elb-8"></a>

**Related requirements:** NIST.800-53.r5 AC-17(2), NIST.800-53.r5 AC-4, NIST.800-53.r5 IA-5(1), NIST.800-53.r5 SC-12(3), NIST.800-53.r5 SC-13, NIST.800-53.r5 SC-23, NIST.800-53.r5 SC-23(3), NIST.800-53.r5 SC-7(4), NIST.800-53.r5 SC-8, NIST.800-53.r5 SC-8(1), NIST.800-53.r5 SC-8(2), NIST.800-53.r5 SI-7(6), NIST.800-171.r2 3.13.8, NIST.800-171.r2 3.13.15, PCI DSS v4.0.1/4.2.1

**Category:** Protect > Data Protection > Encryption of data-in-transit

**Severity:** Medium

**Resource type:** `AWS::ElasticLoadBalancing::LoadBalancer`

**AWS Config rule:** [elb-predefined-security-policy-ssl-check](https://docs.aws.amazon.com/config/latest/developerguide/elb-predefined-security-policy-ssl-check.html)

**Schedule type:** Change triggered

**Parameters:**
+ `predefinedPolicyName`: `ELBSecurityPolicy-TLS-1-2-2017-01` (not customizable)

This control checks whether your Classic Load Balancer HTTPS/SSL listeners use the predefined policy `ELBSecurityPolicy-TLS-1-2-2017-01`. The control fails if the Classic Load Balancer HTTPS/SSL listeners do not use `ELBSecurityPolicy-TLS-1-2-2017-01`.

A security policy is a combination of SSL protocols, ciphers, and the Server Order Preference option. Predefined policies control the ciphers, protocols, and preference orders to support during SSL negotiations between a client and load balancer.

Using `ELBSecurityPolicy-TLS-1-2-2017-01` can help you to meet compliance and security standards that require you to disable specific versions of SSL and TLS. For more information, see [Predefined SSL security policies for Classic Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-security-policy-table.html) in *User Guide for Classic Load Balancers*.

### Remediation
<a name="elb-8-remediation"></a>

For information on how to use the predefined security policy `ELBSecurityPolicy-TLS-1-2-2017-01` with a Classic Load Balancer, see [Configure security settings](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-create-https-ssl-load-balancer.html#config-backend-auth) in *User Guide for Classic Load Balancers*.

## [ELB.9] Classic Load Balancers should have cross-zone load balancing enabled
<a name="elb-9"></a>

**Related requirements:** NIST.800-53.r5 CP-10, NIST.800-53.r5 CP-6(2), NIST.800-53.r5 SC-36, NIST.800-53.r5 SC-5(2), NIST.800-53.r5 SI-13(5)

**Category:** Recover > Resilience > High availability

**Severity:** Medium

**Resource type:** `AWS::ElasticLoadBalancing::LoadBalancer`

**AWS Config rule:** [elb-cross-zone-load-balancing-enabled](https://docs.aws.amazon.com/config/latest/developerguide/elb-cross-zone-load-balancing-enabled.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks if cross-zone load balancing is enabled for the Classic Load Balancers (CLBs). The control fails if cross-zone load balancing is not enabled for a CLB.

A load balancer node distributes traffic only across the registered targets in its Availability Zone. When cross-zone load balancing is disabled, each load balancer node distributes traffic only across the registered targets in its Availability Zone. If the number of registered targets is not same across the Availability Zones, traffic wont be distributed evenly and the instances in one zone may end up over utilized compared to the instances in another zone. With cross-zone load balancing enabled, each load balancer node for your Classic Load Balancer distributes requests evenly across the registered instances in all enabled Availability Zones. For details see [Cross-zone load balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/how-elastic-load-balancing-works.html#cross-zone-load-balancing) in the Elastic Load Balancing User Guide.

### Remediation
<a name="elb-9-remediation"></a>

To enable cross-zone load balancing in a Classic Load Balancer, see [Enable cross-zone load balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/enable-disable-crosszone-lb.html#enable-cross-zone) in the *User Guide for Classic Load Balancers*.

## [ELB.10] Classic Load Balancer should span multiple Availability Zones
<a name="elb-10"></a>

**Related requirements:** NIST.800-53.r5 CP-10, NIST.800-53.r5 CP-6(2), NIST.800-53.r5 SC-36, NIST.800-53.r5 SC-5(2), NIST.800-53.r5 SI-13(5)

**Category:** Recover > Resilience > High availability

**Severity:** Medium

**Resource type:** `AWS::ElasticLoadBalancing::LoadBalancer`

**AWS Config rule:** [clb-multiple-az](https://docs.aws.amazon.com/config/latest/developerguide/clb-multiple-az.html)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
| `minAvailabilityZones` | Minimum number of Availability Zones | Enum | `2, 3, 4, 5, 6` | `2` | 

This control checks whether a Classic Load Balancer has been configured to span at least the specified number of Availability Zones (AZs). The control fails if the Classic Load Balancer does not span at least the specified number of AZs. Unless you provide a custom parameter value for the minimum number of AZs, Security Hub CSPM uses a default value of two AZs.

 A Classic Load Balancer can be set up to distribute incoming requests across Amazon EC2 instances in a single Availability Zone or multiple Availability Zones. A Classic Load Balancer that does not span multiple Availability Zones is unable to redirect traffic to targets in another Availability Zone if the sole configured Availability Zone becomes unavailable. 

### Remediation
<a name="elb-10-remediation"></a>

 To add Availability Zones to a Classic Load Balancer, see [Add or remove subnets for your Classic Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/elb-manage-subnets.html) in the *User Guide for Classic Load Balancers*. 

## [ELB.12] Application Load Balancer should be configured with defensive or strictest desync mitigation mode
<a name="elb-12"></a>

**Related requirements:** NIST.800-53.r5 AC-4(21), NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-2, PCI DSS v4.0.1/6.2.4

**Category:** Protect > Data Protection > Data integrity

**Severity:** Medium

**Resource type:** `AWS::ElasticLoadBalancingV2::LoadBalancer`

**AWS Config rule:** [alb-desync-mode-check](https://docs.aws.amazon.com/config/latest/developerguide/alb-desync-mode-check.html)

**Schedule type:** Change triggered

**Parameters:**
+ `desyncMode`: `defensive, strictest` (not customizable)

This control checks whether an Application Load Balancer is configured with defensive or strictest desync mitigation mode. The control fails if an Application Load Balancer is not configured with defensive or strictest desync mitigation mode.

HTTP Desync issues can lead to request smuggling and make applications vulnerable to request queue or cache poisoning. In turn, these vulnerabilities can lead to credential stuffing or execution of unauthorized commands. Application Load Balancers configured with defensive or strictest desync mitigation mode protect your application from security issues that may be caused by HTTP Desync. 

### Remediation
<a name="elb-12-remediation"></a>

To update desync mitigation mode of an Application Load Balancer, see [Desync mitigation mode](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/application-load-balancers.html#desync-mitigation-mode) in the *User Guide for Application Load Balancers*. 

## [ELB.13] Application, Network and Gateway Load Balancers should span multiple Availability Zones
<a name="elb-13"></a>

**Related requirements:** NIST.800-53.r5 CP-10, NIST.800-53.r5 CP-6(2), NIST.800-53.r5 SC-36, NIST.800-53.r5 SC-5(2), NIST.800-53.r5 SI-13(5)

**Category:** Recover > Resilience > High availability 

**Severity:** Medium

**Resource type:** `AWS::ElasticLoadBalancingV2::LoadBalancer`

**AWS Config rule:** [elbv2-multiple-az](https://docs.aws.amazon.com/config/latest/developerguide/elbv2-multiple-az.html)

**Schedule type:** Change triggered

**Parameters:**


| Parameter | Description | Type | Allowed custom values | Security Hub CSPM default value | 
| --- | --- | --- | --- | --- | 
| `minAvailabilityZones` | Minimum number of Availability Zones | Enum | `2, 3, 4, 5, 6` | `2` | 

This control checks whether an Elastic Load Balancer V2 (Application, Network, or Gateway Load Balancer) has registered instances from at least the specified number of Availability Zones (AZs). The control fails if an Elastic Load Balancer V2 doesn't have instances registered in at least the specified number of AZs. Unless you provide a custom parameter value for the minimum number of AZs, Security Hub CSPM uses a default value of two AZs.

Elastic Load Balancing automatically distributes your incoming traffic across multiple targets, such as EC2 instances, containers, and IP addresses, in one or more Availability Zones. Elastic Load Balancing scales your load balancer as your incoming traffic changes over time. It is recommended to configure at least two availability zones to ensure availability of services, as the Elastic Load Balancer will be able to direct traffic to another availability zone if one becomes unavailable. Having multiple availability zones configured will help eliminate having a single point of failure for the application. 

### Remediation
<a name="elb-13-remediation"></a>

To add an Availability Zone to an Application Load Balancer, see [Availability Zones for your Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-subnets.html) in the *User Guide for Application Load Balancers*. To add an Availability Zone to an Network Load Balancer, see [Network Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-load-balancers.html#availability-zones) in the *User Guide for Network Load Balancers*. To add an Availability Zone to a Gateway Load Balancer, see [Create a Gateway Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/create-load-balancer.html) in the *User Guide for Gateway Load Balancers*. 

## [ELB.14] Classic Load Balancer should be configured with defensive or strictest desync mitigation mode
<a name="elb-14"></a>

**Related requirements:** NIST.800-53.r5 AC-4(21), NIST.800-53.r5 CA-9(1), NIST.800-53.r5 CM-2, PCI DSS v4.0.1/6.2.4

**Category:** Protect > Data Protection > Data integrity

**Severity:** Medium

**Resource type:** `AWS::ElasticLoadBalancing::LoadBalancer`

**AWS Config rule:** [clb-desync-mode-check](https://docs.aws.amazon.com/config/latest/developerguide/clb-desync-mode-check.html)

**Schedule type:** Change triggered

**Parameters:**
+ `desyncMode`: `defensive, strictest` (not customizable)

This control checks whether a Classic Load Balancer is configured with defensive or strictest desync mitigation mode. The control fails if the Classic Load Balancer isn't configured with defensive or strictest desync mitigation mode.

HTTP Desync issues can lead to request smuggling and make applications vulnerable to request queue or cache poisoning. In turn, these vulnerabilities can lead to credential hijacking or execution of unauthorized commands. Classic Load Balancers configured with defensive or strictest desync mitigation mode protect your application from security issues that may be caused by HTTP Desync. 

### Remediation
<a name="elb-14-remediation"></a>

To update desync mitigation mode on a Classic Load Balancer, see [Modify desync mitigation mode](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/config-desync-mitigation-mode.html#update-desync-mitigation-mode) in the *User Guide for Classic Load Balancers*. 

## [ELB.16] Application Load Balancers should be associated with an AWS WAF web ACL
<a name="elb-16"></a>

**Related requirements:** NIST.800-53.r5 AC-4(21)

**Category:** Protect > Protective services

**Severity:** Medium

**Resource type:** `AWS::ElasticLoadBalancingV2::LoadBalancer`

**AWS Config rule:** [alb-waf-enabled](https://docs.aws.amazon.com/config/latest/developerguide/alb-waf-enabled.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Application Load Balancer is associated with an AWS WAF Classic or AWS WAF web access control list (web ACL). The control fails if the `Enabled` field for the AWS WAF configuration is set to `false`.

AWS WAF is a web application firewall that helps protect web applications and APIs from attacks. With AWS WAF, you can configure a web ACL, which is a set of rules that allow, block, or count web requests based on customizable web security rules and conditions that you define. We recommend associating your Application Load Balancer with an AWS WAF web ACL to help protect it from malicious attacks.

### Remediation
<a name="elb-16-remediation"></a>

To associate an Application Load Balancer with a web ACL, see [Associating or disassociating a web ACL with an AWS resource](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-associating-aws-resource.html) in the *AWS WAF Developer Guide*. 

## [ELB.17] Application and Network Load Balancers with listeners should use recommended security policies
<a name="elb-17"></a>

**Related requirements:** NIST.800-53.r5 AC-17(2), NIST.800-53.r5 AC-4, NIST.800-53.r5 IA-5(1), NIST.800-53.r5 SC-12(3), NIST.800-53.r5 SC-13, NIST.800-53.r5 SC-23, NIST.800-53.r5 SC-23(3), NIST.800-53.r5 SC-7(4), NIST.800-53.r5 SC-8, NIST.800-53.r5 SC-8(1), NIST.800-53.r5 SC-8(2), NIST.800-53.r5 SI-7(6)

**Category:** Protect > Data Protection > Encryption of data-in-transit

**Severity:** Medium

**Resource type:** `AWS::ElasticLoadBalancingV2::Listener`

**AWS Config rule:** [elbv2-predefined-security-policy-ssl-check](https://docs.aws.amazon.com/config/latest/developerguide/elbv2-predefined-security-policy-ssl-check.html)

**Schedule type:** Change triggered

**Parameters:** `sslPolicies`: `ELBSecurityPolicy-TLS13-1-3-2021-06, ELBSecurityPolicy-TLS13-1-3-FIPS-2023-04, ELBSecurityPolicy-TLS13-1-2-Res-2021-06, ELBSecurityPolicy-TLS13-1-2-Res-FIPS-2023-04, ELBSecurityPolicy-TLS13-1-2-Res-PQ-2025-09, ELBSecurityPolicy-TLS13-1-3-PQ-2025-09, ELBSecurityPolicy-TLS13-1-2-Res-FIPS-PQ-2025-09, ELBSecurityPolicy-TLS13-1-3-FIPS-PQ-2025-09` (not customizable)

This control checks whether the HTTPS listener for an Application Load Balancer or the TLS listener for a Network Load Balancer is configured to encrypt data in transit by using a recommended security policy. The control fails if the HTTPS or TLS listener for a load balancer isn't configured to use a recommended security policy.

Elastic Load Balancing uses an SSL negotiation configuration, known as a *security policy*, to negotiate connections between a client and a load balancer. The security policy specifies a combination of protocols and ciphers. The protocol establishes a secure connection between a client and a server. A cipher is an encryption algorithm that uses encryption keys to create a coded message. During the connection negotiation process, the client and the load balancer present a list of ciphers and protocols that they each support, in order of preference. Using a recommended security policy for a load balancer can help you meet compliance and security standards.

### Remediation
<a name="elb-17-remediation"></a>

For information about recommended security policies and how to update listeners, see the following sections of the *Elastic Load Balancing User Guides*: [Security policies for Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/describe-ssl-policies.html), [Security policies for Network Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/describe-ssl-policies.html), [Update an HTTPS listener for your Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/listener-update-certificates.html), and [Update a listener for your Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/listener-update-rules.html).

## [ELB.18] Application and Network Load Balancer listeners should use secure protocols to encrypt data in transit
<a name="elb-18"></a>

**Category:** Protect > Data Protection > Encryption of data-in-transit

**Severity:** Medium

**Resource type:** `AWS::ElasticLoadBalancingV2::Listener`

**AWS Config rule:** [elbv2-listener-encryption-in-transit](https://docs.aws.amazon.com/config/latest/developerguide/elbv2-listener-encryption-in-transit.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether the listener for an Application Load Balancer or Network Load Balancer is configured to use a secure protocol for encryption of data in transit. The control fails if an Application Load Balancer listener isn't configured to use the HTTPS protocol, or a Network Load Balancer listener isn't configured to use the TLS protocol.

To encrypt data that's transmitted between a client and a load balancer, Elastic Load Balancer listeners should be configured to use industry-standard security protocols: HTTPS for Application Load Balancers, or TLS for Network Load Balancers. Otherwise, data that's transmitted between a client and a load balancer is vulnerable to interception, tampering, and unauthorized access. Use of HTTPS or TLS by a listener aligns with security best practices and helps ensure the confidentiality and integrity of data during transmission. This is particularly important for applications that handle sensitive information, or must comply with security standards that require encryption of data in transit.

### Remediation
<a name="elb-18-remediation"></a>

For information about configuring security protocols for listeners, see the following sections of the *Elastic Load Balancing User Guides*: [Create an HTTPS listener for your Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html) and [Create a listener for your Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-listener.html).

## [ELB.21] Application and Network Load Balancer target groups should use encrypted health check protocols
<a name="elb-21"></a>

**Category:** Protect > Data Protection > Encryption of data-in-transit

**Severity:** Medium

**Resource type:** `AWS::ElasticLoadBalancingV2::TargetGroup`

**AWS Config rule:** [elbv2-targetgroup-healthcheck-protocol-encrypted](https://docs.aws.amazon.com/config/latest/developerguide/elbv2-targetgroup-healthcheck-protocol-encrypted.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether the target group for application and network load balancer health checks use an encrypted transport protocol. The control fails if the health check protocol does not use HTTPS. This control is not applicable to Lambda target types.

 Load Balancers send health check requests to registered targets to determine their status and route traffic accordingly. The health check protocol specified in the target group configuration determines how these checks are performed. When health check protocols use unencrypted communication such as HTTP, the requests and responses can be intercepted or manipulated during transmission. This allows attackers to gain insights into infrastructure configuration, tamper with health check results, or conduct man-in-the-middle attacks that affect routing decisions. Using HTTPS for health checks provides encrypted communication between the load balancer and its targets, protecting the integrity and confidentiality of health status information.

### Remediation
<a name="elb-21-remediation"></a>

To configure encrypted health checks for your Application Load Balancer target group, see [Update the health check settings of an Application Load Balancer target group](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/modify-health-check-settings.html) in the *Elastic Load Balancing User Guide*. To configure encrypted health checks for your Network Load Balancer target group, see [Update the health check settings of an Network Load Balancer target group](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/modify-health-check-settings.html) in the *Elastic Load Balancing User Guide*.

## [ELB.22] ELB target groups should use encrypted transport protocols
<a name="elb-22"></a>

**Category:** Protect > Data Protection > Encryption of data-in-transit

**Severity:** Medium

**Resource type:** `AWS::ElasticLoadBalancingV2::TargetGroup`

**AWS Config rule:** [elbv2-targetgroup-protocol-encrypted](https://docs.aws.amazon.com/config/latest/developerguide/elbv2-targetgroup-protocol-encrypted.html)

**Schedule type:** Change triggered

**Parameters:** None

This control checks whether an Elastic Load Balancing target group uses an encrypted transport protocol. This control does not apply to target groups with a target type of Lambda or ALB, or target groups using the GENEVE protocol. The control fails if the target group does not use HTTPS, TLS, or QUIC protocol.

 Encrypting data in transit protects it from interception by unauthorized users. Target groups that use unencrypted protocols (HTTP, TCP, UDP) transmit data without encryption, making it vulnerable to eavesdropping. Using encrypted protocols (HTTPS, TLS, QUIC) ensures that data transmitted between load balancers and targets is protected.

### Remediation
<a name="elb-22-remediation"></a>

To use an encrypted protocol, you must create a new target group with HTTPS, TLS, or QUIC protocol. Target group protocol cannot be modified after creation. To create Application Load Balancer target group, see [Create a target group for your Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-target-group.html) in the *Elastic Load Balancing User Guide*. To create Network Load Balancer target group, see [Create a target group for your Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-target-group.html) in the *Elastic Load Balancing User Guide*. 