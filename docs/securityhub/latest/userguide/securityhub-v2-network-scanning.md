# Network Scanning in Security Hub

Network Scanning is an opt-in feature of Security Hub that performs active network reachability testing on your cloud resources.
Control-plane analysis evaluates security groups, Network Access Control Lists (NACLs), and route tables to determine what _could_ be reachable. Network Scanning goes further by detecting what is _actually_ reachable. It probes your resources from outside your accounts to identify open ports and running services.

All scans originate from AWS-owned IP addresses and answer two questions: Is this
resource reachable from the internet? If reachable, what is running? Network Scanning publishes
results as standalone OCSF findings in Security Hub with scan evidence.

## Supported resource types

Network Scanning supports the following resource types.

| Cloud provider | Resource type                   |
| -------------- | ------------------------------- |
| AWS            | EC2 Instance (with public IP)   |
| AWS            | Elastic IP (EIP)                |
| AWS            | Network Load Balancer (NLB)     |
| AWS            | Application Load Balancer (ALB) |
| AWS            | Classic Load Balancer (CLB)     |
| Azure          | Public IP Address               |

###### Note

Network Scanning scans each resource type independently. For load balancers, Network
Scanning resolves and scans the DNS name. Network Scanning only scans individual EC2
instances behind a load balancer if they have their own public IP or EIP.

## Enable Network Scanning

To enable Network Scanning, Security Hub must be enabled on your account. You can enable
Network Scanning through a configuration policy or for individual accounts.

**Organization accounts (recommended)** – Enable Network
Scanning across your organization's accounts and Regions by creating or editing a configuration policy.
For more information about editing a configuration policy, see [Editing a configuration policy](securityhub-v2-da-policy.md#securityhub-v2-configuration-edit "securityhub-v2-da-policy.md#securityhub-v2-configuration-edit").
When Network Scanning is enabled through a configuration policy, member accounts cannot turn off the feature.

**Individual accounts** – For accounts that are not managed
by a configuration policy, you can enable Network Scanning using one of the following methods.

###### Note

By enabling Network Scanning, you authorize Security Hub to perform active network scanning
against resources in your AWS environments and Azure environments. This includes TCP port
connection attempts, application and protocol identification, and collection of service
banners, HTTP headers, and TLS certificate metadata.

Security Hub console

###### To enable Network Scanning

1. Open the Security Hub console at
   [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home "https://console.aws.amazon.com/securityhub/v2/home").
2. In the navigation pane, choose **General settings**.
3. Locate the **Network Scanning** section.
4. Choose **Enable**.
5. Confirm the authorization to proceed with active network scanning.

Security Hub API
Invoke the `EnableSecurityHubFeatureV2` API with the feature name
`NETWORK_SCANNING`.

###### Note

Calling this API when Network Scanning is already enabled returns a 200 response.
The service preserves the `UpdatedAt` timestamp from the original
enablement.

AWS CLI
Run the following command to enable Network Scanning:

```
aws securityhub enable-security-hub-feature-v2 --feature-name NETWORK_SCANNING
```

## How Network Scanning works

After you enable Network Scanning, the following occurs:

- Network Scanning scans existing resources within approximately 24 hours of enabling the feature.
- Network Scanning scans new resources shortly after Security Hub receives notification of the created resource.
- Network Scanning rescans resources when certain eligible control plane changes are made to a scan-eligible resource.
- Network Scanning rescans active resources roughly every 12 hours to detect reachability changes.

Ephemeral or short-lived resources might not be scanned before they are terminated.

## Network Scanning findings

Network Scanning publishes findings in OCSF format, using the AWS OCSF Extension, and
they appear alongside other Security Hub findings. Each finding represents a single reachable
port on a specific resource and address combination.
Scan results are contained in the `port_scan_result_list` section of an OCSF finding.
The following examples show information returned for a reachable resource:

```

"port_scan_result_list": [
    {
      "port_info": {
        "port": 6379,
        "protocol_name": "tcp",
        "protocol_num": 6
      },
      "status": "Open",
      "status_id": 1,
      "svc_name": "redis"
    }
],

```

```

"port_scan_result_list": [
    {
      "http_response": {
        "code": 200,
        "content_type": "text/html; charset=UTF-8",
        "http_headers": [
          {
            "name": "Server",
            "value": "Apache/2.4.68 (Amazon Linux)"
          },
          {
            "name": "Content-Type",
            "value": "text/html; charset=UTF-8"
          }
        ],
        "latency": 124
      },
      "port_info": {
        "port": 8080,
        "protocol_name": "tcp",
        "protocol_num": 6
      },
      "status": "Open",
      "status_id": 1
    }
  ],

```

If no finding exists for a resource, Network Scanning did not detect it as reachable from the
internet. The absence of a finding indicates that the resource is not internet-reachable from
the scanning infrastructure.

The following table describes the lifecycle for a Network Scanning finding.

Finding lifecycle events| Event | What happens |
| --- | --- |
| Port first detected as reachable | Network Scanning creates and publishes a new finding |
| Port still reachable on rescan (no change) | Network Scanning periodically refreshes the finding |
| Port still reachable but evidence changed | Network Scanning republishes the finding with updated evidence |
| Port no longer reachable | Finding remains open until next rescan confirms port is unreachable |
| Resource terminated or deleted | Network Scanning closes all findings for the resource by setting the `activity_name` attribute to `Close` |
| IP address removed from resource | Network Scanning closes findings for that specific IP |
| Network Scanning disabled | Network Scanning produces no new findings; existing findings remain until aged off |
| Security Hub disabled | You no longer have access to findings |

If a port is intermittently reachable, Network Scanning bases findings on positive evidence
at scan time. After you fix an issue (for example, by closing a firewall rule or stopping
a service), Network Scanning closes the finding on the next scan.

Disabling Network Scanning does not immediately close findings. Existing findings
remain visible until they age out through the normal Security Hub finding lifecycle.

###### Note

When an EIP is attached to an EC2 instance, Network Scanning produces findings on the
EIP resource. The EIP is the top-level IP resource that owns the address. For NLB
resources, the DNS name and attached EIPs are distinct network entry points, so Network
Scanning produces separate findings for each.

## Scan evidence

When Network Scanning detects that a port is reachable, the finding includes evidence about the reachable service. The following types of evidence can be collected:

**TCP Banner**

Initial bytes sent by the service upon connection, such as an SSH version string.

**HTTP Metadata**

Response headers and HTTP status code.

**TLS Certificate**

Common Name (CN), issuer, expiry date, and self-signed status.

**Service Detection**

Identified application or protocol running on the port.

## Excluding resources from scanning

To exclude a resource from Network Scanning, add the tag key
`SecurityHubNetworkScanExclusion` to the resource. The tag value can be any value
or empty.

You must apply the tag to the actual resource with the scannable public IP:

- For an EIP attached to an EC2 instance – tag the EIP, not the EC2
  instance.
- For an EC2 instance with only a public IP (no EIP) – tag the EC2
  instance.
- For a load balancer – tag the load balancer and any targets with individual
  public IPs.

When you add the exclusion tag, Network Scanning stops future scans and closes active
findings for that resource. Removing the tag makes the resource eligible for scanning
again.

## Scan traffic

Scans use TCP only (no UDP) and scan a well-known subset of TCP ports.
The exact list of ports might evolve over time.
The scanning service never runs inside your VPC or account – it operates from AWS-owned infrastructure.

## Multi-cloud support

Network Scanning supports Azure Public IP Addresses.
To scan Azure resources, create a Security Hub connector to your Azure environment.
For more information about integrating with Microsoft Azure, see [Integrating Security Hub with Microsoft Azure](securityhub-v2-azure.md "securityhub-v2-azure.md").

Scanning behavior, evidence, and findings for Azure resources are identical to AWS resources.
Findings appear alongside AWS findings with appropriate cloud provider and region metadata.

## Region availability

Network Scanning is available in commercial AWS Regions where Security Hub is available.

## Disable Network Scanning

If your organization uses configuration policies, the delegated administrator can disable Network Scanning across specific accounts and Regions by editing the configuration policy.
For more information about editing a configuration policy, see [Editing a configuration policy](securityhub-v2-da-policy.md#securityhub-v2-configuration-edit "securityhub-v2-da-policy.md#securityhub-v2-configuration-edit").
When editing the policy, select the Network Scanning capability, choose **Disable**, and then specify the accounts and Regions where you want to turn off scanning.

For accounts that are not managed by a configuration policy, you can disable Network Scanning using one of the following methods.

Security Hub console

###### To disable Network Scanning

1. Open the Security Hub console at
   [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home "https://console.aws.amazon.com/securityhub/v2/home").
2. In the navigation pane, choose **General settings**.
3. Locate the **Network Scanning** section.
4. Choose **Disable**.
5. Confirm that you want to disable Network Scanning.

Security Hub API
Invoke the `DisableSecurityHubFeatureV2` API with the feature name
`NETWORK_SCANNING`.

AWS CLI
Run the following command to disable Network Scanning:

```
aws securityhub disable-security-hub-feature-v2 --feature-name NETWORK_SCANNING
```

When you disable Network Scanning:

- Network Scanning does not trigger new scans.
- Existing findings remain visible until they age out through the normal Security Hub finding lifecycle.
- Network Scanning completes any scans already in progress.
