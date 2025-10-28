# Compute & storage

## Compute

Amazon EBS volumes are exposed as NVMe block devices on [Instances built on the Nitro System](../../../AWSEC2/latest/WindowsGuide/instance-types.md#ec2-nitro-instances "../../../AWSEC2/latest/WindowsGuide/instance-types.md#ec2-nitro-instances"). When changing Amazon EC2 instance types from a previous generation to a Nitro generation, NVMe device IDs associated with the volume can change. To avoid mount errors during change of instance type or instance reboots, you need to create a label for your file systems and mount it by the label, _and not_ the NVMe IDs. For more details, see [support article](https://aws.amazon.com/premiumsupport/knowledge-center/boot-error-linux-nitro-instance/ "https://aws.amazon.com/premiumsupport/knowledge-center/boot-error-linux-nitro-instance/").

Aside from operating system maintenance, you should consider maintenance for your Amazon EC2 instances. It can be driven by using [Creating your own runbooks](../../../systems-manager/latest/userguide/automation-documents.md "../../../systems-manager/latest/userguide/automation-documents.md"). The following are some examples.

- Use `AWS-StopEC2InstanceWithApproval` to request one or more IAM users approve the instance stop action. After the approval is received, runbook stops the instance.
- Use `AWS-StopEC2Instance` to automatically stop instances on a schedule, using CloudWatch Events or a Maintenance Window task. For example, you can configure an Automation workflow to stop instances every Friday evening and restart on Monday mornings. Note that this automation will only stop and start the Amazon EC2 instance. You must create additional document to gracefully stop and start SAP applications and database and then use the AWS Systems Manager to run such automations.
- Use `AWS-UpdateCloudFormationStackWithApproval` to update resources that were deployed using AWS CloudFormation template. The update applies a new template. You can configure the Automation to request approval by one or more IAM users before the update begins.

You can also use [AWS Instance Scheduler](https://aws.amazon.com/solutions/implementations/instance-scheduler/ "https://aws.amazon.com/solutions/implementations/instance-scheduler/") to configure custom start and stop schedules for Amazon EC2 and Amazon RDS instances.

## Storage

The following are the storage services used across this guide.

- Amazon EBS provides persistent storage for SAP applications and database. Amazon EBS volumes can be resized and even have the volume type changed without disrupting the applications. For more details, see [Amazon EBS Elastic Volumes](../../../AWSEC2/latest/UserGuide/ebs-modify-volume.md "../../../AWSEC2/latest/UserGuide/ebs-modify-volume.md"). After modifying the Amazon EBS volume, you need to extend the file system to match the extended volume size. For more details, see [Extend a Linux file system after resizing a volume](../../../AWSEC2/latest/UserGuide/recognize-expanded-volume-linux.md "../../../AWSEC2/latest/UserGuide/recognize-expanded-volume-linux.md").
- Amazon EFS does not require you to explicitly provision storage, you pay only for your usage. It is built to scale on demand, without disrupting applications, growing and shrinking automatically as you add and remove files. This ensures that your applications have the required storage.
- Amazon S3 also does not require you to explicitly provision storage, you pay only for your usage. You can use Object lifecycle management to set rules that define when objects are transitioned or archived to colder storage (Amazon S3 IA or S3 Glacier) and when they expire. For more information, see [Managing your storage lifecycle](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md").
