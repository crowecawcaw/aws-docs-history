# Accepting and activating grants

After a grant has been distributed to a member account, the grant must be accepted and activated before the third-party Bedrock model can be used. The acceptance and activation workflow differs depending on your organization configuration.

## For organizations with all features enabled

When you create a grant to a member account in an organization with all features enabled, the grant is automatically accepted and appears in a Disabled state. Either the grantor can activate the grant for all recipients, or each recipient can activate their own grant.

### Console

###### To activate grants as the grantor (bulk activation)

1. Sign in to your management account (or delegated administrator account).
2. Open the AWS License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
3. In the navigation pane, choose **Granted Licenses**.
4. Choose the grant you want to activate. For organization-wide grants, select the parent grant.
5. Choose **Activate**.
6. Confirm the activation.

This action activates the grant for all recipient accounts. You can verify individual account grant statuses on the grant details page by scrolling to the **Grants** section.

###### To activate grants as a recipient

1. Sign in to the recipient member account.
2. Open the AWS License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
3. Make sure you are in the us-east-1 Region.
4. In the navigation pane, choose **Granted Licenses**.
5. Choose the grant you want to activate.
6. Choose **Activate**.
7. Confirm the activation.

The grant status changes to Active, and users in your account can now invoke the third-party Bedrock model.

## For organizations with consolidated billing only

If your organization uses consolidated billing without all features enabled, grants appear in a Pending Acceptance state in the recipient account. The recipient must first accept the grant, then activate it.

### Console

###### To accept and activate a grant (consolidated billing organizations)

1. Sign in to the recipient member account.
2. Open the AWS License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
3. Make sure you are in the us-east-1 Region.
4. In the navigation pane, choose **Granted Licenses**.
5. Choose the grant you want to accept.
6. Choose **Accept & Activate** to accept and activate the grant in one action.
   - Alternatively, choose **Accept** to accept the grant but keep it in Disabled state for future activation.
   - Or choose **Reject** to decline the license (this is a terminal state).

If you chose **Accept**, you must come back later and choose **Activate** to begin using the model.

## API

You can activate grants programmatically using the [CreateGrantVersion API.](../../../license-manager/latest/APIReference/API_CreateGrantVersion.md "../../../license-manager/latest/APIReference/API_CreateGrantVersion.md")
