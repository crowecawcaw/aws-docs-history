End of support notice: On March 31, 2027, AWS
will end support for AWS Service Management Connector. After March 31, 2027, you will
no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources.
For more information, see [AWS Service Management Connector end of support](smc-end-of-support.md "smc-end-of-support.md").

# Creating Connector for ServiceNow users

For each AWS account, the Connector for ServiceNow requires two
users:

- **AWS Sync User**: A user to sync AWS resources
  (such as portfolios, products, automation documents (runbook), Ops Items,
  Incident Manager incidents, change templates and requests, configuration
  items, and security Findings), sync AWS support cases, and AWS Health
  events and resources to ServiceNow .
- **AWS End User**: A user who can
  provision products as an end user, execute requests, and view resources that
  ServiceNow exposes. This role includes any required roles to provision and
  execute.

###### Note

To align with best practices, AWS recommends periodically rotating IAM user access keys. For more information, refer to [Manage IAM user access keys properly](../../../IAM/latest/UserGuide/id_credentials_access-keys.md#securing_access-keys "../../../IAM/latest/UserGuide/id_credentials_access-keys.md#securing_access-keys").
