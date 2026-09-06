

# Enterprise Esri ArcGIS Platform on AWS
<a name="enterprise-esri-arcgis-platform"></a>

Publication date: **April 20, 2022 ([Diagram history](#esri-history))**

With this architecture, you can deploy a highly available Esri ArcGIS platform on AWS. [ArcGIS Enterprise](https://www.esri.com/en-us/arcgis/products/arcgis-enterprise/overview) is the foundational software system for a geographic information system (GIS). It powers mapping and visualization, analytics, and data management. It is the backbone for running the Esri suite of applications and your own custom applications.

This architecture uses [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/), [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/), Application Load Balancer, [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/), [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/), [Amazon Elastic File System](https://docs.aws.amazon.com/efs/latest/ug/), [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/), and [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/).

## Enterprise Esri ArcGIS Platform on AWS diagram
<a name="esri-diagram"></a>

![Reference architecture diagram showing a highly available Esri ArcGIS Enterprise deployment on AWS with Route 53, CloudFront, Amazon EC2, Amazon RDS, Amazon EFS, Amazon S3, and DynamoDB.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/enterprise-esri-arcgis-platform/images/enterprise-esri-arcgis-platform-on-aws-ra.png)


The following steps describe the architecture:

1. GIS users connect to the Esri ArcGIS Enterprise platform through Amazon Route 53. Route 53 offers a highly available, scalable Domain Name System (DNS) web service. Amazon CloudFront then fronts user traffic to securely deliver static and dynamic web content with low latency.

1. Application Load Balancer, in the public subnet, channels user requests to either Portal for ArcGIS or ArcGIS Server. The balancer routes requests based on the request type.

1. Highly available Portal for ArcGIS runs on Amazon EC2 instances across two Availability Zones. It controls access to ArcGIS Server services through portal groups. Portal for ArcGIS lets you publish data and maps as web services. As a portal administrator, you can assign a GIS server site to act as a hosting server.

1. Highly available ArcGIS Server runs on Amazon EC2 instances across two Availability Zones within an Auto Scaling group. ArcGIS Server is a central component of ArcGIS Enterprise. ArcGIS servers federate with an ArcGIS Enterprise portal. Your geographic data is available through layers and web maps.

1. The ArcGIS database runs on Amazon RDS across two Availability Zones. It provides a highly available relational geodatastore for your hosted feature layer data. This includes layers that feature analysis tools create in ArcGIS Enterprise Map Viewer Classic or ArcGIS Pro.

1. Highly available ArcGIS Data Store runs on Amazon EC2 instances across two Availability Zones. ArcGIS Data Store configures data storage for the hosting server used with ArcGIS Enterprise. It creates a relational data store, tile cache data store, spatiotemporal big data store, and graph store.

1. Amazon EFS provides directory and config stores. Both ArcGIS Server and Portal for ArcGIS share these stores.

1. Amazon S3 serves as the portal content store. It contains portal items, caching, and ArcGIS spatiotemporal data store backups.

1. Amazon DynamoDB tables store configuration and directories of the highly available ArcGIS Server sites. The VPC endpoint provides secure connections between the Enterprise ArcGIS platform, Amazon S3, and DynamoDB.

## Further reading
<a name="esri-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="esri-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#esri-history) | Reference architecture diagram first published. | April 20, 2022 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.