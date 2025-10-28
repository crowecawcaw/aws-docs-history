# Using resources with AMS Resource Scheduler

**Amazon EC2**

- Amazon EC2 instances that are part of an Auto Scaling group aren't processed individually and skipped by
  AMS Resource Scheduler, even if they are tagged.
- If the target instance root volume is encrypted with a AWS KMS customer master key (CMK), an additional `kms:CreateGrant`
  permission needs to be added to your Resource Scheduler IAM role, for the scheduler to be able to start such
  instances. This permission is not added to the role by default for improved security. If you require this permission, you can add the
  permission by updating the CloudFormation stack, `ams-resource-scheduler`, with a list of CMK as value to the `UseCMK` parameter
  (use one or more CMK Key ARNs in the format
  `arn:`partition`:kms:`region`:`account-id`:key/`key-id``
  instead of a KMS alias).
- If your Amazon EC2 instances are configured with specific software, or vendor licences managed by AWS License Manager,
  Resource Scheduler needs permissions to the specific AWS License Manager licences to be able to start the instance. You can grant
  Resource Scheduler the necessary permissions by adding the list of ARN(s) of the AWS License Manager licences to the
  License manager license for EC2 instance parameter of the CloudFormation stack (`ams-resource-scheduler`).
  **Amazon EC2 Auto Scaling**

- AMS Resource Scheduler starts or stops the auto scaling of Auto Scaling
  groups, not individual instances in the group. That is, the scheduler restores the size of the
  Auto Scaling group (start) or sets the size to 0 (stop).
- Tag Auto Scaling group with the specified tag and not the instances within the group.
- During stop, AMS Resource Scheduler stores the Auto Scaling group's
  Minimum, Desired, and Maximum capacity values and sets the Minimum and Desired Capacity
  to 0. During start, the scheduler restores the Auto Scaling group size as it was during the
  stop. Therefore, Auto Scaling group instances must use an appropriate capacity configuration
  so that the instances' termination and relaunch don't affect any application running in the Auto Scaling group.
- If the Auto Scaling group is modified (the minimum or maximum capacity)
  during a running period, the scheduler stores the new Auto Scaling group size and uses it
  when restoring the group at the end of a stop schedule.
  **Amazon RDS**

- The scheduler can take a snapshot before stopping the RDS instances (does not apply to Aurora DB cluster).
  This feature is turned on by default with the **Create RDS Instance Snapshot** AWS CloudFormation
  template parameter set to **true**. The snapshot is kept until the next time the Amazon RDS instance is stopped
  and a new snapshot is created.
- Scheduler can start/stop Amazon RDS instance that are part of a cluster or Amazon RDS Aurora database or in a multi availability zone (Multi-AZ) configuration.
  However, check Amazon RDS limitation when the scheduler won't be able to stop the Amazon RDS instance, especially Multi-AZ instances.
- To schedule Aurora Cluster for start or stop use the **Schedule Aurora Clusters** template parameter (default is **true**).
  The Aurora cluster (not the individual instances within the cluster) must be tagged with the tag key defined during initial
  configuration and the schedule name as the tag value to schedule that cluster.

###### Note

The Resource Scheduler doesn't validate that a resource is started or stopped. It makes the
API call for the relevant service and moves on. If the API call fails, it logs the error for investigation.

AMS Resource Scheduler does not support AWS Backup window. If you map an AWS Backup-enabled RDS instance with Resource Scheduler schedule,
for the backup to work as expected, the backup window must lie within the running window of the schedule.
