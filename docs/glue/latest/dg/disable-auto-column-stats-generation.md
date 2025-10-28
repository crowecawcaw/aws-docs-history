# Disabling catalog-level column statistics generation

You can disable automatic column statistics generation for new tables using
the AWS Lake Formation console, the `glue:UpdateCatalogSettings` API, or the
`glue:DeleteColumnStatisticsTaskSettings` API.

###### To disable the automatic column statistics generation at the

account-level

1. Open the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/").
2. On the left navigation bar, choose **Catalogs**.
3. On the **Catalog summary** page, choose **Edit** under **Optimization configuration**.
4. On the **Table optimization configuration** page,
   unselect the **Enable automatic statistics generation for the tables
   of the catalog** option.
5. Choose **Submit**.
