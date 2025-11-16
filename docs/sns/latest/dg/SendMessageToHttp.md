# Step 3: Confirm your Amazon SNS subscription

To confirm your Amazon SNS subscription, follow these steps to ensure your endpoint can
successfully receive messages. This process involves setting up your endpoint to handle
incoming confirmation messages, retrieving the confirmation URL, and confirming the
subscription. You can confirm the subscription either automatically or manually, depending on
your setup.

1. After subscribing to an Amazon SNS topic, Amazon SNS sends a confirmation message to your
   endpoint. This message contains a `SubscribeURL` that you must use to confirm
   the subscription.
2. Your endpoint must be set up to listen for incoming messages from Amazon SNS. When the
   confirmation message arrives, extract the **`SubscribeURL`** from the message.
3. Once you have the `SubscribeURL`, you can confirm the subscription in one
   of two ways:
   - **Automatic confirmation** – Your endpoint can
     automatically confirm the subscription by sending an **HTTP GET
     request** to the `SubscribeURL`.

   This method does not require manual intervention.
   - **Manual confirmation** – If automatic
     confirmation is not set up, **copy** the **`SubscribeURL`** from the confirmation message and
     **paste** it into your browser’s address bar.

   This will confirm the subscription manually.

4. You can also verify the **subscription status** using the
   Amazon SNS console:
   1. Sign in to the [Amazon SNS console](https://console.aws.amazon.com/sns/home "https://console.aws.amazon.com/sns/home").
   2. In the navigation pane, choose **Subscriptions**.
   3. Find your **subscription** in the list.
      - If confirmed, the `SubscriptionArn` will be displayed.
      - If still unconfirmed, it will show as `PendingConfirmation`.
