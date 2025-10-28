# Integrations for ServiceNow

###### Note

Security Hub is in preview release and is subject to change.

This topic describes how to access the Security Hub console to configure an integration for ServiceNow ITSM.
Before completing any of the procedures in this topic, you must have a subscription to ServiceNow ITSM before you can add this integration.
For more information, see [the pricing page](https://www.servicenow.com/lpgp/pricing-itsm.html "https://www.servicenow.com/lpgp/pricing-itsm.html") on the ServiceNow website.

For accounts in an organization, only the delegated administrator can configure an integration.
The delegated administrator can manually use the create ticket feature for any member account findings.
Additionally, the delegated administrator can use [automation rules](security-hub-v2-automation-rules.md "security-hub-v2-automation-rules.md") to automatically create tickets for any findings associated with member accounts.
When defining an automation rule, the delegated administrator can set criteria, which can include all member accounts or specific member accounts.
For information about setting a delegated administrator, see [Setting a delegated administrator account in Security Hub](security-hub-v2-set-da.md "security-hub-v2-set-da.md").

For accounts not in an organization, all aspects of this feature are available.

## Prerequisites

You must complete the following prerequisites before configuring an integration for ServiceNow ITSM.
Otherwise, your integration between ServiceNow ITSM and Security Hub will not work.

### 1. Install Security Hubfindings integration for IT Service Management (ITSM)

The following procedure describes how to install Security Hub plugin.

1. Sign into your ServiceNow ITSM instance, and then open the application navigator.
2. Navigate to the [ServiceNow Store](https://store.servicenow.com/store "https://store.servicenow.com/store").
3. Search for _Security Hub findings integration for IT Service Management (ITSM)_, and then choose **Get** to install the application.

###### Note

In the settings for the Security Hub application, choose which action to take when new Security Hub findings are sent to your ServiceNow ITSM environment.
You can choose **Do nothing**, **Create incident**, **Create problem**, or **Create both (incident/problem)**.

### 2. Configure the Client Credentials grant type for inbound OAuth requests

You must configure this grant type for inbound OAuth requests.
For more information, see [Client Credentials grant type for Inbound OAuth is supported](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1645212 "https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB1645212") in the ServiceNow Support webpage.

### 3. Create an OAuth application

If you already created an OAuth application, you can skip this prerequisite.
For information about creating an OAuth application, see [Setting up OAuth](https://www.servicenow.com/docs/csh?topicname=client-credentials.html&version=latest "https://www.servicenow.com/docs/csh?topicname=client-credentials.html&version=latest").

## Configure an integration for ServiceNow ITSM

Security Hub can create incidents or problems automatically in ServiceNow ITSM.

###### To configure an integration for ServiceNow ITSM

1. Sign in to your AWS account with your credentials, and open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home?region=us-east-1](https://console.aws.amazon.com/securityhub/v2/home?region=us-east-1 "https://console.aws.amazon.com/securityhub/v2/home?region=us-east-1").
2. From the navigation pane, choose **Management**, and then choose **Integrations**.
3. Under **ServiceNow ITSM**, choose **Add integration**.
4. For **Details**, enter a name for your integration, and determine whether to enter an optional description for your integration.
5. For **Security settings**, decide how to encrypt your Jira Cloud credentials in Security Hub.
   If you choose **Service owned key**, an AWS owned key is used to encrypt your data.
   If you choose **Customized key**, you must enter the ARN for an existing customized key, or create a new key by choosing **Create an AWS KMS key**.
   For information about how to create a KMS key, see [Create a symmetric encryption KMS key](../../../kms/latest/developerguide/create-symmetric-cmk.md "../../../kms/latest/developerguide/create-symmetric-cmk.md").

###### Note

You cannot change these settings once you complete this configuration.
However, if you choose **Customized key**, you can edit your customized key policy at any time. 6. For **Authorizations**, enter ServiceNow ITSM URL, Client ID, and Client Secret. 7. For **Tags**, determine whether to create and add an optional tag to your integration. 8. Choose **Complete configuration**.
After you complete the configuration, you can view your configured integrations in the **Configured integrations** tab.
