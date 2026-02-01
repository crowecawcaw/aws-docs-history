# Creating a transport stream flow that uses a

VPC source

Transport stream flows transport compressed content that is muxed into a single
stream.

When you create a flow that uses a source from your virtual private cloud (VPC), your
content does not go over the public internet. This is useful for security reasons as
well as reliability. You set up your VPC and then create a flow that has an interface to
that VPC. Alternatively, you can create a flow based on an entitlement that another
AWS account granted to allow you to use their content ([entitled source](flows-create-entitled-source.md "flows-create-entitled-source.md")) or a [standard source](flows-create-standard-source.md "flows-create-standard-source.md").

## Prerequisites

Before you begin, make sure you've completed the following steps:

**VPC configuration**

In Amazon VPC, set up your VPC and associated security groups. For more
information about VPCs, see the [Amazon VPC User Guide](../../../vpc/latest/userguide.md "../../../vpc/latest/userguide.md"). For information about
configuring security groups to work with your VPC interface, see [Security group
considerations](vpc-interface-security-groups.md "vpc-interface-security-groups.md").

**IAM setup**

In IAM, [set up
MediaConnect as a trusted service](security-iam-trusted-entity.md "security-iam-trusted-entity.md").

**Encryption setup (if required)**

If the source of your flow requires encryption, [set up
encryption](encryption-static-key-set-up.md "encryption-static-key-set-up.md").

**NDI® configuration (for NDI use cases
only)**

We recommend reviewing the [NDI
outputs](outputs-using-ndi.md "outputs-using-ndi.md") documentation to familiarize yourself with this
feature before getting started.

If you want to add an NDI output to your flow, you need a VPC with NDI
discovery servers provisioned in your network. MediaConnect connects to these
servers, but it doesn't create them for you.

- AWS provides guidance on automated setup across multiple
  Availability Zones using AWS CloudFormation, including best practices for
  installation and configuration. For instructions, see [Setting Up NDI Discovery Servers for Broadcast
  Workflows](https://aws.amazon.com/solutions/guidance/programmatic-deployment-of-ndi-discovery-servers-for-broadcast-workflows-on-aws/ "https://aws.amazon.com/solutions/guidance/programmatic-deployment-of-ndi-discovery-servers-for-broadcast-workflows-on-aws/").
- We recommend that you configure your security groups with a
  self-referencing ingress rule and egress rule. You can then attach
  this security group to the EC2 instances where your NDI servers
  are running within the VPC. This approach automatically allows
  all necessary NDI communication between components in your VPC,
  and all required network traffic is permitted. For guidance on
  setting up self-referencing security group rules, see [Security Group Referencing](../../../vpc/latest/userguide/security-group-rules.md#security-group-referencing "../../../vpc/latest/userguide/security-group-rules.md#security-group-referencing") in the Amazon VPC User
  Guide.

## Procedure

###### To create a transport stream flow that uses a VPC source (console)

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
change the name. 4. For **Availability Zone**, choose
**Any** or choose the Availability Zone where your VPC
subnet resides. We recommend that you leave this as **Any**
and let the service ensure that the Availability Zone is set correctly. 5. Under **Flow size**, select the size that matches your
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

6. In the **Source** section, for **Source
   type**, choose **VPC source**.
7. For **Name**, specify a name for your source. This value
   is an identifier that is visible only on the MediaConnect console.
8. Determine which protocol your source uses.

###### Note

If you want to specify redundant sources for failover, create the flow
with one of the sources. After the flow is created, update it to
activate failover on the source, and add the second source to the flow.
Because MediaConnect treats both sources as the primary source, it
doesn't matter which one you specify when you first create the flow. 9. For specific instructions based on your protocol, choose one of the
following tabs:

RIST

    1. For **Protocol**, choose
     **RIST**.
    2. For **Ingest port**, specify the port
     that the flow will listen on for incoming content.


    ###### Note

    The RIST protocol requires one additional port for
     error correction. To accommodate this requirement,
     MediaConnect reserves the port that is +1 from the
     port that you specify. For example, if you specify
     port 4000 for the output, the service assigns ports
     4000 and 4001.
    3. For **VPC interface name**, choose
     the name of the VPC interface that you want to use as
     the source.
    4. For **Maximum bitrate**, specify the
     maximum expected bitrate (in bits per second) for the
     flow. We recommend that you specify a value that is
     twice the actual bitrate.
    5. For **Maximum latency**, specify the
     size of the buffer (delay) that you want the service to
     maintain. A higher latency value means a longer delay in
     transmitting the stream, but more room for error
     correction. A lower latency value means a shorter delay,
     but less room for error correction. You can choose a
     value from 1-15,000 ms. If you keep this field blank,
     the service uses the default value of 2,000 ms.

RTP or RTP-FEC

    1. For **Protocol**, choose
     **RTP** or
     **RTP-FEC**.
    2. For **Ingest port**, specify the port
     that the flow will listen on for incoming
     content.


    ###### Note

    The RTP-FEC protocol requires two additional ports
     for error correction. To accommodate this
     requirement, MediaConnect reserves the ports that
     are +2 and +4 from the port that you specify. For
     example, if you specify port 4000 for the output,
     the service assigns ports 4000, 4002, and 4004.
    3. For **VPC interface name**, choose
     the name of the VPC interface that you want to use as
     the source.
    4. For **Maximum bitrate**, specify the
     maximum expected bitrate (in bits per second) for the
     flow. We recommend that you specify a value that is
     twice the actual bitrate.

SRT listener

    1. In the **Source** section, for
     **Source type**, choose
     **VPC source**.
    2. For **Name**, specify a name for your
     source. This value is an identifier that is visible only
     on the MediaConnect console. It is not visible to
     anyone outside of the current AWS account.
    3. For **Protocol**, choose
     **SRT listener**.
    4. For **Source description**, enter a
     description that will remind you later where this source
     is from. This might be the company name or notes about
     the setup.
    5. For **VPC interface name**, choose
     the name of the VPC interface that you want to use as
     the source.
    6. For **Inbound port**, specify the
     port that the flow listens on for incoming
     content.
    7. For **Maximum bitrate**, specify the
     maximum expected bitrate (in bits per second) for the
     flow. We recommend that you specify a value that is
     twice the actual bitrate.
    8. For **Minimum latency**, specify the
     size of the buffer (delay) that you want the service to
     maintain. A higher latency value means a longer delay in
     transmitting the stream, but more room for error
     correction. A lower latency value means a shorter delay,
     but less room for error correction. You can choose a
     value from 10 -15,000 ms. If you keep this field blank,
     the service uses the default value of 2,000 ms.


    The SRT protocol uses a **minimum
     latency** configuration on each side of the
     connection. The larger of these two values is used as
     the *recovery latency*. If the
     transmitted bitrate, multiplied by the recovery latency,
     is higher than the *receiver
     buffer*, the buffer will overflow and the
     stream can fail with a `Buffer Overflow
     Error`. On the SRT receiver side, the receiver
     buffer is configured by the SRTO\_RCVBUF value. The size
     of the receiver buffer is limited by the *flow control window
     size* (SRTO\_FC) value. On the MediaConnect side, the
     receiver buffer is calculated as the **maximum bitrate** value
     multiplied by the **minimum
     latency** value. For more information about
     the SRT buffer, see [the SRT Configuration Guidelines.](https://github.com/Haivision/srt/blob/master/docs/API/configuration-guidelines.md "https://github.com/Haivision/srt/blob/master/docs/API/configuration-guidelines.md")
    9. If the source is encrypted, choose
     **Activate** in the
     **Decryption** section and do the
     following:




    	1. For **Role ARN**, specify the
    	 ARN of the role that you created when you [set up encryption](encryption-static-key-set-up.md#encryption-static-key-set-up-create-iam-role "encryption-static-key-set-up.md#encryption-static-key-set-up-create-iam-role").
    	2. For **Secret ARN**, specify
    	 the ARN that AWS Secrets Manager assigned when you [created the secret to store the encryption
    	 key](encryption-static-key-set-up.md#encryption-static-key-set-up-store-key "encryption-static-key-set-up.md#encryption-static-key-set-up-store-key").

SRT caller

    1. In the **Source** section, for
     **Source type**, choose
     **VPC source**.
    2. For **Name**, specify a name for your
     source. This value is an identifier that is visible only
     on the MediaConnect console. It is not visible to
     anyone outside of the current AWS account.
    3. For **Protocol**, choose
     **SRT caller**.
    4. For **Source description**, enter a
     description that will remind you later where this source
     is from. This might be the company name or notes about
     the setup.
    5. For **VPC interface name**, choose
     the name of the VPC interface that you want to use as
     the source.
    6. For **Source listener port**, enter
     the port the flow will use to pull the source
     from.
    7. For **Maximum bitrate** (optional),
     specify the maximum expected bitrate (in bits per
     second) for the flow. We recommend that you specify a
     value that is twice the actual bitrate.
    8. For **Minimum latency**, specify the
     minimum size of the buffer (delay) that you want the
     service to maintain. A higher latency value means a
     longer delay in transmitting the stream, but more room
     for error correction. A lower latency value means a
     shorter delay, but less room for error correction. You
     can choose a value from 10–15,000 ms. If you keep this
     field blank, MediaConnect uses the default value of 2,000 ms.


    The SRT protocol uses a **minimum
     latency** configuration on each side of the
     connection. The larger of these two values is used as
     the *recovery latency*. If the
     transmitted bitrate, multiplied by the recovery latency,
     is higher than the *receiver
     buffer*, the buffer will overflow and the
     stream can fail with a `Buffer Overflow
     Error`. On the SRT receiver side, the receiver
     buffer is configured by the SRTO\_RCVBUF value. The size
     of the receiver buffer is limited by the *flow control window
     size* (SRTO\_FC) value. On the MediaConnect side, the
     receiver buffer is calculated as the **maximum bitrate** value
     multiplied by the **minimum
     latency** value. For more information about
     the SRT buffer, see [the SRT Configuration Guidelines.](https://github.com/Haivision/srt/blob/master/docs/API/configuration-guidelines.md "https://github.com/Haivision/srt/blob/master/docs/API/configuration-guidelines.md")
    9. For **Stream ID** (optional), enter
     an identifier for the stream. This identifier can be
     used to communicate information about the stream.
    10. If the source is encrypted, choose
     **Activate** in the
     **Decryption** section and do the
     following:




    	1. For **Role ARN**, specify the
    	 ARN of the role that you created when you [set up encryption](encryption-static-key-set-up.md#encryption-static-key-set-up-create-iam-role "encryption-static-key-set-up.md#encryption-static-key-set-up-create-iam-role").
    	2. For **Secret ARN**, specify
    	 the ARN that AWS Secrets Manager assigned when you [created the secret to store the encryption
    	 key](encryption-static-key-set-up.md#encryption-static-key-set-up-store-key "encryption-static-key-set-up.md#encryption-static-key-set-up-store-key").

Zixi push

    1. For **Name**, specify a name for your
     source. This value is an identifier that is visible only
     on the MediaConnect console. It is not visible to
     anyone outside of the current AWS account.
    2. For **Protocol**, choose
     **Zixi push**.


    ###### Note

    MediaConnect assigns the inbound port for Zixi
     push VPC sources at the time of creation. A port
     number 2090–2099 will be assigned
     automatically.
    3. For **VPC interface name**, choose
     the name of the VPC interface that you want to use as
     the source.
    4. For **Stream ID**, specify the stream
     ID set in the Zixi feeder.


    ###### Important

    If you leave this field blank, the service uses
     the source name as the stream ID. Because the stream
     ID must match the value set in the Zixi feeder, you
     need to specify the stream ID if it is not exactly
     the same as the source name.
    5. For **Maximum latency**, specify the
     size of the buffer (delay) that you want the service to
     maintain. A higher latency value means a longer delay in
     transmitting the stream, but more room for error
     correction. A lower latency value means a shorter delay,
     but less room for error correction. You can choose a
     value between 0 and 60,000 ms. If you keep this field
     blank, the service uses the default value of 6,000 ms.
    6. If the source is encrypted, choose
     **Activate** in the
     **Decryption** section and do the
     following:




    	1. For **Decryption type**,
    	 choose **Static key**.
    	2. For **Role ARN**, specify the
    	 ARN of the role that you created when you [set up encryption](encryption-static-key-set-up.md#encryption-static-key-set-up-create-iam-role "encryption-static-key-set-up.md#encryption-static-key-set-up-create-iam-role").
    	3. For **Secret ARN**, specify
    	 the ARN that AWS Secrets Manager assigned when you [created the secret to store the encryption
    	 key](encryption-static-key-set-up.md#encryption-static-key-set-up-store-key "encryption-static-key-set-up.md#encryption-static-key-set-up-store-key").
    	4. For **Decryption algorithm**,
    	 choose the type of encryption that was used to
    	 encrypt the source.

10. For each VPC that you want to connect to the flow, do the following:
    1.  In the **VPC interface** section, choose
        **Add VPC interface**.
    2.  For **Name**, specify a name for your VPC
        interface. The name of the VPC interface must be unique within the
        flow.
    3.  For **Role ARN**, specify the Amazon Resource
        Name (ARN) of the role that you created when you set up
        MediaConnect as a trusted service.
    4.  For **VPC**, choose the ID of the VPC that you
        want to use.

    ###### Note

    If you don't see the VPC that you want in the list, verify
    that the VPC has been set up in Amazon Virtual Private Cloud and that you have
    IAM permissions to view the VPC. 5. For **Subnet**, choose the VPC subnet that you
    want MediaConnect to use to set up your VPC configuration. You must
    choose at least one and can choose as many as you want. 6. For **Security groups**, specify the VPC security
    groups that you want MediaConnect to use to set up your VPC
    configuration. You must choose at least one security group.

11. Under **Source monitoring configuration**, choose which
    monitoring features you want to enable.
    1.  Turn on **Thumbnails state** to generate source
        thumbnails that you can preview in the console.
    2.  Turn on **Content quality analysis state** to
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

12. At the bottom of the page, choose **Create flow**.

## Next steps

Now that you've created a flow, complete these steps to start delivering your
content:

- [Add outputs](outputs-add.md "outputs-add.md") to specify where you want your
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
