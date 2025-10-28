# Using a project with trusted identity propagation

enabled

Trusted identity propagation in IAM Identity Center enables administrators of AWS
services to grant permissions based on user attributes, such as user ID or group associations.
With trusted identity propagation, identity context is added to an IAM role to identify the
user requesting access to AWS resources. This context is propagated to other AWS
services.

For more information on how to enable trusted identity propagation in Amazon SageMaker Unified Studio, see
[Trusted Identity Propagation](../adminguide/trusted-identity-propagation.md "../adminguide/trusted-identity-propagation.md") in the Amazon SageMaker Unified Studio Administrator Guide.

Currently in Amazon SageMaker Unified Studio, you can use trusted identity propagation in the following use
cases:

- If you want to use Amazon SageMaker Unified Studio to run Amazon Athena queries using your single sign-on
  (SSO) user or group credentials.
- If you want to use Amazon SageMaker Unified Studio to connect to your existing Amazon Redshift clusters or
  Amazon Redshift Serverless endpoints that are IAM Identity Center enabled and run Amazon
  Redshift queries that are authorized based on your SSO credentials.
  Once your administrator has enabled trusted identity propagation for your Amazon SageMaker
  unified domain, you can use this feature in your Amazon SageMaker Unified Studio projects. The procedures below
  describe the currently supported use cases.

###### Topics

- [Create a new project with trusted identity
  propagation](#create-new-project-tip "#create-new-project-tip")
- [Working with Amazon Athena with trusted identity propagation](#athena-workgroup-tip "#athena-workgroup-tip")
- [Connect to existing Amazon Redshift
  clusters or Serverless endpoints with trusted identity propagation](#create-redshift-connection-tip "#create-redshift-connection-tip")

## Create a new project with trusted identity

propagation

First, you need to create a new project in your trusted identity propagation-enabled
domain. In the current release of Amazon SageMaker Unified Studio, trusted identity propagation is only supported
for projects that are created starting with 07/23/2025 and beyond. Trusted identity
propagation is NOT supported for projects that were created prior to 07/23/2025 even if they
live in a domain that has trusted identity propagation enabled.

You can follow the steps in [Create a new project](create-new-project.md "create-new-project.md") to create your trusted identity propagation enabled
project. When selecting a project profile with which you create your project, make sure to
select a project profile that has configured/set `enableTIPPermissions` to true.

## Working with Amazon Athena with trusted identity propagation

Once you create a project with trusted identity propagation enabled, this project
launches a default connection to an Amazon Athena workgroup - you can see AWS Data Catalog
under Lakehouse in the query editor's data explorer tab. You can then use the query editor
to write and run queries against this Amazon Athena workgroup. Your access to the data in
this Amazon Athena workgroup is authorized through your SSO credentials due to trusted
identity propagation.

**Considerations and limitations for this use
case:**

- There is only one connection for Athena in SM US (by design). Setting
  `enableTrustedIdentityPropagation` to true on an existing project does not
  create a new blueprint that can authorize on trusted identity propagation
  credentials.
- In the current release of Amazon SageMaker Unified Studio, the default project database which provides
  project users with data access based on their roles is not displayed in the query
  editor's data explorer tab in this new project with trusted identity propagation
  enabled. project role-based data access, will not appear in the SQL Editor's data
  explorer.
- Currently, users cannot use their SSO credentials via trusted identity propagation
  to subscribe to or publish data. Users can create a separate project without trusted
  identity propagation to view the default project data catalog and use the subscriptions
  capability.
- When a project has trusted identity propagation enabled, as you mouse over the nodes
  in the data explorer tab in the query editor, you'll see a tip informing you that all
  data authorization in this project is based on user SSO credentials with trusted
  identity propagation.
- In the current release of Amazon SageMaker Unified Studio, in Jupyter Lab, Visual ETL, and other tools
  where Amazon Athena is used but where trusted identity propagation is currently NOT
  supported, data explorer displays the default project database and users are authorized
  to access this data based on the project role.

## Connect to existing Amazon Redshift

clusters or Serverless endpoints with trusted identity propagation

Within trusted identity propagation-enabled project, you can connect to an existing
Amazon Redshift provisioned cluster or Amazon Redshift Serverless endpoint and then run
queries against that data with your SSO credentials. You can follow the steps described in
[Connecting to an existing Amazon Redshift resource](adding-a-existing-compute-connection.md "adding-a-existing-compute-connection.md"), and under
**Authentication**, make sure to select **IAM Identity
Center** since you want to access the resource with you SSO credentials and run
Amazon Redshift queries in Amazon SageMaker Unified Studio with trusted identity propagation.

**Considerations and limitations for this use
case:**

- When trusted identity propagation is enabled in a project, there is no default
  connection for Amazon Redshift. Users have to explicitly create a connection to an
  existing Amazon Redshift cluster or serverless endpoint that supports IdC with trusted
  identity propagation. For more information, see Connect to existing Amazon Redshift
  clusters or Serverless endpoints with trusted identity propagation
- Currently, users cannot use their SSO credentials via trusted identity propagation
  to subscribe to or publish data products.
- Trusted identity propagation is only supported if your Amazon SageMaker Unified Studio project and your
  Amazon Redshift cluster or serverless endpoint are in the same AWS account.
- Currently, IAM identity Center does not support trusted identity propagation across
  regions. Therefore, your IAM Identity Center instance and your Amazon SageMaker unified
  domain must be in the same AWS account.
