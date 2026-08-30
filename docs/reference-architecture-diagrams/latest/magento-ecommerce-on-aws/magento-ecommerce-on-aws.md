# Adobe Commerce and Magento Open Source on AWS

Publication date: **April 25, 2022 ([Diagram history](#magento-history "#magento-history"))**

With this architecture, you can deploy [Adobe
Commerce](https://business.adobe.com/products/magento/magento-commerce.html "https://business.adobe.com/products/magento/magento-commerce.html") or [Magento
Open Source](https://business.adobe.com/products/magento/open-source.html "https://business.adobe.com/products/magento/open-source.html") on AWS. Ecommerce platforms require high availability,
fast response times, and the ability to scale during traffic spikes. You use [Amazon Aurora](../../../AmazonRDS/latest/AuroraUserGuide.md "../../../AmazonRDS/latest/AuroraUserGuide.md") for the
database, [Amazon ElastiCache](../../../AmazonElastiCache/latest/mem-ug.md "../../../AmazonElastiCache/latest/mem-ug.md") for Redis for caching, and [Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide.md "../../../opensearch-service/latest/developerguide.md") for catalog search.

## Magento eCommerce diagram

![Adobe Commerce or Magento Open Source deployed across multiple Availability Zones on Amazon Elastic Compute Cloud, with Amazon Route 53, AWS WAF, Amazon CloudFront, Varnish Cache, Amazon Aurora, Amazon ElastiCache for Redis, Amazon OpenSearch Service, and Amazon EFS.](images/magento-ecommerce-on-aws.png)

The following steps describe the architecture:

1. [Amazon Route 53](../../../Route53/latest/DeveloperGuide.md "../../../Route53/latest/DeveloperGuide.md") routes end user requests. It
   resolves domain name service (DNS) and provides global traffic management.
2. [AWS WAF](../../../waf/latest/developerguide.md "../../../waf/latest/developerguide.md") helps
   protect Magento from common web exploits that affect application
   availability or compromise security.
3. [Amazon CloudFront](../../../AmazonCloudFront/latest/DeveloperGuide.md "../../../AmazonCloudFront/latest/DeveloperGuide.md") speeds up the
   distribution of static and dynamic web content as a content delivery network
   (CDN).
4. An internet-facing Application Load Balancer distributes HTTP/S requests to
   Varnish instances in an Auto Scaling group across multiple Availability
   Zones.
5. (Optional) Use [Varnish Cache](https://varnish-cache.org/ "https://varnish-cache.org/"), a web
   application accelerator, to reduce response times. The Enterprise version on AWS
   Marketplace includes advanced scaling and management features.
6. An internal Application Load Balancer distributes traffic from Varnish
   Cache across Magento instances in an Auto Scaling group across multiple
   Availability Zones.
7. [Amazon Elastic Compute Cloud](../../../AWSEC2/latest/UserGuide.md "../../../AWSEC2/latest/UserGuide.md") instances run the
   Magento Open Source or Adobe Commerce software. An Auto
   Scaling group provides high availability and dynamic scaling.
8. An Amazon OpenSearch Service cluster provides a fully managed search solution for the
   Magento catalog.
9. Amazon ElastiCache for Redis provides in-memory session storage and database request
   caching.
10. Aurora provides a fully managed, high-performance relational database. Multi-AZ
    deployments provide high availability.
11. [Amazon Elastic File System
    (Amazon EFS)](../../../efs/latest/ug.md "../../../efs/latest/ug.md") stores and shares content with the Auto Scaling groups.

## Further reading

For additional information, see the following resources:

- [AWS Architecture Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture/ "https://aws.amazon.com/architecture/")
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")

## Diagram history

To receive updates about this reference architecture diagram, subscribe to the RSS
feed.

| Change              | Description                                     | Date           |
| ------------------- | ----------------------------------------------- | -------------- |
| Initial publication | Reference architecture diagram first published. | April 25, 2022 |

###### RSS subscription requirement

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you
are using.
