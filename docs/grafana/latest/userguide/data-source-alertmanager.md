# Connect to an Alertmanager data

source

Grafana includes built-in support for Prometheus Alertmanager. Once Grafana
alerting is configured, you can use the Grafana alerting UI to manage silences,
contact points as well as notification policies. A drop-down option in these pages
allows you to switch between Grafana and any configured Alertmanager data
sources.

**Alertmanager implementations**

[Prometheus](https://prometheus.io/ "https://prometheus.io/"), [Cortex](https://cortexmetrics.io/ "https://cortexmetrics.io/"), and [Grafana Mimir](https://grafana.com/docs/mimir/latest/ "https://grafana.com/docs/mimir/latest/")
implementations of Alertmanager are supported. You can specify implementation in the
data source settings page. Prometheus contact points and notification policies are
read-only in the Grafana alerting UI, as it does not support updating configuration
via HTTP API.

## Configuring an Alertmanager

data source

You can configure an Alertmanager data source to use with Grafana
alerting.

**Prerequisites**

To configure Alertmanager, you must have the following pre-requisite
complete:

- A Prometheus instance, with ingested metrics, and at least one alert
  or recording rule configured. You will need the URL for your
  workspace.
- Permissions defined for Amazon Managed Grafana to have read access to your alerts,
  alert groups, silences, and contact points from your Alertmanager
  implementation.

###### To configure an Alertmanager data source

1. From your Grafana console, in the Grafana menu, choose the
   **Data source** page under
   **Configuration**.
2. Choose **Add data source**, and select
   **Alertmanager** from the list of data source
   types.
3. Provide the following information for your new data source.
   - For **Name**, provide a name of your choosing
     for your data source.
   - For **Implementation**, choose your
     Alertmanager implementation – either
     **Prometheus**, **Mimir**,
     or **Cortex**.
   - Under **HTTP**, for **URL**,
     provide the Alertmanager URL. For Prometheus, this is the
     workspace URL, with `alertmanager` appended. For
     example,
     `https://myprometheus/workspaces/ws-example-1234-5678-abcd-xyz00000001/alertmanager`.
   - Under **Auth**, configure the authentication
     details needed to access your Alertmanager
     implementation.

4. Choose **Save & test** to finish your data source
   setup.

If your data source is set up correctly, you will see a message saying
**Health check passed**.
