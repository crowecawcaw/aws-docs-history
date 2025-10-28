# OpenText InfoArchive Architecture Using Amazon EKS and Amazon RDS

Publication date: **May 23, 2023 ([Diagram history](#diagram-history "#diagram-history"))**

Run OpenText InfoArchive on Amazon Elastic Kubernetes Service (Amazon EKS) and Amazon Relational Database Service (Amazon RDS). An in-depth exploration of
this OpenText InfoArchive can also be found at
[Manage data with OpenText InfoArchive and AWS.](https://aws.amazon.com/blogs/apn/manage-your-business-complete-data-with-opentext-infoarchive-and-aws/ "https://aws.amazon.com/blogs/apn/manage-your-business-complete-data-with-opentext-infoarchive-and-aws/")

## OpenText InfoArchive Architecture Using Amazon EKS and Amazon RDS Diagram

![Reference architecture diagram showing how to run OpenText InfoArchive on Amazon EKS and Amazon RDS](images/opentext-infoarchive-architecture-using-amazon-eks.png)

1. RESTful API call for administration, configuration, search, or retrieval.
2. RESTful API for ingestion and application integration.
3. OAuth2 flow generates an authorization request and token request
   from OpenText Directory Services.
4. HTTPS REST calls from InfoArchive web application clients passed
   to the InfoArchive server.
5. Search and store metadata in the InfoArchive database on **Amazon RDS**.
   Communication is over TLS 1.2. Multi Availability Zones disaster
   recovery with automatic failover.
6. Store binary (unstructured data) such as binary ingested content,
   backups of structured and retention data, and export results using an
   optional VPC gateway endpoint on **Amazon Simple Storage Service** (Amazon S3)
   and **Amazon Glacier**. Additional storage options are available.
7. **Amazon Elastic File System** (Amazon EFS) is used as
   persistent **Amazon EKS** volumes for temporary
   and working storage for local optimization.

## Download editable diagram

To customize this reference architecture diagram based on your business needs, [download the ZIP file](samples/opentext-infoarchive-architecture-using-amazon-eks.md "samples/opentext-infoarchive-architecture-using-amazon-eks.md") which contains an editable PowerPoint.

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
- [Blog - Manage Your Business Complete Data with OpenText InfoArchive and AWS](https://aws.amazon.com/blogs/apn/manage-your-business-complete-data-with-opentext-infoarchive-and-aws/ "https://aws.amazon.com/blogs/apn/manage-your-business-complete-data-with-opentext-infoarchive-and-aws/")

## Contributors

Contributors to this reference architecture diagram include:

- Chavi Gupta, Solutions Architect

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change              | Description                                     | Date               |
| ------------------- | ----------------------------------------------- | ------------------ | ----------------------------------------------------------------------------------------------------------- |
| Update              | Reference architecture updated                  | May 23, 2023       |
| Initial publication | Reference architecture diagram first published. | September 20, 2021 | ###### Note To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using. |
