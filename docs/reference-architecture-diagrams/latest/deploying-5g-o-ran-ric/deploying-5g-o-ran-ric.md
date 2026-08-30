# Deploying 5G O-RAN RIC on AWS

Publication date: **June 16, 2022 ([Diagram history](#ric-history "#ric-history"))**

With this architecture, you can deploy the Open Radio Access Network (O-RAN) Radio
Intelligent Controller (RIC) on AWS. The RIC optimizes control algorithms for load balancing,
mobility management, multi-connection control, quality of experience (QoE) management, and
network energy saving. The solution uses [Amazon Elastic Kubernetes Service](../../../eks/latest/userguide.md "../../../eks/latest/userguide.md") for compute and [Amazon SageMaker AI](../../../sagemaker/latest/dg.md "../../../sagemaker/latest/dg.md") for machine learning (ML) model lifecycle
operations.

## Deploying 5G O-RAN RIC on AWS diagram

![Reference architecture diagram showing how to deploy near-real-time and non-real-time O-RAN RIC on AWS by using Amazon EKS, SageMaker AI, and AWS Lake Formation.](images/deploying-5g-o-ran-ric.png)

The following steps describe the RIC components and data flow for this
architecture:

1. Use the E2 O-RAN specified Stream Control Transmission Protocol (SCTP) over Internet
   Protocol (IP) interface for near-real-time (10 ms to 1 s) data collection and control
   loops.
2. Monitor and control the Central Units (CUs) and Distributed Units (DUs) by using the
   near-real-time RIC. Persist data with NoSQL database instances by using Amazon EBS storage
   attached to Amazon EKS nodes on AWS Outposts or in AWS Local Zones.
3. Host apps on the near-real-time RIC that provide services such as QoE prediction and
   proactive, closed-loop network optimization.
4. Include SageMaker AI inference endpoints running ML models trained, updated, and deployed on
   Amazon EC2 instances by the non-real-time RIC in near-real-time and non-real-time apps.
5. Use the A1 O-RAN specified REST HTTP/TCP/IP interface to deploy policy-based guidance
   for the near-real-time RIC and to manage ML models used in RIC apps.
6. Use the O1 O-RAN REST HTTP/TCP/IP interface for non-real-time (1 s+) control loops,
   such as static Radio Resource Management (RRM) policies.
7. Provide guidance, enrichment information, and management of ML models by using the
   non-real-time control loop.
8. Store raw data, processed data, inference results, trained models, and Amazon EBS backup
   snapshots in an [Amazon Simple Storage Service](../../../AmazonS3/latest/userguide.md "../../../AmazonS3/latest/userguide.md")-backed [AWS Lake Formation](../../../lake-formation/latest/dg.md "../../../lake-formation/latest/dg.md") data lake on the non-real-time
   RIC.
9. Use SageMaker AI to develop, train, and deploy ML models used by the near-real-time and
   non-real-time apps.

## Further reading

For additional information, see the following resources:

- [AWS Architecture Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture/ "https://aws.amazon.com/architecture/")
- [AWS
  Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")

## Diagram history

To receive updates about this reference architecture diagram, subscribe to the RSS
feed.

| Change              | Description                                     | Date          |
| ------------------- | ----------------------------------------------- | ------------- |
| Initial publication | Reference architecture diagram first published. | June 16, 2022 |

###### RSS subscription requirement

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are
using.
