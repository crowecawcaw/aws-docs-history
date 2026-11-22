

# Moodle learning management system on AWS

Publication date: **August 18, 2022 ([Diagram history](diagram-history.md))**

[Moodle](https://moodle.org/) is a learning platform designed to provide educators, administrators, and learners with a single robust, secure, and integrated system to create personalized learning environments. Moodle learning management system (LMS) on AWS can be deployed using architecture and can scale up on demand. Separate the application and data layers for elasticity and security.

## Moodle learning management system on AWS diagram
<a name="moodle-learning-management-system-on-aws-diagram"></a>

![The Moodle LMS runs on Amazon EC2 across multiple Availability Zones, with Aurora, ElastiCache, and Amazon EFS for data.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/education/images/moodle-learning-management-system-on-aws.png)


The following steps describe the architecture:

1. [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/) offers a scalable cloud Domain Name System (DNS) web service. It directs students to the closest [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/) location to access Moodle web application content while reducing latency.

1. CloudFront provides access to the Moodle web application server, which sits behind [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/), providing low latency access to content while serving cached content from edge locations spread across the globe.

1. [AWS Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/) (ACM) manages secure sockets layer (SSL) certificates for secure, encrypted communication with public and private resources. It provides free SSL certificates that integrate with CloudFront or Application Load Balancer with automated certificate rotation.

1.  Application Load Balancer automatically distributes incoming traffic to Moodle web application servers. The internet gateway provides an entry point to virtual private cloud (VPC) resources inside the public subnet, providing access to Application Load Balancer.

1. Network Address Translation (NAT) gateway allows outbound traffic for resources within a private subnet, such as Moodle App Server, that requires internet access.

1. Moodle App Server is deployed horizontally using [Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/) groups with multiple [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/) (Amazon EC2) instances across multiple Availability Zones (AZs), which are deployed in a separate private subnet for additional security. A [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/) Agent (SSM Agent) can be configured on the instances to provide SSH access without exposing an SSH port.

1. [Amazon Elastic File System](https://docs.aws.amazon.com/efs/latest/ug/) (Amazon EFS) can be used to store moodledata and other content, providing consistent performance, high availability, and durability.

1. [Amazon ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/) for Redis or Amazon ElastiCache for Memcached stores Moodle sessions and application caches in managed clusters with replicas across AZs.

1. [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/) offers both MySQL and PostgreSQL compatible global scale database clusters. It provides on-demand scale of replica instances within minutes to handle workload spikes during peak periods.

1. [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/) provides private git repositories to host Moodle's PHP codebase and CI/CD configuration files. [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/) compiles source code, runs tests, and produces software packages ready to deploy onto Moodle App Server. [AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/) manages the complexity of updating applications. It can deploy into Moodle with zero downtime using blue-green deployment methodologies. [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/) automates the build, test, and deploy phases for code changes.

1. [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/) protects Moodle application secrets and rotates secrets automatically to match lifecycle requirements.

1. Systems Manager Parameter Store manages Moodle's configuration parameters, including shared storage endpoints, databases, and cache configuration. This avoids the security risk associated with hard-coding configuration within the codebase or environment.

## Further reading
<a name="moodle-learning-management-system-on-aws-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 
+ [Moodle website](https://moodle.org/)