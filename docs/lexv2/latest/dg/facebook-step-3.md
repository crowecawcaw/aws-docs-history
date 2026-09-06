

# Step 3: Complete Facebook integration with your Lex V2 bot
<a name="facebook-step-3"></a>

In this step, use the Facebook developer console to complete integration with Amazon Lex V2. 

**To complete Facebook Messenger integration**

1. Open [ https://developers.facebook.com/apps ](https://developers.facebook.com/apps) 

1. From the list of apps, choose the app that you are integrating with Facebook Messenger.

1. In the left menu, choose **Messenger**, then choose **Settings**.

1. In the **Webhooks** section:

   1. Choose **Add Callback URL**.

   1. In **Edit Callback URL**, enter the following:
      + **Callback URL** – Enter the callback URL that you recorded from the Amazon Lex V2 console.
      + **Verify Token** – Enter the alias that you entered in the Amazon Lex V2 console.

   1. Choose **Verify and Save**.

   1. Choose **Add subscriptions** under **Webhooks** next to your page.

   1. In the window that pops up, choose `messages` and then click **Save**.

## Next step
<a name="facebook-step-3-next"></a>

[Step 4: Test the integration with Facebook Messenger](facebook-step-4.md)