# Configuring projects enabled for the

Connector

The AWS Service Management Connector for Jira Service Management
requires the add-on to be associated to one or more Jira projects and
for JSM request types. You can configure which Connector features are
enabled for each Jira project.

###### To configure the Jira projects for AWS Service Catalog, AWS Config, AWS Systems Manager

Automation, AWS Systems Manager OpsCenter, AWS Security Hub, Support, and
AWS Systems Manager Incident Manager.

1. In the left navigation menu, under **AWS
   Service Management Connector**, choose **Connector settings**.
2. Under **Projects enabled for
   Connector**, you must enable at least one Jira project.
   You can [create a new Jira Service Management project](https://confluence.atlassian.com/servicedeskserver043/setting-up-your-service-desk-974367545.html "https://confluence.atlassian.com/servicedeskserver043/setting-up-your-service-desk-974367545.html") or add an
   existing one. Only users with access to the associated project can
   access the Connector. When you apply this update, the Connector adds
   the necessary issue types and other Jira items for AWS Service Catalog products
   to be available in those projects. You can return to this screen and
   add or remove projects at any time.
3. Projects initially take the default configuration for which
   Connector features are enabled. Choose **Edit** in a project row to change the configuration for
   individual projects. We permit projects to use more features than
   the default.
4. Choose **Save.**

###### Note

For end-users to be able to request AWS Service Catalog products, one or
more projects must be enabled and users must have Jira permissions
to create issues in the Jira project and Permission to Request in
the Jira settings for the AWS Account for at least one portfolio
with products.

**AWS Systems Manager Automation enablement
considerations**

We currently do not support fine-grained permissions in Jira for
which users and groups should be allowed to access which AWS Systems Manager
automation documents. If you enable a project for Systems Manager
Automation, then any user with permission to create issues in that
project can run any of the automations. You can restrict access by
limiting which users have access to projects with AWS Systems Manager
Automation enabled.
