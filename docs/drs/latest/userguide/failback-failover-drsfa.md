

# Performing a failback with the DRS Mass Failback Automation Client
<a name="failback-failover-drsfa"></a>

The DRS Mass Failback Automation Client (DRSFA client) is a command-line tool that automates the failback process for vCenter source servers. Instead of manually initiating failback for each Recovery instance individually, the DRSFA client orchestrates failback across multiple machines simultaneously — handling ISO attachment, network configuration, and replication initiation automatically.

The DRSFA client supports two failback modes:
+ **One-click failback** — Fails back all Recovery instances in your account using automatic configuration. Best for environments where the default network and device settings are acceptable.
+ **Custom failback** — Generates a configuration file that you can edit to set specific network settings, device mappings, and other parameters for each machine before initiating failback. Best for environments requiring per-machine control.

The client runs on a dedicated Ubuntu host that has network access to both your vCenter environment and AWS. It communicates with the AWS Elastic Disaster Recovery API to identify Recovery instances and with vCenter to attach ISOs and manage VMs during the failback process.

To get started, complete the following steps in order:

1. Verify that you meet the [prerequisites](failback-failover-drsfa-prereques.md).

1. [Install](failback-failover-drsfa-launching.md) the DRSFA client on your Ubuntu host.

1. [Generate IAM credentials](failback-failover-drsfa-credentials.md) for the client.

1. [Run the client](failback-failover-drsfa-running.md) and choose your failback mode.