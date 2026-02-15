# Troubleshooting cluster secret rotation in AWS PCS

Cluster secret rotation fails if the environment isn't properly prepared. The most common cause is active instances in your cluster. To prevent failure:

1. Set all node groups to 0 capacity.
2. Wait for nodes to stop.
3. Verify your cluster isn't in these states: `CREATE_FAILED`, `DELETE_FAILED`, `RESUMING`, `SUSPENDING`, or `SUSPENDED`.
   If rotation fails:

- A RotationFailed CloudTrail event appears
- The cluster secret remains unchanged
- Check the RotationFailed event in CloudTrail for details
- Complete all preparation steps for successful rotation
