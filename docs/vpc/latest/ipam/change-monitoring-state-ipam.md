# Change the monitoring state of VPC CIDRs

Follow the steps in this section to change the monitoring state of a VPC CIDR. You may want to change a VPC CIDR from monitored to ignored
if you do not want IPAM to manage or monitor the VPC and allow the CIDR allocated to the VPC to be available for use. You may want to change
a VPC CIDR from ignored to monitored if you want IPAM to manage and monitor the VPC CIDR.

###### Note

- You cannot ignore VPC CIDRs in the public scope.
- If a CIDR is ignored, you are still charged for the active IP addresses in the CIDR. For more information, see [Pricing for IPAM](pricing-ipam.md "pricing-ipam.md").
- If a CIDR is ignored, you can still view the history of IP addresses in the CIDR. For more information, see [View IP address history](view-history-cidr-ipam.md "view-history-cidr-ipam.md").
  You can change the monitoring state of a VPC CIDR to monitored or ignored:

- **Monitored**: The VPC CIDR has been detected by IPAM and is being monitored for overlap with other CIDRs and allocation rule compliance.
- **Ignored**: The VPC CIDR has been chosen to be exempt from monitoring.
  Ignored VPC CIDRs are not evaluated for overlap with other CIDRs or Allocation rule compliance. Once a VPC CIDR is chosen to be ignored,
  any space allocated to it from an IPAM pool is returned to the pool and the VPC CIDR will not be imported again via auto-import
  (if the auto-import Allocation rule is set on the pool).

AWS Management Console

###### To change the monitoring status of a CIDR allocated to a VPC

1. Open the IPAM console at
   [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/ "https://console.aws.amazon.com/ipam/").
2. In the navigation pane, choose **Resources**.
3. From the dropdown menu at the top of the content pane, choose the private scope you want to use.
4. In the content pane, choose the VPC and view the details of the VPC.
5. Under **VPC CIDRs**, select one of the CIDRs
   allocated to the VPC and choose **Actions** >
   **Mark as ignored** or **Unmark as
   ignored**.
6. Choose **Mark as ignored** or **Unmark as ignored**.

Command line
Use the following AWS CLI commands to change the monitoring state of a VPC CIDR:

1. Get a scope ID: [describe-ipam-scopes](../../../cli/latest/reference/ec2/describe-ipam-pools.md "../../../cli/latest/reference/ec2/describe-ipam-pools.md")
2. View the current monitoring state for the VPC CIDR: [get-ipam-resource-cidrs](../../../cli/latest/reference/ec2/get-ipam-resource-cidrs.md "../../../cli/latest/reference/ec2/get-ipam-resource-cidrs.md")
3. Change the state of the VPC CIDR: [modify-ipam-resource-cidr](../../../cli/latest/reference/ec2/modify-ipam-resource-cidr.md "../../../cli/latest/reference/ec2/modify-ipam-resource-cidr.md")
4. View the new monitoring state for the VPC CIDR: [get-ipam-resource-cidrs](../../../cli/latest/reference/ec2/get-ipam-resource-cidrs.md "../../../cli/latest/reference/ec2/get-ipam-resource-cidrs.md")
