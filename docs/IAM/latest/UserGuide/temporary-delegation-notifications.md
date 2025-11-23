# Notifications

IAM temporary delegation integrates with AWS User Notifications to help you stay informed about delegation request state changes. Notifications are particularly useful for administrators who need to review and approve delegation requests.

With AWS User Notifications, you can configure alerts to be delivered through multiple channels, including email, Amazon Simple Notification Service (SNS), AWS Chatbot for Slack or Microsoft Teams, and AWS Console Mobile Application. This ensures that the right people are notified at the right time, enabling faster response to pending approvals or awareness of access changes. You can also customize which events trigger notifications based on your organization's needs and security requirements.

## Available Notification Events

You can subscribe to receive notifications for the following IAM temporary delegation events:

- IAM Temporary Delegation Request Created
- IAM Temporary Delegation Request Assigned
- IAM Temporary Delegation Request Pending Approval
- IAM Temporary Delegation Request Rejected
- IAM Temporary Delegation Request Accepted
- IAM Temporary Delegation Request Finalized
- IAM Temporary Delegation Request Expired

## Configuring Notifications

To configure notifications for IAM temporary delegation events:

1. Open the AWS User Notifications console
2. Create or update a notification configuration
3. Select AWS IAM as the service
4. Choose which delegation request events you want to be notified about
5. Configure your delivery channels (email, AWS Chatbot, etc.)

For detailed instructions on configuring AWS User Notifications, including setting up delivery channels and managing notification rules, see the AWS User Notifications documentation.
