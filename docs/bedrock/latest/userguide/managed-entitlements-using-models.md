# Using third-party Bedrock models with granted licenses

Once a grant has been activated in your account, you can invoke the third-party Bedrock model using the Amazon Bedrock console, AWS CLI, or AWS SDKs. The experience is identical to invoking a model with a direct subscription.

## To verify you have an active license

Before attempting to use a third-party Bedrock model, verify that your grant is in an Active state.

1. Open the AWS License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. Make sure you are in the us-east-1 Region.
3. In the navigation pane, choose **Granted Licenses**.
4. Find the grant for the third-party Bedrock model you want to use.
5. Verify the Grant status shows as **Active**.

If the status shows Disabled, you must activate the grant before using the model. If the status shows Pending Acceptance, you must first accept the grant.

## To invoke a third-party Bedrock model with a granted license

1. Open the Amazon Bedrock console in any supported region where the model is available.
2. In the navigation pane, choose **Text** or **Chat** under **Playgrounds**, depending on the model type.
3. Select the model you have a license for from the model dropdown.
4. Enter your prompt and choose **Run**.

The model invocation works the same way as if you had subscribed directly. All usage is billed to the account that holds the original subscription (typically the management account).

You can also invoke models programmatically using the AWS CLI or AWS SDKs with the [InvokeModel API.](../APIReference/API_runtime_InvokeModel.md "../APIReference/API_runtime_InvokeModel.md") The only requirement is that you have an active license grant in your account.
