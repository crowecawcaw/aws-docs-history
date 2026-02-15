# Modify AWS Outposts instance capacity

The capacity of each new Outpost order is configured with a default capacity
configuration. You can convert the default configuration to create various instances to meet
your business needs. To do so, you create a capacity task, choose an Outposts or a single
asset, specify the instance sizes and quantity, and run the capacity task to implement the
changes.

## Considerations

Consider the following before modifying instance capacity:

- Capacity tasks can be run only by the AWS account that owns the Outpost resources
  (owner). Consumers cannot run capacity tasks. For more information about owners and
  consumers, see [Share your AWS Outposts
  resources](../userguide/sharing-outposts.md "../userguide/sharing-outposts.md").
- Instances sizes and quantities can be defined at the Outpost level or at an
  individual asset level.
- Capacity is configured automatically across an asset or all the assets in an Outpost
  based on possible configurations and best practices.
- While a capacity task is running, the assets associated with the selected outpost
  may be isolated. For this reason we recommend creating a capacity task only when you
  don't expect to launch new instances on your Outposts.
- You can choose to run the capacity task instantly or to keep attempting periodically
  over the next 48 hours. Choosing to run instantly requires less asset isolation time,
  but the task might fail if instances need to be stopped to run the task. Choosing to run
  periodically allows more time to stop instances before the task would fail, but assets
  may be isolated for longer.
- It is possible for valid capacity configurations to not utilize all of the available
  vCPU on an asset. When this is the case, a message at the end of the **Instance
  type** section will inform you that you are under capacity, but will allow
  the configuration to be applied as requested.
- When you modify an Outpost in the console, not all supported instances are shown
  because mixing disk-backed instances with non-disk-backed instances is not fully
  supported in console. To access all possible instances, utilize the [StartCapacityTask](../APIReference/API_StartCapacityTask.md "../APIReference/API_StartCapacityTask.md") API.
- You can only modify your existing Outposts capacity configuration to use valid Amazon EC2
  instance sizes from instance families supported on your respective asset model.
- If you have instances running on your Outpost that you do not want to stop to run a
  capacity task, select their respective Instance ID under the section **Instances
  to keep as-is – _optional_** and make sure to retain the
  necessary quantity of this instance size in your updated capacity configuration. This
  will retain instances being used to support production workloads while a capacity task
  runs.
- When configuring an asset with multiple instance sizes within an instance family,
  use **Auto-balance** to make sure you aren’t attempting to over or
  under-provision your droplet. Over-provisioning is not supported, and will cause a
  capacity task failure.
- Several capacity tasks can run in parallel as long as they apply to mutually
  exclusive sets of AssetIDs. For example, you can create several asset-level capacity
  tasks for different AssetIDs at the same time. However, if there is a running
  Outpost-level task, you cannot create another Outpost or asset-level task at the same
  time. Similarly, if there is a running asset-level task, you cannot create an
  Outpost-level task or an asset-level task on the same AssetID at the same time.

###### To modify capacity configuration for your Outpost using the console

1. Open the AWS Outposts console at [https://console.aws.amazon.com/outposts/](https://console.aws.amazon.com/outposts/home "https://console.aws.amazon.com/outposts/home").
2. From the left navigation pane, choose **Capacity tasks**.
3. On the **Capacity tasks** page, choose **Create capacity
   task**.
4. On the **Getting started** page, choose the order, Outpost, or asset
   to configure.
5. To modify capacity, specify an option for **Method of modification**:
   e steps in the console or upload a JSON file.
   - **Modify capacity configuration plan** to use the steps in the
     console
   - **Upload a capacity configuration plan** to upload a JSON
     file

###### Note

- To prevent capacity management from recommending specific instances to stop, specify
  the instances that should not be stopped. These instances will be excluded from the list
  of instances to stop.

Console steps

1. Choose **Instance view** or **Rack
   view**.
2. Choose **Modify an Outpost capacity configuration** or
   **Modify** on a single asset.
3. Choose an Outpost or asset if different than the current selection.
4. Choose to either run this capacity task immediately or periodically over 48
   hours.
5. Choose **Next**.
6. On the **Configure instance capacity** page, each instance type
   shows one instance size with the maximum quantity preselected. To add more instance
   sizes, choose **Add instance size**.
7. Specify the instance quantity and note the capacity that is displayed for that
   instance size.
8. View the message at the end of each instance-type section that informs you if
   you are over or under capacity. Make adjustments at the instance size or quantity
   level to optimize your total available capacity.
9. You can also request AWS Outposts to optimize the instance quantity for a specific
   instance size. To do so:
   1. Choose the instance size.
   2. Choose **Auto-balance** at the end of the related
      instance-type section.

10. For each instance type, ensure that the instance quantity is specified for at
    least one instance size.
11. Optionally, choose instances to keep as-is.
12. Choose **Next**.
13. On the **Review and create** page, verify the updates that you
    are requesting.
14. Choose **Create**. AWS Outposts creates a capacity task.
15. On the capacity task page, monitor the status of the task.

Upload a JSON file

1. Choose **Upload a capacity configuration**.
2. Choose **Next**.
3. On the **Upload capacity configuration plan** page, upload the
   JSON file that specifies the instance type, size, and quantity. Optionally, you can
   specify the [InstancesToExclude](../APIReference/API_StartCapacityTask.md#outposts-StartCapacityTask-request-InstancesToExclude "../APIReference/API_StartCapacityTask.md#outposts-StartCapacityTask-request-InstancesToExclude"), and [TaskActionOnBlockingInstances](../APIReference/API_StartCapacityTask.md#outposts-StartCapacityTask-response-TaskActionOnBlockingInstances "../APIReference/API_StartCapacityTask.md#outposts-StartCapacityTask-response-TaskActionOnBlockingInstances") parameters in the JSON file.

###### Example

Example JSON file:

```
{
  "InstancePools": [
    {
      "InstanceType": "c5.24xlarge",
      "Count": 1
    },
    {
      "InstanceType": "m5.24xlarge",
      "Count": 2
    }
  ],
  "InstancesToExclude": {
    "AccountIds": [
      "111122223333"
    ],
    "Instances": [
      "i-1234567890abcdef0"
    ],
    "Services": [
      "ALB"
    ]
  },
  "TaskActionOnBlockingInstances": "WAIT_FOR_EVACUATION"
}
```

4. Review the contents of the JSON file in the **Capacity configuration
   plan** section.
5. Choose **Next**.
6. On the **Review and create** page, verify the updates that you
   are requesting.
7. Choose **Create**. AWS Outposts creates a capacity task.
8. On the capacity task page, monitor the status of the task.
