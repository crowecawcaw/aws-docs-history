# Visualize alerts from Amazon Managed Service for Prometheus

You can visualize your Amazon Managed Service for Prometheus or Prometheus alerts in Amazon Managed Grafana by
configuring an Alertmanager data source for Prometheus data sources that you are
already connected to.

**Prerequisites**

To configure an Alertmanager for use with Amazon Managed Service for Prometheus, you must have the
following pre-requisites complete:

- An [Amazon Managed Service for Prometheus](../../../prometheus/latest/userguide/AMP-onboard-create-workspace.md "../../../prometheus/latest/userguide/AMP-onboard-create-workspace.md") instance, with ingested metrics, and at least one
  alert or recording rule configured. You will need the URL for your
  workspace (from the details of your workspace in Amazon Managed Service for Prometheus you can see
  the **Endpoint** URL. The workspace URl is the Endpoint
  URL without the `api/v1/remote_write` at the end).
- An Amazon Managed Grafana workspace [created](AMG-create-workspace.md "AMG-create-workspace.md") with the Prometheus instance [configured as a data
  source](prometheus-data-source.md "prometheus-data-source.md").
- Amazon Managed Grafana must have the following permissions for your Prometheus
  resources. You must add them to either the service-managed or
  customer-managed policies described in [Amazon Managed Grafana permissions and policies for AWS data
  sources](AMG-manage-permissions.md "AMG-manage-permissions.md").
  - `aps:ListRules`
  - `aps:ListAlertManagerSilences`
  - `aps:ListAlertManagerAlerts`
  - `aps:GetAlertManagerStatus`
  - `aps:ListAlertManagerAlertGroups`
  - `aps:PutAlertManagerSilences`
  - `aps:DeleteAlertManagerSilence`

###### To configure an Alertmanager data source for use with Amazon Managed Service for Prometheus

1. From your Grafana console, in the Grafana menu, choose the
   **Data source** page under
   **Configuration**.
2. Choose **Add data source**, and select
   **Alertmanager** from the list of data source
   types.
3. Provide the following information for your new data source.
   - For **Implementation**, choose
     **Prometheus**.
   - Under **HTTP**, for **URL**,
     provide the Prometheus workspace URL, with
     `alertmanager` appended. For example,
     `https://aps-workspaces.us-east1.amazonaws.com/workspaces/ws-example-1234-5678-abcd-xyz00000001/alertmanager`.
   - Under **Auth**, turn on
     **SigV4Auth**. This tells Grafana to use
     the [AWS
     authentication](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md") for the requests.
   - Under **SigV4Auth Details**, for
     **Default Region**, provide the region of
     your Prometheus instance, for example
     `us-east-1`.

4. Choose **Save & test** to finish your data source
   setup.

If your data source is set up correctly, you will see a message saying
**Health check passed**.

###### To connect your new Alertmanager data source to the Prometheus data

source

1. From your Grafana console, in the Grafana menu, choose the
   **Data source** page under
   **Configuration**.
2. Select your original Amazon Managed Service for Prometheus data source and turn on the
   **Manage alerts via Alerting UI** toggle
   switch.
3. Choose **Save & test** to finish configuring your
   data source.
