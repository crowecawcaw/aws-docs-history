

# OpenText InfoArchive on Amazon EKS and Amazon RDS

Publication date: **May 23, 2023 ([Diagram history](diagram-history.md))**

You can run OpenText InfoArchive on [Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/eks/latest/userguide/) (Amazon EKS) and [Amazon Relational Database Service](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/) (Amazon RDS). For an in-depth exploration of this architecture, see [Manage data with OpenText InfoArchive and AWS](https://aws.amazon.com/blogs/apn/manage-your-business-complete-data-with-opentext-infoarchive-and-aws/).

## OpenText InfoArchive on Amazon EKS and Amazon RDS diagram
<a name="opentext-infoarchive-architecture-using-amazon-eks-diagram"></a>

![OpenText InfoArchive runs on Amazon EKS and Amazon RDS, with content stored in Amazon S3 and Amazon EFS.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/digital-marketing/images/opentext-infoarchive-architecture-using-amazon-eks.png)


The following steps describe the architecture:

1. RESTful API call for administration, configuration, search, or retrieval. 

1. RESTful API for ingestion and application integration. 

1. OAuth2 flow generates an authorization request and token request from OpenText Directory Services. 

1. HTTPS REST calls from InfoArchive web application clients passed to the InfoArchive server. 

1. Search and store metadata in the InfoArchive database on Amazon RDS. Communication is over TLS 1.2. Multi Availability Zones disaster recovery with automatic failover. 

1. Store binary (unstructured data) such as binary ingested content, backups of structured and retention data, and export results using an optional VPC gateway endpoint on [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) (Amazon S3), including the Amazon S3 Glacier storage classes. Additional storage options are available. 

1. [Amazon Elastic File System](https://docs.aws.amazon.com/efs/latest/ug/) (Amazon EFS) is used as persistent Amazon EKS volumes for temporary and working storage for local optimization. 

## Further reading
<a name="opentext-infoarchive-architecture-using-amazon-eks-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 
+  [Blog - Manage Your Business Complete Data with OpenText InfoArchive and AWS](https://aws.amazon.com/blogs/apn/manage-your-business-complete-data-with-opentext-infoarchive-and-aws/) 