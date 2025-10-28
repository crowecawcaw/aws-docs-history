# Resilience in Amazon Kendra

The AWS global infrastructure is built around AWS Regions and Availability Zones.
AWS Regions provide multiple physically separated and isolated Availability Zones, which
are connected with low-latency, high-throughput, and highly redundant networking. With
Availability Zones, you can design and operate applications and databases that automatically
fail over between zones without interruption. Availability Zones are more highly available,
fault tolerant, and scalable than traditional single or multiple data center
infrastructures.

For more information about AWS Regions and Availability Zones, see [AWS Global
Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/").

With AWS global infrastructure, Amazon Kendra Enterprise Edition is fault tolerant,
scalable, and highly available. Rolling back to previous versions of an index is not
currently supported, but you can refresh or recreate portions of your index by [deleting](API_BatchDeleteDocument.md "API_BatchDeleteDocument.md") and [adding](API_BatchPutDocument.md "API_BatchPutDocument.md") existing data sources
back into your index.
