AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Automating a manual Migration Hub Journeys task

###### Note

The task-automation feature is in preview release. It is available in
US East (N. Virginia).

This is pre-release documentation. Both the task-automation feature and this
documentation are subject to change.

To automate a task, first ensure that you have the following two
prerequisites.

## Prerequisites

- Ensure that you have an AWS account connection. For information
  about account connections and how to create them, see [AWS account connections in AWS Migration Hub Journeys](account-connections.md "account-connections.md").
- Associate with the account connection an IAM role with the
  permissions described in [IAM roles for Migration Hub Journeys task
  automation](task-automation-role.md "task-automation-role.md").

## To automate a task

1. Perform the steps described in [Updating Migration Hub Journeys tasks](updating-tasks.md "updating-tasks.md")
2. In the **Task details** section, choose
   **Edit**.
3. For **Task type** choose
   **Automated**.
4. Choose **Browse automation unit**.
5. Select an account connection with which you have associated the IAM
   role described in [Prerequisites](#automation-prereqs "#automation-prereqs").
6. Select the IAM role described in [Prerequisites](#automation-prereqs "#automation-prereqs").
7. Select the automation unit that you want the task to run when you
   execute the task.
8. Choose **Select**.
9. Choose **Save changes**.
