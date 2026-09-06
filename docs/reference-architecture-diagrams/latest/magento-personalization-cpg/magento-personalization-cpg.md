

# Personalization in Magento eCommerce on AWS for CPG
<a name="magento-personalization-cpg"></a>

Publication date: **May 20, 2021 ([Diagram history](#magpers-history))**

With this architecture, you can deploy containerized Magento ecommerce software on AWS with personalization for consumer packaged goods (CPG). Product recommendations based on user behavior increase conversions and customer engagement. You use [Amazon Personalize](https://docs.aws.amazon.com/personalize/latest/dg/) for ML-based recommendations and [Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/eks/latest/userguide/) for container orchestration.

## Magento personalization diagram
<a name="magpers-diagram"></a>

![Containerized Magento deployed on Amazon Elastic Kubernetes Service with Varnish Cache pods, Amazon Personalize providing product recommendations, Amazon Aurora database, Amazon ElastiCache for Redis, Amazon OpenSearch Service, and Amazon Elastic Container Registry hosting container images.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/magento-personalization-cpg/images/magento-personalization-cpg.png)


The following steps describe the architecture:

1. [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/) provides DNS configuration.

1. [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/) protects Magento against common web exploits.

1. [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/) speeds up the distribution of static and dynamic web content as a content delivery network (CDN).

1. Elastic Load Balancing (Application Load Balancer) distributes traffic across Varnish pods running in Amazon EKS through a Kubernetes ingress across multiple Availability Zones.

1. Varnish Cache runs as Kubernetes pods on Amazon EKS. The Enterprise version provides better features for cloud backends and cache-purge across dynamic hosts.

1. Magento Open Source or Commerce edition runs as Kubernetes pods on Amazon EKS. Each pod includes the Magento application, Nginx web server, and PHP.

1. [Amazon Elastic Container Registry](https://docs.aws.amazon.com/AmazonECR/latest/userguide/) hosts the container images for both Varnish and Magento.

1. [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/) provides a managed search solution for the Magento catalog.

1. [Amazon ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/mem-ug/) for Redis provides a caching layer for the database.

1. Use [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/) or Amazon RDS for the relational database. These provide high availability and multi-AZ configuration.

1. Use [Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/) to access shared configuration across Varnish and shared media assets across Magento pods.

1. Use the Amazon Personalize extension for Magento to export user historical data into an [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) bucket.

1. Amazon Personalize trains on the historical data exported from Magento. It creates a custom solution and campaign as a private ML model hosted in your AWS account.

1. After activating the Amazon Personalize model, it displays product recommendations to end users. Real-time data interaction indicators let Amazon Personalize learn from user actions such as adding products to carts or wish lists.

## Further reading
<a name="magpers-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture/)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="magpers-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#magpers-history) | Reference architecture diagram first published. | May 20, 2021 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.