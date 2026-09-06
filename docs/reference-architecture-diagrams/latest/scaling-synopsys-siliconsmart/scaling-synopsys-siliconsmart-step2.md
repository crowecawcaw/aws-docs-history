

# Scaling Synopsys SiliconSmart on AWS: Scale out to multiple clusters
<a name="scaling-synopsys-siliconsmart-step2"></a>

Publication date: **April 1, 2021 ([Diagram history](#ss-step2-history))**

With this architecture, you can scale the previous Scale-Out Computing on AWS deployment to multiple clusters and Availability Zones. Limit total SiliconSmart jobs to fewer than 40,000 for each scheduler instance and keep each cluster within the same Availability Zone.

## Step 2: Scale out to multiple clusters diagram
<a name="ss-step2-diagram"></a>

![Reference architecture diagram showing step 2 of scaling Synopsys SiliconSmart by deploying multiple clusters across Availability Zones with FSx for Lustre and Amazon EC2 Spot Fleet.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/scaling-synopsys-siliconsmart/images/scaling-synopsys-siliconsmart-2.png)


The following steps describe the scale-out configuration for this architecture:

1. Limit total SiliconSmart jobs to fewer than 40,000 for each scheduler instance. Keep each cluster within the same Availability Zone.

1. Add 1 communication instance for every 1,000 compute instances. See Step 3 for tuning details.

1. Create an [FSx for Lustre](https://docs.aws.amazon.com/fsx/latest/LustreGuide/) file system for each cluster in each Availability Zone. Move the data needed to run your jobs.

1. Launch a license server in each Availability Zone to reduce or eliminate inter-Availability Zone traffic.

1. Use the scheduler instance to launch SiliconSmart coordinators through an AWS Auto Scaling group. Scale to 50 or more coordinators.

1. Launch [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/) instances in the compute fleet to meet the cores required by the coordinators.

1. Each coordinator invokes 500 to 2,000 job submissions by using `qsub` commands. Jobs then run on the compute fleet.

## Further reading
<a name="ss-step2-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="ss-step2-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](scaling-synopsys-siliconsmart-step1.md#ss-step1-history) | Reference architecture diagram first published. | April 1, 2021 | 
| [Initial publication](#ss-step2-history) | Reference architecture diagram first published. | April 1, 2021 | 
| [Initial publication](scaling-synopsys-siliconsmart-step3.md#ss-step3-history) | Reference architecture diagram first published. | April 1, 2021 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.