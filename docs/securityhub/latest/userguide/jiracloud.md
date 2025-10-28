# Integrations for AWS Security Hub Jira Cloud

###### Note

Security Hub is in preview release and is subject to change.

This topic describes how to access the Security Hub console to configure an integration for Jira Cloud.
Before completing any of the procedures in this topic, you must purchase a Jira Cloud subscription plan.
For information about subscription plans, see [Pricing](https://www.atlassian.com/software/jira/pricing#:~:text=Up%20to%2050%2C000%20users%20on,that%20drive%20better%20decision%20making. "https://www.atlassian.com/software/jira/pricing#:~:text=Up%20to%2050%2C000%20users%20on,that%20drive%20better%20decision%20making.") on the Atlassian website.

For accounts in an organization, only the delegated administrator can configure an integration.
The delegated administrator can manually use the create ticket feature for any member account findings.
Additionally, the delegated administrator can use [automation rules](security-hub-v2-automation-rules.md "security-hub-v2-automation-rules.md") to automatically create tickets for any findings associated with member accounts.
When defining an automation rule, the delegated administrator can set criteria, which can include all member accounts or specific member accounts.
For information about setting a delegated administrator, see [Setting a delegated administrator account in Security Hub](security-hub-v2-set-da.md "security-hub-v2-set-da.md").

For accounts not in an organization, all aspects of this feature are available.

## Prerequisites

You must complete the following prerequisites before configuring an integration for Jira Cloud.
Otherwise, your integration between Jira Cloud and Security Hub will not work.

### 1. Install the AWS Security Hub for Jira Cloud app

The following procedure describes how to install the app.

1. Sign in to your Atlassian site as the administrator.
2. Choose **Settings**, and choose **Apps**.
3. If directed to the marketplace page, choose **Find new apps**.
   If directed to the apps page, choose **Explore apps**, and then search for _AWS Security Hub for Jira Cloud_.
   Then choose **Get it now**.

### 2. Create a project

This step is required if you haven't created a project.
For information about how to create a project, see [Create a new project](https://support.atlassian.com/jira-software-cloud/docs/create-a-new-project/ "https://support.atlassian.com/jira-software-cloud/docs/create-a-new-project/") in the Jira Cloud Support documentation.

###### Requirements for creating a project

Make sure to do the following when creating a new project.

- Choose **Software development** for the project template.
- Choose **Company-managed** for the project type.
- Make a note of the project key.

### 3. Add your software development projects to the AWS Security Hub for Jira Cloud app

The following procedure describes how to add your software development projects to the Security Hub for Jira Cloud app.

1. Sign in to your Atlassian site as the administrator.
2. Choose **Settings**, and choose **Apps**.
3. From the list of apps, choose **AWS Security Hub for Jira Cloud**.
4. Choose the **Connector settings** tab.
5. Under **Projects enabled**, choose **Add Jira Project**.
   1. From the dropdown, choose **Add all**, or select a project.
      Repeat this part of the step if you want to add more than one project, but not all projects.
   2. Choose **Save**.

You can verify which projects have been successfully installed from the **Installation Manager** tab.
You can also verify configurations for fields, screens, statuses, and workflows from the **Installation Manager** tab.

###### Note

You can choose the **Installation Manager** tab to verify all of the projects you selected were installed successfully.

For additional information regarding Jira Cloud, see [Jira Cloud resources](https://support.atlassian.com/jira-software-cloud/resources/ "https://support.atlassian.com/jira-software-cloud/resources/") on the Atlassian website.

## Recommendations

The following are recommendations to consider before configuring an integration for Jira Cloud.

- Create a dedicated system account in Jira Cloud.
- Use one system account per Jira Cloud instance.

## Configure an integration for Jira Cloud

Security Hub automatically creates issues in Jira Cloud.
This integration allows you to send Security Hub findings to Jira Cloud, so you can manage them as part of your operational workflows.
For example, you can assign ownership to issues that need investigation and remediation.
You must complete the following procedure for each of your Jira Cloud projects that you want to send Security Hub findings to.

###### Note

When you create a Jira Cloud connector, you are redirected from the current AWS Region to `"https://3rdp.oauth.console.api.aws"`, so you can complete the connector registration.
Afterwards, you are returned to the AWS Region where the connector is being created.

###### To configure an integration for Jira Cloud

1. Sign in to your AWS account with your credentials, and open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home?region=us-east-1](https://console.aws.amazon.com/securityhub/v2/home?region=us-east-1 "https://console.aws.amazon.com/securityhub/v2/home?region=us-east-1").
2. From the navigation pane, choose **Management**, and then choose **Integrations**.
3. Choose **Add Jira Cloud**.
4. For **Details**, enter a unique and descriptive name for your integration, and determine whether to enter an optional description for your integration.
5. For **Security settings**, decide how to encrypt your Jira Cloud credentials in Security Hub.
   If you choose **Service owned key**, an AWS owned key is used to encrypt your data.
   If you choose **Customized key**, you must enter the ARN for an existing customized key, or create a new key by choosing **Create an AWS KMS key**.
   For information about how to create an KMS key, see [Create a symmetric encryption KMS key](../../../kms/latest/developerguide/create-symmetric-cmk.md "../../../kms/latest/developerguide/create-symmetric-cmk.md") .

###### Note

You cannot change these settings once you complete this configuration.
However, If you choose **Customized key**, you can edit your customized key policy at any time. 6. (Optional) For **Tags**, create and add a tag to your integration.
You can add up to 50 tags. 7. For **Authorizations**, choose **Create connector and authorize**.
A pop-up appears where you choose **Allow** to complete the authorization.
After you complete the authorization, a check box appears letting you know the authorization was successful. 8. For **Configurations**, enter the Jira Cloud project ID. 9. Choose **Complete configuration**.
After you complete the configuration, you can view your configured integrations in the **Configured integrations** tab.
