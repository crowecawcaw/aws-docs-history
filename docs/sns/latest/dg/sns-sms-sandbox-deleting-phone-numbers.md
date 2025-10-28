# Deleting phone numbers from the

Amazon SNS SMS sandbox

You can delete both pending and verified destination phone numbers from the [SMS sandbox](sns-sms-sandbox.md "sns-sms-sandbox.md").

###### Important

You can only delete a phone number 24 hours after [verifying the phone number](sns-sms-sandbox-verifying-phone-numbers.md "sns-sms-sandbox-verifying-phone-numbers.md"),
or 24 hours after your last verification attempt.

###### To delete destination phone numbers from the SMS sandbox

1. Sign in to the [Amazon SNS console](https://console.aws.amazon.com/sns/home "https://console.aws.amazon.com/sns/home").
2. In the console menu, choose a [region that supports SMS
   messaging](../../../general/latest/gr/end-user-messaging.md "../../../general/latest/gr/end-user-messaging.md") where you added a destination phone number.
3. In the navigation pane, select **Text messaging (SMS)**.
4. On the **Mobile text messaging (SMS)** page, navigate to the
   **Sandbox destination phone numbers** section.
5. Choose the specific phone number you want to delete, and then choose
   **Delete phone number**.
6. To confirm that you want to delete the phone number, enter `delete
me`, and then choose **Delete**.

Ensure that 24 hours or more have passed since you verified or attempted to verify
the destination phone number before proceeding with the deletion. 7. Repeat these steps in each Region where you added the destination phone number and
no longer plan to use it.
