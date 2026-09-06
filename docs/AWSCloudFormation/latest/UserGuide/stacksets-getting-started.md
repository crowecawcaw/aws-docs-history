

# Get started with StackSets using a sample template
<a name="stacksets-getting-started"></a>

This tutorial will help you get started with StackSets using the AWS Management Console. It guides you through creating a StackSet using a sample template. You'll learn how to deploy stacks across multiple Regions, monitor StackSet operations, and view the results.

In this tutorial, you'll create a StackSet that enables AWS Config in your AWS account within the US West (Oregon) Region (`us-west-2`) and US East (N. Virginia) Region (`us-east-1`). With StackSets, you can create, update, or delete stacks across multiple accounts and Regions with a single operation, making it an ideal solution for managing infrastructure at scale. While this tutorial uses a single account for simplicity, it effectively demonstrates the multi-region capabilities of StackSets. 

The sample template is available in the following S3 bucket: [https://s3.amazonaws.com/cloudformation-stackset-sample-templates-us-east-1/EnableAWSConfig.yml](https://s3.amazonaws.com/cloudformation-stackset-sample-templates-us-east-1/EnableAWSConfig.yml).

**Note**  
StackSets is free, but you'll be charged for the AWS resources you create with it, such as AWS Config in this tutorial. For more information, see [AWS Config pricing](https://aws.amazon.com/config/pricing/).

**Topics**
+ [Prerequisites](#stacksets-tutorial-prerequisites)
+ [Create a StackSet with a sample template from the console](#stacksets-tutorial-create-stackset)
+ [Monitor StackSet creation](#stacksets-tutorial-monitor-creation)
+ [View StackSet results](#stacksets-tutorial-view-results)
+ [Update your StackSet](#stacksets-tutorial-update-stackset)
+ [Add stacks to your StackSet](#stacksets-tutorial-add-stacks)
+ [Clean up](#stacksets-tutorial-clean-up)
+ [Next steps](#stacksets-tutorial-next-steps)

## Prerequisites
<a name="stacksets-tutorial-prerequisites"></a>

Before you begin this tutorial, make sure you have completed the following prerequisites:
+ You must have set up the required IAM roles for self-managed permissions. To create a StackSet and deploy stacks within a single account, you need the following roles in your account:
  + `AWSCloudFormationStackSetAdministrationRole`
  + `AWSCloudFormationStackSetExecutionRole`

  For detailed instructions on setting up these roles, see [Grant self-managed permissions](stacksets-prereqs-self-managed.md).

## Create a StackSet with a sample template from the console
<a name="stacksets-tutorial-create-stackset"></a>

**To create a StackSet that enables AWS Config**

1. Open the [CloudFormation console](https://console.aws.amazon.com/cloudformation/).

1. On the navigation bar at the top of the screen, choose the AWS Region that you want to manage the StackSet from.

   You can choose any Region that supports StackSets. The Region you select doesn't affect which Regions you can deploy to with your StackSet.

1. From the navigation pane, choose **StackSets**.

1. From the top of the **StackSets** page, choose **Create StackSet**.

1. Under **Permissions**, choose **Self-service permissions** and choose the IAM roles you created in the prerequisites.
   + For IAM admin role, choose **AWSCloudFormationStackSetAdministrationRole**.
   + For IAM execution role name, choose **AWSCloudFormationStackSetExecutionRole**. 

1. Under **Prerequisite - Prepare template**, choose **Use a sample template**.

1. Under **Select a sample template**, choose the **Enable AWS Config** template. Then, choose **Next**.

   This template creates the necessary resources to enable AWS Config in your account, including a configuration recorder and delivery channel.

1. On the **Specify StackSet details** page, for **StackSet name**, enter **my-awsconfig-stackset**.

1. For **StackSet description**, enter **A StackSet that enables Config across multiple Regions**.

1. Under **Parameters**, configure the AWS Config settings as follows:

   1. For **Support all resource types**, keep the default value, **true**, to record all supported resource types.

   1. For **Include global resource types**, keep the default value, **false**, to exclude global resources like IAM roles.

   1. Leave **List of resource types if not all supported** set to **<All>**.

   1. For **The region containing the Config service-linked role resource**, replace **<DeployToAnyRegion>** with **us-west-2**.

      This means that the service-linked role named `AWSServiceRoleForConfig` will only be created if a stack is deployed to the US West (Oregon) Region. You'll choose the deployment Regions later in this procedure.

   1. For **Configuration recorder recording frequency**, choose **DAILY** recording.

1. Choose **Next** to continue.

1. On the **Configure StackSet options** page, choose **Add new tag** and add a tag by specifying a key and value pair:

   1. For **Key**, enter **Stage**.

   1. For **Value**, enter **Test**.

   Tags that you apply to StackSets are applied to resources that are created by your stacks.

1. For **Execution configuration**, choose **Active** to enable CloudFormation's optimized operation handling:
   + Non-conflicting operations run concurrently for faster deployment times.
   + Conflicting operations are automatically queued and processed in the order they were requested.

   While operations are running or queued, CloudFormation queues all incoming operations even if they're non-conflicting. You can't change execution settings during this time.

1. Choose **Next**.

1. On the **Set deployment options** page, for **Add stacks to StackSet**, choose **Deploy new stacks**.

1. For **Accounts**, choose **Deploy stacks in accounts**.

1. In the text box, enter your AWS account ID.

1. For **Specify regions**, select the following Regions in this order:

   1. US West (Oregon) Region (`us-west-2`)

   1. US East (N. Virginia) Region (`us-east-1`)

   Use the up arrow next to US West (Oregon) Region to move it to be the first entry in the list if needed. The order of the Regions determines their deployment order.

1. For **Deployment options**, configure the following settings:

   1. For **Maximum concurrent accounts**, keep the defaults of **Number** and **1**.

      For multi-account deployments, this setting means that CloudFormation deploys your stack in only one account at a time.

   1. For **Failure tolerance**, keep the defaults of **Number** and **0**.

      This means that a maximum of zero stack deployments can fail in one of your specified Regions before CloudFormation stops deployment in the current Region and cancels deployments in remaining Regions.

   1. For **Region concurrency**, choose **Sequential** (default).

      This setting ensures that CloudFormation completes deployments in one Region before moving to the next.

   1. For **Concurrency mode**, keep the default of **Strict failure tolerance**.

      For multi-account deployments, this reduces the account concurrency level when failures occur, staying within **Failure tolerance** \+1.

1. Choose **Next**.

1. On the **Review** page, review your choices. To make changes, choose **Edit** on the related section.

1. When you are ready to create your StackSet, choose **Submit**.

## Monitor StackSet creation
<a name="stacksets-tutorial-monitor-creation"></a>

After you choose **Submit**, CloudFormation begins creating your StackSet and deploying stacks to the specified Regions in your account. The StackSet details page opens automatically, where you can monitor the progress of the operation.

**To monitor the StackSet creation**

1. On the StackSet details page, the **Operations** tab is displayed by default, showing the current operation in progress.

1. The operation status should be `RUNNING` initially. CloudFormation creates stacks in the Regions you specified according to the deployment options you configured.

1. To see more details about the operation, select the operation ID in the list.

1. On the operation details page, you can view the status of stack instances being created in each Region.

1. Wait for the operation status to change to `SUCCEEDED`, which indicates that the StackSet and all its stack instances were created successfully.

## View StackSet results
<a name="stacksets-tutorial-view-results"></a>

After the StackSet creation is complete, you can view the deployed stack instances and verify that AWS Config has been enabled in your account across the specified Regions.

**To view the StackSet results**

1. On the StackSet details page, choose the **Stack instances** tab.

1. You should see a list of stack instances that were created in your account across the specified Regions. Each stack instance should have a status of `SUCCEEDED`, indicating that it was successfully deployed.

1. To verify that AWS Config is enabled in your account, you can check the AWS Config console in each of the deployed Regions.

## Update your StackSet
<a name="stacksets-tutorial-update-stackset"></a>

After creating your StackSet, you might want to update it to modify parameter values or add more Regions. This section shows you how to update the AWS Config recording frequency parameter.

**To update your StackSet**

1. On the **StackSets** page, select your **my-awsconfig-stackset**.

1. With the StackSet selected, choose **Edit StackSet details** from the **Actions** menu.

1. On the **Choose a template** page, for **Prerequisite - Prepare template**, choose **Use current template**.

1. Choose **Next**.

1. On the **Specify StackSet details** page, under **Parameters**, find **Configuration recorder recording frequency** and change it from **DAILY** to **CONTINUOUS**.

1. Choose **Next**.

1. On the **Configure StackSet options** page, leave the settings as they are and choose **Next**.

1. On the **Set deployment options** page, specify your account ID and the same Regions that you used when creating the StackSet.

1. For **Deployment options**, keep the same settings as before.

1. Choose **Next**.

1. On the **Review** page, review your changes and choose **Submit**.

1. CloudFormation starts updating your StackSet. You can monitor the progress on the **Operations** tab of the StackSet details page.

## Add stacks to your StackSet
<a name="stacksets-tutorial-add-stacks"></a>

You can add more stacks to your StackSet by deploying to additional Regions. This section shows you how to add stacks to a new Region.

**To add stacks to your StackSet**

1. On the **StackSets** page, select your **my-awsconfig-stackset**.

1. With the StackSet selected, choose **Add stacks to StackSet** from the **Actions** menu.

1. On the **Set deployment options** page, for **Add stacks to StackSet**, choose **Deploy new stacks**.

1. For **Accounts**, choose **Deploy stacks in accounts** and enter your account ID.

1. For **Specify regions**, select a new Region, such as **Europe (Ireland)** (`eu-west-1`).

1. For **Deployment options**, keep the same settings as before.

1. Choose **Next**.

1. On the **Specify Overrides** page, leave the property values as specified and choose **Next**.

1. On the **Review** page, review your choices and choose **Submit**.

1. CloudFormation starts creating new stacks in the specified Region. You can monitor the progress on the **Operations** tab of the StackSet details page.

## Clean up
<a name="stacksets-tutorial-clean-up"></a>

To avoid incurring charges for unwanted AWS Config resources, you should clean up by deleting the stacks from your StackSet, deleting the StackSet itself, and removing the IAM roles you created for this tutorial. Since all resources are deployed within your account, cleanup is straightforward.

**To delete stacks from your StackSet**

1. On the **StackSets** page, select your **my-awsconfig-stackset**.

1. With the StackSet selected, choose **Delete stacks from StackSet** from the **Actions** menu.

1. On the **Set deployment options** page, for **Accounts**, choose **Deploy stacks in accounts** and enter your account ID.

1. For **Specify regions**, select all the Regions where you deployed stacks.

1. For **Deployment options**, keep the default settings.

1. Make sure **Retain stacks** is *not* turned on, so that the stacks and their resources are deleted.

1. Choose **Next**.

1. On the **Review** page, review your choices and choose **Submit**.

1. CloudFormation starts deleting the stacks from your StackSet. You can monitor the progress on the **Operations** tab of the StackSet details page.

**To delete your StackSet**

1. After all stacks have been deleted, on the **StackSets** page, select your **my-awsconfig-stackset**.

1. With the StackSet selected, choose **Delete StackSet** from the **Actions** menu.

1. When prompted to confirm, choose **Delete**.

**To delete the IAM service roles**

Since you deployed only to your account, you only need to delete the IAM roles from this single account, making cleanup much simpler than multi-account deployments.

1. Open the [IAM console](https://console.aws.amazon.com/iam/).

1. From the navigation pane, choose **Roles**.

1. In the search box, enter **AWSCloudFormationStackSet** to find the roles you created for this tutorial.

1. Select the checkbox next to **AWSCloudFormationStackSetAdministrationRole**.

1. Choose **Delete** from the top of the page.

1. In the confirmation dialog box, enter **delete** and choose **Delete**.

1. Repeat the same process to delete the **AWSCloudFormationStackSetExecutionRole**.

After deleting the StackSet, an Amazon S3 bucket will remain in each AWS Region due to the `DeletionPolicy` attribute on the `AWS::S3::Bucket` resource. This preserves your AWS Config history data. If you no longer need this data, you can safely delete the bucket manually. Before you can delete a bucket, you must first empty it. Emptying a bucket deletes all objects in it.

**To empty and delete the Amazon S3 buckets**

1. Open the [Amazon S3 console](https://console.aws.amazon.com/s3/).

1. In the navigation pane on the left side of the console, choose **Buckets**.

1. In the **Buckets** list, you'll see buckets created for this StackSet in each Region where you deployed. Select the option next to the name of the bucket created for this StackSet, and then choose **Empty**.

1. On the **Empty bucket** page, confirm that you want to empty the bucket by typing **permanently delete** into the text field, and then choose **Empty**.

1. Monitor the progress of the bucket emptying process on the **Empty bucket: Status** page. 

1. To return to your bucket list, choose **Exit**.

1. Select the option next to the name of the bucket, and then choose **Delete**.

1. When prompted for confirmation, type the name of the bucket and then choose **Delete bucket**.

1. Monitor the progress of the bucket deletion process from the **Buckets** list. When Amazon S3 completes the deletion of the bucket, it removes the bucket from the list.

1. Repeat this process for each bucket created by the StackSet in the different Regions.

## Next steps
<a name="stacksets-tutorial-next-steps"></a>

Congratulations\! You've successfully created a StackSet using a sample template, deployed stacks to multiple Regions within your account, updated the StackSet, added more stacks, and cleaned up your resources. By focusing on single-account deployment, you've simplified the cleanup process while still learning the core multi-region capabilities of StackSets.

To learn more about StackSets, explore the following topics:
+ [Override parameter values on stacks within your CloudFormation StackSet](stackinstances-override.md) – Learn how to override parameter values for specific accounts and Regions.
+ [Create CloudFormation StackSets with service-managed permissions](stacksets-orgs-associate-stackset-with-org.md) – Explore creating StackSets for multi-account deployments with AWS Organizations.