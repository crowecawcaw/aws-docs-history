

# Rotate a cluster secret in AWS PCS
<a name="cluster-secret-rotation-procedure"></a>

Rotate your cluster secret to comply with security requirements and address potential compromises. This process requires putting your cluster into maintenance mode.

**Note**  
By default, AWS PCS encrypts the cluster secret with an AWS managed key. If you encrypt it with a customer managed key instead, make sure the key policy grants the AWS PCS service-linked role access to the key. Otherwise, AWS PCS can't rotate the secret. For more information, see [Use a customer managed key to encrypt the cluster secret](working-with_clusters_secrets_cmk.md).

## Prerequisites
<a name="cluster-secret-rotation-procedure-prerequisites"></a>
+ IAM role with `secretsmanager:RotateSecret` permission
+ Cluster in `ACTIVE` or `UPDATE_FAILED` state

## Procedure
<a name="cluster-secret-rotation-procedure-steps"></a>

1. Notify cluster users of the upcoming maintenance window.

1. Put the cluster into maintenance mode by scaling all compute node groups to 0 capacity.

   1. Use the UpdateComputeNodeGroup API to set both minInstanceCount and maxInstanceCount to 0 for all compute node groups.

   1. Wait until all nodes stop.

   1. (Optional) Drain scheduler queues with Slurm commands before you terminate capacity for graceful job handling.
**Note**  
Rotation requires zero running instances. If instances are still running when you start rotation, rotation fails with the following error:  

   ```
   All instances must be terminated before you rotate a secret. Set the minimum instance count to 0 to terminate active instances.
   ```
**Note**  
A compute node group can report `ACTIVE` while instances are still terminating during scale-down. It can also report `ACTIVE` before any instance exists during scale-up. Scaling can take several minutes, up to about 30 minutes. While a compute node group is `UPDATING`, `get-compute-node-group` returns the pre-update scaling values, and AWS PCS refuses further update requests until the update completes. Don't treat `ACTIVE` as confirmation that instances exist.

1. Initiate rotation through Secrets Manager.
   + **Console method**:

     1. Navigate to Secrets Manager, select your cluster secret, and choose **Rotate secret**.
   + **API method**:

     1. Use Secrets Manager `rotate-secret` API.

1. Confirm that rotation succeeded.
**Note**  
The `rotate-secret` call returns HTTP 200 even if rotation later fails. The outcome arrives later, as a separate `RotationFailed` or `RotationSucceeded` event. The 200 response only confirms that AWS PCS accepted the request, not that rotation succeeded.

   1. Run `describe-secret` and confirm that the `AWSCURRENT` staging label moved to the new version and that `lastRotatedDate` updated.

   1. Alternatively, wait for a `RotationSucceeded` event in AWS CloudTrail.
**Note**  
Use `describe-secret` rather than `list-secret-version-ids` to inspect versions. `list-secret-version-ids` can omit the `AWSPENDING` version even when you specify `--include-deprecated`.

1. After successful rotation, restore cluster capacity.

   1. Use the UpdateComputeNodeGroup API to reset node groups to desired min/max capacity.

   1. For AWS PCS-managed login nodes: No additional action required.

   1. For BYO login nodes:

      1. Connect to login nodes.

      1. Update `/etc/slurm/slurm.key` with the new secret from Secrets Manager.

      1. Restart the Slurm Auth and Cred Kiosk Daemon (sackd).

## Recover from a stranded pending version
<a name="cluster-secret-rotation-procedure-recover-pending"></a>

A failed rotation can strand a version at the `AWSPENDING` staging label and block later rotations with the following error:

```
A previous rotation isn't complete. That rotation will be reattempted.
```

The `cancel-rotate-secret` command alone doesn't remove the `AWSPENDING` staging label, and it sets `RotationEnabled` to `false`. To clear the stranded version, remove the `AWSPENDING` staging label from the pending version:

```
aws secretsmanager update-secret-version-stage \
    --secret-id {{secret-arn}} \
    --version-stage AWSPENDING \
    --remove-from-version-id {{pending-version-id}}
```

## Verify the rotation
<a name="cluster-secret-rotation-procedure-verify"></a>

To confirm that the Slurm controller is reachable and that nodes are healthy, use `scontrol ping` and `scontrol show nodes`. Don't use `sinfo` to check a cluster that has no queues, because `sinfo` shows nothing in that case and isn't a valid check.

To confirm that nodes use the current key, compare the SHA-256 hash of the base64-decoded `AWSCURRENT` secret with the hash of `/etc/slurm/slurm.key` on the nodes:

```
sha256sum /etc/slurm/slurm.key
```

Compare the node hash against the `AWSPREVIOUS` version as well to prove that nodes aren't on a stale key. We recommend that you compare hashes rather than print key material.