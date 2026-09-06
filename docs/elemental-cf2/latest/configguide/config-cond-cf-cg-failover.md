

This is version 2.18 of the AWS Elemental Conductor File documentation. This is the latest version. For prior versions, see the *Archive* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server).

# Set Failover Timing for the Cluster
<a name="config-cond-cf-cg-failover"></a>

This section describes how to set the timeout rate for failover.

To set up failover timings for the entire cluster, you need to perform this setup only on the Conductor node. If you have two Conductor nodes, you need to perform this setup only on the primary Conductor node. 

**To set failover timing**

1. Hover over **Configuration** (cog icon) on the main menu and choose **Authentication** from the drop-down menu.

1. On the Conductor Configuration screen, choose **Failover**.

1. On the Failover screen, complete the fields and choose **Save**.

The fields have the following implications on worker and Conductor nodes.

**Worker Nodes**  
The primary Conductor node expects to receive a heartbeat from each worker node according to the frequency specified in **Heartbeat Frequency**. If it does not receive a heartbeat for more than the seconds specified in **Failover Threshold**, then the Conductor considers the worker node to have failed. 

The Conductor node flags the worker node as failed. 

**Conductor Nodes**  
The settings on this screen have an effect only if you have set up for Conductor redundancy.

The secondary Conductor node expects to receive a heartbeat from the primary Conductor node according to the frequency specified in **Heartbeat Frequency**. If it does not receive a heartbeat for more than the seconds specified in **Failover Threshold**, then the secondary Conductor considers the primary node to have failed. It then flags itself as the primary Conductor node and flags the other node as the secondary, and takes over control of the cluster.