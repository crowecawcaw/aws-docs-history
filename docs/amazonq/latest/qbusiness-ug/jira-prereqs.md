# Prerequisites for connecting Amazon Q Business to Jira

Before you begin, make sure that you have completed the following
prerequisites.

**In Jira, make sure you have:**

- Created Jira API token authentication credentials that include a
  Jira ID (email ID with domain) and a Jira credential (Jira API token). See the
  [Atlassian documentation for information about managing API
  tokens](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/ "https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/").
- Noted the Jira account URL from your Jira account
  settings. For example,
  `https://company.atlassian.net/`.
- Noted your Jira project key ID from your Jira
  project settings if you want to crawl only specific Jira
  projects.
- If you want to have Amazon Q automatically rotate your secret,
  ensure that your IAM role includes the
  `secretsmanager:PutSecretValue` and
  `secretsmanager:UpdateSecret` permissions.
  If you have company-managed Jira projects, you need to perform the
  following:

- **Administer Jira Permissions**:
  The service account - the user configuring the Amazon Q Business
  integration - must have **Administer Jira** permissions. These
  permissions are required to read and interpret the permission schemes of
  company-managed projects to build appropriate Access Control Lists (ACLs). To
  assign this permission, go to the Settings icon in Jira, then
  navigate to **System > Global Permissions**. Add the
  _Administer Jira_ permission to the service
  account.
- **Email Visibility Settings**: Jira
  must provide access to the email address of the users for Amazon Q Business to correctly validate document-level permissions. To enable this, update
  profile settings by navigating to **Profile Picture → Manage Account >
  Privacy**, and setting **Email Visibility** to
  Anyone. This is a requirement due to limitations in Jira's API
  that impact integrations with external tools such as Amazon Q Business.
- **User and Project-Level Permissions**: The admin
  user associated with the integration must have at least **Browse
  Projects** permission in Jira. This can be granted
  directly or indirectly through a group, project role, or any other applicable
  configuration. To verify permissions, navigate to the specific
  Jira project, go to **Project Settings >
  Permissions**, and confirm that the admin user **Browse
  Projects** permission. To validate permissions, use the
  **Permission Helper**. Enter the user alias and select
  **Browse Projects** permission to check access.
  **In your AWS account, make sure you have:**

- Created a Amazon Q Business application.
- Created a [Amazon Q Business retriever and added an index](select-retriever.md "select-retriever.md").
- Created an [IAM role](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds") for your data source and, if using the Amazon Q API, noted the ARN of the IAM role.
- Stored your Jira authentication credentials in an AWS Secrets Manager
  secret and, if using the Amazon Q API, noted the ARN of the
  secret.

###### Note

If you’re a console user, you can create the IAM role and Secrets Manager
secret as part of configuring your Amazon Q application on the
console.
For a list of things to consider while configuring your data source, see [Data source connector configuration best practices](connector-best-practices.md "connector-best-practices.md").

###### Note

For more information on connecting Jira to Amazon Q Business,
see [Improve the productivity of your customer support and project management teams
using Amazon Q Business and Atlassian Jira](https://aws.amazon.com/blogs/machine-learning/improve-the-productivity-of-your-customer-support-and-project-management-teams-using-amazon-q-business-and-atlassian-jira/ "https://aws.amazon.com/blogs/machine-learning/improve-the-productivity-of-your-customer-support-and-project-management-teams-using-amazon-q-business-and-atlassian-jira/") in the _AWS
Machine Learning Blog_.
