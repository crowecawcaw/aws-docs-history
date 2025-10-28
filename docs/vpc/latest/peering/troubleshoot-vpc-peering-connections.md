# Troubleshoot a VPC peering connection

If you're having trouble connecting to a resource in a VPC from a resource in a
peer VPC, do the following:

- For each resource in each VPC, verify that the route table for its subnet contains a route that sends traffic destined for the peer VPC to the VPC peering connection. This ensures network traffic can properly flow between the two VPCs. For more information, see [Update route tables](vpc-peering-routing.md "vpc-peering-routing.md").
- For any EC2 instances involved, verify that the security groups for those instances allow inbound and outbound traffic from the peer VPC. Security group rules control which traffic is permitted to access your EC2 instances. For more information, see [Reference peer security groups](vpc-peering-security-groups.md "vpc-peering-security-groups.md").
- Check that the network ACLs for the subnets containing your resources allow the necessary traffic from the peer VPC. Network ACLs are an additional layer of security that filter traffic at the subnet level.
  If you're still having issues, you can leverage Reachability Analyzer. Reachability Analyzer can help identify the specific component - whether a route table, security group, or network ACL - that is causing the connectivity problem between the two VPCs. For more information, see the [Reachability Analyzer Guide](../reachability.md "../reachability.md").

Thoroughly verifying your VPC networking configurations is key to troubleshooting and resolving any VPC peering connection issues you may encounter.
