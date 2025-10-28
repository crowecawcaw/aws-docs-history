# Deleting prefetch schedules

The following procedure explains how to delete a prefetch schedule by using the MediaTailor
console. For information about how to delete prefetch schedules programmatically using the MediaTailor
API, see [DeletePrefetchSchedule](../apireference/API_DeletePrefetchSchedule.md "../apireference/API_DeletePrefetchSchedule.md") in the _AWS Elemental MediaTailor API Reference_.

###### Note

Deletion doesn't occur in real time. You might experience a delay while MediaTailor deletes the
prefetch schedule(s), during which time prefetch retrieval and consumption will continue to run
in the background.

###### To delete a prefetch schedule using the console

1. Open the MediaTailor console at [https://console.aws.amazon.com/mediatailor/](https://console.aws.amazon.com/mediatailor/ "https://console.aws.amazon.com/mediatailor/").
2. In the navigation pane, choose **Configurations**. Select the playback
   configuration that contains the prefetch schedule(s) that you want to delete.
3. On the **Prefetch schedules** tab, select the prefetch schedule that you
   want to delete. Then, choose **Delete**.
