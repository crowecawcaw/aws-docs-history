

# Scaling Synopsys SiliconSmart on AWS
<a name="scaling-synopsys-siliconsmart"></a>

Publication date: **April 1, 2021 ([Diagram history](diagram-history.md))**

With these three architectures, you can scale Synopsys SiliconSmart characterization jobs on AWS. First, deploy the base Scale-Out Computing on AWS architecture. Next, scale out to multiple clusters across Availability Zones. Finally, tune PBS communication and the PostgreSQL database for large-scale job execution.

## Step 1: Deploy the base architecture
<a name="ss-step1-diagram"></a>

With this architecture, you can scale 100,000 or more concurrent Synopsys SiliconSmart jobs by using Scale-Out Computing on AWS. This first step deploys the base architecture by using [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/).

![Reference architecture diagram showing step 1 of scaling Synopsys SiliconSmart by deploying Scale-Out Computing on AWS with CloudFormation, Amazon EC2 Spot Fleet, and FSx for Lustre.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/electronics-hpc/images/scaling-synopsys-siliconsmart-1.png)


The following steps describe the deployment and configuration for this architecture:

1. Set up a Amazon VPC with private subnets and access from on-premises through AWS Direct Connect or AWS Site-to-Site VPN before launching Scale-Out Computing on AWS.

1. Deploy Scale-Out Computing on AWS as a baseline by using CloudFormation.

1. Enable license server access with one of two methods. Use the VM UUID (which is the AWS instance ID), or use an Elastic IP address attached to the instance.

1. Use AWS Auto Scaling groups for coordinator instances.

1. Use [Amazon EC2 Spot Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html) to launch a compute fleet for running jobs.

1. Use POSIX-compliant file systems for the Scale-Out Computing on AWS environment. Use [Amazon Elastic File System](https://docs.aws.amazon.com/efs/latest/ug/) for cluster automation, and [FSx for Lustre](https://docs.aws.amazon.com/fsx/latest/LustreGuide/) for SiliconSmart binaries and job data.

1. Move data to and from [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) by using an Amazon S3 endpoint.

1. Enable encryption for intellectual property (IP) data and multiple AWS services by using [AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/).

## Step 2: Scale out to multiple clusters
<a name="ss-step2-diagram"></a>

With this architecture, you can scale the previous Scale-Out Computing on AWS deployment to multiple clusters and Availability Zones. Limit total SiliconSmart jobs to fewer than 40,000 for each scheduler instance and keep each cluster within the same Availability Zone.

![Reference architecture diagram showing step 2 of scaling Synopsys SiliconSmart by deploying multiple clusters across Availability Zones with FSx for Lustre and Amazon EC2 Spot Fleet.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/electronics-hpc/images/scaling-synopsys-siliconsmart-2.png)


The following steps describe the scale-out configuration for this architecture:

1. Limit total SiliconSmart jobs to fewer than 40,000 for each scheduler instance. Keep each cluster within the same Availability Zone.

1. Add 1 communication instance for every 1,000 compute instances. See Step 3 for tuning details.

1. Create an [FSx for Lustre](https://docs.aws.amazon.com/fsx/latest/LustreGuide/) file system for each cluster in each Availability Zone. Move the data needed to run your jobs.

1. Launch a license server in each Availability Zone to reduce or eliminate inter-Availability Zone traffic.

1. Use the scheduler instance to launch SiliconSmart coordinators through an AWS Auto Scaling group. Scale to 50 or more coordinators.

1. Launch [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/) instances in the compute fleet to meet the cores required by the coordinators.

1. Each coordinator invokes 500 to 2,000 job submissions by using `qsub` commands. Jobs then run on the compute fleet.

## Step 3: Tune PBS communication
<a name="ss-step3-diagram"></a>

With this architecture, you can move the PBS Communication process from the PBS Scheduler to multiple communication instances. This step tunes the scheduler and database configuration for large-scale job execution.

![Reference architecture diagram showing step 3 of scaling Synopsys SiliconSmart by moving PBS communication to multiple instances and tuning PostgreSQL.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/electronics-hpc/images/scaling-synopsys-siliconsmart-3.png)


The following steps describe the PBS tuning configuration for this architecture:

1. Increase the number of threads for the `pbs_sched` process. Use the maximum processes for each scheduler instance.

1. Tune the PostgreSQL database (for example, max memory, number of connections, processes).

1. Launch communication instances (which run the `pbs_comm` process) for every 200 to 1,000 compute instances.

1. Update PBS configuration in coordinators and compute instances (in the AMI) to use multiple communication instances.

General recommendations:
+ Create AMIs for the license manager, scheduler, communication nodes, and coordinators with all software and EDA base tooling baked in. This reduces ramp-up time.
+ Reduce inter-Availability Zone traffic by keeping all components of a cluster within the same Availability Zone.
+ Monitor throughput, IOPS, and metadata server operations to optimize file system performance.

## Further reading
<a name="ss-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 