

# Connecting to a VPC in another account
<a name="workflows-vpc-cross-account"></a>

You can give your HealthOmics workflow runs access to resources in an Amazon VPC managed by another AWS account, without exposing either VPC to the internet. This access pattern allows you to share data with other organizations using AWS. Using this access pattern, you can share data between VPCs with a greater level of security and performance than over the internet. Configure your workflow runs to use a VPC peering connection to access these resources.

**Warning**  
When you allow access between accounts or VPCs, check that your plan meets the security requirements of the respective organizations that manage these accounts. Following the instructions in this document will affect the security posture of your resources.

In this tutorial, you connect two accounts together with a peering connection using IPv4. You configure a HealthOmics configuration resource that is not already connected to a VPC in another account. You configure DNS resolution to connect your workflow runs to resources that do not provide static IPs. To adapt these instructions to other peering scenarios, consult the [VPC Peering Guide](https://docs.aws.amazon.com/vpc/latest/peering/).

## Prerequisites
<a name="vpc-cross-account-prerequisites"></a>

To give a HealthOmics workflow run access to a resource in another account, you must have:
+ A HealthOmics workflow configured to authenticate with and then read from your resource.
+ A resource in another account, such as an Amazon RDS cluster or license server, available through Amazon VPC.
+ Credentials for your workflow's account and your resource's account. If you are not authorized to use your resource's account, contact an authorized user to prepare that account.
+ Permission to create and update a VPC (and supporting Amazon VPC resources) to associate with your HealthOmics workflow runs.
+ Permission to create HealthOmics configuration resources.
+ Permission to create a VPC peering connection in your workflow's account.
+ Permission to accept a VPC peering connection in your resource's account.
+ Permission to update the configuration of your resource's VPC (and supporting Amazon VPC resources).
+ Permission to start HealthOmics workflow runs.

## Create an Amazon VPC in your workflow's account
<a name="vpc-cross-account-create-vpc"></a>

Create an Amazon VPC, subnets, route tables, and a security group in your HealthOmics workflow's account.

**To create a VPC, subnets, and other VPC resources using the console**

1. Open the Amazon VPC Console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the dashboard, choose **Create VPC**.

1. For **IPv4 CIDR block**, provide a private CIDR block. Your CIDR block must not overlap with blocks used in your resource's VPC. Don't pick a block your resource's VPC uses to assign IPs to resources or a block already defined in the route tables in your resource's VPC. For more information about defining appropriate CIDR blocks, see [VPC CIDR blocks](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-cidr-blocks.html).

1. Choose **Customize AZs**.

1. Select at least one Availability Zone where HealthOmics operates in your Region.

1. For **Number of public subnets**, choose **0**.

1. For **VPC endpoints**, choose **None** (you can add these later for cost optimization).

1. Choose **Create VPC**.

## Create a VPC peering connection request
<a name="vpc-cross-account-create-peering"></a>

Create a VPC peering connection request from your workflow's VPC (the requester VPC) to your resource's VPC (the accepter VPC).

**To request a VPC peering connection from your workflow's VPC**

1. Open the [Amazon VPC Console](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Peering connections**.

1. Choose **Create peering connection**.

1. For **VPC ID (Requester)**, select your workflow's VPC.

1. For **Account ID**, enter the ID of your resource's account.

1. For **VPC ID (Accepter)**, enter your resource's VPC ID.

1. Choose **Create peering connection**.

## Prepare your resource's account
<a name="vpc-cross-account-prepare-resource"></a>

To create your peering connection and prepare your resource's VPC to use the connection, log in to your resource's account with a role that holds the permissions listed in the prerequisites. The steps to log in may be different based on how the account is secured. For more information about how to sign in to an AWS account, see the [AWS Sign-in User Guide](https://docs.aws.amazon.com/signin/latest/userguide/what-is-sign-in.html). In your resource's account, perform the following procedures.

**To accept the VPC peering connection request**

1. Open the [Amazon VPC Console](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Peering connections**.

1. Select the pending VPC peering connection (the status is pending-acceptance).

1. Choose **Actions**.

1. From the dropdown list, choose **Accept request**.

1. When prompted for confirmation, choose **Accept request**.

1. Choose **Modify my route tables now** to add a route to the main route table for your VPC so that you can send and receive traffic across the peering connection.

Inspect the route tables for the resource's VPC. The route generated by Amazon VPC might not establish connectivity, based on how your resource's VPC is set up. Check for conflicts between the new route and existing configuration for the VPC. For more information about troubleshooting, see [Troubleshoot a VPC peering connection](https://docs.aws.amazon.com/vpc/latest/peering/troubleshoot-vpc-peering-connections.html) in the *Amazon VPC Peering Guide*.

**To update the route table for your resource's VPC**

1. Open the [Amazon VPC Console](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Route tables**.

1. Select the check box next to the name of the route table for the subnet associated with your resource.

1. Choose **Actions**.

1. Choose **Edit routes**.

1. Choose **Add route**.

1. For **Destination**, enter the CIDR block for your workflow's VPC.

1. For **Target**, select your VPC peering connection.

1. Choose **Save changes**.

For more information about considerations you may encounter while updating your route tables, consult [Update your route tables for a VPC peering connection](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-routing.html).

**To update the security group for your resource**

1. Open the [Amazon VPC Console](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Security groups**.

1. Select the security group for your resource.

1. Choose **Actions**.

1. From the dropdown list, choose **Edit inbound rules**.

1. Choose **Add rule**.

1. For **Type**, select the protocol your resource uses (for example, HTTPS, MySQL/Aurora, or Custom TCP).

1. For **Port range**, enter the port your resource listens on.

1. For **Source**, enter your workflow's VPC CIDR block (for example, 10.0.0.0/16).

1. Choose **Save rules**.

1. Choose **Edit outbound rules**.

1. Check whether outbound traffic is restricted. Default VPC settings allow all outbound traffic. If outbound traffic is restricted, continue to the next step.

1. Choose **Add rule**.

1. For **Type**, select **All traffic** or the specific protocol needed.

1. For **Destination**, enter your workflow's VPC CIDR block (for example, 10.0.0.0/16).

1. Choose **Save rules**.

**To enable DNS resolution for your peering connection**

1. Open the [Amazon VPC Console](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Peering connections**.

1. Select your peering connection.

1. Choose **Actions**.

1. Choose **Edit DNS settings**.

1. Below **Accepter DNS resolution**, select **Allow requester VPC to resolve DNS of accepter VPC hosts to private IP**.

1. Choose **Save changes**.

## Update VPC configuration in your workflow's account
<a name="vpc-cross-account-update-workflow"></a>

Log in to your workflow's account, then update the VPC configuration.

**To add a route for your VPC peering connection**

1. Open the [Amazon VPC Console](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Route tables**.

1. Select the check box next to the name of the route table for the subnet you will associate with your HealthOmics configuration.

1. Choose **Actions**.

1. Choose **Edit routes**.

1. Choose **Add route**.

1. For **Destination**, enter the CIDR block for your resource's VPC.

1. For **Target**, select your VPC peering connection.

1. Choose **Save changes**.

For more information about considerations you may encounter while updating your route tables, consult [Update your route tables for a VPC peering connection](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-routing.html).

**To update the security group for your HealthOmics workflow runs**

1. Open the [Amazon VPC Console](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Security groups**.

1. Select the security group you will use for your HealthOmics configuration.

1. Choose **Actions**.

1. Choose **Edit outbound rules**.

1. Choose **Add rule**.

1. For **Type**, select the protocol your resource uses (for example, HTTPS, MySQL/Aurora, or Custom TCP).

1. For **Port range**, enter the port your resource listens on.

1. For **Destination**, enter your resource's VPC CIDR block (for example, 10.1.0.0/16).

1. Choose **Save rules**.

1. Choose **Edit inbound rules**.

1. Check whether inbound traffic rules exist. If your resource needs to initiate connections back to your workflow runs, continue to the next step. Otherwise, skip to the DNS resolution step.

1. Choose **Add rule**.

1. For **Type**, select the appropriate protocol.

1. For **Source**, enter your resource's VPC CIDR block (for example, 10.1.0.0/16).

1. Choose **Save rules**.

**To enable DNS resolution for your peering connection**

1. Open the [Amazon VPC Console](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Peering connections**.

1. Select your peering connection.

1. Choose **Actions**.

1. Choose **Edit DNS settings**.

1. Below **Requester DNS resolution**, select **Allow accepter VPC to resolve DNS of requester VPC hosts to private IP**.

1. Choose **Save changes**.

## Running workflows with cross-account VPC access
<a name="vpc-cross-account-running-workflows"></a>

When starting a workflow run, use the subnets and security groups from the VPC in your workflow's account. Traffic from your workflow runs will be routed to the VPC in the other account through the VPC peering connection.

For information on creating HealthOmics configuration resources and starting workflow runs with VPC networking, see [Connecting HealthOmics workflows to a VPC](workflows-vpc-networking.md).

**Important**  
We recommend enabling VPC Flow Logs on both VPCs to verify traffic flow between them and to troubleshoot connectivity issues. For more information, see [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) in the *Amazon VPC User Guide*.

## Troubleshooting
<a name="vpc-cross-account-troubleshooting"></a>

If your workflow run cannot connect to resources in the peered VPC:

1. **Verify route tables**: Ensure both VPCs have bidirectional routes pointing to the VPC peering connection.

1. **Check security groups**: Confirm that security groups in both VPCs allow the required traffic (inbound in resource VPC, outbound in workflow VPC).

1. **Verify DNS resolution**: Ensure DNS resolution is enabled in both directions on the peering connection if using DNS names.

1. **Check CIDR blocks**: Verify that the CIDR blocks do not overlap between the two VPCs.

1. **Review VPC Flow Logs**: Enable VPC Flow Logs in both VPCs to diagnose traffic flow issues.

1. **Verify peering connection status**: Ensure the peering connection status is `active` in both accounts.

For more troubleshooting guidance, see [Troubleshoot a VPC peering connection](https://docs.aws.amazon.com/vpc/latest/peering/troubleshoot-vpc-peering-connections.html) in the *Amazon VPC Peering Guide*.

## Best practices
<a name="vpc-cross-account-best-practices"></a>

1. **Use least-privilege security groups**: Only allow the specific ports and protocols required for your workflow to access the resource.

1. **Document the peering relationship**: Maintain documentation of which VPCs are peered and for what purpose.

1. **Monitor cross-account traffic**: Use VPC Flow Logs and CloudWatch metrics to monitor traffic patterns and detect anomalies.

1. **Plan CIDR blocks carefully**: Ensure CIDR blocks do not overlap and leave room for future expansion.

1. **Test thoroughly**: Validate connectivity with test workflows before running production workloads.

1. **Coordinate with resource account owners**: Establish clear communication channels with the team managing the resource account for troubleshooting and maintenance.

1. **Use tags**: Tag your VPC peering connections, route tables, and security groups to identify their purpose and ownership.

## Additional resources
<a name="vpc-cross-account-resources"></a>
+ [VPC Peering Guide](https://docs.aws.amazon.com/vpc/latest/peering/)
+ [Connecting HealthOmics workflows to a VPC](workflows-vpc-networking.md)
+ [VPC CIDR blocks](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-cidr-blocks.html)
+ [Update your route tables for a VPC peering connection](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-routing.html)
+ [Troubleshoot a VPC peering connection](https://docs.aws.amazon.com/vpc/latest/peering/troubleshoot-vpc-peering-connections.html)