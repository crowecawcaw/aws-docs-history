# MediaConnect use case: receiving SRT content from MediaLive

You can set up AWS Elemental MediaConnect to receive content from an AWS Elemental MediaLive channel using the SRT
protocol. This enables you to establish a secure, reliable transport of live video from MediaLive to
MediaConnect for further distribution or processing.

This page describes your responsibilities for setting up to receive SRT output from MediaLive,
as described in [Creating an SRT caller output group](../../../medialive/latest/ug/opg-srt-caller.md "../../../medialive/latest/ug/opg-srt-caller.md").

## Planning

Before you get started, make sure you’ve considered the following.

- [Coordinate with the upstream system](#coordinate_with_upstream_system "#coordinate_with_upstream_system")
- [Plan for delivery using Amazon VPC](#plan_for_vpc_delivery "#plan_for_vpc_delivery")

### Coordinate with the upstream system

You and the MediaLive operator must agree on the following things:

- **Channel configuration** - Determine which type of
  MediaLive channel you’ll use:
  - If the MediaLive channel is a standard channel, you need two flow sources.
  - If the MediaLive channel is a single-pipeline channel, you need one flow source.

- **Latency** - Determine the appropriate latency for
  your streams.
  - We recommend that you choose a latency value that's close to the MediaLive
    configuration.
  - If you want the source from MediaLive to include a stream ID, tell the MediaLive
    operator what that ID is.

- **Encryption algorithm** - Determine the appropriate
  algorithm.
  - You must agree about the encryption algorithm that you'll use, which can be: AES
    128, AES 192, or AES 256

- **Encryption passphrase** - Determine the passphrase
  that you’ll use.
  - The passphrase can be 10 to 79 Unicode characters, which means that spaces are
    allowed.

### Plan for delivery using Amazon VPC

###### Considerations for Secrets Manager

When connecting to a MediaLive channel output that's running in a VPC, note that SRT
outputs are always encrypted and require AWS Secrets Manager integration. As a result, the MediaLive
channel output will be in a subnet with these characteristics:

- The subnet for the channel output must have a Secrets Manager endpoint.
- The subnet for the channel output and the Secrets Manager endpoint must use the same
  security group.

###### Considerations for MediaLive

When receiving content from MediaLive, the MediaLive channel output and the MediaConnect flow source
can be in the same VPC or in different VPCs. They typically share the same VPC but use
different subnets with separate VPC security groups. Note the following:

- If both services are in the same AWS account, they can use the same Secrets Manager
  secret. You don’t need to duplicate the secret just because MediaLive and MediaConnect are in
  different VPCs or subnets.
- If the services are in different AWS accounts, each operator typically sets up the
  secret separately in their respective AWS account.

## Tasks

You’ll need to complete the following tasks to receive SRT output from MediaLive.

- [1. Request a secret for encryption](#request_encryption_secret "#request_encryption_secret")
- [2. Create a MediaConnect flow with SRT
  listener](#create_mediaconnect_flow_srt_listener "#create_mediaconnect_flow_srt_listener")
- [3. Configure the MediaConnect flow's allowlist with
  MediaLive source IPs](#configure_flow_allowlist "#configure_flow_allowlist")
- [4. Start the flow and channel](#start_flow_and_channel "#start_flow_and_channel")

### 1. Request a secret for encryption

Someone in your organization with appropriate permissions must store the agreed-upon SRT
encryption passphrase in a secret in Secrets Manager.

###### To request the secret

1. Determine if you need one or two secrets.
   - **If MediaConnect and MediaLive are in the same
     AWS account**: You need only one shared secret that both services will
     use.
   - **If MediaConnect and MediaLive are in different
     AWS accounts**: Typically each operator sets up an identical secret
     separately in their respective AWS account, rather than using a shared secret.

2. Coordinate with the MediaLive operator and agree on who will request the secret
   creation.
3. If you're responsible for the secret creation, follow these steps for each secret
   that's needed:
   - Ask your AWS administrator to [create a secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md")
     in Secrets Manager, using **Other type** as the secret type.
   - Give your AWS administrator the agreed-upon SRT encryption passphrase to store
     in the secret.
   - Ask your AWS administrator to provide you with the following
     information:
     - The secret's name
     - The secret's ARN, which will look like this:
       `arn:aws:secretsmanager:`region`:123456789012:secret:`Sample-abcdef``

4. If you're using one shared secret, ensure that both MediaConnect and MediaLive operators
   receive the secret details.

### 2. Create a MediaConnect flow with SRT

listener

You must set up a MediaConnect flow to receive the content from MediaLive. You can then get the
inbound IP address from your flow and give it to the MediaLive operator, who will need this to
configure their channel.

###### To set up the flow and find the inbound IP address

1. Open the MediaConnect console.
2. Follow the steps to [create a flow](flows-create.md "flows-create.md") or [edit an existing
   flow](flows-update.md "flows-update.md") with these specific settings:
   - **Source type**: Choose either **Standard
     source** or **VPC source** based on your network
     configuration.
   - **Protocol**: Choose **SRT listener**.
   - **Source description**: Enter a descriptive name.

   ###### Tip

   If MediaLive is sending two sources, use this field to distinguish between each
   source. For example, `source-pipeline-0` and
   `source-pipeline-1`.
   - (For standard sources only):
     - **Allowlist CIDR block**: Enter a temporary value (such as
       `192.168.76.54/32`). You'll update this later with the
       actual MediaLive channel IP address.

   - (For VPC sources only):
     - **VPC interface name**: Specify your VPC interface.
     - **Subnet**: Choose the VPC subnet that you want MediaConnect to
       use.
     - **Security groups**: Specify the VPC security groups that
       you want MediaConnect to use.

   - **Port**: Enter a port number between 1 and 65535.
   - **Maximum latency**: Enter the agreed value.
   - **Encryption**: Select **Enable
     encryption**.
   - **Role ARN**: Specify a role that has permission to access
     Secrets Manager.
   - **Secret ARN**: Enter the ARN of the secret from the previous
     task ([1. Request a secret for encryption](#request_encryption_secret "#request_encryption_secret")).

3. After you’ve configured the flow, find the **Sources**
   tab on the flow details page.
4. Note the **Inbound IP address** value. For example,
   `srt://203.0.113.22:5000` or `srt://203.0.113.88:5001`.
5. Give this IP address to the MediaLive operator. The MediaLive operator can now [create a channel with an SRT caller output group](../../../medialive/latest/ug/creating-srt-caller-output-group.md "../../../medialive/latest/ug/creating-srt-caller-output-group.md") that points to your MediaConnect
   flow.

### 3. Configure the MediaConnect flow's allowlist with

MediaLive source IPs

After the MediaLive channel is created, you must configure the MediaConnect flow to accept traffic
from the channel.

###### To configure the flow

1. Ask the MediaLive operator for the source IP addresses from their channel.
   - For standard MediaLive channels: Request both Source IP addresses.
   - For single-pipeline channels: Request the single Source IP address.
   - For MediaLive Anywhere channels: Request the Gateway IP address into the network
     where the channel is running.

2. When you have the IP addresses:
   - Go to the MediaConnect console and open your flow.
   - Go to the **Sources** tab and select the SRT source.
   - Choose **Update**.
   - Under **Allowlist CIDR block**, enter the Source IP as a CIDR
     block (for example, `203.0.113.1/32`).
   - Choose **Update**.

###### Note

- If you have two sources, apply each IP address to the correct source.
- The IP addresses might be labeled as `pipeline 0` and
  `pipeline 1`.
- If you followed the example in the previous task ([2. Create a MediaConnect flow with SRT
  listener](#create_mediaconnect_flow_srt_listener "#create_mediaconnect_flow_srt_listener")), `pipeline
0` will correspond to the flow source that has
  `source-pipeline-0` in the source description field.

### 4. Start the flow and channel

After the flow and channel are both set up, you can now start the content flow from
MediaLive to MediaConnect.

###### To start the flow and channel

1. In the MediaConnect console, [start your flow](flows-start.md "flows-start.md").
2. After the flow is active (this takes about 1 minute), tell the MediaLive operator they
   can [start the channel](../../../medialive/latest/ug/aif-behavior-startup.md "../../../medialive/latest/ug/aif-behavior-startup.md").
3. After both are running, the MediaLive channel starts sending content to your MediaConnect
   flow.

## Troubleshooting

If you encounter issues with this workflow, use this checklist to identify and resolve
common problems:

- Verify that both services are using the same encryption passphrase.
- Check that the MediaConnect flow's allowlist includes the correct MediaLive channel IP
  address.
- Ensure that both services have the necessary permissions to access the secrets.
- Verify that the port specified in the MediaLive destination URL matches the port in the
  MediaConnect flow.
- For VPC setups, check that security groups allow the necessary traffic.
