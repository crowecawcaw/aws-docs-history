# Configure Linux subscription

discovery in License Manager

You can configure discovery of Linux subscriptions through the License Manager console, the
AWS CLI, the License Manager Linux subscription API, or the associated SDKs. When you activate
discovery of Linux subscriptions for the AWS Regions you specify, you can optionally
extend discovery to your accounts in AWS Organizations. If you no longer want to track subscription
utilization, you can also deactivate discovery.

###### Note

You can discover and display up to 5,000 resources per account per AWS Region by default.
To request an increase to these limits, use the
[limit increase form](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase "https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase").

###### Topics

- [Configure Linux subscription
  discovery](#linux-subscriptions-configure-discovery "#linux-subscriptions-configure-discovery")
- [Activate Red Hat Subscription Manager subscription
  discovery](#rhsm-subscription-discovery "#rhsm-subscription-discovery")
- [Resource discovery status reasons](#linux-subscriptions-status-reasons "#linux-subscriptions-status-reasons")
- [Deactivate discovery of Linux
  subscriptions](#linux-subscriptions-disable-discovery "#linux-subscriptions-disable-discovery")

## Configure Linux subscription

discovery

To configure Linux subscription discovery from the **Settings**
page in the License Manager console, follow these steps:

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. In the navigation pane, choose **Settings**. This
   opens the **Settings** page.
3. Open the **Linux subscriptions** tab, and choose
   **Configure**. This opens the
   **Configure Linux subscriptions settings** panel.
4. Select the **Source AWS Regions** where Linux subscription
   discovery should run.
5. To aggregate subscription data across your accounts in AWS Organizations, select
   **Link AWS Organizations**. This option only appears if AWS Organizations is
   configured for your account.
6. Review and acknowledge the option that grants AWS License Manager permission to create a
   service-linked role for Linux subscriptions.
7. Choose **Save configuration**.

## Activate Red Hat Subscription Manager subscription

discovery

To retrieve subscription information from Red Hat Subscription Manager (RHSM) on your behalf, License Manager must
provide your Red Hat customer account API credentials.

### Prerequisites

Before you activate subscription discovery, make sure that you've met the following
prerequisites.

- Default discovery for Linux subscriptions must be activated for your
  AWS account before you can configure RHSM subscription discovery. If default
  discovery is **Not activated**, see
  [Configure Linux subscription
  discovery](#linux-subscriptions-configure-discovery "#linux-subscriptions-configure-discovery").
- If you use a corporate Red Hat login provided by your Organization
  Administrator, ensure that your login ID has the following roles and permissions
  assigned:

      + **Role:** Manage your subscriptions
      + **Permissions:** `View All`, or
       `View/Edit All`

  If your login ID doesn't have the required roles and permissions, contact your
  Red Hat portal Organization Administrator and request to add them to your login.
  For more information about Red Hat roles and permissions, see [Roles and Permissions for
  Red Hat Customer Portal](https://access.redhat.com/articles/1757953 "https://access.redhat.com/articles/1757953"). For more information about how to contact your
  Red Hat Portal Organization Administrator, see [How do I
  know who my Organization Administrator is?](https://access.redhat.com/articles/customer-service-accounts#OrgAdmin "https://access.redhat.com/articles/customer-service-accounts#OrgAdmin") in the _Red Hat Customer
  Portal Knowledgebase_.

- To activate RHSM subscription discovery, you must provide the Red Hat customer
  account API offline token, or an AWS Secrets Manager secret that contains the offline token.
  To get your offline token, follow the steps described in [Generating a new offline token](https://docs.redhat.com/en/documentation/subscription_central/1-latest/html-single/using_apis_in_red_hat_subscription_management/index#using-rhsm-apis-con "https://docs.redhat.com/en/documentation/subscription_central/1-latest/html-single/using_apis_in_red_hat_subscription_management/index#using-rhsm-apis-con") on the
  _Red Hat Documentation_ website.

###### Important

Your security is important to us. Your Red Hat offline access token is stored
securely in Secrets Manager. License Manager uses your secret to generate a temporary access token
each time it requests subscription details from Red Hat.

### Activation

To activate RHSM discovery from the **Settings** page in
the License Manager console, follow these steps:

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. In the navigation pane, choose **Settings**.
3. On the **Settings** page, open the
   **Linux subscriptions** tab.
4. Choose **Edit** to update your Linux subscription settings.
   This opens the **Configure Linux subscriptions discovery** page.
5. To begin the activation process, select the **Activate Red Hat Subscription Manager (RHSM)
   discovery** check box. This displays the **Link
   RHSM account** panel.
6. Select the **Secret (Token)** option that applies
   for your secret, and follow remaining steps that depend on which
   option you choose.
7. ###### Option: Create a new secret – _recommended_

Provide the Red Hat offline access token and let License Manager create the
access secret in Secrets Manager on your behalf.

    1. Enter a name for your secret in **Secret name**.
    2. Paste your Red Hat offline access token into the
     **Offline token** box. Make sure that there are
     no extra spaces or line breaks before or after your token value. You
     can generate your Red Hat offline access token on the [Red Hat Subscription Manager API Tokens](https://access.redhat.com/management/api "https://access.redhat.com/management/api") page.###### Option: Select a secret

Select an existing secret in Secrets Manager that contains your Red Hat
offline access token. 8. (optional) Add tags for your secret. 9. Select the check box at the bottom of the page to acknowledge that by activating
Red Hat Subscription Manager discovery, you grant access to the AWS License Manager service to
collect data that relates to Red Hat subscriptions used on Amazon EC2
instances. 10. Choose **Activate**.

## Resource discovery status reasons

AWS License Manager will display a status and a corresponding status reason for each AWS Region
you choose to enable discovery for Linux subscriptions. The status reason will vary if you have
linked Linux subscriptions with AWS Organizations:

- In progress
- Successful
- Failed

The status reason that displays for each Region you choose will show up to two status
reasons at a time. The following table provides more detail:

| Status reason action                                                      | Description                                                                                                                                                                                                                                          |
| ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Account-onboard                                                           | Onboarding a single account.                                                                                                                                                                                                                         |
| Account-offboard                                                          | Offboarding a single account.                                                                                                                                                                                                                        |
| Org-onboard                                                               | Onboarding an entire organization.                                                                                                                                                                                                                   |
| Org-offboard                                                              | Offboarding an entire organization.                                                                                                                                                                                                                  | You can call the `UpdateServiceSettings` API and subsequently call the `GetServiceSettings` API to monitor the progress of enabling Linux subscriptions. Each status and status reason can apply to multiple Regions at once. The follow table provides more detail on the status and status reason: |
| Status                                                                    | Status reason                                                                                                                                                                                                                                        | Description                                                                                                                                                                                                                                                                                          |
| ---                                                                       | ---                                                                                                                                                                                                                                                  | ---                                                                                                                                                                                                                                                                                                  |
| In Progress                                                               | `"Region": "Account-Onboard: Pending"`                                                                                                                                                                                                               | Enabling Linux subscriptions for a single account is in progress.                                                                                                                                                                                                                                    |
| `"Region": "Org-Onboard: Pending"`                                        | Enabling Linux subscriptions for an organization is in progress.                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                      | `"Region": "Account-Offboard: Pending`                                                | Disabling Linux subscriptions for a single account is in progress.                                                                                                                                           |
| `"Region": "Org-Offboard: Pending`                                        | Disabling Linux subscriptions for an organization is in progress.                                                                                                                                                                                    |
| Successful                                                                | `"Region": "Account-Onboard: Successful"`                                                                                                                                                                                                            | Enabling Linux subscriptions for a single account was successful.                                                                                                                                                                                                                                    |
| `"Region": "Org-Onboard: Successful"`                                     | Enabling Linux subscriptions for an organization was successful.                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                      | `"Region": "Account-Offboard: Successful`                                             | Disabling Linux subscriptions for a single account was successful.                                                                                                                                           |
| `"Region": "Org-Offboard: Successful`                                     | Disabling Linux subscriptions for an organization was successful.                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                      | Failed                                                                                | `"Region": "Account-Onboard: Failed - Service-linked role not present"`                                                                                                                                      | Enabling Linux subscriptions for a single account has failed due to the required service-linked role not being created. Create the required role, and try again.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `"Region": "Account-Onboard: Failed - An internal error occurred"`        | Enabling Linux subscriptions for a single account has failed due to an internal error.                                                                                                                                                               |                                                                                                                                                                                                                                                                                                      | `"Region": "Org-Onboard: Failed - Account isn't the management account"`              | Enabling Linux subscriptions for an organization has failed due to the account performing the operation not being the organization's management account. Log in to the management account, and try again.    |
| `"Region": "Org-Onboard: Failed - Account isn't part of an organization"` | Enabling Linux subscriptions for an organization has failed due to the account performing the operation not being in an organization. Try the operation from an account in the organization, or add this account to the organization, and try again. |                                                                                                                                                                                                                                                                                                      | `"Region": "Org-Onboard: Failed - Linux subscriptions can't access the organization"` | Enabling Linux subscriptions for an organization has failed due to License Manager not having permissions to access the organization. Create the service-linked role for Linux subscriptions, and try again. | ## Deactivate discovery of Linux subscriptions You can deactivate discovery of Linux subscriptions from the AWS License Manager settings page. However, if you have activated discovery for ###### Warning If you disable discovery, all of your data previously discovered for Linux subscriptions will be removed from AWS License Manager. ###### To disable discovery for Linux subscriptions 1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/"). 2. In the left navigation pane, choose **Settings**. 3. On the **Settings** page, choose the **Linux subscriptions** tab and choose **Disable Linux subscription discovery**. 4. Enter `Disable` and then choose **Disable** to confirm deactivation. 5. (Optional) Remove the service-linked role used for Linux subscriptions. For more information, see [Delete a service-linked role for License Manager](linux-subscriptions-role.md "linux-subscriptions-role.md"). 6. (Optional) Disable trusted access between License Manager and your organization. For more information, see [AWS License Manager and AWS Organizations](../../../organizations/latest/userguide/services-that-can-integrate-license-manager.md "../../../organizations/latest/userguide/services-that-can-integrate-license-manager.md"). |
