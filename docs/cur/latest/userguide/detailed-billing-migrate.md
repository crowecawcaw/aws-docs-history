

# Migrating from Detailed Billing Reports to Cost and Usage Reports
<a name="detailed-billing-migrate"></a>

Detailed Billing Reports (DBR) and AWS Cost and Usage Reports (AWS CUR) both provide information about your charges. However, if you're using DBR, we recommend you transfer your report to Cost and Usage Reports.

**Topics**
+ [Comparing benefits of the Cost and Usage Reports (AWS CUR)](#migrate-benefit-cur)
+ [Key differences between Detailed Billing Reports and Cost and Usage Reports](#migrate-key)
+ [Reporting on advanced charge types](#reporting-advanced-chargetype)

## Comparing benefits of the Cost and Usage Reports (AWS CUR)
<a name="migrate-benefit-cur"></a>

AWS CUR provides the most comprehensive source of information. You can use AWS CUR to understand individual costs in depth, and to analyze them in greater detail. This is especially useful at an enterprise scale. AWS CUR is helpful if you have complex cost management needs and require dedicated query or analytic-based systems. AWS CUR also provides detailed information about Reserved Instances (RI), including amortized costs.

### Comprehensive reservation information
<a name="migrate-reservation"></a>

Reserved Instances (RI), or reservations, offer a discounted hourly rate compared to On-Demand usage in exchange for committing to a one- or three-year term of service. This can result in significant savings. You can use AWS CUR to monitor and manage your reservation portfolio. AWS CUR provides you with detailed information, such as reservation Amazon Resource Numbers (ARNs), numbers of reservations, and total RIs. You can track your reservation-related discounts to specific resources to build a better understanding of your savings.

Detail Billing Reports (DBR) provide a subset of this metadata, but work is required to transform the required columns.

AWS CUR provides additional columns that are not available in DBR, such as information regarding your amortized reservation costs. For more information, see [Understanding your amortized reservation data](amortized-reservation.md).

### On-Demand pricing availability
<a name="migrate-ondemand"></a>

AWS CUR provides information regarding the On-Demand rates for each individual line item of usage. You can use this information to quantify your savings by subtracting the amount you paid from the On-Demand rate. This also gives you the flexibility of choosing to allocate your costs using public On-Demand rates.

DBR doesn’t contain information for On-Demand rates, but only the billed amount. This makes it difficult to calculate your overall savings or to allocate costs using On-Demand rates.

### Granular breakdown of discounts
<a name="migrate-granular"></a>

AWS CUR can access a granular view of the usage-based discounts. If discounts were applied, you can use AWS CUR to view the following:
+ Cost before being discounted
+ Discounted amount
+ Total cost after the discount was applied at the line item level

DBR does not contain a granular breakdown of your discounts.

### Automated data ingestion at scale
<a name="migrate-autodata"></a>

When you use AWS CUR, you can easily configure an event to trigger an automated data ingestion process, streamlining the process of refreshing the billing data in your in-house systems. AWS CUR data can automatically be refreshed when charges related to previous months are detected.

Additionally, AWS CUR is generated as multiple files, providing the added benefit of segmenting the data into smaller pieces. This way, you can ingest the data according to the processes used by multiple workers. Moreover, you can retry data downloads in smaller pieces.

AWS CUR is formatted in a way that enables you to locate and extract data quickly. This report is modeled from a manifest file that contains information for the overall structure of the data. This includes a list of every column that's contained in the report. Using this information, you can extend the report and include new information regarding your usage when it becomes available.

### Cross-product integration
<a name="migrate-crossproduct"></a>

AWS CUR is integrated with Amazon Redshift, Quick, and Amazon Athena. You can use AWS CUR to build an AWS-based cost management solution. AWS CUR also provides data in Parquet format. This provides you with more options for building out your own cost and usage reporting system. For more information, see [AWS Cost and Usage Reports Manifest Files](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-reports-costusage-files.html#manifests) in the *AWS Billing User Guide*.

## Key differences between Detailed Billing Reports and Cost and Usage Reports
<a name="migrate-key"></a>

There are a few differences between DBR and AWS CUR to consider after you migrate to AWS CUR. For example, you might need to adjust how you ingest the data into your systems.

### File structure
<a name="key-file"></a>

Detailed Billing Reports (DBR) are delivered as a single file. In contrast, AWS CUR are a consolidated set of files. In AWS CUR, you can view the following files in your Amazon S3 bucket:
+ A set of data files that contain all of your usage line items
+ A separate data file that contains all of your discounts (if applicable)
+ A manifest file that lists all of the data files that belong to a single report

### Column structure
<a name="key-column"></a>

DBR have a fixed list of columns, limiting its flexibility. AWS CUR don't have a fixed column structure, and instead allow you to freely add or remove columns as needed. When you begin using a new AWS service, AWS CUR can dynamically start to include new data in the report that might be useful in your case. The manifest file provides a map of all columns present in the report.


**Equivalent Column Names for DBR and AWS CUR**  

| DBR column name | AWS CUR column name | 
| --- | --- | 
| InvoiceId | bill/InvoiceId | 
| PayerAccountId | bill/PayerAccountId | 
| LinkedAccountId | lineItem/UsageAccountId | 
| ProductName | product/ProductName | 
| SubscriptionId | reservation/subscriptionid | 
| UsageType | lineItem/UsageType | 
| Operation | lineItem/Operation | 
| AvailabilityZone | lineItem/AvailabilityZone | 
| ReservedInstance | Not Supported | 
| ItemDescription | lineItem/LineItemDescription | 
| UsageStartDate | lineItem/UsageStartDate | 
| UsageEndDate | lineItem/UsageEndDate | 
| UsageQuantity | lineItem/UsageAmount | 
| BlendedRate | lineItem/BlendedRate | 
| BlendedCost | lineItem/BlendedCost | 
| UnBlendedRate | lineItem/UnblendedRate | 
| UnBlendedCost | lineItem/UnblendedCost | 
| ResourceId | lineItem/ResourceId | 
| RecordType | Not Supported | 
| PricingplanId | Not Supported | 
| RateID | pricing/RateId | 

**Note**  
There's no equivalent for RecordId in AWS CUR. But, you can gather this information by combining identity/LineItemId, identity/TimeInterval, and bill/BillType.


**Retrieving DBR RecordType values through AWS CUR**  

| RecordType values in DBR | Syntax to retrieve RecordType through AWS CUR | Use case | 
| --- | --- | --- | 
| LineItem | SELECT SUM(line\_item\_unblended\_cost) FROM [CUR] WHERE line\_item\_line\_item\_type = 'Usage' | Usage line item partitions out usage costs from one-time charges (for example, upfront RI payment). | 
| InvoiceTotal | SELECT (bill\_invoice\_id), sum(line\_item\_unblended\_cost) FROM [CUR] GROUP BY bill\_invoice\_id | You can use invoice total to reconcile your costs between Invoices and Cost and Usage Reports. | 
| AccountTotal | SELECT line\_item\_usage\_account\_id, sum(line\_item\_unblended\_cost) FROM [CUR] GROUP BY line\_item\_usage\_account\_id  | You can use account total to isolate costs related to your member accounts for charge back purposes. | 
| StatementTotal | SELECT SUM(line\_item\_unblended\_cost) FROM [CUR] | You can use statement total to understand your costs for the billing period. | 
| Discount | SELECT SUM(line\_item\_unblended\_cost) FROM [CUR] WHERE line\_item\_line\_item\_type = 'Discount'  | You can use discount line items to identify all of your discount-related line items. | 
| Rounding | Not yet supported | Not yet supported | 

## Reporting on advanced charge types
<a name="reporting-advanced-chargetype"></a>

### Refunds
<a name="reporting-advanced-refunds"></a>

AWS CUR: Refunds are identified by filtering for the `lineItem/LineItemDescription = ‘Refund’` string.

DBR: Refunds are identified by checking the ItemDescription column for the `‘Refund’` substring.

### Credits
<a name="reporting-advanced-credits"></a>

AWS CUR: Credits are identified by filtering for the `lineItem/LineItemDescription = ‘Credit’` string.

DBR: Credits are identified by checking the ItemDescription column for the `‘Credit’` substring.

### Taxes
<a name="reporting-advanced-taxes"></a>

AWS CUR: Taxes are identified by filtering for the `lineItem/LineItemDescription = ‘Tax’` string.

DBR: Taxes are identified by checking the ItemDescription column for the `‘Tax’` substring.

### Identifying reservation-related upfront costs
<a name="reporting-advanced-upfront"></a>

AWS CUR: Reservation-related upfront costs are identified by filtering for the `"lineItem/LineItemType" = 'Fee'` string.

DBR: Reservation-related upfront costs are identified by checking the UsageType column for the `'HeavyUsage'` substring, and whether the `'SubscriptionId'` is null.

### Identifying reservation-related monthly fees
<a name="reporting-advanced-monthly"></a>

AWS CUR: Reservation-related monthly fees are identified by filtering for the `"lineItem/LineItemType" = 'RIfee'` string.

DBR: Reservation-related monthly fees are identified by checking the UsageType column for the `'HeavyUsage'` substring.

### Identifying instances that received reserved instance benefits
<a name="identify-benefit-instance"></a>

AWS CUR: Reservation-related upfront fees are identified by filtering for the `"lineItem/LineItemType" = 'DiscountedUsage'` string.

DBR: Reservation-related upfront fees are identified by checking the ReservedInstance column for the `'Y'` substring. 