# Customizing AMS Resource Scheduler

When onboarded, AMS Resource Scheduler is deployed as a CloudFormation stack, with name `ams-resource-scheduler`, in the
primary AWS region for your AMS Accelerate account. You can configure the properties of AMS Resource Scheduler based on your preferences
through CloudFormation stack parameters and performing a stack update. For information on updating CloudFormation stacks, see
[Updating stacks directly](../../../AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-direct.md "../../../AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-direct.md").

We recommend you customize the following properties and leave the rest at default for optimal functionality.

- **Tag name**: The name of the tag that Resource Scheduler will use to associate instance schedules with resources.
  The default value is `Schedule`.
- **Service(s) to schedule**: A comma-separated list of services that Resource Scheduler can manage. The default value
  is "`ec2,rds,autoscaling`". Valid values are "ec2", "rds" and "autoscaling".
- **Default time zone**:Specify the default time zone for the Resource Scheduler to use. The default value is
  `UTC`.
- **CMK for encrypted EBS volumes**: A comma-separated list of Amazon KMS Customer Managed Key (CMK) ARNs that
  Resource Scheduler can be granted permissions to.
- **License manager license for EC2 instance**: A comma-separated list of AWS Licence Manager ARNs to that
  Resource Scheduler can be granted permissions to.

###### Note

AMS occasionally releases features and fixes to keep AMS Resource Scheduler up to date in your account.
When this happens, any customization that you make to the AMS Resource Scheduler stack via stack parameters are preserved.

We strongly recommend against making any customization directly to any of the component resource of AMS Resource Scheduler.
Doing so impacts Resource Scheduler functionality and AMS’s ability to keep it up to date.
