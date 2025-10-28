# Creating a schedule group in EventBridge Scheduler

Use schedule groups and tagging to organize schedules that share a common purpose or
belong to the same environment. In the following steps, you create a new schedule group
and label it using a tag. You then associate a new schedule with that group.

###### Note

Once you create a group, you can't remove a schedule from that group, or associate the schedule with a different group.
You can only associate a schedule with a group when you first create the schedule.

## Step one: Create a new schedule group

The following topics describe how to create a new schedule group and label it with
the following tag: `environment:development`.

AWS Management Console

###### To create a new group using the AWS Management Console

1. Sign in to the AWS Management Console and open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the left navigation pane, choose **Schedule
   groups**.
3. On the Schedule groups page, choose **Create schedule
   group**.
4. In the **Schedule group detail** section, for
   **Name**, enter a name for the group. For
   example, `TestGroup`.
5. In the **Tags** section, do the
   following:
   1. Choose **Add new tag**.
   2. For **Key**, enter the name that you
      want to assign to this key. For this tutorial, to label
      the environment this schedule group belongs to, enter
      `environment`.
   3. For **Value -
      _optional_**, enter the
      value that you want to assign to this key. For this
      tutorial, enter the value
      `development` for your
      environment key.

   ###### Note

   You can add additional tags to your group after
   you create it.

6. To finish, choose **Create schedule group**.
   Your new group appears in the **Schedule
   groups** list.
7. (Optional) To edit a group or manage its tags, select the
   check box for the new group and choose
   **Edit**.

###### Note

You can't edit the `default` schedule
group.

AWS CLI

###### To create a new group using the AWS CLI

1. Open a new command prompt window.
2. From the AWS Command Line Interface (AWS CLI), enter the following [`create-schedule-group`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/scheduler/create-schedule-group.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/scheduler/create-schedule-group.html") command to
   create a new group. This command creates a group with one tag:
   `environment:development`. You can use this tag
   or a similar tagging system to label your schedule groups
   according to the environment they belong to.

Replace the schedule name and the tag key and value with your information.

```
`$` **aws scheduler create-schedule-group** `--name` `TestGroup` `--tags` Key=environment,Value=development
```

By default, your new group is in the `ACTIVE` state. You can now
associate new schedules with the new group you created.

## Step two: Associating a schedule with the group

Use the following steps to associate a new schedule with the group you created in
the [previous step](#create-schedule-group "#create-schedule-group").

AWS Management Console

###### To associate a schedule with a group using the AWS Management Console

1. Sign in to the AWS Management Console and open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the left navigation pane, choose
   **Schedules** in the left navigation pane.
3. From the **Schedules** table, choose
   **Create schedule** to create a new
   schedule.
4. On the **Specify schedule details** page, for
   **Schedule group**, select the name of your
   new group from the drop down list. For example, select
   `TestGroup`.
5. Specify a schedule pattern, target, settings then review your
   selection on the **Review and save schedule**
   page. For more information on configuring a new schedule, see
   [Getting started with EventBridge Scheduler](getting-started.md "getting-started.md").
6. To finish and save your schedule, choose **Save
   schedule**.

AWS CLI

###### To associate a schedule with a group using the AWS CLI

1. Open a new command prompt window.
2. From the AWS Command Line Interface (AWS CLI), enter the following [`create-schedule`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/scheduler/create-schedule.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/scheduler/create-schedule.html") command. This
   creates a schedule and associates it with the group from the
   [previous step](#create-schedule-group "#create-schedule-group"),
   named `sqs-test-schedule`. This schedule uses the
   templated [Amazon SQS](managing-targets-templated.md#managing-targets-templated-sqs "managing-targets-templated.md#managing-targets-templated-sqs") target type to invoke the
   `SendMessage` operation. Replace the schedule
   name, target, and group name with your information.

```
`$` `aws scheduler create-schedule --name `sqs-test-schedule` --schedule-expression 'rate(5 minutes)' \
--target '{"RoleArn": "`ROLE_ARN`", "Arn": "`QUEUE_ARN`", "Input": "`TEST_PAYLOAD`" }' \
**--group-name `TestGroup`**
--flexible-time-window '{ "Mode": "OFF"}'`
```

Your new schedule is now associated with the `TestGroup` schedule group.
