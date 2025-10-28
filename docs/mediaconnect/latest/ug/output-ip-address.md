# Determining an output's IP address

When you're working with outputs on standard flows, there are two important IP
addresses to understand:

- **Output IP address** - This is the MediaConnect
  endpoint address where your downstream receivers connect to. You’ll need this
  address when you configure your receivers to connect to your flow and start
  receiving its content.
- **Output peer IP address** - This is the IP
  address of the device that’s currently receiving content from your output. This
  address is useful for troubleshooting connectivity issues and monitoring which
  devices are actively connected to your output.
  The following sections explain how to find the IP address and the peer IP address for
  your flow outputs.

## Finding an output’s IP address

You can view the IP address for each of your flow outputs in the MediaConnect console, or
by using the [DescribeFlow](../api/API_DescribeFlow.md "../api/API_DescribeFlow.md") API
operation.

###### To determine an output's IP address

1. On the **Flows** page, choose the name of the flow that
   you want to view.
2. For specific instructions based on how content is sent to your output,
   choose one of the following tabs:

Public internet

    1. In the **Details** section, note the
     **Public Outbound IP address**.
     This is the IP address that the receiver needs.

Private internet

    1. Choose the **Outputs** tab, and then
     find the output that you want to view.
    2. Under **Listener
     address** for that output, note the IP
     address. This is the IP address that the receiver
     needs.

## Finding an output’s peer IP

address

You can view the current peer IP address for each of your flow outputs in the
MediaConnect console, or by using the [DescribeFlow](../api/API_DescribeFlow.md "../api/API_DescribeFlow.md") API
operation.

###### To determine an output’s peer IP address

1. On the **Flows** page, choose the name of the flow that
   you want to view.
2. Choose the **Outputs** tab.
3. Select the output that you want to view, and then choose
   **Details**.
4. Under **Peer IP Address**, note the peer IP
   address.

###### Note

For certain types of outputs, the peer IP address matches the IP address that
you configured during setup.

These include:

- SRT Caller outputs
- RTP/FEC outputs
- Zixi Push outputs
  For these output types, the peer IP is effectively static because you
  pre-configure the destination IP address. However, MediaConnect still reports these
  addresses for consistency and to provide a complete picture of your flow's
  configuration.

For other protocols (like RIST outputs and SRT Listener outputs), the peer IP
address is dynamic and shows the current address of the device that's receiving
traffic from your output.

### Important information

about peer IP addresses

###### Peer IP display and updates

- For troubleshooting purposes, MediaConnect shows the latest IP address
  information in near real-time.
- Although most updates happen quickly, it might take up to 20 seconds
  for peer IP address changes to be reflected in the console and API
  responses.
- Only the current peer IP address is displayed. Historical records
  aren't currently available.
- The peer IP address might not be visible for flows that haven't been
  started yet, or flows that were started before May 2025. In these cases,
  you might need to restart your flow to see the peer IP
  information.

###### Supported protocols and output types

- Peer IP addresses are shown for most protocols, including:
  - Pre-configured connections (like SRT Caller or Zixi Push
    outputs)
  - Dynamic connections (like RTP sources or SRT Listener)

- Peer IP addresses aren't available for:
  - Entitlements
  - Managed (MediaLive) outputs
  - CDI/ST2110 outputs
  - NDI outputs
