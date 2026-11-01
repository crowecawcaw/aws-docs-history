

# High Performance Computing on AWS
<a name="high-performance-computing-on-aws"></a>

Publication date: **September 1, 2021 ([Diagram history](diagram-history.md))**

This architecture enables you to deploy and burst a suite of high performance computing (HPC) cases to the cloud directly from the desktop.

## High Performance Computing on AWS
<a name="high-performance-computing-on-aws-diagram1"></a>

![Reference architecture diagram showing how you can use AWS services to deploy and burst a suite of high performance computing (HPC) cases to the cloud directly from the desktop.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/electronics-hpc/images/high-performance-computing.png)


1. Users deploy HPC cases with one of the AWS SDKs or the [AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/) (AWS CLI). Users can interface directly with the cluster through NICE DCV. 

1. Data is staged both to and from AWS with [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) (Amazon S3). Amazon S3 offers low-cost, reliable storage while interfacing directly to [Amazon FSx for Lustre](https://docs.aws.amazon.com/fsx/latest/LustreGuide/) for a fully managed, high-performance storage. 

1. Serverless services manage case workflow. [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/) provides workflow management and orchestrates other services, such as serverless compute with [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/). [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/) can be used for operational management of compute clusters. 

1. [AWS ParallelCluster](https://docs.aws.amazon.com/parallelcluster/latest/ug/), [AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/), and custom-made clusters lie at the core of the HPC infrastructure, each with access to high-performance [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/) (Amazon EC2) instances connected by a high performance network with an optional Elastic Fabric Adapter. Cost optimization with Amazon EC2 is achieved with payment-model choice and environment right sizing

1. Manage applications with a consistent, versioned, and repeatable framework. AWS Developer Tools accelerate software development. Installed software can be stored in containers or snapshots, depending on the compute cluster. 

## Further reading
<a name="high-performance-computing-on-aws-further-reading"></a>

 For additional information, refer to 
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 
+  [High Performance Computing Lens — AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/welcome.html) 