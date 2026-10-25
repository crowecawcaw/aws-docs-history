

# Design a new AWS network
<a name="transform-vmware-design-network"></a>

Build a clean, AWS-native network in a fraction of the time, without carrying over your legacy on-premises design or needing deep networking expertise. AWS Transform designs a production-ready network that follows AWS best practices from the start, which you review and adjust before deployment.

Choose **Design a new AWS network** when you don't want to translate an existing network into AWS and your target VPCs don't exist yet.

The AWS Transform agent guides you through the following steps, handling the design and generation while you make the decisions:

1. Select a network topology.

1. Define your network.

1. Review and optimize your network.

1. Generate a network diagram (optional).

1. Configure resource tagging.

1. Deploy your network.

**Note**  
For multi-account deployments, you must set up cross-account access before you start the network migration. For more information, see [Set up multi-account network migration](transform-vmware-network-multi-account-setup.md).

## Step 1: Select a network topology
<a name="transform-vmware-design-network-topology"></a>

AWS Transform asks how your applications and servers connect to each other, and uses your answer to select a network topology:
+ **Hub and Spoke** – Choose this topology when your applications and servers communicate with each other, for example when a web application calls a shared database, an internal API, or a common authentication service. An AWS Transit Gateway connects your VPCs and routes cross-VPC traffic through a central hub.
+ **Isolated VPCs** – Choose this topology when your applications run independently and don't need to reach each other.

For details about what AWS Transform deploys for each topology, see [Network topologies](transform-vmware-migrate-network-new-vpcs.md#network-topologies) in [Map source network to new VPCs](transform-vmware-migrate-network-new-vpcs.md).

## Step 2: Define your network
<a name="transform-vmware-design-network-define"></a>

Describe the applications you're migrating, and AWS Transform designs a VPC for each application environment. You can provide all of the following inputs in a single prompt, and refine them as you go.

For each application, provide the following:
+ **Application name** – A name for the application, for example `Billing`.
+ **Environments** – The environments the application runs in, for example production, staging, and development. AWS Transform creates one VPC for each application environment.
+ **Number of servers** – The approximate number of servers, per environment if they differ.

You can also provide the following optional details:
+ **Description** – A short description of what the application does.
+ **Preferred IP ranges** – The CIDR ranges you want to use, or avoid so that they don't overlap your existing networks. If you leave this blank, AWS Transform assigns non-overlapping ranges for you.
+ **Expected growth** – How much the application is expected to grow.

AWS Transform then asks you to size each VPC. The size sets the VPC's address space and how many addresses are available for subnets and future growth:
+ **Small** – Up to 250 addresses.
+ **Medium** – Up to 1,000 addresses.
+ **Large** – Up to 4,000 addresses.
+ **XL** – Up to 16,000 addresses.

After you confirm the design, AWS Transform generates the VPCs, along with the appliance VPCs required by your topology, and connects them.

## Step 3: Review and optimize your network
<a name="transform-vmware-design-network-review"></a>

Review the generated network through the same visual and chat interface that you use when you map a source network to new VPCs, and make changes through natural-language Direct Edits. AWS Transform validates each change and detects conflicts before it applies them. AWS Transform also marks the VPCs it proposes as *New* and any VPCs already in your target accounts as *Existing*, so you can see the full network across accounts and avoid CIDR conflicts before deployment. For more information, see [Review and optimize your network](transform-vmware-migrate-network-new-vpcs.md#transform-vmware-review-vpc-configs) in [Map source network to new VPCs](transform-vmware-migrate-network-new-vpcs.md).

**Note**  
Because you defined this network, AWS Transform doesn't recommend changes to your design choices, such as VPC names and sizes. It still validates your edits and flags conflicts.

## Step 4: Generate a network diagram (optional)
<a name="transform-vmware-design-network-diagram"></a>

You can generate a diagram of your network. For more information, see [Network diagram](transform-vmware-migrate-network-new-vpcs.md#transform-vmware-network-diagram) in [Map source network to new VPCs](transform-vmware-migrate-network-new-vpcs.md).

## Step 5: Configure resource tagging
<a name="transform-vmware-design-network-tagging"></a>

You can add custom tags to the resources that AWS Transform generates. For more information, see [Configure resource tagging](transform-vmware-migrate-network-new-vpcs.md#transform-vmware-tag-network-resources) in [Map source network to new VPCs](transform-vmware-migrate-network-new-vpcs.md).

## Step 6: Deploy your network
<a name="transform-vmware-design-network-deploy"></a>

Choose how to deploy your network. You can choose AWS Transform-managed deployment or self-deployment, and the same deployment approvals apply. For more information, see [Deploy your network](transform-vmware-migrate-network-new-vpcs.md#transform-vmware-deploy-network) in [Map source network to new VPCs](transform-vmware-migrate-network-new-vpcs.md).