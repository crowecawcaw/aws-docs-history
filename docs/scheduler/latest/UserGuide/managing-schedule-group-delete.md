# Deleting a schedule group in EventBridge Scheduler

In the following, you can learn how to delete a schedule group using the AWS Management Console and
the AWS Command Line Interface. When you delete a group, it is in the `DELETING` state until
EventBridge Scheduler deletes all schedules in the group. After EventBridge Scheduler deletes the schedules in the
group, the group is no longer available in your account.

###### Note

Once you create a group, you can't remove a schedule from that group, or associate the schedule with a different group.
You can only associate a schedule with a group when you first create the schedule.

AWS Management Console

###### To delete a group using the AWS Management Console

1. Sign in to the AWS Management Console and open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the left navigation pane, choose **Schedule
   groups** in the left navigation pane.
3. On the **Schedule groups** page, from the list of
   existing groups in the current AWS Region, locate the group you
   want to delete. If you don't see the group you're looking for,
   choose another AWS Region.

###### Note

You can't delete, or edit, the **default**
group. 4. Select the check box for the group that you want to delete. 5. Choose **Delete**. 6. In the **Delete schedule group** dialog box,
enter the name of the group to confirm your choice, then choose
**Delete**. 7. In the **Schedule groups** list, the
**Status** column changes to indicate that your
group is now **Deleting**. The group remains in
this state until EventBridge Scheduler deletes all of the schedules associated with
the group. 8. To refresh the list and confirm that the group was deleted, choose
the **Refresh** icon.

AWS CLI

###### To delete a group using the AWS CLI

1. Open a new command prompt window.
2. From the AWS Command Line Interface (AWS CLI), enter the following[`delete-schedule-group`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/scheduler/delete-schedule-group.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/scheduler/delete-schedule-group.html") command to
   delete the schedule group. Replace the value for `--name`
   with your information.

```
`$` **aws scheduler delete-schedule-group** `--name` `TestGroup`
```

If successful, this AWS CLI operation doesn't return a response. 3. To verify that the group is in the `DELETING` state,
run the following [`get-schedule-group`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/scheduler/get-schedule-group.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/scheduler/get-schedule-group.html") command.

```
`$` **aws scheduler get-schedule-group** `--name` `TestGroup`
```

If successful, you receive output similar to the following:

```
{
    "Arn": "arn:aws::scheduler:us-west-2:123456789012:schedule-group/TestGroup",
    "CreationDate": "2023-01-01T09:00:00.000000-07:00",
    "LastModificationDate": "2023-01-01T09:00:00.000000-07:00",
    "Name": "**TestGroup**",
    "State": "**DELETING**"
}
```

EventBridge Scheduler deletes the group after it deletes the schedules associated
with the group. If you run `get-schedule-group` again,
you receive following `ResourceNotFoundException`
response:

```
An error occurred (ResourceNotFoundException) when calling the GetScheduleGroup operation: Schedule group **TestGroup** does not exist.
```
