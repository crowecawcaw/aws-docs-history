

# Connecting to a VPC in another account
<a name="workflows-vpc-cross-account"></a>

You can give your HealthOmics workflow runs access to resources in an Amazon VPC that belongs to a different AWS account. With AWS Resource Access Manager (AWS RAM) sharing, the VPC owner shares subnets with your account, and HealthOmics places the elastic network interfaces (ENIs) for your runs in those subnets. With VPC peering, the ENIs stay in your own VPC, and a peering connection routes traffic to the VPC in the other account. RAM sharing requires both accounts to belong to the same organization in AWS Organizations, while peering has no such requirement and fits runs that only need to reach specific resources in the other account.

**Note**  
The Amazon VPC and other resources that you create for these approaches might result in charges to your AWS account. Before you allow access between accounts, confirm that your plan meets the security requirements of the organizations that manage both accounts.

**Topics**
+ [Key concepts](#vpc-cross-account-key-concepts)
+ [Using RAM sharing](#vpc-cross-account-ram)
+ [Using VPC peering](#vpc-cross-account-peering)
+ [Best practices](#vpc-cross-account-best-practices)
+ [Additional resources](#vpc-cross-account-resources)

## Key concepts
<a name="vpc-cross-account-key-concepts"></a>

Choose between RAM sharing and VPC peering based on where your workflow runs must operate. With RAM sharing, the VPC owner shares subnets (and optionally security groups) with a participant in the same AWS Organization, and HealthOmics places elastic network interfaces (ENIs) directly in the shared VPC. With VPC peering, the requester and the accepter route traffic between their VPCs. The ENIs remain in the requester's VPC, and the peering connection routes traffic to the accepter's VPC. Both approaches use the same HealthOmics configuration resource. Only RAM sharing sets the `vpcOwnerAccountId` parameter.

The following terms identify the accounts in each approach:
+ **VPC owner (RAM sharing):** The account that owns the VPC and shares subnets (and optionally security groups). In this approach, the other account is the VPC owner.
+ **Participant (RAM sharing):** The account that runs HealthOmics workflows and receives shared subnets and security groups from the VPC owner. In this approach, your account is the participant.
+ **Requester (VPC peering):** The account that initiates the VPC peering connection; the workflow run's ENIs remain here. In this approach, your account is the requester.
+ **Accepter (VPC peering):** The account that accepts the peering connection request and whose VPC holds the resource you want to reach. In this approach, the other account is the accepter.

### Choosing an approach
<a name="vpc-cross-account-choosing"></a>

The following table summarizes the differences between the two approaches.


| Consideration | RAM sharing | VPC peering | 
| --- | --- | --- | 
| AWS Organizations required | Yes. Both accounts must be in the same organization. | No | 
| Use when | The workflow must operate inside a shared VPC (centralized egress, central network account) | The workflow only needs to reach resources in another account's VPC | 
| Scaling considerations | Subject to AWS RAM service quotas (default 25,000 resource shares per AWS Region, with up to 5,000 resources and 5,000 principals per share) | Subject to VPC peering connection service quotas (default 50 active peering connections per VPC). If you expect to exceed this limit, consider RAM sharing instead. | 

If you already know your requirements, use the following guidance:
+ If the accounts are not in the same organization, use VPC peering.
+ If the workflow must run inside the other account's VPC, use RAM sharing.
+ If you expect more than 50 active peering connections on one VPC, use RAM sharing.

## Using RAM sharing
<a name="vpc-cross-account-ram"></a>

Use this procedure to give your HealthOmics workflow runs access to subnets (and optionally security groups) that another AWS account shares with you using AWS Resource Access Manager (AWS RAM). The VPC owner shares subnets to your (participant) account, and HealthOmics places your workflow run's elastic network interfaces (ENIs) directly in the shared subnets. Use this approach for centralized networking models, such as a shared egress VPC managed by a central network account.

For more information about sharing VPC resources, see [Share your VPC subnets with other accounts](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-sharing.html) and [Share security groups with AWS Organizations](https://docs.aws.amazon.com/vpc/latest/userguide/security-group-sharing.html) in the Amazon VPC User Guide.

### Prerequisites
<a name="vpc-cross-account-ram-prerequisites"></a>

To use a RAM-shared VPC with HealthOmics, you must have:
+ Both the VPC owner account and your (participant) account in the same AWS Organization.
+ The `AWSServiceRoleForHealthOmics` service-linked role in *both* accounts. HealthOmics automatically creates this role in your account when you create your first configuration. HealthOmics cannot create the role in the VPC owner account because that would be a cross-account operation. Contact the VPC owner to confirm that the role exists in their account, or ask them to create it.
+ A VPC with subnets in the VPC owner account that meets your connectivity needs (for example, NAT Gateway for internet access). Subnets must be in Availability Zones where HealthOmics operates in the AWS Region. You cannot share subnets in a default VPC; only subnets in a non-default VPC can be shared with AWS RAM.
+ A security group in the shared VPC. The security group can be owned by either the VPC owner account (and shared to your account with AWS RAM) or by your (participant) account.
+ Permission to create AWS RAM resource shares in the VPC owner account.
+ Permission to create HealthOmics configuration resources in your account.
+ Permission to start HealthOmics workflow runs.

### Step 1: Create the VPC and share resources (VPC owner account)
<a name="vpc-cross-account-ram-share"></a>

Perform the following steps in the VPC owner account. You need permission to create AWS RAM resource shares. To enable sharing with AWS Organizations, sign in to the AWS RAM console with the organization's management account. For more information, see [Enable resource sharing within AWS Organizations](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html#getting-started-sharing-orgs) in the AWS RAM User Guide.

Before you begin, create the VPC, subnets, security groups, and any required connectivity (such as a NAT gateway) in the VPC owner account. For more information about VPC setup, see [Connecting HealthOmics workflows to a VPC](workflows-vpc-networking.md).

**To enable sharing and create a resource share**

1. If the accounts aren't in the same AWS organization, create an organization and invite the participant account.

1. From the management account, enable resource sharing with AWS Organizations:

   ```
   aws ram enable-sharing-with-aws-organization
   ```

   Member accounts then receive shared resources without accepting an invitation.

1. Open the [AWS RAM console](https://console.aws.amazon.com/ram/).

1. Choose **Create resource share**.

1. For **Resources**, add the subnets that your runs will use. Optionally add a security group.

1. For **Principals**, enter the participant account ID or the organization ID.

1. Choose **Create resource share**.

For more information, see [Creating a resource share in AWS RAM](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing-create.html) in the AWS RAM User Guide.

### Step 2: Accept the share and create a configuration (participant account)
<a name="vpc-cross-account-ram-configure"></a>

To run your workflows inside the shared VPC, perform the following steps in the account that runs your HealthOmics workflows.

**To accept a resource share invitation**

1. Open the [AWS RAM console](https://console.aws.amazon.com/ram/).

1. In the navigation pane, choose **Shared with me**, then **Resource shares**.

1. If a resource share invitation is pending, select the invitation and choose **Accept resource share**.
**Note**  
If the VPC owner enabled sharing with AWS Organizations, no invitation appears. The shared resources are available in your account automatically.

1. Open the [Amazon VPC console](https://console.aws.amazon.com/vpc/) and verify that the shared subnets (and security groups, if shared) are visible in your account.

Create the HealthOmics configuration. Set `vpcOwnerAccountId` to the VPC owner's 12-digit account ID, and provide one or more shared subnet and security group IDs.

**Console**

In the HealthOmics console, create a configuration with the following JSON:

```
{
  "name": "{{cross-account-ram-config}}",
  "runConfigurations": {
    "vpcConfig": {
      "securityGroupIds": ["{{sg-1234567890abcdef0}}"],
      "subnetIds": ["{{subnet-1234567890abcdef0}}"],
      "vpcOwnerAccountId": "{{111122223333}}"
    }
  }
}
```

**AWS CLI**

```
aws omics create-configuration \
  --name {{cross-account-ram-config}} \
  --run-configurations '{
    "vpcConfig": {
      "securityGroupIds": ["{{sg-1234567890abcdef0}}"],
      "subnetIds": ["{{subnet-1234567890abcdef0}}"],
      "vpcOwnerAccountId": "{{111122223333}}"
    }
  }'
```

After creating the configuration:

1. Wait for the configuration status to become `ACTIVE`. This can take up to 15 minutes.

1. Start your workflow run with networking mode set to `VPC` and specify the name of the configuration that you created.

For more information about VPC networking, see [Connecting HealthOmics workflows to a VPC](workflows-vpc-networking.md).

### Verification
<a name="vpc-cross-account-ram-verification"></a>

Confirm that RAM sharing is configured correctly:
+ The HealthOmics configuration status shows `ACTIVE` (this can take up to 15 minutes after creation).
+ The shared subnets (and security groups, if shared) are visible in the participant account's Amazon VPC console.
+ A workflow run started with `networkingMode` set to `VPC` and the RAM-shared configuration completes without network-related errors, and its ENIs appear in the shared subnets.

### Troubleshooting RAM sharing
<a name="vpc-cross-account-ram-troubleshooting"></a>

For general AWS RAM problems, see [Troubleshooting AWS Resource Access Manager](https://docs.aws.amazon.com/ram/latest/userguide/troubleshooting.html) in the AWS RAM User Guide.


| Problem | Common cause | Resolution | 
| --- | --- | --- | 
| The shared subnets don't appear in your account | The resource share doesn't include your account or organization, you haven't accepted the invitation, or you're in a different AWS Region than the share. |  1. In the AWS RAM console, check whether a resource share invitation is pending, and accept it.<br />2. Confirm that you're in the same AWS Region as the shared subnets.<br />3. Ask the VPC owner to confirm that the resource share includes your account ID or your organization.  | 
| The configuration doesn't become ACTIVE, or the run can't start | The vpcOwnerAccountId value is incorrect, or the AWSServiceRoleForHealthOmics service-linked role doesn't exist in the VPC owner account. |  1. Confirm that `vpcOwnerAccountId` is the 12-digit account ID of the VPC owner, not your own.<br />2. Ask the VPC owner to confirm that the `AWSServiceRoleForHealthOmics` role exists in their account, or to create it.  | 
| A run can't reach the resource in the shared VPC | A security group or route in the shared VPC blocks the traffic. |  1. Confirm that the security group you chose in the configuration allows the traffic on the resource's port.<br />2. Ask the VPC owner to confirm that the route tables for the shared subnets provide the connectivity your runs need, such as a route to a NAT gateway.<br />3. Enable VPC Flow Logs in the shared VPC to see whether the traffic is accepted or rejected.  | 
| The VPC owner can't delete a shared subnet or VPC after stopping a share | HealthOmics ENIs remain attached to the shared subnets. HealthOmics removes them after they've been unused for 48 hours. | Wait until HealthOmics removes the ENIs, and then delete the subnets or VPC. | 

### Stopping a RAM share
<a name="vpc-cross-account-ram-stopping"></a>

As the VPC owner, you might stop sharing your subnets with a participant account when the participant no longer needs access, or to revoke access for security or compliance reasons. To stop a share, delete the AWS RAM resource share (or remove the participant as a principal) in the AWS RAM console.

When you stop a share, HealthOmics protects you from losing control of your VPC:
+ The participant can no longer use configurations that reference the unshared resources to start new runs.
+ The participant can no longer use the unshared resources to create new configurations.
+ HealthOmics sweeps the elastic network interfaces (ENIs) it created in the shared subnets after they have been unused for 48 hours.

**Important**  
HealthOmics creates ENIs in the participant account, even though they are attached to the shared subnets. While those ENIs remain attached, the VPC owner cannot delete them and cannot delete the shared VPC or subnets. After HealthOmics sweeps the ENIs, the VPC owner can delete the associated resources.

## Using VPC peering
<a name="vpc-cross-account-peering"></a>

Use this procedure to give your HealthOmics workflow runs private connectivity to a resource in another account's VPC by creating a VPC peering connection. Your workflow run's ENIs remain in your own (requester) VPC, and the peering connection routes traffic to the accepter's VPC. You don't need any HealthOmics-specific setup for VPC peering, and you don't set the `vpcOwnerAccountId` parameter.

This procedure connects two accounts with a peering connection using IPv4. For more information about other peering scenarios, see the [VPC Peering Guide](https://docs.aws.amazon.com/vpc/latest/peering/).

### Prerequisites
<a name="vpc-cross-account-peering-prerequisites"></a>

To use VPC peering with HealthOmics workflow runs, you must have:
+ An HealthOmics workflow configured to authenticate with and then read from your resource.
+ A resource in another account, such as an Amazon RDS cluster or license server, available through Amazon VPC.
+ Credentials for your requester's account and your accepter's account. If you are not authorized to use your accepter's account, contact an authorized user to prepare that account.
+ Permission to create and update a VPC (and supporting Amazon VPC resources) to associate with your HealthOmics workflow runs.
+ Permission to create HealthOmics configuration resources.
+ Permission to create a VPC peering connection in your requester's account.
+ Permission to accept a VPC peering connection in your accepter's account.
+ Permission to update the configuration of your accepter's VPC (and supporting Amazon VPC resources).
+ Permission to start HealthOmics workflow runs.

### Step 1: Create an Amazon VPC in your requester's account
<a name="vpc-cross-account-peering-create-vpc"></a>

Create an Amazon VPC, subnets, route tables, and a security group in your HealthOmics requester account. For instructions, see [Create a VPC](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html) in the Amazon VPC User Guide.

**To create a VPC for your HealthOmics workflow runs**

1. Open the Amazon VPC Console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the dashboard, choose **Create VPC**.

1. For **IPv4 CIDR block**, provide a private Classless Inter-Domain Routing (CIDR) block that doesn't overlap with blocks used in your accepter's VPC. Don't pick a block your accepter's VPC uses to assign IPs to resources or a block already defined in the route tables in your accepter's VPC. For more information, see [VPC CIDR blocks](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-cidr-blocks.html) in the Amazon VPC User Guide.

1. For **Availability Zones**, select at least one Availability Zone where HealthOmics operates in your AWS Region.

1. Set **Number of public subnets** to **0**.

1. Set **VPC endpoints** to **None** (you can add these later for cost optimization).

1. Choose **Create VPC**.

### Step 2: Create a VPC peering connection request
<a name="vpc-cross-account-peering-create"></a>

Create a VPC peering connection request from your requester's VPC to the accepter's VPC. For instructions, see [Create a VPC peering connection](https://docs.aws.amazon.com/vpc/latest/peering/create-vpc-peering-connection.html) in the Amazon VPC Peering Guide.

**To request a VPC peering connection**

1. Open the [Amazon VPC Console](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Peering connections**.

1. Choose **Create peering connection**.

1. For **VPC ID (Requester)**, select your requester's VPC.

1. For **Account**, choose **Another account** and enter the accepter's account ID.

1. For **VPC ID (Accepter)**, enter the accepter's VPC ID.

1. Choose **Create peering connection**.

The peering connection stays in the `Pending acceptance` state until the accepter's account accepts it.

### Step 3: Prepare the accepter's account
<a name="vpc-cross-account-peering-prepare-accepter"></a>

To create your peering connection and prepare the accepter's VPC to use the connection, log in to the accepter's account with a role that holds the permissions listed in the prerequisites. In the accepter's account, perform the following procedures.

**Important**  
Accept peering requests only from AWS accounts that you know and trust. A request from an unknown account might be an attempt to gain network access to your VPC.

**To accept the VPC peering connection request**

1. Open the [Amazon VPC Console](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Peering connections**.

1. Select the pending VPC peering connection (the status is `pending-acceptance`).

1. Choose **Actions**, then **Accept request**.

1. When prompted for confirmation, choose **Accept request**.

1. Choose **Modify my route tables now** to add a route to the main route table for your VPC.

Inspect the route tables for the accepter's VPC afterward. The route that Amazon VPC generates might not establish connectivity, based on how the accepter's VPC is set up. Check for conflicts between the new route and existing configuration for the VPC. For instructions on troubleshooting, see [Troubleshoot a VPC peering connection](https://docs.aws.amazon.com/vpc/latest/peering/troubleshoot-vpc-peering-connections.html) in the Amazon VPC Peering Guide.

**To update the route table for the accepter's VPC**

1. Open the [Amazon VPC Console](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Route tables**.

1. Select the route table for the subnet associated with your resource.

1. Choose **Actions**, then **Edit routes**.

1. Choose **Add route**.

1. For **Destination**, enter the CIDR block for your requester's VPC.

1. For **Target**, select your VPC peering connection. The connection must have the status `Active` to appear in the target list.

1. Choose **Save changes**.

For more information, see [Update your route tables for a VPC peering connection](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-routing.html) in the Amazon VPC Peering Guide.

**To update the security group for the accepter's resource**

1. Open the [Amazon VPC Console](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Security groups**.

1. Select the security group for your resource.

1. Choose **Actions**, then **Edit inbound rules**.

1. Choose **Add rule**.

1. For **Type**, select the protocol your resource uses (for example, HTTPS, MySQL/Aurora, or Custom TCP).

1. For **Port range**, enter the port your resource listens on.

1. For **Source**, enter your requester's VPC CIDR block (for example, 10.0.0.0/16).

1. Choose **Save rules**.

1. Choose **Edit outbound rules**. Default VPC settings allow all outbound traffic. If outbound traffic from your accepter's security group is restricted, add an outbound rule allowing traffic to your requester's VPC CIDR block.

For more information, see [Configure security group rules](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-security-group-rules.html) in the Amazon VPC User Guide.

**(Optional) To enable DNS resolution for the peering connection**

1. Open the [Amazon VPC Console](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Peering connections**.

1. Select your peering connection.

1. Choose **Actions**, then **Edit DNS settings**.

1. Below **Accepter DNS resolution**, select **Allow requester VPC to resolve DNS of accepter VPC hosts to private IP**.

1. Choose **Save changes**.

For more information, see [Enable DNS resolution for a VPC peering connection](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-dns.html) in the Amazon VPC Peering Guide.

### Step 4: Update VPC configuration in the requester's account
<a name="vpc-cross-account-peering-update-requester"></a>

Log in to your requester's account, then update the VPC configuration.

**To add a route for the VPC peering connection**

1. Open the [Amazon VPC Console](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Route tables**.

1. Select the route table for the subnet you will associate with your HealthOmics configuration.

1. Choose **Actions**, then **Edit routes**.

1. Choose **Add route**.

1. For **Destination**, enter the CIDR block for the accepter's VPC.

1. For **Target**, select your VPC peering connection. The connection must have the status `Active` to appear in the target list.

1. Choose **Save changes**.

For more information, see [Update your route tables for a VPC peering connection](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-routing.html) in the Amazon VPC Peering Guide.

**To update the security group for your HealthOmics workflow runs**

1. Open the [Amazon VPC Console](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Security groups**.

1. Select the security group you will use for your HealthOmics configuration.

1. Choose **Actions**, then **Edit outbound rules**.

1. Choose **Add rule**.

1. For **Type**, select the protocol your resource uses (for example, HTTPS, MySQL/Aurora, or Custom TCP).

1. For **Port range**, enter the port your resource listens on.

1. For **Destination**, enter the accepter's VPC CIDR block (for example, 10.1.0.0/16).

1. Choose **Save rules**.

1. If your resource needs to initiate connections back to your workflow runs, choose **Edit inbound rules**, add a rule allowing traffic from the accepter's VPC CIDR block, and choose **Save rules**.

For more information, see [Configure security group rules](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-security-group-rules.html) in the Amazon VPC User Guide.

**(Optional) To enable DNS resolution for the peering connection**

1. Open the [Amazon VPC Console](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Peering connections**.

1. Select your peering connection.

1. Choose **Actions**, then **Edit DNS settings**.

1. Below **Requester DNS resolution**, select **Allow accepter VPC to resolve DNS of requester VPC hosts to private IP**.

1. Choose **Save changes**.

For more information, see [Enable DNS resolution for a VPC peering connection](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-dns.html) in the Amazon VPC Peering Guide.

### Step 5: Run workflows with VPC peering
<a name="vpc-cross-account-peering-run"></a>

When starting a workflow run, use the subnets and security groups from the VPC in your requester's account. Don't set `vpcOwnerAccountId`. The VPC peering connection routes traffic from your workflow runs to the VPC in the other account.

For information about creating HealthOmics configuration resources and starting workflow runs with VPC networking, see [Connecting HealthOmics workflows to a VPC](workflows-vpc-networking.md).

### Verification
<a name="vpc-cross-account-peering-verification"></a>

Confirm that VPC peering is configured correctly:
+ The VPC peering connection status is `Active` in both the requester and accepter accounts.
+ Both VPCs have bidirectional routes in their route tables pointing to the VPC peering connection.
+ If using DNS names, DNS resolution is enabled in both directions on the peering connection.
+ A workflow run started with the requester's subnets and security groups, and without `vpcOwnerAccountId` set, successfully reaches the resource in the accepter's VPC.

### Troubleshooting VPC peering
<a name="vpc-cross-account-peering-troubleshooting"></a>

For general VPC peering problems, see [Troubleshoot a VPC peering connection](https://docs.aws.amazon.com/vpc/latest/peering/troubleshoot-vpc-peering-connections.html) in the Amazon VPC Peering Guide.


| Problem | Common cause | Resolution | 
| --- | --- | --- | 
| A run can't reach the resource in the other account | The peering connection isn't active, the CIDR blocks overlap, a route is missing in one of the VPCs, or a security group blocks the traffic. If the run uses a private hostname, DNS resolution might be off. |  1. Confirm that the peering connection status is `active`.<br />2. Confirm that the two VPC CIDR blocks don't overlap.<br />3. Confirm that each VPC has a route to the other VPC's CIDR block that targets the peering connection.<br />4. Confirm that the security groups in both VPCs allow the traffic on the resource's port.<br />5. If the run uses a private DNS hostname, confirm that DNS resolution is enabled on the peering connection for the direction you need.<br />6. Confirm that you didn't set `vpcOwnerAccountId` in the configuration.  | 

## Best practices
<a name="vpc-cross-account-best-practices"></a>

Follow these practices to keep your cross-account VPC configuration secure and maintainable:
+ **Use least-privilege security groups.** Only allow the specific ports and protocols required for your workflow to access the resource.
+ **Document the cross-account relationship.** Record which VPCs are shared or peered, with whom, and for what purpose, including the ENI cleanup timing (HealthOmics sweeps unused ENIs 48 hours after a RAM share is stopped) so the VPC owner knows when shared resources can be safely deleted.
+ **Monitor cross-account traffic.** Use VPC Flow Logs and CloudWatch metrics to monitor traffic patterns and detect anomalies.
+ **Test thoroughly.** Validate connectivity with test workflows before running production workloads, and confirm the configuration status reaches `ACTIVE` (RAM sharing) or the peering connection status reaches `Active` (VPC peering) before starting production runs.
+ **Coordinate with account owners.** Establish clear communication channels with the team managing the other account for troubleshooting and maintenance.
+ **Use tags.** Tag your VPC resources, peering connections, and AWS RAM shares to identify their purpose and ownership.
+ **Plan for ENI cleanup (RAM sharing).** Establish a process between the VPC owner and participant accounts for cleaning up ENIs when configurations are no longer needed. HealthOmics sweeps unused ENIs automatically after 48 hours, but the VPC owner cannot delete the shared VPC or subnets until that sweep completes.
+ **Plan CIDR blocks carefully (VPC peering).** Ensure CIDR blocks do not overlap and leave room for future expansion. If you expect to need more than the default 50 active peering connections per VPC, consider RAM sharing instead.

## Additional resources
<a name="vpc-cross-account-resources"></a>
+ [Connecting HealthOmics workflows to a VPC](workflows-vpc-networking.md)
+ [Share your VPC with other accounts](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-sharing.html) in the Amazon VPC User Guide
+ [Update your route tables for a VPC peering connection](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-routing.html) in the *Amazon VPC Peering Guide*
+ [Troubleshoot a VPC peering connection](https://docs.aws.amazon.com/vpc/latest/peering/troubleshoot-vpc-peering-connections.html) in the Amazon VPC Peering Guide
+ [VPC CIDR blocks](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-cidr-blocks.html) in the Amazon VPC User Guide
+ [AWS RAM User Guide](https://docs.aws.amazon.com/ram/latest/userguide/)
+ [VPC Peering Guide](https://docs.aws.amazon.com/vpc/latest/peering/)