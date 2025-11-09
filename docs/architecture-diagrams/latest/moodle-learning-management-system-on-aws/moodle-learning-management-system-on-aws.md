# Moodle Reference Architecture

Publication date: **August 18, 2022 ([Diagram history](#diagram-history "#diagram-history"))**

[Moodle](https://moodle.org/ "https://moodle.org/") is a learning platform designed to provide educators, administrators
and learners with a single robust, secure, and integrated system to create
personalized learning environments. Moodle learning management system (LMS) on
AWS can be deployed using architecture and can scale up on demand. Separate the
application and data layers for elasticity and security.

## Moodle Reference Architecture Diagram

![Reference architecture diagram showing how to architect the Moodle learning management system.](images/moodle-learning-management-system-on-aws.png)

1. **Amazon Route 53** offers a scalable cloud Domain Name System
   (DNS) web service. It directs students to the closest **Amazon CloudFront**
   location to access Moodle web application content while reducing latency.
2. **CloudFront** provides access to the Moodle web application
   server, which sits behind Application Load Balancer, providing low latency access to content
   while serving cached content from edge locations spread across the globe.
3. **AWS Certificate Manager** (ACM) manages secure sockets
   layer (SSL) certificates for secure, encrypted communication with public and
   private resources. It provides free SSL certificates that integrate with
   **CloudFront** or Application Load Balancer with automated certificate rotation.
4. Application Load Balancer automatically distributes incoming traffic to Moodle web application servers.
   The internet gateway provides an entry point to virtual private cloud (VPC) resources
   inside the public subnet, providing access to Application Load Balancer.
5. Network Address Translation (NAT) gateway allows outbound traffic for resources
   within a private subnet, such as Moodle App Server, that requires internet access.
6. Moodle App Server is deployed horizontally using Auto Scaling groups with
   multiple **Amazon Elastic Compute Cloud** (Amazon EC2) instances across
   multiple Availability Zones (AZs), which are deployed in a separate private
   subnet for additional security. An AWS Systems Manager Agent (SSM Agent) can
   be configured on the instances to provide SSH access without exposing an SSH port.
7. **Amazon Elastic File System** (Amazon EFS) can be used to store
   moodledata and other content, providing consistent performance,
   high availability, and durability.
8. **Amazon ElastiCache** for Redis or Amazon ElastiCache for Memcached
   stores Moodle sessions and application caches in managed clusters
   with replicas across AZs.
9. **Amazon Aurora** offers both MySQL and PostgreSQL
   compatible global scale database clusters. It provides on-demand scale of
   replica instances within minutes to handle workload spikes during peak periods.
10. **AWS CodeCommit** provides private git repositories
    to host Moodle’s PHP codebase and CI/CD configuration files. **AWS CodeBuild**
    compiles source code, runs tests, and produces software packages ready to
    deploy onto Moodle App Server. **AWS CodeDeploy** manages the
    complexity of updating applications. It can deploy into Moodle with zero downtime using
    blue-green deployment methodologies. **AWS CodePipeline**
    automates the build, test, and deploy phases for code changes.
11. **AWS Secrets Manager** protects Moodle application secrets
    and rotates secrets automatically to match lifecycle requirements.
12. **AWS Systems Manager Parameter Store** manages Moodle’s
    configuration parameters, including shared storage endpoints, databases, and
    cache configuration. This avoids the security risk associated with
    hard-coding configuration within the codebase or environment.

## Download editable diagram

To customize this reference architecture diagram based on your business needs, [download the ZIP file](samples/moodle-learning-management-system-on-aws.md "samples/moodle-learning-management-system-on-aws.md") which contains an editable PowerPoint.

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
- [Moodle website](https://moodle.org/ "https://moodle.org/")

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change              | Description                                     | Date            |
| ------------------- | ----------------------------------------------- | --------------- |
| Initial publication | Reference architecture diagram first published. | August 18, 2022 |

###### Note

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
