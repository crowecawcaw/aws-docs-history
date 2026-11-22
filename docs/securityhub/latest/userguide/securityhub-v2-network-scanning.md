

# Network Scanning in Security Hub

 Network Scanning is an opt-in feature of Security Hub that performs active network reachability testing on your cloud resources. Control-plane analysis evaluates security groups, Network Access Control Lists (NACLs), and route tables to determine what *could* be reachable. Network Scanning goes further by detecting what is *actually* reachable. It probes your resources from outside your accounts to identify open ports and running services. 

 All scans originate from AWS-owned IP addresses and answer two questions: Is this resource reachable from the internet? If reachable, what is running? Network Scanning publishes results as standalone OCSF findings in Security Hub with scan evidence. 

## Supported resource types
<a name="network-scanning-supported-resources"></a>

 Network Scanning supports the following resource types. 


| Cloud provider | Resource type | 
| --- | --- | 
| AWS | EC2 instance (with public IP) | 
| AWS | Elastic IP (EIP) | 
| AWS | Network Load Balancer (NLB) | 
| AWS | Application Load Balancer (ALB) | 
| AWS | Classic Load Balancer (CLB) | 
| AWS | Amazon Relational Database Service (Amazon RDS) DB instance | 
| Azure | Public IP Address | 
| GCP | VM instance (with public IP) | 
| GCP | External Forwarding Rule (Global and Regional) | 

 The following list describes, at a high level, how Network Scanning scans these resource types: 
+ Network Scanning scans each resource type independently.
+ Only IPv4 addresses are currently supported for scanning across all resource types.
+ For load balancers and RDS DB instances, Network Scanning resolves and scans the DNS name.
+ Network Scanning only scans individual EC2 instances behind a load balancer if they have their own public IP or EIP.
+ For RDS DB instances, Network Scanning scans only instances with public access turned on. For more information, see [Setting up public or private access in Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/gettingstartedguide/security-public-private.html#security-public).
+ For GCP scanning, if the VM instance behind a Forwarding Rule has its own public IP address, Network Scanning will scan both the Forwarding Rule and the VM instance.

## Enable Network Scanning
<a name="enable-network-scanning"></a>

 To enable Network Scanning, Security Hub must be enabled on your account. You can enable Network Scanning through a configuration policy or for individual accounts. 

 **Organization accounts (recommended)** – Enable Network Scanning across your organization's accounts and Regions by creating or editing a configuration policy. For more information about editing a configuration policy, see [Editing a configuration policy](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-v2-da-policy.html#securityhub-v2-configuration-edit). When Network Scanning is enabled through a configuration policy, member accounts cannot turn off the feature. 

 **Individual accounts** – For accounts that are not managed by a configuration policy, you can enable Network Scanning using one of the following methods. 

**Note**  
 By enabling Network Scanning, you authorize Security Hub to perform active network scanning against resources in your AWS environments and Azure environments. This includes TCP port connection attempts, application and protocol identification, and collection of service banners, HTTP headers, and TLS certificate metadata. 

------
#### [ Security Hub console ]

**To enable Network Scanning**

1. Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home).

1. In the navigation pane, choose **General settings**.

1. Locate the **Network Scanning** section.

1. Choose **Enable**.

1. Confirm the authorization to proceed with active network scanning.

------
#### [ Security Hub API ]

Invoke the `EnableSecurityHubFeatureV2` API with the feature name `NETWORK_SCANNING`.

**Note**  
 Calling this API when Network Scanning is already enabled returns a 200 response. The service preserves the `UpdatedAt` timestamp from the original enablement. 

------
#### [ AWS CLI ]

Run the following command to enable Network Scanning:

```
aws securityhub enable-security-hub-feature-v2 --feature-name NETWORK_SCANNING
```

------

## How Network Scanning works
<a name="network-scanning-how-it-works"></a>

 After you enable Network Scanning, the following occurs: 
+ Network Scanning scans existing resources within approximately 24 hours of enabling the feature.
+ Network Scanning scans new resources shortly after Security Hub receives notification of the created resource.
+ Network Scanning rescans resources when certain eligible control plane changes are made to a scan-eligible resource.
+ Network Scanning rescans active resources roughly every 12 hours to detect reachability changes.

 Ephemeral or short-lived resources might not be scanned before they are terminated. 

## Network Scanning findings
<a name="network-scanning-findings"></a>

 Network Scanning publishes findings in Open Cybersecurity Schema Framework (OCSF) format, using the AWS OCSF Extension, and they appear alongside other Security Hub findings. Network Scanning creates findings whether or not a resource has reachable ports. If a finding does not exist for a supported resource type, Network Scanning has not scanned the resource yet. 

### Findings for reachable ports
<a name="network-scanning-reachable-ports"></a>

 Each finding represents a single reachable port on a specific resource and address combination. The `port_scan_result_list` section of an OCSF finding contains the scan results. The following examples show information returned for a reachable resource: 

```json
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

```json
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

### Informational findings for no open ports
<a name="network-scanning-informational-findings"></a>

 Network Scanning creates a finding when it detects no open ports on a resource. This finding has a severity of `Informational` and requires no action. It confirms that Network Scanning scanned the resource. 

 The Informational finding remains open in Security Hub until you delete the resource or until Network Scanning detects open ports on the resource. When Network Scanning identifies open ports on a resource with an Informational finding, it closes the Informational finding. It then creates a finding for each open port. 

 Informational findings for no open ports cover the ports that Network Scanning currently supports. For a list of supported ports, see [Supported ports](#network-scanning-supported-ports). 

### Finding lifecycle events
<a name="network-scanning-finding-lifecycle"></a>

 The following table describes the lifecycle for a Network Scanning finding. 


| Event | What happens | 
| --- | --- | 
| No open ports detected | Network Scanning creates an Informational finding that requires no action. | 
| Open ports detected on resource with Informational finding | Network Scanning closes the Informational finding by setting the activity\_name attribute to Close and creates a finding for each open port. | 
| Port first detected as reachable | Network Scanning creates and publishes a new finding. | 
| Port still reachable on rescan (no change) | Network Scanning periodically refreshes the finding. | 
| Port still reachable but evidence changed | Network Scanning republishes the finding with updated evidence. | 
| Port no longer reachable | Network Scanning keeps the finding open until the next rescan confirms that the port is unreachable. | 
| Connection endpoint port changed (RDS only) | Network Scanning re-scans the instance. A new finding is created if the new port is reachable. Network Scanning closes the finding for the old port by setting the activity\_name attribute to Close. | 
| Public access turned off (RDS only) | Network Scanning closes all findings for the instance by setting the activity\_name attribute to Close. | 
| Resource terminated or deleted | Network Scanning closes all findings for the resource by setting the activity\_name attribute to Close. | 
| IP address removed from resource | Network Scanning closes findings for that specific IP by setting the activity\_name attribute to Close. | 
| Network Scanning disabled | Network Scanning produces no new findings. Existing findings remain until they age out. | 
| Security Hub disabled | You no longer have access to findings. | 

 If a port is intermittently reachable, Network Scanning bases findings on positive evidence at scan time. After you fix an issue (for example, by closing a firewall rule or stopping a service), Network Scanning closes the finding on the next scan. 

 Disabling Network Scanning does not immediately close findings. Existing findings remain visible until they age out through the normal Security Hub finding lifecycle. 

**Note**  
 When you attach an Elastic IP address (EIP) to an Amazon EC2 instance, Network Scanning produces findings on the EIP resource. The EIP is the top-level IP resource that owns the address. For Network Load Balancer (NLB) resources, the DNS name and attached EIPs are distinct network entry points, so Network Scanning produces separate findings for each. 

## Scan evidence
<a name="network-scanning-evidence"></a>

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
<a name="network-scanning-exclude-resources"></a>

 To exclude a resource from Network Scanning, add an exclusion tag (AWS and Azure) or label (GCP) to the resource that has the scannable public IP. The key name and casing depend on the cloud provider. 

 When you add the exclusion tag or label, Network Scanning stops future scans and closes active findings for that resource. Removing the tag or label makes the resource eligible for scanning again. 

**AWS resources**

 Add the tag key `SecurityHubNetworkScanExclusion` to the resource. The tag value can be any value or empty. You must apply the tag to the actual resource with the scannable public IP: 
+ For an EIP attached to an EC2 instance – tag the EIP, not the EC2 instance. See [Tag your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html) for guidance on tagging an EIP.
+ For an EC2 instance with only a public IP (no EIP) – tag the EC2 instance. See [Tag your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html) for guidance on tagging an instance.
+ For a load balancer – tag the load balancer and any targets with individual public IPs. See [Tag a Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-tags.html) for guidance on tagging an NLB. See [Tag an Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-tags.html) for guidance on tagging an ALB.
+ For an RDS DB instance – tag the DB instance. See [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) for guidance on tagging a DB instance.

**Azure resources**

 Add the tag key `SecurityHubNetworkScanExclusion` to the Azure public IP address resource. The tag value can be any value or empty. For more information about tagging an Azure resource, see [Apply tags with Azure portal](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources-portal) on the Microsoft Learn website. 

**GCP resources**

 Add the label key `securityhubnetworkscanexclusion` to the resource. GCP requires label keys to be lowercase. You must apply the label key to the actual resource with the scannable public IP: 
+ For a VM instance with a public IP – add the label to the VM instance. See [Organize resources using labels](https://docs.cloud.google.com/compute/docs/labeling-resources) on the Google Cloud website.
+ For a Forwarding Rule – add the label to the Forwarding Rule and any VM instances with public IP addresses behind the load balancer. See [Organize resources using labels](https://docs.cloud.google.com/compute/docs/labeling-resources) on the Google Cloud website.

## Supported ports
<a name="network-scanning-supported-ports"></a>

 Network Scanning scans the following well-known TCP ports on eligible resources, except RDS DB instances. 

```
21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 1433, 3306, 3389, 5432,
5900, 6379, 8080, 8443, 9200, 27017
```

 For RDS DB instances, Network Scanning scans the port from the DB instance endpoint and the following engine-specific ports. Engines not listed are scanned on the endpoint port only. 


| Engine | Ports | 
| --- | --- | 
| MySQL | 11211, 33060 | 
| Amazon Aurora PostgreSQL | 1433 | 
| Oracle | 1158, 1522, 1535, 1830, 2057, 2484, 3306, 3872, 3873, 5433, 5500, 5533, 6141 | 
| SQL Server - Enterprise Edition, Standard Edition | 2383, 8443, 5000 | 
| SQL Server - Developer Edition, Express Edition, Web Edition | 5000 | 

## Multi-cloud support
<a name="network-scanning-multicloud"></a>

 With Network Scanning, you can scan resources in your Microsoft Azure and GCP environments. Scanning behavior, evidence, and findings for Azure and GCP resources are identical to AWS resources. Findings appear alongside AWS findings with appropriate cloud provider and region metadata. For supported resource types, see [Supported resource types](#network-scanning-supported-resources). 

 For more information about integrating with Microsoft Azure, see [Integrating Security Hub with Microsoft Azure](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-v2-azure.html). For more information about integrating with GCP, see [Integrating Security Hub with Google Cloud Platform](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-v2-gcp.html). 

## Disable Network Scanning
<a name="network-scanning-disable"></a>

 If your organization uses configuration policies, the delegated administrator can disable Network Scanning across specific accounts and Regions by editing the configuration policy. For more information about editing a configuration policy, see [Editing a configuration policy](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-v2-da-policy.html#securityhub-v2-configuration-edit). When editing the policy, select the Network Scanning capability, choose **Disable**, and then specify the accounts and Regions where you want to turn off scanning. 

For accounts that are not managed by a configuration policy, you can disable Network Scanning using one of the following methods.

------
#### [ Security Hub console ]

**To disable Network Scanning**

1. Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home).

1. In the navigation pane, choose **General settings**.

1. Locate the **Network Scanning** section.

1. Choose **Disable**.

1. Confirm that you want to disable Network Scanning.

------
#### [ Security Hub API ]

Invoke the `DisableSecurityHubFeatureV2` API with the feature name `NETWORK_SCANNING`.

------
#### [ AWS CLI ]

Run the following command to disable Network Scanning:

```
aws securityhub disable-security-hub-feature-v2 --feature-name NETWORK_SCANNING
```

------

 When you disable Network Scanning: 
+ Network Scanning does not trigger new scans.
+  Existing findings remain visible until they age out through the normal Security Hub finding lifecycle. 
+  Network Scanning completes any scans already in progress. 