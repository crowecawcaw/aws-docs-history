

# Configuring alerting permissions
<a name="observability-alerting-permissions"></a>

Before you configure alerting, set up access to the data sources that your monitors query. The permissions you need depend on the data source: an Amazon OpenSearch Service domain or an Amazon OpenSearch Serverless collection.

## Data source prerequisites
<a name="observability-alerting-permissions-prerequisites"></a>

Alerting runs in the Observability workspace in OpenSearch UI. Before you begin, confirm the following:
+ An OpenSearch UI application with a workspace that has your data source attached. For more information, see [Using OpenSearch UI in Amazon OpenSearch Service](application.md).
+ Your user role trusts the OpenSearch UI service principal (`application.opensearchservice.amazonaws.com`). You configure this trust policy during application setup.

## Domain permissions
<a name="observability-alerting-permissions-domains"></a>

On an Amazon OpenSearch Service domain, alerting access is controlled by fine-grained access control. Assign the built-in alerting roles to the users who create and manage monitors:
+ `alerting_full_access` – Grants full access to alerting, including creating, updating, and deleting monitors and notification channels.
+ `alerting_read_access` – Grants read-only access to monitors, alerts, and notification channels.
+ `alerting_ack_alerts` – Grants access to view and acknowledge alerts.

For more information about fine-grained access control and the domain-level alerting experience, see [Fine-grained access control in Amazon OpenSearch Service](fgac.md) and [Configuring alerts in Amazon OpenSearch Service](alerting.md).

## Collection permissions
<a name="observability-alerting-permissions-collections"></a>

On an Amazon OpenSearch Serverless collection, monitors run as background jobs that require a collection data access policy. The policy grants collection and index permissions and includes `aoss:DelegateAccess` so that the alerting job can access the collection on your behalf. For the full policy and a description of each permission, see [Configuring permissions for alerting](serverless-configure-alerting.md#serverless-configure-alerting-permissions).