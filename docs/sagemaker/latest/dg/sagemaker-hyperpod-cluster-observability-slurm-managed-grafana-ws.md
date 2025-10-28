# Setting

up an Amazon Managed Grafana workspace

Create a new Amazon Managed Grafana workspace or update an existing Amazon Managed Grafana workspace with Amazon Managed Service for Prometheus as the
data source.

###### Topics

- [Create a Grafana workspace and set Amazon Managed Service for Prometheus as a data source](#sagemaker-hyperpod-cluster-observability-slurm-managed-grafana-ws-create "#sagemaker-hyperpod-cluster-observability-slurm-managed-grafana-ws-create")
- [Open the Grafana workspace and finish setting up the data source](#sagemaker-hyperpod-cluster-observability-slurm-managed-grafana-ws-connect-data-source "#sagemaker-hyperpod-cluster-observability-slurm-managed-grafana-ws-connect-data-source")
- [Import open-source Grafana dashboards](#sagemaker-hyperpod-cluster-observability-slurm-managed-grafana-ws-import-dashboards "#sagemaker-hyperpod-cluster-observability-slurm-managed-grafana-ws-import-dashboards")

## Create a Grafana workspace and set Amazon Managed Service for Prometheus as a data source

To visualize metrics from Amazon Managed Service for Prometheus, create an Amazon Managed Grafana workspace and set it up to use
Amazon Managed Service for Prometheus as a data source.

1. To create a Grafana workspace, follow the instructions at [Creating a workspace](../../../grafana/latest/userguide/AMG-create-workspace.md#creating-workspace "../../../grafana/latest/userguide/AMG-create-workspace.md#creating-workspace") in the _Amazon Managed Service for Prometheus User
   Guide_.
   1. In Step 13, select Amazon Managed Service for Prometheus as the data source.
   2. In Step 17, you can add the admin user and also other users in
      your IAM Identity Center.

For more information, see also the following resources.

- [Set up Amazon Managed Grafana for use with Amazon Managed Service for Prometheus](../../../prometheus/latest/userguide/AMP-amg.md "../../../prometheus/latest/userguide/AMP-amg.md") in the _Amazon Managed Service for Prometheus User
  Guide_
- [Use AWS data
  source configuration to add Amazon Managed Service for Prometheus as a data source](../../../grafana/latest/userguide/AMP-adding-AWS-config.md "../../../grafana/latest/userguide/AMP-adding-AWS-config.md") in the
  _Amazon Managed Grafana User Guide_

## Open the Grafana workspace and finish setting up the data source

After you have successfully created or updated an Amazon Managed Grafana workspace, select the
workspace URL to open the workspace. This prompts you to enter a user name and the
password of the user that you have set up in IAM Identity Center. You should log
in using the admin user to finish setting up the workspace.

1. In the workspace **Home** page, choose
   **Apps**, **AWS Data Sources**, and
   **Data sources**.
2. In the **Data sources** page, and choose the
   **Data sources** tab.
3. For **Service**, choose Amazon Managed Service for Prometheus.
4. In the **Browse and provision data sources** section,
   choose the AWS region where you provisioned an Amazon Managed Service for Prometheus workspace.
5. From the list of data sources in the selected Region, choose the one for
   Amazon Managed Service for Prometheus. Make sure that you check the resource ID and the resource alias of
   the Amazon Managed Service for Prometheus workspace that you have set up for HyperPod observability
   stack.

## Import open-source Grafana dashboards

After you've successfully set up your Amazon Managed Grafana workspace with Amazon Managed Service for Prometheus as the data
source, you'll start collecting metrics to Prometheus, and then should start seeing
the various dashboards showing charts, information, and more. The Grafana open
source software provides various dashboards, and you can import them into
Amazon Managed Grafana.

**To import open-source Grafana dashboards to
Amazon Managed Grafana**

1. In the **Home** page of your Amazon Managed Grafana workspace, choose
   **Dashboards**.
2. Choose the drop down menu button with the UI text
   **New**, and select **Import**.
3. Paste the URL to the [Slurm
   Dashboard](https://grafana.com/grafana/dashboards/4323-slurm-dashboard/ "https://grafana.com/grafana/dashboards/4323-slurm-dashboard/").

```
https://grafana.com/grafana/dashboards/4323-slurm-dashboard/
```

4. Select **Load**.
5. Repeat the previous steps to import the following dashboards.
   1. [Node Exporter Full Dashboard](https://grafana.com/grafana/dashboards/1860-node-exporter-full/ "https://grafana.com/grafana/dashboards/1860-node-exporter-full/")

   ```
   https://grafana.com/grafana/dashboards/1860-node-exporter-full/
   ```

   2. [NVIDIA DCGM Exporter Dashboard](https://grafana.com/grafana/dashboards/12239-nvidia-dcgm-exporter-dashboard/ "https://grafana.com/grafana/dashboards/12239-nvidia-dcgm-exporter-dashboard/")

   ```
   https://grafana.com/grafana/dashboards/12239-nvidia-dcgm-exporter-dashboard/
   ```

   3. [EFA Metrics Dashboard](https://grafana.com/grafana/dashboards/20579-efa-metrics-dev/ "https://grafana.com/grafana/dashboards/20579-efa-metrics-dev/")

   ```
   https://grafana.com/grafana/dashboards/20579-efa-metrics-dev/
   ```

   4. [FSx for Lustre Metrics Dashboard](https://grafana.com/grafana/dashboards/20906-fsx-lustre/ "https://grafana.com/grafana/dashboards/20906-fsx-lustre/")

   ```
   https://grafana.com/grafana/dashboards/20906-fsx-lustre/
   ```
