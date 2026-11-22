

# Ingress endpoints

An ingress endpoint is a managed Simple Mail Transfer Protocol (SMTP) endpoint that receives email for Mail Manager. You do not provision, scale, or patch the SMTP server. You configure how senders connect, which traffic the endpoint accepts, and what happens to accepted email.

Every ingress endpoint references one traffic policy and one rule set. You can assign the same traffic policy or rule set to multiple ingress endpoints. You can also create separate ingress endpoints for different sender groups, domains, applications, or security requirements.

The following diagram shows three separate email flows that use open, mutual TLS, and authenticated ingress endpoints.

![Three horizontal email flows use separate ingress points. Internet email uses an open public ingress point, a partner mail server uses a private mutual TLS ingress point, and an application uses a public authenticated ingress point. Each traffic policy accepts or rejects recipients before its rule set processes accepted messages. Application logs and traffic policy debug logs can be delivered to CloudWatch Logs, Amazon S3, or Amazon Data Firehose.](https://docs.aws.amazon.com/ses/latest/dg/images/ingress-point-flows.png)


Each ingress endpoint provides a separate SMTP entry path. Its traffic policy accepts or rejects each recipient before its rule set processes the accepted message. Application and traffic policy logs from every flow can share the same delivery destinations.

## How ingress points process SMTP traffic
<a name="eb-ingress-how-it-works"></a>

An SMTP connection passes through the following stages.

1. The sender connects to the public SMTP endpoint hostname or to a DNS name for the associated Amazon VPC endpoint.

1. The ingress endpoint applies the connection requirements for its type. A public open ingress endpoint is reachable by any internet SMTP sender and does not require a username, password, or client certificate. Its traffic policy controls which recipients and traffic attributes are accepted. For example, an address-list condition can allow only recipients in a maintained list. An authenticated ingress endpoint requires an SMTP username and password. An mTLS ingress endpoint requires a trusted client certificate.

1. The traffic policy evaluates each envelope recipient during the SMTP `RCPT TO` command. A rejected recipient does not enter rule-set processing. For evaluation order and conditions, see [Traffic policies and policy statements](eb-filters.md).

1. The traffic policy checks the received message size against its configured maximum during the SMTP `DATA` command.

1. The assigned rule set processes the accepted email and runs its configured actions. For rule execution behavior, see [Rule sets and rules](eb-rules.md).

**Note**  
Authentication and a traffic policy have different purposes. Authentication controls which clients can establish an authorized SMTP session. A traffic policy evaluates message and connection attributes, such as recipient, sender IP address, and TLS version.

## Choosing an ingress point type
<a name="eb-ingress-types"></a>

The following table compares the available ingress endpoint types.


| Type | Client verification | Common use | Detailed guidance | 
| --- | --- | --- | --- | 
| OPEN | A public endpoint permits connections from any internet SMTP sender without credentials or a client certificate. The traffic policy controls which traffic is accepted. | Receiving internet email through an MX record, or receiving email from systems on a restricted private network. | [Open ingress points](eb-ingress-open.md) | 
| AUTH | SMTP username and password using AUTH LOGIN or AUTH PLAIN. | Applications, mail servers, and partner systems that support SMTP credentials. | [Authenticated ingress points](eb-ingress-auth.md) | 
| MTLS | A client certificate that chains to a certificate authority in the configured trust store. | System-to-system integrations that use certificate-based client identity. | [Mutual TLS ingress points](eb-ingress-mtls.md) | 

## Before you create an ingress point
<a name="eb-ingress-before-you-begin"></a>

1. Create a traffic policy that accepts only the intended traffic. For instructions, see [Creating traffic policies and policy statements in the SES console](eb-filters.md#eb-filters-create-console).

1. Create a rule set that processes accepted email. For instructions, see [Create and manage rule sets](eb-rules-setup.md).

1. Choose an ingress endpoint type and prepare its authentication configuration. An authenticated ingress endpoint requires an SMTP password or AWS Secrets Manager secret. An mTLS ingress endpoint requires a CA certificate bundle.

1. Choose public access or create the required interface Amazon VPC endpoint for private access.

The principal that creates the ingress endpoint needs `ses:CreateIngressPoint` permission for the ingress point resource. You can restrict the selected type, traffic policy, and rule set with the `ses:MailManagerIngressPointType`, `ses:MailManagerTrafficPolicyArn`, and `ses:MailManagerRuleSetArn` condition keys.

In the following IAM policy, replace the AWS Region, account ID, traffic policy ID, and rule set ID with your own values. The policy permits a principal to create only an open ingress endpoint that uses the approved traffic policy and rule set.

```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Sid": "CreateOpenIngressPointWithApprovedResources",
    "Effect": "Allow",
    "Action": "ses:CreateIngressPoint",
    "Resource": "arn:aws:ses:{{us-east-1}}:{{123456789012}}:mailmanager-ingress-point/*",
    "Condition": {
      "StringEquals": {
        "ses:MailManagerIngressPointType": "OPEN",
        "ses:MailManagerTrafficPolicyArn": "arn:aws:ses:{{us-east-1}}:{{123456789012}}:mailmanager-traffic-policy/{{tp-0123456789abcdef01234567}}",
        "ses:MailManagerRuleSetArn": "arn:aws:ses:{{us-east-1}}:{{123456789012}}:mailmanager-rule-set/{{rs-0123456789abcdef01234567}}"
      }
    }
  }]
}
```

To authorize a different type, replace `OPEN` with `AUTH` or `MTLS`. For a policy that also manages traffic policies and updates an existing ingress endpoint, see [Permissions for traffic policies and ingress points](eb-filters.md#eb-filters-permissions).

If the SES service-linked role does not exist, creating the first ingress endpoint also requires `iam:CreateServiceLinkedRole`. Creating a private ingress endpoint requires `ec2:DescribeVpcEndpoints`. A request that adds tags requires `ses:TagResource`.

## Configuring public and private ingress points
<a name="eb-ingress-config-endpoints"></a>

### Receiving email through public endpoints
<a name="eb-ingress-a-record"></a>

After a public ingress endpoint becomes active, its `ARecord` field contains the SMTP endpoint hostname. Use this hostname as the server name in an SMTP client. For an open ingress endpoint that receives internet email for a domain, use the hostname as the target of the domain's MX record.

For example, the following MX record routes email for `marketing.example.com` to a public ingress endpoint.


|  |  | 
| --- |--- |
| Record name | marketing.example.com | 
| Record type | MX | 
| Priority | 10 | 
| Value | 890123abcdef.ghijk.mail-manager-smtp.amazonaws.com | 

Replace the example value with the hostname returned for your ingress endpoint. DNS providers use different interfaces and terminology for MX records.

### Receiving email through Amazon VPC endpoints
<a name="eb-ingress-vpc-endpoint"></a>

A private ingress endpoint uses the DNS names of an associated interface Amazon VPC endpoint. It does not return the public SMTP endpoint hostname described in [Receiving email through public endpoints](#eb-ingress-a-record). Configure SMTP clients to use a DNS name returned by the Amazon VPC endpoint.

The Amazon VPC endpoint must be active, available to the same AWS account, and created for the service name that matches the ingress endpoint type and TLS policy. One Amazon VPC endpoint can be associated with only one ingress endpoint.

The following table lists the production service names.


| Ingress point type | Standard service | FIPS service | 
| --- | --- | --- | 
| OPEN | com.amazonaws.{{region}}.mail-manager-smtp.open | com.amazonaws.{{region}}.mail-manager-smtp.open.fips | 
| AUTH | com.amazonaws.{{region}}.mail-manager-smtp.auth | com.amazonaws.{{region}}.mail-manager-smtp.auth.fips | 
| MTLS | com.amazonaws.{{region}}.mail-manager-smtp.mtls | com.amazonaws.{{region}}.mail-manager-smtp.mtls.fips | 

**Note**  
A `FIPS` ingress endpoint requires the matching FIPS Amazon VPC endpoint service. An ingress endpoint with `REQUIRED` or `OPTIONAL` requires the standard service.

## TLS policies for ingress points
<a name="eb-ingress-tls-policy"></a>

An ingress endpoint uses STARTTLS to upgrade an SMTP connection to Transport Layer Security (TLS). Implicit TLS, in which the connection starts inside TLS, is not supported.

`FIPS`  
Requires TLS with FIPS-validated cryptographic modules. This value is available only in US and Canada Regions and cannot be changed after the ingress endpoint is created.

`REQUIRED`  
Requires the SMTP client to use STARTTLS.

`OPTIONAL`  
Accepts SMTP traffic with or without STARTTLS. Using `OPTIONAL` is not recommended unless the integration must accept clients that cannot use TLS.

The following table shows where each policy is supported.


| Ingress point | Public network | Private network | 
| --- | --- | --- | 
| OPEN | FIPS, REQUIRED, or OPTIONAL | FIPS, REQUIRED, or OPTIONAL | 
| AUTH | FIPS in US and Canada Regions; otherwise REQUIRED | FIPS, REQUIRED, or OPTIONAL | 
| MTLS | FIPS in US and Canada Regions; otherwise REQUIRED | FIPS in US and Canada Regions; otherwise REQUIRED | 

For open ingress endpoints and private authenticated ingress endpoints, you can change between `REQUIRED` and `OPTIONAL`. You cannot change the TLS policy of a public authenticated ingress endpoint or an mTLS ingress endpoint. To change an immutable TLS policy, create a replacement ingress endpoint.

## Creating and managing ingress points
<a name="eb-ingress-create-console"></a>

**To create an ingress point in the SES console**

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/).

1. In the navigation pane, under **Mail Manager**, choose **Ingress endpoints**.

1. Choose **Create ingress endpoint**, and enter a unique name.

1. Choose **Open**, **Authenticated**, or **mTLS**. Complete the authentication settings described on the corresponding type page.

1. Select the rule set and traffic policy that the ingress endpoint will use.

1. Choose a public network with IPv4 or dual-stack addressing, or choose a private network and select the matching Amazon VPC endpoint.

1. Select the TLS policy, and then choose **Create ingress endpoint**.

1. Refresh the details page until **Status** is **Active**. A public ingress endpoint then displays the endpoint hostname in **ARecord**. A private ingress endpoint uses the DNS names of the selected Amazon VPC endpoint.

1. Copy the ingress endpoint ID, such as `inp-0123456789abcdef01234567`. An authenticated ingress endpoint uses this ID as its SMTP username.

1. Configure the SMTP client or MX record as described in [Configuring public and private ingress points](#eb-ingress-config-endpoints).

To change the name, active status, rule set, traffic policy, authentication configuration, or a supported TLS policy, choose the ingress endpoint and then choose **Edit** for the corresponding settings. To delete an ingress endpoint, select it on the **Ingress endpoints** page and choose **Delete**.

### Ingress point provisioning status
<a name="eb-ingress-status"></a>

`CreateIngressPoint` returns an `IngressPointId` before the SMTP endpoint is ready. Run the following command until `Status` is `ACTIVE`. Replace the AWS Region and ingress endpoint ID with your own values.

```bash
PROMPT> aws mailmanager get-ingress-point \
  --region {{us-east-1}} \
  --ingress-point-id {{inp-0123456789abcdef01234567}} \
  --query '{Status:Status,Endpoint:ARecord,Network:NetworkConfiguration}'
```

An ingress endpoint in `PROVISIONING` is not ready to receive messages. An `ACTIVE` ingress endpoint can receive messages subject to its authentication, TLS, and traffic-policy configuration. A `CLOSED` ingress endpoint rejects new messages.

## Monitoring accepted and rejected traffic
<a name="eb-ingress-monitoring"></a>

Configure `APPLICATION_LOGS` to inspect messages accepted by an ingress endpoint. Configure `TRAFFIC_POLICY_DEBUG_LOGS` to inspect per-recipient policy evaluation for accepted and rejected traffic. For setup instructions, schemas, and CloudWatch Logs Insights queries, see [Mail Manager logging](eb-logging.md).

## Choosing an ingress point for your email flow
<a name="eb-ingress-examples"></a>

For complete inbound, outbound, security, archiving, application-processing, and tenant-isolation patterns based on AWS Messaging Blog architectures, see [Ingress point use cases and recommendations](eb-ingress-use-cases.md).

**Topics**
+ [How ingress points process SMTP traffic](#eb-ingress-how-it-works)
+ [Choosing an ingress point type](#eb-ingress-types)
+ [Before you create an ingress point](#eb-ingress-before-you-begin)
+ [Configuring public and private ingress points](#eb-ingress-config-endpoints)
+ [TLS policies for ingress points](#eb-ingress-tls-policy)
+ [Creating and managing ingress points](#eb-ingress-create-console)
+ [Monitoring accepted and rejected traffic](#eb-ingress-monitoring)
+ [Choosing an ingress point for your email flow](#eb-ingress-examples)
+ [Open ingress points](eb-ingress-open.md)
+ [Authenticated ingress points](eb-ingress-auth.md)
+ [Mutual TLS ingress points](eb-ingress-mtls.md)
+ [Ingress point use cases and recommendations](eb-ingress-use-cases.md)