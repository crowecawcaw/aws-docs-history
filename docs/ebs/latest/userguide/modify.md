# Modify Amazon Data Lifecycle Manager policies

Keep the following in mind when modifying Amazon Data Lifecycle Manager policies:

- If you modify an AMI or snapshot policy by removing its target tags, the volumes or
  instances with those tags are no longer managed by the policy.
- If you modify a schedule name, the snapshots or AMIs created under the old schedule
  name are no longer managed by the policy.
- If you modify an age-based retention schedule to use a new time interval, the new
  interval is used only for new snapshots or AMIs created after the change. The new
  schedule does not affect the retention schedule of snapshots or AMIs created before
  the change.
- You cannot change the retention schedule of a policy from count-based to age-based
  after creation. To make this change, you must create a new policy.
- If you disable a policy with an age-based retention schedule, the snapshots or AMIs
  that are set to expire while the policy is disabled are retained indefinitely. You must
  delete the snapshots or deregister the AMIs manually. When you re-enable the policy,
  Amazon Data Lifecycle Manager resumes deleting snapshots or deregistering AMIs as their retention periods
  expire.
- If you disable a policy with a count-based retention schedule, the policy stops
  creating and deleting snapshots or AMIs. When you re-enable the policy, Amazon Data Lifecycle Manager resumes
  creating snapshots and AMIs, and it resumes deleting snapshots or AMIs as the retention
  threshold is met.
- If you disable a policy that has a snapshot archiving-enabled policy, snapshots that are
  in the archive tier at the time of disabling the policy are no longer managed by Amazon Data Lifecycle Manager. You
  must manually delete the snapshot if they are no longer needed.
- If you enable snapshot archiving on a count-based schedule, the archiving rule applies
  to all new snapshots that are created and archived by the schedule, and also
  applies to existing snapshots that were previously created and archived by
  the schedule.
- If you enable snapshot archiving on an age-based schedule, the archiving rule applies
  only to new snapshots created after enabling snapshot archiving. Existing
  snapshots created before enabling snapshot archiving continue to be deleted
  from their respective storage tiers, according to the schedule set when
  those snapshots were originally created and archived.
- If you disable snapshot archiving for a count-based schedule, the schedule immediately stops
  archiving snapshots. Snapshots that were previously archived by the schedule remain in the archive
  tier and they will not be deleted by Amazon Data Lifecycle Manager.
- If you disable snapshot archiving for an age-based schedule, the snapshots created by the
  policy and that are scheduled to be archived are permanently deleted at the scheduled archive
  date and time, as indicated by the `aws:dlm:expirationTime` system tag.
- If you disable snapshot archiving for a schedule, the schedule immediately stops archiving
  snapshots. Snapshots that were previously archived by the schedule remain in the archive tier
  and they will not be deleted by Amazon Data Lifecycle Manager.
- If you modify the archive retention count for a count-based schedule, the new retention
  count includes existing snapshots that were previously archived by the schedule.
- If you modify the archive retention period for an age-based schedule, the new
  retention period applies only to snapshots that are archived after modifying
  the retention rule.
  Use one of the following procedures to modify a lifecycle policy.

Console

###### To modify a lifecycle policy

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Elastic Block Store**, **Lifecycle Manager**.
3. Select a lifecycle policy from the list.
4. Choose **Actions**, **Modify lifecycle policy**.
5. Modify the policy settings as needed. For example, you can modify the schedule, add or remove tags, or enable or disable
   the policy.
6. Choose **Modify policy**.

Command line
Use the [update-lifecycle-policy](../../../cli/latest/reference/dlm/update-lifecycle-policy.md "../../../cli/latest/reference/dlm/update-lifecycle-policy.md") command to modify the information in a lifecycle policy.
To simplify the syntax, this example references a JSON file,
`policyDetailsUpdated.json`, that includes the policy details.

```
`aws dlm update-lifecycle-policy \
 --state DISABLED \
 --execution-role-arn arn:aws:iam::`12345678910`:role/`AWSDataLifecycleManagerDefaultRole`" \
 --policy-details file://`policyDetailsUpdated.json``
```

The following is an example of the `policyDetailsUpdated.json`
file.

```
{
   "ResourceTypes":[
      "`VOLUME`"
   ],
   "TargetTags":[
      {
         "Key": "`costcenter`",
         "Value": "`120`"
      }
   ],
   "Schedules":[
      {
         "Name": "`DailySnapshots`",
         "TagsToAdd": [
            {
               "Key": "`type`",
               "Value": "`myDailySnapshot`"
            }
         ],
         "CreateRule": {
            "Interval": `12`,
            "IntervalUnit": "HOURS",
            "Times": [
               "`15:00`"
            ]
         },
         "RetainRule": {
            "Count" :`5`
         },
         "CopyTags": false
      }
   ]
}
```

To view the updated policy, use the `get-lifecycle-policy` command. You can
see that the state, the value of the tag, the snapshot interval, and the snapshot start time
were changed.
