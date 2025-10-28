# Create a new correlation

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

You can create correlations in the Explore correlations editor, or using the Grafana
**Administration** page in your Amazon Managed Grafana workspace.

**Prerequisites**

You must have permission to add new correlations. Only users with write
permissions to data sources can define new correlations.

## Creating a correlation in Explore’s

correlations editor

You can create a correlation in the Explore correlation editor. For more details,
see [Creating a correlation](v10-explore-correlations.md#v10-explore-corr-create-a-correlation "v10-explore-correlations.md#v10-explore-corr-create-a-correlation").

## Creating a correlation in

the Administration page

You can use the Grafana console **Administration** page to create a
correlation.

###### To create a correlation in the Administration page

1. Go to the **Administration** section in Grafana.
2. Under **Plugins and data**, open the
   **Correlations** page.
3. Choose the **Add** button in the top right corner.
4. Provide a **label** for the correlation.
5. (Optional) Provide an **description**.
6. Go to the next page.
7. Provide **target data source**.
8. Provide **target query** using variables.
9. Go to the next page.
10. Provide **source data source**.
11. Provide **results field**.
12. Add transformations if you need variables that are not fields in the
    source data source.
13. Choose **Add** to add a new transformation.
14. Select the type of a transformation.
15. Configure transformation depending on the selected type.
16. Save the correlation.

You can edit a correlation in the same way, but when editing, you can't change the
selected data sources.
