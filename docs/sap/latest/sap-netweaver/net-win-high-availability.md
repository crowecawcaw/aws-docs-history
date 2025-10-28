# High Availability

After your HA cluster is deployed and configured successfully on AWS, the operation of the HA software still follows the third-party software interface. This can be best understood by following the operational guides from the respective vendors.

It’s also important to have a test environment available (often called a staging or pre-production environment) that has an identical cluster configuration to your production environment. This environment can be used to test any configuration changes to the cluster before deploying the changes to production.

Two key AWS features that support the cluster software are:

- Amazon FSx for shared storage: See the storage section for maintenance considerations for Amazon FSx. For Multi-AZ deployments, DFS replication is required across multiple filesystems so ensure that you monitor the replication.
- Overlay IP for IP failover
  - Ensure that IAM authorizations are in place to minimize update access to the route table so that only the cluster agent can edit it.
  - Ensure that the route table configuration is coupled with your change management process so that any wider environment updates that might affect this feature are captured and can therefore be tested.
