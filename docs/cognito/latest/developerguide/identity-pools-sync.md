

# Using Amazon Cognito Sync with identity pools
<a name="identity-pools-sync"></a>

 Amazon Cognito Sync is an AWS service and client library that makes it possible to sync application-related user data across devices. Amazon Cognito Sync can synchronize user profile data across mobile devices and the web without using your own back end. The client libraries cache data locally so that your app can read and write data regardless of device connectivity status. When the device is online, you can synchronize data. If you set up push sync, you can notify other devices immediately that an update is available. 

## Managing datasets
<a name="managing-datasets-in-the-amazon-cognito-console"></a>

If you have implemented Amazon Cognito Sync functionality in your application, the Amazon Cognito identity pools console enables you to manually create and delete datasets and records for individual identities. Any change you make to an identity's dataset or records in the Amazon Cognito identity pools console isn't saved until you select **Synchronize** in the console. The change isn't visible to the end user until the identity calls **Synchronize**. The data being synchronized from other devices for individual identities is visible once you refresh the list datasets page for a particular identity.

### Create a dataset for an identity
<a name="create-a-dataset-for-an-identity"></a>

Amazon Cognito Sync associates a dataset with one identity. You can populate your dataset with identifying information about the user that the identity represents, then sync that information to all of your user's devices.

**To add a dataset and dataset records to an identity**

1. Choose **Identity pools** from the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home). Select an identity pool.

1. Choose the **Identity browser** tab.

1. Select the identity that you want to edit.

1. In **Datasets**, choose **Create dataset**.

1. Enter a **Dataset name** and select **Create dataset**.

1. If you want to add records to your dataset, choose your dataset from identity details. In **Records**, select **Create record**.

1. Enter a **Key** and **Value** for your record. Choose **Confirm**. Repeat to add more records.

### Delete a dataset associated with an identity
<a name="delete-a-dataset-associated-with-an-identity"></a>

**To delete a dataset and its records from an identity**

1. Choose **Identity pools** from the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home). Select an identity pool.

1. Choose the **Identity browser** tab.

1. Select the identity that contains the dataset that you want to delete.

1. In **Datasets**, choose the radio button next to the dataset that you want to delete.

1. Select **Delete**. Review your choice and select **Delete** again.

## Bulk publish data
<a name="bulk-publish-data"></a>

 Bulk publish can be used to export data already stored in your Amazon Cognito Sync store to a Amazon Kinesis stream. For instructions on how to bulk publish all of your streams, see [Implementing Amazon Cognito Sync streams](cognito-streams.md). 

## Activate push synchronization
<a name="enable-push-synchronization"></a>

 Amazon Cognito automatically tracks the association between identity and devices. Using the push sync feature, you can make sure that every instance of a given identity is notified when identity data changes. Push sync makes it so that, whenever the dataset changes for an identity, all devices associated with that identity receive a silent push notification informing them of the change.

 You can activate push sync in the Amazon Cognito console. 

**To activate push synchronization**

1. Choose **Identity pools** from the [Amazon Cognito console](https://console.aws.amazon.com/cognito/home). Select an identity pool.

1. Choose the **Identity pool properties** tab.

1. In **Push synchronization**, select **Edit**

1. Select **Activate push synchronization with your identity pool**.

1. Choose one of the Amazon Simple Notification Service (Amazon SNS) **Platform applications** that you created in the current AWS Region. Amazon Cognito publishes push notifications to your platform application. Select **Create platform application** to navigate to the Amazon SNS console and create a new one.

1. To publish to your platform application, Amazon Cognito assumes an IAM role in your AWS account. Choose to **Create a new IAM role** if you want Amazon Cognito to create a new role for you with basic permissions and a trust relationship with your identity pool. Enter an **IAM role name** to identify your new role, for example `myidentitypool_authenticatedrole`. Select **View policy document** to review the permissions that Amazon Cognito assigns to your new IAM role.

1. You can choose to **Use an existing IAM role** if you already have a role in your AWS account that you want to use. You must configure your IAM role trust policy to include `cognito-identity.amazonaws.com`. Configure your role trust policy to only allow Amazon Cognito to assume the role when it presents evidence that the request originated from an authenticated user in your specific identity pool. For more information, see [Role trust and permissions](iam-roles.md#role-trust-and-permissions).

1. Select **Save changes**.

## Set up Amazon Cognito Streams
<a name="set-up-cognito-streams"></a>

 Amazon Cognito Streams gives developers control and insight into their data stored in Amazon Cognito Sync. Developers can now configure a Kinesis stream to receive events as data. Amazon Cognito can push each dataset change to a Kinesis stream you own in real time. For instructions on how to set up Amazon Cognito Streams in the Amazon Cognito console, see [Implementing Amazon Cognito Sync streams](cognito-streams.md). 

## Set up Amazon Cognito Events
<a name="set-up-cognito-events"></a>

 Amazon Cognito Events allows you to run an AWS Lambda function in response to important events in Amazon Cognito Sync. Amazon Cognito Sync raises the Sync Trigger event when a dataset is synchronized. You can use the Sync Trigger event to take an action when a user updates data. For instructions on setting up Amazon Cognito Events from the console, see [Customizing workflows with Amazon Cognito Events](cognito-events.md). 

 To learn more about AWS Lambda, see [AWS Lambda](https://aws.amazon.com/lambda/). 