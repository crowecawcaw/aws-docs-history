

# EDA on AWS with IBM Spectrum LSF
<a name="eda-ibm-spectrum-lsf"></a>

Publication date: **February 18, 2021 ([Diagram history](#lsf-history))**

With this architecture, you can run Electronic Design Automation (EDA) workloads on AWS by using IBM Spectrum LSF Resource Connector. The solution dynamically provisions [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/) instances to satisfy workload in the queue and terminates them after jobs finish.

For more information about this workshop, see [aws-eda-workshops](https://github.com/aws-samples/aws-eda-workshops/blob/master/workshops/eda-workshop-lsf) on GitHub.

## EDA on AWS with IBM Spectrum LSF diagram
<a name="lsf-diagram"></a>

![Reference architecture diagram showing how to run EDA workloads on AWS with IBM Spectrum LSF Resource Connector, Amazon EC2, and Amazon EFS.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/eda-ibm-spectrum-lsf/images/eda-ibm-spectrum-lsf.png)


The following steps describe the data flow and job execution for this architecture:

1. Log in to the login server from within the corporate network.

1. Submit simulation jobs from the login server.

1. IBM Spectrum LSF provisions Amazon EC2 instances to satisfy the workload in the queue.

1. Provisioned Amazon EC2 instances join the cluster as dynamic execution hosts.

1. Dispatch jobs to the new execution hosts.

1. Load the pre-licensed Xilinx Vivado Design Suite from the FPGA Developer AMI on each job execution host.

1. Vivado loads example IP and design from `/ec2-nfs/proj`.

1. Vivado writes job runtime data and results to `/ec2-nfs/scratch`.

1. IBM Spectrum LSF terminates Amazon EC2 instances after jobs finish.

1. Read and write IBM Spectrum LSF binaries, configuration, and logs to [Amazon Elastic File System](https://docs.aws.amazon.com/efs/latest/ug/).

## Further reading
<a name="lsf-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="lsf-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#lsf-history) | Reference architecture diagram first published. | February 18, 2021 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.