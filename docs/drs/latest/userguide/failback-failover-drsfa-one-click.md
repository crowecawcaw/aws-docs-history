

# One-click failback
<a name="failback-failover-drsfa-one-click"></a>

After the client connects and completes verification, the main menu displays:

```
What would you like to do?
1. One-Click Failback
2. Custom Failback
3. Generate a default failback configuration file
4. Find servers in vCenter
5. Exit
```

Select **1** for One-Click Failback.

1. Enter a custom prefix for the results output file.

1. If failback replication has already started for some Recovery instances, the client prompts you to skip those instances or restart replication for them.

1. The client lists the Recovery instances in your AWS account. Enter **Y** to continue.

1. The client initiates failback. Monitor progress on the **Recovery instances** page in the DRS console.

## Failback results
<a name="failback-failover-drsfa-results"></a>

After the failback completes, the client displays a summary showing how many servers succeeded and how many failed.

The full results are exported as a JSON file to `/drs_failback_automation_client/results/Failback` with the naming convention: `{prefix}_{account_id}_{region}_{timestamp}.json`

The JSON file contains the following fields for each server:
+ The AWS ID of the Recovery instance
+ The status of the failback (succeeded, skipped, or failed)
+ A message (provides the cause for failure if applicable)
+ The vCenter VM UUID
+ The vCenter UUID of the original source server

If failback failed for any machines, review the `failback_hosts_settings.json` file in the same folder to see the exact configuration used. Fix any problems and use the custom failback flow to retry those specific machines.