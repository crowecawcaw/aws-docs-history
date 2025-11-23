# AMS Resource Scheduler best practices

**Scheduling Amazon EC2 Instances**

- Instance shut down behavior must be set to `stop` and not
  to `terminate`. This is pre-set to `stop` for instances that
  are created with the AMS Amazon EC2 Create automated change type (ct-14027q0sjyt1h) and
  can be set for Amazon EC2 instances created with AWS CloudFormation ingestion, by setting the
  `InstanceInitiatedShutdownBehavior` property to `stop`. If
  instances have shut down behavior set to `terminate`, then the instances
  will end when the Resource Scheduler stops them and the scheduler won't be able to start them back up.
- Amazon EC2 instances that are part of an Auto Scaling group aren't processed
  individually by AMS Resource Scheduler, even if they are tagged.
- If the target instance root volume is encrypted with a KMS customer master key (CMK), an
  additional `kms:CreateGrant` permission needs to be added to your
  Resource Scheduler IAM role, for the scheduler to be able to start such
  instances. This permission is not added to the role by default for improved
  security. If you require this permission, submit an RFC with the Management | AMS Resource Scheduler | Solution | Update change type,
  and specify a comma separated list of ARNs of the KMS CMKs.
  **Scheduling Auto Scaling groups**

- AMS Resource Scheduler starts or stops the auto scaling of Auto Scaling
  groups, not individual instances in the group. That is, the scheduler restores the size of the
  Auto Scaling group (start) or sets the size to 0 (stop).
- Tag AutoScaling group with the specified tag and not the instances within the
  group.
- During stop, AMS Resource Scheduler stores the Auto Scaling group's
  Minimum, Desired, and Maximum capacity values and sets the Minimum and Desired Capacity
  to 0. During start, the scheduler restores the Auto Scaling group size as it was during the
  stop. Therefore, Auto Scaling group instances must use an appropriate capacity configuration
  so that the instances' termination and relaunch don't affect any application running in the Auto
  Scaling group.
- If the Auto Scaling group is modified (the minimum or maximum capacity)
  during a running period, the scheduler stores the new Auto Scaling group size and uses it
  when restoring the group at the end of a stop schedule.
  **Scheduling Amazon RDS instances**

- The scheduler can take a snapshot before stopping the RDS instances (does not apply to Aurora DB cluster).
  This feature is turned on by default with the **Create RDS Instance Snapshot** CloudFormation template parameter set to **true**.
  The snapshot is kept until the next time the Amazon RDS instance is stopped and a new snapshot is created.

Scheduler can start/stop Amazon RDS instance that are part of a cluster or Amazon RDS Aurora database or in a multi availability zone (Multi-AZ) configuration.
However, check Amazon RDS limitation when the scheduler won't be able to stop the Amazon RDS instance, especially Multi-AZ instances.
To schedule Aurora Cluster for start or stop use the **Schedule Aurora Clusters** template
parameter (default is **true**). The Aurora cluster
(not the individual instances within the cluster) must be tagged with the tag key defined during initial
configuration and the schedule name as the tag value to schedule that cluster.

Every Amazon RDS instance has a weekly maintenance window during which any system changes are applied.
During the maintenance window, Amazon RDS will automatically start instances that have been stopped for more than
seven days to apply maintenance. Note that Amazon RDS will not stop the instance once the maintenance event is complete.

The scheduler allows specifying whether to add the preferred maintenance window of an Amazon RDS instance
as a running period to its schedule. The solution will start the instance at the beginning of the maintenance
window and stop the instance at the end of the maintenance window if no other running period specifies that
the instance should run, and if the maintenance event is completed.

If the maintenance event is not completed by the end of the maintenance window, the instance will run until
the scheduling interval after the maintenance event is completed.

###### Note

The Scheduler doesn't validate that a resource is started or stopped. It makes the
API call and moves on. If the API call fails, it logs the error for investigation.
