# Creating a flow that uses an NDI® source

You can use MediaConnect to create flows that ingest content from NDI® senders
within your VPC. This guide explains how to create and configure a flow with an
NDI source in MediaConnect.

## Prerequisites

Before you begin, make sure you've completed the following steps:

- **Documentation review**

Review the [NDI sources](sources-using-ndi.md "sources-using-ndi.md")
documentation to understand the capabilities of this feature.

- **Infrastructure setup**

Set up your VPC infrastructure with at least one NDI discovery server
running, and with NDI senders actively broadcasting content within the
VPC.

    + For VPC setup: You can use the [AWS CloudFormation VPC
     template](../../../vpc/latest/userguide/create-vpc.md "../../../vpc/latest/userguide/create-vpc.md") to automatically create a VPC with public and
     private subnets. For more information about VPCs, see the [Amazon VPC User
     Guide](../../../vpc/latest/userguide.md "../../../vpc/latest/userguide.md").
    + For NDI discovery server deployment: AWS provides guidance on
     automated setup across multiple Availability Zones using AWS CloudFormation,
     including best practices for installation and configuration. For
     instructions, see [Setting Up NDI Discovery Servers for Broadcast
     Workflows](https://aws.amazon.com/solutions/guidance/programmatic-deployment-of-ndi-discovery-servers-for-broadcast-workflows-on-aws/ "https://aws.amazon.com/solutions/guidance/programmatic-deployment-of-ndi-discovery-servers-for-broadcast-workflows-on-aws/").
    + For security group configuration: We recommend that you configure
     your security groups with a self-referencing ingress rule and egress
     rule. You can then attach this security group to the EC2 instances
     where your NDI servers are running within the VPC. This approach
     automatically allows all necessary NDI communication between
     components in your VPC, and all required network traffic is
     permitted. For guidance, see [Security Group Referencing](../../../vpc/latest/userguide/security-group-rules.md#security-group-referencing "../../../vpc/latest/userguide/security-group-rules.md#security-group-referencing") in the Amazon VPC User
     Guide.

## Procedure

1.  Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/ "https://console.aws.amazon.com/mediaconnect/").
2.  On the **Flows** page, choose **Create
    flow**.
3.  Configure the basic flow details:
    - For **Name**, enter a name for your flow.
      - You can create multiple flows with the same name. However,
        we encourage you to use unique flow names within an
        AWS Region to help with organization.
      - Keep in mind that you can’t change this name after you
        create the flow.

    - For **Availability Zone**, choose an Availability
      Zone for your flow.
      - If you leave this as **Any**,
        MediaConnect will assign one based on your VPC
        subnet.

    - For **Flow size**, select
      **Large**.
      - You can only use NDI sources with large sized
        flows.
      - For more information about flow sizes, see [Flow sizes and
        capabilities](flow-sizes-capabilities.md "flow-sizes-capabilities.md").

4.  Configure your flow source:
    - For **Source type**, select **NDI
      Source**.
    - For **Flow source name**, enter a unique name for
      the NDI flow source.
      - Keep in mind that you can't change this name after you
        create the flow.

    - For **Flow source description**, enter a
      description to help you identify this source and its purpose.
    - (Optional) For **NDI source name**, specify the
      name of the upstream NDI sender that will send to your flow.

    You can either:

        + Leave this field empty for now, and select from a list of
         discovered sources after starting the flow.
        + Enter the exact name of an existing NDI sender that's
         registered with your discovery server (for example,
         `MACHINE (program)`).

5.  Configure the VPC interfaces for your flow:
    - In the **VPC interface** section, choose Add VPC
      interface.
    - For **Name**, enter a unique name for your VPC
      interface.
    - For **Role ARN**, specify the Amazon Resource
      Name (ARN) of the role that you created when you set up MediaConnect as a
      trusted service.
    - For VPC, choose the ID of the VPC that you want to use.
      - If your VPC isn't listed, verify that it's set up in
        Amazon Virtual Private Cloud and that you have IAM
        permissions to view it.

    - For **Subnet**, choose the VPC subnet that you
      want MediaConnect to use to set up your VPC configuration. You must choose
      at least one and can choose as many as you want.
    - For **Security groups**, specify the VPC security
      groups that you want MediaConnect to use to set up your VPC configuration.
      You must choose at least one security group.

6.  Configure the NDI settings:
    - Set **Flow NDI support** to **Enabled**
      if it's not already.
    - Enter an optional NDI machine name.
      - This name is used as a prefix to help you identify this
        flow source as an NDI receiver in your network. For example,
        if you enter `MACHINENAME`, your flow
        source will appear to your NDI senders as
        `MACHINENAME (ProgramName)`.
      - If you don’t enter a name, MediaConnect generates a unique
        12-character ID from the flow's ARN.

    - Add up to three NDI discovery servers. For each discovery server,
      provide the following information:
      - Enter the discovery server IP address (IPv4 format).
      - Specify a port number if you’re not using the default
        (5959).
      - Select the appropriate VPC interface adapter.

7.  Configure the encoder settings:
    - For **Encoder profile name**, choose the encoder
      profile that you want to apply to your flow outputs.
    - (Optional) For **Maximum bitrate**, specify the
      maximum expected bitrate in bits per second (bps).
      - This setting lets you override the default video bitrate
        within the profile's supported range (10-50 Mbps).
      - If left blank, MediaConnect uses the default value of 20,000,000 bps.

8.  Configure the monitoring options that you want to enable:
    1. Turn on **Thumbnails state** to generate source
       thumbnails that you can preview in the console.
    2. Turn on **Content quality analysis state** to
       monitor for the following audio and video quality issues.
       1. (Optional) Turn on **Black frames** to
          detect periods of black video frames in the stream.
       2. (Optional) Turn on **Frozen frames** to
          detect periods of unchanging video frames in the
          stream.
       3. (Optional) Turn on **Silent audio** to
          detect periods of audio silence in the stream.
       4. (Optional) Set a duration threshold between 10 and 60
          seconds for each metric that you enable. The default is 30
          seconds.

9.  At the bottom of the page, choose **Create flow**.

## Next steps

Now that you've created a flow, complete these steps to start delivering your
content:

- [Add outputs](outputs-add.md "outputs-add.md") to specify where you want
  your MediaConnect flow to send your content
- [Start your flow](flows-start.md "flows-start.md") to begin content
  delivery

### Selecting NDI senders

after you start your flow

When configuring your flow source, you can specify which upstream NDI sender
(like a camera or encoder) will provide content to your MediaConnect flow. If you
didn't specify this sender during flow creation or want to change it, you can
select one after starting your flow.

You must start your flow before you can perform this procedure. MediaConnect
can only discover and list available NDI senders when the flow is active.

###### To select or update upstream NDI sources

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/ "https://console.aws.amazon.com/mediaconnect/").
2. On the **Flows** page, choose the name of the flow
   that you want to update.
3. Start the flow if it’s not already active.
4. Choose the **Source** tab.
5. Choose the source that you want to update.
6. Choose **Update**.
7. Under **NDI source name**, specify the upstream
   source that the NDI sender will send to your flow.
   - Start typing a name in the field. As you type, matching NDI
     sources from your network will appear in a dropdown list.
   - Select the NDI source that you want to use from the
     list.
   - Choose the refresh button (⟳) to update the list of available
     NDI sources as needed.

8. Choose **Update** to save your changes.

## Additional

resources

For more information about source monitoring options for your flow, see the
following pages in this guide:

- [Viewing thumbnails of the source
  video](monitor-with-thumbnails.md "monitor-with-thumbnails.md")
- [Monitoring with content quality analysis in AWS Elemental MediaConnect](monitor-content-quality-analysis.md "monitor-content-quality-analysis.md")
