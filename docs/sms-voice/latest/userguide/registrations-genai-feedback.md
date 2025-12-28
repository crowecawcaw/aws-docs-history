# Gen-AI Feedback on Registrations (Preview)

###### Note

The registration reviewer is designed to provide early feedback on the quality of your registration submissions with generative AI. It may from time-to-time produce inaccurate feedback. You are still responsible to ensure your registrations meet the compliance bar for the phone number or sender ID you're registering. If you disagree with the feedback, you can submit the registration for downstream review without implementing the feedback.

The registration reviewer is a Gen-AI feature available in public preview under AWS End User Messaging SMS. The registration reviewer provides you Gen-AI feedback on your phone number or sender ID registration before submitting for carrier review. The reviewer will check your registration for common denial reasons or format requirements and provide feedback saving time-to-approval. Once you submit your registration for feedback, it will move to carrier review if no additional updates are required or will move to "requires Updates" with feedback on the registration form. The registration reviewer provides two levels of feedback including a summary on the form itself, and field level feedback including a denial reason and descriptive feedback with possible suggestions.

## Improving the registration reviewer

AWS End User Messaging may use certain information from your registrations and feedback to improve the registration reviewer feature. End User Messaging may use this information, for example, to provide better feedback on your registrations, such as providing better feedback on how to format your message samples or use-case descriptions. If you would like to opt-out from End User Messaging using registration information and registration feedback to improve the registration reviewer feature, you can submit your registration without using the registration reviewer feature.

## Data handling for registration reviewer

The registration reviewer feature may require that your registration information and feedback be processed in a different AWS region than the AWS region you selected for End User Messaging. For example, when addressing a request for registration feedback, the feature uses Amazon Bedrock models to process your registration information and registration feedback. The models may process such requests from a region other than the AWS region you selected for End User Messaging. Your registration information and feedback are encrypted while transmitted across Amazon's secure network for the purpose of this cross-region processing. This cross-region processing does not change where your registration information and registration feedback is stored, and those items will still be stored in the AWS region you selected for End User Messaging.

###### Important

The registration reviewer feature is a public preview feature governed by your agreement with AWS governing your use of AWS services and by sections 1 and 2 of the AWS Service Terms. While the feature is currently offered at no charge, feature pricing is subject to change. Standard pricing for AWS End User Messaging SMS still applies when you send SMS with End User Messaging.

## Using Gen-AI feedback

Using Gen-AI feedback (Console)
To receive feedback on your registration using the AWS End User Messaging SMS console, follow these steps:

1. Open the AWS End User Messaging SMS console at [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under **Registrations**, choose **Create registration**.
3. For **Registration type**, choose the registration form from the dropdown list. Each **Registration type** has different forms depending on the regulatory body the registration form is sent to.
4. (optional) Expand **Tags** to:
   - **Add a tag** – In **Manage tags** choose **Add new tag** to create a new blank key/value pair.
   - **Delete a tag** – In **Manage tags**, choose **Remove** next to the key/value pair.
   - **Edit a tag** – In **Manage tags** choose the **Key** or **Value** and edit the text.

5. Choose **Create**.
6. Once you've created the registration, fill out the appropriate fields. For more information related to the specific registration form, check here.
7. On the review and submit page, select receive AI feedback.
8. If your registration passes and does not require any feedback, we will automatically submit it for carrier review.
9. If your registration requires feedback, you will receive the feedback summary on the AI feedback page. You can respond to the feedback and make updates on the flagged form field sections by selecting **Update**.
10. Once you've completed the updates, you can **Submit** or resubmit for AI review.

Using Gen-AI feedback (AWS CLI)
To receive feedback on your registration using the AWS CLI, use the following command:

```
`$` aws pinpoint-sms-voice-v2 --region us-east-1 submit-registration-version \
  --registration-id `<registration-XXXXXXXXX>` \
  --aws-review
```

In the preceding example, do the following:

- Replace `<registration-XXXXXXXXX>` with your actual registration ID.
- The `--aws-review` flag enables AI feedback review before carrier submission.
- Specify the appropriate region using `--region`.

###### Topics

- [Understanding rejection reasons](understanding-rejection-reasons.md "understanding-rejection-reasons.md")
- [Get more information on registration issues](registrations-request-support.md "registrations-request-support.md")
