# Delegating an administrator account

You can delegate a member account in your organization as an administrator for Compute Optimizer. A
delegated administrator can access and manage Compute Optimizer recommendations. A delegated
administrator can also set recommendation preferences for your entire organization without
the need to access the management account. The management account controls the delegated
administrator option for its organization. Each organization can only have one delegated
administrator for Compute Optimizer at a time.

The delegated administrator can get and export recommendations, set recommendation preferences,
set member account opt-in status, and get projected utilization metrics.

###### Note

- You can limit your delegated administrator’s access to Compute Optimizer actions by setting up
  appropriate IAM permissions in your IAM policy. For more
  information, see [Policies and permissions in IAM](../../../IAM/latest/UserGuide/PoliciesOverview.md "../../../IAM/latest/UserGuide/PoliciesOverview.md").
- If you're the delegated administrator and you want to view org-level recommendations, see
  [Policies to grant access to Compute Optimizer for a management account of an organization](security-iam.md#organization-account-access "security-iam.md#organization-account-access").

## Procedure

Use the following procedures to register, update, or deregister an account as a
delegated administrator. You can do this using the Compute Optimizer console or the AWS CLI.

Console

###### To register or update an account as a

delegated administrator

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/ "https://console.aws.amazon.com/compute-optimizer/").
2. Choose **Account management** in the navigation pane.
3. In the **Organization opt-in by account**
   section, choose the account ID that you want to add as the delegated
   administrator.
4. For **Delegate**, choose **Register as delegated
   administrator**.
5. In the prompt that appears, choose **Confirm** if you agree to the change and to add the delegated administrator.

CLI

###### To register or update an account as a

delegated administrator

1. Log in as the management account of your
   organization.
2. Open a terminal or command prompt window.
3. Call the following API
   operation. Replace
   `123456789012` with your account ID.

```
`aws organizations register-delegated-administrator \
 --account-id `123456789012` \
 --service-principal compute-optimizer.amazonaws.com`
```

Console

###### To deregister a member account as a delegated administrator

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/ "https://console.aws.amazon.com/compute-optimizer/").
2. Choose **Account management** in the navigation pane.
3. In the **Organization opt-in by account** section, choose
   the current delegated administrator's account ID.
4. For **Delegate**, choose **Deregister as delegated administrator**.
5. In the prompt that appears, choose **Confirm** if you agree to the change and to remove the delegated administrator.

CLI

###### To deregister a member account as a delegated administrator

1. Log in as the management account of your organization.
2. Open a terminal or command prompt window.
3. Call the following API operation. Replace
   `123456789012` with your account ID.

```
`aws organizations deregister-delegated-administrator \
 --account-id `123456789012` \
 --service-principal compute-optimizer.amazonaws.com`
```

## Additional resources

- [Viewing the status of an organization's member accounts](view-account-opt-in.md "view-account-opt-in.md")
