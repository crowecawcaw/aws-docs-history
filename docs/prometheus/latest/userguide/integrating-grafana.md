# Integrate alerts with Amazon Managed Grafana or open source

Grafana

Alert rules that you have created in Alertmanager within Amazon Managed Service for Prometheus can be forwarded and
viewed in [Amazon Managed Grafana](https://aws.amazon.com/grafana/ "https://aws.amazon.com/grafana/") and [Grafana](https://grafana.com "https://grafana.com"), unifying your alert rules and alerts in a
single environment. Within Amazon Managed Grafana, you can view your alert rules and the alerts that are
generated.

## Prerequisites

Before starting to integrate Amazon Managed Service for Prometheus into Amazon Managed Grafana, you must have completed the following
prerequisites:

- You must have an existing AWS account and IAM credentials to create Amazon Managed Service for Prometheus
  and IAM roles programmatically.

For more information about creating an AWS account and IAM credentials,
see [Set up AWS](AMP-setting-up.md "AMP-setting-up.md").

- You must have an Amazon Managed Service for Prometheus workspace, and be ingesting data into it. To set up
  a new workspace, see [Create an Amazon Managed Service for Prometheus workspace](AMP-onboard-create-workspace.md "AMP-onboard-create-workspace.md"). You should also be familiar
  with the Prometheus concepts such as Alertmanager and Ruler. For more
  information about these topics, see the [Prometheus
  documentation](https://prometheus.io/docs/introduction/overview/ "https://prometheus.io/docs/introduction/overview/").
- You have an Alertmanager configuration and a rules file already configured in
  Amazon Managed Service for Prometheus. For more information about Alertmanager in Amazon Managed Service for Prometheus, see [Managing and forwarding alerts in Amazon Managed Service for Prometheus with alert
  manager](AMP-alert-manager.md "AMP-alert-manager.md"). For more
  information about rules, see [Using rules to modify or monitor metrics as they are
  received](AMP-Ruler.md "AMP-Ruler.md").
- You must either have Amazon Managed Grafana set up, or the open source version of Grafana
  running.
  - If you are using Amazon Managed Grafana, you must be using Grafana alerting. For
    more information see [Migrating legacy
    dashboard alerts to Grafana alerting](../../../grafana/latest/userguide/alert-opt-in.md "../../../grafana/latest/userguide/alert-opt-in.md").
  - If you are using the open source version of Grafana, you must be
    running version 9.1 or higher.

  ###### Note

  You can use earlier versions of Grafana, but you must [enable the unified alerting](https://grafana.com/docs/grafana/v8.4/alerting/unified-alerting/opt-in/ "https://grafana.com/docs/grafana/v8.4/alerting/unified-alerting/opt-in/") (Grafana alerting) feature,
  and you might have to set up a [sigv4
  proxy](https://github.com/awslabs/aws-sigv4-proxy "https://github.com/awslabs/aws-sigv4-proxy") to make calls from Grafana to Amazon Managed Service for Prometheus. For more
  information, see [Set up Grafana open source or
  Grafana Enterprise for use with Amazon Managed Service for Prometheus](AMP-onboard-query-standalone-grafana.md "AMP-onboard-query-standalone-grafana.md").

- Amazon Managed Grafana must have the following permissions for your Prometheus resources.
  You must add them to either the service-managed or customer-managed policies
  described in [https://docs.aws.amazon.com/grafana/latest/userguide/AMG-manage-permissions.html](../../../grafana/latest/userguide/AMG-manage-permissions.md "../../../grafana/latest/userguide/AMG-manage-permissions.md").
  - `aps:ListRules`
  - `aps:ListAlertManagerSilences`
  - `aps:ListAlertManagerAlerts`
  - `aps:GetAlertManagerStatus`
  - `aps:ListAlertManagerAlertGroups`
  - `aps:PutAlertManagerSilences`
  - `aps:DeleteAlertManagerSilence`

## Setting up Amazon Managed Grafana

If you have already set up rules and alerts in your Amazon Managed Service for Prometheus instance, the
configuration to use Amazon Managed Grafana as a dashboard for those alerts is done entirely within
Amazon Managed Grafana.

###### To configure Amazon Managed Grafana as your alerts dashboard

1. Open the Grafana console for your workspace.
2. Under **Configurations**, choose **Data
   sources**.
3. Either create or open your Prometheus data source. If you have not previously
   set up a Prometheus data source, see [Step 2: Add the
   Prometheus data source in Grafana](AMP-onboard-query-standalone-grafana.md#AMP-onboard-query-standalone-grafana-datasource "AMP-onboard-query-standalone-grafana.md#AMP-onboard-query-standalone-grafana-datasource") for more
   information.
4. In the Prometheus data source, select **Manage alerts via Alertmanager
   UI**.
5. Go back to the **Data sources** interface.
6. Create a new Alertmanager data source.
7. In the Alertmanager data source configuration page, add the following
   settings:
   - Set **Implementation** to
     `Prometheus`.
   - For the **URL** setting, use the URL for your
     Prometheus workspace, remove everything after the workspace ID, and
     append `/alertmanager` to the end. In the following example,
     replace the `variables` with you own (account
     specific) information:

   ```
   https://aps-workspaces.`US East (N. Virginia)`.amazonaws.com/workspaces/ws-example-1234-5678-abcd-xyz00000001/`alertmanager`.
   ```

   - Under **Auth**, turn on
     **SigV4Auth**. This tells Grafana to use the [AWS
     authentication](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md") for the requests.
   - Under **SigV4Auth Details**, for **Default
     Region**, provide the region of your Prometheus instance,
     for example `us-east-1`.
   - Set the **Default** option to
     `true`.

8. Choose **Save and test**.
9. Your Amazon Managed Service for Prometheus alerts should now be configured to work with your Grafana
   instance. Verify that you can see any **Alert rules**,
   **Alert groups** (including active alerts), and
   **Silences** from your Amazon Managed Service for Prometheus instance in the Grafana
   **Alerting** page.
