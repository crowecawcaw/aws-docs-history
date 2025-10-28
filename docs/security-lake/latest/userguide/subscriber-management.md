# Subscriber management in Security Lake

An Amazon Security Lake subscriber consumes logs and events from Security Lake. To control costs and
adhere to least privilege access best practices, you provide subscribers access to data on a
per-source basis. For more information about sources, see [Source management in Security Lake](source-management.md "source-management.md").

Security Lake supports two types of subscriber access:

- **Data access** Subscribers with data access to source data in Amazon Security Lake are notified of new objects
  for the source as the data is written to the S3 bucket. By default, subscribers are notified
  about new objects through an HTTPS endpoint that they provide. Alternatively, subscribers
  can be notified about new objects by polling an Amazon Simple Queue Service (Amazon SQS) queue.
- **Query access** – Subscribers with query access can query data that Security Lake collects. These subscribers directly query AWS Lake Formation tables in your S3 bucket with services like Amazon Athena.
  Subscribers only have access to the source data in the AWS Region that you select when you
  create the subscriber. To give a subscriber access to data from multiple Regions, you can
  specify the Region where you create the subscriber as a rollup Region and have other Regions
  contribute data to it. For more information about rollup Regions and contributing Regions,
  see [Managing Regions in Security Lake](manage-regions.md "manage-regions.md").

###### Important

The maximum number of sources that Security Lake allows to add per subscriber is 10. This could be a combination of AWS sources and custom sources.

###### Topics

- [Managing data access for Security Lake
  subscribers](subscriber-data-access.md "subscriber-data-access.md")
- [Managing query access for Security Lake
  subscribers](subscriber-query-access.md "subscriber-query-access.md")
