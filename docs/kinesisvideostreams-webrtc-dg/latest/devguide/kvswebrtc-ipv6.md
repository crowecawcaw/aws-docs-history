# Use IPv6/Dual-Stack endpoints with Amazon Kinesis Video WebRTC

You can configure Amazon Kinesis Video WebRTC to use IPv6 for both control plane and data plane operations. This enables your applications to communicate with Kinesis Video WebRTC services using IPv6 addresses through dual-stack endpoints.

###### Note

IPv6 support requires specific SDK versions and configuration settings. Ensure that your Kinesis Video WebRTC SDK and Amazon Web Services SDK versions support IPv6 dual-stack endpoints. Dual-stack endpoints support both IPv4 and IPv6 traffic and are available for some services in some Region.

Amazon Kinesis Video WebRTC supports IPv6 through dual-stack endpoints for both master and viewer applications. You can configure your applications to use IPv6/Dual-Stack endpoints for control plane API calls and data plane operations.

## Configure the Amazon Web Services SDK for IPv6-Dual-Stack Endpoints

If you're using the Amazon Web Services SDK to call Kinesis Video WebRTC control plane APIs in your production setup, you can enable IPv6 by configuring dual-stack endpoints. The Amazon Web Services SDK provides several standardized methods to enable dual-stack endpoints.

###### Important

When dual-stack endpoints are enabled, the SDK attempts to use dual-stack endpoints to make network requests. If a dual-stack endpoint doesn't exist for the service or Region, the request fails.

### Use environment variables

Set the following environment variable to enable IPv6 dual-stack endpoints:

```
export AWS_USE_DUALSTACK_ENDPOINT=true
```

### Use the Amazon Web Services configuration file

Add the following setting to your Amazon Web Services configuration file (~/.aws/config):

```
[default]
use_dualstack_endpoint = true
```

### Use JVM system properties (Java and Kotlin SDKs only)

For Java and Kotlin applications, set the following JVM system property:

```
-Daws.useDualstackEndpoint=true
```

Or programmatically in your Java code:

```
System.setProperty("aws.useDualstackEndpoint", "true");
```

### SDK support

The following Amazon Web Services SDKs support dual-stack endpoint configuration:

| SDK                     | Supported | Configuration methods                                  |
| ----------------------- | --------- | ------------------------------------------------------ |
| AWS CLI v2              | Yes       | Environment variable, configuration file               |
| SDK for C++             | Yes       | Environment variable, configuration file               |
| SDK for Go V2 (1.x)     | Yes       | Environment variable, configuration file               |
| SDK for Go 1.x (V1)     | Yes       | Environment variable, configuration file               |
| SDK for Java 2.x        | Yes       | Environment variable, configuration file, JVM property |
| SDK for Java 1.x        | No        | Not supported                                          |
| SDK for JavaScript 3.x  | Yes       | Environment variable, configuration file               |
| SDK for JavaScript 2.x  | Yes       | Environment variable, configuration file               |
| SDK for Kotlin          | Yes       | Environment variable, configuration file, JVM property |
| SDK for .NET 4.x        | Yes       | Environment variable, configuration file               |
| SDK for .NET 3.x        | Yes       | Environment variable, configuration file               |
| SDK for PHP 3.x         | Yes       | Environment variable, configuration file               |
| SDK for Python (Boto3)  | Yes       | Environment variable, configuration file               |
| SDK for Ruby 3.x        | Yes       | Environment variable, configuration file               |
| SDK for Rust            | Yes       | Environment variable, configuration file               |
| SDK for Swift           | Yes       | Environment variable, configuration file               |
| Tools for PowerShell V5 | Yes       | Environment variable, configuration file               |
| Tools for PowerShell V4 | Yes       | Environment variable, configuration file               |

After you configure dual-stack endpoints, the Amazon Web Services SDK automatically uses IPv6 endpoints when calling Kinesis Video WebRTC control plane APIs.

## Configure the Kinesis Video WebRTC SDK for IPv6/Dual-Stack Endpoints

The Kinesis Video WebRTC SDK provides dual-stack configuration options for both control plane and data plane operations. These settings work with the Amazon Web Services SDK dual-stack endpoint configuration.

## Configure the WebRTC C SDK

To use dual-stack AWS KVS endpoints and attempt to gather IPv6 ICE candidates, set the following environment variable:

```
export KVS_DUALSTACK_ENDPOINTS=ON
```

In dual-stack mode, ICE gathering will attempt to include IPv6 candidates, but compatibility ultimately depends on the local network configuration and the capabilities of the receiving peers.

To disable dual-stack mode, unset the environment variable:

```
unset KVS_DUALSTACK_ENDPOINTS
```

## Data plane endpoint resolution

For data plane operations, the Kinesis Video WebRTC SDK uses the GetSignalingChannelEndpoint API to retrieve the appropriate IPv6/Dual-stack data plane endpoint. The SDK automatically requests IPv6/Dual-stack endpoints when IPv6/Dual-stack is configured.

###### Important

The GetSignalingChannelEndpoint API has been updated to support IPv6 endpoints. Ensure that you're using a compatible SDK version that supports this functionality.

## Configure the AWS CLI for IPv6/Dual-Stack

If you're using the AWS CLI for Kinesis Video WebRTC operations (typically for proof-of-concept work), you can enable IPv6 by configuring dual-stack endpoints.

### Use an environment variable

```
export AWS_USE_DUALSTACK_ENDPOINT=true
```

### Use the Amazon Web Services configuration file

Add the following to your AWS CLI configuration file (~/.aws/config):

```
[default]
use_dualstack_endpoint = true
```

After you configure dual-stack endpoints, the AWS CLI uses IPv6 dual-stack endpoints for all Amazon Web Services calls, including Kinesis Video WebRTC operations.

## Considerations

### IoT credentials provider

If you're using IoT credentials for authentication:

- IoT credentials endpoints support IPv6
- Configure dual-stack endpoints using the standard Amazon Web Services SDK configuration methods described previously
- The IoT credentials flow is separate from Kinesis Video WebRTC-specific IPv6 configuration

### Network requirements

- Ensure that your network infrastructure supports IPv6 connectivity
- Verify that your security groups and network ACLs allow IPv6 traffic
- Test connectivity to Amazon Web Services IPv6 endpoints from your deployment environment
- Dual-stack endpoints are available for some services in some Regions—verify availability for your target Regions

### SDK compatibility

- Ensure that you're using a supported Amazon Web Services SDK version (see the compatibility table)
- The Amazon Web Services SDK for Java 1.x doesn't support dual-stack endpoint configuration
- For the SDK for Go 1.x (V1), you must enable loading from the configuration file to use shared configuration file settings

### Testing and validation

Before you deploy IPv6-enabled Kinesis Video WebRTC applications to production:

- Test control plane operations (channel creation, deletion, listing)
- Verify data plane operations (STUN, TURN and WebRTC Signaling)
- Verify successful peer-to-peer streaming session establishment
- Validate performance and connectivity in your network environment
- Run canary tests to ensure consistent IPv6 functionality
- Test failover behavior when dual-stack endpoints aren't available

## Customers impacted by the upgrade to include IPv6

When you enable IPv6 for Amazon Kinesis Video WebRTC, there are several areas where you might need to update your existing configurations and policies to ensure continued functionality. This section outlines the key areas that require attention when transitioning to IPv6-enabled endpoints.

### IAM policies and IP address filtering

If you use source IP address filtering in your IAM user policies, role policies, or resource-based policies, you need to update these policies to include IPv6 address ranges.

###### Important

Existing IAM policies that use IPv4 CIDR blocks in IpAddress or NotIpAddress conditions will not automatically work with IPv6 addresses. You must explicitly add IPv6 ranges to maintain access control.

Example IAM policy update for IPv6:

```
{
  "Version": "2012-10-17"		 	 	 ,
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": "kinesisvideo:*",
      "Resource": "*",
      "Condition": {
        "IpAddress": {
          "aws:SourceIp": [
            "192.0.2.0/24",
            "203.0.113.0/24",
            "2001:db8::/32"
          ]
        }
      }
    }
  ]
}
```

Key considerations for IAM policy updates:

- Add IPv6 CIDR blocks alongside existing IPv4 ranges
- Use the aws:SourceIp condition key for both IPv4 and IPv6 addresses
- Test policies in a non-production environment before deploying
- Consider using aws:RequestedRegion as an additional condition for enhanced security

### Network security groups and access control lists

If you're running Kinesis Video WebRTC applications on Amazon EC2 instances or other Amazon Web Services services, you need to update your security groups and network ACLs to allow IPv6 traffic.

- **Security groups** – Add inbound and outbound rules for IPv6 CIDR blocks (::/0 for all IPv6 traffic, or specific IPv6 ranges)
- **Network ACLs** – Update subnet-level network ACLs to allow IPv6 traffic on the required ports
- **Route tables** – Ensure that your VPC route tables include routes for IPv6 traffic to reach internet gateways or NAT gateways

### Logging and monitoring

IPv6 addresses have a different format than IPv4 addresses, which can impact your logging, monitoring, and analytics systems.

#### AWS CloudTrail logs

AWS CloudTrail logs will contain IPv6 addresses in the sourceIPAddress field when requests are made over IPv6. Update your log parsing tools and scripts to handle IPv6 address formats.

Example IPv6 address in AWS CloudTrail logs:

```
{
  "sourceIPAddress": "2001:db8::1",
  "eventName": "CreateSignalingChannel",
  "eventSource": "kinesisvideo.amazonaws.com"
}
```

#### Application logs

If your applications log client IP addresses or perform IP-based analytics, ensure that your logging infrastructure can handle IPv6 addresses:

- Update log parsing regular expressions to match IPv6 format
- Modify database schemas if you store IP addresses with fixed-length fields
- Update analytics queries and dashboards to work with IPv6 addresses
- Consider using IP address normalization libraries for consistent handling

#### Monitoring and alerting

Update your monitoring and alerting systems to account for IPv6 traffic:

- Amazon CloudWatch metrics and alarms that filter by IP address
- Custom metrics that track IP-based patterns
- Security monitoring tools that analyze traffic patterns
- Geolocation services that map IP addresses to locations

### Third-party integrations

Review and update third-party services and tools that integrate with your Kinesis Video WebRTC applications:

- **Content delivery networks (CDNs)** – Ensure CDN configurations support IPv6 if you're using CDNs for video distribution
- **Load balancers** – Configure Application Load Balancers or Network Load Balancers to handle IPv6 traffic
- **DNS services** – Update DNS records to include AAAA records for IPv6 addresses
- **Firewall and security appliances** – Configure network security appliances to allow IPv6 traffic
- **Monitoring tools** – Verify that third-party monitoring and analytics tools support IPv6 address formats

### Application code updates

Review your application code for IPv4-specific assumptions that might need updating:

- **IP address validation** – Update input validation to accept IPv6 address formats
- **Database schemas** – Ensure IP address fields can store IPv6 addresses (typically requiring larger field sizes)
- **Configuration files** – Update any hardcoded IPv4 addresses or CIDR blocks
- **Client libraries** – Verify that HTTP clients and networking libraries support IPv6
- **Error handling** – Update error handling to account for IPv6-specific network errors

### Testing and validation

Before enabling IPv6 in production, thoroughly test your applications and infrastructure:

- **Connectivity testing** – Verify that all components can communicate over IPv6
- **Performance testing** – Compare IPv6 and IPv4 performance to identify any issues
- **Security testing** – Validate that security controls work correctly with IPv6 traffic
- **Failover testing** – Test behavior when IPv6 connectivity is unavailable
- **Log analysis** – Verify that logging and monitoring systems correctly handle IPv6 addresses
- **Integration testing** – Test all third-party integrations with IPv6 enabled

### Migration strategy

Consider implementing a phased approach to IPv6 adoption:

1. **Assessment phase** – Inventory all systems and identify IPv6 readiness
2. **Preparation phase** – Update policies, security groups, and application code
3. **Testing phase** – Enable IPv6 in development and staging environments
4. **Pilot phase** – Enable IPv6 for a subset of production traffic
5. **Full deployment** – Gradually increase IPv6 traffic until fully deployed
6. **Monitoring phase** – Continuously monitor for issues and optimize performance

## Troubleshooting

### Common issues

- **Connection failures** – Verify IPv6 network connectivity and DNS resolution
- **SDK errors** – Ensure that you're using compatible SDK versions that support dual-stack endpoints
- **Authentication issues** – Confirm that IAM policies and credentials work with IPv6 endpoints
- **Endpoint not available** – If a dual-stack endpoint doesn't exist for the service or Region, requests fail

### Verification steps

- Check that AWS_USE_DUALSTACK_ENDPOINT=true is set or use_dualstack_endpoint = true is in your configuration file
- Verify that Kinesis Video WebRTC SDK IPv6 configuration flags are properly set
- Test network connectivity to Amazon Web Services IPv6 endpoints
- Review application logs for IPv6-specific error messages
- Confirm that your Region supports dual-stack endpoints for Kinesis Video WebRTC

### Configuration validation

You can verify your dual-stack endpoint configuration by checking:

- **Environment variables:** echo $AWS_USE_DUALSTACK_ENDPOINT
- **Amazon Web Services configuration file:** cat ~/.aws/config | grep use_dualstack_endpoint
- **JVM properties (Java):** Check system properties in your application logs

For additional support and troubleshooting, see the AWS documentation or contact AWS.
