

# Moodle for high availability on AWS

Publication date: **December 22, 2021 ([Diagram history](diagram-history.md))**

Moodle is an open source learning management system (LMS) that supports distributed online learning. When implemented on AWS, Moodle can scale flexibly to optimize cost and maximize availability. We recommend separation of the application and database layers to enable autoscaling for elasticity. Instructors and students can focus on teaching and learning, and organizations can reduce administrative overhead by building a highly available Moodle architecture on AWS.

## Moodle for high availability on AWS diagram
<a name="moodle-for-high-availability-on-aws-diagram"></a>

![Moodle runs on Amazon ECS with Fargate, using Aurora, ElastiCache, and Amazon EFS across multiple Availability Zones.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/education/images/moodle-for-high-availability-on-aws.png)


The following steps describe the architecture:

1. [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/) provides highly available routing policies and directs students to the closest [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/) locations to access static content, reducing latency.

1. Use [AWS Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/) to manage your SSL certificates for secure communication with public and private resources.

1. The public [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/) scales automatically with your student traffic and keeps in-flight student data secure with HTTPS and SSL termination.

1. The NAT gateway provides a pathway to external entities and platforms should that be required.

1. Run the Moodle platform application layer on [Amazon Elastic Container Service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/) (Amazon ECS), using [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html), the serverless compute engine for containers. Fargate removes the need to provision and manage servers, lets you specify and pay for resources per application, and improves security through application isolation by design.

1. [Amazon ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/) allows you to set up, run, and scale popular open-source compatible in-memory data stores in the cloud. Use multi-AZ ElastiCache in your Moodle architecture to provide automated disaster recovery.

1. [Amazon Elastic File System](https://docs.aws.amazon.com/efs/latest/ug/) (Amazon EFS) provides a serverless, set-and-forget, elastic file system that lets you share file data without provisioning or managing storage.

1. [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/) provides a MySQL or PostgreSQL compatible solution for Moodle relational database workloads.

1.  [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/) helps you protect secrets needed to access your applications, services, and IT resources.

1. [Amazon Elastic Container Registry](https://docs.aws.amazon.com/AmazonECR/latest/userguide/) (Amazon ECR) is a fully managed container registry that makes it easy to store, manage, share, and deploy your container images and artifacts anywhere.

## Further reading
<a name="moodle-for-high-availability-on-aws-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 