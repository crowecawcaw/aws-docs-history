# Initialize Network Flow Monitor

Before you can view performance metrics for network flows, you must initialize Network Flow Monitor, which grants
required permissions and creates an initial topology for your account or accounts. If you plan to monitor
resources for multiple accounts, you must also configure AWS Organizations with Amazon CloudWatch. Then,
you specify accounts for your Network Flow Monitor scope, so that Network Flow Monitor can create an initial topology for all
the accounts that you'll be tracking performance metrics for.

In addition, you must install agents on your instances,
to send performance metrics to the Network Flow Monitor backup ingestion server. For more information,
see [Install Network Flow Monitor agents on EC2 and self-managed Kubernetes instances](CloudWatch-NetworkFlowMonitor-agents.md "CloudWatch-NetworkFlowMonitor-agents.md").

The steps that you take to initialize Network Flow Monitor vary depending on whether you are measuring performance
metrics for resources in a single account, or you want to monitor metrics from resources that are owned by multiple
accounts in your organization.

- [Single account monitoring initialization](CloudWatch-NetworkFlowMonitor-single-account.md "CloudWatch-NetworkFlowMonitor-single-account.md")
- [Multi-account monitoring initialization](CloudWatch-NetworkFlowMonitor-multi-account.md "CloudWatch-NetworkFlowMonitor-multi-account.md")

## Install agents on instances

To track network performance with Network Flow Monitor, you must initialize the service, but you
must also install Network Flow Monitor agents on your workload's EC2 instances and add permissions for
the agents to send networking performance metrics to Network Flow Monitor. After you install the
agents, wait a short period of time (about 20 minutes), for data to begin being sent
to the Network Flow Monitor backend. Then, you can view network
performance metrics, on the **Workload insights** tab, and also
create monitors, to view detailed information.

For example, you can view the top contributor performance metrics for data transferred
and retransmission timeouts, for network flows between your local and
remote resources, collected by Network Flow Monitor agents. By viewing and analyzing these metrics, you
can choose specific flows that you want to see more details for and track more closely with
a monitor. By creating a monitor for specific flows, you can see detailed information
about them, including metrics, sorted by the top contributors for each metric type
and network paths for each network flow.

With a monitor, Network Flow Monitor also provides a network health indicator (NHI), which
you can use to see if there have been AWS network impairments for network flows that you're
tracking in the monitor, during a time period that you've selected. That information
can help you decide where to focus your network troubleshooting efforts.

For more information, and instructions for how to install agents,
see [Install Network Flow Monitor agents on EC2 and self-managed Kubernetes instances](CloudWatch-NetworkFlowMonitor-agents.md "CloudWatch-NetworkFlowMonitor-agents.md").
