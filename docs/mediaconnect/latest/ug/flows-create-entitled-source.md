# Creating a transport stream flow that

uses an entitled source

Transport stream flows transport compressed content that is muxed into a single
stream. An entitled source is content that comes from another AWS account.

## Prerequisites

- **NDI® configuration (for NDI use cases
  only)**

We recommend reviewing the [NDI
outputs](outputs-using-ndi.md "outputs-using-ndi.md") documentation to familiarize yourself with this feature
before getting started.

If you want to add an NDI output to your flow, you need a VPC with NDI
discovery servers provisioned in your network. MediaConnect connects to these
servers, but it doesn't create them for you.

    + For a quick start with VPCs, you can use our [AWS CloudFormation VPC template](../../../vpc/latest/userguide/create-vpc.md "../../../vpc/latest/userguide/create-vpc.md") to automatically create a VPC
     with public and private subnets. For more information about VPCs,
     see the [Amazon VPC User Guide](../../../vpc/latest/userguide.md "../../../vpc/latest/userguide.md").
    + For NDI discovery server deployment, AWS provides guidance on
     automated setup across multiple Availability Zones using AWS CloudFormation,
     including best practices for installation and configuration. For
     instructions, see [Setting Up NDI Discovery Servers for Broadcast
     Workflows](https://aws.amazon.com/solutions/guidance/programmatic-deployment-of-ndi-discovery-servers-for-broadcast-workflows-on-aws/ "https://aws.amazon.com/solutions/guidance/programmatic-deployment-of-ndi-discovery-servers-for-broadcast-workflows-on-aws/").
    + We recommend that you configure your security groups with a
     self-referencing ingress rule and egress rule. You can then attach this
     security group to the EC2 instances where your NDI servers are
     running within the VPC. This approach automatically allows all
     necessary NDI communication between components in your VPC, and all
     required network traffic is permitted. For guidance on setting up
     self-referencing security group rules, see [Security Group Referencing](../../../vpc/latest/userguide/security-group-rules.md#security-group-referencing "../../../vpc/latest/userguide/security-group-rules.md#security-group-referencing") in the Amazon VPC User
     Guide.

## Procedure

###### To create a transport stream flow that uses an entitled source

(console)

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/ "https://console.aws.amazon.com/mediaconnect/").
2. On the **Flows** page, choose **Create
   flow**.
3. In the **Details** section, for
   **Name**, specify a name for your flow. This name will
   become part of the ARN for this flow.

###### Note

MediaConnect allows you to create multiple flows with the same name.
However, we encourage you to use unique flow names within an AWS
Region to help with organization. After you create a flow, you can't
change the name. 4. For **Availability Zone**, choose one of the following
options:

    * Select **Any** (recommended)
    * Select a specific Availability Zone (useful if you're setting up
     redundant flows)

If you use the default setting (**Any**), MediaConnect will
randomly assign an Availability Zone within the current AWS Region. If
your source comes from a VPC, the service will assign the Availability Zone
of the VPC subnet to the flow.

###### Note

If your source comes from your VPC, the Availability Zone of your flow
must match that of your VPC subnet. We recommend that you leave this as
**Any** and let the service ensure that the
Availability Zone is set correctly. 5. Under **Flow size**, select the size that matches your
use case. For more information about flow sizes, see [Flow sizes and
capabilities](flow-sizes-capabilities.md "flow-sizes-capabilities.md").

**For medium flows:**

    * Proceed directly to step 6.

**For large flows:**

    * If you don't need NDI outputs for your flow, proceed directly to
     step 6.
    * If you want to add NDI outputs to your flow, configure the NDI
     settings as follows:




    	1. Set **Flow NDI support** to
    	 **Enabled**.
    	2. (Optional) Enter an **NDI machine
    	 name**.




    		+ This name is used as a prefix to help you identify
    		 the NDI sources that your flow creates. For example,
    		 if you enter `MACHINENAME`,
    		 your NDI sources will appear as
    		 `MACHINENAME`
    		`(ProgramName)`.
    		+ If you don’t enter a name, MediaConnect generates
    		 a unique 12-character ID as the prefix. This ID is
    		 derived from the flow's Amazon Resource Name (ARN),
    		 so the machine name references the flow
    		 resource.


    		###### Tip

    		Thoughtful naming is especially important when
    		 you have multiple flows creating NDI sources. For
    		 example, a production environment with 100 NDI
    		 sources would benefit from clear, descriptive
    		 machine name prefixes like `STUDIO-A`,
    		 `STUDIO-B`, `NEWSROOM`, and
    		 so on.
    	3. Add up to three **NDI discovery
    	 servers**. For each server, provide the
    	 following information:




    		+ Enter the server IP address from your existing NDI
    		 infrastructure.
    		+ Select the VPC interface adapter to control
    		 network access.
    		+ (Optional) Specify a port number. If you leave
    		 this blank, MediaConnect uses the NDI Discovery
    		 server default of TCP-5959.


    		###### Tip

    		You can add up to three discovery servers.
    		 Having multiple discovery servers improves
    		 reliability and helps ensure your NDI sources are
    		 discoverable across your network.

6. In the **Source** section:
   - For **Source type**, choose **Entitled
     source**.
   - For **Entitlement ARN**, choose the appropriate
     entitlement. This list includes all entitlements that have been
     granted to you.

###### Tip

You can click in this field and start entering the entitlement name.
MediaConnect will filter the list to include only entitlements with a
name that matches what you enter. 7. Under **Source monitoring configuration**, choose which
monitoring features you want to enable.

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

8. Choose **Create flow**.

## Next steps

Now that you've created a flow, complete these steps to start delivering your
content:

- [Add outputs](outputs-add.md "outputs-add.md") to specify where you want
  MediaConnect flow to send your content
- [Grant entitlements](entitlements-grant.md "entitlements-grant.md") to allow
  users of other AWS accounts to subscribe to your content
- [Start your flow](flows-start.md "flows-start.md") to begin content
  delivery

## Additional resources

For more information about source monitoring options for your flow, see the
following pages in this guide:

- [Viewing thumbnails of the source
  video](monitor-with-thumbnails.md "monitor-with-thumbnails.md")
- [Monitoring with content quality analysis in AWS Elemental MediaConnect](monitor-content-quality-analysis.md "monitor-content-quality-analysis.md")
