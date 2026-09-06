

# Hosting Adobe Experience Manager on AWS
<a name="hosting-adobe-experience-manager"></a>

Publication date: **October 11, 2022 ([Diagram history](#aem-history))**

With this architecture, you can deploy Adobe Experience Manager (AEM) on AWS. The solution uses [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/) for DNS, [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/) for web application protection, [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/) for content delivery, and [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/) for compute.

## Hosting Adobe Experience Manager on AWS diagram
<a name="aem-diagram"></a>

![Reference architecture diagram showing how to deploy Adobe Experience Manager on AWS by using Route 53, AWS WAF, CloudFront, AWS Certificate Manager, Amazon EC2, Lambda, and Amazon S3.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/hosting-adobe-experience-manager/images/hosting-aem-aws-ra.png)


The following steps describe the architecture:

1. Amazon Route 53 provides DNS configuration for the AEM deployment.

1. AWS WAF protects AEM against common web exploits.

1. Amazon CloudFront is a content delivery network (CDN) that speeds distribution of static and dynamic web content.

1. [AWS Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/) (ACM) provisions, manages, and deploys public and private SSL certificates for AEM.

1. An internet-facing Application Load Balancer distributes traffic to AEM dispatcher instances across multiple Availability Zones.

1. The AEM dispatcher on Amazon EC2 is an Apache httpd-based static webserver that provides caching, load balancing, and application security. We recommend Amazon EBS I/O optimized volumes. Each dispatcher maps to a publish instance 1:1 per Availability Zone.

1. [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) provides scaling logic for scale up and scale down events. Use Lambda to pair and unpair dispatcher-publish instances and update replication agents.

1. AEM publish is an AEM installation on Amazon EC2 that serves published content. Publish uses TarMK as a node store.

1. [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) (Amazon S3) is the preferred shared datastore for binary content for AEM publish and author instances. Use a VPC endpoint for private access to Amazon S3.

1. AEM author is an AEM installation on Amazon EC2 that you use to author content and administer the website. TarMK on Amazon EBS is preferred. Use a MongoDB node store for scalability.

1. AEM author cold standby provides high availability. Lambda automates failover logic.

1. (Optional) Author-dispatcher instances on Amazon EC2 improve authoring performance with caching disabled.

## Further reading
<a name="aem-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="aem-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#aem-history) | Reference architecture diagram first published. | October 11, 2022 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.