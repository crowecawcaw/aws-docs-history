

# Remediating exposures for GCP Compute Engine instances

AWS Security Hub can generate exposure findings for GCP Compute Engine instances.

On the Security Hub console, the GCP Compute Engine instance involved in an exposure finding and its identifying information are listed in the **Resources** section of the finding details. Programmatically, you can retrieve resource details with the `GetFindingsV2` operation of the Security Hub CSPM API.

After identifying the resource involved in an exposure finding, you can delete the resource if you don't need it. Deleting a nonessential resource can reduce your exposure profile and AWS costs. If the resource is essential, follow these recommended remediation steps to help mitigate the risk. The remediation topics are divided based on the type of trait. 

A single exposure finding contains issues identified in multiple remediation topics. Conversely, you can address an exposure finding and bring down its severity level by addressing just one remediation topic. Your approach to risk remediation depends on your organizational requirements and workloads.

**Note**  
 The remediation guidance provided in this topic might require additional consultation in other Google Cloud resources. 

**Contents**
+ [Misconfiguration traits for GCP Compute Engine instances](#gcp-vm-misconfiguration)
  + [The role associated with the Compute Engine instance has an administrative access policy](#administrative-access-policy)
  + [The Compute Engine instance has an end-of-life operating system](#end-of-life-operating-system-detected)
  + [The Compute Engine instance has a public IP address](#public-ip-assigned)
  + [The Compute Engine instance has a security rule that allows SSH or RDP access](#remote-access-allowed)
+ [Reachability traits for GCP Compute Engine instances](#gcp-vm-reachability)
  + [The Compute Engine instance is reachable from the public internet](#internet-reachable)
+ [Vulnerability traits for GCP Compute Engine instances](#gcp-vm-vulnerability)
  + [The Compute Engine instance has network-exploitable software vulnerabilities with a high likelihood of exploitation](#high-priority-vulnerability)
  + [The Compute Engine instance has software vulnerabilities](#low-priority-vulnerability)
  + [The Compute Engine instance has malicious software packages](#malicious-package)

## Misconfiguration traits for GCP Compute Engine instances
<a name="gcp-vm-misconfiguration"></a>

Here are misconfiguration traits for GCP Compute Engine instances and suggested remediation steps.

### The role associated with the Compute Engine instance has an administrative access policy
<a name="administrative-access-policy"></a><a name="service-admin-policy"></a>

 The instance uses the Compute Engine default service account with the `cloud-platform` access scope, so the service account's Identity and Access Management (IAM) roles control what the instance can access. Depending on your organization policies, the default service account might have the Editor role (`roles/editor`) on the project, and anyone who can run code on the instance can use that access. Following standard security principles, attach a dedicated service account that has only the roles that your workload needs. 

**Remediation: Attach a dedicated service account**  
 Create a user-managed service account with only the roles that your workload needs, and attach it to the instance instead of the default service account. You must stop the instance to change its service account. For a managed instance group, update the group's instance template instead. For more information, see [Service accounts for instances](https://docs.cloud.google.com/compute/docs/access/service-accounts) and [Change the attached service account](https://docs.cloud.google.com/compute/docs/instances/change-service-account) on the Google Cloud website. 

### The Compute Engine instance has an end-of-life operating system
<a name="end-of-life-operating-system-detected"></a>

 The instance runs an operating system version that has reached end of life. When an operating system reaches end of life, its vendor stops releasing security updates for it. Known vulnerabilities then stay unpatched and leave the instance open to attack. Following security best practices, run a supported operating system version on your Compute Engine instances. 

**Remediation: Migrate to a supported operating system version**  
 Create a new instance from a supported operating system image, migrate the workload to it, and then retire the old instance. An in-place upgrade is riskier, so if you upgrade in place, create snapshots of the disks first. For more information about end-of-support dates, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details) on the Google Cloud website. 

### The Compute Engine instance has a public IP address
<a name="public-ip-assigned"></a>

 The instance has an external IP address, so it can receive connections from the internet that its firewall rules allow. A firewall rule with a broad source range, such as `0.0.0.0/0`, then exposes the instance's services to anyone on the internet. Following standard security principles, assign external IP addresses only to instances that need them. 

**Remediation: Remove the external IP address**  
 Remove the external IP address from each network interface that has one. Inbound services that use it stop working, and you can't recover an ephemeral address. Use Public NAT in Cloud NAT for outbound access and Identity-Aware Proxy (IAP) TCP forwarding for administration. For more information, see [Configure static external IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address), [Cloud NAT overview](https://docs.cloud.google.com/nat/docs/overview), and [Use IAP for TCP forwarding](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding) on the Google Cloud website. 

### The Compute Engine instance has a security rule that allows SSH or RDP access
<a name="remote-access-allowed"></a>

 Administrators use Secure Shell (SSH) on port 22 and Remote Desktop Protocol (RDP) on port 3389 to manage instances remotely. A Virtual Private Cloud (VPC) firewall rule in the instance's network allows connections to these ports from any IPv4 address (`0.0.0.0/0`). If the instance has an external IP address, anyone on the internet can attempt brute-force and credential-based attacks on these ports. Following standard security principles, limit SSH and RDP access to trusted sources. 

**Remediation**  
Take one or more of the following actions to address this exposure:

**Restrict the rule's source ranges**  
 Replace `0.0.0.0/0` in the rule's source ranges with the address ranges of trusted administrator networks. In the default network, these rules are often `default-allow-ssh` and `default-allow-rdp`. The change affects every instance that the rule applies to, and other rules in the network can also allow these ports. For more information, see [VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls) on the Google Cloud website. 

**Use IAP TCP forwarding for SSH and RDP**  
 Connect over SSH or RDP through IAP TCP forwarding instead of directly from the internet, and replace `0.0.0.0/0` in the rule's source ranges with the IAP range, `35.235.240.0/20`. For more information, see [Use IAP for TCP forwarding](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding) on the Google Cloud website. 

## Reachability traits for GCP Compute Engine instances
<a name="gcp-vm-reachability"></a>

Here are reachability traits for GCP Compute Engine instances and suggested remediation steps.

### The Compute Engine instance is reachable from the public internet
<a name="internet-reachable"></a><a name="potentially-internet-reachable"></a>

 A network scan from the internet found open ports on the instance's external IP address. Anyone on the internet can send traffic to the services that listen on them. This section also covers the trait for instances that might be reachable from the public internet, which means that a network interface has an external IPv4 or IPv6 address. Following standard security principles, limit inbound traffic to the sources and ports that your workload needs. 

**Remediation**  
Take one or more of the following actions to address this exposure:

**Remove the external IP address**  
 Remove every external IPv4 and IPv6 address from the instance's network interfaces. This action addresses both traits. Use Public NAT in Cloud NAT for outbound access and IAP TCP forwarding for administration. For more information, see [Configure static external IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address) and [Cloud NAT overview](https://docs.cloud.google.com/nat/docs/overview) on the Google Cloud website. 

**Tighten VPC firewall rules**  
 Narrow the source ranges of the VPC firewall rules that allow traffic from `0.0.0.0/0` to the open ports, or narrow their targets to exclude the instance. Serve services that must stay public through a load balancer instead. Because the instance keeps its external IP address, this action doesn't address the trait for instances that might be reachable. For more information, see [VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls) on the Google Cloud website. 

## Vulnerability traits for GCP Compute Engine instances
<a name="gcp-vm-vulnerability"></a>

Here are vulnerability traits for GCP Compute Engine instances and suggested remediation steps.

### The Compute Engine instance has network-exploitable software vulnerabilities with a high likelihood of exploitation
<a name="high-priority-vulnerability"></a>

 Common Vulnerabilities and Exposures (CVEs) can affect software packages installed on Compute Engine instances. A high-priority vulnerability is network-exploitable with a high likelihood of exploitation. Such a vulnerability is an immediate security threat because public exploit code might already exist and attackers might be using it. Patch these vulnerabilities promptly to protect your instance. 

**Remediation**  
Take one or more of the following actions to address this exposure:

**Apply operating system and package updates**  
 Review the affected CVEs in the finding, and then apply operating system and package updates to the instance. You can use VM Manager Patch, which requires the OS Config agent. For instances in a managed instance group, update the instance template to a patched image, and then replace the instances. For more information, see [VM Manager Patch](https://docs.cloud.google.com/compute/vm-manager/docs/patch) on the Google Cloud website. 

**Future considerations**  
 To prevent future occurrences, schedule recurring patch deployments with VM Manager Patch so that your instances receive operating system patches regularly. For more information, see [VM Manager Patch](https://docs.cloud.google.com/compute/vm-manager/docs/patch) on the Google Cloud website. 

### The Compute Engine instance has software vulnerabilities
<a name="low-priority-vulnerability"></a>

 Common Vulnerabilities and Exposures (CVEs) can affect software packages installed on Compute Engine instances. Noncritical vulnerabilities are security weaknesses with lower severity or exploitability than high-priority vulnerabilities. They pose less immediate risk, but attackers can still exploit them to compromise the confidentiality, integrity, or availability of data, or to access other systems. Following security best practices, patch these vulnerabilities to protect your instance. 

**Remediation: Apply operating system and package updates**  
 Review the affected CVEs in the finding, and then apply operating system and package updates to the instance. You can use VM Manager Patch, which requires the OS Config agent. For instances in a managed instance group, update the instance template to a patched image, and then replace the instances. For more information, see [VM Manager Patch](https://docs.cloud.google.com/compute/vm-manager/docs/patch) on the Google Cloud website. 

### The Compute Engine instance has malicious software packages
<a name="malicious-package"></a>

 Malicious packages are software components that contain harmful code designed to compromise the confidentiality, integrity, and availability of your systems and data. Code from these packages can run on the instance with the permissions of the instance's service account. Following security best practices, remove malicious packages to protect your instance from potential attacks. 

**Remediation: Investigate and remove malicious packages**  
 Review the finding to identify the malicious packages, remove them from the instance, and then make sure that a later scan no longer reports them. Treat credentials on the instance as compromised. Rotate secrets that the instance can access, and review the activity of the instance's service account. 