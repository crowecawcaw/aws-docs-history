# Troubleshooting Amazon EBS volume attachments to Amazon ECS

tasks

You might need to troubleshoot or verify the attachment of Amazon EBS volumes to Amazon ECS
tasks.

## Check volume attachment

status

You can use the AWS Management Console to view the status of an Amazon EBS volume's attachment to an
Amazon ECS task. If the task starts and the attachment fails, you'll also see a status reason
that you can use to troubleshoot. The created volume will be deleted and the task will
be stopped. For more information about status reasons, see [Status reasons for Amazon EBS volume attachment to Amazon ECS tasks](troubleshoot-ebs-volumes-scenarios.md "troubleshoot-ebs-volumes-scenarios.md").

###### To view a volume's attachment status and status reason using the console

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. On the **Clusters** page, choose the cluster that your task
   is running in. The cluster's details page appears.
3. On the cluster's details page, choose the **Tasks**
   tab.
4. Choose the task that you want to view the volume attachment status for. You
   might need to use **Filter desired status** and choose
   **Stopped** if the task you want to examine has
   stopped.
5. On the task's details page, choose the **Volumes** tab. You
   will be able to see the attachment status of the Amazon EBS volume under
   **Attachment status**. If the volume fails to attach to the
   task, you can choose the status under **Attachment status** to display the cause of the failure.

You can also view a task's volume attachment status and associated status reason by
using the [DescribeTasks](../APIReference/API_DescribeTasks.md "../APIReference/API_DescribeTasks.md")
API.

## Service and task failures

You might encounter service or task failures that aren't specific to Amazon EBS volumes
that can affect volume attachment. For more information, see

- [Service
  event messages](service-event-messages.md "service-event-messages.md")
- [Stopped
  task error codes](stopped-task-error-codes.md "stopped-task-error-codes.md")
- [API failure
  reasons](api_failures_messages.md "api_failures_messages.md")
