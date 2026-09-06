

# Moodle for High Availability on AWS
<a name="moodle-for-high-availability-on-aws"></a>

Publication date: **December 22, 2021 ([Diagram history](#diagram-history))**

Moodle is an open source learning management system (LMS) that supports distributed online learning. When implemented on AWS, Moodle can scale flexibly to optimize cost and maximize availability. We recommend separation of the application and database layers to enable autoscaling for elasticity. Instructors and students can focus on teaching and learning, and organizations can reduce administrative overhead by building a highly available Moodle architecture on AWS.

## Moodle for High Availability on AWS Diagram
<a name="diagram1"></a>

![Reference architecture diagram showing you how to implement Moodle on AWS.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/moodle-for-high-availability-on-aws/images/moodle-for-high-availability-on-aws.png)


1. **Amazon Route 53** provides highly available routing policies and directs students to the closest **Amazon CloudFront** locations to access static content, reducing latency.

1. Use **AWS Certificate Manager** to manage your SSL certificates for secure communication with public and private resources.

1. The public **Application Load Balancer** scales automatically with your student traffic and keeps in-flight student data secure with HTTPS and SSL termination.

1. The **NAT gateway** provides a pathway to external entities and platforms should that be required.

1. Run the Moodle platform application layer on **Amazon Elastic Container Service** (Amazon ECS), leveraging **AWS Fargate**, the serverless compute engine for containers. **Fargate** removes the need to provision and manage servers, lets you specify and pay for resources per application, and improves security through application isolation by design.

1. **Amazon ElastiCache** allows you to set up, run, and scale popular open-source compatible in-memory data stores in the cloud. Use multi-AZ **ElastiCache** in your Moodle architecture to provide automated disaster recovery.

1. **Amazon Elastic File System** (Amazon EFS) provides a serverless, set-and-forget, elastic file system that lets you share file data without provisioning or managing storage.

1. **Amazon Aurora** provides a MySQL or PostgreSQL compatible solution for Moodle relational database workloads.

1.  **AWS Secrets Manager** helps you protect secrets needed to access your applications, services, and IT resources.

1. **Amazon Elastic Container Registry** (ECR) is a fully managed container registry that makes it easy to store, manage, share, and deploy your container images and artifacts anywhere.

## Further reading
<a name="further-reading"></a>

 For additional information, refer to 
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | December 22, 2021 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.