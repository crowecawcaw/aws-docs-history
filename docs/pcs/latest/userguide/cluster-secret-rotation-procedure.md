# Rotate a cluster secret in AWS PCS

Rotate your cluster secret to comply with security requirements and address potential compromises. This process requires putting your cluster into maintenance mode.

## Prerequisites

- IAM role with `secretsmanager:RotateSecret` permission
- Cluster in `ACTIVE` or `UPDATE_FAILED` state

## Procedure

1. Notify cluster users of the upcoming maintenance window.
2. Put the cluster into maintenance mode by scaling all compute node groups to 0 capacity.
   1. Use the UpdateComputeNodeGroup API to set both minInstanceCount and maxInstanceCount to 0 for all compute node groups.
   2. Wait until all nodes stop.
   3. Optional: Drain scheduler queues with Slurm commands before you terminate capacity for graceful job handling.

3. Initiate rotation through Secrets Manager.
   - **Console method**:
     1. Navigate to Secrets Manager, select your cluster secret, and choose **Rotate secret**.

   - **API method**:
     1. Use Secrets Manager `rotate-secret` API.

4. Monitor rotation progress.
   1. Track progress through CloudTrail events.
   2. Check `lastRotatedDate` through either the Secrets Manager console or the `secretsmanager:describeSecret` API.
   3. Wait for `RotationSucceeded` or `RotationFailed` CloudTrail event.

5. After successful rotation, restore cluster capacity.
   1. Use the UpdateComputeNodeGroup API to reset node groups to desired min/max capacity.
   2. For AWS PCS-managed login nodes: No additional action required.
   3. For BYO login nodes:
      1. Connect to login nodes.
      2. Update `/etc/slurm/slurm.key` with the new secret from Secrets Manager.
      3. Restart the Slurm Auth and Cred Kiosk Daemon (sackd).
