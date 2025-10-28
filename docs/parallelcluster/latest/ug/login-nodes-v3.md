# Login nodes provisioned by AWS ParallelCluster

Starting from version 3.7.0, AWS ParallelCluster cluster administrators can provision login nodes that can be used to provide access to users to run jobs vs directly accessing the cluster head
node.  Cluster users with appropriate permissions can use Active Directory or their ssh credential to login, submit and manage their jobs. As a result, cluster management can be improved and the
chances of depleting the resources of the head node required by Slurm to manage the cluster can be minimized. Logged in users will also have access to all shared storage of the cluster mounted on
login nodes. If a login node needs to be stopped, users that are logged in will be notified in advance through the active shell session they are using.

Login nodes are specified as pools  where a pool defines a group of login nodes that have the same resource configuration. All the login nodes in a pool are configured to be part of a [network load balancer](../../../elasticloadbalancing/latest/network/introduction.md "../../../elasticloadbalancing/latest/network/introduction.md") that enables distributing sessions across login nodes in a round-robin fashion.
The present implementation allows users to specify multiple login node pools.
