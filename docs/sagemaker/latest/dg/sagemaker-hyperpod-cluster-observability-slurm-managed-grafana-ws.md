

# Setting up an Amazon Managed Grafana workspace
<a name="sagemaker-hyperpod-cluster-observability-slurm-managed-grafana-ws"></a>

Create a new Amazon Managed Grafana workspace or update an existing Amazon Managed Grafana workspace with Amazon Managed Service for Prometheus as the data source.

**Topics**
+ [Create a Grafana workspace and set Amazon Managed Service for Prometheus as a data source](#sagemaker-hyperpod-cluster-observability-slurm-managed-grafana-ws-create)
+ [Open the Grafana workspace and finish setting up the data source](#sagemaker-hyperpod-cluster-observability-slurm-managed-grafana-ws-connect-data-source)
+ [Import open-source Grafana dashboards](#sagemaker-hyperpod-cluster-observability-slurm-managed-grafana-ws-import-dashboards)

## Create a Grafana workspace and set Amazon Managed Service for Prometheus as a data source
<a name="sagemaker-hyperpod-cluster-observability-slurm-managed-grafana-ws-create"></a>

To visualize metrics from Amazon Managed Service for Prometheus, create an Amazon Managed Grafana workspace and set it up to use Amazon Managed Service for Prometheus as a data source.

1. To create a Grafana workspace, follow the instructions at [Creating a workspace](https://docs.aws.amazon.com/grafana/latest/userguide/AMG-create-workspace.html#creating-workspace) in the *Amazon Managed Service for Prometheus User Guide*.

   1. In Step 13, select Amazon Managed Service for Prometheus as the data source.

   1. In Step 17, you can add the admin user and also other users in your IAM Identity Center.

For more information, see also the following resources.
+ [Set up Amazon Managed Grafana for use with Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-amg.html) in the *Amazon Managed Service for Prometheus User Guide*
+ [Use AWS data source configuration to add Amazon Managed Service for Prometheus as a data source](https://docs.aws.amazon.com/grafana/latest/userguide/AMP-adding-AWS-config.html) in the *Amazon Managed Grafana User Guide*

## Open the Grafana workspace and finish setting up the data source
<a name="sagemaker-hyperpod-cluster-observability-slurm-managed-grafana-ws-connect-data-source"></a>

After you have successfully created or updated an Amazon Managed Grafana workspace, select the workspace URL to open the workspace. This prompts you to enter a user name and the password of the user that you have set up in IAM Identity Center. You should log in using the admin user to finish setting up the workspace.

1. In the workspace **Home** page, choose **Apps**, **AWS Data Sources**, and **Data sources**.

1. In the **Data sources** page, and choose the **Data sources** tab.

1. For **Service**, choose Amazon Managed Service for Prometheus.

1. In the **Browse and provision data sources** section, choose the AWS region where you provisioned an Amazon Managed Service for Prometheus workspace.

1. From the list of data sources in the selected Region, choose the one for Amazon Managed Service for Prometheus. Make sure that you check the resource ID and the resource alias of the Amazon Managed Service for Prometheus workspace that you have set up for HyperPod observability stack.

## Import open-source Grafana dashboards
<a name="sagemaker-hyperpod-cluster-observability-slurm-managed-grafana-ws-import-dashboards"></a>

After you've successfully set up your Amazon Managed Grafana workspace with Amazon Managed Service for Prometheus as the data source, you'll start collecting metrics to Prometheus, and then should start seeing the various dashboards showing charts, information, and more. The Grafana open source software provides various dashboards, and you can import them into Amazon Managed Grafana.

**To import open-source Grafana dashboards to Amazon Managed Grafana**

1. In the **Home** page of your Amazon Managed Grafana workspace, choose **Dashboards**.

1. Choose the drop down menu button with the UI text **New**, and select **Import**.

1. Paste the URL to the [Slurm Dashboard](https://grafana.com/grafana/dashboards/4323-slurm-dashboard/).

   ```
   https://grafana.com/grafana/dashboards/4323-slurm-dashboard/
   ```

1. Select **Load**.

1. Repeat the previous steps to import the following dashboards.

   1. [Node Exporter Full Dashboard](https://grafana.com/grafana/dashboards/1860-node-exporter-full/)

      ```
      https://grafana.com/grafana/dashboards/1860-node-exporter-full/
      ```

   1. [NVIDIA DCGM Exporter Dashboard](https://grafana.com/grafana/dashboards/12239-nvidia-dcgm-exporter-dashboard/)

      ```
      https://grafana.com/grafana/dashboards/12239-nvidia-dcgm-exporter-dashboard/
      ```

   1. [EFA Metrics Dashboard](https://grafana.com/grafana/dashboards/20579-efa-metrics-dev/)

      ```
      https://grafana.com/grafana/dashboards/20579-efa-metrics-dev/
      ```

   1. [FSx for Lustre Metrics Dashboard](https://grafana.com/grafana/dashboards/20906-fsx-lustre/)

      ```
      https://grafana.com/grafana/dashboards/20906-fsx-lustre/
      ```