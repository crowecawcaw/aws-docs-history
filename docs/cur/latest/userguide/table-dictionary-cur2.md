

# Cost and Usage Report (CUR) 2.0
<a name="table-dictionary-cur2"></a>

The CUR 2.0 table provides the same information as Cost and Usage Reports (CUR) with a few improvements.

Cost and Usage Reports 2.0 provides the following improvements over Cost and Usage Reports:
+ **Consistent schema**: CUR 2.0 contains a fixed set of columns, whereas the columns included for CUR can vary monthly depending on your usage of AWS services, cost categories, and resource tags.
+ **Nested data**: CUR 2.0 reduces data sparsity by collapsing certain columns from CUR into individual columns with key-value pairs of the collapsed columns. The nested keys can optionally be queried in Data Exports as separate columns to match the original CUR schema and data.
+ **Additional columns**: CUR 2.0 contains additional columns: **bill\_payer\_account\_name**, **line\_item\_usage\_account\_name**, **capacity\_reservation\_capacity\_reservation\_arn**, **capacity\_reservation\_capacity\_reservation\_status** and **capacity\_reservation\_capacity\_reservation\_type**. 

The SQL table name for CUR 2.0 is `COST_AND_USAGE_REPORT`.

## Table configurations
<a name="cur2-table-configurations"></a>

Table configurations are user-controlled properties that a user can set to change the data or schema of a table before it's queried in Data Exports. The table configurations are saved as a JSON statement and are either specified through user input in the AWS SDK/CLI or user selections in the console.

CUR 2.0 has the following table configurations:



| Configuration name | Description | Valid values | 
| --- | --- | --- | 
| TIME\_GRANULARITY | This configuration changes the cost and usage line items in the CUR 2.0 table to have different time granularities.<br />For example, selecting "HOURLY" will make all line items represent a single hour of usage. | HOURLY, DAILY, MONTHLY | 
| INCLUDE\_RESOURCES | This configuration changes the cost and usage line items in the CUR 2.0 table to have resource-level granularity and adds the "line\_item\_resource\_id" column to the table schema.<br />Enabling this configuration causes the CUR 2.0 table to have a line item for each resource that incurred usage for a given service, instead of showing combined total usage for that service.<br />Enabling this configuration can greatly increase the number of rows, and also the file size of your export. | TRUE, FALSE | 
| INCLUDE\_SPLIT\_COST\_ALLOCATION\_DATA | This configuration adds split cost allocation data and columns (split\_line\_item\_\*) to the CUR 2.0 table. This data indicates how the usage of certain AWS resources can be allocated to different business units or teams.<br />Enabling this configuration can add additional rows and columns which show how an EC2 instance can be allocated to different containers running in that instance. For more information, see [Understanding split cost allocation data](https://docs.aws.amazon.com/cur/latest/userguide/split-cost-allocation-data.html). | TRUE, FALSE | 
| INCLUDE\_CAPACITY\_RESERVATION\_DATA | **Note:** This configuration only adds data in the new columns starting November 1, 2025.<br />Enabling this configuration changes the cost and usage line items in the CUR 2.0 table to have resource-level granularity when an instance usage is split across multiple capacity reservations or used partially in a capacity reservationin an hour. This also adds 3 new columns to the table schema, which show how an EC2 instance is launched in a capacity reservation.  | TRUE, FALSE | 
| INCLUDE\_IAM\_PRINCIPAL\_DATA | **Note:** This configuration only adds data in the new columns starting April 8, 2026.<br />Enabling this configuration causes the CUR 2.0 table to include caller identity (IAM principal) allocation data for Amazon Bedrock model inference costs. This adds the line\_item\_iam\_principal column to the table schema, which contains the AWS IAM principal ARN of the caller making Bedrock inference requests. When IAM principal tags are activated as cost allocation tags, those tags also appear in the tags column with the iamPrincipal/ prefix (e.g., iamPrincipal/department, iamPrincipal/cost-center). Enabling this configuration can increase the number of CUR rows and file size. | TRUE, FALSE | 
| INCLUDE\_MANUAL\_DISCOUNT\_COMPATIBILITY | **Note:** This configuration only applies to AWS customers who have onboarded to the Discount Automation program where discounts are computed automatically.<br />This configuration changes the discounts in the CUR 2.0 table to appear as when they were added "manually" to the CUR, usually as separate line items, and removes two columns from the schema ("discount" and "total\_discount"). | TRUE, FALSE | 

## AWS Organizations support
<a name="cur2-table-organizations"></a>

The CUR 2.0 table inherits the settings you made in the consolidated billing feature in AWS Organizations. When consolidated billing is enabled, there are different behaviors for management and member accounts. If you’re using a management account, your CUR 2.0 table includes cost and usage data for the management account and all member accounts in your organization. If you’re using a member account, your CUR 2.0 table only includes cost and usage data for that member account.

After joining an organization, a member account can only export data for the time that the account has been a member of the organization. For example, let's say that a member account leaves organization A and joins organization B on the 15th of the month. Then, the member account creates an export. Because the member account created an export after joining organization B, the member account’s export of CUR 2.0 for the month only includes cost and usage data for the time that the account has been a member of organization B.

After a member account joins a new organization, the member account's cost and usage data is recorded in the new organization’s exports. This is the same outcome for a management account that converts to a member account and joins a new organization.

When a member account leaves an organization or converts to a standalone account, the member account can still access previous exports as long as they have permissions to the Amazon S3 bucket where the previous exports are stored.

For more information, see [Consolidated billing for AWS Organizations](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html) in the *AWS Billing User Guide*.

## CUR 2.0 column groups
<a name="cur2-column-groups"></a>

There are 125 possible columns in the CUR 2.0 table, grouped as follows:
+ **Bill:** Data about your bill for the billing period.
+ **Cost category:** Data about cost categories that apply to the line item.
+ **Capacity reservation:** Data about capacity reservation that applies to the line item.
+ **Discount:** Data about any discounts you are receiving.
+ **Identity:** Data to identify a line item.
+ **Line item:** Data about cost, usage, type of usage, pricing rates, product name, and more. 
+ **Pricing:** Data about the pricing for a line item.
+ **Product:** Data about the product that is being charged in the line item.
+ **Reservation:** Data about a reservation that applies to the line item.
+ **Resource tags:** Data about resource tags that apply to the line item.
+ **Savings plan:** Data about savings plans that apply to the line item.
+ **Split line item:** Data about split cost allocation for another line item.
+ **Capacity Reservation:** Data about capacity reservation that applies to the line item.
+ **Tags:** Data about user, account, cost category and resource tags.