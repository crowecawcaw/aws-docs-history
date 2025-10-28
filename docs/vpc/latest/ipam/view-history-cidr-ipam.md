# View IP address history

Follow the steps in this section to view the history of an IP address or CIDR in an IPAM
scope. You can
use the historical data to analyze and audit your network security and routing
policies. IPAM automatically retains IP address monitoring data for up to three years.

You can use the IP historical data to search for the status change of IP addresses or
CIDRs for the following types of resources:

- VPCs
- VPC subnets
- Elastic IP addresses
- EC2 instances
- EC2 network interfaces attached to instances

###### Important

Although IPAM doesn't monitor Amazon EC2 instances or EC2 network interfaces that are attached to
instances, you can use the Search IP history feature to search for historical data on
EC2 instance and network interface CIDRs.

###### Note

- If you move a resource from one IPAM scope to another,
  the previous history record ends and a new history record is created under the new scope. For more information, see [Move VPC CIDRs between scopes](move-resource-ipam.md "move-resource-ipam.md").
- If you delete or transfer a resource to an AWS account that's not monitored by your IPAM, any new history related to the resource will not be visible and your IPAM won't monitor the resource. The IP address of the resource, however, will still be searchable.
- If you [Integrate IPAM with accounts outside of your organization](enable-integ-ipam-outside-org.md "enable-integ-ipam-outside-org.md"), the IPAM owner can view the IP address history of all resource CIDRs owned by those accounts.

AWS Management Console

###### To view the history of a CIDR

1. Open the IPAM console at
   [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/ "https://console.aws.amazon.com/ipam/").
2. In the navigation pane, choose **Search IP
   history**.
3. Enter an IPv4 or IPv6 IP address or CIDR. This must be a specific CIDR
   for the resource.
4. Choose an IPAM scope ID.
5. Choose a date/time range.
6. If you want to filter the results by VPC, enter a VPC ID. Use this option if the CIDR appears
   in multiple VPCs.
7. Choose **Search**.

Command line
The commands in this section link to the _AWS CLI Command Reference_.
The documentation provides detailed descriptions of the options that you can use
when you run the commands.

- View the history of a CIDR: [get-ipam-address-history](../../../cli/latest/reference/ec2/get-ipam-address-history.md "../../../cli/latest/reference/ec2/get-ipam-address-history.md")

To see examples of how you can use the AWS CLI to analyze and audit IP address usage, see [Tutorial: View IP address history using the AWS CLI](tutorials-historical-insights.md "tutorials-historical-insights.md").

The results of the search are organized into the following columns:

- **Sampled end time**: Sampled end time of the resource-to-CIDR
  association within the IPAM scope. Changes are picked up in periodic snapshots, so
  the end time might have occurred before this specific time.
- **Sampled start time**: Sampled start time of the
  resource-to-CIDR association within the IPAM scope. Changes are picked up in
  periodic snapshots, so the start time might have occurred before this specific
  time.

To help explain the times that you see under Sampled start time and Sampled end time, let’s look at an example use case:

At 2:00 PM, a VPC was created with CIDR 10.0.0.0/16. At 3:00 PM, you create an
IPAM and IPAM pool with CIDR 10.0.0.0/8, and select the auto-import option to
allow IPAM to discover and import any CIDRs that fall within the 10.0.0.0/8 IP
address range. Because IPAM picks up changes to CIDRs in periodic snapshots, it
doesn’t discover the existing VPC CIDR until 3:05 PM. When you search for the ID
of this VPC using the Search IP history feature, the Sampled start time for your
VPC is 3:05 PM, which is when IPAM discovered it, not 2:00 PM, which is when you
created the VPC. Now, let’s say that you decide to delete the VPC at 5:00 PM.
When the VPC is deleted, the CIDR 10.0.0.0/16 that was allocated to the VPC is
recycled back into the IPAM pool. IPAM takes its periodic snapshot at 5:05 PM
and picks up the change. When you search for the ID of this VPC in Search IP
history, 5:05 PM is the Sampled end time for the VPC’s CIDR, not 5:00 PM, which
is when the VPC was deleted.

- **Resource ID**: The ID generated when the resource was
  associated with the CIDR.
- **Name:** The name of the resource (if applicable).
- **Compliance status**: The
  compliance status of the CIDR.
  - **Compliant**: A managed
    resource complies with the allocation rules of the IPAM
    pool.
  - **Noncompliant**: The
    resource CIDR does not comply with one or more of the
    allocation rules of the IPAM pool.

  If a VPC has a CIDR that does not meet the netmask
  length parameters of the IPAM pool, or if the
  resource is not in the same AWS Region as the IPAM
  pool, it will be flagged as noncompliant.
  - **Unmanaged**: The
    resource does not have a CIDR allocated from an IPAM
    pool and is not being monitored by IPAM for potential
    CIDR compliance with pool allocation rules. The CIDR is
    monitored for overlap.
  - **Ignored**: The managed
    resource has been chosen to be exempt from monitoring.
    Ignored resources are not evaluated for overlap or
    allocation rule compliance. When a resource is chosen to
    be ignored, any space allocated to it from an IPAM pool
    is returned to the pool and the resource will not be
    imported again through automatic import (if the
    automatic import allocation rule is set on the
    pool).
  - **-**: This resource is
    not one of the types of resources that IPAM can monitor
    or manage.

- **Overlap status**: The overlap
  status of CIDR.
  - **Nonoverlapping**: The
    resource CIDR does not overlap with another CIDR in the
    same scope.
  - **Overlapping**: The
    resource CIDR overlaps with another CIDR in the same
    scope. Note that if a resource CIDR is overlapping, it
    could be overlapping with a manual allocation.
  - **Ignored**: The managed
    resource has been chosen to be exempt from monitoring.
    IPAM does not evaluate ignored resources for overlap or
    allocation rule compliance. When a resource is chosen to
    be ignored, any space allocated to it from an IPAM pool
    is returned to the pool and the resource will not be
    imported again through automatic import (if the
    automatic import allocation rule is set on the
    pool).
  - **-**: This resource is not one of the types of resources that
    IPAM can monitor or manage.

- **Resource type**
  - **vpc**: The CIDR is associated with a
    VPC.
  - **subnet**: The CIDR is associated with a VPC
    subnet.
  - **eip**: The CIDR is associated with an
    Elastic IP address.
  - **instance**: The CIDR is associated with an
    EC2 instance.
  - **network-interface**: The CIDR is associated
    with a network interface.

- **VPC ID**: The ID of the VPC that this resource
  belongs to (if applicable).
- **Region**: The AWS Region of this resource.
- **Owner ID**: The AWS account ID of the user that
  created this resource (if applicable).
