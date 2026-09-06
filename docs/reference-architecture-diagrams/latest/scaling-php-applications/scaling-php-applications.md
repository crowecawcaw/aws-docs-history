

# Scaling PHP Applications on AWS
<a name="scaling-php-applications"></a>

Publication date: **January 20, 2022 ([Diagram history](#diagram-history))**

This architecture shows how to run highly available, performant, and secure PHP applications on AWS. You use [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) with Auto Scaling, Amazon Aurora for the database layer, and [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html) for content delivery with CI/CD automation.

## Scaling PHP Applications on AWS
<a name="diagram1"></a>

![Architecture diagram showing a scalable PHP application on AWS using Amazon Elastic Compute Cloud, Amazon Aurora, Amazon ElastiCache, and Amazon CloudFront.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/scaling-php-applications/images/scaling-php-applications.png)


The following steps describe the architecture:

1. [Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html) routes end-user requests resolving Domain Name Service (DNS).

1. Amazon CloudFront caches content and accelerates delivery, by using global points of presence. CloudFront also handles SSL termination, integrating with AWS Certificate Manager which automatically creates and renews SSL certificates.

1. AWS WAF integration with CloudFront and Application Load Balancer mitigates OWASP top 10 application vulnerabilities.

1. The Application Load Balancer routes HTTP/S requests to Amazon EC2 instances running on private subnets.

1. An Amazon Linux 2 AMI contains the PHP and other needed binaries including the AWS SDK for PHP.

1. The [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) Agent installed on the Amazon Linux 2 AMI streams application logs, additional host-level metrics, and custom business metrics.

1. Amazon EC2 Auto Scaling manages instance launch based on metrics such as CPU and memory. It uses Amazon Graviton instances for cost optimization.

1. Using [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) Session Manager, you connect to Amazon EC2 instances with web-based sessions on the AWS Console without needing key pairs or open SSH ports.

1. Database credentials are securely stored on AWS Secrets Manager. Using the AWS SDK for PHP, the application code retrieves the credentials stored on Secrets Manager through an IAM role.

1. Application code is stored on AWS CodeCommit using the familiar Git command line interface (CLI).

1. [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) implements CI/CD, orchestrating code deployment using an AWS CodeDeploy hook that triggers when new Amazon EC2 instances are launched.

1. [Amazon ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.html) for Redis caches session data.

1. Amazon Aurora Multi-AZ enables high availability. The application connects through the DNS endpoint that handles failover automatically. The Aurora reader endpoint handles read operations, offloading Aurora writer instance load.

1. Amazon Elastic File System (Amazon EFS) stores and shares web content with the Auto Scaling group.

## Further reading
<a name="further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | January 20, 2022 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.