# Telecom Charging (OCS/CHF) on AWS Outposts

Publication date: **December 15, 2022 ([Diagram history](#diagram-history "#diagram-history"))**

This architecture enables you to deploy a fully automated, resilient, low latency, and highly available Telecom Online Charging System (OCS) / Charging Function (CHF) on AWS Outposts to run in the country of (or close to) the operator core network in cases of country data residency regulations or low latency requirements.

## Telecom Charging (OCS/CHF) on AWS Outposts

Diagram

![Reference architecture diagram showing how you can use AWS services to deploy a fully automated, resilient, low latency, and highly available Telecom Online Charging System (OCS) / Charging Function (CHF) on AWS Outposts to run in the country of (or close to) the operator core network in cases of country data residency regulations or low latency requirements.](images/telecom-charging-ocs-chf-on-aws-outposts.png)

1. 4G/5G network devices connect through the Radio Access Network (RAN) to the Communication Service Provider (CSP) data center.
2. The core network integrates with the OCS/CHF on the local network through the outpost’s local gateway.
3. For resiliency and high availability, two logical **AWS Outposts** racks are installed in two different, physically isolated sites,
   and homed to different Availability Zones in the parent AWS Region.
4. A [service
   link](../../../outposts/latest/userguide/how-outposts-works.md#how-service-link "../../../outposts/latest/userguide/how-outposts-works.md#how-service-link") connects the outpost to the home AWS Region. The service link is used for
   both management of **AWS Outposts** and intra-Virtual Private
   Cloud (VPC) traffic between the AWS Region and **AWS Outposts**.
   The service link can use the customer’s existing internet connection or **AWS Direct Connect**.
5. Online charging can be deployed on **Amazon Elastic Kubernetes Service** (Amazon EKS)
   and **Amazon Elastic Compute Cloud** (Amazon EC2) instances running on **AWS Outposts**. Charging can run in active-active mode on the two
   **AWS Outposts**.
6. Vendor-supported databases run on **Amazon EC2** with near
   real-time replication to support high availability.
7. Applications that run on **AWS Outposts** can securely
   connect with other applications running in the AWS Region such as the Business Support
   System (BSS), and can use a broad set of services in the AWS Region such as **Amazon CloudWatch** and **AWS CodeCommit**.

## Download editable diagram

To customize this reference architecture diagram based on your business needs, [download the ZIP file](samples/telecom-charging-ocs-chf-on-aws-outposts.md "samples/telecom-charging-ocs-chf-on-aws-outposts.md") which contains an editable PowerPoint.

## Create a free AWS account

[![Sign up for a free AWS account](images/signup.png)](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html")

Sign up for an AWS account. New accounts include 12 months of [AWS Free Tier](https://aws.amazon.com/free/ "https://aws.amazon.com/free/") access, including the use of Amazon EC2, Amazon S3, and
Amazon DynamoDB.

## Further reading

For additional information, refer to

- [AWS Architecture
  Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture "https://aws.amazon.com/architecture")
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change              | Description                                     | Date              |
| ------------------- | ----------------------------------------------- | ----------------- |
| Initial publication | Reference architecture diagram first published. | December 15, 2022 |

###### Note

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
