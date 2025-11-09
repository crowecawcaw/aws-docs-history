# Open edX on AWS

Publication date: **April 14, 2023 ([Diagram history](#diagram-history "#diagram-history"))**

[Open edX](https://openedx.org/ "https://openedx.org/") is an open-source, distributed learning platform that, when implemented on AWS, can scale flexibly to optimize cost and maximize availability. Instructors and students can focus on teaching and learning, and organizations can reduce administrative overhead.

## Open edX on AWS Diagram

![Reference architecture diagram showing Open edX on AWS.](images/open-edx-for-high-availability-on-aws.png)

1. **Amazon Route 53** provides highly-available
   routing policies and reduces latency by directing students to the closest
   **Amazon CloudFront** locations for accessing static content.
2. Use **AWS Certificate Manager** (ACM) to manage your SSL
   certificates for secure communication with public and private resources.
3. **CloudFront** provides access to stateless
   Open edX mobile front ends (MFEs) that are stored on **Amazon Simple Storage Service**
   (Amazon S3). This access to Open edX includes services such as instructor reports,
   student/learner accounts, payments, and credit/debit card access MFEs.
4. **Application Load Balancer** scales automatically with your
   student traffic, and keeps student data secure and compliant with SSL
   termination and HTTPS.
5. Within this subnet, the Bastion host grants Open edX platform administrators
   secure access to manage the platform components. The NAT gateway provides a pathway
   to Open edX code repositories.
6. The Open edX layer of user-facing backend web apps is shown as an abstraction
   layer and run on **Amazon Elastic Compute Cloud** (Amazon EC2). Each of the
   apps can be created with its own **AWS Auto Scaling**
   group so that instances within separate private subnets or within private
   subnets are shared by other front end apps. The application instances
   (including Open edX CMS, LMS, and Insights) are accessible through
   **Application Load Balancer**.
7. The Open edX layer API backend services is shown as an abstraction layer.
   Each app can be created with its own **AWS Auto Scaling**
   group so that instances within separate private subnets or within private
   subnets are shared by other backend apps. The application instances (including
   Open edX Notes, Forums, and Blockstore) are accessible through **Application Load Balancer**.
8. [MongoDB](https://www.mongodb.com/ "https://www.mongodb.com/") is an open-source, NoSQL database
   that provides support for JSON-styled, document-oriented storage within the
   [Open edX platform](https://open.edx.org/the-platform/ "https://open.edx.org/the-platform/"). This
   clustered implementation provides resiliency through replication.
   The two secondary nodes provide a sufficient quorum to select a lead if the primary fails.
9. The load balancer receives a connection request, selects a target from the
   target group for the default rule, and opens a TCP connection to the
   selected target on the port specified in the listener configuration.
10. ProxySQL provides a single MySQL-compatible **Amazon Aurora**
    endpoint that automatically directs write traffic to the cluster endpoint and read
    traffic to the reader endpoint, improving the performance and scalability of the
    Open edX platform by adding read replicas to meet peak utilization.
11. **Amazon ElastiCache [for Redis](https://aws.amazon.com/elasticache/redis/ "https://aws.amazon.com/elasticache/redis/") and
    [for Memcached](https://aws.amazon.com/elasticache/memcached/ "https://aws.amazon.com/elasticache/memcached/")** provide fully-managed
    solutions that enhance robustness and reduce the cost of installing, operating, and
    maintaining highly-available cache clusters. **ElastiCache** manages the state of transactions
    to allow separation of application and database tiers. **ElastiCache** can deploy nodes across
    Availability Zones to provide higher resiliency.
12. **Aurora** provides a MySQL solution for Open edX
    relational database workloads, combining the performance and availability of
    traditional enterprise databases with the simplicity and cost-effectiveness
    of open-source databases.
13. **Amazon OpenSearch Service** provides support for open source Elasticsearch APIs,
    managed Kibana, integration with Logstash and other AWS services, and built-in alerting and SQL querying.
14. Use **Amazon S3** to store learning assets and log files generated
    by your servers. Leverage **Amazon S3** services to manage logs,
    active learning assets, and archived material and lower operations costs.
15. Use **Amazon Simple Email Service** (Amazon SES) to communicate with your
    students via Open edX SMTP email integration.

## Download editable diagram

To customize this reference architecture diagram based on your business needs, [download the ZIP file](samples/open-edx-for-high-availability-on-aws.md "samples/open-edx-for-high-availability-on-aws.md") which contains an editable PowerPoint.

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
- [Open edX](https://open.edx.org/ "https://open.edx.org/")

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change              | Description                                                         | Date             |
| ------------------- | ------------------------------------------------------------------- | ---------------- |
| Refresh             | Reference architecture diagram reviewed for relevance and accuracy. | April 14, 2023   |
| Initial publication | Reference architecture diagram first published.                     | October 27, 2021 |

###### Note

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
