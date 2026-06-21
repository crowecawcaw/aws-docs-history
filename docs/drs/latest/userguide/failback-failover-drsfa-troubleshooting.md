# Troubleshooting the DRSFA Client

The following table describes common issues and resolutions when using the DRSFA
client.

| Issue                                   | Possible cause                                                                               | Resolution                                                                                                                                        |
| --------------------------------------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cannot connect to vCenter               | vCenter host is unreachable from the DRSFA client host, or the<br>specified port is blocked. | Verify network connectivity between the DRSFA client host and<br>vCenter. Confirm that the `VCENTER_PORT` (usually 443) is<br>open.               |
| Replication fails to start              | TCP port 1500 is blocked on the Recovery instance.                                           | Verify that inbound TCP port 1500 is open on the Recovery instance<br>security group in AWS.                                                      |
| Permission errors on vCenter operations | The vCenter credentials lack required permissions.                                           | Confirm that the vCenter user has all required permissions listed in<br>the prerequisites (Virtual machine and Datastore permissions).            |
| AWS API permission errors               | The IAM credentials lack the required policy.                                                | Verify that the IAM role or user includes the<br>AWSElasticDisasterRecoveryFailbackInstallationPolicy policy.                                     |
| CD-ROM attachment failures              | The VM does not have two available IDE CD-ROM slots, or the<br>datastore path is incorrect.  | Verify that the VM has available IDE controller slots. Confirm<br>that `VCENTER_FAILBACK_CLIENT_PATH` and<br>`VCENTER_SEED_ISO_PATH` are correct. |
| Replication stalls or fails             | Network connectivity issues between the source server and the<br>Recovery instance.          | Verify that the source server can reach the Recovery instance on TCP<br>port 1500. Check the `failback.log` on the source VM for<br>details.      |

## Log locations

- **DRSFA client log**:
  `drs_failback_automation_client/drs_failback_automation.log` on the
  host where the client runs.
- **Per-server failback log**:
  `failback.log` on the individual source VM being failed back.
- **CloudWatch**: If configured, logs are sent to
  the `DRS_Mass_Failback_Automation` log group.
