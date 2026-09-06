

# Scaling Synopsys SiliconSmart on AWS: Deploy base architecture
<a name="scaling-synopsys-siliconsmart-step1"></a>

Publication date: **April 1, 2021 ([Diagram history](#ss-step1-history))**

With this architecture, you can scale 100,000 or more concurrent Synopsys SiliconSmart jobs by using Scale-Out Computing on AWS. This first step deploys the base architecture by using [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/).

## Step 1: Deploy the base architecture diagram
<a name="ss-step1-diagram"></a>

![Reference architecture diagram showing step 1 of scaling Synopsys SiliconSmart by deploying Scale-Out Computing on AWS with CloudFormation, Amazon EC2 Spot Fleet, and FSx for Lustre.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/scaling-synopsys-siliconsmart/images/scaling-synopsys-siliconsmart-1.png)


The following steps describe the deployment and configuration for this architecture:

1. Set up a Amazon VPC with private subnets and access from on-premises through AWS Direct Connect or AWS Site-to-Site VPN before launching Scale-Out Computing on AWS.

1. Deploy Scale-Out Computing on AWS as a baseline by using CloudFormation.

1. Enable license server access with one of two methods. Use the VM UUID (which is the AWS instance ID), or use an Elastic IP address attached to the instance.

1. Use AWS Auto Scaling groups for coordinator instances.

1. Use [Amazon EC2 Spot Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html) to launch a compute fleet for running jobs.

1. Use POSIX-compliant file systems for the Scale-Out Computing on AWS environment. Use [Amazon Elastic File System](https://docs.aws.amazon.com/efs/latest/ug/) for cluster automation, and [FSx for Lustre](https://docs.aws.amazon.com/fsx/latest/LustreGuide/) for SiliconSmart binaries and job data.

1. Move data to and from [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) by using an Amazon S3 endpoint.

1. Enable encryption for intellectual property (IP) data and multiple AWS services by using [AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/).

## Further reading
<a name="ss-step1-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="ss-step1-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#ss-step1-history) | Reference architecture diagram first published. | April 1, 2021 | 
| [Initial publication](scaling-synopsys-siliconsmart-step2.md#ss-step2-history) | Reference architecture diagram first published. | April 1, 2021 | 
| [Initial publication](scaling-synopsys-siliconsmart-step3.md#ss-step3-history) | Reference architecture diagram first published. | April 1, 2021 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.