# Determining a source's peer IP address

A source peer IP address shows which device is currently sending content to your flow.
This information is valuable for troubleshooting and monitoring, as it helps you to
diagnose connectivity issues on your own without having to contact AWS support.

For example, you can use the source peer IP address to do the following:

- Verify that the expected source is connected
- Troubleshoot connection issues
- Monitor security by ensuring content is coming from expected IPs

## Finding a source’s peer IP

address

You can view the current peer IP address for each of your flow sources in the
MediaConnect console, or by using the [DescribeFlow](../api/API_DescribeFlow.md "../api/API_DescribeFlow.md") API
operation.

###### To determine a source’s peer IP address

1. On the **Flows** page, choose the name of the flow that
   you want to view.
2. Choose the **Sources** tab.
3. Select the source that you want to view, and then choose
   **Details**.
4. Under **Peer IP Address**, note the peer IP
   address.

###### Note

For SRT caller sources, the peer IP address matches the IP address that you
configured during setup. This is because MediaConnect initiates the connection
to this pre-defined IP address. MediaConnect reports this address to provide a
complete picture of your flow's configuration.

For protocols with dynamic peers (like RTP sources, RIST sources, and SRT
listener sources), the peer IP address reflects the current state of the flow,
showing the address of the device currently sending traffic to your
source.

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

###### Supported protocols and source types

- Peer IP addresses are shown for most protocols, including both
  pre-configured and dynamic connections
- Peer IP addresses aren't available for:
  - Entitlements
  - CDI/ST2110 sources
