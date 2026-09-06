

This is version 2.18 of the AWS Elemental Conductor File documentation. This is the latest version. For prior versions, see the *Archive* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server).

# Configuring the AWS Elemental Conductor File Node
<a name="config-cond-cf-cg"></a>

The procedures in this guide describe how to do the following:

**Important**  
Perform these steps in the order that they are presented.

1. Perform the initial cluster setup via the remote console to configure two Conductor File nodes to be able to communicate with each other, and to enable user authentication (if you want this feature): [Run the Configuration Script for AWS Elemental Conductor File](config-cond-cf-cg-script.md)

1. Enable various network features on the entire cluster. If you have two Conductor File nodes, these steps must be performed on each Conductor File node:
   + [Configure Ethernet Devices on AWS Elemental Conductor File Nodes](config-cond-cf-cg-ethernet.md)
   + [Configure DNS and NTP Servers for the Cluster](config-cond-cf-cg-servers.md)
   + [Open Ports on the Firewall for AWS Elemental Conductor File Nodes](config-cond-cf-cg-firewall.md)
   + [Add Mount Points to AWS Elemental Conductor File Nodes](config-cond-cf-cg-mount.md)

1. Enable other optional features on the entire cluster. These steps need be performed only on one Conductor File node:
   + [Work with Database Backups for AWS Elemental Conductor File](config-cond-cf-cg-bkup.md)
   + [Add Users](config-cond-cf-cg-users.md)

1. Set the heartbeat for redundancy features: [Set Failover Timing for the Cluster](config-cond-cf-cg-failover.md)

1. Enable optional Conductor File redundancy: [Configure Redundancy for AWS Elemental Conductor File Nodes](config-cond-cf-cg-redundancy.md)