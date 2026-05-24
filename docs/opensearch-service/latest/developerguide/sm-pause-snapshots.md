# Pausing automated snapshots

OpenSearch Service lets you temporarily pause automated snapshots on your domain. This is
useful when you need to perform data migrations, run maintenance operations, or
avoid snapshot overhead during peak traffic periods.

When you pause automated snapshots, OpenSearch Service stops taking hourly automated snapshots
for the duration you specify. You configure the pause by setting a start time and
end time in the `SnapshotOptions` of your domain configuration. The
pause operates on Unix epoch time with hourly granularity, and the maximum duration
cannot exceed 72 hours.

If you omit the start time, OpenSearch Service begins the pause immediately. To resume
snapshots before the scheduled end time, remove the pause parameters from your
domain configuration or set them to null.

###### Important

While automated snapshots are paused, your domain has reduced data
protection. You cannot restore to any point in time during the pause window.
Use this feature only for short-term operational needs.

To pause automated snapshots, include the following parameters when you update
your domain configuration:

```
POST https://es.`us-east-1`.amazonaws.com/2021-01-01/opensearch/domain/`my-domain`/config
{
  "SnapshotOptions": {
    "AutomatedSnapshotStartHour": 0,
    "PauseAutomatedSnapshotStartTime": 1737100800,
    "PauseAutomatedSnapshotEndTime": 1737360000
  }
}
```

`PauseAutomatedSnapshotStartTime` is optional. If you don't provide
it, the pause takes effect at the current time.
`PauseAutomatedSnapshotEndTime` specifies when OpenSearch Service resumes taking
automated snapshots.

After a pause expires, you must wait at least one hour before configuring a new
pause. This ensures that OpenSearch Service takes at least one snapshot between consecutive pause
windows, maintaining a minimum level of data protection.

You can extend an active pause as long as the total duration does not exceed 72
hours. If you attempt to set a pause longer than 72 hours, the request fails with
a validation error.

When snapshots are paused, the OpenSearch Service console displays a warning banner on the
domain details page indicating the pause end time and reduced data protection
status.
