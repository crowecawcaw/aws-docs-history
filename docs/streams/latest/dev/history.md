

# Document history
<a name="history"></a>

The following table describes the important changes to the Amazon Kinesis Data Streams documentation.

| Change | Description | Date | 
| --- |--- |--- |
| [Added support for rolling back from KCL 3.x Phase 1 to KCL 2.x](#history) | Added [Migrate from previous KCL versions](https://docs.aws.amazon.com/streams/latest/dev/kcl-migration-previous-versions.html) covering the `rollback-to-v2` mode and the `useAbsoluteReBalanceThreshold` configuration. | September 25, 2026 | 
| [Added service-managed record distribution](#history) | Added [Service-managed record distribution](https://docs.aws.amazon.com/streams/latest/dev/service-managed-record-distribution.html). | September 23, 2026 | 
| [Added Regions for enhanced fan-out consumers](#history) | Added new supported AWS Regions to [Develop enhanced fan-out consumers with dedicated throughput](https://docs.aws.amazon.com/streams/latest/dev/enhanced-consumers.html). | September 1, 2026 | 
| [Added the streaming tables and Amazon S3 delivery chapter](#history) | Added [Streaming tables and Amazon S3 delivery for Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/data-delivery.html). | August 31, 2026 | 
| [Added dry run validation for data plane APIs](#history) | Added [Test your permissions and request inputs with dry run](https://docs.aws.amazon.com/streams/latest/dev/kds-dryrun-validation.html). | August 25, 2026 | 
| [Added warm throughput scale-down behavior and CLI/API updates](#history) | Updated [Create and manage Kinesis data streams](https://docs.aws.amazon.com/streams/latest/dev/working-with-streams.html) with warm throughput scale-down behavior. | July 22, 2026 | 
| [Documented single table migration metrics for the KCL](#history) | Updated [Single table format for KCL](https://docs.aws.amazon.com/streams/latest/dev/kcl-single-table-format.html) with migration metrics. | July 21, 2026 | 
| [Added KCL v3.5 single table format documentation](#history) | Added [Single table format for KCL](https://docs.aws.amazon.com/streams/latest/dev/kcl-single-table-format.html). | June 18, 2026 | 
| [Added support for large record sizes up to 10 MiB](#history) | Added [Handle large records](https://docs.aws.amazon.com/streams/latest/dev/large-records.html). | October 27, 2025 | 
| [Added support for resilience testing with AWS Fault Injection Service](#history) | Added [Perform resilience testing with AWS Fault Injection Service](https://docs.aws.amazon.com/streams/latest/dev/kinesis-fis.html). | October 15, 2025 | 
| [End-of-support dates and version lifecycle policy](#history) | Added information about end-of-support dates and version lifecycle policy for Amazon Kinesis Producer Library (KPL) and Amazon Kinesis Client Library (KCL). For more information, see [KPL version lifecycle policy](https://docs.aws.amazon.com/streams/latest/dev/kpl-version-lifecycle-policy.html) and [KCL version lifecycle policy](https://docs.aws.amazon.com/streams/latest/dev/kcl-version-lifecycle-policy.html). | March 13, 2025 | 
| [Added support for sharing data streams across accounts](#history) | Added [Share your data stream with another account](https://docs.aws.amazon.com/streams/latest/dev/controlling-access.html#sharing-data-streams). | November 22, 2023 | 
| [Added support for the on-demand and provisioned data stream capacity modes](#history) | Added [Choose the right mode to stream in](https://docs.aws.amazon.com/streams/latest/dev/how-do-i-size-a-stream.html) | November 29, 2021 | 
| [Enabled multi-stream processing in Kinesis Client Library](#history) | Added [Process multiple data streams with the same KCL 2.x for Java consumer application ](https://docs.aws.amazon.com/streams/latest/dev/shared-throughput-kcl-consumers.html#shared-throughput-kcl-multistream) | October 20, 2020 | 
| [Added two new API features to simplify consuming data from Kinesis data streams](#history) | Added two new API features to simplify consuming data from Kinesis data streams. See [List shards](https://docs.aws.amazon.com/streams/latest/dev/kinesis-using-sdk-java-list-shards.html). | August 18, 2020 | 
| [Added information about controlling access to VPC endpoints for Kinesis Data Streams](#history) | Added [Control access to VPC endpoints for Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/vpc.html#interface-vpc-endpoints-policies). | August 23, 2019 | 
| [New documentation for consumers that use enhanced fan-out](#history) | Added [Develop enhanced fan-out consumers with dedicated throughput](https://docs.aws.amazon.com/streams/latest/dev/enhanced-consumers.html) | August 2, 2018 | 
| [Updated summary of service limits](#history) | Provided a clearer description of the service limits in [Quotas and limits](https://docs.aws.amazon.com/streams/latest/dev/service-sizes-and-limits.html). | June 6, 2018 | 
| [New content for server-side encryption](#history) | Added [Data protection in Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/server-side-encryption.html). | July 7, 2017 | 
| [New content for enhanced CloudWatch metrics](#history) | Updated [Monitor Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/monitoring.html). | April 19, 2016 | 
| [New content for enhanced Kinesis Agent](#history) | Updated [Write to Amazon Kinesis Data Streams using Kinesis Agent](https://docs.aws.amazon.com/streams/latest/dev/writing-with-agents.html) | April 11, 2016 | 
| [New content for using Kinesis Agent](#history) | Added [Write to Amazon Kinesis Data Streams using Kinesis Agent](https://docs.aws.amazon.com/streams/latest/dev/writing-with-agents.html). | October 2, 2015 | 
| [Update KPL content for release 0.10.0](#history) | Added [Develop producers using the Amazon Kinesis Producer Library (KPL)](https://docs.aws.amazon.com/streams/latest/dev/developing-producers-with-kpl.html). | July 15, 2015 | 
| [Update KCL metrics topic for configurable metrics](#history) | Updated [Monitor the Amazon Kinesis Client Library with Amazon CloudWatch](https://docs.aws.amazon.com/streams/latest/dev/monitoring-with-kcl.html). | July 9, 2015 | 
| [Re-organized content](#history) | Significantly re-organized content topics for more concise tree view and more logical grouping. | July 1, 2015 | 
| [New KPL topic](#history) | Added [Develop producers using the Amazon Kinesis Producer Library (KPL)](https://docs.aws.amazon.com/streams/latest/dev/developing-producers-with-kpl.html). | June 2, 2015 | 
| [New KCL metrics topic](#history) | Added [Monitor the Amazon Kinesis Client Library with Amazon CloudWatch](https://docs.aws.amazon.com/streams/latest/dev/monitoring-with-kcl.html). | May 19, 2015 | 
| [Support for KCL .NET](#history) | Added [Develop an Amazon Kinesis Client Library consumer in .NET](https://docs.aws.amazon.com/streams/latest/dev/kinesis-record-processor-implementation-app-dotnet.html). | May 1, 2015 | 
| [Support for KCL Node.js](#history) | Added [Develop an Amazon Kinesis Client Library consumer in Node.js](https://docs.aws.amazon.com/streams/latest/dev/kinesis-record-processor-implementation-app-nodejs.html). | March 26, 2015 | 
| [Support for KCL Ruby](#history) | Added links to KCL Ruby library. | January 12, 2015 | 
| [New API PutRecords](#history) | Added information about new PutRecords API to [Add multiple records with PutRecords](https://docs.aws.amazon.com/streams/latest/dev/developing-producers-with-sdk.html#kinesis-using-sdk-java-putrecords). | December 15, 2014 | 
| [Support for tagging](#history) | Added [Tag your Amazon Kinesis Data Streams resources](https://docs.aws.amazon.com/streams/latest/dev/tagging.html). | September 11, 2014 | 
| [New CloudWatch metric](#history) | Added the metric `GetRecords.IteratorAgeMilliseconds` to [Amazon Kinesis Data Streams dimensions and metrics](https://docs.aws.amazon.com/streams/latest/dev/monitoring-with-cloudwatch.html#kinesis-metrics). | September 3, 2014 | 
| [New monitoring chapter](#history) | Added [Monitor Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/monitoring.html) and [Monitor the Amazon Kinesis Data Streams service with Amazon CloudWatch](https://docs.aws.amazon.com/streams/latest/dev/monitoring-with-cloudwatch.html). | July 30, 2014 | 
| [Default shard limit](#history) | Updated the [Quotas and limits](https://docs.aws.amazon.com/streams/latest/dev/service-sizes-and-limits.html). The default shard limit has been raised from 5 to 10. | February 25, 2014 | 
| [Default shard limit](#history) | Updated the [Quotas and limits](https://docs.aws.amazon.com/streams/latest/dev/service-sizes-and-limits.html). The default shard limit has been raised from 2 to 5. | January 28, 2014 | 
| [API version updates](#history) | Updates for version 2013-12-02 of the Kinesis Data Streams API. | December 12, 2013 | 
| [Initial release](#history) | Initial release of the Amazon Kinesis Developer Guide. | November 14, 2013 | 