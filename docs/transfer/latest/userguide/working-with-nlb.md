

# Working with Network Load Balancers
<a name="working-with-nlb"></a>

Whether you can place a Network Load Balancer (NLB) in front of an AWS Transfer Family server depends on the protocol that your server uses. Review the following guidance before you add an NLB to your architecture.
+ **FTP and FTPS** – We recommend against placing an NLB in front of the server. An NLB in this path increases costs and reduces the number of simultaneous connections that the server accepts. If your FTP or FTPS implementation requires an NLB, see [Avoid placing NLBs and NATs in front of AWS Transfer Family servers](infrastructure-security.md#nlb-considerations) for configuration recommendations.
+ **SFTP** – An NLB is supported. With PROXY protocol v2 (PPv2), you can preserve the client's source IP address on SFTP connections.

A common reason to place an NLB in front of an AWS Transfer Family server is to offer a custom listener port. AWS Transfer Family already offers several ports, so review [AWS Transfer Family endpoint type matrix](sftp-for-transfer-family.md#endpoint-matrix) and [Create an SFTP-enabled server](create-server-sftp.md) for the supported ports before you add an NLB.

## Preserving the client's source IP for SFTP with PROXY protocol v2
<a name="nlb-sftp-source-ip"></a>

When an NLB is in the path between your client and your SFTP server, AWS Transfer Family sees the private IP address of the NLB instead of the client's source IP address. PROXY protocol v2 (PPv2) solves this problem. The NLB adds a PPv2 header that carries the client's source IP address, and AWS Transfer Family reads that header.

When you enable PPv2, the client's source IP address becomes available in the following places:
+ Authentication requests that AWS Transfer Family sends to your custom identity provider. You can then write IP-based access policies.
+ Log entries in Amazon CloudWatch Logs.

## Enable PROXY protocol v2 enforcement on an existing server
<a name="nlb-sftp-enable-ppv2"></a>

The `SftpMode` member of `ProxyConfig` controls how your server handles the PPv2 header. It has exactly two values: `NONE` (the default) and `PROXY_PROTOCOL_V2_ENFORCED`. For more information, see [ProtocolDetails](https://docs.aws.amazon.com/transfer/latest/APIReference/API_ProtocolDetails.html) in the *AWS Transfer Family API Reference*.

**Important**  
With `PROXY_PROTOCOL_V2_ENFORCED` you must restrict the server's VPC endpoint security group to allow inbound traffic only via the trusted NLB.

Complete the following three steps in order to enable enforcement without refusing any connections. This order keeps the migration free of downtime.

### Step 1: Enable PROXY protocol v2 on the NLB target group
<a name="nlb-sftp-enable-step1"></a>

Enable the `proxy_protocol_v2.enabled` attribute on the NLB target group that points at your server's VPC endpoint. This attribute tells the NLB to prepend a PPv2 header to each connection. For instructions, see [Proxy protocol](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/edit-target-group-attributes.html#proxy-protocol) in the *Elastic Load Balancing User Guide*.

While the server is still set to `SftpMode=NONE`, it reads and ignores any PPv2 header. Enabling PROXY protocol v2 on the target group at this stage causes no disruption.

### Step 2: Verify that the header arrives on every connection
<a name="nlb-sftp-enable-step2"></a>

Before you enforce PPv2, confirm that the server receives a PPv2 header on every connection. Inspect your server logs for the `CONNECTED` activity type. In structured (JSON) logs in Amazon CloudWatch Logs, check the `proxy-protocol-v2-header` field for the value `ignored`; in legacy logs, check the `ProxyProtocolV2Header` field for the same value.

The field has the following semantics:
+ The field is absent when the connection included no PPv2 header.
+ The value is `ignored` when the connection included a PPv2 header while `SftpMode` is `NONE`.
+ The value is `applied` when the connection included a PPv2 header and the server honored it under `PROXY_PROTOCOL_V2_ENFORCED`.

Keep checking the logs until every `CONNECTED` entry carries the field with the value `ignored`. An absent field means that some path still reaches the server without a PPv2 header. If you enforce while any path is missing the header, the server refuses those connections. For more information about these log fields, see [JSON structured logs for Transfer Family](cw-structure-logs.md#json-log-entries) and [Legacy logs for Transfer Family](cw-structure-logs.md#legacy-log-entries).

### Step 3: Enforce PROXY protocol v2
<a name="nlb-sftp-enable-step3"></a>

Update the server so that the `SftpMode` member of `ProxyConfig` is `PROXY_PROTOCOL_V2_ENFORCED`. The server then requires a valid PPv2 header on every incoming SFTP connection. The server refuses connections that arrive without a valid PPv2 header and logs an error to Amazon CloudWatch Logs. To roll back, set `SftpMode` to `NONE`.

------
#### [ Console ]

On the **Server details** page, choose **Edit** next to **Additional details**, and then turn on the **PROXY protocol configuration** option. For the full edit-server procedure, see [Edit server details](edit-server-config.md).

------
#### [ AWS CLI ]

Run the following command to enforce PROXY protocol v2 on your server.

```
aws transfer update-server --server-id {{your-server-id}} --protocol-details ProxyConfig={SftpMode=PROXY_PROTOCOL_V2_ENFORCED}
```

If successful, the command returns the following code and updates your server.

```
{
    "ServerId": "{{your-server-id}}"
}
```

------