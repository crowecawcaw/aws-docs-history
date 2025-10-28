# Delegating an administrator account

You can delegate a member account in your organization as an administrator for Cost Optimization Hub.
Delegating an administrator removes the need for you to use the management account to access
and manage Cost Optimization Hub on behalf of the organization. This also enables you to adopt an AWS
security best-practice, which recommends that you delegate responsibilities outside of the
management account where possible.

A delegated administrator can perform most Cost Optimization Hub actions, including getting
recommendations and setting preferences, without the need to access the management account.
However, the delegated administrator cannot change the opt-in status of the management
account.

The management account controls the delegated administrator option for its organization.
Each organization can only have one delegated administrator for Cost Optimization Hub at a time.

**To register or update an account as a delegated
administrator:**

Console

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Cost Management
   preferences**.
3. In the **Preferences** page, choose the
   **Cost Optimization Hub** tab.
4. Under **Organization and member account settings**, select
   **Delegated administrator**.
5. Choose the account ID that you want to add as the delegated
   administrator.
6. Choose **Save preferences**.

CLI

1. Log in as the management account of your organization.
2. Open a terminal or command prompt window.
3. Call the following API operation. Replace `123456789012` with your
   account ID.

```
aws organizations register-delegated-administrator \
                  --account-id 123456789012 \
                  --service-principal cost-optimization-hub.bcm.amazonaws.com
```

**To remove a member account as a delegated
administrator:**

Console

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Cost Management
   preferences**.
3. In the **Preferences** page, choose the
   **Cost Optimization Hub** tab.
4. Under **Organization and member account settings**, clear
   **Delegated administrator**.
5. Choose **Save preferences**.

CLI

1. Log in as the management account of your organization.
2. Open a terminal or command prompt window.
3. Call the following API operation. Replace `123456789012` with your
   account ID.

```
aws organizations deregister-delegated-administrator \
                  --account-id 123456789012 \
                  --service-principal cost-optimization-hub.bcm.amazonaws.com
```
