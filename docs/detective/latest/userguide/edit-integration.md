# Changing the Detective integration configuration

If you want to change any of the parameters that you used to integrate Detective with Security Lake, you can edit them, and then enable the integration again. You can edit the AWS CloudFormation template to re-enable this integration for the following scenarios:

- To update the Security Lake subscription, you can either create a new subscriber, or
  the Security Lake administrator can update the data source for the existing
  subscription.
- To specify a different Amazon S3 bucket to store the raw query logs.
- To specify different Lake Formation principals.
  When you re-enable Detective integration with Security Lake, you can edit the **Resource
  Share ARN**, and view the **IAM permissions**. To edit
  the IAM permissions, you can go to the IAM console from Detective. You can also edit
  the values you previously entered in the AWS CloudFormation template. You must delete the existing
  CloudFormation stack and re-create it to re-enable the integration.

###### To re-enable Detective integration with Security Lake

1. Open the Detective console at [https://console.aws.amazon.com/detective/](https://console.aws.amazon.com/detective/ "https://console.aws.amazon.com/detective/").
2. In the navigation pane, choose **Integrations**.
3. You can edit the integration using either of these steps:
   - In the **Security Lake** pane, choose
     **Edit**.
   - In the **Security Lake** pane, choose
     **View**. In the view page, choose
     **Edit**.

4. Enter a new **Resource Share ARN**, to access the data
   sources in a Region.
5. View the current IAM permissions, and go to the IAM console, if you want to edit the IAM permissions.
6. Edit the values in the CloudFormation template.
   1. Delete the existing stack first, before creating a new stack. If you do not delete the existing stack and you try to create a new stack in the same Region, your request fails. For more details, see [Deleting a CloudFormation stack](disable-integration.md#delete-stack "disable-integration.md#delete-stack").

   1. Create a new CloudFormation stack. For more details, see [Creating a stack using the AWS CloudFormation
      template](resource-share-arn.md#cloud-formation-template "resource-share-arn.md#cloud-formation-template").

7. Choose **Enable integration**.
