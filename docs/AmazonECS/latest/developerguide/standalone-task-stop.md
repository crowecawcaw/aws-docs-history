# Stopping an Amazon ECS task

If you no longer need to keep a standalone task running, you can stop the task. The
Amazon ECS console makes it easy to stop one or more tasks.

You can't restart a standalone stopped task.

If you want to stop a service, see [Deleting an Amazon ECS service using the console](delete-service-v2.md "delete-service-v2.md").

###### To stop a standalone task (AWS Management Console)

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. In the navigation pane, choose **Clusters**.
3. On the **Clusters** page, choose the cluster to navigate to
   the cluster details page.
4. On the cluster detail page, choose the **Tasks** tab.
5. You can filter tasks by launch type using the **Filter launch
   type** list.

| Tasks to stop | Steps                                                                                                                                                                                                                                                                                                                            |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| One or more   | 1. Select the tasks, and then choose **Stop**, **Stop selected**. 2. On the **Stop task confirmation page**, choose **Stop**                                                                                                                                                                                                     |
| All           | ImportantIf you choose to stop all tasks using the console, Amazon ECS stops all standalone tasks and tasks that are part of a service. Therefore, we recommend caution when using this option. 1. Choose **Stop**, **Stop all**. 2. On the **Stop task confirmation page**, enter **Stop all tasks**, and then choose **Stop**. |
