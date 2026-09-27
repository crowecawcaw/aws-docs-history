

# Getting started with the router
<a name="getting-started-router"></a>

This tutorial shows you how to use the MediaConnect router to dynamically route live video between independent inputs and outputs in real time, with centralized control across AWS Regions.

The tutorial is based on a scenario where you want to do all of the following:
+ Receive two live video feeds into the router: a primary awards show feed from New York City and a backup feed.
+ Route the primary feed to a distribution destination and a recording destination simultaneously.
+ Dynamically switch from the primary feed to the backup feed during a live event.

**Important**  
The router resources you create in this tutorial incur charges to your AWS account. AWS Elemental MediaConnect is not eligible for the AWS Free Tier. When you finish the tutorial, complete the cleanup step to delete the resources and stop incurring charges. For more information, see [AWS Elemental MediaConnect pricing](https://aws.amazon.com/mediaconnect/pricing/).

**Topics**
+ [Prerequisites](#getting-started-router-prerequisites)
+ [Step 1: Access AWS Elemental MediaConnect](#getting-started-router-access-console)
+ [Step 2: Create a router network interface](#getting-started-router-create-network-interface)
+ [Step 3: Create router inputs](#getting-started-router-create-inputs)
+ [Step 4: Create router outputs](#getting-started-router-create-outputs)
+ [Step 5: Assign routes](#getting-started-router-assign-routes)
+ [Step 6: Switch sources dynamically](#getting-started-router-switch-sources)
+ [Step 7: Clean up](#getting-started-router-clean-up)
+ [Next steps](#getting-started-router-next-steps)

## Prerequisites
<a name="getting-started-router-prerequisites"></a>

Before you can use the MediaConnect router, you need an AWS account and the appropriate permissions to access, view, and edit MediaConnect components. Complete the steps in [Setting up AWS Elemental MediaConnect](setting-up.md), and then return to this tutorial.

## Step 1: Access AWS Elemental MediaConnect
<a name="getting-started-router-access-console"></a>

After you set up your AWS account and create IAM roles, you sign in to the console for AWS Elemental MediaConnect.

**To access AWS Elemental MediaConnect**
+ Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/).

## Step 2: Create a router network interface
<a name="getting-started-router-create-network-interface"></a>

Before you can create router inputs, you need a router network interface. A network interface defines how your sources and destinations connect to the router. You can connect over the public internet or through your Amazon VPC.

For this tutorial, you create a public router network interface with the following details:
+ Network interface name: AwardsNYCInterface
+ Network interface type: Public
+ Allowlist CIDR: 10.24.34.0/23
+ Region: N. Virginia

**To create a router network interface**

1. In the navigation pane, choose **Router network interfaces**.

1. Choose **Create router network interface**.

1. For **Name**, enter **AwardsNYCInterface**.

1. For **Interface type**, choose **Public interface**.

1. For **Allowed CIDRs**, enter **10.24.34.0/23**.

1. For **AWS Region**, choose **N. Virginia**.

1. Choose **Create router network interface**.

**Note**  
If you need to receive content through your Amazon VPC instead of the public internet, choose **VPC interface** as the type and provide the subnet ID and security group IDs for your Amazon VPC configuration.

## Step 3: Create router inputs
<a name="getting-started-router-create-inputs"></a>

You create router inputs to receive content from your source endpoints. A router input is a connection point in the MediaConnect router that can receive content from your source. Each input is associated with a network interface and can be routed to multiple outputs.

For this tutorial, you create two inputs: one for the primary awards show feed and one for a backup feed. Use the following details:

**Primary input:**
+ Input name: AwardsPrimaryFeed
+ Tier: 20 Mbps
+ Maximum bitrate: 20,000,000 bps
+ Region: N. Virginia
+ Routing scope: Regional
+ Input type: Standard
+ Network interface ARN: (the ARN from Step 2)
+ Protocol: SRT Listener
+ Port: 5000
+ Minimum latency: 100 ms

**Backup input:**
+ Input name: AwardsBackupFeed
+ Tier: 20 Mbps
+ Maximum bitrate: 20,000,000 bps
+ Region: N. Virginia
+ Routing scope: Regional
+ Input type: Standard
+ Network interface ARN: (the ARN from Step 2)
+ Protocol: SRT Listener
+ Port: 5001
+ Minimum latency: 100 ms

**To create the primary router input**

1. In the navigation pane, choose **Router inputs**.

1. Choose **Create router input**.

1. For **Name**, enter **AwardsPrimaryFeed**.

1. For **Tier**, choose **20 Mbps**.

1. For **Maximum bitrate (bps)**, enter **20000000** or use the slider.

1. For **AWS Region**, choose **N. Virginia**.

1. For **Routing scope**, choose **Regional**.

1. For **Input type**, choose **Standard**.

1. For **Network interface ARN**, select the ARN for **AwardsNYCInterface**.

1. For **Protocol**, choose **SRT Listener**.

1. For **Port**, enter **5000**.

1. For **Minimum latency**, enter **100**.

1. Choose **Create router input**.

**To create the backup router input**

1. In the navigation pane, choose **Router inputs**.

1. Choose **Create router input**.

1. For **Name**, enter **AwardsBackupFeed**.

1. For **Tier**, choose **20 Mbps**.

1. For **Maximum bitrate (bps)**, enter **20000000** or use the slider.

1. For **AWS Region**, choose **N. Virginia**.

1. For **Routing scope**, choose **Regional**.

1. For **Input type**, choose **Standard**.

1. For **Network interface ARN**, select the ARN for **AwardsNYCInterface**.

1. For **Protocol**, choose **SRT Listener**.

1. For **Port**, enter **5001**.

1. For **Minimum latency**, enter **100**.

1. Choose **Create router input**.

After creation, each router input is in a **Standby** state. You must start the input before it can receive content.

**To start a router input**

1. On the **Router inputs** page, select the **AwardsPrimaryFeed** input.

1. Choose **Start**. The input transitions to an **Active** state and is ready to receive content.

1. Repeat for the **AwardsBackupFeed** input.

After the inputs start, provide your upstream sources with the input IP address and the port number for each input so they can begin sending content.

## Step 4: Create router outputs
<a name="getting-started-router-create-outputs"></a>

You create router outputs to deliver content to your downstream destinations. A router output is a connection point in the MediaConnect router that delivers content to a destination.

For this tutorial, you create two outputs: one for primary distribution and one for recording. Use the following details:

**Primary distribution output:**
+ Output name: PrimaryDistribution
+ Tier: 20 Mbps
+ Maximum bitrate: 20,000,000 bps
+ Region: N. Virginia
+ Output type: Standard
+ Network interface ARN: (the ARN from Step 2)
+ Protocol: SRT Caller
+ Destination IP address: {{destination-ip-address}}
+ Port: 6000
+ Minimum latency: 100 ms

**Recording output:**
+ Output name: RecordingDestination
+ Tier: 20 Mbps
+ Maximum bitrate: 20,000,000 bps
+ Region: N. Virginia
+ Output type: Standard
+ Network interface ARN: (the ARN from Step 2)
+ Protocol: SRT Caller
+ Destination IP address: {{destination-ip-address}}
+ Port: 6100

**To create the primary distribution output**

1. In the navigation pane, choose **Router outputs**.

1. Choose **Create router output**.

1. For **Name**, enter **PrimaryDistribution**.

1. For **Tier**, choose **20 Mbps**.

1. For **Maximum bitrate (bps)**, enter **20000000** or use the slider.

1. For **AWS Region**, choose **N. Virginia**.

1. For **Output type**, choose **Standard**.

1. For **Network interface ARN**, select the ARN for **AwardsNYCInterface**.

1. For **Protocol**, choose **SRT Caller**.

1. For **Destination address**, enter your destination IP address.

1. For **Port**, enter **6000**.

1. For **Minimum latency**, enter **100**.

1. Choose **Create router output**.

**To create the recording output**

1. In the navigation pane, choose **Router outputs**.

1. Choose **Create router output**.

1. For **Name**, enter **RecordingDestination**.

1. For **Tier**, choose **20 Mbps**.

1. For **Maximum bitrate (bps)**, enter **20000000** or use the slider.

1. For **AWS Region**, choose **N. Virginia**.

1. For **Output type**, choose **Standard**.

1. For **Network interface ARN**, select the ARN for **AwardsNYCInterface**.

1. For **Protocol**, choose **SRT Caller**.

1. For **Destination address**, enter your destination IP address.

1. For **Port**, enter **6100**.

1. Choose **Create router output**.

After creation, each router output is in a **Standby** state. You must start the output before it can deliver content.

**To start a router output**

1. On the **Router outputs** page, select the **PrimaryDistribution** output.

1. Choose **Start**. The output transitions to an **Active** state and is ready to deliver content.

1. Repeat for the **RecordingDestination** output.

## Step 5: Assign routes
<a name="getting-started-router-assign-routes"></a>

After you set up your router inputs and outputs, you can assign routes to control how content flows between them. A route connects an input to one or more outputs. It determines where your content goes.

AWS Elemental MediaConnect provides two ways to manage your route assignments:
+ **Router control panel view** – A real-time control interface well suited to live production. Like a traditional broadcast router, it lets you make immediate changes and see them take effect instantly. Visual indicators help you monitor your routes' status during live events.
+ **Router matrix view** – When you need to plan more complex changes, the matrix view lets you set up multiple route changes at once, making it particularly useful for scheduled program changes and complex routing scenarios.

**To assign a route using the control panel view**

1. In the navigation pane, choose **Router control panel**.

1. Choose **Configure** to open the configuration panel.

1. Select both the **AwardsPrimaryFeed** and **AwardsBackupFeed** inputs from the configuration panel.

1. Select both the **PrimaryDistribution** and **RecordingDestination** outputs from the configuration panel.

1. Select **Real-time control**.

1. Select the **PrimaryDistribution** output and then select the **AwardsPrimaryFeed** input. The route takes effect immediately.

1. Select the **RecordingDestination** output. Select the **AwardsPrimaryFeed** input again. The route takes effect immediately.

Your content now flows from **AwardsPrimaryFeed** to both **PrimaryDistribution** and **RecordingDestination** simultaneously.

You can also manage your route assignments in the **Router matrix**. The matrix shows all inputs as rows and all outputs as columns, with a marker at each intersection that is currently routed. The matrix is useful for reviewing and planning multiple route changes at once. Because you already assigned routes in the control panel, the matrix shows **AwardsPrimaryFeed** routed to both **PrimaryDistribution** and **RecordingDestination**.

**To review and change routes using the matrix view**

1. In the navigation pane, choose **Router matrix**.

1. Choose **Configure** to open the configuration panel.

1. Select both the **AwardsPrimaryFeed** and **AwardsBackupFeed** inputs and both the **PrimaryDistribution** and **RecordingDestination** outputs.

1. In the matrix, the intersections of **AwardsPrimaryFeed** with **PrimaryDistribution** and with **RecordingDestination** are marked as routed. To change a route, choose a different intersection in the same output column. For example, to switch **PrimaryDistribution** to the backup feed, choose the intersection of **AwardsBackupFeed** and **PrimaryDistribution**.

1. When you finish adjusting routes, choose **Apply route matrix** to apply your changes.

## Step 6: Switch sources dynamically
<a name="getting-started-router-switch-sources"></a>

With the router, you can switch sources instantly during a live event. For example, to switch from the primary feed to the backup feed:

**To switch sources using the control panel view**

1. In the control panel view, select the **PrimaryDistribution** output.

1. Select the **AwardsBackupFeed** input. The switch takes effect immediately; your downstream destination now receives the backup feed.

The previous route from **AwardsPrimaryFeed** to **PrimaryDistribution** is automatically unassigned when you assign a new input to the same output.

You can switch back to the primary feed at any time by reassigning **AwardsPrimaryFeed** to the **PrimaryDistribution** output.

## Step 7: Clean up
<a name="getting-started-router-clean-up"></a>

To avoid extraneous charges, be sure to stop and delete all unnecessary router resources. You must stop router inputs and outputs before they can be deleted.

**To stop and delete router outputs**

1. In the navigation pane, choose **Router outputs**.

1. Select the **PrimaryDistribution** output.

1. Choose **Stop** to put the output in **Standby** state.

1. After the output stops, choose **Delete**.

1. Repeat for the **RecordingDestination** output.

**To stop and delete router inputs**

1. In the navigation pane, choose **Router inputs**.

1. Select the **AwardsPrimaryFeed** input.

1. Choose **Stop** to put the input in **Standby** state.

1. After the input stops, choose **Delete**.

1. Repeat for the **AwardsBackupFeed** input.

**To delete the router network interface**

1. In the navigation pane, choose **Router network interfaces**.

1. Select the **AwardsNYCInterface** network interface.

1. Choose **Delete**.

## Next steps
<a name="getting-started-router-next-steps"></a>

To learn about ingesting and transporting live video with flows, see [Getting started with flows](getting-started-flows.md).