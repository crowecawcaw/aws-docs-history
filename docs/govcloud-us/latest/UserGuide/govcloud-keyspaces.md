

# Amazon Keyspaces (for Apache Cassandra) in AWS GovCloud (US)
<a name="govcloud-keyspaces"></a>

Amazon Keyspaces (for Apache Cassandra) is a scalable, highly available, and managed Apache Cassandra–compatible database service. With Amazon Keyspaces, you don’t have to provision, patch, or manage servers, and you don’t have to install, maintain, or operate software.

 Amazon Keyspaces is serverless, so you pay for only the resources that you use, and the service automatically scales tables up and down in response to application traffic. You can build applications that serve thousands of requests per second with virtually unlimited throughput and storage.

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West) 
+  AWS GovCloud (US-East) 

## How Amazon Keyspaces differs
<a name="govcloud-diffs-16"></a>

The following differences apply to Amazon Keyspaces:
+ Amazon Keyspaces Multi-Region replication is not available.
+ Amazon Keyspaces integration with CloudFormation is not available.

This section describes the Amazon Keyspaces quotas and default values in AWS GovCloud (US) Regions that differ from Amazon Keyspaces [quotas](https://docs.aws.amazon.com/keyspaces/latest/devguide/quotas.html) in other AWS Regions.


**​**  

| Quota | Description |  Amazon Keyspaces default | 
| --- | --- | --- | 
| Max read throughput per second | The maximum read throughput per second—read request units (RRUs) or read capacity units (RCUs)—that can be allocated to a table per Region. This default value is adjustable in the [AWS Service Quotas](https://console.aws.amazon.com/servicequotas/home#!/services/cassandra/quotas) console. | 10,000 | 
| Max write throughput per second | The maximum write throughput per second—write request units (WRUs) or write capacity units (WCUs)—that can be allocated to a table per Region. This default value is adjustable in the [AWS Service Quotas](https://console.aws.amazon.com/servicequotas/home#!/services/cassandra/quotas) console. | 10,000 | 

For more information about quotas in AWS GovCloud (US) Regions, see [Service Quotas](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-servicequotas.html) in the [AWS GovCloud (US) User Guide](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/).

## Documentation
<a name="govcloud-docs-54"></a>
+  [Amazon Keyspaces documentation](https://docs.aws.amazon.com/keyspaces/index.html) 

## Export-controlled content
<a name="govcloud-itar-content-94"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+  Amazon Keyspaces metadata is not permitted to contain export-controlled data. This metadata includes all the configuration data that you enter when creating and maintaining your Amazon Keyspaces resources such as keyspaces and tables, for example resource names and tags.
+ Do not enter export-controlled data in the following fields:
  + Keyspace names
  + Table names
  + Resource tags