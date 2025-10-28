# Provisioning Grafana Alerting

resources

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

Alerting infrastructure is often complex, with many pieces of the pipeline that
often live in different places. Scaling this across multiple teams and organizations
is an especially challenging task. Grafana Alerting provisioning makes this process
easier by enabling you to create, manage, and maintain your alerting data in a way
that best suits your organization.

There are two options to choose from:

1. Provision your alerting resources using the Alerting Provisioning HTTP
   API.

###### Note

Typically, you cannot edit API-provisioned alert rules from the
Grafana UI.

In order to enable editing, add the x-disable-provenance header to the
following requests when creating or editing your alert rules in the
API:

```
POST /api/v1/provisioning/alert-rules
PUT /api/v1/provisioning/alert-rules/{UID}
```

2. Provision your alerting resources using Terraform.

###### Note

Currently, provisioning for Grafana Alerting supports alert rules, contact points,
mute timings, and templates. Provisioned alerting resources using file provisioning
or Terraform can only be edited in the source that created them and not from within
Grafana or any other source. For example, if you provision your alerting resources
using files from disk, you cannot edit the data in Terraform or from within
Grafana.

###### Topics

- [Create and manage
  alerting resources using Terraform](v10-alerting-setup-provision-terraform.md "v10-alerting-setup-provision-terraform.md")
- [Viewing provisioned
  alerting resources in Grafana](v10-alerting-setup-provision-view.md "v10-alerting-setup-provision-view.md")
