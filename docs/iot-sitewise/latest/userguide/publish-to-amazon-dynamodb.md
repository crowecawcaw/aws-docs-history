

# Publish property value updates to Amazon DynamoDB
<a name="publish-to-amazon-dynamodb"></a>

This tutorial introduces a convenient way to store your data by using [Amazon DynamoDB](https://aws.amazon.com/dynamodb/), making it easier to access historical asset data without repeatedly querying the AWS IoT SiteWise API. After you complete this tutorial, you can create custom software that consumes your asset data, such as a live map of wind speed and direction over an entire wind farm. If you want to monitor and visualize your data without implementing a custom software solution, see [Monitor data with AWS IoT SiteWise Monitor](monitor-data.md).

In this tutorial, you build on the AWS IoT SiteWise demo that provides a sample set of data for a wind farm. You configure property value updates from the wind farm demo to send data, through AWS IoT Core rules, to a DynamoDB table that you create. When you enable property value updates, AWS IoT SiteWise sends your data to AWS IoT Core in MQTT messages. Then, define AWS IoT Core rules that perform actions, such as the DynamoDB action, depending on the contents of those messages. For more information, see [Interact with other AWS services](interact-with-other-services.md).

**Topics**
+ [Prerequisites](#dynamodb-tutorial-prerequisites)
+ [Step 1: Configure AWS IoT SiteWise to publish property value updates](#dynamodb-tutorial-enable-value-notifications)
+ [Step 2: Create a rule in AWS IoT Core](#dynamodb-tutorial-create-iot-rule)
+ [Step 3: Configure the DynamoDB rule action](#dynamodb-tutorial-configure-rule-action)
+ [Step 4: Explore data in DynamoDB](#dynamodb-tutorial-explore-dynamodb-data)
+ [Clean up resources](#dynamodb-tutorial-clean-up-resources)
+ [Additional resources](#dynamodb-tutorial-additional-resources)

## Prerequisites
<a name="dynamodb-tutorial-prerequisites"></a>

To complete this tutorial, you need the following:
+ An AWS account. If you don't have one, see [Set up an AWS account](getting-started.md#set-up-aws-account).
+ A development computer running Windows, macOS, Linux, or Unix to access the AWS Management Console. For more information, see [What is the AWS Management Console?](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/what-is.html)
+ An AWS Identity and Access Management (IAM) user with administrator permissions. For detailed instructions, see [How AWS IoT SiteWise works with IAM](security_iam_service-with-iam.md).
+ A running AWS IoT SiteWise demo. For more information, see [Use the AWS IoT SiteWise demo](getting-started-demo.md).

**Note**  
This tutorial requires the use of resources created in the [Use the AWS IoT SiteWise demo](getting-started-demo.md). You must complete it before proceeding with this tutorial.

**Important**  
Keep all demo resources until you complete this tutorial. Deleting any components might disrupt the demo's functionality and affect your ability to complete the tutorial.

## Step 1: Configure AWS IoT SiteWise to publish property value updates
<a name="dynamodb-tutorial-enable-value-notifications"></a>

In this procedure, you enable property value notifications on your demo turbine assets' **Wind Speed** properties. After you enable property value notifications, AWS IoT SiteWise publishes each value update in an MQTT message to AWS IoT Core.

**To enable property value update notifications on asset properties**

1. Sign in to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/).

1. Review the [AWS IoT SiteWise endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/iot-sitewise.html) where AWS IoT SiteWise is supported and switch AWS Regions, if necessary. Switch to a Region where you're running the AWS IoT SiteWise demo.

1. In the left navigation pane, choose **Assets**.

1. Choose the arrow next to **Demo Wind Farm Asset** to expand the wind farm asset's hierarchy.

1. Choose a demo turbine and choose **Edit**.

1. Choose **Measurements**.

1. Update the **Wind Speed** property's **MQTT Notification status** to **ACTIVE**.

1. Choose **Save** at the bottom of the page.

1. Repeat steps 5 through 7 for each demo turbine asset.

1. Choose a demo turbine (for example, **Demo Turbine Asset 1**).

1. Choose **Measurements**.

1. Choose the copy icon next to the **Wind Speed** property to copy the notification topic to your clipboard. Save the notification topic to use later in this tutorial. You only need to record the notification topic from one turbine.

   The notification topic should look like the following example.

   ```
   $aws/sitewise/asset-models/{{a1b2c3d4-5678-90ab-cdef-11111EXAMPLE}}/assets/{{a1b2c3d4-5678-90ab-cdef-22222EXAMPLE}}/properties/{{a1b2c3d4-5678-90ab-cdef-33333EXAMPLE}}
   ```

## Step 2: Create a rule in AWS IoT Core
<a name="dynamodb-tutorial-create-iot-rule"></a>

In this step, create a rule in AWS IoT Core that parses the property value notification messages and inserts data into an Amazon DynamoDB table. AWS IoT Core rules parse MQTT messages and perform actions based on the contents and topic of each message. Then, you create a rule with a DynamoDB action to insert data to a DynamoDB table that you create as part of this tutorial.

**To create a rule with a DynamoDB action**

1. Navigate to the [AWS IoT console](https://console.aws.amazon.com/iot/).

1. In the left navigation pane, choose **Message routing**, and then choose **Rules**.

1. Choose **Create rule**.

1. Under **Specify rule properties**, enter a name and description for the rule.

1. Find the notification topic that you saved earlier in this tutorial.

   ```
   $aws/sitewise/asset-models/{{a1b2c3d4-5678-90ab-cdef-11111EXAMPLE}}/assets/{{a1b2c3d4-5678-90ab-cdef-22222EXAMPLE}}/properties/{{a1b2c3d4-5678-90ab-cdef-33333EXAMPLE}}
   ```

   Replace the asset ID (the ID after `assets/`) in the topic with a `+`. This selects the wind speed property for all demo wind turbine assets. The `+` topic filter accepts all nodes from a single level in a topic. Your topic should look like the following example.

   ```
   $aws/sitewise/asset-models/{{a1b2c3d4-5678-90ab-cdef-11111EXAMPLE}}/assets/+/properties/{{a1b2c3d4-5678-90ab-cdef-33333EXAMPLE}}
   ```

1. Enter the following rule query statement. Replace the topic in the `FROM` section with your notification topic.

   ```
   SELECT
     payload.assetId AS asset,
     (SELECT VALUE (value.doubleValue) FROM payload.values) AS windspeed,
     timestamp() AS timestamp
   FROM
     '$aws/sitewise/asset-models/{{a1b2c3d4-5678-90ab-cdef-11111EXAMPLE}}/assets/+/properties/{{a1b2c3d4-5678-90ab-cdef-33333EXAMPLE}}' 
   WHERE
     type = 'PropertyValueUpdate'
   ```

1. Under **Rule actions**, navigate to **Action 1**.

1. On the **Select an action** page, choose **DynamoDBv2**. This splits the message into multiple columns of a DynamoDB table

1. Under **Table name**, choose **Create new table**. You create an Amazon DynamoDB table to receive wind speed data from the rule action.

1. Under **Table name** in the [DynamoDB console](https://console.aws.amazon.com/dynamodb/) enter a name for your table.

1. For **Partition key**, do the following:

   1. Enter **timestamp** as the partition key.

   1. Choose the **Number** type.

   1. Select the **Add sort key** check box.

   1. Enter **asset** as the sort key, and leave the default sort key type of **String**.

1. Choose **Create table**.

1. Return to the tab with the **Configure action** page.

1. On the **Attach rule action** page, refresh the **Table name** list, and choose your new DynamoDB table you created in the previous step.

## Step 3: Configure the DynamoDB rule action
<a name="dynamodb-tutorial-configure-rule-action"></a>

In this step, configure the Amazon DynamoDB rule action to insert data from property value updates to your new DynamoDB table.

**To configure the DynamoDB rule action**

1. Choose **Create role** to create an IAM role that grants AWS IoT Core access to perform the rule action.

1. Enter a role name, for example, `WindSpeedDataRole`. Choose **Create role**.

1. Choose **Next**.

1. Choose **Create** at the bottom of the page to finish creating the rule.

   Your demo asset data should start appearing in your DynamoDB table.

## Step 4: Explore data in DynamoDB
<a name="dynamodb-tutorial-explore-dynamodb-data"></a>

In this step, explore the demo assets' wind speed data in your new Amazon DynamoDB table.

**To explore asset data in DynamoDB**

1. Return to the tab with the DynamoDB table open.

1. In the table you created earlier, choose the **Explore table items** tab to view the data in the table. Refresh the page if you don't see rows in the table. If rows don't appear after a few minutes, see [Troubleshoot a rule (DynamoDB)](troubleshoot-rule.md#dynamodb-tutorial-troubleshoot-rule).

1. In a row in the table, choose the edit icon to expand the data.

1. Choose the arrow next to the **windspeed** structure to expand the list of wind speed data points. Each list reflects a batch of wind speed data points sent to AWS IoT SiteWise by the wind farm demo. You might want a different data format if you set up a rule action for your own use. For more information, see [Query asset property notifications in AWS IoT SiteWise](query-notification-messages.md).

Now that you have completed the tutorial, you can disable or delete the rule and delete your DynamoDB table to avoid incurring additional charges. To clean up your resources, see [Clean up resources](#dynamodb-tutorial-clean-up-resources).

You can also learn how to create custom applications to consume and visualize this data. For a guided tutorial on visualizing AWS IoT SiteWise data, see [Visualize and share data in Grafana](visualize-with-grafana.md).

## Clean up resources
<a name="dynamodb-tutorial-clean-up-resources"></a>

After you complete the tutorial, clean up your resources to avoid incurring additional charges.

**To delete the AWS IoT SiteWise demo**

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/).

1. In the upper-right corner of the page, choose **Delete demo**.

1. In the confirmation dialog, enter **DELETE** and then choose **Delete**.

For more information, see [Delete the AWS IoT SiteWise demo](getting-started-demo.md#delete-getting-started-demo).

Use the following procedures to disable property value update notifications (if you didn't delete the demo), disable or delete your AWS IoT rule, and delete your DynamoDB table.

**To disable property value update notifications on asset properties**

1. Navigate to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/).

1. In the left navigation pane, choose **Assets**.

1. Choose the arrow next to **Demo Wind Farm Asset** to expand the wind farm asset's hierarchy.

1. Choose a demo turbine and choose **Edit**.

1. Update the **Wind Speed** property's **Notification status** to **INACTIVE**.

1. Choose **Save asset** at the bottom of the page.

1. Repeat steps 4 through 6 for each demo turbine asset.

**To disable or delete a rule in AWS IoT Core**

1. Navigate to the [AWS IoT console](https://console.aws.amazon.com/iot/).

1. In the left navigation pane, choose **Message routing** and then choose **Rules**.

1. Select your rule and choose **Delete**.

1. In the confirmation dialog, enter the name of the rule and then choose Delete.

**To delete a DynamoDB table**

1. Navigate to the [DynamoDB console](https://console.aws.amazon.com/dynamodb/).

1. In the left navigation pane, choose **Tables**.

1. Choose the table you created earlier, for example, `WindSpeedData`.

1. Choose **Delete**.

1. In the confirmation dialog, enter **confirm** to delete the table.

## Additional resources
<a name="dynamodb-tutorial-additional-resources"></a>

For more information about working with DynamoDB and monitoring your data, see the following resources:
+ [Monitoring metrics in with CloudWatch ](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Monitoring-metrics-with-Amazon-CloudWatch.html) in the *DynamoDB Developer Guide*
+ [Best practices for designing and using partition keys effectively in ](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html) in the *DynamoDB Developer Guide*
+ [Rules for AWS IoT](https://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html) in the *AWS IoT Developer Guide*
+ [Visualize and share data in Grafana](visualize-with-grafana.md)