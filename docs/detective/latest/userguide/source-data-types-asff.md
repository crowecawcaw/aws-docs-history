# \*\*AWS security

findings\*\*

**AWS security findings** is an optional data
source package that can be added to your Detective behavior graph.

You can view the available optional source packages, and their status in your account, from
the Settings page in the console or through the Detective API.

A 30 day free trial is provided for this data source. To learn more see [Free trial for optional data sources](free-trial-overview.md#free-trial-datasource "free-trial-overview.md#free-trial-datasource").

Enabling **AWS security findings** allows Detective to
use the findings from Security Hub CSPM aggregated by Security Hub from upstream services in a standard findings format called the AWS Security Format (ASFF), which eliminates the need for time-consuming data conversion efforts. Then it correlates
ingested findings across products to prioritize the most important ones.

###### \*\*Adding or removing AWS security findings as an optional data

source:\*\*

###### Note

The AWS security findings data source is enabled by default for new behavior graphs
created after May 16, 2023. For behavior graphs created before May 16, 2023 it must be enabled
manually.

1. Open the Detective console at [https://console.aws.amazon.com/detective/](https://console.aws.amazon.com/detective/ "https://console.aws.amazon.com/detective/").
2. From the navigation panel under **Settings**, choose
   **General**.
3. Under **Source packages**, select AWS security findings to enable this data source. If it is
   already enabled, select it again to stop ingesting AWS Security Finding Format (ASFF) findings
   into your behavior graph.

## Currently supported findings

Detective ingests all ASFF findings in Security Hub CSPM from services that are owned by Amazon
or AWS.

- To see the list of supported service integrations, see [Available AWS service
  integrations](../../../securityhub/latest/userguide/securityhub-internal-providers.md "../../../securityhub/latest/userguide/securityhub-internal-providers.md") in the AWS Security Hub CSPM User Guide.
- For the list of supported resources, see [Resources](../../../securityhub/latest/userguide/asff-resources.md "../../../securityhub/latest/userguide/asff-resources.md") in the
  AWS Security Hub CSPM User Guide.
- AWS Service Findings with a Compliance status not set to `FAILED` and cross-Region aggregated findings are not ingested.
