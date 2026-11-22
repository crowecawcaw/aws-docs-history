

# Delegating an administrator account

With AWS Compute Optimizer, you can make one member account in your organization the delegated administrator. This account can view and manage Compute Optimizer recommendations for the whole organization. It can do this without signing in to the management account.

The management account chooses the delegated administrator. Each organization can have only one delegated administrator for Compute Optimizer at a time.

As the delegated administrator, you can do the following:
+ Get and export recommendations.
+ Set recommendation preferences.
+ Set the opt-in status of member accounts.
+ Get projected utilization metrics.

**Note**  
Keep the following in mind about delegated administrator access:  
You can limit your delegated administrator's access to Compute Optimizer actions. To do this, set up IAM permissions in your IAM policy. For more information, see [Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/PoliciesOverview.html).
If you're the delegated administrator and you want to view org-level recommendations, see [ Policies to grant access to Compute Optimizer for a management account of an organization](https://docs.aws.amazon.com/compute-optimizer/latest/ug/security-iam.html#organization-account-access).

## Procedure
<a name="da-process"></a>

Before you begin, make sure that you're signed in to the management account of your organization and that you have the IAM permissions required to manage delegated administrators. Only the management account can register or deregister a delegated administrator.

Use the following procedures to register, update, or remove a delegated administrator. You can use the Compute Optimizer console or the AWS CLI.

### Registering or updating a delegated administrator in Compute Optimizer
<a name="register-da"></a>

------
#### [ Console ]

**To register or update an account as a delegated administrator**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. Choose **Account management** in the navigation pane.

1. In the **Organization opt-in by account** section, choose the account ID that you want to add as the delegated administrator.

1. For **Delegate**, choose **Register as delegated administrator**.

1. In the prompt that appears, choose **Confirm** if you agree to the change and to add the delegated administrator.

------
#### [ CLI ]

**To register or update an account as a delegated administrator**

1. Log in as the management account of your organization.

1. Open a terminal or command prompt window.

1. Call the following API operation. Replace {{123456789012}} with your account ID.

   ```bash
   aws organizations register-delegated-administrator \
                                           --account-id {{123456789012}} \
                                           --service-principal compute-optimizer.amazonaws.com
   ```

------

### Deregistering a delegated administrator in Compute Optimizer
<a name="deregister-da"></a>

------
#### [ Console ]

**To deregister a member account as a delegated administrator**

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/).

1. Choose **Account management** in the navigation pane.

1. In the **Organization opt-in by account** section, choose the current delegated administrator's account ID.

1. For **Delegate**, choose **Deregister as delegated administrator**.

1. In the prompt that appears, choose **Confirm** if you agree to the change and to remove the delegated administrator.

------
#### [ CLI ]

**To deregister a member account as a delegated administrator**

1. Log in as the management account of your organization.

1. Open a terminal or command prompt window.

1. Call the following API operation. Replace {{123456789012}} with your account ID.

   ```bash
   aws organizations deregister-delegated-administrator \ 
                                           --account-id {{123456789012}} \
                                           --service-principal compute-optimizer.amazonaws.com
   ```

------

## Additional resources
<a name="da-resources"></a>
+ [Viewing the status of an organization's member accounts](view-account-opt-in.md)