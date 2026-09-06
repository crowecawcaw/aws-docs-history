

# Web Application Architecture on AWS
<a name="web-application-architecture"></a>

Publication date: **November 19, 2021 ([Diagram history](#diagram-history))**

This architecture shows how you can host a classic web application on AWS. You use multiple Availability Zones for high availability, Application Load Balancers for traffic distribution, and managed services for database, caching, and shared storage.

## Web Application Architecture on AWS
<a name="diagram1"></a>

![Architecture diagram showing a web application hosted on AWS with Amazon Elastic Compute Cloud, Amazon RDS, Amazon ElastiCache, and Amazon Simple Storage Service.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/web-application-architecture/images/web-application-architecture.png)


The following steps describe the architecture:

1. Route traffic from the web client based on the request path for static and dynamic content using [Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html).

1. Use a content delivery network (CDN) like [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html) to reduce latency when delivering your static content.

1. Use [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) to store static content and backups.

1. Protect your web application from common web exploits with a web application firewall like AWS WAF.

1. Simplify your SSL certificates management using AWS Certificate Manager (ACM).

1. Use an internet-facing Application Load Balancer to distribute web traffic to your web servers spread across multiple Availability Zones.

1. Use NAT gateways in each public subnet to enable [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) instances in private subnets to access the internet.

1. Use an internal Application Load Balancer to distribute traffic to your application servers spread across multiple Availability Zones.

1. Simplify your database administration by running your database layer in [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html).

1. If database access patterns are read-heavy, take advantage of a caching layer like [Amazon ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.html).

1. Consider using a shared storage service like Amazon Elastic File System (Amazon EFS) if your servers access shared files.

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
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | November 19, 2021 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.