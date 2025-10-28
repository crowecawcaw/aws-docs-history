# Monitor CIDR usage with the IPAM dashboard

The IPAM dashboard in Amazon VPC IP Address Manager allows you to monitor CIDR usage for several key scenarios:

- **Identify unused or underutilized IP address space**: The
  dashboard provides visibility into CIDR utilization, enabling you to identify CIDRs
  with available capacity that can be reclaimed or reallocated.
- **Optimize IP address management**: By closely tracking CIDR
  usage, you can make informed decisions about expanding, contracting, or reassigning
  IP address blocks to meet changing business and infrastructure requirements.
- **Prevent IP address exhaustion**: Monitoring CIDR usage helps
  you anticipate when you may need to acquire additional IP address space, allowing
  you to proactively plan and avoid service disruptions due to IP address depletion.
- **Ensure compliance and governance**: The IPAM dashboard can help
  you demonstrate IP address usage patterns to meet regulatory requirements or
  internal policies around IP address management.
- **Troubleshoot network issues**: Detailed CIDR usage data can
  assist in identifying the root causes of network connectivity problems or resource
  conflicts.
  By closely monitoring CIDR usage through the IPAM dashboard, you can enhance the efficiency, resilience, and compliance of your IP address management within AWS.

AWS Management Console

###### To monitor CIDR usage using the IPAM dashboard

1. Open the IPAM console at
   [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/ "https://console.aws.amazon.com/ipam/").
2. In the navigation pane, choose **Dashboard**.
3. By default, when you view the dashboard, the default private scope is
   selected. If you don’t want to use the default private scope, from the
   dropdown menu at the top of the content pane, choose the scope you want
   to use. For more information about scopes, see [How IPAM works](how-it-works-ipam.md "how-it-works-ipam.md").
4. The dashboard presents an overview of your IPAM pools and CIDRs within a scope. You can add, remove, resize, and move widgets to customize the dashboard.
   - **Scope**: The details for this
     scope. A scope is the highest-level container within IPAM.
     An IPAM contains two default scopes, one private and one public. Each scope represents the IP
     space for a single network. You may have multiple private scopes, but you can only have one public scope.
     - **Scope ID**: The ID for
       this scope.
     - **Scope type**: The type
       of scope.
     - **IPAM ID**: The ID of
       the IPAM that the scope is in.
     - **IPAM pools in this
       scope**: The ID of the IPAM that the scope
       is in.
     - **View networking resources in
       this scope**: Takes you to the **Resources** section
       of the IPAM console.
     - **Search the history of an IP
       address in this scope**: Takes you to the **Search
       IP history** section of the IPAM console.

   - **Resource CIDR types**: The
     types of resource CIDRs in the scope.
     - **Subnet**: The number of
       CIDRs for subnets.
     - **VPC**: The number of
       CIDRs for VPCs.
     - **EIPs**: The number of
       CIDRs for Elastic IP addresses.
     - **Public IPv4 pools**:
       The number of CIDRs for public IPv4 pools.

   - **Management state**: The
     management state of the CIDRs.
     - **Unmanaged CIDRs**: The number
       of resource CIDRs for unmanaged resources in this scope.
     - **Ignored CIDRs**: The number of
       resource CIDRs that you have chosen to be exempt from monitoring
       with IPAM in the scope. IPAM does not evaluate ignored resources
       for overlap or compliance within a scope. When a resource is
       chosen to be ignored, any space that's allocated to it from an
       IPAM pool is returned to the pool, and the resource will not be
       imported again through automatic import (if the automatic import
       allocation rule is set on the pool).
     - **Managed CIDRs**: The
       number of resource CIDRs for manageable resources (VPCs
       or public IPv4 pools) that are allocated from an IPAM
       pool in the scope.

   - **Overlapping resource CIDRs**:
     The number of overlapping and nonoverlapping CIDRs. Overlapping
     CIDRs can lead to incorrect routing in your VPCs.
     - **Overlapping CIDRs**:
       The number of CIDRs that currently overlap within the
       IPAM pools in this scope. Overlapping CIDRs can lead to
       incorrect routing in your VPCs.
     - **Nonoverlapping CIDRs**:
       The number of resource CIDRs that do not overlap within
       the IPAM pools in this scope.

   - **Compliant resource CIDRs**: The
     number of compliant resource CIDRs.
     - **Compliant CIDRs**: The number
       of resource CIDRs that comply with the allocation rules for IPAM
       pools in the scope.
     - **Noncompliant CIDRs**:
       The number of resource CIDRs that do not comply with the
       allocation rules for the IPAM pools in the scope.

   - **Overlap status**: The number of
     CIDRs that overlap over time.
     - **OverlappingResourceCidrs**: The number of
       CIDRs that overlap within the IPAM pools in this scope.
       Overlapping CIDRs can lead to incorrect routing in your
       VPCs.

   - **Compliance status**: The number
     of CIDRs that comply versus do not comply with the allocation
     rules for IPAM pools in the scope over time.
     - **CompliantResourceCidrs**: The number of
       resource CIDRs that comply with the allocation
       rules.
     - **NoncompliantResourceCidrs**: The number of
       resource CIDRs that do not comply with the allocation
       rules.

   - **VPC utilization**: VPCs (IPv4 and IPv6) with the highest or lowest IP utilization. You can use this information to configure Amazon CloudWatch alarms to be alerted if an IP utilization threshold is breached. For more information, see [IPAM resource utilization metrics](cloudwatch-ipam-res-util.md "cloudwatch-ipam-res-util.md").
   - **Subnet utilization**: Subnets (IPv4 only) with the highest or lowest IP utilization. You can use this information to decide if you want to keep or delete resources that are underutilized. For more information, see [IPAM resource utilization metrics](cloudwatch-ipam-res-util.md "cloudwatch-ipam-res-util.md").
   - **VPCs with highest IPs
     allocated**: The VPCs that have the highest
     percentage of IP address space allocated to subnets. This is
     useful to show you if you need to provision additional IP
     address space to the VPCs.
   - **Subnets with highest IPs
     allocated**: The subnets that have the highest
     percentage of IP address space allocated to resources. This is
     useful to show you if you need to provision additional IP
     address space to the subnets.
   - **Pool assignment**: The percentage of IP space that has been
     assigned to resources and manual allocations in the scope over
     time.
   - **Pool allocation**: The percentage of a pool's IP space that has
     been allocated to other pools in the scope over time.

Command line
The information displayed in the dashboard comes from metrics stored in Amazon
CloudWatch. For more information about the metrics stored in Amazon CloudWatch, see [Monitor IPAM with Amazon CloudWatch](cloudwatch-ipam.md "cloudwatch-ipam.md").
Use the Amazon CloudWatch options in the [AWS CLI Reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/index.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/index.html") to view metrics for allocations in your IPAM
pools and scopes.

If you find that the CIDR that's provisioned for a pool is almost fully allocated, you
might need to provision additional CIDRs. For more information, see [Provision CIDRs to a pool](prov-cidr-ipam.md "prov-cidr-ipam.md").
