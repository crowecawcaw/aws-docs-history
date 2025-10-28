# Amazon Managed Grafana

Amazon Managed Grafana provides an AWS IoT TwinMaker plugin so you can quickly integrate AWS IoT TwinMaker with
Grafana. Because Amazon Managed Grafana manages Grafana servers for you, you can visualize your data without
having to build, package, or deploy any hardware or any other Grafana infrastructure. For
more information about Amazon Managed Grafana, see [What is Amazon
Managed Grafana?](../../../grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.md "../../../grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.md").

###### Note

Amazon Managed Grafana currently supports version **1.3.1** of the AWS IoT TwinMaker Grafana plugin.

## Amazon Managed Grafana prerequisites

To use AWS IoT TwinMaker in an Amazon Managed Grafana dashboard, first complete the following
prerequisite:

- Create an AWS IoT TwinMaker workspace. For more information about creating workspaces, see [Getting
  started with AWS IoT TwinMaker](twinmaker-gs.md "twinmaker-gs.md").

###### Note

When you first create an Amazon Managed Grafana workspace in the AWS Management Console, AWS IoT TwinMaker isn't
listed. However, the plugin is already installed on all workspaces. You can find the
AWS IoT TwinMaker plugin on the open source Grafana plugins list. You can find the AWS IoT TwinMaker
datasource by choosing **Add a datasource** on the Datasources
page.

When you create an Amazon Managed Grafana workspace, an IAM role is created automatically to
manage the permissions for the Grafana instance. This is called the **Workspace
IAM Role**. It's the authentication provider option you'll use to configure all
AWS IoT TwinMaker datasources
for Grafana. Amazon Managed Grafana doesn't support automatically adding permissions for
AWS IoT TwinMaker, so you must set up these permissions manually. For more information about setting
up manual permissions, see [Creating a dashboard IAM role](dashboard-IAM-role.md "dashboard-IAM-role.md").
