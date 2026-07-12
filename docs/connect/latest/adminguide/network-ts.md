# Troubleshoot your network for call quality and disconnect problems

Network issues are the number one reason for call quality and disconnect problems in
contact centers. Before reading this topic, we recommend that you review [Set up your network to use the Connect Customer Contact Control Panel (CCP)](ccp-networking.md "ccp-networking.md") to verify that your
network is set up correctly for Connect Customer.

## Get started

Make sure your environment is set up as follows:

- If a router is experiencing congestion, increase its bandwidth
  or replace it with a router that can handle the full bandwidth of your
  internet connection.
- Use fixed Ethernet (not Wi-Fi) wherever possible.
- Reduce packet conflicts on Wi-Fi by reducing the number of devices operating
  on the same channel.
- Avoid large data file transfers going over the same Wi-Fi environment
  concurrently.

## Run the Endpoint Test Utility

Run the [Endpoint Test Utility](check-connectivity-tool.md "check-connectivity-tool.md") tool
from the affected agent's computer and check the results:

- This tool helps determine the latency between your Connect Customer instance and the
  agent browser. For a successful test, the status is
  **Success**. The average latency should not exceed 300 milliseconds (ms). Latency
  above this threshold might cause audio quality issues.

The following image shows example results from a latency test.

![Endpoint Test Utility latency results showing average latency and a Success status.](images/latencytest.png)

You can also test latency by selecting different AWS Regions to test
connectivity from the agent's browser.

- Check whether the agent's workstation is set up correctly: verify they are
  using a supported browser and verify network connectivity across required
  ports for media streams. The following image shows the results for an agent
  workstation that meets all of the requirements for Connect Customer.

![Endpoint Test Utility results showing all checks passing for an agent workstation that meets all requirements.](images/endpointtestresults.png)

- Higher latency also leads to packet loss.

## Investigate network components and devices

To investigate network components and devices, check the following:

- Confirm whether the agents who are experiencing the issue are signing in
  using the same network or are signing in remotely.
- If they are using a virtual private network (VPN) or firewall, does this issue happen only on the company
  VPN or over the public internet as well?
- If there is a virtual desktop infrastructure (VDI) setup, follow recommendations in [Use Connect Customer in a VDI environment](using-ccp-vdi.md "using-ccp-vdi.md"). Were there any
  changes made? Does the issue occur in a non-VDI setup (in a simple desktop
  environment)?
- Confirm that no antivirus software on the agent's machine or in
  the agent network impacts calls or causes audio quality
  issues.
- Verify that agents do not have network connectivity or
  bandwidth issues.
- Firewalls—Firewalls, proxies, or security groups blocking required ports
  and protocols can cause audio issues, drops, and delays. Make sure UDP 3478,
  TCP 443, and web sockets are allowed.
- Network address translation (NAT) devices—NAT traversal can cause one-way or no audio if not properly
  configured. Use static NAT when possible and enable keep-alives.
- VPNs—Encrypted VPN tunnels add overhead and latency that degrade audio.
  Prioritize quality over encryption for real-time traffic.
- Wi-Fi—Wireless connections are prone to interference and congestion
  leading to jitter and packet loss. Use wired connections when
  possible.
