# Managing a schedule group in EventBridge Scheduler

A _schedule group_ is an Amazon EventBridge Scheduler resource that you use to organize
your schedules.

Your AWS account comes with a `default` scheduler group. You can associate a
new schedule with the `default` group or with schedule groups that you create and
manage. You can create up to [500 schedule groups](scheduler-quotas.md "scheduler-quotas.md") in
your AWS account. With EventBridge Scheduler, you organize schedule groups, instead of individual
schedules, by applying [tags](../../../general/latest/gr/aws_tagging.md "../../../general/latest/gr/aws_tagging.md").

A _tag_ is a label comprised of a case-sensitive key and a
case-sensitive value that you define. You can create tags to categorize schedules by
criteria like purpose, owner, or environment. For example, you can identify the environment
that your schedules belong to with the following tag:
`environment:`production``.

###### Important

Do not add personally identifiable information (PII) or other confidential or sensitive information in tags. Tags are accessible to many AWS services, including billing.
Tags are not intended to be used for private or sensitive data.

A schedule group has two possible [states](../APIReference/API_GetScheduleGroup.md#scheduler-GetScheduleGroup-response-State "../APIReference/API_GetScheduleGroup.md#scheduler-GetScheduleGroup-response-State"): **ACTIVE** and **DELETING**.

When you first create a group, it is `ACTIVE` by default. You can add schedules
to an `ACTIVE` group. When you delete a group, the state changes to
`DELETING` until EventBridge Scheduler finishes the deletion of the associated schedules.
After EventBridge Scheduler deletes the schedules in the group, the group is no longer available in your
account.

Use the following topics to create a schedule group and apply a tag to it. You'll also
associate a schedule with the group. Finally, you'll delete the group.

###### Topics

- [Creating a schedule group in EventBridge Scheduler](managing-schedule-group-create.md "managing-schedule-group-create.md")
- [Deleting a schedule group in EventBridge Scheduler](managing-schedule-group-delete.md "managing-schedule-group-delete.md")
- [Related resources](#managing-schedule-group-related-resources "#managing-schedule-group-related-resources")

## Related resources

For more information on schedule groups, see the following resources:

- [CreateScheduleGroup](../APIReference/API_CreateScheduleGroup.md "../APIReference/API_CreateScheduleGroup.md") operation in the
  _EventBridge Scheduler API Reference_.
- [DeleteScheduleGroup](../APIReference/API_DeleteScheduleGroup.md "../APIReference/API_DeleteScheduleGroup.md") operation in the
  _EventBridge Scheduler API Reference_.
