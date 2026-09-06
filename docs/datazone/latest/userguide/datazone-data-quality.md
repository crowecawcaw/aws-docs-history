

# Data quality in Amazon DataZone
<a name="datazone-data-quality"></a>

Data quality metrics in Amazon DataZone help you understand the different quality metrics such as completeness, timeliness, and accuracy of your data sources. Amazon DataZone integrates with AWS Glue Data Quality and offers APIs to integrate data quality metrics from third-party data quality solutions. Data users can see how data quality metrics change over time for their subscribed assets. To author and run the data quality rules, you can use your data quality tool of choice such as AWS Glue data quality. With data quality metrics in Amazon DataZone, data consumers can visualize the data quality scores for the assets and columns, helping build trust in the data they use for decisions. 

**Pre-requisites and IAM role changes**

If you are using Amazon DataZone's AWS managed policies, there are no additional configuration steps and these managed policies are automatically updated to support data quality. If you are using your own policies for the roles that grant Amazon DataZone the required permissions to interoperate with supported services, you must update the policies attached to these roles to enable support for reading the AWS Glue data quality information in the [AWS managed policy: AmazonDataZoneGlueManageAccessRolePolicy](security-iam-awsmanpol-AmazonDataZoneGlueManageAccessRolePolicy.md) and enable support for the time series APIs in the [AWS managed policy: AmazonDataZoneDomainExecutionRolePolicy](security-iam-awsmanpol-AmazonDataZoneDomainExecutionRolePolicy.md) and the [AWS managed policy: AmazonDataZoneFullUserAccess](security-iam-awsmanpol-AmazonDataZoneFullUserAccess.md). 

## Enabling data quality for AWS Glue assets
<a name="datazone-data-quality-glue"></a>

Amazon DataZone pulls the data quality metrics from AWS Glue in order to provide context during a point in time, for example, during a business data catalog search. Data users can see how data quality metrics change over time for their subscribed assets. Data producers can ingest AWS Glue data quality scores on a schedule. The Amazon DataZone business data catalog can also display data quality metrics from third-party systems through data quality APIs. For more information, see [AWS Glue Data Quality](https://docs.aws.amazon.com/glue/latest/dg/glue-data-quality.html) and [Getting started with AWS Glue Data Quality for the Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/data-quality-getting-started.html).

You can enable data quality metrics for your Amazon DataZone assets in the following ways:
+ Use the Data Portal or the Amazon DataZone APIs to enable data quality for your AWS Glue data source via the Amazon DataZone data portal either while creating new or editing existing AWS Glue data source.

  For more information on enabling data quality for a data source via the portal, see [Create and run an Amazon DataZone data source for the AWS Glue Data Catalog](create-glue-data-source.md). 
**Note**  
You can use the Data Portal to enable data quality only for your AWS Glue inventory assets. In this release of Amazon DataZone enabling data quality for Amazon Redshift or custom types assets via the data portal is not supported.

  You can also use the APIs to enable data quality for your new or existing data sources. You can do this by invoking the [CreateDataSource](https://docs.aws.amazon.com/datazone/datazone/latest/APIReference/API_CreateDataSource.htmlAPI) or [UpdateDataSource](https://docs.aws.amazon.com/datazone/datazone/latest/APIReference/API_UpdateDataSource.htmlAPI) and setting the `autoImportDataQualityResult` parameter to 'True'.

  After data quality is enabled, you can run the data source on demand or on schedule. Each run can bring in up to 100 metrics per asset. There is no need to create forms or add metrics manually when using data source for data quality. When the asset is published, the updates that were made to the data quality form (up to 30 data points per rule of history) are reflected in the listing for the consumers. Subsequently, each new addition of metrics to the asset, is automatically added to the listing. There is no need to republish the asset to make the latest scores available to consumers. 

## Enabling data quality for custom asset types
<a name="datazone-data-quality-third-party"></a>

You can use the Amazon DataZone APIs to enable data quality for any of your custom type assets. For more information, see the following:
+ [PostTimeSeriesDataPoints](https://docs.aws.amazon.com/datazone/latest/APIReference/API_PostTimeSeriesDataPoints.html)
+ [ListTimeSeriesDataPoints](https://docs.aws.amazon.com/datazone/latest/APIReference/API_ListTimeSeriesDataPoints.html)
+ [GetTimeSeriesDataPoint](https://docs.aws.amazon.com/datazone/latest/APIReference/API_GetTimeSeriesDataPoint.html)
+ [DeleteTimeSeriesDataPoints](https://docs.aws.amazon.com/datazone/latest/APIReference/API_DeleteTimeSeriesDataPoints.html)

The following steps provide an example of using APIs or CLI to import third-party metrics for your assets in Amazon DataZone:

1. Invoke the `PostTimeSeriesDataPoints` API as follows:

   ```
   aws datazone post-time-series-data-points  \
   --cli-input-json file://createTimeSeriesPayload.json \
   ```

   with the following payload:

   ```
   "domainId": "dzd_5oo7xzoqltu8mf",
       "entityId": "4wyh64k2n8czaf",
       "entityType": "ASSET",
       "form": {
           "content": "{\n  \"evaluations\" : [ {\n    \"types\" : [ \"MaximumLength\" ],\n    \"description\" : \"ColumnLength \\\"ShippingCountry\\\" <= 6\",\n    \"details\" : { },\n    \"applicableFields\" : [ \"ShippingCountry\" ],\n    \"status\" : \"PASS\"\n  }, {\n    \"types\" : [ \"MaximumLength\" ],\n    \"description\" : \"ColumnLength \\\"ShippingState\\\" <= 2\",\n    \"details\" : { },\n    \"applicableFields\" : [ \"ShippingState\" ],\n    \"status\" : \"PASS\"\n  }, {\n    \"types\" : [ \"MaximumLength\" ],\n    \"description\" : \"ColumnLength \\\"ShippingCity\\\" <= 8\",\n    \"details\" : { },\n    \"applicableFields\" : [ \"ShippingCity\" ],\n    \"status\" : \"PASS\"\n  }, {\n    \"types\" : [ \"Completeness\" ],\n    \"description\" : \"Completeness \\\"ShippingStreet\\\" >= 0.59\",\n    \"details\" : { },\n    \"applicableFields\" : [ \"ShippingStreet\" ],\n    \"status\" : \"PASS\"\n  }, {\n    \"types\" : [ \"MaximumLength\" ],\n    \"description\" : \"ColumnLength \\\"ShippingStreet\\\" <= 101\",\n    \"details\" : { },\n    \"applicableFields\" : [ \"ShippingStreet\" ],\n    \"status\" : \"PASS\"\n  }, {\n    \"types\" : [ \"MaximumLength\" ],\n    \"description\" : \"ColumnLength \\\"BillingCountry\\\" <= 6\",\n    \"details\" : { },\n    \"applicableFields\" : [ \"BillingCountry\" ],\n    \"status\" : \"PASS\"\n  }, {\n    \"types\" : [ \"Completeness\" ],\n    \"description\" : \"Completeness \\\"biLlingcountry\\\" >= 0.5\",\n    \"details\" : {\n      \"EVALUATION_MESSAGE\" : \"Value: 0.26666666666666666 does not meet the constraint requirement!\"\n    },\n    \"applicableFields\" : [ \"biLlingcountry\" ],\n    \"status\" : \"FAIL\"\n  }, {\n    \"types\" : [ \"Completeness\" ],\n    \"description\" : \"Completeness \\\"Billingstreet\\\" >= 0.5\",\n    \"details\" : { },\n    \"applicableFields\" : [ \"Billingstreet\" ],\n    \"status\" : \"PASS\"\n  } ],\n  \"passingPercentage\" : 88.0,\n  \"evaluationsCount\" : 8\n}",
           "formName": "shortschemaruleset",
           "id": "athp9dyw75gzhj",
           "timestamp": 1.71700477757E9,
           "typeIdentifier": "amazon.datazone.DataQualityResultFormType",
           "typeRevision": "8"
       },
       "formName": "shortschemaruleset"
   }
   ```

   You can obtain this payload by invoking the `GetFormType` action:

   ```
   aws datazone get-form-type --domain-identifier <your_domain_id> --form-type-identifier amazon.datazone.DataQualityResultFormType --region <domain_region> --output text --query 'model.smithy'
   ```

1. Invoke the `DeleteTimeSeriesDataPoints` API as follows:

   ```
   aws datazone delete-time-series-data-points\
   --domain-identifier dzd_bqqlk3nz21zp2f \
   --entity-identifier dzd_bqqlk3nz21zp2f \
   --entity-type ASSET \
   --form-name rulesET1 \
   ```