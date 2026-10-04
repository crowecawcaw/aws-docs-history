

# Provisioning Grafana Alerting resources
<a name="v13-alerting-setup-provision"></a>

****  
This documentation topic is designed for Grafana workspaces that support **Grafana version 13.x**.  
For Grafana workspaces that support Grafana version 12.x, see [Working in Grafana version 12](using-grafana-v12.md).  
For Grafana workspaces that support Grafana version 10.x, see [Working in Grafana version 10](using-grafana-v10.md).  
For Grafana workspaces that support Grafana version 9.x, see [Working in Grafana version 9](using-grafana-v9.md).

Alerting infrastructure is often complex, with many pieces of the pipeline that often live in different places. Scaling this across multiple teams and organizations is an especially challenging task. Grafana Alerting provisioning makes this process easier by enabling you to create, manage, and maintain your alerting data in a way that best suits your organization.

There are two options to choose from:

1. Provision your alerting resources using the Alerting Provisioning HTTP API.
**Note**  
Typically, you cannot edit API-provisioned alerting resources from the Grafana UI.  
In order to enable editing, add the `X-Disable-Provenance` header when creating or editing resources through the provisioning API. This applies to all provisioning write operations, not only alert rules. For example, for alert rules:  

   ```
   POST /api/v1/provisioning/alert-rules
   PUT /api/v1/provisioning/alert-rules/{UID}
   ```

1. Provision your alerting resources using Terraform.

**Note**  
Provisioning for Grafana Alerting supports alert rules, rule groups, contact points, mute timings, notification policies, and templates. Export endpoints are available for all of these except templates.  
Alerting resources provisioned using Terraform can only be edited in Terraform, not from within Grafana. Resources provisioned through the HTTP API behave the same way unless you send the `X-Disable-Provenance` header when creating them.

**Topics**
+ [Create and manage alerting resources using Terraform](v13-alerting-setup-provision-terraform.md)
+ [Viewing provisioned alerting resources in Grafana](v13-alerting-setup-provision-view.md)