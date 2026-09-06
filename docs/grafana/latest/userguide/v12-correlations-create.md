

# Create a new correlation
<a name="v12-correlations-create"></a>

****  
This documentation topic is designed for Grafana workspaces that support **Grafana version 12.x**.  
For Grafana workspaces that support Grafana version 10.x, see [Working in Grafana version 10](using-grafana-v10.md).  
For Grafana workspaces that support Grafana version 9.x, see [Working in Grafana version 9](using-grafana-v9.md).  
For Grafana workspaces that support Grafana version 8.x, see [Working in Grafana version 8](using-grafana-v8.md).

You can create correlations in the Explore correlations editor, or using the Grafana **Administration** page in your Amazon Managed Grafana workspace.

**Prerequisites**

You must have permission to add new correlations. Only users with write permissions to data sources can define new correlations.

## Creating a correlation in Explore’s correlations editor
<a name="v12-correlations-create-explore"></a>

You can create a correlation in the Explore correlation editor. For more details, see [Creating a correlation](v12-explore-correlations.md#v12-explore-corr-create-a-correlation).

## Creating a correlation in the Administration page
<a name="v12-correlations-create-administration"></a>

You can use the Grafana console **Administration** page to create a correlation.

**To create a correlation in the Administration page**

1. Go to the **Administration** section in Grafana.

1. Under **Plugins and data**, open the **Correlations** page.

1. Choose the **Add** button in the top right corner.

1. Provide a **label** for the correlation.

1. (Optional) Provide an **description**.

1. Go to the next page.

1. Provide **target data source**.

1. Provide **target query** using variables.

1. Go to the next page.

1. Provide **source data source**.

1. Provide **results field**.

1. Add transformations if you need variables that are not fields in the source data source.

1. Choose **Add** to add a new transformation.

1. Select the type of a transformation.

1. Configure transformation depending on the selected type.

1. Save the correlation.

You can edit a correlation in the same way, but when editing, you can't change the selected data sources.