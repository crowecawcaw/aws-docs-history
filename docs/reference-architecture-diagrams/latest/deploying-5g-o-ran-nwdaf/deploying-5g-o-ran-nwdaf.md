

# Deploying 5G O-RAN NWDAF on AWS
<a name="deploying-5g-o-ran-nwdaf"></a>

Publication date: **June 16, 2022 ([Diagram history](#nwdaf-history))**

With this architecture, you can implement the Network Data Analytics Function (NWDAF) on AWS to achieve observed service experience data analytics. The solution uses [Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/eks/latest/userguide/) for network functions and [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) for machine learning (ML) lifecycle operations including training and deploying inference endpoints.

## Deploying 5G O-RAN NWDAF on AWS diagram
<a name="nwdaf-diagram"></a>

![Reference architecture diagram showing how to implement NWDAF on AWS for service experience analytics by using Amazon EKS, SageMaker AI, and AWS Lake Formation.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/deploying-5g-o-ran-nwdaf/images/deploying-5g-o-ran-nwdaf.png)


The following steps describe the NWDAF components and data flow for this architecture:

1. Monitor end-user experience by using observed service experience analytics.

1. Provide Open Radio Access Network (O-RAN) standards-based network connectivity through 5G RAN and core network functions.

1. Run network functions on Amazon EKS compute with Amazon EBS storage (backed up in remote regions).

1. Send application, session, location, and quality of experience (QoE) data from network functions to the Data Collection Coordination Function (DCCF).

1. Use the DCCF to coordinate the collection and distribution of data. The DCCF prevents overlapping data subscriptions and notifications.

1. Forward or retrieve data from the Analytics Data Repository Function (ADRF) through the DCCF. The ADRF aggregates data and handles data lifecycle management.

1. Coordinate data collection and delivery through the Messaging Framework Adaptor Function (MFAF), which formats and processes data received from network functions.

1. Use SageMaker AI for ML lifecycle operations in the NWDAF Model Training Logical Function (MTLF). Train and deploy ML model inference endpoints for Analytics Logical Functions (AnLFs) to use for predictions.

1. Store processed analytics, inference results, and trained models in an [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/)-backed [AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/) data lake.

1. Compare current data values against historical, expected, and predicted Mean Opinion Score (MoS) values to derive an observed service experience analysis. Send results to Operations, Administration, and Management (OAM) services for network optimization.

## Further reading
<a name="nwdaf-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="nwdaf-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#nwdaf-history) | Reference architecture diagram first published. | June 16, 2022 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.