# Integrations for AWS Security Hub Jira Cloud

This topic describes how to integrate with Jira Cloud.
Before completing any of the procedures in this topic, you must purchase a Jira Cloud subscription plan.
For information about subscription plans, see [Pricing](https://www.atlassian.com/software/jira/pricing "https://www.atlassian.com/software/jira/pricing") on the Atlassian website.

This integration allows you to send Security Hub findings to Jira Cloud, manually or automatically, so you can manage them as part of your operational workflows.
For example, you can assign ownership to issues that need investigation and remediation.

For accounts in an organization, only the delegated administrator can configure an integration.
The delegated administrator can manually use the create ticket feature for any member account findings.
Additionally, the delegated administrator can use [automation rules](security-hub-v2-automation-rules.md "security-hub-v2-automation-rules.md") to automatically create tickets for any findings associated with member accounts.
When defining an automation rule, the delegated administrator can set criteria, which can include all member accounts or specific member accounts.
For information about setting a delegated administrator, see [Setting a delegated administrator account in Security Hub](security-hub-v2-set-da.md "security-hub-v2-set-da.md").

For accounts not in an organization, all aspects of this feature are available.

## Prerequisites

Prior to connecting Security Hub with your Jira Cloud environment you must ensure that the following configuration steps are done in your Jira environment.

- Install the AWS Security Hub for Jira cloud app.
- Have at least one software development project that is company managed.
- Assign the AWS app to the software development projects you want to receive findings from Security Hub.

Steps for each of these prerequisites are listed below.

### 1. Install the AWS Security Hub for Jira Cloud app

Security Hub has an app to support its integration with Jira.
This app installs custom fields and a custom issue type which allows Security Hub b to populate specific attributes about Security Hub findings.

1. Sign in to your Atlassian site as the administrator.
2. Choose **Settings**, and choose **Apps**.
3. If directed to the marketplace page, choose **Find new apps**.
   If directed to the apps page, choose **Explore apps**, and then search for _AWS Security Hub for Jira Cloud_.
   Then choose **Get it now**.

### 2. Create a project or verify existing projects

This step is required if you haven't created a project.
For information about how to create a project, see [Create a new project](https://support.atlassian.com/jira-software-cloud/docs/create-a-new-project/ "https://support.atlassian.com/jira-software-cloud/docs/create-a-new-project/") in the Jira Cloud Support documentation.

###### Requirements for creating a project

Make sure to do the following when creating a new project.

- Choose **Software development** for the project template.
- Choose **Company-managed** for the project type.

###### Requirements for existing projects

Any existing projects in your Jira environment, which will be integrated with Security Hub, must be a project type of **Company-managed**.

### 3. Add your projects to the AWS Security Hub for Jira Cloud app

In order for Security Hub to be able to successfully send findings to your Jira environment each project that you want to use with Security Hub must be associated with the AWS Security Hub for Jira Cloud app.
Associating a Jira project with the app ensures that the necessary custom fields for are associated with the project and can be populated when Security Hub sends findings to the project.

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

For additional information regarding Jira Cloud, see [Jira Cloud resources](https://support.atlassian.com/jira-software-cloud/resources/ "https://support.atlassian.com/jira-software-cloud/resources/") on the Atlassian website.

## Recommendations

###### Creating a dedicated system account for your Jira environment

Security Hub’s integration with Jira Cloud uses an OAuth connection that is associated with a specific user within your Jira instance.
Creating a dedicated system account to use for your Security Hub OAuth connection is recommended for your connection for the following reasons:

- A dedicated system user ensures that the connection is not associated with an employee who’s permissions to the Jira environment could change over time, impacting the ability for Security Hub to integrate with your Jira environment.
- Each issue that Security Hub creates in Jira will show a created by that is the username that was used to create the OAuth connection.
  Using a system account for the OAuth connection will result in this system account showing as the ticket creator, helping to provide visibility that the finding was created through the Security Hub integration and not manually by another Jira user.

## Configure an integration between Security Hub and Jira Cloud

The following procedure needs to be completed for each of your Jira Cloud projects that you want to send Security Hub findings to.

###### Note

When you create a Jira Cloud connector, you are redirected from the current AWS Region to `"https://3rdp.oauth.console.api.aws"`, so you can complete the connector registration.
Afterwards, you are returned to the AWS Region where the connector is being created.

###### To configure an integration for Jira Cloud

1. Sign in to your AWS account with your credentials, and open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home?region=us-east-1](https://console.aws.amazon.com/securityhub/v2/home?region=us-east-1 "https://console.aws.amazon.com/securityhub/v2/home?region=us-east-1").
2. From the navigation pane, choose **Management**, and then choose **Integrations**.
3. Choose **Add Jira Cloud**.
4. For **Details**, enter a unique and descriptive name for your integration, and determine whether to enter an optional description for your integration.
5. For **Encryptions** choose how you want to encrypt your integration credentials within Security Hub.
   - **Use AWS owned key** - With this option a Security Hub owned service key will be used to encrypt your integration credential data within Security Hub.
   - **Choose a different KMS key (advanced)** - With this option you choose an AWS KMS key that you have created which you want to be used for encrypting your integration credential data within Security Hub.
     For information about how to create an AWS KMS key, see [Create a AWS KMS key](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the _AWS Key Management Service Developer Guide_.
     If you choose to use your own key you must add policy statements to the KMS key that allow Security Hub access to the key.
     See [AWS KMS key policies for Security Hub ticketing integrations](securityhub-v2-integrations-key-policy.md "securityhub-v2-integrations-key-policy.md") for details on the necessary policies.

###### Note

You cannot change these settings once you complete this configuration.
However, If you choose **Customized key**, you can edit your customized key policy at any time. 6. (Optional) For **Tags**, create and add a tag to your integration.
You can add up to 50 tags. 7. For **Authorizations**, choose **Create connector and authorize**.
A pop-up appears where you choose **Allow** to complete the authorization.
After you complete the authorization, a check box appears letting you know the authorization was successful. 8. For **Configurations**, enter the Jira Cloud project ID. 9. Choose **Complete configuration**.
After you complete the configuration, you can view your configured integrations in the **Configured integrations** tab.

Once you have configured your integration with Jira you can test the connection to confirm that everything is configured properly in your Jira environment and in Security Hub.
See the [Testing configured ticketing integrations](securityhub-v2-test-ticket-integration.md "securityhub-v2-test-ticket-integration.md") for more details.

## Additional Jira integration details

###### Rate limit considerations

Jira enforces API rate limits to maintain service stability and ensure fair usage across their platform.
When using the AWS Security Hub integration with Jira, these rate limits may impact the processing of Security Hub findings, particularly in environments generating high volumes of findings.
This can result in delayed ticket creation, and in scenarios with extremely high finding volumes, some findings may not be processed into Jira tickets at all.
To optimize your integration, consider implementing filters on Automation rules in Security Hub to prioritize ticketing on most important findings, monitoring your Jira API usage through their admin console, and planning your workflow based on your Jira license tier's specific rate limits.
For business-critical implementations, contact your Jira administrator to review your rate limit allocations.

For detailed information about Jira API rate limits, refer to the [Rate limiting](http://developer.atlassian.com/cloud/jira/platform/rate-limiting/ "http://developer.atlassian.com/cloud/jira/platform/rate-limiting/") documentation on the Atlassian Developers Guide website.

###### Authentication and security

Jira API authentication requires proper OAuth 2.0 configuration for secure access.
Ensure your application follows Atlassian's security best practices for API integration.

Resources:

- Jira Rest APi v3: [https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/ "https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/")
- Implementing OAuth 2.0 (3LO): [https://developer.atlassian.com/cloud/oauth/getting-started/implementing-oauth-3lo/](https://developer.atlassian.com/cloud/oauth/getting-started/implementing-oauth-3lo/ "https://developer.atlassian.com/cloud/oauth/getting-started/implementing-oauth-3lo/")
- Administer Jira Cloud apps: [https://support.atlassian.com/jira-cloud-administration/resources/](https://support.atlassian.com/jira-cloud-administration/resources/ "https://support.atlassian.com/jira-cloud-administration/resources/")
- Manage Jira permissions: [https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/ "https://support.atlassian.com/jira-cloud-administration/docs/manage-project-permissions/")
