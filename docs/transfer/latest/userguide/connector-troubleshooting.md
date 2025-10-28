# Troubleshoot SFTP connector issues

This section describes possible solutions for issues with SFTP connectors.

###### Topics

- [Troubleshoot adding trusted host keys for your
  SFTP connector](#sftp-connector-keys "#sftp-connector-keys")
- [Key negotiation fails](#sftp-connector-issue-kex "#sftp-connector-issue-kex")
- [SFTP connector throttling](#sftp-connector-throttling "#sftp-connector-throttling")
- [Optimizing SFTP connector
  performance](#sftp-connector-performance "#sftp-connector-performance")
- [Troubleshoot VPC connectivity
  issues](#sftp-connector-vpc-troubleshooting "#sftp-connector-vpc-troubleshooting")
- [Miscellaneous SFTP connector issues](#sftp-connector-issue-misc "#sftp-connector-issue-misc")

## Troubleshoot adding trusted host keys for your

SFTP connector

Description

When you are creating or editing an SFTP connector, and you are adding a trusted host
key, you receive the following error: `Failed to edit connector details (Invalid
 host key format.)`

Cause

If you paste in a correct public key, the issue might be that you included the
`comment` portion of the key. AWS Transfer Family does not currently accept the
comment portion of the key.

Solution

Delete the comment portion of the key, when you paste it into the text field. For
example, assume your key looks similar to the following:

```
ssh-rsa AAAA...== marymajor@dev-dsk-marymajor-1d-c1234567.us-east-1.amazon.com
```

Remove the text that follows the `==` characters and only paste in the
portion of the key up to and including the `==`.

```
ssh-rsa AAAA...==
```

## Key negotiation fails

Description

You receive an error where the key exchange negotiation fails. For example:

```
Key exchange negotiation failed due to incompatible host key algorithms.
Client offered: [ecdsa-sha2-nistp256, ecdsa-sha2-nistp384,
ecdsa-sha2-nistp521, rsa-sha2-512, rsa-sha2-256] Server offered: [ssh-rsa]
```

Cause

This error is because there's no overlap between the host key algorithms supported by
the server and those supported by the connector.

Solution

Ensure that the remote server supports at least one of the Client host key algorithms
listed in the error message. For the list of supported algorithms, see [Security policies for AWS Transfer Family SFTP
connectors](security-policies-connectors.md "security-policies-connectors.md").

## SFTP connector throttling

Description

When using SFTP connectors for file transfers, you encounter errors such as:

```
{"type":"ExecutionThrottled","details":{},"connectorId":"c-1234567890abcdef0"}
```

Or you notice that file transfers are being delayed or failing intermittently during
high-volume operations.

Cause

SFTP connectors have service quotas that limit the number of concurrent file transfers
and API operations. When these limits are exceeded, throttling occurs to protect the
service and ensure fair usage across all customers.

Solution

To address SFTP connector issues, try the following solutions:

1. Implement exponential backoff and retry logic in your applications. For
   example, create a function that automatically retries failed operations with
   increasing wait times between attempts.
2. Implement rate limiting in your application:
   - Limit the number of concurrent transfers.
   - Add delays between batches of transfers.

3. Monitor your usage against service quotas:
   - Use CloudWatch metrics to track API usage.
   - Set up alarms to notify you when approaching quota limits.

4. For options to scale your SFTP connectors, see [Scaling your SFTP
   connectors](scale-and-limits-sftp-connector.md#scaling-sftp-connector "scale-and-limits-sftp-connector.md#scaling-sftp-connector").
5. If throttling persists and impacts your business operations, request a quota
   increase through the Service Quotas console.

## Optimizing SFTP connector

performance

Description

Your SFTP connector transfers are slower than expected or you experience inconsistent
performance.

Cause

SFTP connector performance can be affected by various factors including network
conditions, file sizes, remote server configuration, and concurrent transfer
limits.

Solution

To optimize SFTP connector performance:

- Configure your remote SFTP server for optimal performance:
  - Increase maximum sessions and transfers per session
  - Optimize TCP window sizes for high-latency connections
  - Use compression if supported by both ends

- Consider network optimization, by placing your Transfer Family connector in a region
  close to your remote SFTP server.
- Implement a monitoring strategy to identify performance bottlenecks:
  - Monitor network throughput and latency
  - Analyze logs for patterns in slow transfers

## Troubleshoot VPC connectivity

issues

This section describes solutions for common issues with VPC_LATTICE-enabled SFTP
connectors.

### Connector stuck in PENDING

status

Description

Your VPC_LATTICE-enabled SFTP connector remains in `PENDING` status for an
extended period (more than 10 minutes).

Cause

This can occur due to DNS resolution delays, Resource Gateway configuration
issues, or VPC Lattice service network association problems.

Solution

Contact AWS Support at [Contact
AWS](https://aws.amazon.com/contact-us "https://aws.amazon.com/contact-us").to help analyze the root cause of the issue. You can also try the
following work-around.

1. Verify that your Resource Gateway is in `ACTIVE` status:

```
aws vpc-lattice get-resource-gateway --resource-gateway-identifier `rgw-1234567890abcdef0`
```

2. Check that your Resource Configuration is properly configured and
   active:

```
aws vpc-lattice get-resource-configuration --resource-configuration-identifier `rcfg-1234567890abcdef0`
```

3. Ensure your Resource Gateway has subnets in at least two Availability
   Zones that support VPC Lattice.
4. If the issue persists, delete and recreate the connector with the same
   configuration.

### Connector in ERRORED status

Description

Your VPC_LATTICE-enabled SFTP connector shows `ERRORED` status with error
details.

Cause

Common causes include invalid Resource Configuration ARN, insufficient IP
addresses in VPC subnets, or cross-region resource sharing attempts.

Solution

1. Check the error details using `describe-connector`:

```
aws transfer describe-connector --connector-id `c-1234567890abcdef0`
```

2. Verify the Resource Configuration ARN is correct and in the same region as
   your connector.
3. Ensure your VPC subnets have sufficient available IP addresses for the
   Resource Gateway.
4. Check that your Resource Configuration target (IP address or DNS name) is
   reachable from your VPC.

### Public IP address not supported

error

Description

You receive an error when trying to create a Resource Configuration with a public
IP address: `ValidationException: IP address x.x.x.x is not in allowed
 ranges.`

Cause

Resource Configurations for public endpoints must use DNS names, not IP
addresses.

Solution

Use the public DNS name of your SFTP server instead of its IP address when
creating the Resource Configuration:

```
aws vpc-lattice create-resource-configuration \
    --name my-public-server-config \
    --resource-gateway-identifier `rgw-1234567890abcdef0` \
    --resource-configuration-definition dnsResource={domainName="my.sftp.server.com"} \
    --port-ranges 22
```

### Availability Zone not supported

error

Description

You receive an error when creating a Resource Gateway: `Subnet subnet-xxx is
 not valid because it is not in a supported Availability Zone.`

Cause

Not all Availability Zones support VPC Lattice Cross-VPC Resource Access. The
error message lists the supported AZs for your region.

Solution

1. Create subnets in the supported Availability Zones listed in the error
   message.
2. Update your Resource Gateway to use subnets from supported AZs
   only.
3. Ensure you have at least two subnets in different supported AZs.

### Connection timeouts with

VPC_LATTICE connectors

Description

File transfers through VPC connectors time out or fail intermittently.

Cause

VPC Lattice has connection limits (350 connections per resource) and idle timeouts
(350 seconds for TCP).

Solution

1. Monitor concurrent connections to stay within the 350 connection limit per
   resource.
2. Implement connection pooling and reuse in your applications.
3. Configure appropriate timeout values in your SFTP client applications
   (less than 350 seconds).
4. Consider creating multiple Resource Configurations for the same target to
   distribute load.

## Miscellaneous SFTP connector issues

Description

You receive an error after you run `StartFileTransfer`, but do not know the
cause of the issue, and only the connector ID is returned after the API call.

Cause

This error can have several causes. To troubleshoot, we recommend that you test your
connector and search your CloudWatch logs.

Solution

- **Test your connector**: See [Test an SFTP connector](test-sftp-connector.md "test-sftp-connector.md"). If the
  test fails, the system provides an error message based on the reason the test
  failed. That section describes how to test your connector from either the
  console or by using the [TestConnection](../APIReference/API_TestConnection.md "../APIReference/API_TestConnection.md") API command.
- **View CloudWatch logs for your connector**: See [Example log entries for SFTP
  connectors](cw-example-logs.md#example-sftp-connector-logs "cw-example-logs.md#example-sftp-connector-logs"). This topic provides examples
  for SFTP connector log entries, and the naming convention to help you find the
  appropriate logs.
