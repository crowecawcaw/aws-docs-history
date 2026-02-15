# Subscribing to third-party Bedrock models through Private Offer

Before you can distribute licenses, you must first subscribe to a Bedrock model through AWS Marketplace.

###### To subscribe to a third-party Bedrock model through AWS Marketplace

1. Choose the private offer link from the sellers to get started or sign in to your management account or designated billing account
2. Open the AWS Marketplace console at [https://console.aws.amazon.com/marketplace/](https://console.aws.amazon.com/marketplace/ "https://console.aws.amazon.com/marketplace/").
3. Navigate to Private Offers for the list of Available Offers
4. Review the subscription agreement and pricing details.
5. Choose **Subscribe** to complete the subscription.
6. You will see a confirmation message indicating your subscription is active.

## To verify license creation

After subscribing, AWS License Manager automatically creates a license for your subscription.

1. Wait 1-2 minutes for the license to be created.
2. Open the AWS License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
3. Make sure you are in the us-east-1 region.
4. In the navigation pane, choose **Granted Licenses**.
5. You should see a new license for your third-party Bedrock model subscription.
6. The license status should display as **Available**.

###### Note

The license is always created in the us-east-1 region, regardless of which region you subscribed in. Always check License Manager in us-east-1 to view your licenses.

If the license does not appear after 5 minutes, verify your subscription is active by going to AWS Marketplace Console, choosing Manage Subscriptions, and confirming your third-party Bedrock model subscription shows as Active.
