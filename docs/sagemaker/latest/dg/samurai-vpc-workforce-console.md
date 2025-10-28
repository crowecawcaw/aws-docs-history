# Using the SageMaker AI console to manage a VPC config

You can use the [SageMaker AI console](https://console.aws.amazon.com/sagemaker "https://console.aws.amazon.com/sagemaker") to add or remove a VPC configuration. You can also delete an existing
workforce.

## Adding a VPC configuration to your workforce

### Create a private workforce

- [Create a private workforce using Amazon Cognito](sms-workforce-private-use-cognito.md "sms-workforce-private-use-cognito.md")
- [Create a private workforce using OpenID Connect (OIDC) Identity Provider(IdP)](sms-workforce-private-use-oidc.md "sms-workforce-private-use-oidc.md").

After you have created your private workforce, add a VPC configuration to it.

1. Navigate to [Amazon SageMaker Runtime](https://console.aws.amazon.com/sagemaker "https://console.aws.amazon.com/sagemaker") in your console.
2. Select **Labeling workforces** in the left panel.
3. Select **Private** to access your private workforce. After your **Workforce status** is **Active**, select **Add** next to **VPC**.
4. When you are prompted to configure your VPC, provide the following:
   1. Your **VPC**
   2. **Subnets**
      1. Ensure that your VPC has an existing subnet

   3. **Security groups**
      1. ###### Note

      You cannot select more than 5 security groups.

   4. After filling in this information, choose **Confirm**.

5. After you choose **Confirm**, you are redirected back to the **Private** page under **Labeling workforces**. You
   should see a green banner at the top that reads **Your private workforce update with VPC configuration was successfully initialized.**
   The workforce status is **Updating**. Next to the **Delete workforce** button is the **Refresh** button, which can be used to retrieve the latest **Workforce status**.
   After the workforce status has changed to **Active**, the VPC endpoint ID is updated as well.

## Removing a VPC configuration from your workforce

Use the following information to remove a VPC configuration from your workforce using the console.

1. Navigate to [Amazon SageMaker Runtime](https://console.aws.amazon.com/sagemaker "https://console.aws.amazon.com/sagemaker") in your console.
2. Select **Labeling workforces** in the left panel.
3. Find and select your workforce.
4. Under **Private workforce summary**, find **VPC** and choose **Remove** next to it.
5. Select **Remove**.

## Deleting a workforce through the console

If you delete a workforce, you should not have any teams associated with it. You can delete a workforce only if the workforce status is **Active** or **Failed**.

Use the following information to delete a workforce using the console.

1. Navigate to [Amazon SageMaker Runtime](https://console.aws.amazon.com/sagemaker "https://console.aws.amazon.com/sagemaker") in your console.
2. Select **Labeling workforces** in the left panel.
3. Find and select your workforce.
4. Choose **Delete workforce**.
5. Choose **Delete**.
