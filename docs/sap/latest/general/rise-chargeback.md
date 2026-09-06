

# Implement chargeback for connectivity to RISE
<a name="rise-chargeback"></a>

If you are a company with subsidiaries, you may have different RISE contracts, leading to deployments in separate AWS accounts while requiring an interlinked network connectivity. In this instance, you must deploy Transit Gateway connection in a Landing Zone (multi-account) setup. It can scale your RISE deployment and integrate with multiple RISE with SAP VPCs.

Transit Gateway Flow Logs enables effective cost management. Transit Gateway Flow Logs can be integrated with Cost and Usage Report (CUR) that can be attributed as chargeback to the business units. For more information, see [Logging network traffic using Transit Gateway Flow Logs](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-flow-logs.html).

![How to implement chargeback capability for connectivity to RISE.](http://docs.aws.amazon.com/sap/latest/general/images/rise-chargeback.png)


The preceding diagram displays how Transit Gateway can be used to connect multiple RISE with SAP VPCs and provide chargeback capability through the Flow Logs.

For more information, see the following blogs:
+  [Using AWS Transit Gateway Flow Logs to chargeback data processing costs in a multi-account environment](https://aws.amazon.com/blogs/networking-and-content-delivery/using-aws-transit-gateway-flow-logs-to-chargeback-data-processing-costs-in-a-multi-account-environment/) 
+  [How-to chargeback shared services: An AWS Transit Gateway example](https://aws.amazon.com/blogs/aws-cloud-financial-management/gs-chargeback-shared-services-an-aws-transit-gateway-example/) 

Use the following steps to enable this setup:

1. Enable Transit Gateway Flow Logs. For more information, see [Create a flow log that publishes to Amazon S3](https://docs.aws.amazon.com/vpc/latest/tgw/flow-logs-s3.html#flow-logs-s3-create-flow-log).

1. Setup Cost and Usage Reporting and setup Athena to utilize the reporting. For more information, see [Creating Cost and Usage Reports](https://docs.aws.amazon.com/cur/latest/userguide/cur-create.html) and [Querying Cost and Usage Reports using Amazon Athena](https://docs.aws.amazon.com/cur/latest/userguide/cur-query-athena.html).

1. Obtain the Transit Gateway data processing charge per-account.

   1. Decide a cost allocation strategy - distribute costs evenly across all accounts or distribute proportionally across all accounts.

   1. Calculate the total network traffic and percentage allocation per account using [AWS Transit Gateway](https://catalog.workshops.aws/cur-query-library/en-US/queries/networking-and-content-delivery/aws-transit-gateway) query.

   1. Estimate cost per account, by collecting from CloudWatch that collects Network In(Upload) and NetworkOut(Download).

      1. NetworkIn(Upload) \+ NetworkOut(Download) per usage account/ total data processed in network account

      1. % of usage x total cost = chargeback cost per usage account