

# Adobe Commerce and Magento Open Source on AWS
<a name="magento-ecommerce-on-aws"></a>

Publication date: **April 25, 2022 ([Diagram history](#magento-history))**

With this architecture, you can deploy [Adobe Commerce](https://business.adobe.com/products/magento/magento-commerce.html) or [Magento Open Source](https://business.adobe.com/products/magento/open-source.html) on AWS. Ecommerce platforms require high availability, fast response times, and the ability to scale during traffic spikes. You use [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/) for the database, [Amazon ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/mem-ug/) for Redis for caching, and [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/) for catalog search.

## Magento eCommerce diagram
<a name="magento-diagram"></a>

![Adobe Commerce or Magento Open Source deployed across multiple Availability Zones on Amazon Elastic Compute Cloud, with Amazon Route 53, AWS WAF, Amazon CloudFront, Varnish Cache, Amazon Aurora, Amazon ElastiCache for Redis, Amazon OpenSearch Service, and Amazon EFS.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/magento-ecommerce-on-aws/images/magento-ecommerce-on-aws.png)


The following steps describe the architecture:

1. [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/) routes end user requests. It resolves domain name service (DNS) and provides global traffic management.

1. [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/) helps protect Magento from common web exploits that affect application availability or compromise security.

1. [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/) speeds up the distribution of static and dynamic web content as a content delivery network (CDN).

1. An internet-facing Application Load Balancer distributes HTTP/S requests to Varnish instances in an Auto Scaling group across multiple Availability Zones.

1. (Optional) Use [Varnish Cache](https://varnish-cache.org/), a web application accelerator, to reduce response times. The Enterprise version on AWS Marketplace includes advanced scaling and management features.

1. An internal Application Load Balancer distributes traffic from Varnish Cache across Magento instances in an Auto Scaling group across multiple Availability Zones.

1. [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/) instances run the Magento Open Source or Adobe Commerce software. An Auto Scaling group provides high availability and dynamic scaling.

1. An Amazon OpenSearch Service cluster provides a fully managed search solution for the Magento catalog.

1. Amazon ElastiCache for Redis provides in-memory session storage and database request caching.

1. Aurora provides a fully managed, high-performance relational database. Multi-AZ deployments provide high availability.

1. [Amazon Elastic File System (Amazon EFS)](https://docs.aws.amazon.com/efs/latest/ug/) stores and shares content with the Auto Scaling groups.

## Further reading
<a name="magento-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture/)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="magento-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#magento-history) | Reference architecture diagram first published. | April 25, 2022 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.