# Setting up AWS Transform

## Before you begin

Before you set up AWS Transform make sure you have an AWS account with administrator access

###### Note

If you want to try out AWS Transform as a proof-of-concept or for test environments see [Quick start: Trying AWS Transform](transform-setup.md#transform-app-admin-starting-standalone "transform-setup.md#transform-app-admin-starting-standalone").

## Getting started with AWS Organizations

Follow these steps to set up AWS Transform:

1. Sign in to your AWS Organizations management account.
2. Navigate to the AWS Transform service.
3. Choose **Enable service** for your organization to use AWS Transform.
4. Configure the necessary permissions for organizational member accounts.
5. Access the AWS Transform web experience from your member accounts.

###### Note

To use the Landing Zone Accelerator (LZA) on AWS solution to build your landing zone together with
AWS Transform for migration capabilities, your AWS Transform account and LZA installation must be in the
same AWS Organization. Using separate Organizations IDs for LZA and AWS Transform deployments is
not supported because this can cause inconsistencies in organizational management and resource
deployments. To learn how to set up your LZA installation using Organizations see [Deploy a cloud foundation to support highly-regulated workloads and complex compliance requirements](../../../solutions/latest/landing-zone-accelerator-on-aws/solution-overview.md "../../../solutions/latest/landing-zone-accelerator-on-aws/solution-overview.md") in the _Landing Zone Accelerator on AWS
Implementation Guide user guide_.

## Getting started with AWS IAM Identity Center

Follow these steps to use IAM Identity Center for AWS Transform and to add users and groups.

###### Note

By default, no users have access to AWS Transform when you first enable it.

1. Set up IAM Identity Center following the instructions in [To enable an instance of IAM Identity Center](../../../singlesignon/latest/userguide/enable-identity-center.md#to-enable-identity-center-instance "../../../singlesignon/latest/userguide/enable-identity-center.md#to-enable-identity-center-instance").

Configure IAM Identity Center to use an external enterprise identity provider, and replicate its user and group info into IAM Identity Center. 2. In the AWS console, select AWS Transform and choose **Get started**. 3. Choose **Enable service** for your organization to use AWS Transform. 4. Select an encryption key. The default selection is an AWS managed key. To use a custom key:

    1. Under **Encryption key**, choose **Customize encryption settings**.
    2. Select **Use an AWS KMS key**.
    3. Choose an existing key or create a new one.
    4. Choose **Submit** to apply your changes, and then choose **Enable AWS Transform**.Click **View profile** to view the configuration. The Web application URL is used by your users to access the AWS Transform unified web experience.

5. Select **Users** in the navigation pane and select **Assign users or groups**.
6. Search for the name of the user or groups you want to authorize to use AWS Transform. The search references users and groups propagated from your identity provider.
7. Select a group or user, select **Done**, and then, **Assign**. These users are authorized to use the AWS Transform unified web interface.

## Enable AWS Transform

To enable AWS Transform:

1. Sign in to the AWS Management Console.
2. In the search bar at the top of the console, search for "AWS Transform".
3. Select **AWS Transform** from the search results.
4. On the AWS Transform homepage, choose **Get started**.
5. Review the service information, including benefits and features.
6. Choose **Get started** again to enable the service in your current Region.
7. The system displays "Enabling AWS Transform" while it creates the necessary resources.

After AWS Transform is enabled, the service configuration page displays the following information:

- **Web application URL** - The URL for accessing the AWS Transform web application
- **Start URL for IDE** - The URL for accessing AWS Transform in integrated development environments
- **Region** - The AWS Region where AWS Transform is enabled

## Quick start: Trying AWS Transform

The easiest way to try out AWS Transform is with a standalone AWS account. You may want to do this as a proof-of-concept or for test environments. Use this procedure:

1. Sign in to the AWS Management Console.
2. Navigate to the AWS Transform service.
3. Choose **Get started** to enable the service.
4. After the service is enabled, you'll see the AWS Transform web application URL.
5. Open that URL in a new browser window to access the AWS Transform web experience.

Now you're ready to set up your workspace.
