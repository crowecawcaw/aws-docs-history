

# Troubleshooting capacity task issues
<a name="order-troubleshooting"></a>

Review the following known issues to resolve an issue related to capacity management in a new order. If you do not see your issue listed, contact Support.

## Order {{oo-xxxxxx}} is not associated with Outpost ID {{op-xxxxx}}
<a name="troubleshooting_order_outpost_id"></a>

This issue occurs when you use the AWS CLI or API to run the [`StartCapacityTask`](https://docs.aws.amazon.com/outposts/latest/APIReference/API_StartCapacityTask.html) and the Outpost ID in the request does not match the Outpost ID in the order.

To resolve this issue:

1. Sign in to AWS.

1. Open the AWS Outposts console at [https://console.aws.amazon.com/outposts/](https://console.aws.amazon.com/outposts/home).

1. From the navigation pane, choose **Orders**.

1. Select the order and verify that the order status is one of the following: `PREPARING`, `IN_PROGRESS`, or `ACTIVE`.

1. Note the Outpost ID in the order.

1. Enter the correct Outpost ID in the `StartCapacityTask` API request.

## The capacity plan includes instance types that are not supported
<a name="troubleshooting_instance_type_unsupported"></a>

This issue occurs when you use the AWS CLI or API to create or modify the capacity task and the request contains unsupported instances types.

To resolve this issue, use the console or CLI.

**Use the console**

1. Sign in to AWS.

1. Open the AWS Outposts console at [https://console.aws.amazon.com/outposts/](https://console.aws.amazon.com/outposts/home).

1. From the navigation pane, choose **Capacity task**.

1. Use the **Upload a capacity configuration** option to upload a JSON with the same list of instance types.

1. The console displays an error message with the list of supported instance types.

1. Correct the request to remove the unsupported instance types.

1. Create or modify the capacity task on the console using the corrected JSON or use the CLI or API with this corrected list of instance types.

**Use the CLI**

1. Use the [GetOutpostSupportedInstanceTypes](https://docs.aws.amazon.com/cli/latest/reference/outposts/get-outpost-supported-instance-types.html) command to see the list of supported instance types.

1. Create or modify the capacity task with the correct list of instance types.

## No Outpost with Outpost ID {{op-xxxxx}}
<a name="troubleshooting_outpost_id_notfound"></a>

This issue occurs when you use the AWS CLI or API to run the [`StartCapacityTask`](https://docs.aws.amazon.com/outposts/latest/APIReference/API_StartCapacityTask.html) and the request contains an Outpost ID that is not valid for one of the following reasons:
+ The Outpost is in a different AWS Region.
+ You do not have permissions to this Outpost.
+ The Outpost ID is incorrect.

To resolve this issue:

1. Note the AWS Region that you used in the `StartCapacityTask` API request.

1. Use the [`ListOutposts`](https://docs.aws.amazon.com/outposts/latest/APIReference/API_ListOutposts.html) API action to get a list of Outposts that you own in the AWS Region.

1. Check if the Outpost ID is listed.

1. Enter the correct Outpost ID in the `StartCapacityTask` request.

1. If you do not find the Outpost ID, use the `ListOutposts` API action again to check if the Outpost exists in a different AWS Region.

## Active CapacityTask cap-{{XXXX}} already found for Outpost op-{{XXXX}}
<a name="troubleshooting_capacity_task_running"></a>

This issue occurs when you use the AWS Outposts console or API to run [StartCapacityTask](https://docs.aws.amazon.com/outposts/latest/APIReference/API_StartCapacityTask.html) on an Outpost and there is already a running capacity task for the Outpost. A capacity task is considered running if it has any of the following statuses: `REQUESTED`, `IN_PROGRESS`, `WAITING_FOR_EVACUATION`, or `CANCELLATION_IN_PROGRESS`.

To resolve this issue, use the AWS Outposts console or CLI.

**Use the console**

1. Sign in to AWS.

1. Open the AWS Outposts console at [https://console.aws.amazon.com/outposts/](https://console.aws.amazon.com/outposts/home).

1. From the navigation pane, choose **Capacity tasks**.

1. Ensure that there are no running capacity tasks for the OutpostId.

1. If there are running capacity tasks for the OutpostId, wait for them to terminate, or cancel them if desired.

1. When there no running capacity tasks for the requested OutpostId, retry your request to create the capacity task.

**Use the CLI**

1. Use the [ListCapacityTasks](https://docs.aws.amazon.com/outposts/latest/APIReference/API_ListCapacityTasks.html) command to find running capacity tasks for the Outpost.

1. Wait for all running capacity tasks to terminate, or cancel them if desired.

1. When there no running capacity tasks for the requested OutpostId, retry your request to create the capacity task.

## Active CapacityTask cap-{{XXXX}} already found for Asset {{XXXX}} on Outpost op-XXXX
<a name="troubleshooting_capacity_task_found_asset"></a>

This issue occurs when you use the AWS Outposts console or API to run [StartCapacityTask](https://docs.aws.amazon.com/outposts/latest/APIReference/API_StartCapacityTask.html) on an asset and there is already a running capacity task for the asset. A capacity task is considered running if it has any of the following statuses: `REQUESTED`, `IN_PROGRESS`, `WAITING_FOR_EVACUATION`, or `CANCELLATION_IN_PROGRESS`.

To resolve this issue, use the AWS Outposts console or CLI.

**Use the console**

1. Sign in to AWS.

1. Open the AWS Outposts console at [https://console.aws.amazon.com/outposts/](https://console.aws.amazon.com/outposts/home).

1. From the navigation pane, choose **Capacity tasks**.

1. Ensure that there are no running capacity tasks for the OutpostId and no running asset-level capacity Tasks for the AssetId.

1. If there are running capacity tasks, wait for them to terminate, or cancel them if desired.

1. When there no running capacity tasks, retry your request to create the capacity task.

**Use the CLI**

1. Use the [ListCapacityTasks](https://docs.aws.amazon.com/outposts/latest/APIReference/API_ListCapacityTasks.html) command to find running capacity tasks for the OutpostID and AssetID.

1. Ensure that there are no running Outpost-level capacity tasks for the OutpostId, and no running asset-level capacity Tasks for the AssetId.

1. If there are running capacity tasks, wait for them to terminate, or cancel them if desired.

1. Retry your request to create the capacity task.

## AssetId={{XXXX}} is not valid for Outpost=op-{{XXXX}}
<a name="troubleshooting_asset_id_not_valid"></a>

This issue occurs when you use the AWS Outposts console or API to run [StartCapacityTask](https://docs.aws.amazon.com/outposts/latest/APIReference/API_StartCapacityTask.html) on an asset and the AssetID is not valid for one of the following reasons:
+ The asset is not associated with the Outpost.
+ The asset is isolated.

To resolve this issue, use the AWS Outposts console or CLI.

**Use the console**

1. Sign in to AWS.

1. Open the AWS Outposts console at [https://console.aws.amazon.com/outposts/](https://console.aws.amazon.com/outposts/home).

1. Choose **Rack view** for the Outpost.

1. Verify that the requested AssetId is associated with the Outpost, and that it is not marked as an Isolated Host.

   1. If the Asset is isolated, this may be because a capacity task is running on it. You can navigate to the capacity tasks panel and check if there are any running Outpost or asset-level tasks for the OutpostId and AssetId. If there are, then wait for the task to terminate and for the asset to become available again.

   1. If there are no running capacity tasks for an isolated asset, then the asset may be degraded.

1. After you verify that the asset exists and is in a valid state, retry your request to create the capacity task.

**Use the CLI**

1. Use the [ListAssets](https://docs.aws.amazon.com/outposts/latest/APIReference/API_ListAssets.html) command to find the assets associated with the OutpostID.

1. Verify that the requested AssetId is associated with the Outpost, and that its State is `ACTIVE`.

   1. If the asset State is not ACTIVE, this may be because a capacity task is running on it. Use the [ListCapacityTasks](https://docs.aws.amazon.com/outposts/latest/APIReference/API_ListCapacityTasks.html) command to determine if there are running Outpost or asset-level tasks for the OutpostId and AssetId. If there are, then wait for the task to terminate and for the asset to become ACTIVE again.

   1. If there are no running capacity tasks for an isolated asset, then the asset may be degraded.

1. After you verify that the asset exists and is in a valid state, retry your request to create the capacity task.