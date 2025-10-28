# Adding an NDI® output to a MediaConnect flow

This procedure walks you through the process of setting up an NDI® output and
configuring how your NDI video streams appear to other devices in your VPC
network. After you have the necessary prerequisites in place, you can add an NDI
output to your MediaConnect flow, allowing you to distribute your video and audio
streams over the NDI protocol within your VPC.

###### Note

CDI flows don't support NDI outputs.

## Prerequisites

We recommend reviewing the [NDI
outputs](outputs-using-ndi.md "outputs-using-ndi.md") documentation to familiarize yourself with this feature
before getting started.

Before you can add NDI outputs to a flow, make sure you have the following
resources in place:

**Large MediaConnect flow with NDI configuration
enabled**

- If you haven't created a flow yet, you'll need to
  [create a transport stream flow](flows-create.md "flows-create.md"). When you
  create the flow, you must set the size to large and make
  sure that NDI support is enabled.
- The flow can be in ACTIVE or STANDBY status before you
  add an NDI output.

**Network infrastructure**

- **VPC** - You'll need a
  Virtual Private Cloud (VPC). For a quick start, you can
  use the [AWS CloudFormation
  VPC template](../../../vpc/latest/userguide/create-vpc.md "../../../vpc/latest/userguide/create-vpc.md") to automatically create a VPC
  with public and private subnets. For more information
  about VPCs, see the [Amazon VPC User
  Guide](../../../vpc/latest/userguide.md "../../../vpc/latest/userguide.md").
- **Discovery servers** -
  NDI discovery servers must already be provisioned in
  your VPC network. MediaConnect connects to these servers, but
  it doesn't create them for you. AWS provides guidance
  for automatically deploying NDI discovery servers using
  AWS CloudFormation, including best practices for installation and
  configuration. For instructions, see [Setting Up NDI Discovery Servers for Broadcast
  Workflows](https://aws.amazon.com/solutions/guidance/programmatic-deployment-of-ndi-discovery-servers-for-broadcast-workflows-on-aws/ "https://aws.amazon.com/solutions/guidance/programmatic-deployment-of-ndi-discovery-servers-for-broadcast-workflows-on-aws/").
- **Security groups** - To
  enable NDI functionality, we recommend that you
  configure your security groups with a self-referencing
  ingress rule and egress rule. You can then attach this
  security group to the EC2 instances where your NDI
  servers are running within the VPC. This approach
  automatically allows all necessary NDI communication
  between components in your VPC, and all required network
  traffic is permitted. For guidance on setting up
  self-referencing security group rules, see [Security Group Referencing](../../../vpc/latest/userguide/security-group-rules.md#security-group-referencing "../../../vpc/latest/userguide/security-group-rules.md#security-group-referencing") in the Amazon
  VPC User Guide.
- In the following procedure, you’ll need to know your
  NDI server private IP address and your VPC subnet
  ID.

## Procedure

Follow these steps to set up an NDI output and configure how your NDI
video and audio streams appear to other devices in your VPC network.

###### To add an NDI output to a flow (console)

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/ "https://console.aws.amazon.com/mediaconnect/").
2. On the **Flows** page, choose the name of the
   flow that you want to add an output to.
3. On the flow details page under **Flow size**,
   make sure the size is set to **Large**.
4. On the flow details page under **NDI
   configuration**, configure your settings as
   follows:
   1. Set **Flow NDI support** to
      **Enabled** if it’s not already.
   2. (Optional) Enter an **NDI machine
      name**.
   - This name is used as a prefix to help you identify the NDI
     sources that your flow creates. For example, if you enter
     `MACHINENAME`, your NDI sources
     will appear as `MACHINENAME`
     `(ProgramName)`.
   - If you leave this blank, MediaConnect generates a unique
     12-character ID as the prefix. This ID is derived from the
     flow's Amazon Resource Name (ARN), so the machine name
     references the flow resource.

   ###### Tip

   Thoughtful naming is especially important when you
   have multiple flows creating NDI sources. For example, a
   production environment with 100 NDI sources would
   benefit from clear, descriptive machine name prefixes
   like `STUDIO-A`, `STUDIO-B`,
   `NEWSROOM`, and so on.
   c. Add up to three **NDI discovery
   servers**. For each server, provide the following
   information:
   - Enter the private IP address that's resolvable within the
     VPC subnet where the VPC adapter is pointed. This should be
     a private IP, not a public IP address.
   - Select the VPC interface adapter to control network
     access.
   - (Optional) Specify a port number. If you leave this blank,
     MediaConnect uses the NDI discovery server default of
     TCP-5959.

   ###### Note

   DNS names aren't currently supported for discovery
   servers.

   ###### Tip

   You can add up to three discovery servers. Having
   multiple discovery servers improves reliability and
   helps ensure your NDI sources are discoverable across
   your network.

5. Choose the **Outputs** tab.
6. Choose **Add output**.
7. For **Name**, specify a name for your output.
   This value is an identifier that is visible only on the
   AWS Elemental MediaConnect console and is not visible to the end user.
8. For **Output type**, choose **NDI
   output**.
9. For **NDI codec**, choose
   **SpeedHQ**.
10. For **NDI SpeedHQ quality**, enter a value
    between 100-200.
    - This setting adjusts the NDI encoder's target bitrate as a
      percentage of the default.
    - The default value is 100, which uses the standard NDI
      bitrate. Values up to 200 increase the target bitrate
      proportionally (for example, 200 doubles it).

###### Note

Some kinds of content (such as high-motion sports) will benefit from a higher quality setting.
However, keep in mind that using higher quality settings limits
the total number of outputs that a flow can generate (up to 2.5
Gbps). 11. (Optional) Enter an **NDI program name**.

    * This name is used as a suffix to help you identify the NDI
     sources that your flow creates. For example, if you enter
     `MyNDIProgram`, your NDI sources
     will appear as `MACHINENAME`
    `(MyNDIProgram)`.
    * If you leave this blank, MediaConnect uses the name of the
     output.


    ###### Tip

    Thoughtful naming is especially important when you
     have multiple flows creating NDI sources. For example,
     in a production environment, you might use names like
     `MainCam`, `BackupCam`,
     `GraphicsOutput`, and so on to clearly
     identify different video feeds from the same
     machine.

12. Choose **Add output**.

## Next steps

After you [start your flow](flows-start.md "flows-start.md"), you should
be able to see the MediaConnect NDI flow output as an available NDI source in your
discovery server. You can then subscribe to it to receive NDI traffic. For
more information, see the [NDI
documentation](https://docs.ndi.video/all/developing-with-ndi/introduction "https://docs.ndi.video/all/developing-with-ndi/introduction").
