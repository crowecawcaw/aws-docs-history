

# PTC Windchill Product Lifecycle Management on AWS
<a name="ptc-windchill-plm"></a>

Publication date: **2020 ([Diagram history](#ptcw-diagram-history))**

With this architecture, you can deploy a highly available, load-balanced configuration of PTC Windchill on AWS that automatically scales on demand. This architecture uses [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/) (Amazon EC2), [Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/), [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/), and [Amazon Relational Database Service](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/) (Amazon RDS).

## PTC Windchill PLM architecture diagram
<a name="ptcw-diagram"></a>

![Reference architecture for PTC Windchill product lifecycle management on AWS.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/ptc-windchill-plm/images/ptc-windchill-plm-on-aws.png)


The following steps describe the architecture:

1. Users connect to the system through a web browser, Office apps, a computer-aided design (CAD) tool, or mobile devices.

1. Elastic Load Balancing directs user traffic to the Windchill web servers based on application availability on each node.

1. Elastic Load Balancing directs traffic to the Method Servers for client transactions and interactions with other systems.

1. A Background Server running on an Amazon EC2 instance performs dynamic content generation for end users or backend systems.

1. The Windchill cluster uses CAD/Doc Workers to create PDF versions of CAD and Office content and stores them in Amazon S3.

1. A Solr Index Server on Amazon EC2 supports keyword searches, including searching across metadata stored in the database.

1. Use PTC Solution Monitor (PSM) as a real-time performance monitoring tool for the system, application, and database.

1. Amazon RDS stores metadata for the application. Configure Amazon RDS with synchronous replication across Availability Zones.

1. The Windchill application uses Amazon S3 file storage to store content files.

1. Windchill replicates content for user collaboration through the Replication Server across Windchill workloads by using Amazon VPC peering.

1. Integrate corporate LDAP for both authentication and account management for Windchill by using [AWS Directory Service](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/). Windchill can run in a separate Region.

## Further reading
<a name="ptcw-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="ptcw-diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#ptcw-diagram-history) | Reference architecture diagram first published. | January 1, 2020 | 

**RSS subscription**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser that you are using.