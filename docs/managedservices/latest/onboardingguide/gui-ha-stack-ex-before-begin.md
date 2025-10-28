# Before You Begin

The Deployment | Advanced Stack Components | High Availability Two Tier Stack | Create CT creates an Auto Scaling group, a load balancer, a database,
and a CodeDeploy application name and deployment group (with the same name that you give the application). For information on CodeDeploy see
[What is CodeDeploy?](../../../codedeploy/latest/userguide/welcome.md "../../../codedeploy/latest/userguide/welcome.md")

This walkthrough uses a High Availability Two-Tier Stack RFC that includes `UserData` and also describes how to create a WordPress bundle that CodeDeploy can deploy.

The `UserData` shown in the example gets instance metadata such as instance ID, region, etc,
from within a running instance by querying the EC2 instance metadata service available at http://169.254.169.254/latest/meta-data/. This line in the user data script:
`REGION=$(curl 169.254.169.254/latest/meta-data/placement/availability-zone/ | sed 's/[a-z]$//')`,
retrieves the availability zone name from the meta-data service into the $REGION variable for our supported regions,
and uses it to complete the URL for the S3 bucket where the CodeDeploy agent is downloaded. The 169.254.169.254 IP is routable only within the VPC (all VPCs can query
the service). For information about the service, see
[Instance Metadata and User Data](../../../AWSEC2/latest/UserGuide/ec2-instance-metadata.md "../../../AWSEC2/latest/UserGuide/ec2-instance-metadata.md").
Note also that scripts entered as UserData are executed as the "root" user and do not need to use the "sudo" command.

This walkthrough leaves the following parameters at the default value (shown):

- Auto Scaling group: `Cooldown=300, DesiredCapacity=2, EBSOptimized=false, HealthCheckGracePeriod=600, IAMInstanceProfile=customer-mc-ec2-instance-profile, 
InstanceDetailedMonitoring=true, InstanceRootVolumeIops=0, InstanceRootVolumeType=standard, InstanceType=m3.medium, MaxInstances=2, MinInstances=2, 
ScaleDownPolicyCooldown=300, ScaleDownPolicyEvaluationPeriods=4, ScaleDownPolicyPeriod=60, ScaleDownPolicyScalingAdjustment=-1, ScaleDownPolicyStatistic=Average, 
ScaleDownPolicyThreshold=35, ScaleMetricName=CPUUtilization, ScaleUpPolicyCooldown=60, ScaleUpPolicyEvaluationPeriods=2, ScaleUpPolicyPeriod=60, 
ScaleUpPolicyScalingAdjustment=2, ScaleUpPolicyStatistic=Average, ScaleUpPolicyThreshold=75`.
- Load Balancer: `HealthCheckInterval=30, HealthCheckTimeout=5`.
- Database: `BackupRetentionPeriod=7, Backups=true, InstanceType=db.m3.medium, IOPS=0, MultiAZ=true, PreferredBackupWindow=22:00-23:00, 
PreferredMaintenanceWindow=wed:03:32-wed:04:02, StorageEncrypted=false, StorageEncryptionKey="", StorageType=gp2`.
- Application: `DeploymentConfigName=CodeDeployDefault.OneAtATime`.
  Variable Parameters:

The Console provides an **ASAP** option for the start time and this walkthrough recommends using it. **ASAP** causes
the RFC to be executed as soon as approvals are passed.

###### Note

There are many parameters that you might choose to set differently than as shown. The values
for those parameters shown in the example have been tested but may not be right for
you. Only required values are shown in the examples. Values in
`replaceable` font should be changed as they are
particular to your account.
