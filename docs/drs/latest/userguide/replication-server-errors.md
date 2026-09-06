

# Replication infrastructure errors
<a name="replication-server-errors"></a>

This topic covers errors related to the replication server infrastructure, including launching, booting, disk operations, and firewall rules. Each section describes the error message, cause, and resolution.

**Topics**
+ [Error: Failed to launch replication server](#common-failed-launch-replication-server)
+ [Error: Failed to boot replication server](#common-failed-boot-replication-server)
+ [Error: Failed to create staging disks](#common-failed-create-staging-disks)
+ [Error: Failed to attach staging disks](#common-failed-attach-staging-disks)
+ [Error: Failed to create firewall rules](#common-failed-create-firewall)
+ [Error: Failed to start data transfer](#common-failed-start-data-transfer)
+ [Error: Snapshot failure](#common-snapshot-failure)

## Error: Failed to launch replication server
<a name="common-failed-launch-replication-server"></a>

**Error message:** `FAILED_TO_LAUNCH_REPLICATION_SERVER`

**Cause:** Elastic Disaster Recovery was unable to launch a replication server in the staging area. Common causes include Amazon EC2 instance limits, IAM permissions, or subnet capacity.

**Resolution:**

------
#### [ Console ]
+ Check the staging area subnet and instance type in replication settings.
+ Check Amazon EC2 Service Quotas for the instance type.
+ Verify IAM prerequisites are met.

------
#### [ CLI ]

Run the following command to check the instance type and subnet configured for replication:

```
aws drs get-replication-configuration \
    --source-server-id {{SOURCE_SERVER_ID}}
```

Run the following command to check the Amazon EC2 running instances quota:

```
aws service-quotas get-service-quota \
    --service-code ec2 \
    --quota-code L-1216C47A
```

Compare the quota value against the number of running instances in the staging area.

------

## Error: Failed to boot replication server
<a name="common-failed-boot-replication-server"></a>

**Error message:** `FAILED_TO_BOOT_REPLICATION_SERVER`

**Cause:** The replication server was launched but failed to boot. This is usually a staging area network issue that prevents the server from reaching Elastic Disaster Recovery endpoints during startup.

**Resolution:**
+ Verify the staging area subnet has outbound TCP 443 access to the Elastic Disaster Recovery endpoint.
+ Check the security group and network ACL associated with the staging area subnet.
+ If the issue persists, contact AWS Support.

## Error: Failed to create staging disks
<a name="common-failed-create-staging-disks"></a>

**Error message:** `Failed to create staging disks`

**Cause:** The AWS account might be configured to encrypt EBS volumes by default, and the IAM user or role lacks permissions to use the selected KMS key.

**Resolution:**
+ Verify IAM prerequisites are met.
+ If using default EBS encryption, ensure Elastic Disaster Recovery service roles have permissions on the KMS key (`kms:CreateGrant`, `kms:DescribeKey`).
+ Check EBS volume limits in the staging area Region.

## Error: Failed to attach staging disks
<a name="common-failed-attach-staging-disks"></a>

**Error message:** `FAILED_TO_ATTACH_STAGING_DISKS`

**Cause:** Elastic Disaster Recovery could not attach staging disks to the replication server. This can be caused by IAM permission issues or EBS volume attachment limits.

**Resolution:**
+ Verify IAM permissions for Amazon EC2 volume operations.
+ Check EBS volume attachment limits in the staging area Region.
+ If the issue persists, contact AWS Support.

## Error: Failed to create firewall rules
<a name="common-failed-create-firewall"></a>

**Error message:** `Firewall rules creation failed`

**Cause:** Elastic Disaster Recovery could not configure security group rules for the replication server. This can be caused by missing IAM permissions or invalid replication settings.

**Resolution:**
+ Verify IAM permission prerequisites.
+ Review the replication settings of the associated source server.
+ Ensure the security group specified in replication settings exists and is in the correct VPC.

## Error: Failed to start data transfer
<a name="common-failed-start-data-transfer"></a>

**Error message:** `FAILED_TO_START_DATA_TRANSFER`

**Cause:** The agent and replication server were paired but data transfer could not begin. This is usually a network throughput or connectivity issue.

**Resolution:**
+ Check network connectivity and bandwidth between the source server and the replication server.
+ Check replication agent logs for details. For more information, see [Agent logs](agent-diagnostics.md#agent-log-locations).
+ If the issue persists, contact AWS Support.

## Error: Snapshot failure
<a name="common-snapshot-failure"></a>

**Error message:** `SNAPSHOTS_FAILURE`

**Cause:** Elastic Disaster Recovery is unable to take a consistent snapshot. Common causes include inadequate IAM permissions or API throttling.

**Resolution:**
+ Verify IAM permissions and ensure required roles are correctly configured.
+ Check if you have activated throttling. For more information, see [route control](data-routing.md#route-control).
+ Check CloudTrail logs for throttling errors.