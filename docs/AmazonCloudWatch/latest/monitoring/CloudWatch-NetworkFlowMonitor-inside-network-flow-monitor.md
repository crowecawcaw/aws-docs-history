# How it works

This section provides information about several aspects of how Network Flow Monitor works.

**How Network Flow Monitor agents gather statistics**

Agents in Network Flow Monitor are installed on Amazon EC2 instances, where they gather performance metrics
and send them to the Network Flow Monitor backend. Agents do not have access to the payload of your TCP connections.
Agents receive only what is called the "bpf_sock_ops" structure
from the Linux kernel. This structure provides the local and remote IP address and the
source and destination TCP port, as well as counters and round-trip times. For list of the TCP statistics collected
and published by the agent, see [View Network Flow Monitor metrics in CloudWatch](CloudWatch-NetworkFlowMonitor-cw-metrics.md "CloudWatch-NetworkFlowMonitor-cw-metrics.md").

The agent uses the Network Flow Monitor `Publish` API to send metrics to the Network Flow Monitor backend server.

**How network flows are categorized in Network Flow Monitor**
Network Flow Monitor categorizes network flows into classifications depending on where
the flows originate and terminate.
