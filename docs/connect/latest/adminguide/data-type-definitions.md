

# Data type definitions for the Connect Customer data lake
<a name="data-type-definitions"></a>

This topic details the content in the Connect Customer data lake tables. Each table lists the column, type, and description of the content in the table.

There are two ways to access the analytics data lake and configure data to be shared: 
+ [Option 1: Use the Connect Customer console](access-datalake.md#option1-configure-data-to-be-shared)
+ [Option 2: Use CLI or CloudShell](access-datalake.md#option2-configure-data-to-be-shared)

If you are unable to access the scheduling tables by using Option 1, try using Option 2.

**Topics**
+ [Important things to know](#data-lake-important)
+ [Agent data in the Connect Customer data lake](data-lake-agent-data.md)
+ [Contact data in the Connect Customer data lake](data-lake-contact-data.md)
+ [Contact analytics data in the Connect Customer data lake](data-lake-contact-analytics-data.md)
+ [AI agent data in the Connect Customer data lake](data-lake-ai-agent-data.md)
+ [Flow data in the Connect Customer data lake](data-lake-flow-data.md)
+ [Bot analytics data in the Connect Customer analytics data lake](data-lake-botdata.md)
+ [Cases data in the Connect Customer analytics data lake](data-lake-cases-data.md)
+ [Configuration data in the Connect Customer data lake](data-lake-configuration-data.md)
+ [Forecasting data in the Connect Customer analytics data lake](data-lake-forecasting-data.md)
+ [Outbound campaigns data in the Connect Customer data lake](data-lake-outbound-campaigns-data.md)
+ [Resource tags data in the Connect Customer data lake](data-lake-resource-tags-data.md)
+ [Scheduling data in the Connect Customer analytics data lake](data-lake-scheduling.md)
+ [Reference queries for the Connect Customer data lake](data-lake-reference-queries.md)

## Important things to know
<a name="data-lake-important"></a>
+ The launch of new features results in additional to data fields or values to be added to the tables. When you develop applications that consume data lake data, we recommend that you build them to ignore the addition of new fields.
+ Connect Customer delivers contact records at least once. Contact records might be delivered again for multiple reasons, such as new information arriving after initial delivery which might update the data in the record. For example, when you use the [update-contact-attributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/update-contact-attributes.html) CLI command to update a contact record, Connect Customer delivers a new contact record.
+ For information about data retention, see [Data retention in the Connect Customer analytics data lake](data-lake-data-retention.md).