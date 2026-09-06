

# Moodle Reference Architecture
<a name="moodle-learning-management-system-on-aws"></a>

Publication date: **August 18, 2022 ([Diagram history](#diagram-history))**

[Moodle](https://moodle.org/) is a learning platform designed to provide educators, administrators and learners with a single robust, secure, and integrated system to create personalized learning environments. Moodle learning management system (LMS) on AWS can be deployed using architecture and can scale up on demand. Separate the application and data layers for elasticity and security.

## Moodle Reference Architecture Diagram
<a name="diagram1"></a>

![Reference architecture diagram showing how to architect the Moodle learning management system.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/moodle-learning-management-system-on-aws/images/moodle-learning-management-system-on-aws.png)


1. **Amazon Route 53** offers a scalable cloud Domain Name System (DNS) web service. It directs students to the closest **Amazon CloudFront** location to access Moodle web application content while reducing latency.

1. **CloudFront** provides access to the Moodle web application server, which sits behind Application Load Balancer, providing low latency access to content while serving cached content from edge locations spread across the globe.

1. **AWS Certificate Manager** (ACM) manages secure sockets layer (SSL) certificates for secure, encrypted communication with public and private resources. It provides free SSL certificates that integrate with **CloudFront** or Application Load Balancer with automated certificate rotation.

1.  Application Load Balancer automatically distributes incoming traffic to Moodle web application servers. The internet gateway provides an entry point to virtual private cloud (VPC) resources inside the public subnet, providing access to Application Load Balancer.

1. Network Address Translation (NAT) gateway allows outbound traffic for resources within a private subnet, such as Moodle App Server, that requires internet access.

1. Moodle App Server is deployed horizontally using Auto Scaling groups with multiple **Amazon Elastic Compute Cloud** (Amazon EC2) instances across multiple Availability Zones (AZs), which are deployed in a separate private subnet for additional security. An AWS Systems Manager Agent (SSM Agent) can be configured on the instances to provide SSH access without exposing an SSH port.

1. **Amazon Elastic File System** (Amazon EFS) can be used to store moodledata and other content, providing consistent performance, high availability, and durability.

1. **Amazon ElastiCache** for Redis or Amazon ElastiCache for Memcached stores Moodle sessions and application caches in managed clusters with replicas across AZs.

1. **Amazon Aurora** offers both MySQL and PostgreSQL compatible global scale database clusters. It provides on-demand scale of replica instances within minutes to handle workload spikes during peak periods.

1. **AWS CodeCommit** provides private git repositories to host Moodle’s PHP codebase and CI/CD configuration files. **AWS CodeBuild** compiles source code, runs tests, and produces software packages ready to deploy onto Moodle App Server. **AWS CodeDeploy** manages the complexity of updating applications. It can deploy into Moodle with zero downtime using blue-green deployment methodologies. **AWS CodePipeline** automates the build, test, and deploy phases for code changes.

1. **AWS Secrets Manager** protects Moodle application secrets and rotates secrets automatically to match lifecycle requirements.

1. **AWS Systems Manager Parameter Store** manages Moodle’s configuration parameters, including shared storage endpoints, databases, and cache configuration. This avoids the security risk associated with hard-coding configuration within the codebase or environment.

## Further reading
<a name="further-reading"></a>

 For additional information, refer to 
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 
+ [Moodle website](https://moodle.org/)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | August 18, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.