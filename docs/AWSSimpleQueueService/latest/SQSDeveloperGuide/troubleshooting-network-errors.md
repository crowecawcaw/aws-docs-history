# Troubleshoot Amazon SQS network errors

The following topics cover the most common causes for network issues in Amazon SQS, and how to
troubleshoot them.

## ETIMEOUT error

The ETIMEOUT error occurs when the client can't establish a TCP connection
to an Amazon SQS endpoint.

**Troubleshooting:**

- **Check the network connection**

Test your network connection to Amazon SQS by running commands like
`telnet`.

Example: telnet sqs.us-east-1.amazonaws.com 443

- **Check network settings**
  - Make sure that your local firewall rules, routes, and access control lists (ACLs)
    allow traffic on the port that you use.
  - The security group outbound (egress) rules must allow traffic to the port 80 or
  443.
  - The network ACL outbound (egress) rules must allow traffic to TCP port 80 or
  443.
  - The network ACL inbound (ingress) rules must allow traffic on TCP ports
    1024-65535.
  - Amazon Elastic Compute Cloud (Amazon EC2) instances that connect to the public internet must have [internet connectivity](../../../vpc/latest/userguide/VPC_Internet_Gateway.md#vpc-igw-internet-access "../../../vpc/latest/userguide/VPC_Internet_Gateway.md#vpc-igw-internet-access").

- **Amazon Virtual Private Cloud (Amazon VPC) endpoints**

If you access Amazon SQS through an Amazon VPC endpoint, then the endpoints security group must
allow inbound traffic to the clients security group on port 443. The network ACL
associated with the subnet of the VPC endpoint must have this configuration:

    + The network ACL outbound (egress) rules must allow traffic on TCP ports 1024-65535
     (ephemeral ports).
    + The network ACL inbound (ingress) rules must allow traffic on port 443.

Also, the Amazon SQS VPC endpoint AWS Identity and Access Management (IAM) policy must allow access. The following
example VPC endpoint policy specifies that the IAM user `MyUser` is
allowed to send messages to the Amazon SQS queue `MyQueue`. Other actions,
IAM users, and Amazon SQS resources are denied access through the VPC endpoint.

```
{
    "Statement": [{
        "Action": ["sqs:SendMessage"],
        "Effect": "Allow",
        "Resource": "arn:aws:sqs:us-east-2:123456789012:`MyQueue`",
        "Principal": {
            "AWS": "arn:aws:iam:123456789012:user/`MyUser`"
        }
    }]
}
```

## UnknownHostException error

The UnknownHostException error occurs when the host IP address couldn't be
determined.

**Troubleshooting:**

Use the nslookup utility to return the IP address associated with the host
name:

- Windows and Linux OS

```
nslookup sqs.<region>.amazonaws.com
```

- AWS CLI or SDK for Python legacy endpoints:

```
nslookup <region>.queue.amazonaws.com
```

If you received an unsuccessful output, follow the instructions in [How does DNS work and how do
I troubleshoot partial or intermittent DNS failures?](https://repost.aws/knowledge-center/sqs-connection-error "https://repost.aws/knowledge-center/sqs-connection-error") in the _AWS Knowledge Center Guide_.

If you received a valid output, then it is likely to be an application-level issue. To
resolve application-level issues, try the following methods:

- Restart your application.
- Confirm that your Java application doesn't have a bad DNS cache. If possible,
  configure your application to adhere to the DNS TTL. For more information, see [Setting the
  JVM TTL for DNS name lookups](../../../sdk-for-java/v1/developer-guide/jvm-ttl-dns.md "../../../sdk-for-java/v1/developer-guide/jvm-ttl-dns.md").

For additional information on how to troubleshoot network errors, see [How do I troubleshoot Amazon SQS
“ETIMEOUT” and “UnknownHostException” connection errors?](https://repost.aws/knowledge-center/sqs-connection-error "https://repost.aws/knowledge-center/sqs-connection-error") in the _AWS Knowledge Center Guide_.
