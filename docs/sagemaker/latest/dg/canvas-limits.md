# Limitations and troubleshooting

The following section outlines troubleshooting help and limitations that apply when using Amazon SageMaker Canvas. You can use these
this topic to help troubleshoot any issues you encounter.

## Troubleshooting issues with granting permissions through the SageMaker AI console

If you’re having trouble granting Canvas base permissions or Ready-to-use models permissions to your user, your user
might have an AWS IAM execution role with more than one trust relationship to other AWS services. A trust relationship is a
policy attached to your role that defines which principals (users, roles, accounts, or services) can assume the role. For example, you
might encounter an issue granting additional Canvas permissions to your user if their execution role has a trust relationship to
both Amazon SageMaker AI and Amazon Forecast.

You can fix this problem by choosing one of the following options.

### 1. Remove all but one trusted service from the role.

This solution requires you to edit the trust relationship for your user profile’s IAM role and remove all AWS services except SageMaker AI.

To edit the trust relationship for your IAM execution role, do the following:

1. Go to the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane of the IAM console, choose **Roles**. The console displays the roles for your account.
3. Choose the name of the role that you want to modify, and select the **Trust relationships** tab on the details page.
4. Choose **Edit trust policy**.
5. In the **Edit trust policy editor**, paste the following, and then choose **Update Policy**.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "sagemaker.amazonaws.com"
 ]
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

You can also update this policy document using the IAM CLI. For more information, see
[update-trust](../../../cli/latest/reference/ds/update-trust.md "../../../cli/latest/reference/ds/update-trust.md")
in the _IAM Command Line Reference_.

You can now retry granting the Canvas base permissions or the Ready-to-use models permissions to your user.

### 2. Use a different role with one or fewer trusted services.

This solution requires you to specify a different IAM role for your user profile. Use this option if you already have an IAM role that you can substitute.

To specify a different execution role for your user, do the following:

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the left navigation pane, choose **Admin configurations**.
3. Under **Admin configurations**, choose **domains**.
4. From the list of domains, select the domain that you want to view a list of user profiles for.
5. On the **domain details** page, choose the **User profiles** tab.
6. Choose the user whose permissions you want to edit. On the **User details** page, choose **Edit**.
7. On the **General settings** page, choose the **Execution role** dropdown list and select the role that you want to use.
8. Choose **Submit** to save your changes to the user profile.

Your user should now be using an execution role with only one trusted service (SageMaker AI).

You can retry granting the Canvas base permissions or the Ready-to-use models permissions to your user.

### 3. Manually attach the AWS managed policy to the

execution role instead of using the toggle in the SageMaker AI domain settings.

Instead of using the toggle in the domain or user profile settings, you can manually attach the
AWS managed policies that grant a user the correct permissions.

To grant a user Canvas base permissions, attach the
[AmazonSageMakerCanvasFullAccess](security-iam-awsmanpol-canvas.md#security-iam-awsmanpol-AmazonSageMakerCanvasFullAccess "security-iam-awsmanpol-canvas.md#security-iam-awsmanpol-AmazonSageMakerCanvasFullAccess")
policy. To grant a user Ready-to-use models permissions, attach the
[AmazonSageMakerCanvasAIServicesAccess](security-iam-awsmanpol-canvas.md#security-iam-awsmanpol-AmazonSageMakerCanvasAIServicesAccess "security-iam-awsmanpol-canvas.md#security-iam-awsmanpol-AmazonSageMakerCanvasAIServicesAccess")
policy.

Use the following procedure to attach an AWS managed policy to your role:

1. Go to the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Choose **Roles**.
3. In the search box, search for the user's IAM role by name and select it.
4. On the page for the user's role, under **Permissions**, choose **Add permissions**.
5. From the dropdown menu, choose **Attach policies**.
6. Search for and select the policy or policies that you want to attach to the user’s execution role:
   1. To grant the Canvas base permissions, search for and select the
      [AmazonSageMakerCanvasFullAccess](security-iam-awsmanpol-canvas.md#security-iam-awsmanpol-AmazonSageMakerCanvasFullAccess "security-iam-awsmanpol-canvas.md#security-iam-awsmanpol-AmazonSageMakerCanvasFullAccess") policy.
   2. To grant the Ready-to-use models permissions, search for and select the
      [AmazonSageMakerCanvasAIServicesAccess](security-iam-awsmanpol-canvas.md#security-iam-awsmanpol-AmazonSageMakerCanvasAIServicesAccess "security-iam-awsmanpol-canvas.md#security-iam-awsmanpol-AmazonSageMakerCanvasAIServicesAccess") policy.

7. Choose **Add permissions** to attach the policy to the role.

After attaching an AWS managed policy to the user’s role through the IAM console,
your user should now have the Canvas base permissions or Ready-to-use models permissions.

## Troubleshooting issues with creating a Canvas application due to space failure

When creating a new Canvas application, if you encounter an error stating `Unable
 to create app <app-arn> because space <space-arn> is not in InService state`,
this indicates that the underlying Amazon SageMaker Studio space creation has failed. A Studio
_space_ is the underlying storage that hosts your Canvas
application data. For more general information about Studio spaces, see [Amazon SageMaker Studio spaces](studio-updated-spaces.md "studio-updated-spaces.md"). For more information
about configuring spaces in Canvas, see [Store SageMaker Canvas application data in your own SageMaker AI
space](canvas-spaces-setup.md "canvas-spaces-setup.md").

To determine the root cause of your why space creation failed, you can use the [DescribeSpace](../APIReference/API_DescribeSpace.md "../APIReference/API_DescribeSpace.md")
API to check the `FailureReason` field. For more information about the possible statuses of spaces
and what they mean, see [Amazon SageMaker AI domain entities and statuses](sm-domain.md "sm-domain.md").

To resolve this issue, find your domain in the SageMaker AI console and delete the failed space listed in the error message you received.
For detailed steps on how to find and delete a space, see the page [Stop and delete your Studio running
applications and spaces](studio-updated-running-stop.md "studio-updated-running-stop.md")
and follow the instructions to **Delete a Studio space**.
Deleting the space also deletes any applications associated with the space. After deleting the space, you can try to create your Canvas
application again. The space should now provision successfully, allowing Canvas to launch.
