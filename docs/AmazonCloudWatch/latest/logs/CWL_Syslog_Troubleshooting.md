

# Troubleshooting syslog ingestion
<a name="CWL_Syslog_Troubleshooting"></a>

This section describes common issues with syslog ingestion and how to resolve them.

## Messages not appearing in the log group
<a name="CWL_Syslog_Troubleshooting_NoMessages"></a>

If you have sent syslog messages but they are not appearing in your log group, check the following in order:

1. **Verify the syslog configuration exists.**

   Run `list-syslog-configurations` to confirm that your VPC endpoint is registered with the log group:

   ```
   aws logs list-syslog-configurations \
     --log-group-identifier /syslog/my-devices \
     --region $REGION
   ```

   If no configuration is returned, create one with `put-syslog-configuration`.

1. **Verify the resource policy.**

   Ensure the resource policy on the log group grants `logs:PutLogEvents` and `logs:CreateLogStream` to `syslog.logs.amazonaws.com`, and that the `aws:SourceArn` condition matches your VPC endpoint ARN exactly:

   ```
   aws logs describe-resource-policies --region $REGION
   ```

   Check the `SyslogMessagesDropped` metric with `Reason=AccessDenied` to confirm if authorization is the issue.

1. **Verify the security group.**

   Ensure the security group attached to the VPC endpoint allows inbound traffic on the port you are using (6514, 1514, or 514) from the source CIDR:

   ```
   aws ec2 describe-security-groups \
     --group-ids $VPCE_SG_ID \
     --region $REGION \
     --query 'SecurityGroups[0].IpPermissions'
   ```

1. **Verify network connectivity.**

   From the device or a host on the same network, test TCP connectivity to the endpoint:

   ```
   # TCP connectivity test
   nc -zv $VPCE_DNS 6514
   nc -zv $VPCE_DNS 1514
   ```

   If the connection is refused or times out, verify VPN/Direct Connect routing and that the device can reach the VPC endpoint subnet.

1. **Check the VPC endpoint policy.**

   If you have attached a custom VPC endpoint policy, verify it allows the required actions. Check the `SyslogMessagesDropped` metric with `Reason=VpcePolicyDenied`.

## TLS handshake failures
<a name="CWL_Syslog_Troubleshooting_TLS"></a>

If your syslog client fails to establish a TLS connection on port 6514:
+ **Certificate trust** – Ensure your device's CA trust store includes the Amazon Trust Services root certificates. Most operating systems include these by default. Download them from [https://www.amazontrust.com/repository/](https://www.amazontrust.com/repository/) if needed.
+ **TLS version** – The service supports TLS 1.2 and TLS 1.3. Ensure your syslog client supports at least TLS 1.2.
+ **Hostname verification** – If your client verifies the server hostname, ensure it is configured to connect using the VPC endpoint DNS name (not an IP address).

Test the TLS connection manually with OpenSSL:

```
openssl s_client -connect $VPCE_DNS:6514 -brief
```

A successful connection shows the TLS version and cipher suite. If it fails, the error message indicates the cause.

## UDP messages lost
<a name="CWL_Syslog_Troubleshooting_UDP"></a>

UDP is a best-effort protocol. Some message loss is expected behavior under the following conditions:
+ Network congestion between your device and the VPC endpoint.
+ Messages exceed the maximum UDP datagram size.
+ Temporary service capacity constraints (indicated by `SyslogMessagesDropped` with `Reason=ServiceUnavailable`).

If reliable delivery is required, use TCP (port 1514 or 6514) instead. TCP provides delivery acknowledgment and automatic retransmission.

## Connection refused
<a name="CWL_Syslog_Troubleshooting_ConnectionRefused"></a>

If your device reports "connection refused" when connecting to the VPC endpoint:
+ Verify the VPC endpoint is in the `available` state:

  ```
  aws ec2 describe-vpc-endpoints --vpc-endpoint-ids $VPCE_ID \
    --region $REGION --query 'VpcEndpoints[0].State'
  ```
+ Verify you are connecting on a supported port (6514, 1514, or 514).
+ Verify VPN or Direct Connect routing allows traffic from your device's network to the VPC endpoint subnet.
+ Check the security group allows inbound traffic on the port you are using.

## Messages dropped due to rate limiting
<a name="CWL_Syslog_Troubleshooting_RateLimit"></a>

If the `SyslogMessagesDropped` metric shows `Reason=MessageRateLimitExceeded`, your syslog traffic is exceeding your account's `PutLogEvents` quota.

To resolve this:

1. Check your current quota in the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home#!/services/logs/quotas) under Amazon CloudWatch Logs.

1. Request a quota increase if your syslog throughput requires it. See [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *Service Quotas User Guide*.