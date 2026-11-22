

# Open ingress points

A public open ingress endpoint is reachable from the internet and accepts SMTP connections from any sender without a username, password, or client certificate. Its traffic policy controls which recipients and traffic attributes are accepted. For example, an address-list condition can allow only recipients in a maintained list. Use this configuration to receive internet email through an MX record.

Use a private open ingress endpoint when the network path already restricts which systems can connect and those systems do not support SMTP authentication.

**Warning**  
A public open ingress endpoint can receive connections from any internet sender. Its traffic policy is the primary control that limits accepted recipients and traffic. Use `DENY` as the default action and create explicit `ALLOW` statements for the traffic that the endpoint must accept. Using `ALLOW` as the default action is not recommended because it accepts every recipient that does not match a `DENY` statement.

## Connecting to an open ingress point
<a name="eb-ingress-open-connection"></a>

The following table lists the supported connection settings.


| Network | Ports | STARTTLS | Server name | 
| --- | --- | --- | --- | 
| Public | 25 | Supported | The hostname returned in ARecord. | 
| Private | 25, 587 | Supported | A DNS name returned by the associated Amazon VPC endpoint. | 

To receive internet email, publish an MX record whose value is the public endpoint hostname. For a complete record example, see [Receiving email through public endpoints](eb-ingress.md#eb-ingress-a-record). For private connectivity, see [Receiving email through Amazon VPC endpoints](eb-ingress.md#eb-ingress-vpc-endpoint).

## Restricting traffic to an open ingress point
<a name="eb-ingress-open-policy"></a>

An open ingress endpoint does not establish the sender's identity. A traffic policy can evaluate the envelope recipient, connecting IPv4 or IPv6 address, negotiated TLS version, address-list membership, and supported Email Add On results. Combine the properties needed for the integration instead of relying on one broad condition.

For example, a partner-facing policy can use `DENY` as the default action and allow a recipient only when all of the following conditions match.
+ The connecting sender address is in `192.0.2.0/24` or `2001:db8:1234::/48`.
+ The recipient address ends with `@example.com`.
+ The negotiated TLS version is TLS 1.2 or later.

For complete IPv4, IPv6, recipient, and TLS examples, see [Traffic policy examples](eb-filters.md#eb-filters-examples). For evaluation order and limitations, see [How traffic policy evaluation works](eb-filters.md#eb-filters-how-it-works).

## Creating open ingress points with the AWS CLI
<a name="eb-ingress-open-cli"></a>

The following commands use rule set ID `rs-0123456789abcdef01234567` and traffic policy ID `tp-0123456789abcdef01234567`. Replace the AWS Region, names, and IDs with your own values.

### Create a public dual-stack open ingress point
<a name="eb-ingress-open-cli-public"></a>

```bash
PROMPT> aws mailmanager create-ingress-point \
  --region {{us-east-1}} \
  --ingress-point-name {{internet-inbound}} \
  --type OPEN \
  --rule-set-id {{rs-0123456789abcdef01234567}} \
  --traffic-policy-id {{tp-0123456789abcdef01234567}} \
  --network-configuration 'PublicNetworkConfiguration={IpType=DUAL_STACK}' \
  --tls-policy REQUIRED
```

The response contains the `IngressPointId`. Wait for the endpoint to become active as described in [Ingress point provisioning status](eb-ingress.md#eb-ingress-status). Then publish an MX record that uses the returned `ARecord` hostname.

### Create a private open ingress point
<a name="eb-ingress-open-cli-private"></a>

Create the interface Amazon VPC endpoint before running this command. The service name must match the open ingress endpoint type and selected TLS policy.

```bash
PROMPT> aws mailmanager create-ingress-point \
  --region {{us-east-1}} \
  --ingress-point-name {{private-application-ingress}} \
  --type OPEN \
  --rule-set-id {{rs-0123456789abcdef01234567}} \
  --traffic-policy-id {{tp-0123456789abcdef01234567}} \
  --network-configuration 'PrivateNetworkConfiguration={VpcEndpointId={{vpce-0123456789abcdef0}}}' \
  --tls-policy REQUIRED
```

After the ingress endpoint becomes active, configure the SMTP client to use a DNS name returned by the Amazon VPC endpoint.

## Monitoring accepted and rejected traffic
<a name="eb-ingress-open-monitoring"></a>

Enable `TRAFFIC_POLICY_DEBUG_LOGS` before publishing an MX record or changing an allow condition. The following CloudWatch Logs Logs Insights query shows the newest rejected recipients.

```
fields @timestamp, ingress_point_session_id, sender_ip_address, recipient, traffic_policy_verdict
| filter traffic_policy_verdict = "REJECT"
| sort @timestamp desc
| limit 100
```

Use `APPLICATION_LOGS` for accepted messages. Application logs are not created for a message that the traffic policy rejects before acceptance. For log delivery setup and complete schemas, see [Mail Manager logging](eb-logging.md).

## Recommendations for open ingress points
<a name="eb-ingress-open-recommendations"></a>
+ Use `DENY` as the traffic policy default action.
+ Restrict accepted recipients. Do not publish an MX record for an endpoint that accepts every recipient.
+ Restrict partner integrations by sender IPv4 and IPv6 ranges when the partner publishes stable ranges.
+ Use `REQUIRED` or `FIPS` unless a known sender cannot use STARTTLS.
+ Enable traffic-policy debug logs and test known accepted and rejected recipients before directing production traffic to the endpoint.

**Open ingress point example**  
For a security gateway walkthrough that uses ingress points, traffic policies, security add-ons, and rule sets, see [AWS Messaging Blog: How Amazon SES Mail Manager Elevates Email Security and Efficiency](https://aws.amazon.com/blogs/messaging-and-targeting/how-amazon-ses-mail-manager-elevates-email-security-and-efficiency/).