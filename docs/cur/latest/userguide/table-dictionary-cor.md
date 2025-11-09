# Cost optimization recommendations (from Cost

Optimization Hub)

The cost optimization recommendations table contains your cost optimization
recommendations from Cost Optimization Hub. Cost Optimization Hub recommendations are
consolidated from AWS Compute Optimizer and consist of over 15 types of optimizations,
such as resource rightsizing, idle resource deletion, Savings Plans, and Reserved
Instances. For more detailed information, see [Cost Optimization Hub](../../../cost-management/latest/userguide/cost-optimization-hub.md "../../../cost-management/latest/userguide/cost-optimization-hub.md") in the _AWS Cost Management User
Guide_.

The SQL table name for cost optimization recommendations is
`COST_OPTIMIZATION_RECOMMENDATIONS`.

## Table configurations

Table configurations are user-controlled properties that a user can set to change
the data or schema of a table before it's queried in Data Exports. The table
configurations are saved as a JSON statement and are either specified through user
input in the AWS SDK/CLI or user selections in the console.

Cost optimization recommendations has the following table configurations:

| Configuration name          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Valid values                                                                               |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| INCLUDE_ALL_RECOMMENDATIONS | When set to "FALSE", only the highest savings value<br>recommendation is kept in the table from any set of<br>recommendations that are incompatible with one another. For<br>example, only "Terminate instance" is kept from a recommendation<br>to terminate an instance and a recommendation to rightsize the<br>same instance.<br>When set to "TRUE", all recommendations are kept in the<br>table.<br>This is also known as \*_Group related<br>recommendations_<br>• in the Cost Optimization Hub<br>console. For more information, see [Grouping related<br>recommendations](../../../cost-management/latest/userguide/coh-group-recommendations.md "../../../cost-management/latest/userguide/coh-group-recommendations.md") in the _AWS Cost<br>Management User Guide_.                                                                                                                                                                                                                                                                    | TRUE, FALSE                                                                                |
| FILTER                      | This allows you to filter recommendations based on different<br>recommendation attributes. Filters are applied to the table<br>before the savings deduplication algorithm is applied.<br>You can filter using the same parameters as in the Cost<br>Optimization Hub console. For more information, see [Prioritizing your cost optimization<br>opportunities](../../../cost-management/latest/userguide/coh-prioritize-opportunities.md "../../../cost-management/latest/userguide/coh-prioritize-opportunities.md") in the _AWS Cost Management<br>User Guide_.<br>Filter statements are provided for this configuration using<br>the same JSON structure that is used in the `filter`<br>parameter in the Cost Optimization Hub<br>`list-recommendations` API . It must be provided<br>as a JSON string. For details, see the [`list-recommendations`<br>structure](../../../cli/latest/reference/cost-optimization-hub/list-recommendations.md#options "../../../cli/latest/reference/cost-optimization-hub/list-recommendations.md#options"). | Any JSON string that is valid for the Cost Optimization Hub<br>`list-recommendations` API. |

## Service-linked role

A service-linked role for Data Exports is required to create an export of the cost
optimization recommendations table. For information on how to create the
service-linked role, see [Service-linked roles for Data Exports](../../../cost-management/latest/userguide/data-exports-SLR.md "../../../cost-management/latest/userguide/data-exports-SLR.md") in the
_AWS Cost Management User Guide_.

## AWS Organizations support

Cost Optimization Hub integrates with AWS Organizations to control whether a
management account can see member account recommendations in Cost Optimization Hub.
For more information, see [Getting started with Cost Optimization Hub](../../../cost-management/latest/userguide/coh-getting-started.md "../../../cost-management/latest/userguide/coh-getting-started.md") in the _AWS Cost
Management User Guide_.

The cost optimization recommendations table for a given AWS account inherits the
same AWS Organizations settings you configured for Cost Optimization Hub. This
means the content of the cost optimization recommendations table matches the
recommendations that appear in Cost Optimization Hub for each AWS account.
