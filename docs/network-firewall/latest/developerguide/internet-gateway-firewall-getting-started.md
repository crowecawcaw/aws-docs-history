

# Getting started with Automated Internet Firewall

This section walks you through protecting your VPCs with automated internet firewall. You set it up in the Network Security Manager console or the Amazon VPC console, and you can view the firewall in the Network Firewall console.

You don't create automated internet firewalls directly. In Network Security Manager (NSM), you first define a scope that includes the VPCs to protect, then a policy that describes how to protect them, and then combine the two into a deployment. NSM then sets up each automated internet firewall automatically: it configures the subnet connectivity and creates the firewall at the internet gateway. Automated internet firewalls can't be created or changed any other way.

After you deploy automated internet firewall, each VPC in the scope gets its own igw-firewall, which sits at the VPC's internet gateway and is named after the VPC ARN (`arn:aws:network-firewall:<region>:<account-id>:igw-firewall/<vpc-id>`). You can monitor it by using the Network Firewall monitoring dashboard.

Only Network Security Manager can create, change, or delete an automated internet firewall, or the firewall policies and rule groups that it creates. You can view them in the Network Firewall console on the **Internet firewalls** tab of the **Firewalls** page, and through the Network Firewall API. If you try to change them with the Network Firewall API, the request fails with "IGW Firewalls must be created and updated through AWS Network Security Manager." (firewall) or "This resource is managed by AWS Network Security Manager and can only be modified through Network Security Manager." (policy or rule group).

## Before you begin
<a name="internet-gateway-firewall-getting-started-prereqs"></a>

To follow this tutorial, you need the following:
+ A VPC with an internet gateway attached. Network Firewall builds out the automated internet firewall in an Availability Zone only when the VPC has an internet gateway attached and that Availability Zone has at least one active network interface, such as a running instance. A stopped instance does not count. Until a zone has active resources, it shows **Standby** ("AZ has no active resources") and provisions automatically when you launch the first resource there.
+ Network Security Manager set up for your account. Network Security Manager works in one of two models:
  + **Single-account** – No AWS Organizations or administrator account is needed. Create an IAM identity with Network Security Manager permissions. Network Security Manager creates a service-linked role in your account automatically.
  + **Multi-account** – Your organization in AWS Organizations must have all features enabled, trusted access for Network Security Manager, and a Network Security Manager administrator account. The organization's management account adds administrators on the **Settings** page (**Add administrator**). You register an administrator in each Region where you use Network Security Manager.

For details, see [Setting up AWS Network Security Manager](https://docs.aws.amazon.com/network-security-manager/latest/devguide/setting-up.html) in the *AWS Network Security Manager Developer Guide*.

## Step 1: Create and deploy an Automated Internet Firewall policy
<a name="internet-gateway-firewall-getting-started-step1"></a>

Network Security Manager offers a Quick create and deploy wizard that takes you through creating the policy, scope, and deployment.

**To create an Automated Internet Firewall policy with Quick create**

1. Open the Network Security Manager console at [https://console.aws.amazon.com/network-security-manager/](https://console.aws.amazon.com/network-security-manager/), and in the navigation pane, choose **Overview**.

1. In the top right of the **Overview** page, choose **Quick create and deploy**.

1. In the **Define protections** section:

   1. For **Firewall type**, choose **Automated Internet Firewall**.

   1. Under **Templates and rules**, add at least one template or rule. A policy is made up of rules, which you can stack together in a template. Each rule corresponds to a Network Firewall rule group, and you can share a template across multiple policies. You can add up to 100 items to a policy, where each template and each rule counts as one item. Up to 2 of the items can be templates, and each template can contain up to 50 rules. Rules inside a template don't count toward the 100-item limit. As a result, a policy can have up to 100 rules with no templates, or 2 templates plus up to 98 rules.

      1. To add a template, choose **Manage templates**, select the templates, and choose **Update templates**. The AWS managed template `AWSManagedTemplateIGWFirewallBaseline` "Blocks traffic to known attack infrastructure, malware distribution domains, and botnet command-and-control domains using AWS managed Network Firewall IPS rule groups. All other traffic is allowed (default action ACCEPT)." You can also choose your own templates.

      1. To add rules, choose **Manage rules**, select the rules, and choose **Update rules**.

   1. Under **Automated Internet Firewall settings**, for **Enforcement mode**, choose one of the following:

      1. **Monitor** – Log matching traffic without blocking it. Recommended starting point for VPCs with existing workloads. This is the default.

      1. **Enforce** – Block matching traffic.

   1. (Optional) Under **Logging**, select **Alert logs**, **Flow logs**, or both. For each log type, choose a **Destination type** (Amazon S3 bucket, CloudWatch Logs log group, or Kinesis Data Firehose delivery stream) and the destination. Additional charges apply.

   1. Choose **Done**.

1. In the **Policy details** section:

   1. For **Name**, enter a name for the policy. Use only letters, numbers, hyphens, and underscores (up to 128 characters). Optionally, enter a **Description**.

   1. For **Object names**, choose **Automatic** (the default) to have Network Security Manager create names for the scope and deployment based on the policy name, or **Custom** to enter your own.

   1. **Remediation** is selected and can't be changed. It is required for automated internet firewall policies.

   1. Review **Policy priority**. The new policy evaluates after your existing policies of the same firewall type, so it won't override them where scopes overlap. You can change the priority later in the policy editor.

   1. Choose **Done**.

1. In the **Set the scope** section:

   1. (Multi-account only) Under **Accounts and OUs**, choose **Include the entire AWS Organization**, **Exclude specific OUs and accounts**, or **Include only specific OUs and accounts**. In single-account mode, this section doesn't appear.

   1. Under **Set scope for VPCs**, for **VPC resource scope**, choose one of the following:

      1. **Include all existing and future VPCs** – Protect all existing and future VPCs.

      1. **Include specific VPCs** – Only protect VPCs that match the criteria.

      1. **Exclude specific VPCs** – Protect all VPCs except those that match the criteria.

   1. For **Include specific VPCs** or **Exclude specific VPCs**, add tags or VPC ARNs as the criteria (up to 100 ARNs).

   1. Choose **Done**.

1. In the **Subnet connectivity** section:

   1. For **Subnet connectivity type**, choose one of the following:

      1. **flexible** (recommended) – Applies outbound-only connectivity to resources without a public IP association, and bidirectional connectivity to resources with a public IP association. Subnet traffic routed through a NAT gateway or an egress-only internet gateway automatically gets outbound-only connectivity, regardless of public IP association. This is the default.

      1. **bidirectional** – Subnet resources with a public IP association get bidirectional access to and from the internet.

      1. **outbound-only** – Subnet resources can connect to the internet. Unsolicited connections from the internet are blocked.

   1. (Optional) To give specific subnets a different connectivity type, expand **Subnet connectivity overrides**. For **Override types**, choose one or more of **flexible**, **bidirectional**, **outbound-only**, and **exclude** (leaves these subnets out of automated internet firewall protection). For each override, enter subnet tags or ARNs. If a subnet matches more than one override, the one listed first applies. Each override is saved as its own scope.

   1. Choose **Done**.

1. In the **Review and deploy** section, review the deployment name. (Multi-account only) To make the deployment visible to other accounts in your organization, keep **Enable cross-account visibility for this deployment** selected.

1. (Optional) Under **Tags**, add tags.

1. Choose **Create and deploy**.

The console shows "Successfully created deployment" and opens the deployment's details page. Network Security Manager then discovers resources and applies protections. This process is asynchronous and might take a few minutes to complete.

**Important**  
Deployments incur charges. You pay for each in-scope resource that Network Security Manager monitors and protects. For automated internet firewalls, hourly charges apply per VPC in each Availability Zone, plus a per-GB fee for inspected traffic. Traffic to services reached through VPC gateway endpoints never passes through the internet gateway, so the firewall does not inspect it. Before you deploy, review the Network Security Manager pricing page and automated internet firewall pricing.

**To start from the Amazon VPC console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/), and in the navigation pane, choose **Your VPCs**.

1. (Optional) Select the VPCs that you want to protect.

1. Choose **Actions**, then under **Security**, choose **Create Automated Internet Firewall**.

1. In **About Automated Internet Firewall protection**, review the information, and then choose **Create protection**. The Network Security Manager console opens **Quick create and deploy** in a new tab. If you selected VPCs, **Firewall type** is set to **Automated Internet Firewall**, `AWSManagedTemplateIGWFirewallBaseline` is added, and **Set scope for VPCs** is set to **Include specific VPCs** with the selected VPCs. You can change all of these.

1. Continue from step 3 of the previous procedure.

To see existing deployments, choose **Actions**, then **View Automated Internet Firewall deployments**.

## Step 2: Check the deployment in Network Security Manager
<a name="internet-gateway-firewall-getting-started-step2"></a>

On the deployment's details page, choose the **Synchronization** tab. It lists the resources in scope of this deployment and their synchronization status. To see why a resource is out of sync, select it and review **Out-of-sync reasons** and **Remediation issues**.
+ **In sync** – The resource configuration matches your intended protection settings.
+ **Out of sync** – The resource configuration doesn't match. Network Security Manager remediates this automatically.
+ **Not applicable** – The resource is in scope but can't be evaluated by this deployment.

To see which VPCs a policy governs, open the policy and choose the **Coverage** tab. It lists each VPC that the policy's scope names, with a **Coverage status** of **In effect** or **Superseded**.

## Step 3: View the Automated Internet Firewall in the Network Firewall console
<a name="internet-gateway-firewall-getting-started-step3"></a>

**To view the Automated Internet Firewall**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, under **Network Firewall**, choose **Firewalls**.

1. Choose the **Internet firewalls** tab. The table shows **Firewall name**, **Status**, **Configuration sync state**, **Enforcement mode**, **Protected VPC**, and **Associated policy**. The firewall name is the ID of the VPC that it protects. **Enforcement mode** always shows **Policy controlled**. The firewall's actual mode is the policy mode of its associated policy (ENFORCE blocks, MONITOR only logs), shown on the **Firewall policy settings** tab. **Status** is one of the following:

   1. **Provisioning** – The firewall is being created.

   1. **Ready** – The firewall is ready.

   1. **Standby** – Nothing to protect yet. Network Firewall builds out the firewall automatically when needed. The status is shown for the firewall and for each Availability Zone.

   1. **Deleting** – Network Security Manager is deleting the firewall.

1. Choose a firewall name to open its details page. The details page has an **Overview** section and the tabs **Firewall policy settings**, **NAT IPs**, **Monitoring**, and **Tags**.

   1. **NAT IPs** – The Elastic IP addresses this firewall uses to translate outbound traffic from protected subnets. These Elastic IP addresses are allocated in your account and owned by you; the firewall's service-linked role allocates and attaches them on your behalf, and you cannot release or reassign them while the firewall is using them. Each Availability Zone starts with one address, and the service adds more automatically as NAT port usage grows, up to 8 per Availability Zone. Because allocation happens in your account, an account-level IPAM allocation policy applies, so the addresses can come from your own IPAM pool.

   1. **Tags** – Tags on this automated internet firewall are inherited from the associated Network Security Manager policy and can't be modified directly.

To view the firewall policy, choose the **Associated policy**. The policy page shows "Created by AWS Network Security Manager. Manage this policy in Network Security Manager." On the **Firewall policies** list, **Managed by** shows **AWS Network Security Manager**, and **Delete** is turned off for these policies. To change the policy, choose **Manage in AWS Network Security Manager**.

From the **Internet firewalls** tab, you can also open Network Security Manager:
+ **Create in AWS Network Security Manager** – Opens **Quick create and deploy**.
+ **Actions** > **Edit associated policy** – Opens the selected firewall's policy.
+ **Actions** > **Edit protection scope** – Opens the scopes list.
+ **Actions** > **View policy prioritization and coverage** – Opens the deployments list.

## Step 4: Change the protection
<a name="internet-gateway-firewall-getting-started-step4"></a>

Make all changes in Network Security Manager. Network Security Manager updates the automated internet firewalls through remediation, and adds an Availability Zone to a firewall when coverage is needed there.
+ To change the protections (templates and rules, enforcement mode, logging, priority, or subnet connectivity) – Open the policy, choose **Edit**, make your changes, and choose **Save changes**.
+ To change which VPCs are protected – Open the scope, choose **Edit**, make your changes, and choose **Save**. Or open the deployment, choose **Edit**, choose **Change scope**, and choose **Save changes**.

If a draft version exists, **Edit** is turned off with "A draft version exists. Edit, publish, or discard the draft first."

If you remove a VPC from one deployment's scope while another deployment still covers it, the VPC's automated internet firewall switches to the other deployment's policy.

## Step 5: Clean up
<a name="internet-gateway-firewall-getting-started-step5"></a>

Only Network Security Manager can delete an automated internet firewall. You can't delete it in the Network Firewall console or with the Network Firewall API.

Delete the resources in reverse order, because they reference each other. You can't delete an active resource that another active resource references.

1. In the Network Security Manager console, choose **Overview**, then the **Deployments** tab. Select your deployment, choose **Actions**, then **Delete**. Enter `delete` to confirm, and choose **Delete**. The resources in the scope lose this protection immediately.

1. Choose the **Scopes** tab. Delete the scope, and any subnet connectivity override scopes that Quick create made.

1. Choose the **Policies** tab. Delete the policy.

1. In the Network Firewall console, refresh the **Internet firewalls** tab. After you delete the deployment and its related resources in Network Security Manager, the automated internet firewalls that it created are removed from Network Firewall.