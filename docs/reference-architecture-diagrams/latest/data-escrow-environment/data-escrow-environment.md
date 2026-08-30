# Data Escrow Environment Reference Architecture

Publication date: **May 13, 2022 ([Diagram history](#diagram-history "#diagram-history"))**

This architecture shows how to build a data escrow environment. You can securely store, share, and access data between publishers and advertisers.

## Data Escrow Environment Reference Architecture

![Architecture diagram showing a data escrow environment for publishers and advertisers on AWS.](images/data-escrow-environment.png)

1. The publisher account stores data specific to each advertiser in Amazon S3 object storage.
2. Transformed data stores in transformed Amazon S3 object storage.
3. Data goes through transformation processes by using services such as Amazon EMR or AWS Glue.
4. The local governance and monitoring system governs and catalogs these S3 buckets. This uses AWS Glue catalog, Lake Formation, CloudTrail, and CloudWatch.
5. The local governance and monitoring system catalogs and governs transformed S3 buckets.
6. Resource sharing occurs between the central governance account and the publisher account holding advertiser data. The publisher controls the central governance account.
7. The central governance account provides access to the publisher account. The publisher account transforms Amazon S3 objects to different advertisers' accounts.
8. The advertiser client application starts a process to integrate data from publishers.
9. Amazon Managed Workflows for Apache Airflow creates Airflow DAGs for transformations.
10. The transformation process extracts data from local S3 buckets containing advertiser data.
11. The transformation process gets access to related data from the publisher account. It uses central governance and the metadata access layer.
12. Transformed and joined data from both accounts store in final S3 buckets.
13. Amazon S3 data exports to Amazon Redshift or queries directly with or Amazon Redshift Spectrum.
14. Amazon Quick Sight accesses the tables created in or Amazon Redshift Spectrum.
15. Analysts access dashboards and insights.

## Further reading

For additional information, refer to

- [AWS Architecture Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture "https://aws.amazon.com/architecture")
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")
- [Lake Formation product page](https://aws.amazon.com/lake-formation/ "https://aws.amazon.com/lake-formation/")

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change              | Description                                     | Date         |
| ------------------- | ----------------------------------------------- | ------------ |
| Initial publication | Reference architecture diagram first published. | May 13, 2022 |

###### Note

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
