

# Cost optimization recommendations (from Cost Optimization Hub)
<a name="table-dictionary-cor"></a>

The cost optimization recommendations table contains your cost optimization recommendations from Cost Optimization Hub. Cost Optimization Hub recommendations are consolidated from AWS Compute Optimizer and consist of over 15 types of optimizations, such as resource rightsizing, idle resource deletion, Savings Plans, and Reserved Instances. For more detailed information, see [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/cost-optimization-hub.html) in the *AWS Cost Management User Guide*.

The SQL table name for cost optimization recommendations is `COST_OPTIMIZATION_RECOMMENDATIONS`.

## Table configurations
<a name="cor-table-configurations"></a>

Table configurations are user-controlled properties that a user can set to change the data or schema of a table before it's queried in Data Exports. The table configurations are saved as a JSON statement and are either specified through user input in the AWS SDK/CLI or user selections in the console.

Cost optimization recommendations has the following table configurations:



| Configuration name | Description | Valid values | 
| --- | --- | --- | 
| INCLUDE\_ALL\_RECOMMENDATIONS | When set to "FALSE", only the highest savings value recommendation is kept in the table from any set of recommendations that are incompatible with one another. For example, only "Terminate instance" is kept from a recommendation to terminate an instance and a recommendation to rightsize the same instance.<br />When set to "TRUE", all recommendations are kept in the table.<br />This is also known as **Group related recommendations** in the Cost Optimization Hub console. For more information, see [Grouping related recommendations](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-group-recommendations.html) in the *AWS Cost Management User Guide*. | TRUE, FALSE | 
| FILTER | This allows you to filter recommendations based on different recommendation attributes. Filters are applied to the table before the savings deduplication algorithm is applied.<br />You can filter using the same parameters as in the Cost Optimization Hub console. For more information, see [Prioritizing your cost optimization opportunities](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-prioritize-opportunities.html) in the *AWS Cost Management User Guide*.<br />Filter statements are provided for this configuration using the same JSON structure that is used in the `filter` parameter in the Cost Optimization Hub `list-recommendations` API . It must be provided as a JSON string. For details, see the [`list-recommendations` structure](https://docs.aws.amazon.com/cli/latest/reference/cost-optimization-hub/list-recommendations.html#options). | Any JSON string that is valid for the Cost Optimization Hub list-recommendations API. | 

## Service-linked role
<a name="cor-table-slr"></a>

A service-linked role for Data Exports is required to create an export of the cost optimization recommendations table. For information on how to create the service-linked role, see [Service-linked roles for Data Exports](https://docs.aws.amazon.com/cost-management/latest/userguide/data-exports-SLR.html) in the *AWS Cost Management User Guide*.

## AWS Organizations support
<a name="cor-table-organizations"></a>

Cost Optimization Hub integrates with AWS Organizations to control whether a management account can see member account recommendations in Cost Optimization Hub. For more information, see [Getting started with Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-getting-started.html) in the *AWS Cost Management User Guide*.

The cost optimization recommendations table for a given AWS account inherits the same AWS Organizations settings you configured for Cost Optimization Hub. This means the content of the cost optimization recommendations table matches the recommendations that appear in Cost Optimization Hub for each AWS account.