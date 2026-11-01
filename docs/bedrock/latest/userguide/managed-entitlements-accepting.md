

# Accepting and activating grants
<a name="managed-entitlements-accepting"></a>

After a grant has been distributed to a member account, the grant must be accepted and activated before the third-party Bedrock model can be used. The acceptance and activation workflow differs depending on your organization configuration.

**Note**  
If your administrator distributed a private offer from AWS Marketplace, your grant is already accepted and activated, and no action is required from you. The steps on this page apply to grants created in AWS License Manager.

## For organizations with all features enabled
<a name="managed-entitlements-all-features"></a>

When you create a grant to a member account in an organization with all features enabled, the grant is automatically accepted and appears in a Disabled state. Either the grantor can activate the grant for all recipients, or each recipient can activate their own grant.

### Console
<a name="managed-entitlements-all-features-console"></a>

**To activate grants as the grantor (bulk activation)**

1. Sign in to your management account (or delegated administrator account).

1. Open the AWS License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/).

1. In the navigation pane, choose **Granted Licenses**.

1. Choose the grant you want to activate. For organization-wide grants, select the parent grant.

1. Choose **Activate**.

1. Confirm the activation.

This action activates the grant for all recipient accounts. You can verify individual account grant statuses on the grant details page by scrolling to the **Grants** section.

**To activate grants as a recipient**

1. Sign in to the recipient member account.

1. Open the AWS License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/).

1. Make sure you are in the us-east-1 Region.

1. In the navigation pane, choose **Granted Licenses**.

1. Choose the grant you want to activate.

1. Choose **Activate**.

1. Confirm the activation.

The grant status changes to Active, and users in your account can now invoke the third-party Bedrock model.

## For organizations with consolidated billing only
<a name="managed-entitlements-consolidated-billing"></a>

If your organization uses consolidated billing without all features enabled, grants appear in a Pending Acceptance state in the recipient account. The recipient must first accept the grant, then activate it.

### Console
<a name="managed-entitlements-consolidated-billing-console"></a>

**To accept and activate a grant (consolidated billing organizations)**

1. Sign in to the recipient member account.

1. Open the AWS License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/).

1. Make sure you are in the us-east-1 Region.

1. In the navigation pane, choose **Granted Licenses**.

1. Choose the grant you want to accept.

1. Choose **Accept & Activate** to accept and activate the grant in one action.
   + Alternatively, choose **Accept** to accept the grant but keep it in Disabled state for future activation.
   + Or choose **Reject** to decline the license (this is a terminal state).

If you chose **Accept**, you must come back later and choose **Activate** to begin using the model.

## API
<a name="managed-entitlements-accepting-api"></a>

Activating a grant is one step in the AWS License Manager workflow:

1. Create the grant, as described in [Distributing licenses](managed-entitlements-distributing.md).

1. Activate the grant, as described in this section.

1. Invoke the model, as described in [Using third-party Bedrock models with granted licenses](managed-entitlements-using-models.md).

To activate grants programmatically, use the `CreateGrantVersion` operation. For more information, see [creating a new grant version](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_CreateGrantVersion.html) in the *AWS License Manager API Reference*.

The following AWS CLI command activates a grant for all recipients.

```
aws license-manager create-grant-version \
    --region us-east-1 \
    --client-token "$(uuidgen)" \
    --grant-arn "{{my-grant-arn}}" \
    --status ACTIVE \
    --options ActivationOverrideBehavior=ALL_GRANTS_PERMITTED_BY_ISSUER
```

Replace or set the following values:

`grant-arn`  
The ARN of the grant that you want to activate.

`ActivationOverrideBehavior`  
The activation behavior for existing grants. Use `ALL_GRANTS_PERMITTED_BY_ISSUER` to disable any other active grant for the same product in member accounts and replace it with this grant. To keep existing grants in member accounts, use `DISTRIBUTED_GRANTS_ONLY`.