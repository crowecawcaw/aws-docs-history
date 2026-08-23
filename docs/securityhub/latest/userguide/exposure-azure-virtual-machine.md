# Remediating exposures for Azure virtual machines

AWS Security Hub can generate exposure findings for Azure virtual machines.

On the Security Hub console, the Azure virtual machine involved in an exposure finding and its identifying information are listed in
the **Resources** section of the finding details. Programmatically, you can retrieve resource
details with the [GetFindingsV2](../../1.0/APIReference/API_GetFindingsV2.md "../../1.0/APIReference/API_GetFindingsV2.md") operation of the Security Hub CSPM API.

After identifying the resource involved in an exposure finding, you can delete the resource if you don't need it.
Deleting a nonessential resource can reduce your exposure profile and AWS costs. If the resource is essential,
follow these recommended remediation steps to help mitigate the risk. The remediation topics are
divided based on the type of trait.

A single exposure finding contains issues identified in multiple remediation topics. Conversely, you can address an exposure finding and bring down
its severity level by addressing just one remediation topic. Your approach to risk remediation
depends on your organizational requirements and workloads.

###### Note

The remediation guidance provided in this topic might require additional consultation in other Microsoft Azure resources.

###### Contents

- [Misconfiguration traits for Azure virtual machines](exposure-azure-virtual-machine.md#azure-vm-misconfiguration "exposure-azure-virtual-machine.md#azure-vm-misconfiguration")

  - [The Azure virtual machine has an open network security group](exposure-azure-virtual-machine.md#open-security-group "exposure-azure-virtual-machine.md#open-security-group")
  - [The Azure virtual machine has a security rule that allows SSH or RDP access](exposure-azure-virtual-machine.md#remote-access-allowed "exposure-azure-virtual-machine.md#remote-access-allowed")
  - [The role associated with the Azure virtual machine has an administrative access role assignment](exposure-azure-virtual-machine.md#administrative-access-policy "exposure-azure-virtual-machine.md#administrative-access-policy")
  - [The Azure virtual machine has an end-of-life operating system](exposure-azure-virtual-machine.md#end-of-life-operating-system-detected "exposure-azure-virtual-machine.md#end-of-life-operating-system-detected")

- [Reachability traits for Azure virtual machines](exposure-azure-virtual-machine.md#azure-vm-reachability "exposure-azure-virtual-machine.md#azure-vm-reachability")

  - [The Azure virtual machine is reachable over the internet](exposure-azure-virtual-machine.md#internet-reachable "exposure-azure-virtual-machine.md#internet-reachable")

- [Vulnerability traits for Azure virtual machines](exposure-azure-virtual-machine.md#vulnerability "exposure-azure-virtual-machine.md#vulnerability")

  - [The Azure virtual machine has network-exploitable software vulnerabilities with a high likelihood of exploitation](exposure-azure-virtual-machine.md#high-priority-vulnerability "exposure-azure-virtual-machine.md#high-priority-vulnerability")
  - [The Azure virtual machine has software vulnerabilities](exposure-azure-virtual-machine.md#low-priority-vulnerability "exposure-azure-virtual-machine.md#low-priority-vulnerability")
  - [The Azure virtual machine has malicious software packages](exposure-azure-virtual-machine.md#malicious-package "exposure-azure-virtual-machine.md#malicious-package")

## Misconfiguration traits for Azure virtual machines

Here are misconfiguration traits for Azure virtual machines and suggested remediation steps.

### The Azure virtual machine has an open network security group

A network security group (NSG) acts as a virtual firewall for your Azure virtual machine, filtering inbound and outbound traffic with a set of prioritized security rules.
An open network security group contains rules that allow unrestricted access from any source (for example, a source of `Any` or `0.0.0.0/0`). These rules can expose your virtual machine to unauthorized access from the internet.
Following standard security principles, restrict network security group rules to only the specific IP addresses, ports, and protocols that your workload requires.

###### Remediation

Take one or more of the following actions to address this exposure:

###### Review network security group rules and assess current configuration

Identify the network security group associated with the virtual machine's network interface or subnet, and review its inbound security rules.
Evaluate which ports allow traffic from broad source ranges, such as `Any` or `0.0.0.0/0`.
Rules are processed in priority order, so confirm that a permissive rule is not taking precedence over a more restrictive one. For more information, see [Network security groups](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview "https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview") in the Microsoft Azure documentation.

###### Restrict network security group rules

Modify or remove rules that allow unrestricted access. Replace a broad source such as `Any` with the specific trusted IP addresses, CIDR ranges, service tags, or application security groups that require access. Limit the destination port range to only the ports your workload uses. For more information, see [Manage network security groups](https://learn.microsoft.com/en-us/azure/virtual-network/manage-network-security-group "https://learn.microsoft.com/en-us/azure/virtual-network/manage-network-security-group") in the Microsoft Azure documentation.

### The Azure virtual machine has a security rule that allows SSH or RDP access

Remote management protocols such as SSH (port 22) and RDP (port 3389) let users connect to and manage Azure virtual machines from remote locations.
When a network security group rule permits these ports from the internet (a source of `Any` or `0.0.0.0/0`), your virtual machine's attack surface increases significantly and it becomes exposed to brute-force and credential-based attacks.
Following standard security principles, limit remote access to specific, trusted IP addresses, or remove direct internet access to these ports entirely.

###### Remediation

Take one or more of the following actions to address this exposure:

###### Restrict the network security group rule

Limit SSH and RDP access to specific trusted IP addresses or CIDR ranges instead of `Any`, or remove the inbound rule if remote access from the internet is not required. For more information, see [Manage network security groups](https://learn.microsoft.com/en-us/azure/virtual-network/manage-network-security-group "https://learn.microsoft.com/en-us/azure/virtual-network/manage-network-security-group") in the Microsoft Azure documentation.

###### Use Azure Bastion for secure connectivity

Instead of exposing SSH or RDP ports to the internet, use Azure Bastion to connect to your virtual machine over TLS without a public IP address or open inbound ports. For more information, see [Azure Bastion](https://learn.microsoft.com/en-us/azure/bastion/bastion-overview "https://learn.microsoft.com/en-us/azure/bastion/bastion-overview") in the Microsoft Azure documentation.

###### Use just-in-time virtual machine access

Enable just-in-time (JIT) virtual machine access in Microsoft Defender for Cloud so that management ports such as SSH and RDP stay closed by default and open only for approved, time-bound requests from a specified source IP address. For more information, see [Enable just-in-time access](https://learn.microsoft.com/en-us/azure/defender-for-cloud/enable-just-in-time-access "https://learn.microsoft.com/en-us/azure/defender-for-cloud/enable-just-in-time-access") in the Microsoft Azure documentation.

### The role associated with the Azure virtual machine has an administrative access role assignment

You can assign a managed identity to an Azure virtual machine and grant it Azure role-based access control (Azure RBAC) role assignments to access other Azure resources.
When the associated identity has an administrative role assignment (such as `Owner` or `Contributor`) at a broad scope, it typically grants permissions far beyond what the workload requires.
If the virtual machine is compromised, an attacker can use these excessive permissions to move laterally across your environment, access data, or manipulate resources.
Following standard security principles, grant least privilege by assigning only the permissions the workload needs.

###### Remediation

Take one or more of the following actions to address this exposure:

###### Review and identify administrative role assignments

In the Azure portal, review the role assignments for the identity associated with the virtual machine. Look for privileged administrator roles such as `Owner`, `Contributor`, or `User Access Administrator`, and for custom roles that use a wildcard (`*`) in their `Actions`. For more information, see [List Azure role assignments](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-list-portal "https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-list-portal") in the Microsoft Azure documentation.

###### Implement least privilege access

Replace administrative role assignments with the least-privileged built-in role that grants only the permissions the workload requires. Assign it at the narrowest scope (resource or resource group) that meets your needs. When creating custom roles, specify `Actions` and `DataActions` explicitly instead of using a wildcard. For more information, see [Best practices for Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices "https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices") in the Microsoft Azure documentation.

### The Azure virtual machine has an end-of-life operating system

The Azure virtual machine runs an end-of-life operating system that is no longer supported or maintained by its vendor.
When an operating system reaches end of life, the vendor stops releasing security updates and advisories, which leaves known vulnerabilities permanently unpatched and exposes the virtual machine to attack.
Following security best practices, upgrade to a supported operating system version.

###### Remediation: Upgrade to a supported operating system version

Plan an in-place upgrade or migrate the workload to a virtual machine running a supported operating system version. Before upgrading, confirm application compatibility and take a backup or snapshot so that you can roll back if needed. For Windows, follow the in-place upgrade guidance; for Linux, follow the upgrade guidance from your distribution vendor. For more information, see [Perform an in-place upgrade of a Windows Server VM](https://learn.microsoft.com/en-us/azure/virtual-machines/windows/upgrade-windows-server "https://learn.microsoft.com/en-us/azure/virtual-machines/windows/upgrade-windows-server") in the Microsoft Azure documentation.

## Reachability traits for Azure virtual machines

Here are reachability traits for Azure virtual machines and suggested remediation steps.

### The Azure virtual machine is reachable over the internet

An Azure virtual machine with ports that are reachable from the internet might be exposed to attack. A virtual machine becomes reachable when it has a public IP address. It can also become reachable when a load balancer, application gateway, or other network path permits inbound traffic from the internet.
Following standard security principles, implement least-privilege network access controls by restricting inbound traffic to only necessary sources and ports.

###### Remediation

Take one or more of the following actions to address this exposure:

###### Restrict or remove internet exposure

Review whether the virtual machine requires a public IP address. If it does not, disassociate the public IP address from the network interface and use a private IP address instead. If outbound internet connectivity is still required, use a NAT gateway.

If inbound access is required, place the virtual machine behind a load balancer, Azure Firewall, or application gateway rather than exposing it directly. For more information, see [Public IP addresses](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/public-ip-addresses "https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/public-ip-addresses") in the Microsoft Azure documentation.

###### Tighten inbound network security group rules

Modify or remove inbound network security group rules that allow unrestricted access (`Any` or `0.0.0.0/0`), and restrict access to the specific source ranges, ports, and protocols your workload requires. For more information, see [Network security groups](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview "https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview") in the Microsoft Azure documentation.

###### Use Azure Bastion for management access

For management connectivity, use Azure Bastion to reach the virtual machine over TLS without a public IP address or open SSH/RDP ports. For more information, see [Azure Bastion](https://learn.microsoft.com/en-us/azure/bastion/bastion-overview "https://learn.microsoft.com/en-us/azure/bastion/bastion-overview") in the Microsoft Azure documentation.

## Vulnerability traits for Azure virtual machines

Here are vulnerability traits for Azure virtual machines and suggested remediation steps.

### The Azure virtual machine has network-exploitable software vulnerabilities with a high likelihood of exploitation

Common Vulnerabilities and Exposures (CVEs) can affect software packages installed on Azure virtual machines.
A high-priority vulnerability is network-exploitable with a high likelihood of exploitation. This represents an immediate security threat because exploit code might already be publicly available and actively used by attackers or automated scanning tools.
Patch these vulnerabilities promptly to protect your virtual machine.

###### Remediation

Take one or more of the following actions to address this exposure:

###### Review and remediate the finding

Use Microsoft Defender for Cloud vulnerability assessment to review the affected CVEs and the remediation steps for the virtual machine. The details pane for each finding includes the relevant CVEs and recommended remediation. For more information, see [Remediate machine vulnerabilities](https://learn.microsoft.com/en-us/azure/defender-for-cloud/remediate-vulnerability-findings-vm "https://learn.microsoft.com/en-us/azure/defender-for-cloud/remediate-vulnerability-findings-vm") in the Microsoft Azure documentation.

###### Apply updates

Use Azure Update Manager to assess and deploy operating system and software updates across your virtual machines on a schedule. If an update is not available, consider removing or disabling the vulnerable software, or restricting network access to it, until a patch is released. For more information, see [Azure Update Manager](https://learn.microsoft.com/en-us/azure/update-manager/overview "https://learn.microsoft.com/en-us/azure/update-manager/overview") in the Microsoft Azure documentation.

###### Future considerations

To prevent future occurrences, enable Microsoft Defender for Servers to continuously scan your virtual machines for vulnerabilities, and establish a regular patching schedule with Azure Update Manager. For more information, see [Microsoft Defender for Servers](https://learn.microsoft.com/en-us/azure/defender-for-cloud/plan-defender-for-servers "https://learn.microsoft.com/en-us/azure/defender-for-cloud/plan-defender-for-servers") in the Microsoft Azure documentation.

### The Azure virtual machine has software vulnerabilities

Common Vulnerabilities and Exposures (CVEs) can affect software packages installed on Azure virtual machines.
Noncritical vulnerabilities represent security weaknesses with lower severity or exploitability than high-priority vulnerabilities. Although they pose less immediate risk, attackers can still exploit unpatched vulnerabilities to compromise the confidentiality, integrity, or availability of data, or to access other systems.
Following security best practices, patch these vulnerabilities to protect your virtual machine from attack.

###### Remediation

Take one or more of the following actions to address this exposure:

###### Review and remediate the finding

Use Microsoft Defender for Cloud vulnerability assessment to review the affected CVEs and follow the remediation steps in the finding details pane. For more information, see [Remediate machine vulnerabilities](https://learn.microsoft.com/en-us/azure/defender-for-cloud/remediate-vulnerability-findings-vm "https://learn.microsoft.com/en-us/azure/defender-for-cloud/remediate-vulnerability-findings-vm") in the Microsoft Azure documentation.

###### Apply updates

Use Azure Update Manager to assess and deploy operating system and software updates across your virtual machines. To manage updates consistently at scale, configure scheduled patching. For more information, see [Azure Update Manager](https://learn.microsoft.com/en-us/azure/update-manager/overview "https://learn.microsoft.com/en-us/azure/update-manager/overview") in the Microsoft Azure documentation.

### The Azure virtual machine has malicious software packages

Malicious packages are software components that contain harmful code designed to compromise the confidentiality, integrity, and availability of your systems and data.
Malicious packages pose an active and critical threat to your virtual machine, because attackers can execute the malicious code automatically without exploiting a separate vulnerability.
Following security best practices, remove malicious packages to protect your virtual machine from potential attacks.

###### Remediation: Investigate and remove malicious packages

Review the finding details to understand the threat and identify the affected packages, then remove the identified packages using the appropriate package manager for the operating system. After removal, run a scan to confirm that no related malicious components remain. For more information, see [Microsoft Defender for Servers](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-servers-introduction "https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-servers-introduction") in the Microsoft Azure documentation.
